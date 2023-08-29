class PolicyRecord:
    def __init__(self):
        self.Policy_Number = ""
        self.Policy_Holder_Name = ""
        self.Premium_Amount = 0.0
        self.Policy_Type = ""
        self.Coverage_Limits = 0.0
        self.Policy_Premium = 0.0
        self.Claim_Status = ""

class ClaimRecord:
    def __init__(self):
        self.Policy_Number = ""
        self.Date_of_Loss = ""
        self.Cause_of_Loss = ""
        self.Amount_of_Loss = 0.0

class PolicyDB2Record:
    def __init__(self):
        self.Policy_Number = ""
        self.Policy_Holder_Name = ""
        self.Premium_Amount = 0.0
        self.Policy_Type = ""
        self.Coverage_Limits = 0.0
        self.Policy_Premium = 0.0

def main(policy_db2_records, claim_record):
    for record_count in range(10):
        if policy_db2_records[record_count].Policy_Number == claim_record.Policy_Number:
            policy_record = PolicyRecord()
            policy_record.Coverage_Limits = policy_db2_records[record_count].Coverage_Limits
            policy_record.Policy_Premium = policy_db2_records[record_count].Policy_Premium
            break
    
    if claim_record.Date_of_Loss > "12/31/2023":
        claim_record.Claim_Status = "REJECT"
    else:
        policy_record.Policy_Type = claim_record.Cause_of_Loss
        if policy_record.Policy_Type == "FIRE":
            claim_record.Amount_of_Loss = 5000
        elif policy_record.Policy_Type == "THEFT":
            claim_record.Amount_of_Loss = 10000
        elif policy_record.Policy_Type == "FLOOD":
            claim_record.Amount_of_Loss = 20000
        else:
            claim_record.Amount_of_Loss = 0
            claim_record.Claim_Status = "REJECT"
        
        if claim_record.Amount_of_Loss <= policy_record.Coverage_Limits:
            claim_record.Claim_Status = "PAY"
        else:
            claim_record.Claim_Status = "REJECT"

# Sample data for PolicyDB2File
policy_db2_records = []
for _ in range(10):
    policy_db2_records.append(PolicyDB2Record())

# Sample data for ClaimRecord
claim_record = ClaimRecord()
claim_record.Policy_Number = "POLICY123"
claim_record.Date_of_Loss = "12/15/2023"
claim_record.Cause_of_Loss = "FIRE"

# Call the main function
main(policy_db2_records, claim_record)

print(f"Claim Status: {claim_record.Claim_Status}")
