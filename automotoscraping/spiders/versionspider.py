import scrapy
import json
import os
from automotoscraping.items import AutomotoVersion


class VersionSpider(scrapy.Spider):
    name = "versionspider"
    allowed_domains = ["automoto.it"]
    start_urls = []

    if  os.path.exists(f"{os.getcwd()}/models.json"):
        with open('models.json', 'r', encoding='utf-8') as f:
            models = json.load(f)
            for model in models:
                start_urls.append(model['url'])

        def parse(self, response):

            brand_model = response.css('div.plist-pagehead-top h1.ahead-title::text').get().replace('\n', '').strip()
            brand_model = brand_model[:brand_model.find(' (')]

            versions_names = response.css('div.amodtable-item a.amodtable-item-name::text').extract()
            versions_names = list(map(lambda name: name.replace('\n', '').strip(), versions_names))
            versions_names = list(filter(lambda name: name != '', versions_names))

            versions_urls = response.css('div.amodtable-item a.amodtable-item-name::attr(href)').getall()
            versions = []

            for i in range(len(versions_names)):
                versions.append({
                    'name': f"{brand_model} {versions_names[i]}",
                    'url': f"https://www.automoto.it{versions_urls[i]}"
                })
            
            am_version = AutomotoVersion()

            for version in versions:
                am_version['name'] = version['name']
                am_version['url'] = version['url']
                yield am_version
            pass