import random
import math
from PIL import Image, ImageDraw

# script for creating dot stimuli with two sets deteremined based on a ratio
# script by Michelle Hurst, hurst.mich@gmail.com, April 2022

# setting up canvas size
stimW = 400
stimH = 600

# setting global properties of the stim (for now, we could vary them though, e.g., vary dot size so that area is varied)
set1Color = "gold"
set2Color = "blue"

#setting up stim parameters
nTrials = 7
ratioList = [2, 4, 3]
habType = ["hab21", "hab41", "hab31"]


# draw the rectangles for set 1 and set 2
def create_set1Rect(w, h, r): #width, height, ratio for set2
    x0 = (stimW - w)/2
    x1 = x0 + w
    unit = h/(r + 1)
    set1Height = unit*r
    set2Height = unit

    y0 = (stimH - h)/2 +  set2Height
    y1 = y0 + set1Height
    return draw.rectangle((x0, y0, x1, y1), fill = set1Color, outline = set1Color)
    
def create_set2Rect(w, h, r): #width, height, ratio for set2
    x0 = (stimW - w)/2
    x1 = x0 + w

    unit = h/(r + 1)
    set2Height = unit

    y0 = (stimH - h)/2
    y1 = (stimH - h)/2 +  set2Height
    return draw.rectangle((x0, y0, x1, y1), fill = set2Color, outline = set2Color)

# now to actually create the stim
# looping through the stimList and creating the dots needed for each



for t in range(0, nTrials):

    # setting up new image from PIL
    stim = Image.new('RGBA', (stimW, stimH), color = 'black')
    draw = ImageDraw.Draw(stim)

    width = random.randrange(stimW*(1/4), stimW*(3/4), 1)
    height = random.randrange(stimH*(1/4), stimH*(3/4), 1)

    for b in range(0, len(ratioList)):
        create_set1Rect(width, height, ratioList[b])
        create_set2Rect(width, height, ratioList[b])

        # save image with name of the form cont_habtype_set1_set2
        fileName = "cont_" + habType[b] + "_" + str(width) + "_" + str(height) + ".png"
        stim.save("ContStim/" + fileName)




