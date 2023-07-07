#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on juli 07, 2023, at 09:05
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from baseline_code
timer = core.Clock()


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'FacesNamesProffessions_Encoding'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='C:\\Users\\Hassl\\OneDrive - Lund University\\Biofinder\\fMRI-tasks\\FacesNamesProfessions_fMRI\\Encoding_block\\Encoding_block_design_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instructions" ---
text = visual.TextStim(win=win, name='text',
    text='Instruktioner:\n\nDu kommer att se bilder på ansikten presenterade ett i taget.\nUnder varje bild så står ett NAMN eller ett YRKE .\nDin uppgift är att memorera varje persons namn eller yrke.\n\nVi kommer att se om du kommer ihåg dessa efter skanningen',
    font='Open Sans',
    pos=(0, 0), height=0.055, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0 = keyboard.Keyboard()

# --- Initialize components for Routine "init_parameters" ---
# Run 'Begin Experiment' code from param_init
n_images = 5
image_size = (0.748, 0.755)
image_position = (0, 0.05)
n_blocks = 8

blocks_per_condition = n_blocks /2
total_n_images = 20
image_duration = 5
circle_duration = 0.5
baseline_trial_duration = 5
ITI_duration = 1

condition = "Names_condition.xlsx"

baseline_time_limit = n_images * (image_duration+ITI_duration)

image_list = randchoice(total_n_images, total_n_images, False)
occupation = False

# --- Initialize components for Routine "trigger" ---
trigger_key = keyboard.Keyboard()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Snart börjar experimentet',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
# Run 'Begin Experiment' code from code_4
globalClock = core.Clock()
first_trigger = True

# --- Initialize components for Routine "New_Faces_info" ---
new_faces = visual.TextStim(win=win, name='new_faces',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Encode_info" ---
memorera_text = visual.TextStim(win=win, name='memorera_text',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from block_update
block_count = 0
name_occupation = "namn"

# --- Initialize components for Routine "Encoding_trial" ---
face_image = visual.ImageStim(
    win=win,
    name='face_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=image_position, size=image_size,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=False, depth=0.0)
name_profession = visual.TextStim(win=win, name='name_profession',
    text=None,
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "baseline_instructions" ---
baseline_intructions = visual.TextStim(win=win, name='baseline_intructions',
    text='Tryck när du ser triangeln',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "baseline" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
circle = visual.ShapeStim(
    win=win, name='circle',
    size=(0.15, 0.15), vertices='triangle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=15.0,     colorSpace='rgb',  lineColor='black', fillColor=None,
    opacity=None, depth=-2.0, interpolate=True)
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-3.0, interpolate=True)
circle_press = keyboard.Keyboard()

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Finished" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='Bra jobbat!\n\nDu har slutfört uppgiften. \nFortsätt ligga stilla så kommer vi prata med dig alldeles strax.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instructions" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "Instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        theseKeys = key_resp_0.getKeys(keyList=['1','2','3','space'], waitRelease=False)
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instructions" ---
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "init_parameters" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "init_parameters" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in init_parametersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "init_parameters" ---
for thisComponent in init_parametersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "init_parameters" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "trigger" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "trigger" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trigger_key.started')
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    # Run 'Each Frame' code from code_4
    if trigger_key.keys == 's' and first_trigger:
        expStart = globalClock.getTime()
        first_trigger =False
        core.wait(5)
        continueRoutine = False
    
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "trigger" ---
for thisComponent in triggerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if trigger_key.keys in ['', [], None]:  # No response was made
    trigger_key.keys = None
thisExp.addData('trigger_key.keys',trigger_key.keys)
if trigger_key.keys != None:  # we had a response
    thisExp.addData('trigger_key.rt', trigger_key.rt)
thisExp.nextEntry()
# the Routine "trigger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=n_blocks, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "New_Faces_info" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_5
    
    
    if block_count == 0:
        continueRoutine = False
    
    
    
    if block_count == blocks_per_condition:
        occupation = True
        new_faces.setText("Nu är det dags för yrken")
        condition = "Profession_condition.xlsx"
        first_occupation_block = True
    else: 
        new_faces.setText(f"Dags för {n_images} nya ansikten")
    
        
    
    # keep track of which components have finished
    New_Faces_infoComponents = [new_faces]
    for thisComponent in New_Faces_infoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "New_Faces_info" ---
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *new_faces* updates
        if new_faces.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            new_faces.frameNStart = frameN  # exact frame index
            new_faces.tStart = t  # local t and not account for scr refresh
            new_faces.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(new_faces, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'new_faces.started')
            new_faces.setAutoDraw(True)
        if new_faces.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > new_faces.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                new_faces.tStop = t  # not accounting for scr refresh
                new_faces.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'new_faces.stopped')
                new_faces.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in New_Faces_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "New_Faces_info" ---
    for thisComponent in New_Faces_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # --- Prepare to start Routine "Encode_info" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from block_update
    if occupation:
        name_occupation = "yrkestitel"
        if first_occupation_block:
            image_list = randchoice(total_n_images, total_n_images, False)
            first_occupation_block = False
    
    memorera_text.setText(f"Memorera {name_occupation}")
    
    block_count += 1
    
    selected_images =  np.random.choice(image_list, size=n_images, replace=False)
    print("Selected rows:", selected_images)
    
    # Update the list by removing the extracted numbers
    image_list = np.setdiff1d(image_list, selected_images)
    
    print("Updated list:", image_list)
    print(f"Starting block: {block_count}")
    
    
    
    # keep track of which components have finished
    Encode_infoComponents = [memorera_text]
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
    frameN = -1
    
    # --- Run Routine "Encode_info" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *memorera_text* updates
        if memorera_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            memorera_text.frameNStart = frameN  # exact frame index
            memorera_text.tStart = t  # local t and not account for scr refresh
            memorera_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memorera_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'memorera_text.started')
            memorera_text.setAutoDraw(True)
        if memorera_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > memorera_text.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                memorera_text.tStop = t  # not accounting for scr refresh
                memorera_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'memorera_text.stopped')
                memorera_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Encode_infoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Encode_info" ---
    for thisComponent in Encode_infoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from block_update
    
    
    
    
    
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # set up handler to look after randomisation of conditions etc
    Encoding = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condition, selection=selected_images),
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
        
        # --- Prepare to start Routine "Encoding_trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        face_image.setImage(StimFile)
        name_profession.setText('')
        # Run 'Begin Routine' code from code_3
        
        
        if Name == 0:
            name_profession.text = Proffession
        else:
            name_profession.text = Name
        # keep track of which components have finished
        Encoding_trialComponents = [face_image, name_profession]
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
        frameN = -1
        
        # --- Run Routine "Encoding_trial" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *face_image* updates
            if face_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                face_image.frameNStart = frameN  # exact frame index
                face_image.tStart = t  # local t and not account for scr refresh
                face_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(face_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'face_image.started')
                face_image.setAutoDraw(True)
            if face_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > face_image.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    face_image.tStop = t  # not accounting for scr refresh
                    face_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'face_image.stopped')
                    face_image.setAutoDraw(False)
            
            # *name_profession* updates
            if name_profession.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                name_profession.frameNStart = frameN  # exact frame index
                name_profession.tStart = t  # local t and not account for scr refresh
                name_profession.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(name_profession, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'name_profession.started')
                name_profession.setAutoDraw(True)
            if name_profession.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > name_profession.tStartRefresh + image_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    name_profession.tStop = t  # not accounting for scr refresh
                    name_profession.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'name_profession.stopped')
                    name_profession.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Encoding_trial" ---
        for thisComponent in Encoding_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Encoding_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [blank_screen]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_screen* updates
            if blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_screen.frameNStart = frameN  # exact frame index
                blank_screen.tStart = t  # local t and not account for scr refresh
                blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_screen.started')
                blank_screen.setAutoDraw(True)
            if blank_screen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_screen.tStartRefresh + ITI_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_screen.tStop = t  # not accounting for scr refresh
                    blank_screen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank_screen.stopped')
                    blank_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
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
    
    # --- Prepare to start Routine "baseline_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    baseline_instructionsComponents = [baseline_intructions]
    for thisComponent in baseline_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "baseline_instructions" ---
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_intructions* updates
        if baseline_intructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_intructions.frameNStart = frameN  # exact frame index
            baseline_intructions.tStart = t  # local t and not account for scr refresh
            baseline_intructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_intructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'baseline_intructions.started')
            baseline_intructions.setAutoDraw(True)
        if baseline_intructions.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > baseline_intructions.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                baseline_intructions.tStop = t  # not accounting for scr refresh
                baseline_intructions.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'baseline_intructions.stopped')
                baseline_intructions.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baseline_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "baseline_instructions" ---
    for thisComponent in baseline_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # set up handler to look after randomisation of conditions etc
    baseline_trials = data.TrialHandler(nReps=1000.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='baseline_trials')
    thisExp.addLoop(baseline_trials)  # add the loop to the experiment
    thisBaseline_trial = baseline_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
    if thisBaseline_trial != None:
        for paramName in thisBaseline_trial:
            exec('{} = thisBaseline_trial[paramName]'.format(paramName))
    
    for thisBaseline_trial in baseline_trials:
        currentLoop = baseline_trials
        # abbreviate parameter names if possible (e.g. rgb = thisBaseline_trial.rgb)
        if thisBaseline_trial != None:
            for paramName in thisBaseline_trial:
                exec('{} = thisBaseline_trial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "baseline" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from baseline_code
        cross_duration = np.random.uniform(1.5, 2.5)
        
        circle_start = cross_duration + .01
        
        second_cross_start = circle_start + circle_duration
        second_cross_duration = baseline_trial_duration - second_cross_start
          
        print(f"cross duration: {cross_duration}")
        print(f"Trial duration = {second_cross_start+second_cross_duration}")
        
        if baseline_trials.thisN == 0:
            block_start_time = timer.getTime() 
        circle_press.keys = []
        circle_press.rt = []
        _circle_press_allKeys = []
        # keep track of which components have finished
        baselineComponents = [polygon, circle, polygon_2, circle_press]
        for thisComponent in baselineComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "baseline" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + cross_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            # Run 'Each Frame' code from baseline_code
            if timer.getTime() - block_start_time >= baseline_time_limit -0.01:
                continueRoutine = False
                baseline_trials.finished = True
                
             
            if len(circle_press.keys)>0:
                baseline_trials.addData("Key", circle_press.keys)
            
            # *circle* updates
            if circle.status == NOT_STARTED and tThisFlip >= circle_start-frameTolerance:
                # keep track of start time/frame for later
                circle.frameNStart = frameN  # exact frame index
                circle.tStart = t  # local t and not account for scr refresh
                circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle.started')
                circle.setAutoDraw(True)
            if circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle.tStartRefresh + circle_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    circle.tStop = t  # not accounting for scr refresh
                    circle.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle.stopped')
                    circle.setAutoDraw(False)
            
            # *polygon_2* updates
            if polygon_2.status == NOT_STARTED and tThisFlip >= second_cross_start-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.started')
                polygon_2.setAutoDraw(True)
            if polygon_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_2.tStartRefresh + second_cross_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_2.tStop = t  # not accounting for scr refresh
                    polygon_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                    polygon_2.setAutoDraw(False)
            
            # *circle_press* updates
            waitOnFlip = False
            if circle_press.status == NOT_STARTED and tThisFlip >= circle_start-frameTolerance:
                # keep track of start time/frame for later
                circle_press.frameNStart = frameN  # exact frame index
                circle_press.tStart = t  # local t and not account for scr refresh
                circle_press.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(circle_press, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'circle_press.started')
                circle_press.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(circle_press.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(circle_press.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if circle_press.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > circle_press.tStartRefresh + circle_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    circle_press.tStop = t  # not accounting for scr refresh
                    circle_press.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'circle_press.stopped')
                    circle_press.status = FINISHED
            if circle_press.status == STARTED and not waitOnFlip:
                theseKeys = circle_press.getKeys(keyList=['1', '2', '3', '4', '5', '6', '7', '8'], waitRelease=False)
                _circle_press_allKeys.extend(theseKeys)
                if len(_circle_press_allKeys):
                    circle_press.keys = _circle_press_allKeys[0].name  # just the first key pressed
                    circle_press.rt = _circle_press_allKeys[0].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in baselineComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "baseline" ---
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if circle_press.keys in ['', [], None]:  # No response was made
            circle_press.keys = None
        baseline_trials.addData('circle_press.keys',circle_press.keys)
        if circle_press.keys != None:  # we had a response
            baseline_trials.addData('circle_press.rt', circle_press.rt)
        # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [blank_screen]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ITI" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank_screen* updates
            if blank_screen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank_screen.frameNStart = frameN  # exact frame index
                blank_screen.tStart = t  # local t and not account for scr refresh
                blank_screen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank_screen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank_screen.started')
                blank_screen.setAutoDraw(True)
            if blank_screen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank_screen.tStartRefresh + ITI_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    blank_screen.tStop = t  # not accounting for scr refresh
                    blank_screen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank_screen.stopped')
                    blank_screen.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1000.0 repeats of 'baseline_trials'
    
    # get names of stimulus parameters
    if baseline_trials.trialList in ([], [None], None):
        params = []
    else:
        params = baseline_trials.trialList[0].keys()
    # save data for this loop
    baseline_trials.saveAsExcel(filename + '.xlsx', sheetName='baseline_trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed n_blocks repeats of 'block'


# --- Prepare to start Routine "Finished" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "Finished" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Finished" ---
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)
# Run 'End Experiment' code from code_4
expTime = globalClock.getTime() - expStart


print(f"Duration of experiment: {expTime} seconds")

thisExp.addData("Exeriment Duration", expTime)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
