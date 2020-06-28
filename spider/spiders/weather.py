import scrapy

class WeatherSpider(scrapy.Spider):
    name = 'price'
    start_urls = [
        'http://www.beijingprice.cn/jfcx/sp/index.shtml?ItemCode=E000002',
    ]

    def parse(self, response):
        # blue = response.css('div.blue-text')
        # green = response.css('div.green-text')
        # red = response.css('div.red-text')
        yield {
            'blueRice':response.css('#pricePF::text').get(),
            'greenPrice':response.css('#priceLS::text').get(),
            'redPrice':response.css('#priceCS::text').get(),
        }

