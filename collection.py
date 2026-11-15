from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a="aaaaabbbbcc"
my_counter=Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

point=namedtuple("Point","x,y")
pt=point(1,-4)
print(pt)
print(pt.x,pt.y)

orderDict={}
orderDict['b']=2
orderDict['c']=3
orderDict['d']=5
orderDict['a']=1
print(orderDict)

d=defaultdict(int)
d['a']=1
d['b']=2
print(d['c'])

d=deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.extend([5,6,7])
d.pop()
print(d)
