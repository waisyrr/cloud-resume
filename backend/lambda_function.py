import json
import boto3

# Connect to your DynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-counter')

def lambda_handler(event, context):
    # Atomically increment the visitor count by 1
    response = table.update_item(
        Key={'ID': 'visitors'},
        UpdateExpression='ADD view_count :inc',
        ExpressionAttributeValues={':inc': 1},
        ReturnValues='UPDATED_NEW'
    )
    
    # Return the updated count with CORS headers enabled
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Methods': 'GET,POST'
        },
        'body': json.dumps({'count': int(response['Attributes']['view_count'])})
    }