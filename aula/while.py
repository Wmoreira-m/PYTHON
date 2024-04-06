condicao = True

soma = 0


while condicao:

  numero = eval(input("quais notas vc quer sacar? "))
  if (numero > 0) and (numero <= 10):
    soma += numero
  elif (numero >= 11) and (numero <= 20):
    print ("Infelizmente estamos sem essa nota")
  else:
    break

print(f"Seu saldo será {soma}")    

    