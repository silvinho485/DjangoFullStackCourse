Mrange = int(4)
m = set(map(int, "2 4 5 9".split()))
Nrange = int(4)
n = set(map(int, "2 4 11 12".split()))
print("\n".join([str(x) for x in sorted((m ^ n))]))
# print("\n".join([dif for dif in m if dif not in n] + [dif for dif in n if dif not in m]))
# MinN =
# NinM =
            

