# import json
# dict1={"Name":"Ram", 
#     "Class":"IV", 
#     "Age":9 },
# a=json.loads(dict1)
# print(a)

# Q.1 Json data ko python object main convert karne ka program likho?.
#  Example:Input :
# oad():- load() method ek json object or json file ko json data ke sath python object(dictionaries)
#  mai karta hai. loads() method ek json string leta hai or use json objects mai convert ker deta hai.

import json
dict1={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
file=open("my_file.json","r+")
n=json.load(file)
# print(n)
file.close()


