import scrapy
from automotoscraping.items import AutomotoBrand

class AutomotospiderSpider(scrapy.Spider):
    name = "automotospider"
    allowed_domains = ["automoto.it"]
    start_urls = ["https://www.automoto.it/catalogo"]

    def parse(self, response):
        brands_names = response.css('h2.plist-bcard-title > a::text').extract()
        other_brands_names = response.css('h3.sqlink > a::text').extract()

        brands_names.extend(other_brands_names)
        del other_brands_names
        brands_names = list(map(lambda name: name.replace('\n', '').replace(' ', ''), brands_names))

        brands_urls = response.css('h2.plist-bcard-title > a::attr(href)').getall()
        other_brands_urls = response.css('h3.sqlink > a::attr(href)').getall()

        brands_urls.extend(other_brands_urls)
        del other_brands_urls

        brands = []

        for i in range(len(brands_names)):
            brands.append({
                'name': brands_names[i],
                'url': f"https://www.automoto.it{brands_urls[i]}"
            })
        
        brands = sorted(brands, key=lambda brand: brand['name'].lower())
        am_brand = AutomotoBrand()

        for brand in brands:
            am_brand['name'] = brand['name']
            am_brand['url'] = brand['url']
            yield am_brand
        
        pass