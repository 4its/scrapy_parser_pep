import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            '#numerical-index a.pep.reference.internal'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = ''.join(response.css(
            'h1.page-title ::text'
        ).getall())[4:].split(' – ')
        yield PepParseItem(
            number=number,
            name=name,
            status=response.css(
                'dt:contains("Status")+dd abbr::text'
            ).get()
        )
