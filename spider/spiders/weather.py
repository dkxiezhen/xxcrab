import scrapy

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    start_urls = [
        '',
    ]