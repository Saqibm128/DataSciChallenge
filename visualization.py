import matplotlib.pyplot as plt
import numpy as np
import aggregation as agg

if __name__ == "__main__":
    separatedByEventType = agg.generateSeparatedByEventType()
    photoUploadEvents = separatedByEventType["PhotoUpload"]
    #user_id is nested into the properties attribute, so we just place another attribute
    #   user_id directly into each event
    for event in photoUploadEvents:
        event["user_id"] = event["properties"]["user_id"]

    photoUploadsByUsers = agg.separateByAttr(photoUploadEvents, "user_id")
    numEventsPerUser = [len(photoUploadsByUsers[key]) for key in photoUploadsByUsers.keys()]
    n, bins, patches = plt.hist(numEventsPerUser,  10, (0, 25))
    # print("Bins used", bins) #debug statement for visualization
    plt.title("PhotoUpload Event Frequency Per User")
    plt.xlabel("Number of Photo Uploads per User")
    plt.ylabel("Number of Users")
    plt.xlim(0, 25)
    plt.show()

    print("Mean Number of Events per User", np.mean(numEventsPerUser))
    print("Median Number of Events per User", np.median(numEventsPerUser))
    print("St. Dev of Number of Events per User", np.std(numEventsPerUser))
