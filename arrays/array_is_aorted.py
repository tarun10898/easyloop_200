


# class Solution:
#     arr:list[int]

#     def __init__(self,arr:list[int]) -> None:
#         self.arr = arr

#     def isAssinding(self) -> bool:
#         for i in range(len(self.arr)-1):
#             for j in range(i+1,len(self.arr)):
#                 if self.arr[i] > self.arr[j]:
#                     return False
#         return True
    
#     def isDessending(self) -> bool:
#         for i in range(len(self.arr)-1):
#             for j in range(i+1,len(self.arr)):
#                 if self.arr[i] < self.arr[j]:
#                     return False
#         return True


# if __name__ == "__main__":

#     n:int = int(input("enter the niumber of eleements in th array: "))
#     arr: list[int] =  list(map(int, input("enter the elements in the array: ").strip().split()))[:n]

#     values: Solution = Solution(arr)
#     assending: bool = values.isAssinding()
#     dessending:bool = values.isDessending()
#     print(f"The array {arr} is sorted in assending order: {assending}")
#     print(f"The array {arr} is sorted in dessending order: {dessending}")


# time complexity : O(n^2) as we are traversing the array twice to check if it is sorted in assending or dessending order.
# space complexity : O(1) as we are not using any extra space except for a few variables to store the results.    




# from time import time


# class Solution:
#     arr:list[int]

#     def __init__(self,arr:list[int]) -> None:
#         self.arr = arr

#     def isAssinding(self) -> bool:
#         for i in range(len(self.arr)-1):
#             if self.arr[i] > self.arr[i+1]:
#                 return False
#         return True

#     def isDessending(self) -> bool:
#         for i in range(len(self.arr)-1):
#             if self.arr[i] < self.arr[i+1]:
#                 return False
#         return True

# if __name__ == "__main__":

#     n:int = int(input("enter the niumber of eleements in th array: "))
#     arr: list[int] =  list(map(int, input("enter the elements in the array: ").strip().split()))[:n]

#     values: Solution = Solution(arr)
#     assending: bool = values.isAssinding()
#     dessending:bool = values.isDessending()
#     print(f"The array {arr} is sorted in assending order: {assending}")
#     print(f"The array {arr} is sorted in dessending order: {dessending}")

# time complexity : O(n) as we are traversing the array once to check if it is sorted in assending or dessending order.
# space complexity : O(1) as we are not using any extra space except for a few variables to store the results.    
