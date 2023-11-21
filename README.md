# kbb_scrapy
web-scrape KBB used cars data


## Objective:
1. Using Scrapy library to scrpape used cars data from KBB.com#. Scraped data will be used to build prediction models for used cars.

2. Build prediction models

## The Scrapy documentation:
https://docs.scrapy.org/en/latest/index.html

## KBB Scraper python scripts:
https://github.com/weijiangyb/kelley_blue_book_project/tree/main/data_collection_using_scrapy/kbb

## Data discriptions:

Car_Type: Certified or Used

body_code: cnv, cpe, hch, pic, sed, suv, wag

car_id: Unique identification on KBB for listed cars

car_year: car year

color: exterior color

dealer_id: Unique identification on KBB for listed cars for dealers

driveType: 2 wheel drive - front, 2 wheel drive - rear, 4 wheel drive, 4 wheel drive - front wheel default, 4 wheel drive - rear wheel default, All wheel drive

engine: combination of "engine_litter", "engine_cylinder" and "engine_gas"

engine_cylinder: cylinder type

engine_gas:

engine_litter:

fuelEconomy_city: MPG on city

fuelEconomy_hwy: MPG on highway

interiorSeats: interior seats type

listingPriorityType: FEATURED, PREMIUM or STANDARD

listingTitle: listing title of cars

make: car make

model: car model

odometer: odometer value at the time of listing on KBB

owners_address: dealers/owners address

owners_city: dealers/owners city

owners_name: Name of dealers

owners_rating_count: dealears' rating counts on KBB

owners_rating_value: dealer ratings on KBB

owners_state: dealers/owners state

owners_zip: dealers/owners zip code

price: price of listed cars

transmission: transmission types

trim: trim types

vhrPreview:

vhrPreview_accidents: Whether accidents were reported

vhrPreview_damage: Wheter flood whater damages were reported

vhrPreview_owner: One-owner or not one-owner

vhrPreview_salvage: Have salvage title or no salvage title

vin: VIN code

## Cleaned data set:
https://github.com/weijiangyb/kelley_blue_book_project/blob/main/kbb6.csv

Data columns (total 22 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   Car_Type              24128 non-null  object 
 1   body_code             23668 non-null  object 
 2   car_year              24128 non-null  int64  
 3   driveType             24128 non-null  object 
 4   engine_cylinder       24063 non-null  object 
 5   engine_gas            24128 non-null  object 
 6   engine_litter         24024 non-null  object 
 7   fuelEconomy_city      24128 non-null  int64  
 8   fuelEconomy_hwy       24128 non-null  int64  
 9   listingPriorityType   24128 non-null  object 
 10  make                  24128 non-null  object 
 11  model                 24128 non-null  object 
 12  odometer              24128 non-null  int64  
 13  owners_rating_count   24128 non-null  int64  
 14  owners_rating_value   24128 non-null  float64
 15  owners_state          24128 non-null  object 
 16  price                 24128 non-null  int64  
 17  transmission          24128 non-null  object 
 18  vhrPreview_accidents  24126 non-null  object 
 19  vhrPreview_damage     24128 non-null  object 
 20  vhrPreview_owner      24012 non-null  object 
 21  vhrPreview_salvage    24128 non-null  object 

## Exploratory Data Analysis:

#### Workbook: 
https://github.com/weijiangyb/kelley_blue_book_project/blob/main/1.kbb_EDA.ipynb

#### Top 30 makers - Tree map

![alt text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/73fdf8b7-0da8-47d1-bf52-6f6c3911f2e9)

#### Count plot by make
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/cc8d2526-fc90-4c07-96a5-73ddc6bf4927)


#### Count plot by body type
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/638057ec-b8ea-41e6-86b1-13eb961c7526)

#### Count plot by car year
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/d7e96bc1-0bd2-49ed-a319-8614e1befd18)

#### Average price by make
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/515af648-fcd6-4b04-8196-9b832e04d423)

#### Price histogram
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/f988b859-9436-4ba6-8a2a-e3e3a765db14)

#### Listed car count plot by state
![alt_text](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/330e8872-5c38-497e-82aa-be44480b474c)


## Feature engineering
Categorical values such as Car Type or Body type are engoded in order to feed regression models

## Models tuning and comparison

#### Workbook:
https://github.com/weijiangyb/kelley_blue_book_project/blob/main/2.kbb_price_prediction.ipynb

#### Feature importances from Random Forest model
Odometer, drive type, engine litter, car year, and fuel economy (Mile per Gallon) are marked as top 5 variables that affect car prices. This is finding is very intuitive as most seller use these indicators from benchmarks to decide list prices.

![image](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/7196b989-fd64-406a-b139-cd037defbec0)

#### RMSE
Root Mean Square Error (RMSE) is used to compare 8 models performance in test dataset.

<img width="625" alt="Screenshot 2023-11-20 at 11 40 21 PM" src="https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/977367ee-d91b-4aea-af6e-1913987dbf89">

![image](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/c7b2a13f-0fe6-4e7c-a0e3-4b6a949a680b)


#### R-squred
The value of R-squared lies between 0 to 1. Thie higher the value the the lower the difference between predicted value and actual value. Tree based models performed better than others.
![image](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/a6f3f921-cb25-4519-840e-4efc6097c7a4)


#### Car price prediction with Random Forest model

![image](https://github.com/weijiangyb/kelley_blue_book_project/assets/49177890/a81c9928-2a5c-4c5d-a6fb-8c5587f841e6)
