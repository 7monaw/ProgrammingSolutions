num = list(map(int, input().split(" ")))

stu = list(map(int, input().split(" ")))
students = [i-num[1] for i in stu]

running_sum = students[0]
max_global = students[0]
for i in students[1:]:
    if(i+running_sum>=i):
        print(i)
        running_sum += i
    else:
        running_sum = i #restart

    if(max_global<running_sum):
            max_global = running_sum

print(max(max_global, running_sum))
