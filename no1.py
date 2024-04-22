def count_abc_deletions(s):
    deletions = 0
    i = 0
    
    while i < len(s) - 2:
        # Check if the current three characters form "abc"
        if s[i:i+3] == 'abc':
            # Increment the deletion count
            deletions += 1
            # Remove "abc" from the string
            s = s[:i] + s[i+3:]
            # Start checking again from the beginning of the string
            i = 0
        else:
            # Move to the next character
            i += 1
            
    return deletions

# Contoh penggunaan
s = "acaabcbcd"
total_deletions = count_abc_deletions(s)
print("Total penghapusan yang berhasil dilakukan:", total_deletions)
