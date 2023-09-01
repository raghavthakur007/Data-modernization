# Define the PolicyRecord class to represent policy data
class PolicyRecord:
    def __init__(self, policy_number, policy_holder_name, premium_amount, policy_type,
                 coverage_limits, policy_premium, age, car_value, property_type, property_value, coverage_amount):
        self.policy_number = policy_number
        self.policy_holder_name = policy_holder_name
        self.premium_amount = premium_amount
        self.policy_type = policy_type
        self.coverage_limits = coverage_limits
        self.policy_premium = policy_premium
        self.age = age
        self.car_value = car_value
        self.property_type = property_type
        self.property_value = property_value
        self.coverage_amount = coverage_amount

# Define a merge sort function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Split the array into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        i = j = k = 0  # Initialize indices for the three arrays

        # Copy data to temporary left and right arrays
        while i < len(left_half) and j < len(right_half):
            if left_half[i].policy_number <= right_half[j].policy_number:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements were left in either left_half or right_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Sample data
policy_records = [
    PolicyRecord("POLICY003", "Policy Holder 3", 3000.50, "CAR_INSURANCE", 300000, 2000.75, 30, 25000.50, "Condo", 150000.75, 5000),
    PolicyRecord("POLICY001", "Policy Holder 1", 1000.25, "HOME_INSURANCE", 500000, 1000.50, 40, 18000.25, "Townhouse", 90000.50, 2500),
    PolicyRecord("POLICY002", "Policy Holder 2", 2000.75, "LIFE_INSURANCE", 1000000, 3000.25, 50, 0, "N/A", 0, 10000),
]

# Sort the policy records by policy number
merge_sort(policy_records)

# Print the sorted policy records
for policy_record in policy_records:
    print(f"Policy Number: {policy_record.policy_number}")
    print(f"Policy Holder Name: {policy_record.policy_holder_name}")
    print(f"Premium Amount: {policy_record.premium_amount}")
    print(f"Policy Type: {policy_record.policy_type}")
    print(f"Coverage Limits: {policy_record.coverage_limits}")
    print(f"Policy Premium: {policy_record.policy_premium}")
    print(f"Age: {policy_record.age}")
    print(f"Car Value: {policy_record.car_value}")
    print(f"Property Type: {policy_record.property_type}")
    print(f"Property Value: {policy_record.property_value}")
    print(f"Coverage Amount: {policy_record.coverage_amount}")
    print()
