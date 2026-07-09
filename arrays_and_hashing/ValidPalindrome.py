# This program check if two strings are palindrome or not
class ValidPalindrome:
    def CheckPalindrome(self, str1):
        return (str1 == str1[::-1])
    
    def AdditionalCheckPalindrome(self, str1):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_str = ''.join(char.lower() for char in str1 if char.isalnum())
        return cleaned_str == cleaned_str[::-1]
    
    def CheckPalindromeWithTwoPointers(self, str1):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_str = ''.join(char.lower() for char in str1 if char.isalnum())
        left, right = 0, len(cleaned_str) - 1
        
        while left < right:
            if cleaned_str[left] != cleaned_str[right]:
                return False
            left += 1
            right -= 1
            
        return True
            

if __name__ == "__main__":
    sol = ValidPalindrome()
    # Try these once you've written your solution:
    print(sol.AdditionalCheckPalindrome("A man, a plan, a canal: Panama"))     # True
    print(sol.AdditionalCheckPalindrome("race a car"))                         # False
    print(sol.AdditionalCheckPalindrome(" "))                                  # True
    print(sol.CheckPalindromeWithTwoPointers("A man, a plan, a canal: Panama"))     # True
    print(sol.CheckPalindromeWithTwoPointers("race a car"))                         # False
    print(sol.CheckPalindromeWithTwoPointers(" "))                                  # True