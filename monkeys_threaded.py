from random import randint
import time
import threading
#1836141229362619 = "i eat pi"
#1836141229362619361229362334361725312814 = "i eat pi at my house"

#test = "183614"
#start_time = time.time()
def stuff():
    test = "1836141229362619361229362334361725312814"

    foundWord = 0
    wordLength = 20
    #word = ""
    while(foundWord != 1):
         #start_time = time.time()
         threads = 0
         threads = t.enumerate()
         print(threads)
         word = ""
         for j in range(0, wordLength):
            word = word+str(randint(10,36))
            #print(word)
            
         if test == word:
            return '1'
            foundWord = 1
            t.daemon=False                  #change daemon to false to kill threads when it finds the word
            #print(total_time)
            
#stuff()
start_time = time.time()

threads = []
for i in range(4):                          #basically creating a thread pool of size 4 for now
    t = threading.Thread(target = stuff)    #start threads doing the function
    threads.append(t)                       #append the threads to create the number of threads
    t.daemon = True                         #set a daemon to true because otherwise it won't stop the threads
    t.start()                               #set the threads on
    
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