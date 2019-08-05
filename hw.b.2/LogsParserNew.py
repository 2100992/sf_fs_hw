import json
#from collections import defaultdict

log1_filename = './hw.b.2/data_500.json'
log2_filename = './hw.b.2/data_3000.json'

'''
def getDeserLog(filename):
    with open(filename) as fp:
        data = fp.readlines()
    dslog = []
    for record in data:
        dslog.append(json.loads(record.strip('\n')))
    return dslog
    '''

def getDeserLog(filename):
    with open(filename) as fp:
        data = fp.readlines()
    dslog = [json.loads(record.strip('\n')) for record in data]
    return dslog




def main():
    data1 = getDeserLog(log1_filename)
    print(data1[0]["timestamp"])

    data2 = getDeserLog(log2_filename)
    print(data2[0]["timestamp"])


if __name__ == "__main__":
    main()