class PolicyRecord:
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

class PolicyDB2File:
    def __init__(self):
        self.PolicyDB2Record = [PolicyRecord() for _ in range(10)]

def calculate_additional_premium(age, car_value):
    premium_amount_temp = 300
    if age < 25:
        premium_amount_temp += 200
    elif age < 41:
        premium_amount_temp += 100
    elif age <= 60:
        premium_amount_temp += 400
    
    if car_value < 20000:
        premium_amount_temp += 0.05
    elif car_value < 50000:
        premium_amount_temp += 0.08
    else:
        premium_amount_temp += 0.10
    
    return premium_amount_temp

def policy_creation(policy_db2_file):
    for record_count in range(10):
        policy_record = policy_db2_file.PolicyDB2Record[record_count]
        policy_type = policy_record.Policy_Type
        age = policy_record.Age
        car_value = policy_record.Car_Value

        if policy_type == "CAR_INSURANCE":
            policy_record.Coverage_Limits = 100000
            policy_record.Policy_Premium = 1000
        elif policy_type == "HOME_INSURANCE":
            policy_record.Coverage_Limits = 500000
            policy_record.Policy_Premium = 2000
        elif policy_type == "LIFE_INSURANCE":
            policy_record.Coverage_Limits = 1000000
            policy_record.Policy_Premium = 3000
        else:
            policy_record.Coverage_Limits = 0
            policy_record.Policy_Premium = 0
        
        additional_premium = calculate_additional_premium(age, car_value)
        policy_record.Policy_Premium += additional_premium

        policy_record.Coverage_Limits = round(policy_record.Coverage_Limits, 2)
        policy_record.Policy_Premium = round(policy_record.Policy_Premium, 2)

# Sample usage
policy_db2_file = PolicyDB2File()
# Populate policy_db2_file with data

policy_creation(policy_db2_file)

# Displaying the results
for record_count in range(10):
    policy_record = policy_db2_file.PolicyDB2Record[record_count]
    print(f"Policy {record_count + 1} - Type: {policy_record.Policy_Type}, Premium: ${policy_record.Policy_Premium}, Coverage Limits: ${policy_record.Coverage_Limits}")
