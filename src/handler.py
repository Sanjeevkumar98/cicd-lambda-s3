def lambda_handler(event, context):
    print(f"Event: {event}")
    
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
