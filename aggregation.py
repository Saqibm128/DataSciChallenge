def separateByAttr(eventInstances, attr):
    '''
    Separate out each event in the passed in events and tries to create a
        dictionary of lists of events where events have that attribute
        ex: if we pass in a list of events and ask to separate by event type,
        we will get a dictionary with keys of eventTypes, and values of events
        with that event type
    '''
    eventsByAttr = dict()
    for eventInstance in eventInstances:
        eventAttr = eventInstance[attr]
        if eventAttr not in eventsByAttr.keys():
            eventsByAttr[eventAttr] = list()
        eventsByAttr[eventAttr].append(eventInstance)
    return eventsByAttr

def getInputData():
    '''
    gets the input_data, moves "user_id" to top-level
    '''
    from input_data import INPUT_DATA
    for event in INPUT_DATA:
        event["user_id"] = event["properties"]["user_id"]
    return INPUT_DATA

def generateSeparatedByEventType(input_data = getInputData()):
    '''
    separates input_data by the event type
    '''
    return separateByAttr(input_data, "event")


#Sanity check to see the number of events and each event type
if __name__ == "__main__":
    separatedByEventType = generateSeparatedByEventType()
    [print((key, len(separatedByEventType[key]))) for key in separatedByEventType.keys()]
