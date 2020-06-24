import csv, json, subprocess


def csv2json(csvFile, jsonFile, rootHeader=None):
    data = []
    with open(csvFile, "r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for csvRow in csvReader:
            data.append(csvRow)

    root = {}
    root[rootHeader] = data

    with open(jsonFile, 'w') as jsonFile:
        jsonFile.write(json.dumps(root, indent=4))

    with open('output.json', 'r') as f:
        output = f.read()
        return output


def cert_validity():
    subprocess.run('./cert_validity.sh', shell=True)
    csvFile = 'output.csv'
    jsonFile = 'output.json'
    rootHeader = 'cert_validity'
    return(csv2json(csvFile, jsonFile, rootHeader))
    

def monit_summary():
    # subprocess.run('./cert_validity.sh', shell=True, capture_output=True)
    csvFile = 'monit.csv'
    jsonFile = 'output.json'
    rootHeader = 'monit_summary'
    return(csv2json(csvFile, jsonFile, rootHeader))
    

def disk_usage():
    subprocess.run('./df_usage.sh', shell=True)
    csvFile = 'output.csv'
    jsonFile = 'output.json'
    rootHeader = 'disk_usage'
    return(csv2json(csvFile, jsonFile, rootHeader))


print(monit_summary())
print(cert_validity())
print(disk_usage())