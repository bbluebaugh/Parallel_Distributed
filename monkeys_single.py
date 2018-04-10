from random import randint
import time
#1836141229362619 = "i eat pi"
test = "1836141229"
start_time = time.time()
def stuff():

    foundWord = 0
    wordLength = 5
    #word = ""
    while(foundWord != 1):
         #start_time = time.time()
         word = ""
         for j in range(0, wordLength):
             word = word+str(randint(10,36))
             #print(word)
         if test == word:
             return '1'
             foundWord = 1
             #print(total_time)
stuff()
#start_time = time.time()
print("!-> Stuff Happened")
    #run = 0
    #total = (total)*1458
#print("hi")
finish_time = time.time()
total_time = finish_time - start_time
if total_time < 60:
    print("It took: " + str(total_time) + " seconds.")
elif total_time < 3600:
    total_time = total_time / 60
    print("It took: " + str(total_time) + " minutes")
elif total_time < 86400:
    total_time = total_time / 3600
    print("It took: " + str(total_time) + " hours")
else:
    total_time = total_time / 86400
    print("It took: " + str(total_time) + " days")
found_it = "We finished             <<<"
print(found_it)