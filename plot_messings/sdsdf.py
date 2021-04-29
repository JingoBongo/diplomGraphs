from os.path import abspath
from os.path import basename
from inspect import getsourcefile
import re

# abspath(getsourcefile(lambda:0))
# print(basename(__file__))
# print(str(abspath(getsourcefile(lambda:0))).replace(basename(__file__),''))
# print(abspath(getsourcefile(lambda:0)))

a = ['[', '', '0.', '', '', '', '', '', '90.3687', '192.8256', '108.9082', '186.435', ']']
result = re.findall(r"[-+]?\d*\.\d+|\d+", str(a[0]))[0]
print(result)