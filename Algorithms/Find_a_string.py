# def count_substring(string, sub_string):
#     return 


times = 0

if __name__ == '__main__':
    string, substring = ("ABCDCDCDC".strip(), "CDC".strip())
    for counter in range(len(string)):
        if string[counter:counter+len(substring)] == substring:
            times += 1

    # print(times)

    print(sum([1 for counter in range(len(string)) if string[counter:counter+len(substring)] == substring]))
            
    # print(sum([ 1 for _ in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring]))
