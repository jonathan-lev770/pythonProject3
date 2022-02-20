import json

# dict in the form of a string
odics = '{"K1": "val1", "K2": "val2"}'

# to pass this string in json format, import json
# using json class with loads method( ) passing our string/dictionary, it will PARSE our string as json format
odics_json_result = json.loads(odics)
print(odics_json_result)







