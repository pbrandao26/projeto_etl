import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/calcados"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for prouct in products:
            
            yield{
            'brand':products.css('span.ui-search-item__brand-discoverability ui-search-item__group__element::text').get()
            }

        pass
