import sqlite3

def conectar():
    return sqlite3.connect("./BancoDados/campeonato_brasileiro_2026.db")