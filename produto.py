import json 
from operacoes_estoque import vender_produto, adicionar_produto 

class Produto:
    __arquivo = "produto.json"

    def __init__(self, id, nome, preco, quantidade):
        self.__id = id
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @classmethod
    def cadastrar(cls):
        print("Informe os dados do produto:")
        id = input("ID: ")
        nome = input("Nome: ") 
        
        try:
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
        except ValueError:
            print("❌\033[31m  Preço ou Quantidade inválida. Por favor, insira números válidos.\033[0m")
            
            input("Pressione Enter para continuar...")
            return

        produto = {
            "id": id,
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
       
        with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
            a = json.load(arquivo)
        
        with open(cls.__arquivo, "w", encoding="utf-8") as arquivo:
            a.append(produto) 
            json.dump(a, arquivo, indent=4) 
            print("✅\033[32m  Produto cadastrado com sucesso!\033[0m")

        input("Pressione Enter para continuar...")

    @classmethod
    def listar(cls):
        with open(cls.__arquivo, "r", encoding="utf-8") as arquivo:
            produtos = json.load(arquivo)
            
        print("\033[34mOs produtos do estoque são:\033[0m")
        for produto in produtos:
            print(f"\033[34mID:\033[0m {produto['id']}, \033[34mNome:\033[0m {produto['nome']}, \033[34mPreço:\033[0m {produto['preco']}, \033[34mQuantidade:\033[0m {produto['quantidade']}")
        if not produtos:
            print("Nenhum produto cadastrado.")

        input("Pressione Enter para continuar...")

    @classmethod
    def adicionar(cls):
        adicionar_produto(cls)
        
    @classmethod
    def vender(cls): 
        vender_produto(cls)