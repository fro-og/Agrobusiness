# var = {}
# count = [0, 0]
# with open("file.csv", mode="r", encoding="utf-8") as f:
#     for line in f:
#         name = line.split('","')[0]
#         if name not in var:
#             var[name] = []
#         if "пшениця" in line.lower():
#             var[name].append(line)
#             count[0] += 1
#         count[1] += 1
# i=-1
# for line in var:
#     i+=1
#     with open(f"{i}.csv", mode="w", encoding="utf-8") as f:
#         for text in var[line]:
#             f.write(text)

# for line in list(var):
#     print(line)

# print(count)





# rewrite = []
# with open(f"sowing_area.csv", mode='r', encoding='utf-8') as f:
#     for line in f:
#         rewrite.append(line)
# with open(f"sowing_area.csv", mode='w', encoding='utf-8') as f:
#     for line in rewrite:
#         a = line.split('",', 1)
#         try:
#             f.write(a[1])
#         except:
#             print(line)






# for j in range(4):
#     rewrite = []
#     name = {}
#     with open(f"{j}.csv", mode='r', encoding='utf-8') as f:
#         for line in f:
#             a = line.strip().split('",')
#             k = a[0] + '",' + a[1] + '",' + a[2] + '","' + a[3] + '","'
#             metric = a[3]

#             if k not in name:
#                 name[k] = [0]*12
#             for i in range(11):
#                 if a[i+5][1:]:
#                     name[k][i] += float(a[i+5][1:]) * (1000)**("Тисяча" in metric)
#             if a[11+5][1:1]:
#                 name[k][11] += float(a[11+5][1:-1]) * (1000)**("Тисяча" in metric)

#     print(name)

#     with open(f"{j}_1.csv", mode='w', encoding='utf-8') as f:
#         for line in name:
#             f.write(line + '","'.join([str(i) for i in name[line]]) + "\n")


# file = "a_sowing_area.csv"
# to_rewrite = dict()
# with open(file, mode='r', encoding='utf-8') as f:
#     for line in f:
#         name = line.split('",', 1)[0]
#         if name not in to_rewrite:
#             to_rewrite[name] = line
#         else:
#             vals = to_rewrite[name].split('","')[3:]
#             vals[-1] = vals[-1][:-1]
#             vals2 = line.split('","')[3:]
#             vals2[-1] = vals[-1][:-1]

#             res = []
#             for i in range(12):
#                 a, b = 0, 0
#                 if vals[i]:
#                     a = float(vals[i])
#                 if vals2[i]:
#                     b = float(vals2[i])
#                 res.append(str(a + b))
#             to_rewrite[name] = '",'.join(to_rewrite[name].split('","')[:3]) + '","'.join(res) + "\n"
# print(to_rewrite)
# with open(f"b{file}", mode='w', encoding='utf-8') as f:
#     for line in to_rewrite.values():
#         f.write(line)



# vals = []
# i = 0
# with open("file.csv", mode='r', encoding='utf-8') as f:
#     for line in f:
#         i+=1
#         try:
#             if line.split('","')[10] not in vals:
#                 vals.append(line.split('","')[10])
#                 print(i)
#         except:
#             pass

# print(vals)