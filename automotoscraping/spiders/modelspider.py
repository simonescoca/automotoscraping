import scrapy
import json
from automotoscraping.items import AutomotoModel


class ModelSpider(scrapy.Spider):
    name = "modelspider"
    allowed_domains = ["automoto.it"]
    start_urls = []

    with open('brands.json', 'r', encoding='utf-8') as f:
        brands = json.load(f)
        for brand in brands:
            start_urls.append(brand['url'])

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        brand = response.css('div.plist-pcard a > span.plist-pcard-title-gray::text').get()
        models_names = response.css('div.plist-pcard a::text').extract()
        models_names = list(map(lambda name: name.replace('\n', '').strip(), models_names))
        models_names = list(map(lambda name: name[:name.find(' (')], models_names))
        models_names = list(filter(lambda name: name != '', models_names))

        models_urls = response.css('div.plist-pcard > figure.plist-pcard-img > a::attr(href)').getall()
        models = []

        for i in range(len(models_names)):
            models.append({
                'name': f"{brand} {models_names[i]}",
                'url': f"https://www.automoto.it{models_urls[i]}"
            })
        
        am_model = AutomotoModel()

        for model in models:
            am_model['name'] = model['name']
            am_model['url'] = model['url']
            yield am_model

        # models = []
        # models_names = response.css('div.modello div.tlist-container div.tlist-title a::text').getall()
        # models_urls = response.css('div.modello div.tlist-container div.tlist-title a::attr(href)').getall()

        # models = [{'name': name.strip(), 'url': f"https://www.automoto.it{url}"} for name, url in zip(models_names, models_urls)]

        # with open(f'models_{brand_name}.json', 'w', encoding='utf-8') as f:
        #     json.dump(models, f, ensure_ascii=False, indent=4)
        pass