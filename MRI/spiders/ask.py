import scrapy
from scrapy_playwright.page import PageMethod

term = "dasatinib"

class AskSpider(scrapy.Spider):
    name = 'ask'
    allowed_domains = ['mri.cts-mrp.eu']
    start_urls = ['https://mri.cts-mrp.eu/portal/fulltext-search']

    def start_requests(self):
        url = 'https://mri.cts-mrp.eu/portal/fulltext-search'
        yield scrapy.Request(url, 
        meta=dict(
            playwright=True,
            playwright_include_page=True,
            playwright_page_methods= [
                PageMethod('wait_for_selector', 'input#mat-input-2'),
                PageMethod('fill', 'input#mat-input-2', term),
                PageMethod('click', 'button[mattooltip="Execute query"]'),
                PageMethod('click', f'div[aria-label="Display 1000 items on page"]'),
                PageMethod('wait_for_timeout', 10000)
                ]
        )
        )


    def parse(self, response):
            #for Product in response.css('tr[aria-rowindex]'):
            for Product in response.css('tr.dx-row.dx-data-row.dx-row-lines'):
                yield {
                    'ProductKey': Product.css('td::text').get()
                }
        #yield {'text': response.text}

# <tr class="dx-row dx-data-row dx-row-lines" role="row" aria-selected="false" aria-rowindex="1"><td aria-describedby="dx-col-1" aria-selected="false" role="gridcell" aria-colindex="1" style="text-align: left;" class="dx-cell-focus-disabled" tabindex="0">DK/H/0241/001</td><td aria-describedby="dx-col-3" aria-selected="false" role="gridcell" aria-colindex="2" style="text-align: left;">Human</td><td aria-describedby="dx-col-4" aria-selected="false" role="gridcell" aria-colindex="3" style="text-align: left;">PRODUCT</td><td aria-describedby="dx-col-5" aria-selected="false" role="gridcell" aria-colindex="4" style="text-align: left;">Product metadata</td><td aria-describedby="dx-col-6" aria-selected="false" role="gridcell" aria-colindex="5" style="text-align: left;"><div _ngcontent-ng-cli-universal-c185="" class="dx-template-wrapper"><div _ngcontent-ng-cli-universal-c185="">DK/H/0241/001 | Dialope | Copyfarm A/S
# Denmark | DK | <mark>loperamide</mark> hydrochloride 2 mg | loperamide A07DA03 | Šumivá tableta</div></div></td><td class="dx-command-edit dx-command-edit-with-icons" aria-selected="false" role="gridcell" aria-colindex="6" style="text-align: center;"><a href="#" class="dx-link dx-icon-arrowright dx-link-icon" title="Details"></a>&nbsp;</td></tr>

#<div class="dx-page-size dx-selection" tabindex="0" role="button" aria-label="Display 1000 items on page">1000</div>