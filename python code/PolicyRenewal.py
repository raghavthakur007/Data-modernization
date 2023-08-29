class PolicyRecord:
    def __init__(self):
        self.Policy_Number = ""
        self.Policy_Holder_Name = ""
        self.Premium_Amount = 0.0
        self.Policy_Type = ""
        self.Coverage_Limits = 0.0
        self.Policy_Premium = 0.0

class PolicyDB2File:
    def __init__(self):
        self.PolicyDB2Record = [PolicyRecord() for _ in range(10)]

def policy_renewal(policy_db2_file):
    for record_count in range(10):
        policy_record = policy_db2_file.PolicyDB2Record[record_count]
        policy_type = policy_record.Policy_Type

        if policy_type == "CAR_INSURANCE":
            policy_record.Coverage_Limits = 200000
            policy_record.Policy_Premium = 1200
        elif policy_type == "HOME_INSURANCE":
            policy_record.Coverage_Limits = 600000
            policy_record.Policy_Premium = 2400
        elif policy_type == "LIFE_INSURANCE":
            policy_record.Coverage_Limits = 1200000
            policy_record.Policy_Premium = 3600
        else:
            policy_record.Coverage_Limits = 0
            policy_record.Policy_Premium = 0
        
        policy_record.Coverage_Limits = round(policy_record.Coverage_Limits, 2)
        policy_record.Policy_Premium = round(policy_record.Policy_Premium, 2)

# Sample usage
policy_db2_file = PolicyDB2File()
# Populate policy_db2_file with data

policy_renewal(policy_db2_file)

# Displaying the results
for record_count in range(10):
    policy_record = policy_db2_file.PolicyDB2Record[record_count]
    print(f"Policy {record_count + 1} - Type: {policy_record.Policy_Type}, Premium: ${policy_record.Policy_Premium}, Coverage Limits: ${policy_record.Coverage_Limits}")
