import csv, json

csvFilePath = 'sample.csv'
jsonFilePath = 'output.json'


def csv2json():
    data = []
    with open(csvFilePath, "r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for csvRow in csvReader:
            data.append(csvRow)

    root = {}
    root['employee_data'] = data

    with open(jsonFilePath, 'w') as jsonFile:
        jsonFile.write(json.dumps(root, indent=4))

    with open('output.json', 'r') as f:
        output = f.read()
        return output

print(csv2json())

