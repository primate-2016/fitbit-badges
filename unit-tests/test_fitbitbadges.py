import pytest
from fitbitbadges import handler
from moto import mock_dynamodb
import boto3

@pytest.fixture()
def noto_boto():
    @mock_dynamodb
    def dynamo_boto_resource():
        dynamo_client = boto3.client('dynamodb')
        dynamo_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'UserID',
                    'AttributeType': 'S'
                },
            ],
            TableName='test_FitBitData',
            KeySchema=[
                {
                    'AttributeName': 'UserID',
                    'KeyType': 'HASH'|'RANGE'
                },
            ],
            LocalSecondaryIndexes=[
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    }
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'string',
                    'KeySchema': [
                        {
                            'AttributeName': 'string',
                            'KeyType': 'HASH'|'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'|'KEYS_ONLY'|'INCLUDE',
                        'NonKeyAttributes': [
                            'string',
                        ]
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 123,
                        'WriteCapacityUnits': 123
                    }
                },
            ],
            BillingMode='PROVISIONED'|'PAY_PER_REQUEST',
            ProvisionedThroughput={
                'ReadCapacityUnits': 123,
                'WriteCapacityUnits': 123
            },
            StreamSpecification={
                'StreamEnabled': True|False,
                'StreamViewType': 'NEW_IMAGE'|'OLD_IMAGE'|'NEW_AND_OLD_IMAGES'|'KEYS_ONLY'
            },
            SSESpecification={
                'Enabled': True|False,
                'SSEType': 'AES256'|'KMS',
                'KMSMasterKeyId': 'string'
            }
        )

def test_handler():

    event = {"Records":[{"accessToken":"eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMjdQRzQiLCJzdWIiOiIzWUxKNlgiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE1NTQ2NTQ4MTQsImlhdCI6MTU1MzQyNTg5N30.SXHzHpozo8p76txoud_2JpXhVZ1FPM4-Wu9bg89pxeQ","expiresIn":"2592000","accountUserId":"3YLJ6X"}]}
    context = 'thing'
    test_output = handler(event, context)
    assert test_output == 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMjdQRzQiLCJzdWIiOiIzWUxKNlgiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyYWN0IHJwcm8iLCJleHAiOjE1NTQ2NTQ4MTQsImlhdCI6MTU1MzQyNTg5N30.SXHzHpozo8p76txoud_2JpXhVZ1FPM4-Wu9bg89pxeQ'