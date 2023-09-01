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
datasource = glueContext.create_dynamic_frame.from_catalog(database="your-database", table_name="your-table")

# Define transformation logic
def transform_data(rec):
    if rec["Policy-Type"] == "CAR_INSURANCE":
        rec["Coverage-Limits"] = 100000
        rec["Policy-Premium"] = 1000
    elif rec["Policy-Type"] == "HOME_INSURANCE":
        rec["Coverage-Limits"] = 500000
        rec["Policy-Premium"] = 2000
    elif rec["Policy-Type"] == "LIFE_INSURANCE":
        rec["Coverage-Limits"] = 1000000
        rec["Policy-Premium"] = 3000
    else:
        rec["Coverage-Limits"] = 0
        rec["Policy-Premium"] = 0

    # Additional premium calculation (replace with your logic)
    rec["Policy-Premium"] += additional_premium(rec)

    return rec

def additional_premium(rec):
    premium = 0

    if rec["Age"] < 25:
        premium += 300
    elif rec["Age"] < 41:
        premium += 200
    elif rec["Age"] <= 60:
        premium += 400

    if rec["Car-Value"] < 20000:
        premium += 0.05
    elif rec["Car-Value"] < 50000:
        premium += 0.08

    return premium

# Apply transformations
transformed_data = ApplyMapping.apply(frame=datasource, mappings=[
    ("Policy-Number", "string", "Policy-Number", "string"),
    ("Policy-Holder-Name", "string", "Policy-Holder-Name", "string"),
    ("Premium-Amount", "double", "Premium-Amount", "double"),
    ("Policy-Type", "string", "Policy-Type", "string"),
    ("Coverage-Limits", "int", "Coverage-Limits", "int"),
    ("Policy-Premium", "double", "Policy-Premium", "double"),
    ("Age", "int", "Age", "int"),
    ("Car-Value", "double", "Car-Value", "double"),
    ("Property-Type", "string", "Property-Type", "string"),
    ("Property-Value", "double", "Property-Value", "double"),
    ("Coverage-Amount", "double", "Coverage-Amount", "double")
])

transformed_data = Map.apply(frame=transformed_data, f=transform_data)

# Write the transformed data to the target location
glueContext.write_dynamic_frame.from_catalog(frame=transformed_data, database="your-database", table_name="your-target-table")

# Job completion
job.commit()
