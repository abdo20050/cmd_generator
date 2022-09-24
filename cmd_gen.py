# Bismellah 
#This code is made only for educational purposes, any misuse programmer won't be responsible
#Description: This code used to generate cmd files for "irsim" simulator
import os
def grayGen(num):
    return num ^ (num >> 1)

# print("Input your fileName:\n")
# file name = input()
# print("Input your stepSize:")
# stepSize = input()
fileName = str(input("Input your file name [default is 'GG']:\n") or "GG")
f = open(fileName+".cmd","w")
stepSize = int(input("Enter your StepSize [default is '50':]\n") or 50)
labels = [str("")]*20
I = str(input("Input your input labels [you can add up to 20 labels] [ default is 'a b']:\n") or "a b")
O = str(input("Input your output labels [ default is 'o']:\n") or "o")
numOfI = 0
for i in I :
    if i != ' ' :
        labels[numOfI] += i
    else:
        numOfI += 1
numOfI = 0
for i in labels:
    if i != "":
        numOfI += 1
    else:
        break
numOfIter = 2**numOfI
signals = [0]*(numOfIter)
for i in range(numOfIter):
    signals[i] =  i
txt = ""
txt += "stepsize "+str(stepSize)+'\n'
txt += "ana vdd gnd "+I + " " + O + '\n'
txt += "w vdd gnd "+I + " " + O + '\n'
txt += "h vdd \n"
txt += "l gnd \n"

for i in range(numOfIter):
    for j in range(numOfI):
        txt += ('h' if (signals[i]>>j & 1) else 'l')+' '+labels[j] + '\n'
    txt += "s\n"
f.write(txt)
f.close()
os.system("open "+f.name)

### Made by abdo25 ###
### github.com/abdo20050 ###
