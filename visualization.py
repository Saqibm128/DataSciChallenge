import matplotlib.pyplot as plt
import numpy as np
import aggregation as agg

if __name__ == "__main__":
    separatedByEventType = agg.generateSeparatedByEventType()
    photoUploadEvents = separatedByEventType["PhotoUpload"]

    photoUploadsByUsers = agg.separateByAttr(photoUploadEvents, "user_id")
    numEventsPerUser = [len(photoUploadsByUsers[key]) for key in photoUploadsByUsers.keys()]
    n, bins, patches = plt.hist(numEventsPerUser,  10, (0, 25))
    # print("Bins used", bins) #debug statement for visualization
    plt.title("PhotoUpload Event Frequency Per User")
    plt.xlabel("Number of Photo Uploads per User")
    plt.ylabel("Number of Users")
    plt.xlim(0, 25)
    plt.show()

    totalNumberOfEvents = sum([len(separatedByEventType[key]) for key in separatedByEventType.keys()])

    separatedByUsers = agg.separateByAttr(agg.getInputData(), "user_id")
    print("Proportion of Users Generating PhotoUpload Events", len(photoUploadsByUsers.keys())/len(separatedByUsers.keys()), " ({}/{})".format(len(photoUploadsByUsers.keys()), len(separatedByUsers.keys())))
    print("Proportion of PhotoUpload Events", len(separatedByEventType["PhotoUpload"])/totalNumberOfEvents, " ({}/{})".format(len(separatedByEventType["PhotoUpload"]), totalNumberOfEvents))
    print("Mean Number of Events per User", np.mean(numEventsPerUser), " ({}/{})".format(len(separatedByEventType["PhotoUpload"]), len(photoUploadsByUsers.keys())))
    print("Median Number of Events per User", np.median(numEventsPerUser))
    print("St. Dev of Number of Events per User", np.std(numEventsPerUser))
