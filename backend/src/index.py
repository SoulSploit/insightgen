import json
import os
import boto3
import logging
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

# Initialize DynamoDB resource and logger
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Environment variables for configuration
MAX_ITEMS = int(os.environ.get('MAX_ITEMS', 1000))  # Max number of items to retrieve
PROJECTION_EXPRESSION = os.environ.get('PROJECTION_EXPRESSION', None)  # Optional attribute projection

def scan_table(scan_kwargs):
    """Perform a scan operation with retries."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = table.scan(**scan_kwargs)
            return response
        except ClientError as e:
            if attempt < max_retries - 1:
                logger.warning(f"Retrying scan operation: attempt {attempt + 1}. Error: {e}")
            else:
                logger.error(f"Scan operation failed after {max_retries} attempts. Error: {e}")
                raise
        except Exception as e:
            logger.error(f"Unexpected error during scan operation: {str(e)}")
            raise

def handler(event, context):
    scan_kwargs = {}
    if PROJECTION_EXPRESSION:
        scan_kwargs['ProjectionExpression'] = PROJECTION_EXPRESSION
    
    data = []
    last_evaluated_key = None
    
    try:
        while True:
            if last_evaluated_key:
                scan_kwargs['ExclusiveStartKey'] = last_evaluated_key
            
            response = scan_table(scan_kwargs)
            items = response.get('Items', [])
            data.extend(items)
            
            if len(data) >= MAX_ITEMS or 'LastEvaluatedKey' not in response:
                break
            
            last_evaluated_key = response['LastEvaluatedKey']
        
        # Trim data to MAX_ITEMS if necessary
        if len(data) > MAX_ITEMS:
            data = data[:MAX_ITEMS]
        
        return {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except ClientError as e:
        logger.error(f"ClientError: {e.response['Error']['Message']}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
    
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'}),
            'headers': {
                'Content-Type': 'application/json'
            }
        }
