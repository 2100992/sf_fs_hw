import sys
import json
import pandas as pd
from collections import defaultdict, Counter

log1_filename = './hw.b.2/data_500.json'
log2_filename = './hw.b.2/data_3000.json'


def getDeserLog(filename):
    with open(filename) as fp:
        data = fp.readlines()
    dslog = []
    for record in data:
        dslog.append(json.loads(record.strip('\n')))
    return dslog

def getParameterValueCounter(deserData, parameter):
    valCounter = Counter()
    for record in deserData:
        valCounter[record[parameter]] +=1
    return valCounter

def getParameterValueSum(deserData, parameter, ifKey, ifVal):   # "eventType": "itemBuyEvent"
    valSum = 0
    counter = 0
    for record in deserData:
        if record[ifKey] == ifVal and not record['detectedCorruption'] and not record['detectedDuplicate']:
            valSum += int(record[parameter])
            counter += 1
    return [valSum, counter]

def getUniqueValCounterFromEventType(deserData, parameter, eventType):
    counter = Counter()
    for record in deserData:
        if record['eventType'] == eventType and not record['detectedCorruption'] and not record['detectedDuplicate']:
            counter[record[parameter]] += 1
    return counter

'''

def getDeserLog(filename):
    with open(filename) as fp:
        data = fp.readlines()
    dslog = [json.loads(record.strip('\n')) for record in data]
    return dslog

'''

 
def main():
    data1 = getDeserLog(log1_filename)

    clientCount1 = getParameterValueCounter(data1, 'userAgentName')
    print(f'Число различных браузеров в первом логе - {len(clientCount1)}')

    sumCount1 = getParameterValueSum(data1, 'item_price', "eventType", "itemBuyEvent")
    print(f'Всего покупок - {sumCount1[1]}\nСумма покупок - {sumCount1[0]}')



    data2 = getDeserLog(log2_filename)

    clientCount2 = getParameterValueCounter(data2, 'userAgentName')
    print(f'Число различных браузеров во втором логе - {len(clientCount2)}')

    sumCount2 = getParameterValueSum(data2, 'item_price', "eventType", "itemBuyEvent")
    print(f'Всего покупок - {sumCount2[1]}\nСумма покупок - {sumCount2[0]}')
    
    uniqItem_id = getUniqueValCounterFromEventType(data2, 'item_id', 'itemFavEvent')
    print(f'Во втором логе {len(uniqItem_id)} товаров в избранном')

    print(uniqItem_id)


if __name__ == "__main__":
    main()