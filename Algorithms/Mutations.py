def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]






if __name__ == '__main__':
    s = 'abracadabra'
    i, c = '5','G'
    s_new = mutate_string(s, int(i), c)
    print(s_new)
