from fastopic import Seqpic
from toolstat import Statpic

mypic = Seqpic("sequence.fasta")
#mypic.picShow()
#mypic.histShow()

mystat = Statpic(mypic)
vec = mystat.makeVecFeatures()
print(vec)
