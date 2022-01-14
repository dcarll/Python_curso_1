"""
1. Abrir a pastas do projeto
2. Criar um ambiente virtual
3. Instalar os módulos
4. AbrirAbrir um projeto no python
5. Buscar as informações no IMDB
6. Criar meu código
"""
import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_url = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        filmes = response.css('.titleColumn a')
        votos = response.css('.strong')
        ano_filme = response.css('.secondaryInfo')

        print(filmes.text)


filmes = ImdbSpider()

