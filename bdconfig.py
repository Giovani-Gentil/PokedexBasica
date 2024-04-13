
import requests
import conexaosqlite

class ConfigsBD:
    def __init__(self, ajustarLimiteDados:int):
        self.limite = ajustarLimiteDados
        try:
            self.conn = conexaosqlite.conectar.conexaoBD()
            self.cursor = self.conn.cursor()
            self.pokemons = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit={self.limite}&offset=0')
            
        except requests.exceptions.RequestException as e:
            print("Erro de conexão com API", e)
        except Exception as e:
            print("Erro inesperado", e)
    
    def procedimentoDropCreate(self):
        try:
            self.cursor.execute("DROP TABLE MEUS")
            self.cursor.execute("DROP TABLE TODOS")
            self.cursor.execute("CREATE TABLE TODOS ( ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NOME TEXT(40));")
            self.cursor.execute("CREATE TABLE MEUS ( ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NOME TEXT(40));") 
        except Exception as e:
            print("Erro inesperado", e)

    def verificaLimite(self):
        try:
            dados = self.cursor.execute("SELECT COUNT(*) FROM TODOS;")
            if self.limite != dados:
                self.procedimentoDropCreate()
        except Exception as e:
            print("Erro inesperado", e)

    def inserirTodosResetar(self):
        try:
            self.verificaLimite()
            for c in range(0, self.limite):
                pokemon = self.pokemons.json()["results"][c]["name"]
                print(c + 1, pokemon, "INSERIDO...")
                self.cursor.execute(f'INSERT INTO TODOS (NOME) VALUES ("{pokemon}");')
                self.conn.commit()
            print("INSERÇÃO COMPLETA")
        
        except requests.exceptions.RequestException as e:
            print("Erro de conexão com API", e)
        except Exception as e:
            print("Erro inesperado", e)
            
if __name__ == "__main__":
    bdConfig = ConfigsBD(12)
    bdConfig.inserirTodosResetar()
    
