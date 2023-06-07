import json
import jsonschema
from datetime import datetime
import pytz
from json import dump


with open('products.json', 'r') as data_file:
    data = json.load(data_file)

with open('schema.json', 'r') as schema_file:
    schema = json.load(schema_file)

null = None
false = False
true = True

products = []

for i in range(0,len(data)):
    for j in range(0,len(data[i]['storeProducts'])):
      product_data = {}
      product_data['item_id'] = data[i]['storeProducts'][j]['objectId']
      product_data['item_name'] = data[i]['storeProducts'][j]['product']['name']
      product_data['item_url'] = null
      product_data['brand_id'] = null
      product_data['category'] = [data[i]['subcategory_name']]
      product_data['category_id'] = [data[i]['subcategory_id']]
      product_data['description'] = null
      product_data['country_code'] = "IN"
      product_data['price'] = data[i]['storeProducts'][j]['mrp']
      product_data['price_unit'] = "Paisa"
      product_data['restricted_age'] = null
      product_data['image_url'] = null
      product_data['discount'] = str(data[i]['storeProducts'][j]['discountPercent'])
      product_data['discounted_price'] = data[i]['storeProducts'][j]['mrp'] - data[i]['storeProducts'][j]['discountAmount']
      product_data['location'] = "Bangalore"
      product_data['is_adult_product'] = null
      product_data['rating'] = null
      product_data['review_count'] = null
      product_data['timestamp'] = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
      product_data['is_instock'] = not data[i]['storeProducts'][j]['outOfStock']
      product_data['unit'] = data[i]['storeProducts'][j]['productVariant']['unitOfMeasure']
      product_data['sku'] = data[i]['storeProducts'][j]['objectId']
      product_data['source'] = "Zepto"
      product_data['seller_address'] = null
      product_data['seller_description'] = null
      product_data['seller_id'] = null
      product_data['seller_name'] = null
      product_data['offers'] = null

      brand_name = data[i]['storeProducts'][j]['product']['brand']
      if brand_name == '':
          brand_name = null

      product_data['brand_name'] = brand_name


      unit_price = 0
      if  data[i]['storeProducts'][j]['productVariant']['quantity']!= 0:
          unit_price = data[i]['storeProducts'][j]['mrp'] / data[i]['storeProducts'][j]['productVariant']['quantity']

      product_data['price_per_unit'] = [{
          "measurement_unit": data[i]['storeProducts'][j]['productVariant']['unitOfMeasure'],
          "unit_price": unit_price
      }]

      products.append(product_data)
      jsonschema.validate(products,schema)
      print('validated', product_data)

save_file = f"zepto_compiled_{datetime.now()}.ndjson"

with open(save_file, 'w') as outfile:
    dump(products, outfile)


