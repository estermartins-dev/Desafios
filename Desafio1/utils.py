import os
from src.calculos import calcular_total_arrecadado

LIMITE_PILHA = 5


def adicionar_na_pilha(pilha_recentes, venda):
    pilha_recentes.append(venda)
    if len(pilha_recentes) > LIMITE_PILHA:
        pilha_recentes.pop(0)
    return pilha_recentes


def _formatar_venda(venda):
    return (
        f"Cliente: {venda['cliente']}\n"
        f"Produto: {venda['produto']}\n"
        f"Quantidade: {venda['quantidade']}\n"
        f"Valor Bruto: R$ {venda['valor_bruto']:.2f}\n"
        f"Desconto: R$ {venda['desconto']:.2f}\n"
        f"Valor Final: R$ {venda['valor_final']:.2f}\n"
        + "-" * 40
    )


def gerar_relatorio(vendas):
    if not vendas:
        print("\nNenhuma venda realizada.")
        return

    print("\n=== Relatório de Vendas ===")

    for v in vendas:
        print(_formatar_venda(v))

    total = calcular_total_arrecadado(vendas)
    print(f"\nTotal arrecadado: R$ {total:.2f}")


def exibir_vendas_recentes(pilha_recentes):
    if not pilha_recentes:
        print("\nNenhuma venda recente.")
        return

    print("\n=== Últimas vendas ===")
    for v in reversed(pilha_recentes):
        print(_formatar_venda(v))


def salvar_relatorio(vendas):
    if not vendas:
        print("\nNão há vendas para salvar.")
        return

    base_dir = os.path.dirname(os.path.dirname(__file__))
    pasta = os.path.join(base_dir, "relatorios")
    os.makedirs(pasta, exist_ok=True)

    caminho = os.path.join(pasta, "relatorio_vendas.txt")

    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Relatório de Vendas ===\n")

            for v in vendas:
                arquivo.write(_formatar_venda(v) + "\n")

            total = calcular_total_arrecadado(vendas)
            arquivo.write(f"\nTotal arrecadado: R$ {total:.2f}\n")

        print(f"\nRelatório salvo com sucesso em: {caminho}")

    except Exception as e:
        print("Erro ao salvar:", e)