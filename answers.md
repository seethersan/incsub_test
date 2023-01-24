# TEST

## AWS DynamoDB

1. What is the difference between Query and Scan operations in DynamoDB?
   A Query operation retrieves data based on the primary key of the table, and it can use additional conditions to filter the data. A Scan operation retrieves all the data from a table and can then filter it using additional conditions.
2. What are projection expressions in DynamoDB?
   Projections are used to specify which attributes of an item you want to retrieve in a query or scan operation. When you use a projection expression, you are asking DynamoDB to only return specific attributes of an item, rather than all the attributes of an item.
3. How would you make items in a DynamoDB table expire after a period of time?
   Using Time-to-Live (TTL) attribute. You can set a condition on the TTL attribute that automatically removes items from the table when the timestamp is older than a certain value. Another way is to use DynamoDB Streams and Lambda function to check the timestamp and delete the item if it is expired.

## Docker

4. How would we map ports in docker using cli command?
   Using the -p or --publish option when running the docker run command. The syntax for mapping ports is -p host_port:container_port
5. What is the difference between docker stop and docker kill commands?
   The main difference between docker stop and docker kill is that docker stop gives the container a chance to shut down gracefully, while docker kill does not.

## AWS Batch

6. What are the states a job can have when submitted to an AWS Batch job queue?

   - SUBMITTED: The job has been added to the job queue and is waiting for resources to become available.
   - PENDING: The job is waiting for resources to become available.
   - RUNNABLE: The job has been assigned to a compute environment and is waiting for resources to start running.
   - STARTING: The job is starting.
   - RUNNING: The job is running.
   - SUCCEEDED: The job has completed successfully.
   - FAILED: The job has failed.

7. What are the main AWS Batch resource types used in a CloudFormation template?

- AWS::Batch::JobQueue: This resource creates a job queue.
- AWS::Batch::ComputeEnvironment: This resource creates a compute environment.
- AWS::Batch::JobDefinition: This resource creates a job definition.
- AWS::Batch::Job: This resource creates a job.

8. How would you pass named arguments with parameterized values in a Batch job definition?
   Using the parameters property of the containerProperties object in the job definition. The parameters property is a dictionary that maps the parameter names to their values.
   ´´´
   "containerProperties": {
   "parameters": {
   "my-param": "my-value"
   }
   }

´´´

## AWS Lambda

9. How can we tell at runtime whether or not a Batch job failed and has been attempted again?
   With the status field AWS.Batch.Job of the resource. If the status is FAILED, it means the job has failed. To check if a job has been attempted again, you can check the attempts field of the AWS.Batch.Job resource. Each time a job is retried, the attempts field is incremented.
10. How can we schedule execution of a Lambda function in regular time intervals?
    Using AWS CloudWatch Events that trigger a Lambda function on a schedule, for example, every 5 minutes or every day at a certain time.
11. How can we execute a Lambda function using Python and, once we do, do we have to wait for its results?
    Creating a Lambda function using the AWS Lambda management console, AWS CLI, or AWS SDKs. Once you have created a Lambda function, you can invoke it using the invoke function in the AWS SDKs or using the aws lambda invoke command in the AWS CLI. When you invoke a Lambda function, you don't have to wait for its results. The Lambda function is executed asynchronously and the results are returned in the response. If you need the results, you can use the aws lambda invoke command to get the results of the function.
