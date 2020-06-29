import scrapy

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    start_urls = [
        'https://movie.douban.com/top250',
    ]

    def parse(self, response):
        article = response.css('div.article')
        for node in article.css('ol li'):
            quote = node.css('span.inq::text').get()
            if quote is not None:
                quote.strip()
            yield {
                'cover':node.css('img::attr(src)').get(),
                'name':node.css('span.title::text').getall(),
                'other':node.css('span.other::text').get().strip(),
                'des':node.css('p::text').get().strip(),
                'rating_num':node.css('span.rating_num::text').get(),
                'quote':quote,
            }
        
        next_span = article.css('span.next')
        next_page = next_span.css('a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)



#学习过程中问题
# Crawled (403) <GET https://movie.douban.com/top250> (referer: None)
# Ignoring response <403 https://movie.douban.com/top250>: HTTP status code is not handled or not allowed
# 解决方法
# 网页抓包后获取 User_Agent 并在setting中设置 USER_AGENT = ''
        