import requests
import json
import hashlib

url_get = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=b239bc9eb966a651dd325fb5937812f40f70ff84'
url_post = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=b239bc9eb966a651dd325fb5937812f40f70ff84'

response = requests.get(url_get)
dado = response.json()

header = response.headers
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

answer ={'numero_casas':casas,'token':token,'cifrado':cifrado,'decifrado':decifrado,'resumo_criptografico':resumo}
answer = json.dumps(answer)
print(answer)

arquivo = open ('answer.json','w')
arquivo.write(answer)
arquivo.close()

files={'answer':(open('answer.json','rb'))}
r = requests.post(url_post, files=files)
print(r.status_code)
print(r.text)
