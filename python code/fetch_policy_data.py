import random

class PolicyDB2Record:
    def __init__(self):
        self.Policy_Number = ""
        self.Policy_Holder_Name = ""
        self.Premium_Amount = 0.0
        self.Policy_Type = ""
        self.Coverage_Limits = 0.0
        self.Policy_Premium = 0.0
        self.Age = 0
        self.Car_Value = 0.0
        self.Property_Type = ""
        self.Property_Value = 0.0
        self.Coverage_Amount = 0.0

def fetch_policy_data():
    print("Fetching policy data from DB2...")
    
    policy_db2_records = [PolicyDB2Record() for _ in range(10)]
    
    for record_count in range(10):
        policy_db2_records[record_count].Policy_Number = f"POLICY00{record_count + 1}"
        policy_db2_records[record_count].Policy_Holder_Name = f"Policy Holder {record_count + 1}"
        policy_db2_records[record_count].Premium_Amount = (record_count + 1) * 100.50
        policy_db2_records[record_count].Policy_Type = random_policy_type()
        policy_db2_records[record_count].Coverage_Limits = (record_count + 1) * 1000
        policy_db2_records[record_count].Policy_Premium = (record_count + 1) * 200.75
        policy_db2_records[record_count].Age = record_count + 1
        policy_db2_records[record_count].Car_Value = (record_count + 1) * 5000.50
        policy_db2_records[record_count].Property_Type = random_property_type()
        policy_db2_records[record_count].Property_Value = (record_count + 1) * 10000.25
        policy_db2_records[record_count].Coverage_Amount = (record_count + 1) * 5000
    
    print("Policy data fetched.")
    return policy_db2_records

def random_policy_type():
    random_policy_type = random.randint(1, 3)
    if random_policy_type == 1:
        return "CAR_INSURANCE"
    elif random_policy_type == 2:
        return "HOME_INSURANCE"
    else:
        return "LIFE_INSURANCE"

def random_property_type():
    random_property_type = random.randint(1, 3)
    if random_property_type == 1:
        return "Condo"
    elif random_property_type == 2:
        return "Townhouse"
    else:
        return "Single-family home"

# Call the function to fetch policy data
policy_db2_records = fetch_policy_data()

# Print the fetched policy data
for record in policy_db2_records:
    print("Policy Number:", record.Policy_Number)
    print("Policy Holder Name:", record.Policy_Holder_Name)
    print("Premium Amount:", record.Premium_Amount)
    print("Policy Type:", record.Policy_Type)
    print("Coverage Limits:", record.Coverage_Limits)
    print("Policy Premium:", record.Policy_Premium)
    print("Age:", record.Age)
    print("Car Value:", record.Car_Value)
    print("Property Type:", record.Property_Type)
    print("Property Value:", record.Property_Value)
    print("Coverage Amount:", record.Coverage_Amount)
    print()
