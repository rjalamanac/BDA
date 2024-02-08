from pywebhdfs.webhdfs import PyWebHdfsClient
from pprint import pprint
hdfs = PyWebHdfsClient(host='10.2.14.251',port='9870', user_name='root')
my_data = '01010101010101010101010101010101'
my_file = '/data/myfile.txt'
hdfs.create_file(my_file, my_data)

