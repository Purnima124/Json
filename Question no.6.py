# import json
# a='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
# d=json.loads(a)
# print
# Q6.Python object key unique key value ko access karne ka program likho? Example: Input :- 
import json
a={"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}
print("original python object:")
print(a)
json_obj=json.dumps(a)
print("\nunique key in a json object")
print(json_obj)