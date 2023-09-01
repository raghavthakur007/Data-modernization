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

# Initialize summary report variables
total_policies = 0
total_premiums = 0.0
total_claims = 0
total_rejected_claims = 0

# Process each policy record
for policy_record in policy_dynamic_frame.toDF().collect():
    # Extract relevant fields from the policy record
    policy_number = policy_record["Policy-Number"]
    policy_type = policy_record["Policy-Type"]
    policy_holder_name = policy_record["Policy-Holder-Name"]
    coverage_limits = policy_record["Coverage-Limits"]
    policy_premium = policy_record["Policy-Premium"]
    claim_status = policy_record["Claim-Status"]
    age = policy_record["Age"]
    car_value = policy_record["Car-Value"]
    property_type = policy_record["Property-Type"]
    property_value = policy_record["Property-Value"]
    coverage_amount = policy_record["Coverage-Amount"]

    # Calculate total premiums
    total_premiums += policy_premium

    # Check claim status and update counts
    if claim_status == "PAY":
        total_claims += 1
    else:
        total_rejected_claims += 1

    # Create a policy report record
    policy_report_record = {
        "Policy-Number": policy_number,
        "Policy-Type": policy_type,
        "Policy-Holder-Name": policy_holder_name,
        "Coverage-Limits": coverage_limits,
        "Policy-Premium": policy_premium,
        "Claim-Status": claim_status,
        "Age": age,
        "Car-Value": car_value,
        "Property-Type": property_type,
        "Property-Value": property_value,
        "Coverage-Amount": coverage_amount
    }

    # Write the policy report record to the output table
    glueContext.write_dynamic_frame.from_catalog(
        frame=glueContext.create_dynamic_frame.from_catalog(
            database="your-database-name",
            table_name=output_table
        ),
        transformation_ctx="policy_report_sink",
    )

    # Increment total policies count
    total_policies += 1

# Create a policy summary report
policy_summary_report = {
    "Total-Policies": total_policies,
    "Total-Premiums": total_premiums,
    "Total-Claims": total_claims,
    "Total-Rejected-Claims": total_rejected_claims
}

# Write the policy summary report to the output table
glueContext.write_dynamic_frame.from_catalog(
    frame=glueContext.create_dynamic_frame.from_catalog(
        database="your-database-name",
        table_name=output_table
    ),
    transformation_ctx="policy_summary_report_sink",
)

print("Policy summary report generated.")

# Job completion
job.commit()
