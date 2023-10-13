import json
d1={'name':'vishal','roll no':1}
json_data=json.dumps(d1)
print(json_data)

d2=json.loads(json_data)
print(d2)
