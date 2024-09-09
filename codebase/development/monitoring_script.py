

import boto3
import pprint

def monitor_elasticache(cluster_id):
    cloudwatch = boto3.client('cloudwatch')
    metrics = cloudwatch.list_metrics(Namespace='AWS/ElastiCache', MetricName='CPUUtilization', Dimensions=[{'Name': 'CacheClusterId', 'Value': cluster_id}])
    pprint.pprint(metrics)

# Example usage
# monitor_elasticache('my-cache-cluster')

