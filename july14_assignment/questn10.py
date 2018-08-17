from collections import namedtuple
from collections import OrderedDict

Employee = namedtuple("Employee", ["id", "title", "salary"])
e = Employee(1, "engineer", 10000)

print(e)
print("Title is", e.title)

d = OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
   print (k, v)