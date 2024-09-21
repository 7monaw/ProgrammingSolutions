import sys

case=0
for line in sys.stdin:
    num_cases1 = int(line)
    case+=1
    nums = []
    for _ in range(0, num_cases1):
        nums.append(int(input()))

    print(f"Case {case}:")
    num_cases2 = int(input())
    for __ in range(0, num_cases2):
        test = int(input())
        min_diff = abs(nums[0]+nums[1]-test)
        summation = nums[0]+nums[1]
        for i in range(0, num_cases1-1):
            for j in range(i+1, num_cases1):
                if(abs(nums[i]+nums[j]-test) < min_diff):
                    summation = nums[i]+nums[j]
                    min_diff = abs(nums[i]+nums[j]-test)

        print(f"Closest sum to {test} is {summation}.")
