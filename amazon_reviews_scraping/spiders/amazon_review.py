# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_reviews'
    allowed_domains = ['amazon.es']
    myBaseUrl = 'https://www.amazon.es/Xiaomi-Smart-Band-actividad-frecuencia/product-reviews/B07SNG23JW/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
    #myBaseUrl = 'https://www.amazon.es/Exprimidor-eléctrico-antipolvo-ZitrusEasy-Basic/product-reviews/B072VQBBQN/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber='
    start_urls = []

    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))

    # Defining a Scrapy parser
    def parse(self, response):
        data = response.css('#cm_cr-review_list')

        # Collecting product star ratings
        star_rating = data.css('.review-rating')
             
        # Collecting user reviews
        comments = data.css('.review-text')
        count = 0
             
        # Combining the results
        for review in star_rating:
            yield{'stars': ''.join(review.xpath('.//text()').extract()),
                  'comment': ''.join(comments[count].xpath(".//text()").extract())
                 }
            count = count + 1
