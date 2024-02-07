def is_match(text: str, pattern: str):
	# Dynamic programming matrix to store the match status
	dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
	
	# Empty pattern matches empty text
	dp[0][0] = True
	
	print(dp)
	# # Handle patterns with '*'
	for j in range(1, len(pattern) + 1):
	    if pattern[j - 1] == '*':
	        dp[0][j] = dp[0][j - 2]
	
	# # Build the matrix based on the characters in text and pattern
	for i in range(1, len(text) + 1):
	    for j in range(1, len(pattern) + 1):
	        if pattern[j - 1] == text[i - 1] or pattern[j - 1] == '.':
	            dp[i][j] = dp[i - 1][j - 1]
	        elif pattern[j - 1] == '*':
	            dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (text[i - 1] == pattern[j - 2] or pattern[j - 2] == '.'))

	return dp[len(text)][len(pattern)]

# Example usage:
text = "aab"
pattern = "c*a*b"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "aa"
pattern = "a"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "aa"
pattern = "a*"
result = is_match(text, pattern)
print(result)  # Output: True

# Example usage:
text = "ab"
pattern = ".*"
result = is_match(text, pattern)
print(result)  # Output: True
