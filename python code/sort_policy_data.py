# Define the PolicyRecord structure
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

# Simulated data (replace with actual data)
PolicyDB2Record = [PolicyRecord() for _ in range(10)]
WS_Sort_Buffer = []

# Merge Sort algorithm
def merge_sort(left_index, right_index):
    if left_index < right_index:
        mid_point = (left_index + right_index) // 2
        merge_sort(left_index, mid_point)
        merge_sort(mid_point + 1, right_index)
        merge(left_index, mid_point, right_index)

def merge(left_index, mid_point, right_index):
    i, j, k = left_index, mid_point + 1, left_index

    while i <= mid_point and j <= right_index:
        if PolicyDB2Record[i].Policy_Number <= PolicyDB2Record[j].Policy_Number:
            WS_Sort_Buffer.append(PolicyDB2Record[i])
            i += 1
        else:
            WS_Sort_Buffer.append(PolicyDB2Record[j])
            j += 1

    while i <= mid_point:
        WS_Sort_Buffer.append(PolicyDB2Record[i])
        i += 1

    while j <= right_index:
        WS_Sort_Buffer.append(PolicyDB2Record[j])
        j += 1

    for m in range(left_index, right_index + 1):
        PolicyDB2Record[m] = WS_Sort_Buffer[m - left_index]

# Main sorting function
def sort_policy_data():
    print("Sorting policy data using Merge Sort...")
    merge_sort(0, len(PolicyDB2Record) - 1)
    print("Policy data sorted.")

# Call the sorting function
sort_policy_data()
