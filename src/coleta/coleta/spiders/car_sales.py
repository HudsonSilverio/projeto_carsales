import scrapy

class CarSalesSpider(scrapy.Spider):
    name = "car_sales"
    start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes-em-minas-gerais/carro-a-venda_NoIndex_True#applied_filter_id%3Dstate%26applied_filter_name%3DLocaliza%C3%A7%C3%A3o%26applied_filter_order%3D6%26applied_value_id%3DTUxCUE1JTlMxNTAyZA%26applied_value_name%3DMinas+Gerais%26applied_value_order%3D10%26applied_value_results%3D26650%26is_custom%3Dfalse"]
    page_count = 1
    max_pages = 50

    def parse(self, response):
        car = response.css('div.ui-search-result__content')

        for car in car:
            yield {
                'descricao': car.css('h2.ui-search-item__title::text').get(),
                'preco': car.css('span.andes-money-amount__fraction::text').get(),
                'ano': car.css('li.ui-search-card-attributes__attribute::text').get(),
                'km_rodado': response.css('ul.ui-search-card-attributes.ui-search-item__group__element li:last-child::text').get(),
                'localizacao': response.css('span.ui-search-item__group__element.ui-search-item__location::text').get()
            }

        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
