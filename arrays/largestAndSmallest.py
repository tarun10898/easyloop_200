

# class Solution:

#     arr:list[int]

#     def __init__ (self,arr:list[int]) -> None:
#         self.arr:list[int] = arr

#     def largestAndSmallest(self) -> tuple[int,int,int,int]:

#         self.arr.sort()
#         return self.arr[-1], self.arr[-2], self.arr[0], self.arr[1]


# if __name__ == "__main__":

#     n:int = int(input("enter the number of elements in in the array: "))
#     arr:list[int] = list(map(int,input("enter the elements of the array: ").strip().split()))[:n]

#     if len(arr)<2:
#         raise ValueError("Array should have atleast 2 elements")
#     values:Solution = Solution(arr)
#     all_values: tuple[int,int,int,int] = values.largestAndSmallest()
#     print(f"The largest value in the array is: {all_values[0]}")
#     print(f"The second largest value in the array is: {all_values[1]}")
#     print(f"The smallest value in the array is: {all_values[2]}")
#     print(f"The second smallest value in the array is: {all_values[3]}")



#     time complexity : O(nlogn) due to sorting the array
#     space complexity : O(1) as we are not using any extra space except for a few variables to store the results.



# class Solution:

#     arr:list[int]

#     def __init__ (self,arr:list[int]) -> None:
#         self.arr:list[int] = arr

#     def largestAndSmallest(self) -> tuple[float,float,float,float]:

#         max_value = float('-inf')
#         second_max = float('-inf')
#         min_value = float('inf')
#         second_min = float('inf')

#         for num in self.arr:
#             if num > max_value:
#                 second_max = max_value
#                 max_value =  num
#             elif num > second_max and num != max_value:
#                 second_max = num

#             if num<min_value:
#                 second_min = min_value
#                 min_value = num
#             elif num < second_min and num != min_value:
#                 second_min = num    
#         return max_value, second_max, min_value, second_min              




# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr: list[int] = list(map(int,input("enter the emlements of the array: ").strip().split()))[:n]
#     if len(arr)<2:
#         raise ValueError("Array should have atleast 2 elements")
    
#     values: Solution = Solution(arr)
#     all_values: tuple[float,float,float,float] = values.largestAndSmallest()
#     print(f"The largest value in the array is: {int(all_values[0])}")
#     print(f"The second largest value in the array is: {int(all_values[1])}")        
#     print(f"The smallest value in the array is: {int(all_values[2])}")
#     print(f"The second smallest value in the array is: {int(all_values[3])}")


#     time complexity : O(n) as we are traversing the array only once
#     space complexity : O(1) as we are not using any extra space except for a few variables to store the results.

