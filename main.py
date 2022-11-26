from googleapiclient.discovery import build
import isodate

true = True
false = False

# --------------- INITIATE API --------------- #
api_key_file = open("api_key.txt", "r")
api_key = api_key_file.readline()
youtube = build("youtube", "v3", developerKey = api_key)

# --------------- INITIATE VARIABLES --------------- #
videoIdList = []
oldPageToken = ""
newPageToken = ""
pagesLeft = True
minutes = 0
seconds = 0

subjectList = {'S1' : "PLZ2ps__7DhBYrMs3zybOqr1DzMFCX49xG", 'M1' : "PLZ2ps__7DhBZYDZo9A0pZ_i0xhstrk5cR",
'M2' : "PLZ2ps__7DhBboGlwPVSsWP8loAJCLrKc8", 'S2' : "PLZ2ps__7DhBbLZ6RdNTIXvFdaMpvqagt0", 'CT' : "PLZ2ps__7DhBYSzaAFqpyQKqmoni-EefS7",
'E1' : "PLZ2ps__7DhBbf28nnkgAuFwaWjGtjaNck", 'E2' : "PLZ2ps__7DhBbWy3GL4oWKXGrwf6Ul8Cry", 'PIP' : "PLZ2ps__7DhBb2cXAu5PevO_mzgS3Fj3Fs"}
listOfKeys = list(subjectList.keys())

subject = input("Which subject are you studying? M1/M2/S1/S2/E1/E2/CT/PiP : ").upper()
if (subject in listOfKeys):
    subjectPlaylist = subjectList[subject]
else :
    print("Error! Aborting...")
    quit()

subjectPlaylist = "PLlwFbY0WPIVLh0EQ7b0orZIsbL6ANb7m4"
# --------------- REQUEST PLAYLIST DETAILS--------------- #
while(pagesLeft):
    request = youtube.playlistItems().list (
        part = "contentDetails",
        maxResults = 50,
        pageToken = newPageToken,
        playlistId = subjectPlaylist,
    )
    response = request.execute()
    oldPageToken = newPageToken

    try:
        newPageToken = response['nextPageToken']
    except:
        newPageToken = oldPageToken
    responseList = (response['items'])
    for i in range (len(responseList)) :
        videoIdList.append(responseList[i]['contentDetails']['videoId'])

    if (oldPageToken == newPageToken) :
        pagesLeft = False
        
# --------------- REQUEST VIDEO DURATION DETAILS--------------- #
for i in range (len(videoIdList)) :
    request = youtube.videos().list (
        part = "contentDetails",
        id = videoIdList[i],
    )
    response = request.execute()
    videoDuration = (response['items'][0]['contentDetails']['duration'])
    dur = isodate.parse_duration(videoDuration)
    seconds += dur.total_seconds()

# --------------- CALCULATE DURATIONS --------------- #
Q1 = int(input('''
Calculate time for remaining videos or for complete revision?
1. Remaining Videos
2. Complete Revision
'''))
if (Q1 == 1) :
    currentWeek = int(input("What week are you on right now? "))
    weeksLeft = 12 - currentWeek
    avgSecondsLeft = (seconds / 12) * weeksLeft
    avgMinutesLeft = int(avgSecondsLeft / 60)
    studyDays = int(input("How many days of the week do you study? "))
    studyDaysLeft = weeksLeft * studyDays
    minutes = avgMinutesLeft / studyDaysLeft
    print(f"Over the next {weeksLeft} weeks, with {studyDays} study days every week, you need to spend {int(minutes)} minutes every study day!")
elif (Q1 == 2) :
    currentWeek = int(input("What week are you on right now? "))
    weeksLeft = (12 - currentWeek) + 1
    studyDays = int(input("How many days of the week do you study? "))
    studyDaysLeft = weeksLeft * studyDays
    minutes = (seconds / 60) / studyDaysLeft
    print(f"Over the next {weeksLeft} weeks, with {studyDays} study days every week, you need to spend {int(minutes)} minutes every study day!")
else :
    print("Error! Aborting...")
    quit()