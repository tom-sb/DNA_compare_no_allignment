from fastopic import Seqpic
from toolstat import Statpic
import os

fastaFile = input('ingreser nombre de archivo contenedor de archivos .fasta: ')+'/'
outpath = "out"+fastaFile
##############################
with os.scandir() as itr: 
    find = False
    for entry in itr :
        if entry.name+'/' == outpath:
            find = True
            break
    if find == False:
        os.mkdir(outpath)
###############################


arr = os.listdir(fastaFile)
n = len(arr)
picarr=[]

for i in range(n):
	picarr.append(Seqpic(fastaFile+arr[i],outpath))

statarr = []
for i in range(n):
	picarr[i].picShow()
	picarr[i].histShow()
	stat = Statpic(picarr[i])
	statarr.append(stat.makeVecFeatures())

for i in range(n):
	print(statarr[i])
