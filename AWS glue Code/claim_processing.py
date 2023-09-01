import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Create a GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# Create a Job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define source and target paths in S3
source_path = "s3://your-source-bucket/source-data/"
target_path = "s3://your-target-bucket/target-data/"

# Create a DynamicFrame from the source data
policy_source = glueContext.create_dynamic_frame.from_catalog(database="your-database", table_name="policy-table")
claim_source = glueContext.create_dynamic_frame.from_catalog(database="your-database", table_name="claim-table")

# Define transformation logic
def transform_data(policy_rec, claim_rec):
    if claim_rec["Date-of-Loss"] > "12/31/2023":
        claim_rec["Claim-Status"] = "REJECT"
    else:
        policy_rec["Policy-Number"] = claim_rec["Policy-Number"]
        policy_rec["Coverage-Limits"] = claim_rec["Coverage-Limits"]
        policy_rec["Policy-Premium"] = claim_rec["Policy-Premium"]
        if claim_rec["Cause-of-Loss"] == "FIRE":
            claim_rec["Amount-of-Loss"] = 5000
        elif claim_rec["Cause-of-Loss"] == "THEFT":
            claim_rec["Amount-of-Loss"] = 10000
        elif claim_rec["Cause-of-Loss"] == "FLOOD":
            claim_rec["Amount-of-Loss"] = 20000
        else:
            claim_rec["Amount-of-Loss"] = 0
            claim_rec["Claim-Status"] = "REJECT"
        if claim_rec["Amount-of-Loss"] <= policy_rec["Coverage-Limits"]:
            claim_rec["Claim-Status"] = "PAY"
        else:
            claim_rec["Claim-Status"] = "REJECT"
    return claim_rec

# Apply transformations
transformed_data = Join.apply(policy_source, claim_source, 'Policy-Number', 'Policy-Number')
transformed_data = Map.apply(frame=transformed_data, f=transform_data)

# Write the transformed data to the target location
glueContext.write_dynamic_frame.from_catalog(frame=transformed_data, database="your-database", table_name="claim-output-table")

# Job completion
job.commit()
