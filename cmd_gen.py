# Bismellah 
#This code is made only for educational purposes, any misuse programmer won't be responsible
#Description: This code used to generate cmd files for "irsim" simulator
import os

import sys, getopt

fileName = ""
stepSize = 50
labels = [str("")]*20
bLabels = [str("")]*20
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

f = open(fileName+".cmd","w")
# print("Input your fileName:\n")
# file name = input()
# print("Input your stepSize:")
# stepSize = input()

#############sitting the labels
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
        if i[len(i)-1] == '`':
            bLabels.insert(0,i)
    else:
        break
##############removing nonBared label pair
for i in bLabels:
    if i == "":
        break
    try:
        labels.remove(i[:len(i)-1])
        #print("remove",i[:len(i)-1])
        numOfI-=1
    except:
        # print(i[:len(i)-1],"not found")
        continue
###########################
##########print in terminal
print("file Name is",fileName)
print ("Input labels are " ,end=' ')
for i in labels:
    if i == "":
        break
    if i[len(i)-1] == '`':
        print(i[:len(i)-1],end=' ')
    print(i,end = ' ')
print()
print ("Output labels are ", O)
##########################
numOfIter = 2**numOfI
txt = ""
txt += "stepsize "+str(stepSize)+'\n'
txt += "ana vdd gnd "+I + " " + O + '\n'
txt += "w vdd gnd "+I + " " + O + '\n'
txt += "h vdd \n"
txt += "l gnd \n"

for i in range(numOfIter):
    for j in range(numOfI):
        if '`' in labels[j]:
            txt += ('h' if (i>>j & 1) else 'l')+' '+labels[j][:len(labels[j])-1] + '\n'
            txt += ('l' if (i>>j & 1) else 'h')+' '+labels[j] + '\n'
        else:
            txt += ('h' if (i>>j & 1) else 'l')+' '+labels[j] + '\n'
    txt += "s\n"
f.write(txt)
f.close()
os.system("open "+f.name)



### Made by abdo25 ###
### github.com/abdo20050 ###
