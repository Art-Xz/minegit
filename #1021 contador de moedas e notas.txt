#1021 contador de moedas e notas:
print("NOTAS:")
valor = float(input())
qtd100 = valor//100
valor%=100

qtd50 = valor//50
valor%=50

qtd20 = valor//20
valor%=20

qtd10 = valor//10
valor%=10

qtd5 = valor//5
valor%=5

qtd2 = valor//2
valor%=2

#MOEDAS
valor_centavos = round(valor*100)

qtdm1 = valor_centavos//100
valor_centavos%=100

qtdm050 = valor_centavos//50
valor_centavos%=50

qtdm025 = valor_centavos//25
valor_centavos%=25

qtdm010 = valor_centavos//10
valor_centavos%=10

qtdm005 = valor_centavos//5
valor_centavos%=5

qtdm001 = valor_centavos

print(f"{int(qtd100)} nota(s) de R$ 100.00")
print(f"{int(qtd50)} nota(s) de R$ 50.00")
print(f"{int(qtd20)} nota(s) de R$ 20.00")
print(f"{int(qtd10)} nota(s) de R$ 10.00")
print(f"{int(qtd5)} nota(s) de R$ 5.00")
print(f"{int(qtd2)} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{int(qtdm1)} moeda(s) de R$ 1.00")
print(f"{int(qtdm050)} moeda(s) de R$ 0.50")
print(f"{int(qtdm025)} moeda(s) de R$ 0.25")
print(f"{int(qtdm010)} moeda(s) de R$ 0.10")
print(f"{int(qtdm005)} moeda(s) de R$ 0.05")
print(f"{int(qtdm001)} moeda(s) de R$ 0.01")
