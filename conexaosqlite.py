from sqlite3 import Error
import sqlite3 

class Banco:
    def __init__(self):
        pass

    def cursorBD(self):
        try:
            cursor = self.conexaoBD().cursor()
            return cursor
        except Error as e:
            print("Erro de Conexão com o banco", e)
    
    def conexaoBD(self):
        try:
            self.conexao = sqlite3.connect(r'C:\Users\givij\Projetos\Projetos-Individuais\Programacao\Pokedex\pokemons.db')
            return self.conexao
        except Error as e:
            print("Erro de Conexão com o banco", e)
        
conectar = Banco()


