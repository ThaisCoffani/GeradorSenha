import random

#Importei a biblioteca random, pois quero criar uma senha aleatória

#Criar a variável senha que será igual a um espaço vazio

senha = " "

#o i será para letras maiusculas, o j para minusculas e k para números 

for i in range(3):
    i = chr(random.randint(65,90))
    for j in range(3):
        j = chr(random.randint(65,90)).lower()
        for k in range(3):
            k = (random.randint(0,10))
            
#Declarar como será gerada a nova senha
            
    senha = str(senha) + i + j + str(k) 
                   
print(senha)

