import argparse
# counting vowels of given strings concluding y
task2 = "kj0944eaa8kjhkjgerfqeygjxteeeuhyddetertsaekl"

counter1 = task2.count("a")
counter2 = task2.count("e")
counter3 = task2.count("i")
counter4 = task2.count("o")
counter5 = task2.count("u")
counter6 = task2.count("y")
sum2 = counter1+counter2+counter3+counter4+counter6+counter5

print(sum2)

task1 = "eaiouyyuyuheeeuyykj  jhjkl; rtweta4juureeikojyyee'54767 "

count1 = sum(map(lambda x : 1 if 'a' in x else 0, task1))
count2 = sum(map(lambda x : 1 if 'e' in x else 0, task1))
count3 = sum(map(lambda x : 1 if 'i' in x else 0, task1))
count4 = sum(map(lambda x : 1 if 'o' in x else 0, task1))
count5 = sum(map(lambda x : 1 if 'u' in x else 0, task1))
count6 = sum(map(lambda x : 1 if 'y' in x else 0, task1))

sum1 = count1+count2+count3+count4+count5+count6

print(sum1)

