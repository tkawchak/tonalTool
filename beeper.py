# CREATES A BEEPER OBJECT
# FOR USE WITH THIRD EYE TONAL TOOL PROJECT v2

import pygame


class Beeper():
    """class to make a beeper object designed for Third Eye Project tonal tool testing"""

    def __init__(self, up, right, down, left, target):
        """initializes the beeper object with pre-determined frequency and duration of sound
                @param freq - the frequency of sound in Hz
                @param duration - the duration that the sound plays for
        """

        # SOUND FILES
        self.up = up  # plays a higher pitched tone to indicate to move hand up
        self.right = right  # plays a tone in the right ear
        self.left = left  # plays a tone in the left ear
        self.down = down  # plays a lower pitched tone to indicate to move hand down
        self.target = target  # plays the target acquisition sound

        self.tone = ""  # current tone to play - initialize to anything, doesn't matter
        self.playTone = False  # new tone only plays when this is true
        self.replay = 0  # how many times the sound will repeat (-1 is infinite)

        # HOLDS THE CURRENT BEEP STATE (UP, DOWN, RIGHT, LEFT, ALL, NONE)
        self.direction = "none"
        self.lastDirection = self.direction

    def update_beep(self, direction, lastDirection):
        """updates the beeper object to play the right sound file
            @param direction (str) - new direction of sound
        """

        self.direction = direction
        self.lastDirection = lastDirection

        # ONLY UPDATE IF THE DIRECTION IS DIFFERENT FROM LAST
        if direction != lastDirection:
            if direction == "up":
                self.tone = self.up
            elif direction == "down":
                self.tone = self.down
            elif direction == "left":
                self.tone = self.left
            elif direction == "right":
                self.tone = self.right
            elif direction == "all":
                self.tone = self.target

            # PLAY SOUND ONCE IF IT IS THE TARGET SOUND
            # PLAY NO SOUND IF THE DIRECTION IS NONE
            # LOOP SOUND INFINITELY IF DIRECTION IS ANY OTHER
            if direction == "all":
                self.replay = 0
                self.playTone = True
            elif direction == "none":
                self.playTone = False
            else:
                self.playTone = True
                self.replay = -1

            pygame.mixer.music.stop()
            if self.playTone:
                pygame.mixer.music.load(self.tone)
                pygame.mixer.music.play(self.replay)

    def get_dir(self):
        """returns the current beeping direction"""
        return self.direction

