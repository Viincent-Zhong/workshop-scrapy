import scrapy



class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']

    def start_requests(self):
        start_urls = ['https://webscraper.io/test-sites/e-commerce/static']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
    # def parse(self, response):
    #     item = scrapy.Item()
    #     item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
    #     item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
    #     item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
    #     item['link_text'] = response.meta['link_text']
    #     url = response.xpath('//td[@id="additional_data"]/@href').get()
    #     return response.follow(url, self.parse_additional_page, cb_kwargs=dict(item=item))
