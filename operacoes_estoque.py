import json

def adicionar_produto(cls):
    """ Realiza a entrada (adição) de quantidade em um produto existente. """
    print("Informe os dados para entrada de produto:")
    id_produto = input("ID do produto: ")
    
    try:
        quantidade_entrada = int(input("Quantidade a adicionar: "))
        if quantidade_entrada <= 0:
            print("❌\033[31m  A quantidade adicionada deve ser um número positivo.\033[0m")
            input("Pressione Enter para continuar...")
            return
    except ValueError:
        print("❌\033[31m  Quantidade inválida. Por favor, insira um número inteiro.\033[0m")
        input("Pressione Enter para continuar...")
        return

    arquivo_path = cls._Produto__arquivo

    with open(arquivo_path, "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    produto_encontrado = False
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_encontrado = True
            produto['quantidade'] += quantidade_entrada
            print("✅\033[32m  Entrada de produto realizada com sucesso!\033[0m")
            break
    
    if not produto_encontrado:
        print("❌\033[31m  Produto não encontrado.\033[0m")

    with open(arquivo_path, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4)
    
    input("Pressione Enter para continuar...")


def vender_produto(cls):
    """ Realiza a saída (venda) de um produto do estoque. """
    print("Informe os dados para saída de produto (venda):")
    id_produto = input("ID do produto: ")
    try:
        quantidade_saida = int(input("Quantidade a vender: "))
        if quantidade_saida <= 0:
            print("❌\033[31m  A quantidade vendida deve ser um número positivo.\033[0m")
            input("Pressione Enter para continuar...")
            return
    except ValueError:
        print("❌\033[31m  Quantidade inválida. Por favor, insira um número inteiro.\033[0m")
        input("Pressione Enter para continuar...")
        return

    arquivo_path = cls._Produto__arquivo

    with open(arquivo_path, "r", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)

    produto_encontrado = False
    for produto in produtos:
        if produto['id'] == id_produto:
            produto_encontrado = True
            if produto['quantidade'] >= quantidade_saida:
                produto['quantidade'] -= quantidade_saida
                print("✅\033[32m  Saída de produto (venda) realizada com sucesso!\033[0m")
            else:
                print(f"⚠️\033[33m  Estoque insuficiente! Temos apenas {produto['quantidade']} unidades de {produto['nome']}.\033[0m")
            break
    
    if not produto_encontrado:
        print("❌\033[31m  Produto não encontrado.\033[0m")

    
    with open(arquivo_path, "w", encoding="utf-8") as arquivo:
        json.dump(produtos, arquivo, indent=4)
        
    input("Pressione Enter para continuar...")