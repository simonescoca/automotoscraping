# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutomotoBrand(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class AutomotoModel(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class AutomotoVersion(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    pass

class AutomotoCarSpecs(scrapy.Item):
    brand = scrapy.Field()
    model = scrapy.Field()
    setup = scrapy.Field()
    start_price = scrapy.Field()
    start_production = scrapy.Field()
    end_production = scrapy.Field()
    body = scrapy.Field()
    n_doors = scrapy.Field()
    n_seats = scrapy.Field()
    trunk_capacity = scrapy.Field()
    fuel_tank_capacity = scrapy.Field()
    curb_weight = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    wheelbase = scrapy.Field()
    engine_layout = scrapy.Field()
    displacement = scrapy.Field()
    fuel = scrapy.Field()
    hybrid_type = scrapy.Field()
    combustion_plus_e_power = scrapy.Field()
    combustion_plus_e_torque = scrapy.Field()
    max_power_rpm = scrapy.Field()
    peak_power = scrapy.Field()
    max_torque_rpm = scrapy.Field()
    traction = scrapy.Field()
    gearbox = scrapy.Field()
    n_gears = scrapy.Field()
    top_speed = scrapy.Field()
    zero_to_100 = scrapy.Field()
    co2_emissions = scrapy.Field()
    anti_pollution_class = scrapy.Field()
    urban_fuel_consumption = scrapy.Field()
    extra_urban_fuel_consumption = scrapy.Field()
    combined_fuel_consumption = scrapy.Field()
    e_motor_range = scrapy.Field()
    pass