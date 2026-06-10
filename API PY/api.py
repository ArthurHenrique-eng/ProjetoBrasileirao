from flask import Flask, jsonify, request, abort
from conectar.funcaoConectar import conectar

app = Flask(__name__)



@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "api": "Campeonato Brasileiro",
        "rotas": ["/Serie_A", "/Serie_B", "/Serie_C", "/Serie_D"]
    })

# ==================================================
# ROTAS PARA A TABELA SERIE A
# ==================================================

@app.route("/Serie_A", methods=["GET"])
def listar_serie_a():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serie_A")
    dados = [
        {"idSerieA": row[0], "NomeClube": row[1], "PontosClube": row[2], "PosicaoClube": row[3],
         "JogosClube": row[4], "VitoriasClube": row[5], "EmpatesClube": row[6], "DerrotasClube": row[7],
         "GolsProClube": row[8], "GolsContraClube": row[9], "SaldoGolsClube": row[10]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(dados)


@app.route("/Serie_A", methods=["POST"])
def criar_clube_serie_a():
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    campos_obrigatorios = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                           "VitoriasClube", "EmpatesClube", "DerrotasClube",
                           "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    if not campos_obrigatorios.issubset(dados.keys()):
        abort(400, description=f"Campos obrigatórios: {', '.join(campos_obrigatorios)}")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Serie_A (NomeClube, PontosClube, PosicaoClube, JogosClube, VitoriasClube, "
        "EmpatesClube, DerrotasClube, GolsProClube, GolsContraClube, SaldoGolsClube) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (dados["NomeClube"], dados["PontosClube"], dados["PosicaoClube"], dados["JogosClube"],
         dados["VitoriasClube"], dados["EmpatesClube"], dados["DerrotasClube"],
         dados["GolsProClube"], dados["GolsContraClube"], dados["SaldoGolsClube"])
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    resposta = jsonify({"idSerieA": novo_id, **dados})
    resposta.status_code = 201
    resposta.headers["Location"] = f"/Serie_A/{novo_id}"
    return resposta


@app.route("/Serie_A/<int:id_serie_a>", methods=["PUT", "PATCH"])
def atualizar_clube_serie_a(id_serie_a):
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    if request.method == "PUT":
        campos_esperados = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                            "VitoriasClube", "EmpatesClube", "DerrotasClube",
                            "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
        if not campos_esperados.issubset(dados.keys()):
            abort(400, description=f"PUT requer todos os campos: {', '.join(campos_esperados)}")

    campos_validos = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                      "VitoriasClube", "EmpatesClube", "DerrotasClube",
                      "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    set_clauses = []
    valores = []
    for campo in campos_validos & dados.keys():
        set_clauses.append(f"{campo} = ?")
        valores.append(dados[campo])

    if not set_clauses:
        abort(400, description="Nenhum campo válido para atualizar")

    valores.append(id_serie_a)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Serie_A SET {', '.join(set_clauses)} WHERE idSerieA = ?", tuple(valores))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


@app.route("/Serie_A/<int:id_serie_a>", methods=["DELETE"])
def deletar_clube_serie_a(id_serie_a):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Serie_A WHERE idSerieA = ?", (id_serie_a,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


# ==================================================
# ROTAS PARA A TABELA SERIE B
# ==================================================

@app.route("/Serie_B", methods=["GET"])
def listar_serie_b():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serie_B")
    dados = [
        {"idSerieB": row[0], "NomeClube": row[1], "PontosClube": row[2], "PosicaoClube": row[3],
         "JogosClube": row[4], "VitoriasClube": row[5], "EmpatesClube": row[6], "DerrotasClube": row[7],
         "GolsProClube": row[8], "GolsContraClube": row[9], "SaldoGolsClube": row[10]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(dados)


@app.route("/Serie_B", methods=["POST"])
def criar_clube_serie_b():
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    campos_obrigatorios = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                           "VitoriasClube", "EmpatesClube", "DerrotasClube",
                           "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    if not campos_obrigatorios.issubset(dados.keys()):
        abort(400, description=f"Campos obrigatórios: {', '.join(campos_obrigatorios)}")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Serie_B (NomeClube, PontosClube, PosicaoClube, JogosClube, VitoriasClube, "
        "EmpatesClube, DerrotasClube, GolsProClube, GolsContraClube, SaldoGolsClube) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (dados["NomeClube"], dados["PontosClube"], dados["PosicaoClube"], dados["JogosClube"],
         dados["VitoriasClube"], dados["EmpatesClube"], dados["DerrotasClube"],
         dados["GolsProClube"], dados["GolsContraClube"], dados["SaldoGolsClube"])
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    resposta = jsonify({"idSerieB": novo_id, **dados})
    resposta.status_code = 201
    resposta.headers["Location"] = f"/Serie_B/{novo_id}"
    return resposta


@app.route("/Serie_B/<int:id_serie_b>", methods=["PUT", "PATCH"])
def atualizar_clube_serie_b(id_serie_b):
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    if request.method == "PUT":
        campos_esperados = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                            "VitoriasClube", "EmpatesClube", "DerrotasClube",
                            "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
        if not campos_esperados.issubset(dados.keys()):
            abort(400, description=f"PUT requer todos os campos: {', '.join(campos_esperados)}")

    campos_validos = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                      "VitoriasClube", "EmpatesClube", "DerrotasClube",
                      "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    set_clauses = []
    valores = []
    for campo in campos_validos & dados.keys():
        set_clauses.append(f"{campo} = ?")
        valores.append(dados[campo])

    if not set_clauses:
        abort(400, description="Nenhum campo válido para atualizar")

    valores.append(id_serie_b)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Serie_B SET {', '.join(set_clauses)} WHERE idSerieB = ?", tuple(valores))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


@app.route("/Serie_B/<int:id_serie_b>", methods=["DELETE"])
def deletar_clube_serie_b(id_serie_b):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Serie_B WHERE idSerieB = ?", (id_serie_b,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


# ==================================================
# ROTAS PARA A TABELA SERIE C
# ==================================================

@app.route("/Serie_C", methods=["GET"])
def listar_serie_c():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serie_C")
    dados = [
        {"idSerieC": row[0], "NomeClube": row[1], "PontosClube": row[2], "PosicaoClube": row[3],
         "JogosClube": row[4], "VitoriasClube": row[5], "EmpatesClube": row[6], "DerrotasClube": row[7],
         "GolsProClube": row[8], "GolsContraClube": row[9], "SaldoGolsClube": row[10]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(dados)


@app.route("/Serie_C", methods=["POST"])
def criar_clube_serie_c():
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    campos_obrigatorios = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                           "VitoriasClube", "EmpatesClube", "DerrotasClube",
                           "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    if not campos_obrigatorios.issubset(dados.keys()):
        abort(400, description=f"Campos obrigatórios: {', '.join(campos_obrigatorios)}")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Serie_C (NomeClube, PontosClube, PosicaoClube, JogosClube, VitoriasClube, "
        "EmpatesClube, DerrotasClube, GolsProClube, GolsContraClube, SaldoGolsClube) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (dados["NomeClube"], dados["PontosClube"], dados["PosicaoClube"], dados["JogosClube"],
         dados["VitoriasClube"], dados["EmpatesClube"], dados["DerrotasClube"],
         dados["GolsProClube"], dados["GolsContraClube"], dados["SaldoGolsClube"])
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    resposta = jsonify({"idSerieC": novo_id, **dados})
    resposta.status_code = 201
    resposta.headers["Location"] = f"/Serie_C/{novo_id}"
    return resposta


@app.route("/Serie_C/<int:id_serie_c>", methods=["PUT", "PATCH"])
def atualizar_clube_serie_c(id_serie_c):
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    if request.method == "PUT":
        campos_esperados = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                            "VitoriasClube", "EmpatesClube", "DerrotasClube",
                            "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
        if not campos_esperados.issubset(dados.keys()):
            abort(400, description=f"PUT requer todos os campos: {', '.join(campos_esperados)}")

    campos_validos = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                      "VitoriasClube", "EmpatesClube", "DerrotasClube",
                      "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    set_clauses = []
    valores = []
    for campo in campos_validos & dados.keys():
        set_clauses.append(f"{campo} = ?")
        valores.append(dados[campo])

    if not set_clauses:
        abort(400, description="Nenhum campo válido para atualizar")

    valores.append(id_serie_c)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Serie_C SET {', '.join(set_clauses)} WHERE idSerieC = ?", tuple(valores))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


@app.route("/Serie_C/<int:id_serie_c>", methods=["DELETE"])
def deletar_clube_serie_c(id_serie_c):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Serie_C WHERE idSerieC = ?", (id_serie_c,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


# ==================================================
# ROTAS PARA A TABELA SERIE D
# ==================================================

@app.route("/Serie_D", methods=["GET"])
def listar_serie_d():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serie_D")
    dados = [
        {"idSerieD": row[0], "NomeClube": row[1], "PontosClube": row[2], "PosicaoClube": row[3],
         "JogosClube": row[4], "VitoriasClube": row[5], "EmpatesClube": row[6], "DerrotasClube": row[7],
         "GolsProClube": row[8], "GolsContraClube": row[9], "SaldoGolsClube": row[10]}
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify(dados)


@app.route("/Serie_D", methods=["POST"])
def criar_clube_serie_d():
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    campos_obrigatorios = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                           "VitoriasClube", "EmpatesClube", "DerrotasClube",
                           "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    if not campos_obrigatorios.issubset(dados.keys()):
        abort(400, description=f"Campos obrigatórios: {', '.join(campos_obrigatorios)}")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Serie_D (NomeClube, PontosClube, PosicaoClube, JogosClube, VitoriasClube, "
        "EmpatesClube, DerrotasClube, GolsProClube, GolsContraClube, SaldoGolsClube) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (dados["NomeClube"], dados["PontosClube"], dados["PosicaoClube"], dados["JogosClube"],
         dados["VitoriasClube"], dados["EmpatesClube"], dados["DerrotasClube"],
         dados["GolsProClube"], dados["GolsContraClube"], dados["SaldoGolsClube"])
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    resposta = jsonify({"idSerieD": novo_id, **dados})
    resposta.status_code = 201
    resposta.headers["Location"] = f"/Serie_D/{novo_id}"
    return resposta


@app.route("/Serie_D/<int:id_serie_d>", methods=["PUT", "PATCH"])
def atualizar_clube_serie_d(id_serie_d):
    dados = request.get_json(silent=True)
    if not dados:
        abort(400, description="JSON inválido ou ausente")

    if request.method == "PUT":
        campos_esperados = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                            "VitoriasClube", "EmpatesClube", "DerrotasClube",
                            "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
        if not campos_esperados.issubset(dados.keys()):
            abort(400, description=f"PUT requer todos os campos: {', '.join(campos_esperados)}")

    campos_validos = {"NomeClube", "PontosClube", "PosicaoClube", "JogosClube",
                      "VitoriasClube", "EmpatesClube", "DerrotasClube",
                      "GolsProClube", "GolsContraClube", "SaldoGolsClube"}
    set_clauses = []
    valores = []
    for campo in campos_validos & dados.keys():
        set_clauses.append(f"{campo} = ?")
        valores.append(dados[campo])

    if not set_clauses:
        abort(400, description="Nenhum campo válido para atualizar")

    valores.append(id_serie_d)
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE Serie_D SET {', '.join(set_clauses)} WHERE idSerieD = ?", tuple(valores))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


@app.route("/Serie_D/<int:id_serie_d>", methods=["DELETE"])
def deletar_clube_serie_d(id_serie_d):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Serie_D WHERE idSerieD = ?", (id_serie_d,))
    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        abort(404, description="Clube não encontrado")

    conn.close()
    return ("", 204)


if __name__ == "__main__":
    app.run(debug=True)