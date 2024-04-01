#condição while
'''
contador = 3
while(contador <= 8):
    print(f"O contador esta em {contador}")
    contador = contador + 1

else: 
    print("O contador chegou ao fim")    

'''



'''
contador = True

while contador:
   inp = eval(input("Digite um numero entre 0 e 20: "))
if inp >= 0 and inp <=10:   
    contador = False
else: 
    print("O contador chegou ao fim")    '''


#Condição "For"

'''ene = 10

for i in range(0,ene+1,2):
    print(i)

'''


#vetor

vetor1 = [1,2,3]

vetor2 = [3,2,1]
for x in range (0,len(vetor1)):
    vetor2.append(x*2)
    print(vetor2)

    