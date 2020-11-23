from urllib.request import urlopen
from contextlib import closing
import json
 
def lambda_handler(event, context):
    jsonRequestInput = json.loads(event['body'])
    stockTicker = jsonRequestInput['stockTicker']
    print(stockTicker)
    with closing(urlopen("https://financialmodelingprep.com/api/v3/profile/" + stockTicker + "?apikey=REDACTED")) as responseData:
        jsonData = responseData.read().decode("utf-8")
        deserialisedData = json.loads(jsonData)
        price = deserialisedData[0]['price']
        volAvg = deserialisedData[0]['volAvg']
        mktCap = deserialisedData[0]['mktCap']
        lastDiv = deserialisedData[0]['lastDiv']
        priceRange = deserialisedData[0]['range']
        priceLow = priceRange.split("-")[0]
        priceHigh = priceRange.split("-")[1]
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
            "priceHigh": priceHigh
        }),
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Allow" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Headers" : "*"
        }
    }
