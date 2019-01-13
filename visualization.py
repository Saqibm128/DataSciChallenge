import matplotlib.pyplot as plt
import aggregation as agg

if __name__ == "__main__":
    separatedByEventType = agg.generateSeparatedByEventType()
    photoUploadEvents = separatedByEventType["PhotoUpload"]
    #user_id is nested into the properties attribute, so we just place another attribute
    #   user_id directly into each event
    for event in photoUploadEvents:
        event["user_id"] = event["properties"]["user_id"]

    photoUploadsByUsers = agg.separateByAttr(photoUploadEvents, "user_id")
    n, bins, patches = plt.hist([len(photoUploadsByUsers[key]) for key in photoUploadsByUsers.keys()], 5)
    plt.title("Photo Upload Events By Users")
    plt.xlabel("Number of Users")
    plt.ylabel("Number of Photo Uploads")
    plt.show()
    
