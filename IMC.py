sexo = float(input("Feminino digite 1 | Masculino digite 2  :  "))
altura = float(input("Sua altura : "))
peso = float(input("Seu peso : "))

if  sexo == 1 :
    imc = peso / (altura ** 2)
    ideal = (62.1 * altura) - 44.7
    print(f'IMC de F {imc}   e peso ideal de {ideal}')
else:
    imc = peso / (altura ** 2)
    ideal = (72.7 * altura) - 58
    print(f'Imc de M {imc}    e peso ideal de {ideal}')
