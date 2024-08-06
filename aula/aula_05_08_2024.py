def saudacoes():
    print("Bem vindos de volta!!!!")

saudacoes()

def apresenta_media(nome:str, nota1:float, nota2:float):
    calcMedia = (nota1 + nota2) / 2
    print(f"{nome}, sua média é de {calcMedia}")

apresenta_media("Julio", 10, 3)

def media_funcao(*args): 
    #agrs é usado para quando a quantidade de parametros possa mudar
    soma = 0
    for nota in args:
        soma += nota
    media = soma / len(args)
    return media

print(media_funcao(2, 4, 8, 10))