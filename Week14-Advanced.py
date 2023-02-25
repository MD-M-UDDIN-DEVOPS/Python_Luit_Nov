import boto3

# Create a DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table name
table_name = 'Movies'

# Get a handle to the table
table = dynamodb.Table(table_name)

# Query the table for items with a year greater than or equal to 2017
response = table.query(
    KeyConditionExpression=boto3.dynamodb.conditions.Key('year').gte(2017)
)

# Print the items returned by the query
items = response['Items']
print("Items with year >= 2021:")
print("\n".join([str(item) for item in items]))

# Remove an item from the table
table.delete_item(
    Key={
        'year': 2017,
        'title': 'Vikram Vedha'
    }
)

# Define the schema for a new table
new_table_name = 'Actors'
new_table = dynamodb.create_table(
    TableName=new_table_name,
    KeySchema=[
        {
            'AttributeName': 'last_name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'first_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'first_name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 2,
        'WriteCapacityUnits': 2
    }
)

# Wait for the table to be created
new_table.meta.client.get_waiter('table_exists').wait(TableName=new_table_name)

# Print the status of the new table
print("New table status:", new_table.table_status)

# Delete the new table
new_table.delete()

# Wait for the table to be deleted
new_table.meta.client.get_waiter('table_not_exists').wait(TableName=new_table_name)

# Print a message indicating the new table has been deleted
print("Table {} has been deleted.".format(new_table_name))
