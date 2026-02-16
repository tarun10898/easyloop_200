

# class Solution:
     
#     arr:list[int]
    
#     def __init__(self,arr:list[int]) -> None:
#         self.arr: list[int] = arr

#     def removeDuplicates(self) -> list[int]:
#         unique_values: list[int] = []
#         for num in self.arr:
#             if num not in unique_values:
#                 unique_values.append(num)
#         return unique_values


# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr:list[int] = list(map(int,input("enter the elements in the array: ").strip().split()))[:n]
#     if len(arr)<2:
#         raise ValueError("enter atleast 2 elements in the array")
    
#     values: Solution = Solution(arr)

#     print(f"The array after removing duplicates is: {values.removeDuplicates()}")

# time complexity : O(n^2) as we are traversing the array once to remove duplicates and for each element we are checking if it is already present in the unique_values list which takes O(n) time in the worst case.
# space complexity : O(n) as we are using a list to store the unique values which can have at most n unique values in the worst case.



# class Solution:

#     arr:list[int]

#     def __init__(self,arr:list[int]) -> None:
#         self.arr:list[int] = arr
    
#     def removeDuplicates(self) -> set[int]:
#         unique_values:set[int] = set()
#         for num in self.arr:
#             unique_values.add(num)
#         return unique_values



# if __name__ == "__main__":
#     n:int = int(input("enter the elements of the array: "))
#     arr:list[int] = list(map(int,input("enter the elements of the array: ").strip().split()))[:n]
#     if len(arr) < 2:
#         raise ValueError("array should have atleast 2 elements")
    
#     unique_values: Solution = Solution(arr)
#     print(f"The array after removing duplicates is: {unique_values.removeDuplicates()}")

# time complexity : O(n) as we are traversing the array once to remove duplicates.
# space complexity : O(n) as we are using a set to store the unique values which can
# have at most n unique values in the worst case.


# class Solution:

#     arr:list[int]

#     def __init__ (self,arr:list[int]) -> None:
#         self.arr:list[int] = arr
#     def removeDuplicates(self) -> int:
#         unique_index:int = 0
#         for i in range(1,len(self.arr)):
#             if self.arr[i] != self.arr[unique_index]:
#                 unique_index += 1
#                 self.arr[unique_index] = self.arr[i]
#         return unique_index + 1



# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr:list[int] = list(map(int,input("enter the elements in the array: ").strip().split()))[:n]

#     if len(arr)<2:
#         raise ValueError("array should have atleast 2 elements")
    
#     value: Solution = Solution(arr)
#     print(f"The array after removing the duplicates is: {arr[:value.removeDuplicates()]}")
    

# time complexity : O(n) as we are traversing the array once to remove duplicates.
# space complexity : O(1) as we are not using any extra space except for a few variables to store the results.      

