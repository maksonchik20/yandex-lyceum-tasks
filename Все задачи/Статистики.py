def print_statistics(arr):
    if arr == []:
        print(0, 0, 0, 0, 0, sep="\n")
    else:
        print(len(arr))
        print(sum(arr) / len(arr))
        arr.sort()
        print(arr[0], arr[-1], sep="\n")
        if len(arr) % 2:
            print(arr[len(arr) // 2])
        else:
            print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2)
            
        
    
print_statistics([22])