class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = arr[-1]
        i = len(arr)-2
        while i>=0:
            if arr[i]>=max_so_far:
                current = arr[i]
                arr[i] = max_so_far
                max_so_far = current
                i-=1
            else:
                arr[i] = max_so_far
                i-=1
        arr[-1] = -1
        return arr