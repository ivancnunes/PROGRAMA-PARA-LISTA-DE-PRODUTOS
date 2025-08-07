# Programa de gerenciamento de lista de compras
# Um programa que cria uma lista de compras ,permitindo adicionar, listar, editar e remover produtos de forma rápida e fácil. 

import time  # Biblioteca time para adicionar o tempo de um segundo para apresentação

lista = [("Arroz", 4.5),("Queijo", 15),("Carne Moída", 15)]  # Lista que armazenará os produtos como tuplas (nome, valor)
comando = ""  # Variável que armazena o comando escolhido pelo usuário
valor_total = (4.5+15+15)  # Variável que armazena o valor total dos produtos da lista
produto = ""  # Variável auxiliar para armazenar o nome do produto

while True:  # Loop principal que exibirá o menu até o usuário escolher finalizar

    # Lista inicial para comandos
    time.sleep(1)
    print("-" * 20)
    print("\nLISTA DE PRODUTOS\n"
          "1 - Adicionar produto\n"
          "2 - Listar produtos\n"
          "3 - Remover produto\n"
          "4 - Editar lista\n"
          "5 - Finalizar\n")
    print("-" * 20)

    comando = int(input("Escolha uma opção: ").strip())
    # Comando 1: adiciona itens na lista de produtos com seus valores
    if comando == 1:
        while True:  # Loop onde recebe os produtos e valores até o usuário escolher finalizar os cadastros
            produto = input("\nInforme o nome do produto (escreva 'sair' para finalizar): ").strip()
            if produto == "sair":  # Verifica se o comando 'sair' foi informado, e se for, encerra o loop para cadastro de produtos
                break
            else:
                valor = float(input("Informe o valor do produto: "))
                valor_total += valor
                lista.append((produto, valor))
                print(f"Produto {produto} adicionado com sucesso!\n")

    # Comando 2: Exibir a lista atual de produtos cadastrados
    if comando == 2:
        time.sleep(1)
        print("\nLISTA DE PRODUTOS")
        for produto, valor in lista:  # Apresenta os produtos e valores um de cada vez em formato de lista
            print(f"- {produto}: R$ {valor}")

    # Comando 3: Remove um item específico da lista de produtos
    if comando == 3:
        time.sleep(1)
        remover = input("Informe o produto que deseja remover: ")
        for produto, valor in lista:
            if produto == remover:
                lista.remove((produto, valor))
                valor_total -= valor
                print(f"{produto} removido com sucesso!")

    # Comando 4: Editar o nome e o valor de um produto já existente
    if comando == 4:
        time.sleep(1)
        for indice, (produto, valor) in enumerate(lista):
            print(f"{indice} - {produto}: R$ {valor}")

        produto_antigo = int(input("Informe o número do produto que deseja alterar: "))
        produto_novo = input("Informe o novo produto: ")
        valor_novo = float(input("Informe o novo preço: "))
        valor_antigo= lista[produto_antigo][1]
        lista[produto_antigo] = (produto_novo, valor_novo)
        print(f"{produto_novo} adicionado com sucesso")
        valor_total -= valor_antigo
        valor_total += valor_novo

    # Comando 5: Finaliza o programa e exibe o resumo da lista
    if comando == 5:
        break

# Fim do loop, finalizando e mostrando a lista completa com o valor total dos itens cadastrados
time.sleep(1)
print("LISTA FINALIZADA")
for produto, valor in lista:
    print(f"- {produto}: R$ {valor}")
print(f"O valor total dos itens é R$ {valor_total}")

