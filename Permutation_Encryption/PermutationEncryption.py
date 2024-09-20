for i in range(0, 150):
    num = list(map(int, input().split(" "))) #num[0] is the number of integers that formed permutation
    if(num[0]==0):
        break
    sentence = list(input())
    remainder = len(sentence) % num[0]
    if(remainder != 0):
        for j in range(0, num[0] - remainder):
            sentence.append(" ")
    num_permutations = int(len(sentence) / num[0])

    out = "'"
    for k in range(0, num_permutations):
        for idx in num[1:num[0]+1]:
            out+=sentence[idx + (k*num[0])-1]
    out+="'"
    print(out)
