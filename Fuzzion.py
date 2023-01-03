# En este programa Haremos Fuzzing de Paginas web o Dominios en archivos de TXT, tanto que tendremos La direccion del Diccionario y los Dominos
import requests
import wfuzz
import checkdomains
wordlist =
requests.get('https://raw.githubusercontent.com/maurosoria/dirsearch/master/db/dicc.txt')
domains = open("Dominiospaginasweb.txt","r")
payloads = wfuzz.get_payload(wordlist)
for domain in domains.readlines():
subdomains = open(domain.rstrip("\n")+"_subdominiosweb.txt","r")
for subdomain in subdomains.readlines():
urls = checkdomains.isdomainlive(subdomain.rstrip("\n"))
if urls:
for url in urls:
print("Fuzzing - "+url)
try:
fuzzer = payloads.fuzz(url=url+"/FUZZ",sc=[200])
for result in fuzzer:
print(result)
except:
pass
