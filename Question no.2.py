# Q.2 Python object ko json data main convert karne ka program likho?

import json
dict1={"name": "David",
     "class":"I",
     "age": 6  
 }
out_file = open("myfile.json", "w")
json.dump(dict1, out_file, indent = 6)
out_file.close() 