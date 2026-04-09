if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr)) # remove duplicates
    arr.sort()  # sort the list 
    print(arr[-2]) # print the second largest element
