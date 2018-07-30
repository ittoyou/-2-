
import re
ret = re.match(r'<(?P<name1>)\w+><(?P<name2>)\w+>.*</(?P=name2)></(?name1)>',str)
print(ret)
ret = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>.*</(?P=name2)></(?name1)>',str)
print(ret)
