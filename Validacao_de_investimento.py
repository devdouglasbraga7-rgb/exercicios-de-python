valor_a_investir = float(input("Quanto dinheiro você deseja investir? "))

if valor_a_investir <= 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor_a_investir <= 5000:
    print("Pefil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos ações")