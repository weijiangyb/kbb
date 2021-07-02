from scrapy import Spider, Request
from kbb.items import KbbItem
import re
import json
class kbbSpider(Spider):
    #name: an attribute specifying a unique name to identify the spider
    name = "kbb_spider"
    
    #start_urls: an attribute listing the URLs the spider will start from
    allowed_domains = ['www.kbb.com']
    
    #allowed_urls: the main domain of the website you want to scrape
    start_urls = ['https://www.kbb.com/cars-for-sale/cars/used?p=1&searchRadius=500&color=&numRecords=100']
    
    #parse(): a method of the spider responsible for processing a Response object downloaded from the URL and returning scraped data (as well as more URLs to follow, if necessary)

    def parse(self, response):
        # text = response.xpath('//*[@id="listingsContainer"]//span[@class="page-numbers"]/text()').extract()[1]
        result_pages = ['https://www.kbb.com/cars-for-sale/cars/used?p={}&searchRadius=500&color={}&numRecords=100'.format(x,y) for x in range(1, 300) for y in ['beige', 'black', 'blue', 'brown', 'burgundy','charcoal','gold','gray','green','offwhite','orange','pink','purple','red','silver','tan', 'turquoise','white','yellow']]
        for url in result_pages:
            yield Request(url=url, callback=self.parse_result_page)

    def parse_result_page(self, response):
        products = response.xpath('//div[@data-qaid="cntnr-listings"]//a[@rel="nofollow"]/@href').extract()
        product_urls = ['https://www.kbb.com' + x for x in products]
        for url in product_urls:
            yield Request(url=url, callback=self.parse_product_page)

    def parse_product_page(self, response):
        item = KbbItem()
        item['listingTitle'] = response.xpath('//div[@data-qaid="cntnr-vehicle-title"]//h1[@class="text-bold text-size-400 text-size-sm-700"]/text()').extract()[0]

        script = response.xpath('//script/text()').extract()[6].replace('window.__BONNET_DATA__=','')
        
        item['Car_Type'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['Car_Type']
        item['body_code'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['body_code'][0]
        
        # car_id 
        car_id = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['car_id']
        item['car_id'] = car_id
        item['car_year'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['car_year']
        item['color'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['color'][0]
        
        fuelEconomy = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['fuelEconomy']
        item['fuelEconomy_city'] = int(fuelEconomy[0].split()[0])
        item['fuelEconomy_hwy'] = int(fuelEconomy[1].split()[0])        
        item['listingPriorityType'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['listingPriorityType']
        item['make'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['make'][0]
        item['model'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['model'][0]
        item['odometer'] = int(json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['odometer'].replace(',','').replace(' mi',''))        
        item['make'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['make']
        item['price'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['price']
        item['trim'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['trim']
        item['vin'] = json.loads(script)['initialState']['birf']['pageData']['page']['vehicle']['vin']
        
        item['driveType'] = json.loads(script)['initialState']['inventory'][str(car_id)]['specifications']['driveType']['value']
        
        # engine
        engine = json.loads(script)['initialState']['inventory'][str(car_id)]['specifications']['engineDescription']['value']
        item['engine'] = engine
        item['engine_litter'] = engine.split()[0]
        item['engine_cylinder'] = engine.split()[1]
        item['engine_gas'] = ' '.join(engine.split()[2:]).replace(',',' ')
        
        # interiorSeats
        item['interiorSeats'] = json.loads(script)['initialState']['inventory'][str(car_id)]['specifications']['interiorSeats']['value']

        # transmission
        item['transmission'] = json.loads(script)['initialState']['inventory'][str(car_id)]['specifications']['transmission']['value']
        
        # vhrPreview
        vhrPreview = json.loads(script)['initialState']['inventory'][str(car_id)]['vhrPreview']
        item['vhrPreview'] = vhrPreview
        for i in vhrPreview:
            if 'ACCIDENTS' in i:
                item['vhrPreview_accidents'] = i
            elif 'SALVAGE' in i:
                item['vhrPreview_salvage'] = i
            elif 'DAMAGE' in i:
                item['vhrPreview_damage'] = i
            elif 'OWNER' in i:
                item['vhrPreview_owner'] = i
        
        # dealer
        dealer_id = json.loads(script)['initialState']['birf']['pageData']['page']['owner']['dealer_id']
        item['dealer_id'] = str(dealer_id)

        item['owners_name'] = json.loads(script)['initialState']['owners'][str(dealer_id)]['name']    
        item['owners_address'] = json.loads(script)['initialState']['owners'][str(dealer_id)]['location']['address']['address1']
        item['owners_city'] = json.loads(script)['initialState']['owners'][str(dealer_id)]['location']['address']['city']
        item['owners_state'] = json.loads(script)['initialState']['owners'][str(dealer_id)]['location']['address']['state']
        item['owners_zip'] = json.loads(script)['initialState']['owners'][str(dealer_id)]['location']['address']['zip']
        
        owners_rating = json.loads(script)['initialState']['owners'][str(dealer_id)]['rating']
        item['owners_rating_count'] = owners_rating
        
        if 'count' in owners_rating:
            item['owners_rating_count'] = owners_rating['count']
            item['owners_rating_value'] = owners_rating['value']
        else:            
            item['owners_rating_count'] = 0
            item['owners_rating_value'] = 0

        
        yield item
