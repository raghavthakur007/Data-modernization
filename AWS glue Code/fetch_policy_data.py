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

# Simulate fetching policy data from DB2
print("Fetching policy data from DB2...")
policy_records = []

# Simulate fetching random data for each policy record
for record_count in range(1, 11):
    policy_record = {
        "Policy-Number": f"POLICY00{record_count}",
        "Policy-Holder-Name": f"Policy Holder {record_count}",
        "Premium-Amount": record_count * 100.50,
        "Policy-Type": "CAR_INSURANCE" if record_count % 3 == 1 else
                       "HOME_INSURANCE" if record_count % 3 == 2 else
                       "LIFE_INSURANCE",
        "Coverage-Limits": record_count * 1000,
        "Policy-Premium": record_count * 200.75,
        "Age": record_count,
        "Car-Value": record_count * 5000.50,
        "Property-Type": "Condo" if record_count % 3 == 1 else
                         "Townhouse" if record_count % 3 == 2 else
                         "Single-family home",
        "Property-Value": record_count * 10000.25,
        "Coverage-Amount": record_count * 5000
    }
    policy_records.append(policy_record)

# Convert policy records to a Glue DynamicFrame
policy_dynamic_frame = glueContext.create_dynamic_frame.from_catalog(
    database="your-database-name",
    table_name="your-table-name",
    transformation_ctx="policy_dynamic_frame"
)

# Write the policy data to the Glue DynamicFrame
glueContext.write_dynamic_frame.from_catalog(
    frame=policy_dynamic_frame,
    database="your-database-name",
    table_name="your-table-name",
    transformation_ctx="policy_sink"
)

print("Policy data fetched and written to Glue catalog.")

# Job completion
job.commit()
