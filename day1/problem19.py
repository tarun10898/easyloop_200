if __name__ == "__main__":
    n : int = int(input())
    arr1: list[int] = []
    arr : list[int] = list(map(int,input().strip().split()))[:n]
    for i in range(n):
        arr1.append(arr[i] * arr[i])
    print(f"squared array: {arr1}")    
