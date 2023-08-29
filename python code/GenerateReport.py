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

class PolicyReportRecord:
    def __init__(self):
        self.Policy_Number = ""
        self.Policy_Type = ""
        self.Policy_Holder_Name = ""
        self.Coverage_Limits = 0.0
        self.Policy_Premium = 0.0
        self.Claim_Status = ""
        self.Age = 0
        self.Car_Value = 0.0
        self.Property_Type = ""
        self.Property_Value = 0.0
        self.Coverage_Amount = 0.0

class PolicySummaryReport:
    def __init__(self):
        self.Total_Policies = 0
        self.Total_Premiums = 0.0
        self.Total_Claims = 0
        self.Total_Rejected_Claims = 0

def generate_policy_summary_report(policy_report_record, policy_summary_report):
    print("Generating policy summary report...")
    
    premium_amount_temp = policy_report_record.Policy_Premium
    policy_summary_report.Total_Premiums += premium_amount_temp
    policy_summary_report.Total_Policies += 1

    if policy_report_record.Claim_Status == "PAY":
        policy_summary_report.Total_Claims += 1
    else:
        policy_summary_report.Total_Rejected_Claims += 1
    
    # Write to PolicyIMSFile - You can implement this part as needed

    print("Policy summary report generated.")

# Sample usage
policy_report = PolicyReportRecord()
policy_report.Policy_Number = "POLICY001"
policy_report.Policy_Type = "CAR_INSURANCE"
policy_report.Policy_Holder_Name = "John Doe"
policy_report.Coverage_Limits = 100000
policy_report.Policy_Premium = 1200.50
policy_report.Claim_Status = "PAY"
policy_report.Age = 35
policy_report.Car_Value = 25000.75
policy_report.Property_Type = "Single-family home"
policy_report.Property_Value = 150000.25
policy_report.Coverage_Amount = 75000

policy_summary = PolicySummaryReport()

generate_policy_summary_report(policy_report, policy_summary)
