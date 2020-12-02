from urllib.request import urlopen
from contextlib import closing
import json

def lambda_handler(event, context):
    
    jsonRequestInput = json.loads(event['body'])
    userid = jsonRequestInput['userid']

    db_stocks = getDynamoData(userid)
    
    stocks_list = db_stocks.split(',')
    ret_list = []
    
    for i in range(0, len(stocks_list)):
        ret_list.append(getStockInfo(stocks_list[i]))


    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps(ret_list),
        'headers': {
            "Content-Type" : "application/json",
            "Access-Control-Allow-Origin" : "*",
            "Allow" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Methods" : "GET, OPTIONS, POST",
            "Access-Control-Allow-Headers" : "*"
        }
    }
    
    
def getDynamoData(userid):
    
    import boto3
    
    dynamodb = boto3.client('dynamodb')
    db_ret = dynamodb.get_item(TableName='Stocks', Key={'UserId':{'S': userid}})
    
    db_item = db_ret['Item']
    db_stock_item = db_item['Stock']
    db_stocks = db_stock_item['S']
    
    return db_stocks
    

def getStockInfo(ticker):
    
    with closing(urlopen("https://financialmodelingprep.com/api/v3/profile/" + ticker + "?apikey=aa34ce680f642e24c3f251bb4038c1dd")) as responseData:
        jsonData = responseData.read().decode("utf-8")
        deserialisedData = json.loads(jsonData)
        
        
        companyName = deserialisedData[0]['companyName']
        symbol = deserialisedData[0]['symbol']
        price = deserialisedData[0]['price']
        changes = deserialisedData[0]['changes']
    
    
    return {
                "companyName": companyName,
                "symbol": symbol,
                "price": price,
                "changes": changes
            }