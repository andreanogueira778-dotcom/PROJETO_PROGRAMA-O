#ids e valores
#111 - leite 3.0
#222 - pão 0.75
#333 - manteiga 20.0
#444 - bolo 5.0
#555 - suco 3.0
#666 - bolacha 5.0
#777 - café 2.0
#888 - requeijão 40.0
#999 - chimango 3.0
#000 - queijo 10.0

import os

from produto import Produto #importa a classe produto do arquivo produto.py

def menu():
    while True:
        os.system("clear")#limpar terminal
        print("""
        \033[1;33m=========================================================\033[0m
                \033[94mBEM- VINDO(A) AO ESTOQUE DA BARRACA DA LI\033[0m   
        \033[1;33m=====================\033[0m🧁 \033[91mMENU\033[0m 🧀 \033[1;33m=======================\033[0m
              
          1️⃣  - \033[91mCadastrar Produto\033[0m   2️⃣  - \033[91mListar Produtos\033[0m
          3️⃣  - \033[91mAdicionar produto\033[0m   4️⃣  - \033[91msaida de produto (venda)\033[0m
          0️⃣  - \033[91mSair\033[0m
        \033[1;33m=========================================================\033[0m
              
            """)
        
        OP = input("Escolha uma opção:") 

        if OP == "1":
            Produto.cadastrar()

        elif OP == "2":
            Produto.listar()

        elif OP == "3":
            Produto.adicionar()

        elif OP == "4":
            Produto.vender()

        elif OP == "0":
            print("Saindo...")
            break
            
        else:
            print("❌ Opção inválida, tente novamente.")

    

if __name__ == "__main__":
    menu()