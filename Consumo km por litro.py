""""Codigó para calcular o consumo de um veiculo durante uma viagem"""
km = float(input("Quantos km de percuso: "))
lt = float(input("Quantos litros consumidos: "))

consumo = km / lt
print(f'Seu consumo foi de {consumo} KM/L')
if  consumo < 8:
    print("Venda o carro")
elif 8 < consumo < 14:
    print("Eco")
else:
    print("Super eco")