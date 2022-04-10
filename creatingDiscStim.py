import random
import math
from PIL import Image, ImageDraw

# script for creating dot stimuli with two sets deteremined based on a ratio
# script by Michelle Hurst, hurst.mich@gmail.com, April 2022

# setting up canvas size
stimW = 500
stimH = 500

# setting global properties of the stim (for now, we could vary them though, e.g., vary dot size so that area is varied)
radius = 10
gap = 10
set1Color = "gold"
set2Color = "blue"

# this is the list of stim we want to make
# includes: set1 size, set2 size, habtype as an indicator of stim category
stimList = [
    [8, 4, "hab21"],
    [12, 6, "hab21"],
    [14, 7, "hab21"],
    [20, 10, "hab21"],
    [24, 12, "hab21"],
    [30, 15, "hab21"],
    [38, 19, "hab21"],

    [12, 3, "hab41"],
    [16, 4, "hab41"],
    [24, 6, "hab41"],
    [28, 7, "hab41"],
    [36, 9, "hab41"],
    [40, 10, "hab41"],
    [48, 12, "hab41"],

    [9, 3, "hab31"],
    [15, 5, "hab31"],
    [21, 7, "hab31"],
    [27, 9, "hab31"],
    [36, 12, "hab31"],
    [42, 14, "hab31"],
    [48, 16, "hab31"],
]

# creating the functions needed to create the specs for circles, to draw the circles, and to export the image
# create specs
def generateDots(radius, gap, set1Color, set2Color, set1, set2):
    # creating a dot class to then load into 
    class dot: 
        def __init__(self, x, y, set1, set2, color): 
            self.x = x 
            self.y = y
            self.set1 = set1
            self.set2 = set2
            self.color = color
    n = 0
    while len(circleList) < (set1 + set2):
        # randomly generating x, y coordinates of the dot - using the if statement to add different colors to the dot
        # the first dots will be set1, up until set1 is maxed, then it'll be set2
        if n < set1:
            curDot = dot(random.randrange(radius + gap, stimW - radius - gap, 1), random.randrange(radius + gap, stimH - radius - gap, 1), set1, set2, set1Color)
        else:
            curDot = dot(random.randrange(radius + gap, stimW - radius - gap, 1), random.randrange(radius + gap, stimH - radius - gap, 1), set1, set2, set2Color)
        
        # now checking that the new dot doesn't overlap with the previously made dots
        overlap = False

        for i in range(0, len(circleList)):
            checkDot = circleList[i]
                # this distance needs to be larger than the radii of each dot + the required minimum gap
            distance = math.sqrt(pow(curDot.x - checkDot.x, 2) + pow(curDot.y - checkDot.y, 2))
            if distance < radius + radius + gap: 
                overlap = True

        if overlap == False:
            circleList.append(curDot)

        n = n + 1

# draw the circles
def create_circle(x, y, r, dotColor): #center coordinates, radius, dotColor which will be used for the outline and fill
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return draw.ellipse((x0, y0, x1, y1), fill = dotColor, outline = dotColor) 

# now to actually create the stim
# looping through the stimList and creating the dots needed for each

for j in range(0, len(stimList)):

    # setting up new image from PIL
    stim = Image.new('RGBA', (stimW, stimH), color = 'grey')
    draw = ImageDraw.Draw(stim)

    # getting the number of dots in set1 and set2 from stimList
    set1 = stimList[j][0]
    set2 = stimList[j][1]

    # create specs for circles and add them to new circleList
    circleList = []
    generateDots(radius, gap, set1Color, set2Color, set1, set2)

    # draw each circle in the circleList
    for c in range(0, len(circleList)):
        create_circle(circleList[c].x, circleList[c].y, radius, circleList[c].color)
        
    # save image with name of the form disc_habtype_set1_set2
    fileName = "disc_" + stimList[j][2] + "_" + str(stimList[j][0]) + "_" + str(stimList[j][1]) + ".png"
    stim.save("DiscStim/" + fileName)




