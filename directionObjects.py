# MODULE CONTAINING THE GRAPHICAL COMPONENT FOR THE TONAL TOOL V2 PROJECT

import pygame
from pygame.locals import *


class ArrowUP:
    """upwards arrow using pygame"""

    def __init__(self, window, xpos, ypos, size):
        """initializes an arrow for use with a pygame program
            @param xpos (int) - point of the top-left corner of the arrow
            @param ypos (int) - point of the top-left corner of the arrow
            @param size (int) - height of the square arrow object
        """

        self.window = window

        # ARROW BACKGROUND POINTS
        self.up_left = (xpos, ypos)
        self.up_right = (xpos + size, ypos)
        self.down_left = (xpos, ypos + size)
        self.down_right = (xpos + size, ypos + size)
        self.rectSize = (size, size)

        # ARROW POINTS
        self.point1 = (xpos + 5 * (size / 10.0), ypos + 1 * (size / 10.0))
        self.point2 = (xpos + 9 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point3 = (xpos + 7 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point4 = (xpos + 7 * (size / 10.0), ypos + 9 * (size / 10.0))
        self.point5 = (xpos + 3 * (size / 10.0), ypos + 9 * (size / 10.0))
        self.point6 = (xpos + 3 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point7 = (xpos + 1 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.pointList = (self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7)

        # OTHER ATTRIBUTES OF ARROWS
        self.active = (0, 255, 0)  # color green
        self.notActive = (255, 0, 0)  # color red
        self.arrowColor = (0, 0, 0)  # color black
        self.bgColor = self.notActive

    def update_dir(self, direction):
        """determines whether the given arrow is active based upon the direction
            @param direction (string) - direction that is active for the tonal tool
        """

        if direction == "up" or direction == "all":
            self.bgColor = self.active

        else:
            self.bgColor = self.notActive

    def draw(self):
        """draws the arrow and the background to the screen
            @param window (screen.display.set_mode()) - the screen to draw the arrow to
        """

        pygame.draw.rect(self.window, self.bgColor, Rect(self.up_left, self.rectSize))
        pygame.draw.polygon(self.window, self.arrowColor, self.pointList)


class ArrowRIGHT:
    """rightward arrow using pygame"""

    def __init__(self, window, xpos, ypos, size):
        """initializes an arrow to use with pygame
            @param xpos (int) - point of the top-left corner of the arrow
            @param ypos (int) - point of the top-left corner of the arrow
            @param size (int) - height of the square arrow object
        """

        self.window = window

        # ARROW BACKGROUND POINTS
        self.up_left = (xpos, ypos)
        self.up_right = (xpos + size, ypos)
        self.down_left = (xpos, ypos + size)
        self.down_right = (xpos + size, ypos + size)
        self.rectSize = (size, size)

        # ARROW POINTS
        self.point1 = (xpos + 9 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point2 = (xpos + 5 * (size / 10.0), ypos + 9 * (size / 10.0))
        self.point3 = (xpos + 5 * (size / 10.0), ypos + 7 * (size / 10.0))
        self.point4 = (xpos + 1 * (size / 10.0), ypos + 7 * (size / 10.0))
        self.point5 = (xpos + 1 * (size / 10.0), ypos + 3 * (size / 10.0))
        self.point6 = (xpos + 5 * (size / 10.0), ypos + 3 * (size / 10.0))
        self.point7 = (xpos + 5 * (size / 10.0), ypos + 1 * (size / 10.0))
        self.pointList = (self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7)

        # OTHER ATTRIBUTES OF ARROWS
        self.active = (0, 255, 0)  # color green
        self.notActive = (255, 0, 0)  # color red
        self.arrowColor = (0, 0, 0)  # color black
        self.bgColor = self.notActive

    def update_dir(self, direction):
        """determines whether the given arrow is active based upon the direction
            @param direction (string) - direction that is active for the tonal tool
        """

        if direction == "right" or direction == "all":
            self.bgColor = self.active

        else:
            self.bgColor = self.notActive

    def draw(self):
        """draws the arrow and the background to the screen
            @param window (screen.display.set_mode()) - the screen to draw the arrow to
        """

        pygame.draw.rect(self.window, self.bgColor, Rect(self.up_left, self.rectSize))
        pygame.draw.polygon(self.window, self.arrowColor, self.pointList)


class ArrowLEFT:
    """leftward arrow using pygame"""

    def __init__(self, window, xpos, ypos, size):
        """initializes an arrow using pygame
            @param xpos (int) - point of the top-left corner of the arrow
            @param ypos (int) - point of the top-left corner of the arrow
            @param size (int) - height of the square arrow object
        """

        self.window = window

        # ARROW BACKGROUND POINTS
        self.up_left = (xpos, ypos)
        self.up_right = (xpos + size, ypos)
        self.down_left = (xpos, ypos + size)
        self.down_right = (xpos + size, ypos + size)
        self.rectSize = (size, size)

        # ARROW POINTS
        self.point1 = (xpos + 1 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point2 = (xpos + 5 * (size / 10.0), ypos + 1 * (size / 10.0))
        self.point3 = (xpos + 5 * (size / 10.0), ypos + 3 * (size / 10.0))
        self.point4 = (xpos + 9 * (size / 10.0), ypos + 3 * (size / 10.0))
        self.point5 = (xpos + 9 * (size / 10.0), ypos + 7 * (size / 10.0))
        self.point6 = (xpos + 5 * (size / 10.0), ypos + 7 * (size / 10.0))
        self.point7 = (xpos + 5 * (size / 10.0), ypos + 9 * (size / 10.0))
        self.pointList = (self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7)

        # OTHER ATTRIBUTES OF ARROWS
        self.active = (0, 255, 0)  # color green
        self.notActive = (255, 0, 0)  # color red
        self.arrowColor = (0, 0, 0)  # color black
        self.bgColor = self.notActive

    def update_dir(self, direction):
        """determines whether the given arrow is active based upon the direction
            @param direction (string) - direction that is active for the tonal tool
        """

        if direction == "left" or direction == "all":
            self.bgColor = self.active

        else:
            self.bgColor = self.notActive

    def draw(self):
        """draws the arrow and the background to the screen
            @param window (screen.display.set_mode()) - the screen to draw the arrow to
        """

        pygame.draw.rect(self.window, self.bgColor, Rect(self.up_left, self.rectSize))
        pygame.draw.polygon(self.window, self.arrowColor, self.pointList)


class ArrowDOWN:
    """downward arrow using pygame"""

    def __init__(self, window, xpos, ypos, size):
        """initializes an arrow using pygame
            @param xpos (int) - point of the top-left corner of the arrow
            @param ypos (int) - point of the top-left corner of the arrow
            @param size (int) - height of the square arrow object
        """

        self.window = window

        # ARROW BACKGROUND POINTS
        self.up_left = (xpos, ypos)
        self.up_right = (xpos + size, ypos)
        self.down_left = (xpos, ypos + size)
        self.down_right = (xpos + size, ypos + size)
        self.rectSize = (size, size)

        # ARROW POINTS
        self.point1 = (xpos + 5 * (size / 10.0), ypos + 9 * (size / 10.0))
        self.point2 = (xpos + 1 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point3 = (xpos + 3 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point4 = (xpos + 3 * (size / 10.0), ypos + 1 * (size / 10.0))
        self.point5 = (xpos + 7 * (size / 10.0), ypos + 1 * (size / 10.0))
        self.point6 = (xpos + 7 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.point7 = (xpos + 9 * (size / 10.0), ypos + 5 * (size / 10.0))
        self.pointList = (self.point1, self.point2, self.point3, self.point4, self.point5, self.point6, self.point7)

        # OTHER ATTRIBUTES OF ARROWS
        self.active = (0, 255, 0)  # color green
        self.notActive = (255, 0, 0)  # color red
        self.arrowColor = (0, 0, 0)  # color black
        self.bgColor = self.notActive

    def update_dir(self, direction):
        """determines whether the given arrow is active based upon the direction
            @param direction (string) - direction that is active for the tonal tool
        """

        if direction == "down" or direction == "all":
            self.bgColor = self.active

        else:
            self.bgColor = self.notActive

    def draw(self):
        """draws the arrow and the background to the screen
            @param window (screen.display.set_mode()) - the screen to draw the arrow to
        """

        pygame.draw.rect(self.window, self.bgColor, Rect(self.up_left, self.rectSize))
        pygame.draw.polygon(self.window, self.arrowColor, self.pointList)


class Button:
    """class for the button that the user will press to signal that the target has been reached"""

    def __init__(self, window, xpos, ypos, sizeX, sizeY, message, text):
        """
            @param window (screen.display.set_mode()) - window to draw arrows to
            @param xpos (in) - point of the top-left corner of the arrow
            @param ypos (int) - point of the top-left corner of the arrow
            @param sizeX (int) - size in the x direction
            @param sizeY (int) - size in the y direction
            @param message (str) - the text to display
            @param text (font()) - the text to be used
        """

        self.window = window
        self.bgColor = (0, 0, 0)  # color black
        self.message = text.render(message, True, (255, 255, 255))

        self.up_left = (xpos, ypos)
        self.up_right = (xpos + sizeX, ypos)
        self.down_left = (xpos, ypos + sizeY)
        self.down_right = (xpos + sizeX, ypos + sizeY)
        self.textPos = (xpos + sizeX / 3.0, ypos + sizeY / 3.0)  # update this so that the text is centered
        self.rectSize = (sizeX, sizeY)

    def draw(self):
        """draws the button object to the window"""

        pygame.draw.rect(self.window, self.bgColor, Rect(self.up_left, self.rectSize))
        self.window.blit(self.message, self.textPos)