from src.cadastro import cadastrar_produto, listar_produtos, atualizar_estoque
from src.calculos import calcular_venda
from src.utils import (
    gerar_relatorio,
    salvar_relatorio,
    adicionar_na_pilha,
    exibir_vendas_recentes,
)


def realizar_venda(produtos, vendas, pilha_recentes):
   
    print("\n--- Realizar Venda ---")

    while True:
        cliente = input("Nome do cliente: ").strip()
        if not cliente:
            print("Erro: O nome do cliente não pode ser vazio.")
            continue
        break

    if not listar_produtos(produtos):
        print("Cadastre produtos antes de realizar uma venda.")
        return vendas, pilha_recentes

    while True:
        selecao = input(
            "\nDigite o número ou o nome do produto desejado: "
        ).strip()

        produto_selecionado = None

        try:
            indice = int(selecao) - 1
            if 0 <= indice < len(produtos):
                produto_selecionado = produtos[indice]
            else:
                print("Erro: Índice fora do intervalo. Tente novamente.")
                continue
        except ValueError:
            for p in produtos:
                if p["nome"].lower() == selecao.lower():
                    produto_selecionado = p
                    break
            if produto_selecionado is None:
                print("Erro: Produto não encontrado. Tente novamente.")
                continue

        if produto_selecionado["estoque"] == 0:
            print(f"Erro: '{produto_selecionado['nome']}' está sem estoque.")
            continue

        break

    print(
        f"Produto selecionado: {produto_selecionado['nome']} "
        f"| Estoque disponível: {produto_selecionado['estoque']}"
    )

    while True:
        try:
            quantidade = int(input("Quantidade desejada: "))
            if quantidade <= 0:
                print("Erro: A quantidade deve ser maior que zero.")
                continue
            if quantidade > produto_selecionado["estoque"]:
                print(
                    f"Erro: Estoque insuficiente. "
                    f"Disponível: {produto_selecionado['estoque']} unidades."
                )
                continue
            break
        except ValueError:
            print("Erro: Digite um número inteiro válido para a quantidade.")

    dados_venda = calcular_venda(produto_selecionado, quantidade)
    dados_venda["cliente"] = cliente

    vendas.append(dados_venda)
    pilha_recentes = adicionar_na_pilha(pilha_recentes, dados_venda)

    print("\n--- Resumo da Venda ---")
    print(f"  Cliente : {cliente}")
    print(f"  Produto : {dados_venda['produto']}")
    print(f"  Quantidade: {quantidade}")
    print(f"  Valor Bruto : R$ {dados_venda['valor_bruto']:.2f}")
    print(f"  Desconto    : R$ {dados_venda['desconto']:.2f}")
    print(f"  Valor Final : R$ {dados_venda['valor_final']:.2f}")
    print("Venda realizada com sucesso!")

    return vendas, pilha_recentes


def exibir_menu():
    print("\n" + "=" * 40)
    print("         LOJA — MENU PRINCIPAL")
    print("=" * 40)
    print("  1. Cadastrar produto")
    print("  2. Realizar venda")
    print("  3. Gerar relatório")
    print("  4. Salvar relatório em arquivo")
    print("  5. Atualizar estoque de produto   [extra]")
    print("  6. Ver últimas vendas recentes    [extra]")
    print("  7. Sair")
    print("-" * 40)
    return input("Escolha uma opção: ").strip()


def main():
    produtos = []     
    vendas = []         
    pilha_recentes = [] 

    print("\nBem-vindo ao Sistema de Loja Simples!")

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            produtos = cadastrar_produto(produtos)

        elif opcao == "2":
            vendas, pilha_recentes = realizar_venda(produtos, vendas, pilha_recentes)

        elif opcao == "3":
            gerar_relatorio(vendas)

        elif opcao == "4":
            salvar_relatorio(vendas)

        elif opcao == "5":
            produtos = atualizar_estoque(produtos)

        elif opcao == "6":
            exibir_vendas_recentes(pilha_recentes)

        elif opcao == "7":
            print("\nEncerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Digite um número entre 1 e 7.")


if __name__ == "__main__":
    main()
