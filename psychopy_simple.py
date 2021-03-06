#!/usr/bin/env python
"""

A basic presentation in psychopy

(c) Laurent Perrinet - INT/CNRS


"""
# width and height of your screen
w, h = 1920, 1200

import MotionClouds as mc
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)
color = mc.envelope_color(fx, fy, ft)
env = color *(mc.envelope_gabor(fx, fy, ft, V_X=1.) + mc.envelope_gabor(fx, fy, ft, V_X=-1.))
z = 2*mc.rectif(mc.random_cloud(env), contrast=.5) -1.

# TODO : make a GUI with two threads: one for psychopy, one for the generation / see also experiment_smooth.py for a smooth transition of parameters
from psychopy import *
import time
win = visual.Window([w, h], fullscr=True)
for i_frame in range(mc.N_frame):
    #creating a new stimulus every time
    stim = visual.PatchStim(win, tex=z[:, :, i_frame],
        size=(600, 600), units='pix',
        interpolate=False)
    stim.draw()
    stim.clearTextures()
    win.flip()
