class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        swap_right = float("inf")
        index = 0
        swap_left, check = 0, 0
        for right in range(len(arr)-2, -1, -1):
            if arr[right] > arr[right+1]:
                swap_left = right
                break
        
        for index in range(swap_left+1, len(arr)):
            if 0 < arr[swap_left] - arr[index] < swap_right:
                swap_right = arr[swap_left] - arr[index]
                check = index

        
        arr[swap_left], arr[check] =  arr[check], arr[swap_left]
        return arr
