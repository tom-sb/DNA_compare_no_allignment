from fastopic import Seqpic
from toolstat import Statpic
from mypdist import Pdist
import os
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

fastaFile = input('ingreser nombre de archivo contenedor de archivos .fasta: ')+'/'
outpath = "out"+fastaFile
##############################
with os.scandir() as itr: 
	findin = False
	findout = False
	for entry in itr :
		if entry.name+'/' == fastaFile:
			arr = sorted(os.listdir(fastaFile))
			findin = True
		if entry.name+'/' == outpath:
			findout = True
	if findout == False:
		os.mkdir(outpath)
	if findin == False:
		print('error al ingresar directorio, "'+fastaFile+'" no existe, ingrese un directorio q exista.')
		raise SystemExit
###############################


#arr = sorted(os.listdir(fastaFile))

n = len(arr)
picarr=[]
labelarr=[]

for i in range(n):
	picarr.append(Seqpic(fastaFile+arr[i],outpath))

statarr = []
for i in range(n):
	#picarr[i].picShow()
	#picarr[i].histShow()
	labelarr.append(picarr[i].title)
	stat = Statpic(picarr[i])
	statarr.append(stat.makeVecFeatures())

#for i in range(n):
#	print(statarr[i])

pdist = Pdist(statarr)
vec = pdist.vector

Z=linkage(vec,'average')
#Z2=linkage(statarr,'single',metric='euclidean')

fig = plt.figure(figsize=(25,10))
dn = dendrogram(Z,orientation='left',labels=labelarr)
fig.tight_layout()
plt.show()
#dn2 = dendrogram(Z2)
#plt.show()

