def calcular_salario_estagiario(valor_fixo):
    return valor_fixo, 0.0, 0.0, valor_fixo

def calcular_salario_clt(salario_bruto):
    inss = salario_bruto * 0.08
    irrf = (salario_bruto * 0.10) if salario_bruto > 2000 else 0.0
    liquido = salario_bruto - inss - irrf
    return salario_bruto, inss, irrf, liquido

def calcular_salario_freelancer(horas, valor_hora):
    bruto = horas * valor_hora
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return bruto, desconto, 0.0, liquido