#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on juni 02, 2023, at 14:34
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'FaceNameProfession_recall'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Hassl\\OneDrive - Lund University\\Biofinder\\fMRI-tasks\\FacesNamesProfessions_fMRI\\Recall\\Recall_with_ITI_lastrun.py',
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
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
    text='Instruktioner:\n\nDu kommer att se bilder på ansikten presenterade ett i taget.\nVarje ansikte visas med 3 bokstäver och "NY" under bilden. Din uppgift då är att välja den korrekta första bokstaven i Namnet eller Yrket till ansiktet som visas. Om du aldrig sett ansiktet tidigare så väljer du "NY".\n\nSvara på varje bild med hjälp av följande knappar:\n1 (pekfinger) = VÄNSTER       \n2 (långfinger) = MITTEN\n3 (ringfinger) = HÖGER\n4 (lillfinger) = NY\n\nNär du ser ett kors på skärmen så ska du bara titta på det.\n\nVi vet att det är en svår uppgift så gör så gott du kan och lycka till!\n\nTryck med pekfingret och meddela när du är redo att börja.\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0 = keyboard.Keyboard()
# Set experiment start values for variable component occupation
occupation = 0
occupationContainer = []

# --- Initialize components for Routine "init_parameters" ---
# Run 'Begin Experiment' code from param_init
block = 0
n_images = 40
image_duration = 5
image_size = (0.748, 0.755)
image_position = (0, 0.05)
images_per_condition = 40


images_selection = randchoice(images_per_condition, n_images, False)

# --- Initialize components for Routine "Wait_fMRI" ---
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_4
timer = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Snart börjar experimentet!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall_info" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code_5
name_occupation = "namn"
occupation = False
fingers = visual.TextStim(win=win, name='fingers',
    text=None,
    font='Open Sans',
    pos=(0, -0.25), height=0.045, wrapWidth=600.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall_trial" ---
# Run 'Begin Experiment' code from code_2
face_count = 0

key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from duration_setter
#values = [2.5, 5, 7.5, 10]
#target_sum = 400
#num_values = 80

# Create an initial list with random values
#initial_list = np.random.choice(values, num_values)

# Calculate the sum of the initial list
#current_sum = sum(initial_list)

# Calculate the difference between the target sum and current sum
#diff = target_sum - current_sum

# Randomly adjust values in the list until the sum matches the target sum
#while diff != 0:
    # Choose a random index in the list
#    index = np.random.randint(0, num_values - 1)
    # Choose a random value from the options
#    new_value = np.random.choice(values)

    # Update the list at the chosen index with the new value
#    initial_list[index] = new_value

    # Update the current sum and difference
#    current_sum = sum(initial_list)
#    diff = target_sum - current_sum

ITI_durations = values = [7.5, 5, 5, 7.5, 2.5, 5, 2.5, 5, 5, 5, 2.5, 7.5, 2.5, 2.5, 5, 5, 5, 7.5, 7.5, 5, 2.5, 5, 10, 7.5, 2.5, 2.5, 2.5, 7.5, 2.5, 2.5, 7.5, 5, 7.5, 2.5, 5, 7.5, 2.5, 5, 10, 5, 5, 7.5, 2.5, 2.5, 5, 10, 2.5, 2.5, 2.5, 10, 2.5, 5, 2.5, 2.5, 2.5, 5, 10, 2.5, 10, 5, 2.5, 2.5, 2.5, 2.5, 7.5, 5, 2.5, 2.5, 7.5, 5, 10, 10, 2.5, 5, 7.5, 7.5, 5, 5, 2.5, 5]



# --- Initialize components for Routine "fix_cross" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from duration_setter
#values = [2.5, 5, 7.5, 10]
#target_sum = 400
#num_values = 80

# Create an initial list with random values
#initial_list = np.random.choice(values, num_values)

# Calculate the sum of the initial list
#current_sum = sum(initial_list)

# Calculate the difference between the target sum and current sum
#diff = target_sum - current_sum

# Randomly adjust values in the list until the sum matches the target sum
#while diff != 0:
    # Choose a random index in the list
#    index = np.random.randint(0, num_values - 1)
    # Choose a random value from the options
#    new_value = np.random.choice(values)

    # Update the list at the chosen index with the new value
#    initial_list[index] = new_value

    # Update the current sum and difference
#    current_sum = sum(initial_list)
#    diff = target_sum - current_sum

ITI_durations = values = [7.5, 5, 5, 7.5, 2.5, 5, 2.5, 5, 5, 5, 2.5, 7.5, 2.5, 2.5, 5, 5, 5, 7.5, 7.5, 5, 2.5, 5, 10, 7.5, 2.5, 2.5, 2.5, 7.5, 2.5, 2.5, 7.5, 5, 7.5, 2.5, 5, 7.5, 2.5, 5, 10, 5, 5, 7.5, 2.5, 2.5, 5, 10, 2.5, 2.5, 2.5, 10, 2.5, 5, 2.5, 2.5, 2.5, 5, 10, 2.5, 10, 5, 2.5, 2.5, 2.5, 2.5, 7.5, 5, 2.5, 2.5, 7.5, 5, 10, 10, 2.5, 5, 7.5, 7.5, 5, 5, 2.5, 5]



# --- Initialize components for Routine "instructions_occupation" ---
instructions = visual.TextStim(win=win, name='instructions',
    text='Nu är det dags för yrken',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "Recall_info" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from code_5
name_occupation = "namn"
occupation = False
fingers = visual.TextStim(win=win, name='fingers',
    text=None,
    font='Open Sans',
    pos=(0, -0.25), height=0.045, wrapWidth=600.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "Recall_trial" ---
# Run 'Begin Experiment' code from code_2
face_count = 0

key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from duration_setter
#values = [2.5, 5, 7.5, 10]
#target_sum = 400
#num_values = 80

# Create an initial list with random values
#initial_list = np.random.choice(values, num_values)

# Calculate the sum of the initial list
#current_sum = sum(initial_list)

# Calculate the difference between the target sum and current sum
#diff = target_sum - current_sum

# Randomly adjust values in the list until the sum matches the target sum
#while diff != 0:
    # Choose a random index in the list
#    index = np.random.randint(0, num_values - 1)
    # Choose a random value from the options
#    new_value = np.random.choice(values)

    # Update the list at the chosen index with the new value
#    initial_list[index] = new_value

    # Update the current sum and difference
#    current_sum = sum(initial_list)
#    diff = target_sum - current_sum

ITI_durations = values = [7.5, 5, 5, 7.5, 2.5, 5, 2.5, 5, 5, 5, 2.5, 7.5, 2.5, 2.5, 5, 5, 5, 7.5, 7.5, 5, 2.5, 5, 10, 7.5, 2.5, 2.5, 2.5, 7.5, 2.5, 2.5, 7.5, 5, 7.5, 2.5, 5, 7.5, 2.5, 5, 10, 5, 5, 7.5, 2.5, 2.5, 5, 10, 2.5, 2.5, 2.5, 10, 2.5, 5, 2.5, 2.5, 2.5, 5, 10, 2.5, 10, 5, 2.5, 2.5, 2.5, 2.5, 7.5, 5, 2.5, 2.5, 7.5, 5, 10, 10, 2.5, 5, 7.5, 7.5, 5, 5, 2.5, 5]



# --- Initialize components for Routine "fix_cross" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "ITI" ---
blank_screen = visual.TextStim(win=win, name='blank_screen',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
# Run 'Begin Experiment' code from duration_setter
#values = [2.5, 5, 7.5, 10]
#target_sum = 400
#num_values = 80

# Create an initial list with random values
#initial_list = np.random.choice(values, num_values)

# Calculate the sum of the initial list
#current_sum = sum(initial_list)

# Calculate the difference between the target sum and current sum
#diff = target_sum - current_sum

# Randomly adjust values in the list until the sum matches the target sum
#while diff != 0:
    # Choose a random index in the list
#    index = np.random.randint(0, num_values - 1)
    # Choose a random value from the options
#    new_value = np.random.choice(values)

    # Update the list at the chosen index with the new value
#    initial_list[index] = new_value

    # Update the current sum and difference
#    current_sum = sum(initial_list)
#    diff = target_sum - current_sum

ITI_durations = values = [7.5, 5, 5, 7.5, 2.5, 5, 2.5, 5, 5, 5, 2.5, 7.5, 2.5, 2.5, 5, 5, 5, 7.5, 7.5, 5, 2.5, 5, 10, 7.5, 2.5, 2.5, 2.5, 7.5, 2.5, 2.5, 7.5, 5, 7.5, 2.5, 5, 7.5, 2.5, 5, 10, 5, 5, 7.5, 2.5, 2.5, 5, 10, 2.5, 2.5, 2.5, 10, 2.5, 5, 2.5, 2.5, 2.5, 5, 10, 2.5, 10, 5, 2.5, 2.5, 2.5, 2.5, 7.5, 5, 2.5, 2.5, 7.5, 5, 10, 10, 2.5, 5, 7.5, 7.5, 5, 5, 2.5, 5]



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

# --- Prepare to start Routine "Wait_fMRI" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Wait_fMRIComponents = [key_resp, text_3]
for thisComponent in Wait_fMRIComponents:
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

# --- Run Routine "Wait_fMRI" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
    # Run 'Each Frame' code from code_4
    if (key_resp.keys) == 's':
        expStart = timer.getTime()
        core.wait(5)
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
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_fMRIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Wait_fMRI" ---
for thisComponent in Wait_fMRIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Wait_fMRI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Recall_info" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_5

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
frameN = -1

# --- Run Routine "Recall_info" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.stopped')
            text_6.setAutoDraw(False)
    
    # *fingers* updates
    if fingers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fingers.frameNStart = frameN  # exact frame index
        fingers.tStart = t  # local t and not account for scr refresh
        fingers.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fingers, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fingers.started')
        fingers.setAutoDraw(True)
    if fingers.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fingers.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            fingers.tStop = t  # not accounting for scr refresh
            fingers.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fingers.stopped')
            fingers.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Recall_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Recall_info" ---
for thisComponent in Recall_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# set up handler to look after randomisation of conditions etc
Names = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Recall_names.xlsx', selection=images_selection),
    seed=None, name='Names')
thisExp.addLoop(Names)  # add the loop to the experiment
thisName = Names.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisName.rgb)
if thisName != None:
    for paramName in thisName:
        exec('{} = thisName[paramName]'.format(paramName))

for thisName in Names:
    currentLoop = Names
    # abbreviate parameter names if possible (e.g. rgb = thisName.rgb)
    if thisName != None:
        for paramName in thisName:
            exec('{} = thisName[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Recall_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    
    
    
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVÖ'
    
    
    if occupation:
        correct = Profession[0]
        conditin_file = "Recall_professions.xlsx"
    else:
        correct = Name[0]
        
    
        
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
    
    if Name == "NY" or Profession == "NY":
        correct_answer = 4
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
    frameN = -1
    
    # --- Run Routine "Recall_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1.stopped')
                key_resp_1.status = FINISHED
        if key_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1.getKeys(keyList=['1','2','3','4'], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # *letters_text* updates
        if letters_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letters_text.frameNStart = frameN  # exact frame index
            letters_text.tStart = t  # local t and not account for scr refresh
            letters_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letters_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letters_text.started')
            letters_text.setAutoDraw(True)
        if letters_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letters_text.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                letters_text.tStop = t  # not accounting for scr refresh
                letters_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'letters_text.stopped')
                letters_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recall_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall_trial" ---
    for thisComponent in Recall_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    print(letters)
    print(correct_answer)
    
    if occupation:
        Professions.addData("correct", correct_answer)
    else:
        Names.addData("correct", correct_answer)
    
    # check responses
    if key_resp_1.keys in ['', [], None]:  # No response was made
        key_resp_1.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp_1.corr = 1;  # correct non-response
        else:
           key_resp_1.corr = 0;  # failed to respond (incorrectly)
    # store data for Names (TrialHandler)
    Names.addData('key_resp_1.keys',key_resp_1.keys)
    Names.addData('key_resp_1.corr', key_resp_1.corr)
    if key_resp_1.keys != None:  # we had a response
        Names.addData('key_resp_1.rt', key_resp_1.rt)
    # the Routine "Recall_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from duration_setter
    
    
    ITI_duration = np.random.choice(ITI_durations)
    
    ITI_index = np.where(ITI_durations==ITI_duration)[0][0]
    
    # Update the list by removing the extracted numbers
    ITI_durations = np.delete(ITI_durations, ITI_index)
    
    
    print(ITI_duration)
    
    print(f"Updated ITI duration list length: {len(ITI_durations)}")
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
    
    # --- Prepare to start Routine "fix_cross" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "fix_cross" ---
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
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix_cross" ---
    for thisComponent in fix_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from save_cross_onset
    thisExp.addData('fix_cross Start', polygon.tStart)
    # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from duration_setter
    
    
    ITI_duration = np.random.choice(ITI_durations)
    
    ITI_index = np.where(ITI_durations==ITI_duration)[0][0]
    
    # Update the list by removing the extracted numbers
    ITI_durations = np.delete(ITI_durations, ITI_index)
    
    
    print(ITI_duration)
    
    print(f"Updated ITI duration list length: {len(ITI_durations)}")
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
    
# completed 1.0 repeats of 'Names'

# get names of stimulus parameters
if Names.trialList in ([], [None], None):
    params = []
else:
    params = Names.trialList[0].keys()
# save data for this loop
Names.saveAsExcel(filename + '.xlsx', sheetName='Names',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "instructions_occupation" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_6
occupation = True
ITI_index = 0
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
frameN = -1

# --- Run Routine "instructions_occupation" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions.started')
        instructions.setAutoDraw(True)
    if instructions.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            instructions.tStop = t  # not accounting for scr refresh
            instructions.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions.stopped')
            instructions.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_occupationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_occupation" ---
for thisComponent in instructions_occupationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- Prepare to start Routine "Recall_info" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_5

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
frameN = -1

# --- Run Routine "Recall_info" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.stopped')
            text_6.setAutoDraw(False)
    
    # *fingers* updates
    if fingers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fingers.frameNStart = frameN  # exact frame index
        fingers.tStart = t  # local t and not account for scr refresh
        fingers.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fingers, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fingers.started')
        fingers.setAutoDraw(True)
    if fingers.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fingers.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            fingers.tStop = t  # not accounting for scr refresh
            fingers.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fingers.stopped')
            fingers.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Recall_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Recall_info" ---
for thisComponent in Recall_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# set up handler to look after randomisation of conditions etc
Professions = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Recall_professions.xlsx', selection=images_selection),
    seed=None, name='Professions')
thisExp.addLoop(Professions)  # add the loop to the experiment
thisProfession = Professions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisProfession.rgb)
if thisProfession != None:
    for paramName in thisProfession:
        exec('{} = thisProfession[paramName]'.format(paramName))

for thisProfession in Professions:
    currentLoop = Professions
    # abbreviate parameter names if possible (e.g. rgb = thisProfession.rgb)
    if thisProfession != None:
        for paramName in thisProfession:
            exec('{} = thisProfession[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Recall_trial" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    
    
    
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVÖ'
    
    
    if occupation:
        correct = Profession[0]
        conditin_file = "Recall_professions.xlsx"
    else:
        correct = Name[0]
        
    
        
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
    
    if Name == "NY" or Profession == "NY":
        correct_answer = 4
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
    frameN = -1
    
    # --- Run Routine "Recall_trial" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_1.started')
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_1.stopped')
                key_resp_1.status = FINISHED
        if key_resp_1.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_1.getKeys(keyList=['1','2','3','4'], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                image.setAutoDraw(False)
        
        # *letters_text* updates
        if letters_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            letters_text.frameNStart = frameN  # exact frame index
            letters_text.tStart = t  # local t and not account for scr refresh
            letters_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(letters_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'letters_text.started')
            letters_text.setAutoDraw(True)
        if letters_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > letters_text.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                letters_text.tStop = t  # not accounting for scr refresh
                letters_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'letters_text.stopped')
                letters_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Recall_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Recall_trial" ---
    for thisComponent in Recall_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_2
    print(letters)
    print(correct_answer)
    
    if occupation:
        Professions.addData("correct", correct_answer)
    else:
        Names.addData("correct", correct_answer)
    
    # check responses
    if key_resp_1.keys in ['', [], None]:  # No response was made
        key_resp_1.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp_1.corr = 1;  # correct non-response
        else:
           key_resp_1.corr = 0;  # failed to respond (incorrectly)
    # store data for Professions (TrialHandler)
    Professions.addData('key_resp_1.keys',key_resp_1.keys)
    Professions.addData('key_resp_1.corr', key_resp_1.corr)
    if key_resp_1.keys != None:  # we had a response
        Professions.addData('key_resp_1.rt', key_resp_1.rt)
    # the Routine "Recall_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from duration_setter
    
    
    ITI_duration = np.random.choice(ITI_durations)
    
    ITI_index = np.where(ITI_durations==ITI_duration)[0][0]
    
    # Update the list by removing the extracted numbers
    ITI_durations = np.delete(ITI_durations, ITI_index)
    
    
    print(ITI_duration)
    
    print(f"Updated ITI duration list length: {len(ITI_durations)}")
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
    
    # --- Prepare to start Routine "fix_cross" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "fix_cross" ---
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
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + image_duration-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix_cross" ---
    for thisComponent in fix_crossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from save_cross_onset
    thisExp.addData('fix_cross Start', polygon.tStart)
    # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "ITI" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from duration_setter
    
    
    ITI_duration = np.random.choice(ITI_durations)
    
    ITI_index = np.where(ITI_durations==ITI_duration)[0][0]
    
    # Update the list by removing the extracted numbers
    ITI_durations = np.delete(ITI_durations, ITI_index)
    
    
    print(ITI_duration)
    
    print(f"Updated ITI duration list length: {len(ITI_durations)}")
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
    
# completed 1.0 repeats of 'Professions'

# get names of stimulus parameters
if Professions.trialList in ([], [None], None):
    params = []
else:
    params = Professions.trialList[0].keys()
# save data for this loop
Professions.saveAsExcel(filename + '.xlsx', sheetName='Professions',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

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
while continueRoutine and routineTimer.getTime() < 6.0:
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
        if tThisFlipGlobal > text_2.tStartRefresh + 6-frameTolerance:
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
    routineTimer.addTime(-6.000000)
# Run 'End Experiment' code from code_4
stopTime = timer.getTime() - expStart


print(f"The Experimetn lasted for {stopTime} seconds")

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
