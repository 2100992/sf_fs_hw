from events import events

def getEventsCount(events, eventType):
    count = 0
    for event in events:
            if event['eventType'] == eventType:
                count += 1
    return count

def getMinTimestampEvent(events):
    minTS = events[0]['timestamp']
    sessId = events[0]['sessionId']
    for event in events:
        if event['timestamp'] < minTS:
            minTS = event['timestamp']
            sessId = event['sessionId']
    return [minTS, sessId]

def getSuvItemPrice(events):
    sumPrice = 0
    for event in events:
        sumPrice += event['item_price']
    return sumPrice

def getFirstSession(events):
    for event in events:
        if event['firstInSession']:
            return event['pageViewId']
        else:
            return None

print(getEventsCount(events, 'itemViewEvent'))
print(getEventsCount(events, 'itemBuyEvent'))

print(getEventsCount(events, 'detectedDuplicate'))
print(getMinTimestampEvent(events))

print(getSuvItemPrice(events))

print(getFirstSession(events))