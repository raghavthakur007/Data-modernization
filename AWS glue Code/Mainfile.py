# Import statements and necessary libraries
import oracledb
import getpass
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

# File 1: PolicyCreation
def policy_creation(policy_record):
    # Implementation of PolicyCreation logic
    if policy_record["Policy-Type"] == "CAR_INSURANCE":
        policy_record["Coverage-Limits"] = 100000
        policy_record["Policy-Premium"] = 1000
    elif policy_record["Policy-Type"] == "HOME_INSURANCE":
        policy_record["Coverage-Limits"] = 500000
        policy_record["Policy-Premium"] = 2000
    elif policy_record["Policy-Type"] == "LIFE_INSURANCE":
        policy_record["Coverage-Limits"] = 1000000
        policy_record["Policy-Premium"] = 3000
    else:
        policy_record["Coverage-Limits"] = 0
        policy_record["Policy-Premium"] = 0

    # Additional premium calculation (replace with your logic)
    policy_record["Policy-Premium"] += additional_premium(policy_record)

    return policy_record
def additional_premium(policy_record):
    # Implementation of Additional logic
    premium = 0

    if policy_record["Age"] < 25:
        premium += 300
    elif policy_record["Age"] < 41:
        premium += 200
    elif policy_record["Age"] <= 60:
        premium += 400

    if policy_record["Car-Value"] < 20000:
        premium += 0.05
    elif policy_record["Car-Value"] < 50000:
        premium += 0.08

    return premium



# File 2: ClaimProcessing
def claim_processing(policy_record, claim_record):
    # Implementation of ClaimProcessing logic
    if claim_record["Date-of-Loss"] > "12/31/2023":
        claim_record["Claim-Status"] = "REJECT"
    else:
        policy_record["Policy-Number"] = claim_record["Policy-Number"]
        policy_record["Coverage-Limits"] = claim_record["Coverage-Limits"]
        policy_record["Policy-Premium"] = claim_record["Policy-Premium"]
        if claim_record["Cause-of-Loss"] == "FIRE":
            claim_record["Amount-of-Loss"] = 5000
        elif claim_record["Cause-of-Loss"] == "THEFT":
            claim_record["Amount-of-Loss"] = 10000
        elif claim_record["Cause-of-Loss"] == "FLOOD":
            claim_record["Amount-of-Loss"] = 20000
        else:
            claim_record["Amount-of-Loss"] = 0
            claim_record["Claim-Status"] = "REJECT"
        if claim_record["Amount-of-Loss"] <= policy_record["Coverage-Limits"]:
            claim_record["Claim-Status"] = "PAY"
        else:
            claim_record["Claim-Status"] = "REJECT"
    return claim_record

# File 3: DB2Close
def db2_close():
    # Implementation of DB2Close logic

# File 4: DB2Init
def db2_init():
    # Implementation of DB2Init logic
    print("Initializing DB2 connection...")
    pool = oracledb.create_pool(user="system", password=userpwd, dsn="localhost:1521/XEPDB1",
                            min=1, max=5, increment=1)
    db2_status = "DB2_CONNECTION_SUCCESSFUL"

    # Simulate preparing statements (random values)
    db2_prepared_status = "STATEMENTS_PREPARED"

    # Check if the DB2 connection and statement preparation were successful
    if db2_status == "DB2_CONNECTION_SUCCESSFUL" and db2_prepared_status == "STATEMENTS_PREPARED":
        print("DB2 connection initialized successfully.")
    else:
        print("Error: DB2 connection initialization failed.")

# File 5: FetchPolicyData
def fetch_policy_data():
    # Implementation of FetchPolicyData logic
    policy_db2_file = []
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
        policy_db2_file.append(policy_record)
    return policy_record

# File 6: GenerateReport
def generate_report(policy_record, policy_summary_report):
    # Implementation of GenerateReport logic
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

    print("Policy summary report generated.")
    return policy_summary_report,policy_report_record


# File 7: PolicyRenewal
def policy_renewal(policy_db2_file):
    # Implementation of PolicyRenewal logic
    renewal_policy_data = []

    # Process each policy record
    for policy_record in policy_db2_file:
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

    print("Policy renewals processed.")
    return renewal_policy_data

# File 8: CalculatePremium
def calculate_premium(policy_db2_file):
    # Implementation of CalculatePremium logic
    for policy_record in policy_db2_file:
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
    # glueContext.write_dynamic_frame.from_catalog(
    #     frame=policy_dynamic_frame,
    #     database="your-database-name",
    #     table_name=output_table,
    #     transformation_ctx="premium_calculation_sink"
    # )

    print("Premiums calculated.")


# File 9: CalculatePremiumAdditional
def calculate_premium_additional(policy_db2_file):
    # Implementation of CalculatePremiumAdditional logic
    if policy_db2_file.age < 25:
        additional_premium_age = 300
    elif policy_db2_file.age < 41:
        additional_premium_age = 200
    elif policy_db2_file.age <= 60:
        additional_premium_age = 400
    else:
        additional_premium_age = 0

    # Additional premium based on car value
    if policy_db2_file.car_value < 20000:
        additional_premium_car_value = 0.05
    elif policy_db2_file.car_value < 50000:
        additional_premium_car_value = 0.08
    else:
        additional_premium_car_value = 0.10

    # Calculate the base premium based on policy type
    if policy_db2_file.policy_type == "CAR_INSURANCE":
        base_premium = 1000
    elif policy_db2_file.policy_type == "HOME_INSURANCE":
        base_premium = 2000
    elif policy_db2_file.policy_type == "LIFE_INSURANCE":
        base_premium = 3000
    else:
        base_premium = 0

    # Calculate the total premium
    premium = base_premium + additional_premium_age + (policy_db2_file.car_value * additional_premium_car_value)
    
    # Assign calculated values back to the policy record
    policy_db2_file = premium  # Assuming coverage limits are set to premium for this example
    policy_db2_file.policy_premium = premium

    # # Sample policy records
    # policy_records = [
    #     PolicyRecord("CAR_INSURANCE", 30, 25000, "House", 150000, 5000),
    #     PolicyRecord("HOME_INSURANCE", 45, 18000, "Condo", 90000, 2500),
    #     PolicyRecord("LIFE_INSURANCE", 50, 0, "N/A", 0, 10000),
    # ]

    # Calculate premiums for each policy record
    # for policy_record in policy_records:
    #     calculate_premium(policy_record)

    # # Print the results
    # for i, policy_record in enumerate(policy_records, start=1):
    #     print(f"Policy {i}:")
    #     print(f"Policy Type: {policy_record.policy_type}")
    #     print(f"Coverage Limits: {policy_record.coverage_limits}")
    #     print(f"Policy Premium: {policy_record.policy_premium}")
    #     print()

# File 10: SortPolicyData
def sort_policy_data(ws_sort_buffer):
    # Implementation of SortPolicyData logic
    if len(ws_sort_buffer) > 1:
        mid = len(ws_sort_buffer) // 2  # Find the middle of the array
        left_half = ws_sort_buffer[:mid]  # Split the array into two halves
        right_half = ws_sort_buffer[mid:]

        sort_policy_data(left_half)  # Recursively sort the left half
        sort_policy_data(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for the three arrays

        # Copy data to temporary left and right arrays
        while i < len(left_half) and j < len(right_half):
            if left_half[i].policy_number <= right_half[j].policy_number:
                ws_sort_buffer[k] = left_half[i]
                i += 1
            else:
                ws_sort_buffer[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left in either left_half or right_half
        while i < len(left_half):
            ws_sort_buffer[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            ws_sort_buffer[k] = right_half[j]
            j += 1
            k += 1

# Main program
if __name__ == "__main__":
    # Call the functions from the respective files in the desired sequence
    db2_init()
    fetch_policy_data()
    sort_policy_data(ws_sort_buffer)  # Ensure proper data is passed
    policy_renewal(policy_db2_file)
    calculate_premium_additional()

    # Process claims and generate reports
    for claim_record in claim_records:
        claim_processing(policy_db2_file, claim_record)
        generate_report(policy_report_record, policy_summary_report)

    db2_close()
