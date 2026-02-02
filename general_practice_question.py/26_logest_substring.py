def length_of_longest_substring(s):
    char_map = {}
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # If character is already in our map, move the left pointer
        if s[right] in char_map:
            # We move 'left' to the right of the previous occurrence
            left = max(left, char_map[s[right]] + 1)
            
        # Store/update the index of the character
        char_map[s[right]] = right
        
        # Calculate current window size
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Example
text = "abcabcbb"
print(f"The length is: {length_of_longest_substring(text)}") # Output: 3 ("abc")