bin_num = "10001101" #141
pos_num = []
vet_length = len(bin_num)
aux_vet = []

while vet_length > 0:
    aux_vet.append(vet_length - 1)
    vet_length = vet_length - 1

num = 0
aux_count = 0

for counter in aux_vet:
    aux_count = aux_count + ((int(bin_num[num])*2)**int(counter))
    num += 1

print(aux_count)
