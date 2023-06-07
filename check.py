import json
import requests

answer = []
def getStoreId(latitude, longitude):
    locations_url = "https://api.zepto.co.in/api/v1/config/layout/"
    locations_querystring = {
        "latitude": latitude,
        "longitude": longitude,
        "page_type": "HOME",
        "version": "v2"
    }
    locations_headers = {
        "accept": "application/json",
        "access-control-allow-credentials": "true",
        "x-requested-with": "XMLHttpRequest",
        "sessionid": "383f70bd0100e873e8288021b85ccd20",
        "appversion": "23.5.2",
        "deviceuid": "2326fd1ede6242e0",
        "platform": "android",
        "systemversion": "10",
        "source": "PLAY_STORE",
        "device_model": "Genymotion 'Phone' version",
        "device_brand": "google",
        "compatible_components": "SAMPLING_FOR_COUPON_MOV_ENABLED,CONVENIENCE_FEE,RAIN_FEE,EXTERNAL_COUPONS,STANDSTILL,BUNDLE,MULTI_SELLER_ENABLED,PIP_V1,ROLLUPS,SCHEDULED_DELIVERY,SAMPLING_ENABLED,ETA_NORMAL_WITH_149_DELIVERY,ROLLUPS_UOM,SAMPLING_V2,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SCHEDULED_DELIVERY_M2,RECOMMENDED_COUPON_WIDGET,SMART_BASKET,NZS_CAMPAIGN_COMPONENT,ETA_NORMAL_WITH_199_DELIVERY,NEW_FEE_STRUCTURE,PHARMA_ENABLED,REWARDS_WIDGET_MISSION_V2",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXJzaW9uIjoxLCJzdWIiOiJkMDYzNTRlMy03ZjM1LTRlNGItYjM4YS0zYzE5YWRjNmY3MjMiLCJpYXQiOjE2ODU5NjM3MzMsImV4cCI6MTY4NjA1MDEzM30.VIPeKPHEBvYZaQZnCQNT2TX9bX5maVx4spfdNoUEZ-_dMDtW2CE32uxfHKjjt8e_I1DHlXemnCOaYBRliZLg2A",
        "storeid": "00db393a-dc6a-477d-9c36-f909a1632844",
        "isinternaluser": "false",
        "requestid": "fbbd0cde7f35db5c6305178fc63d856b",
        "bundleversion": "v1394",
        "host": "api.zepto.co.in",
        "connection": "Keep-Alive",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.2",
        "if-modified-since": "Mon, 05 Jun 2023 11:16:21 GMT"
    }

    locations_response = requests.get(locations_url, headers=locations_headers, params=locations_querystring)
    locations_response_json = locations_response.json()

    return locations_response_json['storeServiceableResponse']['storeId']


def getCategories(store_id):
    
    categories_url = "https://api.zepto.co.in/api/v1/inventory/catalogue/categories/"
    categories_querystring = { "store_id": store_id}
    categories_headers = {
        "accept": "application/json",
        "access-control-allow-credentials": "true",
        "x-requested-with": "XMLHttpRequest",
        "sessionid": "9d597cbfb7a3aba565d0a0ca89d2dac0",
        "appversion": "23.5.2",
        "deviceuid": "2326fd1ede6242e0",
        "platform": "android",
        "systemversion": "10",
        "source": "PLAY_STORE",
        "device_model": "Genymotion 'Phone' version",
        "device_brand": "google",
        "compatible_components": "SAMPLING_FOR_COUPON_MOV_ENABLED,CONVENIENCE_FEE,RAIN_FEE,EXTERNAL_COUPONS,STANDSTILL,BUNDLE,MULTI_SELLER_ENABLED,PIP_V1,ROLLUPS,SCHEDULED_DELIVERY,SAMPLING_ENABLED,ETA_NORMAL_WITH_149_DELIVERY,ROLLUPS_UOM,SAMPLING_V2,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SCHEDULED_DELIVERY_M2,RECOMMENDED_COUPON_WIDGET,SMART_BASKET,NZS_CAMPAIGN_COMPONENT,ETA_NORMAL_WITH_199_DELIVERY,NEW_FEE_STRUCTURE,PHARMA_ENABLED,REWARDS_WIDGET_MISSION_V2",
        "storeid": "b1403534-cd6b-49d0-a7cd-ce20e6497768",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXJzaW9uIjoxLCJzdWIiOiJkMDYzNTRlMy03ZjM1LTRlNGItYjM4YS0zYzE5YWRjNmY3MjMiLCJpYXQiOjE2ODU5NjM3MzMsImV4cCI6MTY4NjA1MDEzM30.VIPeKPHEBvYZaQZnCQNT2TX9bX5maVx4spfdNoUEZ-_dMDtW2CE32uxfHKjjt8e_I1DHlXemnCOaYBRliZLg2A",
        "isinternaluser": "false",
        "requestid": "6eb77b194b9181cc8df2f86a0955e7b5",
        "bundleversion": "v1394",
        "host": "api.zepto.co.in",
        "connection": "Keep-Alive",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.2"
    }

    categories_response = requests.get(categories_url, headers=categories_headers, params=categories_querystring).json()['categories']
    categories = []

    for category in categories_response:
        for subcategory in category['availableSubcategories']:
            subcategory_data = {
                'name': subcategory['name'],
                'id': subcategory['id']
            }
            categories.append(subcategory_data)

    return categories


def getProducts(store_id, categories):

    products_url = "https://api.zepto.co.in/api/v2/inventory/catalogue/store-products/"
    products_headers = {
        "accept": "application/json",
        "access-control-allow-credentials": "true",
        "x-requested-with": "XMLHttpRequest",
        "sessionid": "9d597cbfb7a3aba565d0a0ca89d2dac0",
        "appversion": "23.5.2",
        "deviceuid": "2326fd1ede6242e0",
        "platform": "android",
        "systemversion": "10",
        "source": "PLAY_STORE",
        "device_model": "Genymotion 'Phone' version",
        "device_brand": "google",
        "compatible_components": "SAMPLING_FOR_COUPON_MOV_ENABLED,CONVENIENCE_FEE,RAIN_FEE,EXTERNAL_COUPONS,STANDSTILL,BUNDLE,MULTI_SELLER_ENABLED,PIP_V1,ROLLUPS,SCHEDULED_DELIVERY,SAMPLING_ENABLED,ETA_NORMAL_WITH_149_DELIVERY,ROLLUPS_UOM,SAMPLING_V2,RE_PROMISE_ETA_ORDER_SCREEN_ENABLED,SCHEDULED_DELIVERY_M2,RECOMMENDED_COUPON_WIDGET,SMART_BASKET,NZS_CAMPAIGN_COMPONENT,ETA_NORMAL_WITH_199_DELIVERY,NEW_FEE_STRUCTURE,PHARMA_ENABLED,REWARDS_WIDGET_MISSION_V2",
        "storeid": "00db393a-dc6a-477d-9c36-f909a1632844",
        "authorization": "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXJzaW9uIjoxLCJzdWIiOiJkMDYzNTRlMy03ZjM1LTRlNGItYjM4YS0zYzE5YWRjNmY3MjMiLCJpYXQiOjE2ODU5NjM3MzMsImV4cCI6MTY4NjA1MDEzM30.VIPeKPHEBvYZaQZnCQNT2TX9bX5maVx4spfdNoUEZ-_dMDtW2CE32uxfHKjjt8e_I1DHlXemnCOaYBRliZLg2A",
        "isinternaluser": "false",
        "requestid": "ff7a37e623221946591e6e4f45136270",
        "bundleversion": "v1394",
        "host": "api.zepto.co.in",
        "connection": "Keep-Alive",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.2",
        "if-modified-since": "Tue, 06 Jun 2023 05:25:53 GMT"
    }

    for subcategory_data in categories:
        products_querystring = {
            "store_id": store_id,
            "subcategory_id": subcategory_data['id'],
            "preview_mode": "true",
            "page_number": "1"
        }
        products_response = requests.get(products_url, headers=products_headers, params=products_querystring)
        products_response_json = products_response.json()  
        products_response_json['subcategory_name'] = subcategory_data['name']
        products_response_json['subcategory_id'] = subcategory_data['id']
        answer.append(products_response_json)


def getAnswer(latitude, longitude):
    store_id = getStoreId(latitude, longitude)
    categories = getCategories(store_id)
    getProducts(store_id, categories)


with open('geoLocationGeneration.geojson') as f:
    data = json.load(f)

coordinates = data['features'][0]['geometry']['coordinates']
coordinates_array = []

for coordinate in coordinates[0]:
    latitude = coordinate[0]
    longitude = coordinate[1]
    coordinates_array.append((latitude, longitude))


for pair in coordinates_array:
    latitude, longitude = pair
    getAnswer(latitude, longitude)


with open('Page_1_products.json', 'w') as outfile:
    json.dump(answer, outfile)










