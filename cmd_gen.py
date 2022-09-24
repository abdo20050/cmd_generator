# Bismellah 
#This code is made only for educational purposes, any misuse programmer won't be responsible
#Description: This code used to generate cmd files for "irsim" simulator
import os

import sys, getopt

fileName = ""
stepSize = 50
labels = [str("")]*20
I = ""
O = ""

def main(argv):
    global fileName
    global I
    global O
    try:
        opts, args = getopt.getopt(argv,"hn:i:o:",["filename=","iLabels=","oLabels="])
    except getopt.GetoptError:
        print ("cmd_gen.py -n <fileName> -i <inputLabels> -o <outputLabels>")
        sys.exit()
    for opt, arg in opts:
            if opt == '-h':
                print ("cmd_gen.py -n <fileName> -i <inputLabels> -o <outputLabels>")
                sys.exit()
            elif opt in ("-n", "--fileName"):
                fileName = arg
            elif opt in ("-i", "--iLabel"):
                I = arg
            elif opt in ("-o", "--oLabel"):
                O = arg
    fileName = fileName or "GG"
    I = I or "a b"
    O = O or "o"
if __name__ == "__main__":
   main(sys.argv[1:])
print("file Name is",fileName)
print ("Input labels are ", I)
print ("Output labels are ", O)


f = open(fileName+".cmd","w")
# print("Input your fileName:\n")
# file name = input()
# print("Input your stepSize:")
# stepSize = input()

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
