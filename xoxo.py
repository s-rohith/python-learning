import csv, json, subprocess, os
from flask import Flask

app = Flask(__name__)

def csv2json(csvFile, jsonFile, rootHeader=None):
    data = []
    with open(csvFile, "r") as csvFile:
        csvReader = csv.DictReader(csvFile, delimiter=',')
        for csvRow in csvReader:
            data.append(csvRow)


    root = {}
    root['Host_Name'] = hostName.stdout.rstrip()
    root['Host_IP'] = hostIP.stdout.rstrip()
    root[rootHeader] = data


    with open(jsonFile, 'w') as jsonFile:
        jsonFile.write(json.dumps(root, indent=4))

    with open('./output/output.json', 'r') as f:
        output = f.read()
        return output


# def execute_shell_command(cmd, work_dir):
#     pipe = subprocess.Popen(cmd, shell=True, cmd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     (out, error) = pipe.communicate()
#     pipe.wait()

@app.route('/')
def userhelp():
    return """
Try the following api,

    curl localhost:8081/api/monit
    curl localhost:8081/api/disk
    curl localhost:8081/api/certs

"""

@app.route('/api/certs')
def cert_validity():
    # work_dir = './utils/'
    # cmd = './cert_validity.sh'
    # execute_shell_command(cmd, work_dir)
    subprocess.run('./utils/cert_validity.sh', shell=True)
    csvFile = './output/output.csv'
    jsonFile = './output/output.json'
    rootHeader = 'cert_validity'
    return(csv2json(csvFile, jsonFile, rootHeader))


# def cert_validity():
#     subprocess.run('./cert_validity.sh', shell=True)
#     csvFile = './output/output.csv'
#     jsonFile = './output/output.json'
#     rootHeader = 'cert_validity'
#     return(csv2json(csvFile, jsonFile, rootHeader))
    

@app.route('/api/monit')
def monit_summary():
    # subprocess.run('./cert_validity.sh', shell=True, capture_output=True)
    csvFile = './output/monit.csv'
    jsonFile = './output/output.json'
    rootHeader = 'monit_summary'
    return(csv2json(csvFile, jsonFile, rootHeader))
    

@app.route('/api/disk')
def disk_usage():
    # work_dir = './utils/'
    # cmd = './df_usage.sh'
    # # execute_shell_command(cmd, work_dir)
    subprocess.run('./utils/df_usage.sh', shell=True)
    csvFile = './output/output.csv'
    jsonFile = './output/output.json'
    rootHeader = 'cert_validity'
    return(csv2json(csvFile, jsonFile, rootHeader))

# def disk_usage():
#     subprocess.run('./df_usage.sh', shell=True)
#     csvFile = 'output.csv'
#     jsonFile = 'output.json'
#     rootHeader = 'disk_usage'
#     return(csv2json(csvFile, jsonFile, rootHeader))


# print(monit_summary())
# print(cert_validity())
# print(disk_usage())

hostName = subprocess.run(['hostname'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', universal_newlines=True)
hostIP = subprocess.run("hostname -I | awk '{print $1}'", shell=True,  stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8', universal_newlines=True)

if __name__ == '__manin__':
    app.run(host='0.0.0.0', port=8081)