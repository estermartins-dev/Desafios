import os

def gerar_texto_relatorio(lista_funcionarios):
    texto = "=== Relatório de Folha de Pagamento ===\n"
    total_empresa = 0
    for f in lista_funcionarios:
        texto += f"Nome: {f['nome']}\n"
        texto += f"Tipo: {f['tipo']}\n"
        texto += f"Salário Bruto: R$ {f['bruto']:.2f}\n"
        texto += f"Desconto INSS: R$ {f['inss']:.2f}\n"
        texto += f"Desconto IRRF: R$ {f['irrf']:.2f}\n"
        texto += f"Salário Líquido: R$ {f['liquido']:.2f}\n"
        texto += "-" * 30 + "\n"
        total_empresa += f['liquido']
    
    texto += f"Total pago pela empresa: R$ {total_empresa:.2f}"
    return texto

def salvar_em_arquivo(conteudo):
    try:
        if not os.path.exists("relatorios"):
            os.makedirs("relatorios")
            
        caminho = os.path.join("relatorios", "relatorio_folha.txt")
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"Relatório salvo com sucesso em: {caminho}")
    except OSError as e:
        print(f"Erro ao salvar o arquivo: {e}")