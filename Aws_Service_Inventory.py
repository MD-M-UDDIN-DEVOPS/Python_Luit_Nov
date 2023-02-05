
#!/usr/bin/env python3.7.


# I will be creating a list of AWS services and populating it into an empty list

# Create an empty list to store AWS services
aws_services = []
print(aws_services)

# Add some AWS services to the list
aws_services.append("S3")
aws_services.append("Lambda")
aws_services.append("EC2")
aws_services.append("DynamoDB")
aws_services.append("API")
aws_services.append("EFS")
aws_services.append("Cloud9")
aws_services.append("RDS")

# Print the list and its length
print("AWS Services: ", aws_services)
print("Length: ", len(aws_services))

# Remove two specific services from the list
aws_services.remove("S3")
aws_services.remove("DynamoDB")

# Print the new list and its length
print("Updated AWS Services: ", aws_services)
print("New Length: ", len(aws_services))