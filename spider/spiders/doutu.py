import scrapy

class doutuSpider(scrapy.Spider):
    name = 'doutu'
    page_num = 0

    custom_settings = [

    ]

    start_urls = [
        'https://www.doutula.com/photo/list?page=0',
    ]

    def parse(self, response):
        self.page_num += 1
        conDiv = response.css('div.page-content a')
        for aImg in conDiv:
            yield {
                'img':aImg.css('img::attr(data-original)').get(),
                'name':aImg.css('p::text').get(),
            }
        
        nextPages = response.css('ul.pagination li')
        nextPage = nextPages[-1]
        nextLink = nextPage.css('a::attr(href)').get()
        if nextLink is not None and self.page_num < 10:
            nextLink = 'https://www.doutula.com'+nextLink
            yield scrapy.Request(url=nextLink,callback=self.parse)

