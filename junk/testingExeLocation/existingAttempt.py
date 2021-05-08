import datetime
from os.path import abspath
from os.path import basename
from inspect import getsourcefile


file_name = 'filename' + datetime.datetime.now().strftime("-%m-%d-%Y--%H-%M-%S") + '.json'
file_plus_path = str(abspath(getsourcefile(lambda:0))).replace(basename(__file__), '') + file_name
print('path: '+str(file_plus_path))
