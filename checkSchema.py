import json

def check_schema(srcfile, extracted_schema):
    with open('schemas.json', 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)
        c=0
        for d in data:
            if extracted_schema == d["required"]:
                print(d["title"], "is correct schema")
                c=1
                break
        if c==0:
            print("schema not matched")
            return False
        else:
            return True
