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

# Initialize variables for premium calculation
premiums = []
coverage_limits = []
ages = []
car_values = []

# Process each policy record
for policy_record in policy_dynamic_frame.toDF().collect():
    policy_type = policy_record["Policy-Type"]
    age = int(policy_record["Age"])
    car_value = float(policy_record["Car-Value"])
    coverage_limit = float(policy_record["Coverage-Limits"])
    
    # Calculate additional premium based on age
    if age < 25:
        additional_premium_age = 300
    elif age < 41:
        additional_premium_age = 200
    elif age <= 60:
        additional_premium_age = 400
    else:
        additional_premium_age = 0

    # Calculate additional premium based on car value
    if car_value < 20000:
        additional_premium_car_value = 0.05
    elif car_value < 50000:
        additional_premium_car_value = 0.08
    else:
        additional_premium_car_value = 0.10

    # Calculate the total premium
    if policy_type == "CAR_INSURANCE":
        base_premium = 1000
    elif policy_type == "HOME_INSURANCE":
        base_premium = 2000
    elif policy_type == "LIFE_INSURANCE":
        base_premium = 3000
    else:
        base_premium = 0

    premium = base_premium + additional_premium_age + (car_value * additional_premium_car_value)
    
    # Append premium, age, car value, and coverage limit to lists
    premiums.append(premium)
    ages.append(age)
    car_values.append(car_value)
    coverage_limits.append(coverage_limit)

# Add the calculated premiums, ages, car values, and coverage limits to the dynamic frame
policy_dynamic_frame = policy_dynamic_frame.drop_fields(['Premium-Amount', 'Age', 'Car-Value', 'Coverage-Limits'])
policy_dynamic_frame = policy_dynamic_frame.withColumn('Policy-Premium', F.array(*[F.lit(p) for p in premiums]))
policy_dynamic_frame = policy_dynamic_frame.withColumn('Age', F.array(*[F.lit(a) for a in ages]))
policy_dynamic_frame = policy_dynamic_frame.withColumn('Car-Value', F.array(*[F.lit(cv) for cv in car_values]))
policy_dynamic_frame = policy_dynamic_frame.withColumn('Coverage-Limits', F.array(*[F.lit(cl) for cl in coverage_limits]))

# Write the updated dynamic frame to the output table
glueContext.write_dynamic_frame.from_catalog(
    frame=policy_dynamic_frame,
    database="your-database-name",
    table_name=output_table,
    transformation_ctx="premium_calculation_sink"
)

print("Premiums calculated.")

# Job completion
job.commit()
