# n, m = int(9), int(27)
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
n = int(17)
width = len("{0:b}".format(n))
for i in frange(1,n+1):
  print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, wis
                                                                     dth=width)
        
