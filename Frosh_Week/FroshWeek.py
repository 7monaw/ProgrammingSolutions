num = int(input())

# Merge sort
def mergeSort(array):
    counter=0
    if len(array) > 1:
        half = len(array)//2
        left = array[:half]
        right = array[half:]

        counter+=mergeSort(left)
        counter+=mergeSort(right)

        # merge
        i, j, idx = [0, 0, 0]
        while i < len(left) and j < len(right):
            if(left[i]<right[j]):
                array[idx] = left[i]
                i+=1
            else:
                array[idx] = right[j]
                j+=1
                counter+=(len(left)-i)
            idx+=1
        
        # Ran out of elements
        while i < len(left):
            array[idx] = left[i]
            i+=1
            idx+=1
        while j < len(right):
            array[idx] = right[j]
            j+=1
            idx+=1
    return counter
    
array = []
for k in range(0, num):
    array.append(int(input()))

print(mergeSort(array))
