
# begins with 1 without dublicates
index = 100

pp = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216,\
     225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625, 676, 729, 784,\
     841, 900, 961, 1000, 1024, 1089, 1156, 1225, 1296, 1331, 1369, 1444, 1521, 1600,\
     1681, 1728, 1764, 1849, 1936, 2025, 2048, 2116, 2187, 2197, 2209, 2304, 2401, 2500,\
     2601, 2704, 2744, 2809, 2916, 3025, 3125, 3136, 3249, 3364, 3375, 3481, 3600, 3721,\
     3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 4913, 5041, 5184, 5329, 5476,\
     5625, 5776, 5832, 5929, 6084, 6241, 6400]
#print(pp)

int_pp = pp[index-1]
#print(int_pp)




def power(task: int) -> int:
    """
    getting index of perfect power sequence
    :param int task: getting index
    :return int: value in pp sequence
    """
    return pp[task-1]
t =10
y = power(t)
#print(y)














def is_perfect_power(a, b):
  while a % b == 0:
    a = a / b
  if a == 1:
    return True
  return False







#pp2 = [ x for x in range( 100 ) if is_perfect_power( x, 2) ]
print(pp2)
d = [1, 2, 3, 4, 5, 6, 7 ,8 ,9,10]

perfect_list = list(set([x ** i for x in range(1, 100) for i in range(2, 30) if (x ** i) < 6410]))
perfect_list.sort()
pp1 = perfect_list.sort()
print(pp1)
print(perfect_list)
if pp == perfect_list:
    print("true")
else:


    print("false")
print(len(perfect_list))
print(len(pp))


pp == pp1




