import sys

def stack(func, list):
    stack = []
    for i in range(0, len(func)):
        if(func[i]==1):
            stack.append(list[i])
        else:
            try:
                if(list[i] == stack[-1]):
                    stack.pop()
                else:
                    return 0
            except:
                return 0
    return 1

def queue(func, list):
    queue = []
    for i in range(0, len(func)):
        if(func[i]==1):
            queue.append(list[i])
        else:
            try:
                if(list[i] == queue[0]):
                    queue.pop(0)
                else:
                    return 0
            except:
                return 0
    return 1

# def minPriorityQ(func, list):
#     Q = []
#     for i in range(0, len(func)):
#         if(func[i]==1):
#             Q.append(list[i])
#             Q = sorted(Q)
#         else:
#             try:
#                 if(list[i] == Q[0]):
#                     Q.pop(0)
#                 else:
#                     return 0
#             except:
#                 return 0
#     return 1

def maxPriorityQ(func, list):
    Q = []
    for i in range(0, len(func)):
        if(func[i]==1):
            Q.append(list[i])
            Q = sorted(Q, reverse=True)
        else:
            try:
                if(list[i] == Q[0]):
                    Q.pop(0)
                else:
                    return 0
            except:
                return 0
    return 1

#################
# Testing Cases #
#################
for line in sys.stdin:
    num = int(line)
    func = []
    l = []

    for sequence in range(0, num):
        temp = list(map(int, input().split(" ")))
        func.append(temp[0])
        l.append(temp[1])

    token=[0, 0, 0] # stack, queue, priorityQ
    if(stack(func, l)==1):
        token[0] = 1
    if(queue(func, l)==1):
        token[1] = 1
    if(maxPriorityQ(func, l)==1):
        token[2] = 1


    if(sum(token)>1):
        print("not sure")
    elif(token[0]==1):
        print("stack")
    elif(token[1]==1):
        print("queue")
    elif(token[2]==1):
        print("priority queue")
    else:
        print("impossible")
