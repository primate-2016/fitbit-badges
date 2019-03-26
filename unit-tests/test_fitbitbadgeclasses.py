import pytest
from fitbitbadgeclasses import FitBitBadgesUser, BadgesList
import boto3
from botocore.exceptions import ClientError
from moto import mock_dynamodb2

table_name = 'test_FitBitData'

# example of fake, sanitised response from Fitbit API (unneeded key/value pairs from the response
# have been removed)
badge_map = { 
    'badges': [ 
        { 
            'dateTime': '2018-07-13',
            'description': '15,000 steps in a day',
            'image100px': 'https://static0.fitbit.com/images/badges_new/100px/badge_daily_steps15k.png',
            'name': 'Urban Boot (15,000 steps in a day)',
            'shortName': 'Urban Boot',
            'timesAchieved': 20,
            'value': 15000 
        },
        { 
            'dateTime': '2019-03-17',
            'description': '10,000 steps in a day',
            'image100px': 'https://static0.fitbit.com/images/badges_new/100px/badge_daily_steps10k.png',
            'name': 'Sneakers (10,000 steps in a day)',
            'shortName': 'Sneakers',
            'timesAchieved': 196,
            'value': 10000 
        },
        { 
            'dateTime': '2019-03-23',
            'description': '5,000 steps in a day',
            'image100px': 'https://static0.fitbit.com/images/badges_new/100px/badge_daily_steps5k.png',
            'name': 'Boat Shoe (5,000 steps in a day)',
            'shortName': 'Boat Shoe',
            'timesAchieved': 915,
            'value': 5000 }
        ],
    'FullName': 'John Smith'
    }

@pytest.fixture()
def moto_boto_fixture():
    @mock_dynamodb2
    def dynamo_boto_resource():
        dynamo_client = boto3.resource('dynamodb')

        # Create a fake dynamodb table in moto
        dynamo_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'UserID',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'FullName',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Badges',
                    'AttributeType': 'M'
                },
                {
                    'AttributeName': 'LastAccessed',
                    'AttributeType': 'S'
                }
            ],
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'UserID',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'FullName',
                    'KeyType': 'RANGE'
                }
            ],
            BillingMode='PAY_PER_REQUEST',
            StreamSpecification={
                'StreamEnabled': False
            },
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )

        # Write an item to the table
        table = dynamo_client.Table(table_name)
        table.put_item(
                Item={
                    'UserID': 'ABCDEF',
                    'FullName': 'John Smith',
                    'Badges': badge_map,
                    'LastAccessed': '2019-02-21'
                }
            )
        return dynamo_client
    return dynamo_boto_resource

@mock_dynamodb2
def test_canInstantiateExistingFitBitBadgesUser(moto_boto_fixture):
    moto_boto_fixture()
    dynamo_client = boto3.resource('dynamodb')
    fitbit_badges_user = FitBitBadgesUser('ABCDEF', dynamo_client, table_name)
    assert fitbit_badges_user.check_if_user_exists() == 'Yes'

@mock_dynamodb2
def test_cantFindUser(moto_boto_fixture):
    moto_boto_fixture()
    dynamo_client = boto3.resource('dynamodb')
    fitbit_badges_user = FitBitBadgesUser('XYZ123', dynamo_client, table_name)
    assert fitbit_badges_user.check_if_user_exists() == 'No'

def test_canInstantiateBadgesList():
    badges_list = BadgesList()