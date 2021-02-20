import requests
import sys
import os

requests.urllib3.disable_warnings()  #disable ssl warnings

abreficheiro = open('sites_', 'r+')
conteudo = abreficheiro.readlines()
person = sys.argv[1]
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
listatoda_argumento = [''.join([x.strip(), person]) for x in conteudo]

for sites in listatoda_argumento:
        try:
                urls = sites
                person_interest = sites + person
                pedido = requests.get(sites,headers=headers, timeout=10)
                if pedido.status_code == 200:
                        with open("results.txt", 'a') as results:
                                results.write(sites)
                                results.write("\n")
                
        except:
                pass
