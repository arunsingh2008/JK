

#!/bin/bash

# Choose RDS instance type
INSTANCE_TYPE='db.t3.micro'

# Configure RDS instance
DB_NAME='mydatabase'
DB_USER='admin'
DB_PASSWORD='password'
DB_PORT='5432'

# Launch RDS instance
aws rds create-db-instance \
    --db-instance-identifier mydbinstance \
    --db-instance-class $INSTANCE_TYPE \
    --engine postgres \
    --allocated-storage 20 \
    --db-name $DB_NAME \
    --master-username $DB_USER \
    --master-user-password $DB_PASSWORD \
    --port $DB_PORT

# Note: Ensure you have the AWS CLI installed and configured before running this script.
# It might take a few minutes for the RDS instance to become available.

echo 'RDS instance is being created. This may take a few minutes...'


