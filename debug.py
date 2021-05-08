lst_1 = [1, 3, 6]
lst_2 = [1, 5]
lst_1.sort(reverse=True)
lst_2.sort(reverse=True)
print(lst_1, lst_2)
out = []
idx_1, idx_2 = 0, 0
for i in range(len(lst_1) + len(lst_2)):
    if lst_1[idx_1] >= lst_2[idx_2]:
        out.append(lst_1[idx_1])
        idx_1 += 1
        if idx_1 == len(lst_1):
            out.extend(lst_2[idx_2:])
            break
    else:
        out.append(lst_2[idx_2])
        idx_2 += 1
        if idx_2 == len(lst_2):
            out.extend(lst_1[idx_1:])
            break
print(out)