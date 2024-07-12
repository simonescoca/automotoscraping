import scrapy
import json
import os


class CarSpecSpider(scrapy.Spider):
    name = "carspecspider"
    allowed_domains = ["automoto.it"]
    start_urls = []

    if  os.path.exists(f"{os.getcwd()}/versions.json"):
        with open('versions.json', 'r', encoding='utf-8') as f:
            versions = json.load(f)
            for version in versions:
                start_urls.append(version['url'])

        def parse(self, response):

            main_keys = response.css('div#panel-main-data table.datagrid th::text').getall()
            chassis_keys = response.css('div#panel-chassis table.datagrid th::text').getall()
            engine_keys = response.css('div#panel-engine table.datagrid th::text').getall()
            performance_keys = response.css('div#panel-performance table.datagrid th::text').getall()

            keys = main_keys + chassis_keys + engine_keys + performance_keys
            keys = list(map(lambda key: key.replace('\n', '').strip(), keys))
            
            if 'Tutte le versioni disponibili' in keys:
                keys.remove('Tutte le versioni disponibili')

            while '' in keys:
                keys.remove('')

            main_values = response.css('div#panel-main-data table.datagrid td::text').getall()
            chassis_values = response.css('div#panel-chassis table.datagrid td::text').getall()
            engine_values = response.css('div#panel-engine table.datagrid td::text').getall()
            performance_values = response.css('div#panel-performance table.datagrid td::text').getall()

            values = main_values + chassis_values + engine_values + performance_values
            values = list(map(lambda value: value.replace('\n', '').replace('                                                                    ', ' ').strip(), values))

            while '' in values:
                values.remove('')

            specs = {}

            for i in range(len(keys)):
                specs[keys[i]] = values[i]

            yield specs

            pass