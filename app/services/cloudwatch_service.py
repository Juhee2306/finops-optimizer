import boto3
from datetime import datetime, timedelta, timezone


class CloudWatchService:
    def __init__(self, region_name="ap-south-1"):
        self.cloudwatch = boto3.client(
            "cloudwatch",
            region_name=region_name
        )

    def get_average_cpu_utilization(self, instance_id):
        end_time = datetime.now(timezone.utc)
        start_time = end_time - timedelta(days=7)

        response = self.cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[
                {
                    "Name": "InstanceId",
                    "Value": instance_id
                }
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=3600,
            Statistics=["Average"]
        )
        print("\n========== CloudWatch Response ==========")
        print(response)
        print("=========================================\n")

        datapoints = response["Datapoints"]

        if not datapoints:
            return None

        avg_cpu = sum(
            point["Average"]
            for point in datapoints
        ) / len(datapoints)

        return round(avg_cpu, 2)
