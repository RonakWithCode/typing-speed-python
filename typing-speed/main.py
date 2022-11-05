from time import *
import random as r


def GetError(staring1,getinput):
    error = 0
    for i in range(len(staring1)):
        try:
            if staring1[i] !=getinput[i]:
                error= error+1
        except :
            error = error +1
    return error

def GetSpeed(StartTime,EndTime,getInput):
    timeDely = EndTime - StartTime 
    time_round = round(timeDely,2)
    speed = len(getInput)/time_round
    return round(speed)
    

text = ["Red data book is the document established by IUCN for documenting the rare and endangered species of plants, animals, fungi and also a few local species that exist within a state or country",  
        "Python is a high-level programming language designed to be easy to read and simple to implement. It is open source, which means it is free to use,",
        "a very strong man-made material that is used for making clothes, rope, brushes, etc.",
        "man-made made by people, not formed in a natural way; artificial","This is best app","Ronak is best Coder"]
staring1 = r.choice(text)
print()
print("         **********Welcome to Speed Calculator**********         ")
print(staring1)
print()
print()
startTime = time()
getinput = input("Enter text : ")
endTime = time()
print()
print("Speed : ",GetSpeed(startTime,endTime,getinput),"w/sec")
print()
print("error : ",GetError(staring1,getinput))