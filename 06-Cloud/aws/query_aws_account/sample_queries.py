import json
import boto3

def list_ec2_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Call EC2 to retrieve instance information
    response = ec2.describe_instances()
    print("************* List instances *******************")

    # Extract and display information about the instances
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_info = {
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'No Public IP')
            }
            instances.append(instance_info)

    return instances

def list_vpc():
    vpc = boto3.client("ec2")
    response = vpc.describe_vpcs()
    return response

if __name__ == '__main__':
    # List and print EC2 instances
    ec2_instances = list_ec2_instances()
    for instance in ec2_instances:
        print(instance)
    print(json.dumps(list_vpc(), indent=4))