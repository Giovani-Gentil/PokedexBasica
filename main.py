import conexaosqlite
import json


class Pokedex:
    def __init__(self):
        self.conn = conexaosqlite.conectar.conexaoBD()
        self.cursor = conexaosqlite.conectar.cursorBD()
        self.listaTodos = []
        self.listaMeus = []

    def listaCompletaPokemons(self):
        try:
            a = self.cursor.execute('SELECT NOME FROM TODOS')
            show = a.fetchall()
            
            for index in range(0, len(show)):
                self.listaTodos.append(show[index][0])

            for item in self.listaTodos:
                print(item)

        except:
            print("ERRO")
        finally:
            self.cursor.close()
            self.conn.close()

    def listaMeusPokemons(self):
        try:
            query = self.cursor.execute('SELECT NOME FROM MEUS')
            show = query.fetchall()
            
            for index in range(0, len(show)):
                self.listaMeus.append(show[index][0])

            for item in self.listaMeus:
                print(item)

        except:
            print("ERRO")
        finally:
            self.cursor.close()
            self.conn.close()

    def transferenciaPokemon(self):
        pass

    def menuOptions(self):
        while True:
            print('---------------Escolha uma ação:-----------------')
            print('[1] Ver todos os pokemons')
            print('[2] Ver meus pokemons')
            decisao = input('Decisão: ')
            print('-------------------------------------')
            match decisao:
                case '1':
                    self.listaCompletaPokemons()
                case '2':
                    self.listaMeusPokemons()
                case _:
                    pass
            while True:
                continuar = input('Deseja continuar?(Y/n):').upper()          
                if continuar == '' or continuar == ' ' or continuar == 'y':
                    pass
                    
                
                    


if __name__ == "__main__":
    pk = Pokedex()
    pk.menuOptions()
    
    