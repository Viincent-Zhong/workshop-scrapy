from urllib.request import Request
import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        yield {
            'title': response.xpath('//title/text()').getall(),
            'name' : response.css('name').xpath('@src').getall(),
            'description' : response.xpath('//p[contains(@class, "description")]').getall(),
            'id' : response.css('id').xpath('@src').getall(),
            'current_url' : response.xpath('href').getall(),
            'image' : response.css('img').xpath('@src').getall(),
            'detail_link' : response.xpath("//link").getall(),
            'price' : response.css('div').xpath('@src').getall(),
            'old_price' : response.css('old_price').xpath('@src').getall(),
            'availability' : response.css('availability').xpath('@src').getall(),
            'flag' : response.css('flag').xpath('@src').getall()
        }
