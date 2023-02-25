import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table schema
table = dynamodb.create_table(
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'year',
            'KeyType': 'HASH'  # Partition key
        },
        {
            'AttributeName': 'title',
            'KeyType': 'RANGE'  # Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'year',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the table to be created
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')

# Print the table details
print("Table status:", table.table_status)

# Define the items to be added to the table
movies = [
    {'year': 2017, 'title': 'Bahubali 2 : The Conclusion'},
    {'year': 2018, 'title': 'K.G.F'},
    {'year': 2022, 'title': 'K.G.F Chapter 2'},
    {'year': 2017, 'title': 'Vikram Vedha'},
    {'year': 2019, 'title': 'Asuran'},
    {'year': 2018, 'title': 'Naa Peru Surya'},
    {'year': 2021, 'title': 'Jai Bhim'},
    {'year': 2021, 'title': 'Drishyam 2'},
    {'year': 2021, 'title': 'Pushpa'},
    {'year': 2021, 'title': 'Master'}
]

# Add the items to the table
for movie in movies:
    table.put_item(Item=movie)

# Scan the table and print the items
response = table.scan()
items = response['Items']
print("\n".join([str(item) for item in items]))


# Query the table and remove an item
table.delete_item(
    Key={
        'title': 'Pushpa'
    }
)

# Create a new table for games
new_table_name = 'Games'
new_table = dynamodb.create_table(
    TableName=new_table_name,
    KeySchema=[
        {
            'AttributeName': 'title',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait for the new table to be created
new_table.meta

