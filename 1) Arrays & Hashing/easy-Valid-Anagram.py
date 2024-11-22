class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        # My solution

        return sorted(s) == sorted(t)


        # optimal solution

        # check the length
        if len(s) != len(t):
            return False
        # list of 26 zeroes for each letter in alphabet
        count = [0] * 26
        # iterate through and add each character and their number of occurences
        for i in range(len(s)):
            # ord(s[i]) gives the ASCII value of the character s[i].
            # ord('a') is subtracted to calculate the 0-based index of the character.
            count[ord(s[i]) - ord('a')] += 1
            # if t also has the same char, decrement back to 0
            count[ord(t[i]) - ord('a')] -= 1
        # check if the vals are zero
        for val in count:
            # if s and t are anagrams, there should be only 0s
            if val != 0:
                return False
        return True
