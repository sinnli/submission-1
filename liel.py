import argparse


parser = argparse.ArgumentParser('Describe your program here for help')
parser.add_argument('--task', dest="task", type=str, default="0")
parser.add_argument('--arg', dest="argo", default="0")
arg = parser.parse_args()

task = arg.task
arg = arg.argo

# entering the given task with the if loop
if task =='perfect' or task == 'vowels' or task == 'lazy':
    if task == 'perfect':
        # returns the value of the index given of the perfect power sequence
        pp = [1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, 169, 196, 216,
              225, 243, 256, 289, 324, 343, 361, 400, 441, 484, 512, 529, 576, 625, 676, 729, 784,
              841, 900, 961, 1000, 1024, 1089, 1156, 1225, 1296, 1331, 1369, 1444, 1521, 1600,
              1681, 1728, 1764, 1849, 1936, 2025, 2048, 2116, 2187, 2197, 2209, 2304, 2401, 2500,
              2601, 2704, 2744, 2809, 2916, 3025, 3125, 3136, 3249, 3364, 3375, 3481, 3600, 3721,
              3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 4913, 5041, 5184, 5329, 5476,
              5625, 5776, 5832, 5929, 6084, 6241, 6400]
        num=int(arg)-1
        int_pp = pp[num]
        print(int_pp)
    elif task == 'vowels':
        # counts all the vowals in the str given and sum the up
        counter1 = arg.count("a")
        counter2 = arg.count("e")
        counter3 = arg.count("i")
        counter4 = arg.count("o")
        counter5 = arg.count("u")
        counter6 = arg.count("y")
        counter7 = arg.count("A")
        counter8 = arg.count("E")
        counter9 = arg.count("I")
        counter10 = arg.count("O")
        counter11 = arg.count("U")
        counter12 = arg.count("Y")
        sum = counter1 + counter2 + counter3 + counter4 + counter6 + counter5 + counter7 + counter8 + counter9 + counter10 + counter11 + counter12

        print(sum)
    else:
        # returns the value of given index of the lazy number sequence
        lnum = float(arg)
        lnumber = (((lnum-1)**2+(lnum-1)+2)/2)
        lanumber = int(lnumber)
        print(lanumber)
else:
    # otherwise the task is a wrong input
    print('wrong input')
