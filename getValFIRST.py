import pickle

__author__ = 'sri'
ip = open('/home/sri/p/proj/featVal/ka/hexVal54.txt', 'r')
op = open('/home/sri/p/proj/featVal/kaTrial/hexVal.pickle', 'w')
gridNum = int(ip.readline())
val = float(ip.readline())
feat = {}
while gridNum is not None:
    feat[gridNum] = [1, val]
    readGridVal = ip.readline()
    if readGridVal == '':
        break
    else:
        gridNum = int(readGridVal)
    val = float(ip.readline())

pickle.dump(feat, op)
for k in feat.keys():
    print feat[k]
