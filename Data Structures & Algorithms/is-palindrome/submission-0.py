class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for char in s:
            if char.isalnum():
                processed += char.lower()
        
        arr = list(processed)
        l, r = 0, len(arr)-1
        while (l < r):
            if arr[l] != arr[r]: return False
            l += 1
            r -= 1

        return True    
    
