from urllib.request import urlopen
from contextlib import closing
import json
 
def lambda_handler(event, context):
    jsonRequestInput = json.loads(event['body'])
    stockTicker = jsonRequestInput['stockTicker']
    print(stockTicker)
    with closing(urlopen("https://financialmodelingprep.com/api/v3/profile/" + stockTicker + "?apikey=aa34ce680f642e24c3f251bb4038c1dd")) as responseData:
        jsonData = responseData.read().decode("utf-8")
        deserializedData = json.loads(jsonData)
        price = deserializedData[0]['price']
        volAvg = deserializedData[0]['volAvg']
        mktCap = deserializedData[0]['mktCap']
        lastDiv = deserializedData[0]['lastDiv']
        priceRange = deserializedData[0]['range']
        priceLow = priceRange.split("-")[0]
        priceHigh = priceRange.split("-")[1]
        companyName = deserializedData[0]['companyName']
        industry = deserializedData[0]['industry']
        website = deserializedData[0]['website']
        description = deserializedData[0]['description']
        ceo = deserializedData[0]['ceo']
        sector = deserializedData[0]['sector']
        country = deserializedData[0]['country']
        employees = deserializedData[0]['fullTimeEmployees']
        phone = deserializedData[0]['phone']
        address = deserializedData[0]['address']
        city = deserializedData[0]['city']
        state = deserializedData[0]['state']
        zip = deserializedData[0]['zip']
        image = deserializedData[0]['image']
        ipoDate = deserializedData[0]['ipoDate']
    return  {
        "statusCode": 200,
        "body": json.dumps({
            "stockTicker": stockTicker,
            "price": price,
            "volAvg": volAvg,
            "mktCap": mktCap,
            "lastDiv": lastDiv,
            "priceRange": priceRange,
            "priceLow": priceLow,
            "priceHigh": priceHigh,
            "companyName": companyName,
            "industry": industry,
            "website": website,
            "description": description,
            "ceo": ceo,
            "sector": sector,
            "country": country,
            "employees": employees,
            "phone": phone,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "image": image,
            "ipoDate": ipoDate
        }),
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Allow" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Headers" : "*"
        }
    }