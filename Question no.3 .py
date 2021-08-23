# Q.3 Python object ko json string mai convert karne ka program 
# likho?

import json

d={"name": "punam","class":1,"age":12}
m=json.dumps(d)
print(m)



# out_file = open("myfile.json", "w")

# json.dump(dict1, out_file, indent = 6)

# out_file.close() 

# import json

# a={‘lalalala’: 3}
# mystring = json.dumps(a)
# print(mystring)
 