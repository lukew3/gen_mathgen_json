from mathgenerator import mathgen
import json

"""
This script will write a json file with data about the mathgenerator generators including a number of samples formatted to json.
The following is a simplified version of what the json will look like after completion:
[
    {
        name="Addition",
        id=0,
        kwargs=[
            "maxSum=99",
            "maxAddend=50"
        ]
        samples=[
            {
                problem: "2+7=",
                solution: "9",
            }
        ]
    }
]

"""
data = []

print(mathgen.getGenList())
for item in mathgen.getGenList():
    samples = []
    for _ in range(10): #should be 100 after testing
        prob, sol = mathgen.genById(item[0])
        samples.append({"problem": prob, "solution": sol})
    data_obj = {
            "name": item[1],
            "id": item[0],
            "subject": item[4],
            "function_name": item[3],
            "samples": samples,
            "kwargs": item[5]
    }
    data.append(data_obj)
print(json.dumps(data, indent = 4, sort_keys=True))

with open('data.json', 'w') as json_file:
  json.dump(data, json_file, indent = 4, sort_keys=True)
