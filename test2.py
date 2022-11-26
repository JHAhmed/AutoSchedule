import isodate

# subjectList = {'S1' : "PLZ2ps__7DhBYrMs3zybOqr1DzMFCX49xG", 'M1' : "PLZ2ps__7DhBZYDZo9A0pZ_i0xhstrk5cR",
# 'M2' : "PLZ2ps__7DhBboGlwPVSsWP8loAJCLrKc8", 'S2' : "PLZ2ps__7DhBbLZ6RdNTIXvFdaMpvqagt0", 'CT' : "PLZ2ps__7DhBYSzaAFqpyQKqmoni-EefS7",
# 'E1' : "PLZ2ps__7DhBbf28nnkgAuFwaWjGtjaNck", 'E2' : "PLZ2ps__7DhBbWy3GL4oWKXGrwf6Ul8Cry", 'PiP' : "PLZ2ps__7DhBb2cXAu5PevO_mzgS3Fj3Fs"}
# subject = input("Which subject are you studying? M1/M2/S1/S2/E1/E2/CT/PiP : ")

# listOfKeys = list(subjectList.keys())
# for i in range (len(listOfKeys)) :
#     print(listOfKeys[i])
minutes = 0
seconds = 0

# videoDuration = "PT34M600S"

# stripPT = videoDuration.split("PT")
# stripM = stripPT[1].split("M")
# print(stripM)
# if stripM[0] != '':
#     minutes =+ int(stripM[0])
# # stripS = stripM[1].split("S")
# # if stripS[0] != '':
# #     seconds =+ int(stripS[0])

# secsToMins = seconds/60
# minutes += int(secsToMins)
# print(minutes)

videoList = ["PT34M6S"]
totalDur = 0
for i in range (len(videoList)) :

    videoDuration = videoList[i]
    print(videoDuration)
    dur = isodate.parse_duration(videoDuration)
    totalDur += dur.total_seconds()
    print(totalDur)


print(dur.total_seconds())
print(int(totalDur/60))