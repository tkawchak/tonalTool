import numpy as np
import cv2
import pygame
from beeper import Beeper
from directionObjects import *
#import pygame.camera
from pygame.locals import *

# SOUND FILES TO PLAY SOUND - DON'T CHANGE
# FIND MORE PLEASANT TONES
up = "Up.wav"
down = "Down.wav"
left = "Left.wav"
right = "Right.wav"
target = "All.wav"

# WINDOW PROPERTIES - CHANGE THESE, MAYBE HAVE ABILITY TO RESIZE WINDOW
windowHeight = 480
windowWidth = 640

# ARROW SIZING PROPERTIES
sidePadding = 20  # higher number means that the arrows are closer to the sides of the window
topPadding = 4 * sidePadding  # spacing so that there is room for buttons above the top arrow
arrowSize = (windowHeight + windowWidth) / 2.0 / 8.0

# ARROW POSITIONING PROPERTIES
upX = windowWidth / 2.0 - arrowSize / 2.0
upY = topPadding
rightX = windowWidth - windowWidth / sidePadding - arrowSize
rightY = windowHeight / 2.0 - arrowSize / 2.0
leftX = windowWidth / sidePadding
leftY = windowHeight / 2.0 - arrowSize / 2.0
downX = windowWidth / 2.0 - arrowSize / 2.0
downY = windowHeight - windowHeight / sidePadding - arrowSize

# BUTTON ATTRIBUTES
buttonSizeX = windowWidth / 4.0
buttonSizeY = topPadding - 2 * sidePadding
resetX = sidePadding
resetY = sidePadding
targetX = windowWidth / 2.0 - buttonSizeX / 2.0
targetY = sidePadding
closeX = windowWidth - sidePadding - buttonSizeX
closeY = sidePadding

# PYGAME INITIALIZATION
pygame.init()
#pygame.camera.init()
# SET THE TEXT FOR THE WINDOW
text = pygame.font.SysFont("comicsansms", 20)

# SET THE CAMERA TO VIDEO CAPTURE
cap = cv2.VideoCapture(0)

# INITIALIZE THE WINDOW AND OTHER OBJECTS

beeper1 = Beeper(up, right, down, left, target)
# upArrow = ArrowUP(win, upX, upY, arrowSize)
# rightArrow = ArrowRIGHT(win, rightX, rightY, arrowSize)
# leftArrow = ArrowLEFT(win, leftX, leftY, arrowSize)
# downArrow = ArrowDOWN(win, downX, downY, arrowSize)
# reset = Button(win, resetX, resetY, buttonSizeX, buttonSizeY, "reset", text)
# target = Button(win, targetX, targetY, buttonSizeX, buttonSizeY, "target", text)
# close = Button(win, closeX, closeY, buttonSizeX, buttonSizeY, "close", text)

# cameraList = pygame.camera.list_cameras()
# if not cameraList:
#     raise ValueError("Sorry, no cameras found")
# camera = pygame.camera.Camera(cameraList[0], (windowWidth, windowHeight))
# camera.start()
# # SURFACE FOR THE CAMERA TO CAPTURE TO
# snapshot = pygame.surface.Surface((windowWidth, windowHeight), 0, win)


# FUNCTIONS TO SET THE COLORS OF THE ARROWS DEPENDING ON THE DIRECTIONS
def update_directions(direction):
    """updates the directions of the arrows
        @param (str) - direction of the beeping
    """

    upArrow.update_dir(direction)
    downArrow.update_dir(direction)
    rightArrow.update_dir(direction)
    leftArrow.update_dir(direction)

direction = beeper1.get_dir()
exitProgram = False
# PROGRAM LOOPS UNTIL THE USER PRESSES escape or close button
while not exitProgram:

    # if camera.query_image():
    #     snapshot = camera.get_image(snapshot)
    # win.blit(snapshot, (0, 0))
    # win.fill((255, 255, 255))
    img = cap.read()[1]
    img = cv2.rectangle(img,(0,0),(100, 100),(0, 255, 0), -1)
    pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2))
    img = cv2.polylines(img,[pts],True,(0,255,255))
    cv2.imshow("Third Eye Project - Tonal Tool", img)

    # reset.draw()
    # target.draw()
    # close.draw()
    # upArrow.draw()
    # downArrow.draw()
    # rightArrow.draw()
    # leftArrow.draw()

    # CHANGE THE DIRECTION TO NONE IF THE LAST WAS TARGET
    # THIS WILL GIVE A PROBLEM RIGHT NOW IF THE
    lastDirection = beeper1.get_dir()

    key = cv2.waitKey(2)

    if key == 2490368:  # up
        direction = "up"
    elif key == 2621440:  # down
        direction = "down"
    elif key == 2555904:  # right
        direction = "right"
    elif key == 2424832:  # left
        direction = "left"
    elif key == 13:  # enter / return
        direction = "all"
    elif key == 32:  # space bar
        direction = "none"
    elif key == 27:  # escape
        direction = "none"
        exitProgram = True
    else:
        direction = lastDirection


    # for event in pygame.event.get():
    #
    #     # USER CLOSES THE WINDOW
    #     if event.type == QUIT:
    #         quit()
    #
    #     # KEYBOARD EVENTS
    #     if event.type == KEYDOWN:
    #         if event.key == 273:  # up
    #             direction = "up"
    #         elif event.key == 274:  # down
    #             direction = "down"
    #         elif event.key == 275:  # right
    #             direction = "right"
    #         elif event.key == 276:  # left
    #             direction = "left"
    #         elif event.key == 13:  # enter / return
    #             direction = "all"
    #         elif event.key == 32:  # space bar
    #             direction = "none"
    #         elif event.key == 27:  # escape
    #             direction = "none"
    #             exitProgram = True
    #
    #     # MOUSE EVENTS
    #     elif event.type == MOUSEBUTTONDOWN:
    #         (x, y) = event.pos  # gets the x and y position of the click
    #
    #         if upX < x < upX + arrowSize and upY < y < upY + arrowSize:
    #             direction = "up"
    #         elif downX < x < downX + arrowSize and downY < y < downY + arrowSize:
    #             direction = "down"
    #         elif rightX < x < rightX + arrowSize and rightY < y < rightY + arrowSize:
    #             direction = "right"
    #         elif leftX < x < leftX + arrowSize and leftY < y < leftY + arrowSize:
    #             direction = "left"
    #         elif resetX < x < resetX + buttonSizeX and resetY < y < resetY + buttonSizeY:
    #             direction = "none"
    #         elif targetX < x < targetX + buttonSizeX and targetY < y < targetY + buttonSizeY:
    #             direction = "all"
    #         elif closeX < x < closeX + buttonSizeX and closeY < y < closeY + buttonSizeY:
    #             exitProgram = True
    #             direction = "none"
    #
    #     # NO RELEVANT EVENTS
    #     else:
    #         direction = lastDirection

    # UPDATE THE BEEPING AND DISPLAY DIRECTIONS
    beeper1.update_beep(direction, lastDirection)
    # update_directions(direction)

# EXIT THE PROGRAM
cap.release()
cv2.destroyAllWindows()
pygame.quit()
quit()


#
# while( True ):
#     img = cap.read()[1]
#
#     img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#
#     # Display the resulting frame
#     cv2.imshow('frame', img)
#
#     key = cv2.waitKey(1)
#     print(key)
#
#     if key & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()