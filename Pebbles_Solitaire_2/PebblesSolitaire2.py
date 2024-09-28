num = int(input())
hash_map = {}

def backtracking(line):
    minimum=0
    for i in range(0, 23):
        if(line[i] == 'o'):
            minimum+=1  

    for j in range(0, len(line)-2):
        if(''.join(line) in hash_map.keys()): #dp
            return hash_map[''.join(line)]
        
        if(line[j]=='o' and line[j+1]=='o' and line[j+2]=='-'):
            line[j]='-'
            line[j+1]='-'
            line[j+2]='o'
            current = backtracking(line)
            if (current < minimum):
                minimum = current
            # Putting back the pebble (backtracking)
            line[j]='o'
            line[j+1]='o'
            line[j+2]='-'
    
    for j in range(len(line)-1, 1, -1):
        if(line[j]=='o' and line[j-1]=='o' and line[j-2]=='-'):
            line[j]='-'
            line[j-1]='-'
            line[j-2]='o'
            current = backtracking(line)
            if (current < minimum):
                minimum = current
            # Putting back the pebble (backtracking)
            line[j]='o'
            line[j-1]='o'
            line[j-2]='-'

    x = ''.join(line)
    hash_map[x] = minimum
    return minimum

for i in range(0, num):
    line = list(input())
    minimum = backtracking(line)
    print(minimum)
