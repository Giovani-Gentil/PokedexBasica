import sqlite3
from sqlite3 import Error


class Pokedex:
    def __init__(self):
        try:
            self.conexao = sqlite3.connect(r'C:\Users\givij\Projetos\Projetos-Individuais\Programacao\Pokedex\pokemons.db')
            self.cursor = self.conexao.cursor()
        except Error as e:
            print("Erro de Conexão com o banco", e)


    def listaCompletaPokemons(self):
        try:
            a = self.cursor.execute('SELECT NOME FROM TODOS')
            show = a.fetchall()
            
            for index in range(0, len(show)):
                print(f'{index + 1} - {show[index][0]}')

        except:
            print("ERRO")


    def listaMeusPokemons(self):
        try:
            query = self.cursor.execute('SELECT NOME FROM MEUS')
            show = query.fetchall()
            
            for index in range(0, len(show)):
                print(f'{index + 1} - {show[index][0]}')

        except:
            print("ERRO")

    def transferenciaPokemon(self):
        while True:
            nomePokemon = str(input('Escolha um pokemon: ')).lower()
            try:
                a = self.cursor.execute(f'SELECT NOME FROM TODOS WHERE NOME = "{nomePokemon}";')
                show = a.fetchone()

                if nomePokemon == show[0]:
                    self.cursor.execute(f'INSERT INTO MEUS (NOME) VALUES ("{nomePokemon}");')
                    self.cursor.execute(f"DELETE FROM TODOS WHERE NOME ='{nomePokemon}';")
                    self.conexao.commit()
                    break
            except:
                print('O pokemon escolhido não existe')
        
    def excluirPokemon(self):
        while True:
            nomePokemon = str(input('Escolha um pokemon: ')).lower() 
            try:
                a = self.cursor.execute(f'SELECT NOME FROM MEUS WHERE NOME = "{nomePokemon}";')
                show = a.fetchone()

                if nomePokemon == show[0]:
                    self.cursor.execute(f'INSERT INTO TODOS (NOME) VALUES ("{nomePokemon}");')
                    self.cursor.execute(f"DELETE FROM MEUS WHERE NOME='{nomePokemon}';")
                    self.conexao.commit()
                    break
            except:
                print('Você não tem esse pokemon')

    def menuOptions(self):
        while True:
            print('---------------Escolha uma ação:-----------------')
            print('[1] Ver todos os pokemons')
            print('[2] Ver meus pokemons')
            print('[3] Escolher pokemons')
            print('[4] Excluir pokemons')


            decisao = input('Decisão: ')
            print('-------------------------------------')
            match decisao:
                case '1':
                    self.listaCompletaPokemons()

                case '2':
                    self.listaMeusPokemons()

                case '3':
                    self.transferenciaPokemon()

                case '4':
                    self.excluirPokemon()

                case _:
                    pass

            continuar = ''
            while True:
                continuar = input('Deseja continuar?(Y/n): ')
                if continuar == 'Y' or continuar == '' or continuar == 'y' or continuar == 'n' or continuar == 'N':
                    break
                else:
                    continue

            if continuar == 'n' or continuar == 'N':
                self.cursor.close()
                self.conexao.close()
                break      
            
            
if __name__ == "__main__":
    pk = Pokedex()
    pk.menuOptions()
    
    