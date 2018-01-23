if __name__ == '__main__':
    s = "qAv"
    print(any(char.isalnum() for char in s))
    # In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    print(any(char.isalpha() for char in s))
    # In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    print(any(char.isdigit() for char in s))
    # In the third line, print True if  has any digits. Otherwise, print False.
    print(any(char.islower() for char in s))
    # In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    print(any(char.isupper() for char in s))
    # In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
