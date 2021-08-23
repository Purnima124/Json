import json
dict1={
    "Name":"Abhishek",
    "Designation":"CEO of navgurukul",
    "Gender male":"IV",
    "Age":29
}
file=open("q7.json","w")
json.dump(dict1,file,indent=2)
file.close()
# a='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'