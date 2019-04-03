import json
print("Please enter the data")
raw_data = input()
loaded_json = json.loads(raw_data)
for question in loaded_json.get('resInfo').get('testQuesList'):
#	for question in QuesList['testQuesList']:
	index = question['quesIndex']
	keys = question['quesAnswer']
	keys = keys.replace('<as>','')
	keys = keys.replace('</as>','')
	keys = keys.replace('</a>',' ')
	keys = keys.replace('<a>','')
	print(index + ':')
	print(keys)
