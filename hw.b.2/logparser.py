from collections import defaultdict, Counter
import json

FILENAME = './hw.b.2/dummy-access.log'

def parse_line(text_line):
    dict_from_line = {}
    dict_from_line['ip'] = text_line.split()[0]
    dict_from_line['dt'] = text_line.split()[3].strip('[')
    dict_from_line['user_agent'] = text_line.split('"')[1]
    return dict_from_line

def getSerLog(data):
    serLog = []
    for text_line in data:
        serLog.append(parse_line(text_line))
    return serLog

def getIpCount(data, ip):
    counter = 0
    for line in data:
        if line['ip'] == ip:
            counter += 1
    return counter

def getMeanNumberOfRequests(JSONdata):
    pass

def fuulIpCounter(JSONdata):
    c = Counter()
    for record in JSONdata:
        c[record['ip']] += 1
    return c

def main():
    with open(FILENAME) as fp:
        text_lines = fp.readlines()

    serialized_log = getSerLog(text_lines)

    #print(serialized_log[0:10])
    #print(len(serialized_log))
    #print(counter(serialized_log['ip']))

    #print(serialized_log[0:10])
    print(fuulIpCounter(serialized_log).most_common()[-1])
    meanNumberOfRequests = len(serialized_log)/len(fuulIpCounter(serialized_log))
    print(meanNumberOfRequests)


if __name__ == "__main__":
    main()