import requests
import json
import hashlib

codenation = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b239bc9eb966a651dd325fb5937812f40f70ff84')
dado = codenation.json()

token = dado['token']
caracteres = 'abcdefghijklmnopqrstuvwxyz'
casas = dado['numero_casas']
decifrado = dado['decifrado']
cifrado = dado['cifrado']

decifrado = decifrado.lower()
cifrado = cifrado.lower()

#Criptografar

#for letra in decifrado:
#    if letra in caracteres:
#        num = caracteres.find(letra) + casas
#
#        if num >= len(caracteres):
#            num = num - len(caracteres)
#
#        #print(letra, num, caracteres[num])
#     
#        cifrado = cifrado + caracteres[num]
#
#    else:
#        cifrado = cifrado + letra

#Descriptografar

for letra in cifrado:
    if letra in caracteres:
        num = caracteres.find(letra) - casas
        
        if num < 0:
            num = len(caracteres) + num   
        decifrado = decifrado + caracteres[num]

    else:
        decifrado = decifrado + letra

resumo = hashlib.sha1(decifrado.encode('utf-8')).hexdigest()

print('token: ', token,'\ncasas: ',casas,'\ndecifrado: ',decifrado,'\ncifrado: ',cifrado,'\nresumo: ', resumo)
