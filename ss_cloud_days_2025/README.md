Steps to implemente k8sgpt integrated with AmazonBedrock: https://aws.amazon.com/blogs/machine-learning/use-k8sgpt-and-amazon-bedrock-for-simplified-kubernetes-cluster-maintenance/

Note: Those steps could pottentially fail, since some changes have been implemented since then.

Most important change is that now it's required to configure inference profile to have access to BedRock Models.
IAM permissions are required for the inference profile as well. Read the file instance_profile_creation.sh to check how to create the inference profile

