def grayGen(num):
    return num ^ (num >> 1)

# print("Input your fileName:\n")
# file name = input()
# print("Input your stepSize:")
# stepSize = input()
print("Input your labels [you can add up to 20 labels]:\n")
labels = ['']*20
I = "a b c d"
I = input()
numOfI = 0
for i in I :
    if i != ' ' :
        labels[numOfI] = i
        numOfI += 1
numOfIter = 2**numOfI
signals = [[False]*numOfI]*(numOfIter)
for i in range(numOfIter):
    signals[i] =  grayGen(i)

print("stepsize 50")
print("ana vdd gnd "+I)
print("w vdd gnd "+I)
print("h vdd")
print("l gnd")
for i in range(numOfIter):
    for j in range(numOfI):
        print(('h' if (signals[i]>>j & 1) else 'l')+' '+labels[j])
    print('s')
# print(numOfI)
# for i in labels:
#     if i == '':
#         break
#     print(i)
#     print(' ')
#print(I)


