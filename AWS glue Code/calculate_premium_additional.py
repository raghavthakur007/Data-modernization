# Define the input data
class PolicyRecord:
    def __init__(self, policy_type, age, car_value, property_type, property_value, coverage_amount):
        self.policy_type = policy_type
        self.age = age
        self.car_value = car_value
        self.property_type = property_type
        self.property_value = property_value
        self.coverage_amount = coverage_amount
        self.coverage_limits = 0
        self.policy_premium = 0

# Define a function to calculate premiums
def calculate_premium(policy_record):
    # Additional premium based on age
    if policy_record.age < 25:
        additional_premium_age = 300
    elif policy_record.age < 41:
        additional_premium_age = 200
    elif policy_record.age <= 60:
        additional_premium_age = 400
    else:
        additional_premium_age = 0

    # Additional premium based on car value
    if policy_record.car_value < 20000:
        additional_premium_car_value = 0.05
    elif policy_record.car_value < 50000:
        additional_premium_car_value = 0.08
    else:
        additional_premium_car_value = 0.10

    # Calculate the base premium based on policy type
    if policy_record.policy_type == "CAR_INSURANCE":
        base_premium = 1000
    elif policy_record.policy_type == "HOME_INSURANCE":
        base_premium = 2000
    elif policy_record.policy_type == "LIFE_INSURANCE":
        base_premium = 3000
    else:
        base_premium = 0

    # Calculate the total premium
    premium = base_premium + additional_premium_age + (policy_record.car_value * additional_premium_car_value)
    
    # Assign calculated values back to the policy record
    policy_record.coverage_limits = premium  # Assuming coverage limits are set to premium for this example
    policy_record.policy_premium = premium

# Sample policy records
policy_records = [
    PolicyRecord("CAR_INSURANCE", 30, 25000, "House", 150000, 5000),
    PolicyRecord("HOME_INSURANCE", 45, 18000, "Condo", 90000, 2500),
    PolicyRecord("LIFE_INSURANCE", 50, 0, "N/A", 0, 10000),
]

# Calculate premiums for each policy record
for policy_record in policy_records:
    calculate_premium(policy_record)

# Print the results
for i, policy_record in enumerate(policy_records, start=1):
    print(f"Policy {i}:")
    print(f"Policy Type: {policy_record.policy_type}")
    print(f"Coverage Limits: {policy_record.coverage_limits}")
    print(f"Policy Premium: {policy_record.policy_premium}")
    print()
