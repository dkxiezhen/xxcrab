import scrapy

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        article = response.css('div.article')
        