l = [9, 5, 1, 4, 3]
for i in range(1, len(l)):
        min = l[i]
        j = i - 1        
        while j >= 0 and min < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = min
print('Sorted list')
print(l)