import boto3

lastEvalKeyLabel = "LastEvaluatedKey"
itemsLabel = "Items"

dynamoDB = "dynamodb"
region = "eu-west-1"

tableName = "USERS-DEV"


def scan_all(table):

    lastEvaluatedKey = None

    while True:

        scanResp = table.scan() if not lastEvaluatedKey \
            else table.scan(ExclusiveStartKey=lastEvaluatedKey)

        items = scanResp[itemsLabel]
        if not items:
            print("No more items to process")
            break

        print("Scan fetched {0} items".format(len(items)))

        for item in items:
            yield item

        if lastEvalKeyLabel in scanResp:
            lastEvaluatedKey = scanResp[lastEvalKeyLabel]
        else:
            print("No more items to process")
            break

    print("End of scanning")


if __name__ == "__main__":

    dynamoDB = boto3.resource(dynamoDB, region_name=region)
    table = dynamoDB.Table(tableName)

    count = 0
    for elem in scan_all(table):
        count += 1

    print("Items processed: {0}".format(count))


# Last increase time    ...
# Storage size (in bytes) 1.85 MB
# Item count  9,894
# Region  EU West (Ireland)
# Amazon Resource Name (ARN)  arn:aws:dynamodb:eu-west-1:...


# $ python table_scan.py
# Scan fetched 5386 items
# Scan fetched 4508 items
# No more items to process
# End of scanning
# Items processed: 9894
