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

def additional_premium(age, car_value, premium_amount_temp):
    if age < 25:
        premium_amount_temp += 300
    elif age < 41:
        premium_amount_temp += 200
    elif age <= 60:
        premium_amount_temp += 400
    
    if car_value < 20000:
        premium_amount_temp += 0.05
    elif car_value < 50000:
        premium_amount_temp += 0.08
    
    return premium_amount_temp

def main(policy_db2_records):
    print("Calculating premiums for each policy...")

    for record_count in range(10):
        policy_record = PolicyRecord()
        policy_db2_record = policy_db2_records[record_count]

        policy_record.Policy_Type = policy_db2_record.Policy_Type
        policy_record.Age = policy_db2_record.Age
        policy_record.Car_Value = policy_db2_record.Car_Value
        policy_record.Property_Type = policy_db2_record.Property_Type
        policy_record.Property_Value = policy_db2_record.Property_Value
        policy_record.Coverage_Amount = policy_db2_record.Coverage_Amount

        if policy_record.Policy_Type == "CAR_INSURANCE":
            policy_record.Coverage_Limits = 100000
            policy_record.Policy_Premium = 1000
        elif policy_record.Policy_Type == "HOME_INSURANCE":
            policy_record.Coverage_Limits = 500000
            policy_record.Policy_Premium = 2000
        elif policy_record.Policy_Type == "LIFE_INSURANCE":
            policy_record.Coverage_Limits = 1000000
            policy_record.Policy_Premium = 3000
        else:
            policy_record.Coverage_Limits = 0
            policy_record.Policy_Premium = 0

        policy_record.Policy_Premium = additional_premium(policy_record.Age, policy_record.Car_Value, policy_record.Policy_Premium)

        print(f"Policy {record_count + 1}: Premium = {policy_record.Policy_Premium}, Coverage Limits = {policy_record.Coverage_Limits}")

    print("Premiums calculated.")

# Sample data for PolicyDB2File
policy_db2_records = []
for _ in range(10):
    policy_db2_records.append(PolicyDB2Record())

# Call the main function
main(policy_db2_records)
