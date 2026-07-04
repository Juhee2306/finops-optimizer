import boto3


class AWSClient:

    def __init__(self, region_name="ap-south-1"):
        self.ec2 = boto3.client("ec2", region_name=region_name)

    def get_ec2_instances(self):
        response = self.ec2.describe_instances()

        instances = []

        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "instance_id": instance["InstanceId"],
                    "instance_type": instance["InstanceType"],
                    "state": instance["State"]["Name"],
                    "tags": instance.get("Tags", [])
                })

        return instances

    def get_ebs_volumes(self):
        response = self.ec2.describe_volumes()

        volumes = []

        for volume in response["Volumes"]:
            volumes.append({
                "volume_id": volume["VolumeId"],
                "state": volume["State"],
                "attached": len(volume["Attachments"]) > 0
            })

        return volumes
