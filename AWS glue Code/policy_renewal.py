import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.job import Job

# Create a GlueContext
sc = SparkContext()
glueContext = GlueContext(sc)

# Create a Job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define the input and output data sources
input_table = "your-input-table"
output_table = "your-output-table"

# Read policy data from the input table
policy_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="your-database-name",
    table_name=input_table,
    transformation_ctx="policy_dynamic_frame"
)

# Initialize variables for the policy renewal
renewal_policy_data = []

# Process each policy record
for policy_record in policy_dynamic_frame.toDF().collect():
    # Extract relevant fields from the policy record
    policy_number = policy_record["Policy-Number"]
    policy_type = policy_record["Policy-Type"]

    # Calculate renewal coverage limits and premium based on policy type
    if policy_type == "CAR_INSURANCE":
        coverage_limits = 200000
        policy_premium = 1200
    elif policy_type == "HOME_INSURANCE":
        coverage_limits = 600000
        policy_premium = 2400
    elif policy_type == "LIFE_INSURANCE":
        coverage_limits = 1200000
        policy_premium = 3600
    else:
        coverage_limits = 0
        policy_premium = 0

    # Create a renewal policy record
    renewal_policy_data.append({
        "Policy-Number": policy_number,
        "Policy-Holder-Name": policy_record["Policy-Holder-Name"],
        "Premium-Amount": policy_record["Premium-Amount"],
        "Policy-Type": policy_type,
        "Coverage-Limits": coverage_limits,
        "Policy-Premium": policy_premium
    })

# Write the renewal policy data to the output table
renewal_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    frame=glueContext.create_dynamic_frame.from_catalog(
        database="your-database-name",
        table_name=output_table
    ),
    transformation_ctx="renewal_dynamic_frame",
    name="renewal_dynamic_frame"
)

# Append the renewal data to the existing data
renewal_dynamic_frame = renewal_dynamic_frame.append(
    glueContext.create_dynamic_frame.from_catalog(
        frame=glueContext.create_dynamic_frame.from_catalog(
            database="your-database-name",
            table_name=output_table
        ),
        transformation_ctx="renewal_dynamic_frame_append",
        name="renewal_dynamic_frame_append"
    )
)

# Write the combined renewal data to the output table
glueContext.write_dynamic_frame.from_catalog(
    frame=renewal_dynamic_frame,
    database="your-database-name",
    table_name=output_table,
    transformation_ctx="renewal_sink"
)

print("Policy renewals processed.")

# Job completion
job.commit()
