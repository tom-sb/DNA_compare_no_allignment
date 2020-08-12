from fastopic import Seqpic
from toolstat import Statpic
import os

fastaFile = "bacterias/"

arr = os.listdir(fastaFile)
n = len(arr)
picarr=[]

for i in range(n):
	picarr.append(Seqpic(fastaFile+arr[i]))

statarr = []
for i in range(n):
	#picarr[i].picShow()
	picarr[i].histShow()
	stat = Statpic(picarr[i])
	statarr.append(stat.makeVecFeatures())

for i in range(n):
	print(statarr[i])
