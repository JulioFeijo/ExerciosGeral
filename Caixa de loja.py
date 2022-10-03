print('{:=^40}'.format(' LOJA JULIO '))
preço = float(input('Preço das compras: '))
print(''''Qual opção de compra
[ 1 ] - Avista / Cheque
[ 2 ] - Avista no cartão
[ 3 ] - 2x no Cartão
[ 4 ] - 3x ou mais''')

opção = int(input('Qual a opção: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    vezes = 2
    total = preço
    parcela = preço / 2
    print('Sua compra será parcelada em {}X com a parcelade R${:.2f}'.format(vezes, parcela))
elif opção == 4:
    vezes = int(input('Quantidade que você quer parcelar: '))
    total = preço + (preço * 20 / 100)
    parcela = total / vezes
    print('Sua compra será parcelada em {}X com a parcelade R${:.2f} COM JUROS'.format(vezes, parcela))
print('Valor da sua compra R${:.2f} e com um valor final de R${:.2f}'.format(preço, total))
print('Obrigado pela preferencia! Volte sempre')
