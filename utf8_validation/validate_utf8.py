def validUTF8(data):
    # Helper function to check if a given byte is a valid start of a UTF-8 character
    def is_start_of_char(byte):
        return bin(byte).count('1') == 1
    
    # Iterate through the data
    i = 0
    while i < len(data):
        byte = data[i]
        
        # Determine the number of bytes in the current UTF-8 character
        if byte & 0x80 == 0:  # 1-byte character
            length = 1
        elif byte & 0xE0 == 0xC0:  # 2-byte character
            length = 2
        elif byte & 0xF0 == 0xE0:  # 3-byte character
            length = 3
        elif byte & 0xF8 == 0xF0:  # 4-byte character
            length = 4
        else:
            return False  # Invalid UTF-8 encoding
        
        # Check if there are enough bytes in the data
        if i + length > len(data):
            return False
        
        # Check if the following bytes are valid continuations
        for j in range(1, length):
            if not (data[i + j] & 0xC0 == 0x80):
                return False
        
        i += length  # Move to the next character
    
    return True

# Example usage:
data_set = [197, 130, 1]
result = validUTF8(data_set)
print(result)

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
