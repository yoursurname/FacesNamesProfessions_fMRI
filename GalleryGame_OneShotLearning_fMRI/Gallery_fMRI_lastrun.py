#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on December 02, 2021, at 07:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Gallery_fMRI'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\emilo\\OneDrive - Lund University\\Experiment paradigms\\GalleryGame_fMRI\\Gallery_fMRI_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='glfw', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='0.0000, 0.0000, 0.0000', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Instructions:\n\nYou will see images presented one at a time above an arrow pointing either left, up or right.\nYour task is to memorize the image together with the direction of the arrow. \n\nRespond to each image and arrow using the following buttons:\n1 (index finger) = Left\n2 (middle finger) = Up\n3 (ring finger) = Right\n\nThe second time you see each image there will not be one arrow but three highlighted in orange indicating that you may choose the direction you recall was previously presented below the current image.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color=[1,1,1], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0 = keyboard.Keyboard()
import csv
import random

Arrow_list = []
Img_list = []
ImgType_list = []
Direction_list = []

with open("OneShotLearning.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for lines in csv_reader:
      Arrow_list.append(lines['ArrowImg'])
      Img_list.append(lines['StimFile'])
      ImgType_list.append(lines['ImgType'])
      Direction_list.append(lines['Direction'])
      
    #ShuffledArrow_list = shuffle(Arrow_list)
    shuffle(Arrow_list)
        
    with open('OneShotLearning_Shuffled.csv', 'w') as csvfile:
        fieldnames = ['StimFile','ImgType','ArrowImg','Direction']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writerA = csv.writer(csvfile, delimiter=',', lineterminator = '\n')
        writer.writeheader()
        for i in range(48):
            writerA.writerow([Img_list[i], ImgType_list[i], Arrow_list[i], Direction_list[i]])


# Initialize components for Routine "trial"
trialClock = core.Clock()
key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.125), size=(1, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
Arrow = visual.ImageStim(
    win=win,
    name='Arrow', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.375), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
total_corr=0
total_all=0
rt=0

Congruency = []
Outcome = []

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Uncued_trial"
Uncued_trialClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.125), size=(1, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
direction_options = visual.ImageStim(
    win=win,
    name='direction_options', 
    image='Gallery_arrowoptions.png', mask=None,
    ori=0.0, pos=(0, -0.375), size=(1, 0.250),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Finished"
FinishedClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Well done!\n\nYou have finished the task.\nRemain still and await further \ninstructions by the experiment leader.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_0.keys = []
key_resp_0.rt = []
_key_resp_0_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp_0]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_0* updates
    waitOnFlip = False
    if key_resp_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_0.frameNStart = frameN  # exact frame index
        key_resp_0.tStart = t  # local t and not account for scr refresh
        key_resp_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0, 'tStartRefresh')  # time at next scr refresh
        key_resp_0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_0.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0.getKeys(keyList=['1', '2', '3', 'space'], waitRelease=False)
        _key_resp_0_allKeys.extend(theseKeys)
        if len(_key_resp_0_allKeys):
            key_resp_0.keys = _key_resp_0_allKeys[-1].name  # just the last key pressed
            key_resp_0.rt = _key_resp_0_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_0.keys in ['', [], None]:  # No response was made
    key_resp_0.keys = None
thisExp.addData('key_resp_0.keys',key_resp_0.keys)
if key_resp_0.keys != None:  # we had a response
    thisExp.addData('key_resp_0.rt', key_resp_0.rt)
thisExp.addData('key_resp_0.started', key_resp_0.tStartRefresh)
thisExp.addData('key_resp_0.stopped', key_resp_0.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('OneShotLearning_conditions.xlsx'),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Cued = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('OneShotLearning_Shuffled.csv', selection=Condition_rows),
        seed=None, name='Cued')
    thisExp.addLoop(Cued)  # add the loop to the experiment
    thisCued = Cued.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCued.rgb)
    if thisCued != None:
        for paramName in thisCued:
            exec('{} = thisCued[paramName]'.format(paramName))
    
    for thisCued in Cued:
        currentLoop = Cued
        # abbreviate parameter names if possible (e.g. rgb = thisCued.rgb)
        if thisCued != None:
            for paramName in thisCued:
                exec('{} = thisCued[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        image.setImage(StimFile)
        Arrow.setImage(ArrowImg)
        if key_resp_1.corr:
          total_corr=total_corr+1
          total_all=total_all+1
          rt=key_resp_1.rt
        
        else:
          total_all=total_all+1
          rt=key_resp_1.rt
        
        if key_resp_1.keys == 1 and ArrowImg == 'ArrowLeft.png':
            Outcome=1
        else:
            Outcome=0
        
        if Direction == ArrowImg:
            Congruency='Congruent'
        elif Direction == 'ArrowLeft.png' and ArrowImg == 'ArrowRight.png': 
            Congruency='Incongruent_opposite'
        elif Direction == 'ArrowRight.png' and ArrowImg == 'ArrowLeft.png':
            Congruency='Incongruent_opposite'
        elif Direction == 'neutral':
            Congruency='Neutral'
        else:
            Congruency='Incongruent_perpendicular'
        
        
        # keep track of which components have finished
        trialComponents = [key_resp_1, image, Arrow]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_1* updates
            waitOnFlip = False
            if key_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.tStart = t  # local t and not account for scr refresh
                key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
                key_resp_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_1.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_1.tStop = t  # not accounting for scr refresh
                    key_resp_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_1, 'tStopRefresh')  # time at next scr refresh
                    key_resp_1.status = FINISHED
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
                    key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *Arrow* updates
            if Arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Arrow.frameNStart = frameN  # exact frame index
                Arrow.tStart = t  # local t and not account for scr refresh
                Arrow.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Arrow, 'tStartRefresh')  # time at next scr refresh
                Arrow.setAutoDraw(True)
            if Arrow.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Arrow.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    Arrow.tStop = t  # not accounting for scr refresh
                    Arrow.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Arrow, 'tStopRefresh')  # time at next scr refresh
                    Arrow.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
        Cued.addData('key_resp_1.keys',key_resp_1.keys)
        if key_resp_1.keys != None:  # we had a response
            Cued.addData('key_resp_1.rt', key_resp_1.rt)
        Cued.addData('key_resp_1.started', key_resp_1.tStartRefresh)
        Cued.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
        Cued.addData('image.started', image.tStartRefresh)
        Cued.addData('image.stopped', image.tStopRefresh)
        Cued.addData('Arrow.started', Arrow.tStartRefresh)
        Cued.addData('Arrow.stopped', Arrow.tStopRefresh)
        thisExp.addData('Outcome', Outcome)
        thisExp.addData('Congruency', Congruency)
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_crossComponents = [polygon]
        for thisComponent in fix_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross"-------
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Cued.addData('polygon.started', polygon.tStartRefresh)
        Cued.addData('polygon.stopped', polygon.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Cued'
    
    
    # set up handler to look after randomisation of conditions etc
    Uncued = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('OneShotLearning_Shuffled.csv', selection=Condition_rows),
        seed=None, name='Uncued')
    thisExp.addLoop(Uncued)  # add the loop to the experiment
    thisUncued = Uncued.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisUncued.rgb)
    if thisUncued != None:
        for paramName in thisUncued:
            exec('{} = thisUncued[paramName]'.format(paramName))
    
    for thisUncued in Uncued:
        currentLoop = Uncued
        # abbreviate parameter names if possible (e.g. rgb = thisUncued.rgb)
        if thisUncued != None:
            for paramName in thisUncued:
                exec('{} = thisUncued[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Uncued_trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        image_2.setImage(StimFile)
        if key_resp_2.corr:
          total_corr=total_corr+1
          total_all=total_all+1
          rt=key_resp_2.rt
        
        else:
          total_all=total_all+1
          rt=key_resp_2.rt
        
        if Direction == ArrowImg:
            Congruency='Congruent'
        elif Direction == 'ArrowLeft.png' and ArrowImg == 'ArrowRight.png': 
            Congruency='Incongruent_opposite'
        elif Direction == 'ArrowRight.png' and ArrowImg == 'ArrowLeft.png':
            Congruency='Incongruent_opposite'
        elif Direction == 'neutral':
            Congruency='Neutral'
        else:
            Congruency='Incongruent_perpendicular'
        # keep track of which components have finished
        Uncued_trialComponents = [key_resp_2, image_2, direction_options]
        for thisComponent in Uncued_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Uncued_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Uncued_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Uncued_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Uncued_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)
            
            # *direction_options* updates
            if direction_options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                direction_options.frameNStart = frameN  # exact frame index
                direction_options.tStart = t  # local t and not account for scr refresh
                direction_options.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(direction_options, 'tStartRefresh')  # time at next scr refresh
                direction_options.setAutoDraw(True)
            if direction_options.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > direction_options.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    direction_options.tStop = t  # not accounting for scr refresh
                    direction_options.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(direction_options, 'tStopRefresh')  # time at next scr refresh
                    direction_options.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Uncued_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Uncued_trial"-------
        for thisComponent in Uncued_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        Uncued.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            Uncued.addData('key_resp_2.rt', key_resp_2.rt)
        Uncued.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        Uncued.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        Uncued.addData('image_2.started', image_2.tStartRefresh)
        Uncued.addData('image_2.stopped', image_2.tStopRefresh)
        thisExp.addData('Congruency', Congruency)
        Uncued.addData('direction_options.started', direction_options.tStartRefresh)
        Uncued.addData('direction_options.stopped', direction_options.tStopRefresh)
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_crossComponents = [polygon]
        for thisComponent in fix_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fix_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross"-------
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Uncued.addData('polygon.started', polygon.tStartRefresh)
        Uncued.addData('polygon.stopped', polygon.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Uncued'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_1'


# ------Prepare to start Routine "Finished"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinishedComponents = [text_2]
for thisComponent in FinishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Finished"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinishedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finished"-------
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
