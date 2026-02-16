# # brute force approch:

# class Solution:

#     arr: list[int]
    
#     def __init__(self,arr:list[int]) -> None:
#         self.arr: list[int] = arr

#     def largest(self) -> int:

#         self.arr.sort()
#         return self.arr[-1]    



# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements: "))
#     arr:list[int] = list(map(int, input("enter th elements: ").strip().split()))[:n]
#     if len(arr) < 2:
#         print("array should have altleast 2 elements")
#     largest: Solution = Solution(arr)    
#     print(f"largest element in the array is: {largest.largest()}")


# # optimal approch:


# class LargestValue:

#     arr:list[int]

#     def __init__(self,arr:list[int]) -> None:
#         self.arr:list[int] = arr
    
#     def largest(self) ->int:
#         if not self.arr:
#             raise ValueError("Array is empty")
#         max_value:int = self.arr[0]
#         for num in self.arr:
#             if num > max_value:
#                 max_value = num
#         return max_value        


# if __name__ == "__main__":

#     n:int = int(input("enter the number of elements of the array: "))

#     arr:list[int] = list(map(int,input("enter th elements of the array: ").strip().split()))[:n]

#     max: LargestValue = LargestValue(arr)

#     print(f"The largest value in the array is: {max.largest()}")




