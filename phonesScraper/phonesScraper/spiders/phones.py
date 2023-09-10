import scrapy
import re


class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["productindetail.com"]
    start_urls = ["https://productindetail.com/"]

    def parse(self, response):
        # Extract links to category pages
        category_links = response.css('.navbar-nav .dropdown-menu .dropdown-item::attr(href)').extract()
        for index, category_link in enumerate(category_links):
            if index == 0 :
                yield response.follow(category_link, callback=self.parse_category)

    def parse_category(self, response):
        # Extract links to product pages within the category
        product_links = response.css('.card-body p a::attr(href)').extract()
        for product_link in product_links:
            yield response.follow(product_link, callback=self.parse_product)

        # If there are more pages of products in the category, follow pagination links
        next_page = response.css('.page-link[aria-label="Next"]:not(.disabled)::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_category)

    def parse_product(self, response):
            yield {
                "Product name": response.css(".card-body h1 strong::text").get(),
                "Brand": re.match(r'\w+', response.css(".card-body h1 strong::text").extract_first()).group() if response.css(".card-body h1 strong::text").extract_first() else None,
                "Description": response.css('.card > div.row p small::text').getall(),
                "Operating System": response.css('div[id="cellular"] tr:contains("Operating System") td small::text').get(),
                "Display technology": response.css('div[id="display"] tr:contains("Display Technology") td small::text').get(),
                "Image URL": response.css('.card .card-body img::attr(src)').extract_first()
            }
