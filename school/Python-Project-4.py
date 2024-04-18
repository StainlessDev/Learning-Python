def concat_reverse_order(str1, str2, str3):
    parts1 = str1.split()
    parts2 = str2.split()
    parts3 = str3.split()

    all_parts = parts3 + parts2 + parts1  # Adding lists in reverse order
    reversed_parts = all_parts[::-1]     # Reverse the combined list
    

    return ' '.join(reversed_parts)
if __name__ == '__main__':
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    string3 = input("Enter the third string: ")

    result = concat_reverse_order(string1, string2, string3)

    print("The concatenated result in reverse order is:", result)