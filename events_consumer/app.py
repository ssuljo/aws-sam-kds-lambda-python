import base64
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def decode_record(record: bytes) -> dict:
    string_data = base64.b64decode(record).decode('utf-8')
    return json.loads(string_data)

def lambda_handler(event, context):
    logger.info(f"Events Consumer Handler Invoked with Records {event['Records'][:3]}")
    for record in event['Records']:
        try:
            event = decode_record(record['kinesis']['data'])
            logger.info({
                'message':'Processed event record',
                'event': event
            })
        except Exception as e:
            logger.error({
                'error':'failed-decoding-record',
                'exception': str(e),
                'record':record
            })
            raise e