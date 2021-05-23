import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import smtplib


csv_file = open('Produtos.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Titulo', 'Link', 'Valor'])

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input("Digite o nome do produto")

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})
id=0
for produto in produtos:

    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={'class': 'price-tag-cents'})

    #print(produto.prettify())
    print("Titulo do produto: ", titulo.text)
    print("Link do produto: ",link['href'])

    if (centavos):
        print("Preço do produto: R$", real.text + ',' + centavos.text)
    else:
        print("Preço do produto: R$", real.text)
    print('\n\n')
    
    id+=1
    csv_writer.writerow([titulo.text,link['href'], real.text])
csv_file.close()

print("=="*15)
print("Gerando Dados")
print("=="*15)

sleep(3)
print("Dados Salvo Com Sucesso")
sleep(15)





