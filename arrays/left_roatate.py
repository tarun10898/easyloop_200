

# class Solution:

#     arr: list[int]

#     def __init__ (self,arr:list[int]) -> None:
#         self.arr:list[int] = arr

#     def leftRoate(self) -> list[int]:
#         first_element:int = self.arr[0]
#         for i in range(1,len(self.arr)):
#             self.arr[i-1] = self.arr[i]
#         self.arr[-1] = first_element
#         return self.arr
        


# if __name__ == "__main__":
#     n:int = int(input("enter the number of elements in the array: "))
#     arr:list[int] = list(map(int,input("enter the elements in the array: ").strip().split()))[:n]
#     if len(arr)< 2:
#         raise ValueError("array should have atleast 2 elements")
    
#     value:Solution = Solution(arr)
#     print(f"the array after the left rotation is: {value.leftRoate()}")


# time complexity : O(n) as we are traversing the array once to perform the left rotation.
# space complexity : O(1) as we are not using any extra space except for a few variables to store the results.  
