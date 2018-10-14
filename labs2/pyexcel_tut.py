import pyexcel
from collections import OrderedDict
# int, str, list
# int("78")
data = [
    OrderedDict({
        "Name": 'Hoang Anh',
        "Age": 21,
    }),
    OrderedDict({
        "Name":"Hung",
        "Age": 22,
    }),
    OrderedDict({
        "Name": "Hau",
        "Age": 21,
    }),
]
pyexcel.save_as(records=data, dest_file_name="sample.xlsx")