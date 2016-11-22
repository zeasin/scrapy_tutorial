import scrapy

from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.viptijian.com/0592/xmxhfy"
    ]

    def parse(self, response):
        for sel in response.xpath('//body'):
            item = TutorialItem()
            item['title'] = sel.xpath('//div[@class="nameinfo"]').xpath('h1/text()').extract()
            item['link'] = sel.xpath('//div[@class="nameinfo"]').xpath('span/em/text()').extract()
            item['desc'] = sel.xpath('//div[@class="nameinfo"]').xpath('span/em/text()').extract()
            yield item
