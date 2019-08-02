from collections import defaultdict

FILENAME = 'dummy-access.log'

def parse_line(text_line):
    dict_from_line = {}
    dict_from_line['ip'] = text_line.split()[0]
    dict_from_line['dt'] = text_line.split()[3].strip('[')
    dict_from_line['user_agent'] = text_line.split('"')[1]
    return dict_from_line

def getJSON(data):
    dd = []
    for stringLog in data:
        dd.append(parse_line(stringLog))
    return dd

def getIpCount(data, ip):
    counter = 0
    for line in data:
        if ip in line:
            counter += 1
    return counter

def main():
    with open(FILENAME) as fp:
        text_lines = fp.readlines()

    dd = getJSON(text_lines)

    print(dd[0:10])
    print(len(dd))
    print(counter(dd['ip']))


if __name__ == "__main__":
    main()