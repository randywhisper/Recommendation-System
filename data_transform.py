import csv
import json


class data_transform:
    def __init__(self,file_name):
        self.file_name = file_name


    def tran_json(self):
        f = open(self.file_name)
        self.data = [json.loads(line.rstrip()) for line in f]
        return self.data
        
