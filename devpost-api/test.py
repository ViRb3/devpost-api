import api
import json
import sys

test_userdata_file = 'test-userdata.json'
test_projectdata_file = 'test-projectdata.json'

userdata = api.get_user('vala')
projectdata = api.get_project('cat-house')

def compare_data(filename, data):
    with open(filename) as file:
        testdata = json.load(file)
        a, b = json.dumps(testdata, sort_keys=True), json.dumps(data, sort_keys=True)
        if a != b:
            print(a)
            print(b)
            return False
    return True

def dump_data():
    test_userdata = json.dumps(userdata, indent=4, sort_keys=True)
    test_projectdata = json.dumps(projectdata, indent=4, sort_keys=True)
    with open(test_userdata_file, 'w') as file:
        file.write(test_userdata)
    with open(test_projectdata_file, 'w') as file:
        file.write(test_projectdata)
    sys.exit(0)

# dump_data()

if not compare_data(test_userdata_file, userdata):
    sys.exit(1)
if not compare_data(test_projectdata_file, projectdata):
    sys.exit(2)
