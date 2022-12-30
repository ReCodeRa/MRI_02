import scrapy
import json

keys = json.load("ProductKeys.json")

class CardsSpider(scrapy.Spider):
    name = 'cards'
    allowed_domains = ['mri.cts-mrp.eu']
    start_urls = ['https://mri.cts-mrp.eu/portal/details?productnumber=DK/H/0241/001']

    def start_requests(self):
            url = 'https://mri.cts-mrp.eu/portal/details?productnumber=DK/H/0241/001'
            yield scrapy.Request(url, 
            meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods= [
                    PageMethod('click', 'button[mattooltip="Download as excel file"]'),
                    PageMethod('expect_download'),
                    ]
            )
        )
    

    def parse(self, response):
        pass

#<mat-list _ngcontent-ng-cli-universal-c124="" role="list" class="mat-list mat-list-base documents-list"><!----></mat-list>