def obter_dados_funcionario():
    try:
        nome = input("Nome do funcionário: ").strip()
        if not nome:
            print("Erro: O nome não pode ser vazio.")
            return None
        
        tipo = input("Tipo (estagiario, clt, freelancer): ").strip().lower()
        if tipo not in ['estagiario', 'clt', 'freelancer']:
            print("Erro: Tipo de funcionário inválido.")
            return None

        if tipo == 'freelancer':
            h = float(input("Horas trabalhadas: "))
            v = float(input("Valor por hora: "))
            if h <= 0 or v <= 0:
                raise ValueError
            return {"nome": nome, "tipo": tipo, "horas": h, "valor_hora": v}
        else:
            sal = float(input("Salário base: "))
            if sal <= 0:
                raise ValueError
            return {"nome": nome, "tipo": tipo, "salario": sal}
            
    except ValueError:
        print("Erro: Entrada inválida. Use apenas números positivos para valores.")
        return None