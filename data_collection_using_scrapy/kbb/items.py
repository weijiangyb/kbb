import scrapy
class KbbItem(scrapy.Item):

    listingTitle = scrapy.Field()
    Car_Type = scrapy.Field()
    body_code = scrapy.Field()
    car_id = scrapy.Field()
    car_year = scrapy.Field()
    color = scrapy.Field()
    fuelEconomy_city = scrapy.Field()
    fuelEconomy_hwy = scrapy.Field()
    listingPriorityType = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    odometer = scrapy.Field()
    make = scrapy.Field()
    price = scrapy.Field()
    trim = scrapy.Field()
    vin = scrapy.Field()
    driveType = scrapy.Field()
    
    engine = scrapy.Field()
    engine_litter = scrapy.Field()
    engine_cylinder = scrapy.Field()
    engine_gas = scrapy.Field()
    
    interiorSeats = scrapy.Field()
    
    transmission = scrapy.Field()
    
    vhrPreview = scrapy.Field()
    vhrPreview_accidents = scrapy.Field()
    vhrPreview_salvage = scrapy.Field()
    vhrPreview_damage = scrapy.Field()
    vhrPreview_owner = scrapy.Field()
    
        
    dealer_id = scrapy.Field()
    
    owners_name = scrapy.Field()
    owners_address = scrapy.Field()
    owners_city = scrapy.Field()
    owners_state = scrapy.Field()
    owners_zip = scrapy.Field()
    owners_rating = scrapy.Field()
    
    owners_rating_count = scrapy.Field()
    owners_rating_value = scrapy.Field()
