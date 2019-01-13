# Analysis of PhotoUpload Event Frequency per User

## Code Explanation

I used [aggregation.py](./aggregation.py) to solve for Part 1 of the challenge.
I used [visualization.py](./visualization.py) to solve for Part 2 of the challenge.

For part 2, I used numpy and matplotlib. I included the full environment I used inside conda in [this file](./environpy37.yaml)

## Key Statistics
The PhotoUpload event is one of 4 events within the data, making up approximately 0.085 (5018/58859) of all events generated within the dataset. 0.2704 (676/2500) of all users within the dataset generated a PhotoUpload event at all. I first selected only the PhotoUpload events within the dataset. I then separated out the PhotoUpload events for each user_id and generated the number of PhotoUpload events for each user. I found that on average, a user is generating 7.423 (5018 events /676 users) PhotoUpload events. However, the median number of PhotoUpload events generated was 4, which suggests that the distribution of frequency of PhotoUpload events per user is skewed with a long tail towards the left. Standard deviation of PhotoUpload event frequency is 6.69, suggesting that there is a significant amount of variation in the frequency of PhotoUpload events.


## Visualization of PhotoUpload Event Frequency per User

![Histogram of PhotoUpload Events Per User showing a bimodal distribution with skewed tail towards left.](./PhotoUploadEventsPerUserHistogram.png)

I created a histogram of the distribution of PhotoUpload event frequency for each user for all users which ever triggered at least one PhotoUpload event. I can see that there is a long tail towards the left, confirming the reason why the median is much smaller than the mean for the distribution. However, the histogram suggests also that the event frequency is bimodal, with the biggest peak around 0 to 3 PhotoUpload events per user, and another peak centered around 15 to 18 PhotoUpload events per user.

## Interpretation and Conclusions

Most users do not trigger many PhotoUpload events at all, with only slightly more than 1/4 of all users event triggering the PhotoUpload event. Among all users who have ever triggered the PhotoUpload event, most only trigger 1-3 events, suggesting that they may have only been experimenting with it and failed to continue to use it. These users may have only needed it once. It would be worth investigating why the users quit generating this event; it may be the case that the app feature which generates this event may not be user-friendly for such users or that the app feature did not meet user expectations. It may also be the case that the user may have only wanted to use the feature once for their specific use case or that most of the users may not have used the application for long and may therefore have not had an opportunity to generate many events.

However, there is a smaller but sizeable number of users which trigger many more PhotoUpload events. These users are generating 15-18 PhotoUpload events on average and are worth investigating. There may be a use case for the application which needs to be documented which is causing the users to use this feature.
