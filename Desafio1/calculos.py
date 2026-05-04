DESCONTO_PERCENTUAL = 0.05  # 5%
QUANTIDADE_MINIMA_DESCONTO = 10  


def calcular_venda(produto, quantidade):
    
    valor_bruto = produto["preco"] * quantidade

    if quantidade > QUANTIDADE_MINIMA_DESCONTO:
        desconto = valor_bruto * DESCONTO_PERCENTUAL
    else:
        desconto = 0.0

    valor_final = valor_bruto - desconto

  
    produto["estoque"] -= quantidade

    return {
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }


def calcular_total_arrecadado(vendas):
    
    return sum(venda["valor_final"] for venda in vendas)
