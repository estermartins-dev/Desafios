from calculos import calcular_salario_estagiario, calcular_salario_clt, calcular_salario_freelancer
from cadastro import obter_dados_funcionario
from utils import gerar_texto_relatorio, salvar_em_arquivo

def processar_pagamento(dados):
   
    tipo = dados['tipo']
    
    if tipo == 'estagiario':
        bruto, inss, irrf, liquido = calcular_salario_estagiario(dados['salario'])
    elif tipo == 'clt':
        bruto, inss, irrf, liquido = calcular_salario_clt(dados['salario'])
    elif tipo == 'freelancer':
        bruto, inss, irrf, liquido = calcular_salario_freelancer(dados['horas'], dados['valor_hora'])
    
    return {
        "nome": dados['nome'],
        "tipo": tipo.capitalize(),
        "bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido
    }

def main():
    
    funcionarios_processados = []

    while True:
        print("\n--- Sistema de Folha de Pagamento ---")
        print("1. Cadastrar funcionário")
        print("2. Gerar relatório")
        print("3. Salvar relatório em arquivo")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            dados_brutos = obter_dados_funcionario()
            if dados_brutos:
                funcionario_completo = processar_pagamento(dados_brutos)
                funcionarios_processados.append(funcionario_completo)
                print(f"Funcionário {dados_brutos['nome']} cadastrado com sucesso!")

        elif opcao == '2':
            if not funcionarios_processados:
                print("Aviso: Nenhum funcionário cadastrado ainda.")
            else:
                relatorio = gerar_texto_relatorio(funcionarios_processados)
                print("\n" + relatorio)

        elif opcao == '3':
            if not funcionarios_processados:
                print("Erro: Não há dados para salvar.")
            else:
                conteudo = gerar_texto_relatorio(funcionarios_processados)
                salvar_em_arquivo(conteudo)

        elif opcao == '4':
            print("Encerrando o sistema. Até logo!")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()