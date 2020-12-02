import json

def lambda_handler(event, context):
    
    
    jsonRequestInput = json.loads(event['body'])
    userid = jsonRequestInput['userid']
    stock = jsonRequestInput['stock']
    
    
    
    db_stocks = getDynamoData(userid)
    db_stocks = removeDynamoStock(stock, db_stocks)
    
    
    putDynamoData(userid, db_stocks)

    
    # TODO implement
    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": "good"
        }),
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
    
def putDynamoData(userid, stocks):
    
    import boto3
    
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName='Stocks', Item={'UserId':{'S': userid},'Stock':{'S': stocks}})
    
    
def removeDynamoStock(old_stock, existing_stocks):    
    
    if(old_stock in existing_stocks):
        existing_stocks = existing_stocks.replace(old_stock, "")
        existing_stocks = existing_stocks.replace(",,", ",")
    
    if(len(existing_stocks) > 0):
        
        if(existing_stocks[0] == ","):
            existing_stocks = existing_stocks[1:]
            
        if(existing_stocks[len(existing_stocks) - 1] == ","):
            existing_stocks = existing_stocks[:len(existing_stocks) - 1]
    
    return existing_stocks