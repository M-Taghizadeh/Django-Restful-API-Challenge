import boto3.exceptions
import botocore


def create_table():

    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.create_table(
        TableName="Device_DB",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 2},
    )
    return table


if __name__ == "__main__":
    try:
        my_table = create_table()
        my_table.meta.client.get_waiter("table_exists").wait(TableName="Device_DB")
        print("Table was created successfully.")

    except botocore.exceptions.ClientError as error:
        if error.response["Error"]["Code"] == "ResourceInUseException":
            print("Error: This table already exists. please change the table name.")
        else:
            raise error
