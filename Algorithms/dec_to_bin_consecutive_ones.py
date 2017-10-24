from dec_to_bin import toBin

bin_num = "110111"
forw = 0
controll = int(bin_num[0])
cons_one = 0
max_cons = 0

for counter in bin_num:
    if int(counter) == 1:
        cons_one += 1
        if cons_one > max_cons:
            max_cons = cons_one
    if int(counter) == 0:
        cons_one = 0

print max_cons
