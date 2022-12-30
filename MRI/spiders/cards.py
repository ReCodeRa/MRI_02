import scrapy
from scrapy_playwright.page import PageMethod


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
                    PageMethod('expect_download'),
                    PageMethod('click', 'button[mattooltip="Download as excel file"]'),
                    
                    ]
            )
        )
    

    def parse(self, response):
        yield {'text': response.text}


#<mat-list _ngcontent-ng-cli-universal-c124="" role="list" class="mat-list mat-list-base documents-list"><!----></mat-list>