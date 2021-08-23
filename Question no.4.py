# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne 
# ka program likho? Example: Input :- Output:- JSON data:
# 
import json
a={
    "4": 5, 
    "6": 7, 
    "1": 3, 
    "2": 4}
with open("myfile2.json","w")as f:
    json.dump(a,f, indent=4,sort_keys=True)
