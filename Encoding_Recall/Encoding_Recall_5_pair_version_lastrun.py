#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on mars 01, 2023, at 16:04
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
psychopyVersion = '2021.1.4'
expName = 'FacesNamesProffessions_Encoding'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\HP\\Documents\\My Experiments\\7T\\7T060\\FacesNamesProfessions_fMRI\\Encoding_Recall\\Encoding_Recall_5_pair_version_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Instruktioner:\n\nDu kommer att se bilder på ansikten presenterade ett i taget.\nUnder varje bild så står ett NAMN eller ett YRKE .\nDin uppgift är att memorera varje persons namn eller yrke.\n\nEfter det kommer ansikten visas med 3 bokstäver och "NY" under bilden. Din uppgift då är att välja den korrekta första bokstaven i Namnet eller Yrket till ansiktet som visas. Om du aldrig sett ansiktet tidigare så väljer du "NY".\n\nSvara på varje bild med hjälp av följande knappar:\n1 (pekfinger) = VÄNSTER       \n2 (långfinger) = MITTEN\n3 (ringfinger) = HÖGER\n4 (lillfinger) = NY\n\nNär du ser ett kors på skärmen så ska du bara titta på det.\n\nVi vet att det är en svår uppgift så gör så gott du kan och lycka till!\n\nTryck med pekfingret och meddela när du är redo att börja.\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0 = keyboard.Keyboard()
# Set experiment start values for variable component occupation
occupation = 0
occupationContainer = []

# Initialize components for Routine "init_parameters"
init_parametersClock = core.Clock()
block = 0
n_images = 5
jitter = np.arange(2.5, 10, .25)
cross_duration_mean = 4
image_size = (0.748, 0.755)
image_position = (0, 0.05)
n_blocks = 6



# Initialize components for Routine "trigger"
triggerClock = core.Clock()
trigger_key = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Snart börjar experimentet',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Encode_info"
Encode_infoClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Encoding_trial"
Encoding_trialClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=image_position, size=image_size,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=0.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text=None,
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Recall_info"
Recall_infoClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fingers = visual.TextStim(win=win, name='fingers',
    text=None,
    font='Open Sans',
    pos=(0, -0.25), height=0.045, wrapWidth=600.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Recall_trial"
Recall_trialClock = core.Clock()
key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=image_position, size=image_size,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-2.0)
letters_text = visual.TextStim(win=win, name='letters_text',
    text='',
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instructions_occupation"
instructions_occupationClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Nu är det dags för yrken',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Encode_info"
Encode_infoClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Encoding_trial"
Encoding_trialClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=image_position, size=image_size,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=0.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text=None,
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Recall_info"
Recall_infoClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
fingers = visual.TextStim(win=win, name='fingers',
    text=None,
    font='Open Sans',
    pos=(0, -0.25), height=0.045, wrapWidth=600.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "Recall_trial"
Recall_trialClock = core.Clock()
key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=image_position, size=image_size,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=-2.0)
letters_text = visual.TextStim(win=win, name='letters_text',
    text='',
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=1000.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Finished"
FinishedClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Bra jobbat!\n\nDu har slutfört uppgiften. \nFortsätt ligga stilla så kommer vi prata med dig alldeles strax.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
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
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "init_parameters"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
init_parametersComponents = []
for thisComponent in init_parametersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
init_parametersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "init_parameters"-------
while continueRoutine:
    # get current time
    t = init_parametersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=init_parametersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in init_parametersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "init_parameters"-------
for thisComponent in init_parametersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init_parameters" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trigger"-------
continueRoutine = True
# update component parameters for each repeat
trigger_key.keys = []
trigger_key.rt = []
_trigger_key_allKeys = []
# keep track of which components have finished
triggerComponents = [trigger_key, text_3]
for thisComponent in triggerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
triggerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trigger"-------
while continueRoutine:
    # get current time
    t = triggerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=triggerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *trigger_key* updates
    waitOnFlip = False
    if trigger_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_key.frameNStart = frameN  # exact frame index
        trigger_key.tStart = t  # local t and not account for scr refresh
        trigger_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_key, 'tStartRefresh')  # time at next scr refresh
        trigger_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_key.status == STARTED and not waitOnFlip:
        theseKeys = trigger_key.getKeys(keyList=['s'], waitRelease=False)
        _trigger_key_allKeys.extend(theseKeys)
        if len(_trigger_key_allKeys):
            trigger_key.keys = _trigger_key_allKeys[-1].name  # just the last key pressed
            trigger_key.rt = _trigger_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if trigger_key.keys == 's':
        core.wait(6)
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trigger"-------
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_key.keys in ['', [], None]:  # No response was made
    trigger_key.keys = None
thisExp.addData('trigger_key.keys',trigger_key.keys)
if trigger_key.keys != None:  # we had a response
    thisExp.addData('trigger_key.rt', trigger_key.rt)
thisExp.addData('trigger_key.started', trigger_key.tStartRefresh)
thisExp.addData('trigger_key.stopped', trigger_key.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
name_blocks = data.TrialHandler(nReps=n_blocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='name_blocks')
thisExp.addLoop(name_blocks)  # add the loop to the experiment
thisName_block = name_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisName_block.rgb)
if thisName_block != None:
    for paramName in thisName_block:
        exec('{} = thisName_block[paramName]'.format(paramName))

for thisName_block in name_blocks:
    currentLoop = name_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisName_block.rgb)
    if thisName_block != None:
        for paramName in thisName_block:
            exec('{} = thisName_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Encode_info"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    name_occupation = "namn"
    if occupation == 1:
        name_occupation = "yrkestitel"
    
    text_9.setText(f"Memorera {name_occupation}")
    
    
    print(f"Starting block: {block+1}")
    
    if block == 0:
        start_row = block
    else:
        start_row = block * n_images 
    
        
    end = start_row + n_images
    
    selection = f'{start_row}:{end}'
    
    
    # keep track of which components have finished
    Encode_infoComponents = [text_9]
    for thisComponent in Encode_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Encode_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Encode_info"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Encode_infoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Encode_infoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Encode_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Encode_info"-------
    for thisComponent in Encode_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    name_blocks.addData('text_9.started', text_9.tStartRefresh)
    name_blocks.addData('text_9.stopped', text_9.tStopRefresh)
    block +=1
    
    
    
    print(f'starting row: {start_row}\ending row: {end}')
    
    
    # set up handler to look after randomisation of conditions etc
    Encoding = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Names_condition.xlsx', selection=selection),
        seed=None, name='Encoding')
    thisExp.addLoop(Encoding)  # add the loop to the experiment
    thisEncoding = Encoding.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncoding.rgb)
    if thisEncoding != None:
        for paramName in thisEncoding:
            exec('{} = thisEncoding[paramName]'.format(paramName))
    
    for thisEncoding in Encoding:
        currentLoop = Encoding
        # abbreviate parameter names if possible (e.g. rgb = thisEncoding.rgb)
        if thisEncoding != None:
            for paramName in thisEncoding:
                exec('{} = thisEncoding[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        cross_duration = normal(cross_duration_mean,2.2)
        
        if cross_duration > 8:
            cross_duration = 8
        if cross_duration < 2:
            cross_duration = 2
          
        print(f"cross duration: {cross_duration}")
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
        while continueRoutine:
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
                if tThisFlipGlobal > polygon.tStartRefresh + cross_duration-frameTolerance:
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
        Encoding.addData('polygon.started', polygon.tStartRefresh)
        Encoding.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Encoding_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image_3.setImage(StimFile)
        text_8.setText('')
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        circlestart = (jitter[0]/2)-0.5
        
        
        if Name == 0:
            text_8.text = Proffession
        else:
            text_8.text = Name
        # keep track of which components have finished
        Encoding_trialComponents = [image_3, text_8]
        for thisComponent in Encoding_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Encoding_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Encoding_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Encoding_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Encoding_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Encoding_trial"-------
        for thisComponent in Encoding_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Encoding.addData('image_3.started', image_3.tStartRefresh)
        Encoding.addData('image_3.stopped', image_3.tStopRefresh)
        Encoding.addData('text_8.started', text_8.tStartRefresh)
        Encoding.addData('text_8.stopped', text_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Encoding'
    
    # get names of stimulus parameters
    if Encoding.trialList in ([], [None], None):
        params = []
    else:
        params = Encoding.trialList[0].keys()
    # save data for this loop
    Encoding.saveAsExcel(filename + '.xlsx', sheetName='Encoding',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Recall_info"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    name_occupation = "namn"
    if occupation:
        name_occupation = "yrkestitel"
    
    text_6.setText(f"Välj första bokstaven i personens {name_occupation}")
    
    fingers.setText("1 - Pekfinger, 2 - Långfinger, 3 - Ringfinger, 4 - Lillfinger")
    # keep track of which components have finished
    Recall_infoComponents = [text_6, fingers]
    for thisComponent in Recall_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Recall_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall_info"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Recall_infoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Recall_infoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *fingers* updates
        if fingers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fingers.frameNStart = frameN  # exact frame index
            fingers.tStart = t  # local t and not account for scr refresh
            fingers.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fingers, 'tStartRefresh')  # time at next scr refresh
            fingers.setAutoDraw(True)
        if fingers.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fingers.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                fingers.tStop = t  # not accounting for scr refresh
                fingers.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fingers, 'tStopRefresh')  # time at next scr refresh
                fingers.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recall_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall_info"-------
    for thisComponent in Recall_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    name_blocks.addData('text_6.started', text_6.tStartRefresh)
    name_blocks.addData('text_6.stopped', text_6.tStopRefresh)
    name_blocks.addData('fingers.started', fingers.tStartRefresh)
    name_blocks.addData('fingers.stopped', fingers.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    Recall = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Names_condition.xlsx', selection=selection),
        seed=None, name='Recall')
    thisExp.addLoop(Recall)  # add the loop to the experiment
    thisRecall = Recall.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
    if thisRecall != None:
        for paramName in thisRecall:
            exec('{} = thisRecall[paramName]'.format(paramName))
    
    for thisRecall in Recall:
        currentLoop = Recall
        # abbreviate parameter names if possible (e.g. rgb = thisRecall.rgb)
        if thisRecall != None:
            for paramName in thisRecall:
                exec('{} = thisRecall[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        cross_duration = normal(cross_duration_mean,2.2)
        
        if cross_duration > 8:
            cross_duration = 8
        if cross_duration < 2:
            cross_duration = 2
          
        print(f"cross duration: {cross_duration}")
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
        while continueRoutine:
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
                if tThisFlipGlobal > polygon.tStartRefresh + cross_duration-frameTolerance:
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
        Recall.addData('polygon.started', polygon.tStartRefresh)
        Recall.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Recall_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        
        
        alphabet = 'ABCDEFGHIJKLMNOPRSTUV'
        
        if Name != 0:
            correct = Name[0]
        elif Proffession != 0:
            correct = Proffession[0]
            
        letter_alternatives = alphabet.replace(correct, '')
        
        correct = f'{correct}.'
        
        
        letter1 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        letter2 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        
        while letter1 == letter2:
            print("Same letter randomised, performing randmoisation again..")
            letter2 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        
        
        letters_lst = [correct, letter1, letter2]
        shuffle(letters_lst)
        
        letters_lst.append("NY")
        
        letters = "\t\t\t\t".join(letters_lst)
        correct_answer = letters_lst.index(correct) + 1
        
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        image.setImage(StimFile)
        letters_text.setText(letters)
        # keep track of which components have finished
        Recall_trialComponents = [key_resp_1, image, letters_text]
        for thisComponent in Recall_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Recall_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Recall_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Recall_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Recall_trialClock)
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
                if tThisFlipGlobal > key_resp_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_1.tStop = t  # not accounting for scr refresh
                    key_resp_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_1, 'tStopRefresh')  # time at next scr refresh
                    key_resp_1.status = FINISHED
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = [key.name for key in _key_resp_1_allKeys]  # storing all keys
                    key_resp_1.rt = [key.rt for key in _key_resp_1_allKeys]
                    # was this correct?
                    if (key_resp_1.keys == str(correct_answer)) or (key_resp_1.keys == correct_answer):
                        key_resp_1.corr = 1
                    else:
                        key_resp_1.corr = 0
            
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
                if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *letters_text* updates
            if letters_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                letters_text.frameNStart = frameN  # exact frame index
                letters_text.tStart = t  # local t and not account for scr refresh
                letters_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letters_text, 'tStartRefresh')  # time at next scr refresh
                letters_text.setAutoDraw(True)
            if letters_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > letters_text.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    letters_text.tStop = t  # not accounting for scr refresh
                    letters_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(letters_text, 'tStopRefresh')  # time at next scr refresh
                    letters_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Recall_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Recall_trial"-------
        for thisComponent in Recall_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        Recall.addData("correct", correct_answer)
        
        if occupation == 1:
            Recall_prof.addData("correct", correct_answer)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
            # was no response the correct answer?!
            if str(correct_answer).lower() == 'none':
               key_resp_1.corr = 1;  # correct non-response
            else:
               key_resp_1.corr = 0;  # failed to respond (incorrectly)
        # store data for Recall (TrialHandler)
        Recall.addData('key_resp_1.keys',key_resp_1.keys)
        Recall.addData('key_resp_1.corr', key_resp_1.corr)
        if key_resp_1.keys != None:  # we had a response
            Recall.addData('key_resp_1.rt', key_resp_1.rt)
        Recall.addData('key_resp_1.started', key_resp_1.tStartRefresh)
        Recall.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
        Recall.addData('image.started', image.tStartRefresh)
        Recall.addData('image.stopped', image.tStopRefresh)
        Recall.addData('letters_text.started', letters_text.tStartRefresh)
        Recall.addData('letters_text.stopped', letters_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Recall'
    
    # get names of stimulus parameters
    if Recall.trialList in ([], [None], None):
        params = []
    else:
        params = Recall.trialList[0].keys()
    # save data for this loop
    Recall.saveAsExcel(filename + '.xlsx', sheetName='Recall',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed n_blocks repeats of 'name_blocks'


# ------Prepare to start Routine "instructions_occupation"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
occupation =1 
block = 0
# keep track of which components have finished
instructions_occupationComponents = [instructions]
for thisComponent in instructions_occupationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_occupationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_occupation"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions_occupationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_occupationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instructions, 'tStopRefresh')  # time at next scr refresh
            instructions.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_occupationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_occupation"-------
for thisComponent in instructions_occupationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)

# set up handler to look after randomisation of conditions etc
profession_blocks = data.TrialHandler(nReps=n_blocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='profession_blocks')
thisExp.addLoop(profession_blocks)  # add the loop to the experiment
thisProfession_block = profession_blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisProfession_block.rgb)
if thisProfession_block != None:
    for paramName in thisProfession_block:
        exec('{} = thisProfession_block[paramName]'.format(paramName))

for thisProfession_block in profession_blocks:
    currentLoop = profession_blocks
    # abbreviate parameter names if possible (e.g. rgb = thisProfession_block.rgb)
    if thisProfession_block != None:
        for paramName in thisProfession_block:
            exec('{} = thisProfession_block[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Encode_info"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    name_occupation = "namn"
    if occupation == 1:
        name_occupation = "yrkestitel"
    
    text_9.setText(f"Memorera {name_occupation}")
    
    
    print(f"Starting block: {block+1}")
    
    if block == 0:
        start_row = block
    else:
        start_row = block * n_images 
    
        
    end = start_row + n_images
    
    selection = f'{start_row}:{end}'
    
    
    # keep track of which components have finished
    Encode_infoComponents = [text_9]
    for thisComponent in Encode_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Encode_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Encode_info"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Encode_infoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Encode_infoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Encode_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Encode_info"-------
    for thisComponent in Encode_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    profession_blocks.addData('text_9.started', text_9.tStartRefresh)
    profession_blocks.addData('text_9.stopped', text_9.tStopRefresh)
    block +=1
    
    
    
    print(f'starting row: {start_row}\ending row: {end}')
    
    
    # set up handler to look after randomisation of conditions etc
    Encoding_prof = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Profession_condition.xlsx', selection=selection),
        seed=None, name='Encoding_prof')
    thisExp.addLoop(Encoding_prof)  # add the loop to the experiment
    thisEncoding_prof = Encoding_prof.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncoding_prof.rgb)
    if thisEncoding_prof != None:
        for paramName in thisEncoding_prof:
            exec('{} = thisEncoding_prof[paramName]'.format(paramName))
    
    for thisEncoding_prof in Encoding_prof:
        currentLoop = Encoding_prof
        # abbreviate parameter names if possible (e.g. rgb = thisEncoding_prof.rgb)
        if thisEncoding_prof != None:
            for paramName in thisEncoding_prof:
                exec('{} = thisEncoding_prof[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        cross_duration = normal(cross_duration_mean,2.2)
        
        if cross_duration > 8:
            cross_duration = 8
        if cross_duration < 2:
            cross_duration = 2
          
        print(f"cross duration: {cross_duration}")
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
        while continueRoutine:
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
                if tThisFlipGlobal > polygon.tStartRefresh + cross_duration-frameTolerance:
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
        Encoding_prof.addData('polygon.started', polygon.tStartRefresh)
        Encoding_prof.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Encoding_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image_3.setImage(StimFile)
        text_8.setText('')
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        circlestart = (jitter[0]/2)-0.5
        
        
        if Name == 0:
            text_8.text = Proffession
        else:
            text_8.text = Name
        # keep track of which components have finished
        Encoding_trialComponents = [image_3, text_8]
        for thisComponent in Encoding_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Encoding_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Encoding_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Encoding_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Encoding_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *text_8* updates
            if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_8.frameNStart = frameN  # exact frame index
                text_8.tStart = t  # local t and not account for scr refresh
                text_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
                text_8.setAutoDraw(True)
            if text_8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_8.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_8.tStop = t  # not accounting for scr refresh
                    text_8.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                    text_8.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Encoding_trial"-------
        for thisComponent in Encoding_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Encoding_prof.addData('image_3.started', image_3.tStartRefresh)
        Encoding_prof.addData('image_3.stopped', image_3.tStopRefresh)
        Encoding_prof.addData('text_8.started', text_8.tStartRefresh)
        Encoding_prof.addData('text_8.stopped', text_8.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Encoding_prof'
    
    # get names of stimulus parameters
    if Encoding_prof.trialList in ([], [None], None):
        params = []
    else:
        params = Encoding_prof.trialList[0].keys()
    # save data for this loop
    Encoding_prof.saveAsExcel(filename + '.xlsx', sheetName='Encoding_prof',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "Recall_info"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    name_occupation = "namn"
    if occupation:
        name_occupation = "yrkestitel"
    
    text_6.setText(f"Välj första bokstaven i personens {name_occupation}")
    
    fingers.setText("1 - Pekfinger, 2 - Långfinger, 3 - Ringfinger, 4 - Lillfinger")
    # keep track of which components have finished
    Recall_infoComponents = [text_6, fingers]
    for thisComponent in Recall_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Recall_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Recall_info"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Recall_infoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Recall_infoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *fingers* updates
        if fingers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fingers.frameNStart = frameN  # exact frame index
            fingers.tStart = t  # local t and not account for scr refresh
            fingers.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fingers, 'tStartRefresh')  # time at next scr refresh
            fingers.setAutoDraw(True)
        if fingers.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fingers.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                fingers.tStop = t  # not accounting for scr refresh
                fingers.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fingers, 'tStopRefresh')  # time at next scr refresh
                fingers.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recall_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Recall_info"-------
    for thisComponent in Recall_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    profession_blocks.addData('text_6.started', text_6.tStartRefresh)
    profession_blocks.addData('text_6.stopped', text_6.tStopRefresh)
    profession_blocks.addData('fingers.started', fingers.tStartRefresh)
    profession_blocks.addData('fingers.stopped', fingers.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    Recall_prof = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Profession_condition.xlsx', selection=selection),
        seed=None, name='Recall_prof')
    thisExp.addLoop(Recall_prof)  # add the loop to the experiment
    thisRecall_prof = Recall_prof.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRecall_prof.rgb)
    if thisRecall_prof != None:
        for paramName in thisRecall_prof:
            exec('{} = thisRecall_prof[paramName]'.format(paramName))
    
    for thisRecall_prof in Recall_prof:
        currentLoop = Recall_prof
        # abbreviate parameter names if possible (e.g. rgb = thisRecall_prof.rgb)
        if thisRecall_prof != None:
            for paramName in thisRecall_prof:
                exec('{} = thisRecall_prof[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        cross_duration = normal(cross_duration_mean,2.2)
        
        if cross_duration > 8:
            cross_duration = 8
        if cross_duration < 2:
            cross_duration = 2
          
        print(f"cross duration: {cross_duration}")
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
        while continueRoutine:
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
                if tThisFlipGlobal > polygon.tStartRefresh + cross_duration-frameTolerance:
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
        Recall_prof.addData('polygon.started', polygon.tStartRefresh)
        Recall_prof.addData('polygon.stopped', polygon.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Recall_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        
        
        alphabet = 'ABCDEFGHIJKLMNOPRSTUV'
        
        if Name != 0:
            correct = Name[0]
        elif Proffession != 0:
            correct = Proffession[0]
            
        letter_alternatives = alphabet.replace(correct, '')
        
        correct = f'{correct}.'
        
        
        letter1 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        letter2 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        
        while letter1 == letter2:
            print("Same letter randomised, performing randmoisation again..")
            letter2 = f'{letter_alternatives[randint(0, len(letter_alternatives)-1)]}.'
        
        
        letters_lst = [correct, letter1, letter2]
        shuffle(letters_lst)
        
        letters_lst.append("NY")
        
        letters = "\t\t\t\t".join(letters_lst)
        correct_answer = letters_lst.index(correct) + 1
        
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        image.setImage(StimFile)
        letters_text.setText(letters)
        # keep track of which components have finished
        Recall_trialComponents = [key_resp_1, image, letters_text]
        for thisComponent in Recall_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Recall_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Recall_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Recall_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Recall_trialClock)
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
                if tThisFlipGlobal > key_resp_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_1.tStop = t  # not accounting for scr refresh
                    key_resp_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_1, 'tStopRefresh')  # time at next scr refresh
                    key_resp_1.status = FINISHED
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = [key.name for key in _key_resp_1_allKeys]  # storing all keys
                    key_resp_1.rt = [key.rt for key in _key_resp_1_allKeys]
                    # was this correct?
                    if (key_resp_1.keys == str(correct_answer)) or (key_resp_1.keys == correct_answer):
                        key_resp_1.corr = 1
                    else:
                        key_resp_1.corr = 0
            
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
                if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *letters_text* updates
            if letters_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                letters_text.frameNStart = frameN  # exact frame index
                letters_text.tStart = t  # local t and not account for scr refresh
                letters_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(letters_text, 'tStartRefresh')  # time at next scr refresh
                letters_text.setAutoDraw(True)
            if letters_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > letters_text.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    letters_text.tStop = t  # not accounting for scr refresh
                    letters_text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(letters_text, 'tStopRefresh')  # time at next scr refresh
                    letters_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Recall_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Recall_trial"-------
        for thisComponent in Recall_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        Recall.addData("correct", correct_answer)
        
        if occupation == 1:
            Recall_prof.addData("correct", correct_answer)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
            # was no response the correct answer?!
            if str(correct_answer).lower() == 'none':
               key_resp_1.corr = 1;  # correct non-response
            else:
               key_resp_1.corr = 0;  # failed to respond (incorrectly)
        # store data for Recall_prof (TrialHandler)
        Recall_prof.addData('key_resp_1.keys',key_resp_1.keys)
        Recall_prof.addData('key_resp_1.corr', key_resp_1.corr)
        if key_resp_1.keys != None:  # we had a response
            Recall_prof.addData('key_resp_1.rt', key_resp_1.rt)
        Recall_prof.addData('key_resp_1.started', key_resp_1.tStartRefresh)
        Recall_prof.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
        Recall_prof.addData('image.started', image.tStartRefresh)
        Recall_prof.addData('image.stopped', image.tStopRefresh)
        Recall_prof.addData('letters_text.started', letters_text.tStartRefresh)
        Recall_prof.addData('letters_text.stopped', letters_text.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Recall_prof'
    
    # get names of stimulus parameters
    if Recall_prof.trialList in ([], [None], None):
        params = []
    else:
        params = Recall_prof.trialList[0].keys()
    # save data for this loop
    Recall_prof.saveAsExcel(filename + '.xlsx', sheetName='Recall_prof',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed n_blocks repeats of 'profession_blocks'


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

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
