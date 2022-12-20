/********************* 
 * Gallery_Fmri Test *
 *********************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Gallery_fMRI';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('0.0000, 0.0000, 0.0000'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructionsRoutineBegin());
flowScheduler.add(InstructionsRoutineEachFrame());
flowScheduler.add(InstructionsRoutineEnd());
const Randomization_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Randomization_loopLoopBegin(Randomization_loopLoopScheduler));
flowScheduler.add(Randomization_loopLoopScheduler);
flowScheduler.add(Randomization_loopLoopEnd);
const trials_1LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_1LoopBegin(trials_1LoopScheduler));
flowScheduler.add(trials_1LoopScheduler);
flowScheduler.add(trials_1LoopEnd);
flowScheduler.add(FinishedRoutineBegin());
flowScheduler.add(FinishedRoutineEachFrame());
flowScheduler.add(FinishedRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'bookcase.jpg', 'path': 'bookcase.jpg'},
    {'name': 'armadillo.jpg', 'path': 'armadillo.jpg'},
    {'name': 'paragliding.jpg', 'path': 'paragliding.jpg'},
    {'name': 'tiger.jpg', 'path': 'tiger.jpg'},
    {'name': 'snake.jpg', 'path': 'snake.jpg'},
    {'name': 'van.jpg', 'path': 'van.jpg'},
    {'name': 'sofa.jpg', 'path': 'sofa.jpg'},
    {'name': 'bedside_table.jpg', 'path': 'bedside_table.jpg'},
    {'name': 'stool.jpg', 'path': 'stool.jpg'},
    {'name': 'tractor.jpg', 'path': 'tractor.jpg'},
    {'name': 'motorbike.jpg', 'path': 'motorbike.jpg'},
    {'name': 'cart.jpg', 'path': 'cart.jpg'},
    {'name': 'platypus.jpg', 'path': 'platypus.jpg'},
    {'name': 'OneShotLearning.xlsx', 'path': 'OneShotLearning.xlsx'},
    {'name': 'Chest_of_drawers.jpg', 'path': 'Chest_of_drawers.jpg'},
    {'name': 'chair.jpg', 'path': 'chair.jpg'},
    {'name': 'lectern.jpg', 'path': 'lectern.jpg'},
    {'name': 'hippopotamus.jpg', 'path': 'hippopotamus.jpg'},
    {'name': 'kangaroo.jpg', 'path': 'kangaroo.jpg'},
    {'name': 'ArrowRight.png', 'path': 'ArrowRight.png'},
    {'name': 'cat.jpg', 'path': 'cat.jpg'},
    {'name': 'filling_cabinet.jpg', 'path': 'filling_cabinet.jpg'},
    {'name': 'car.jpg', 'path': 'car.jpg'},
    {'name': 'table.jpg', 'path': 'table.jpg'},
    {'name': 'lamp.jpg', 'path': 'lamp.jpg'},
    {'name': 'tapir.jpg', 'path': 'tapir.jpg'},
    {'name': 'Gallery_arrowoptions.png', 'path': 'Gallery_arrowoptions.png'},
    {'name': 'turtle.jpg', 'path': 'turtle.jpg'},
    {'name': 'skateboard.jpg', 'path': 'skateboard.jpg'},
    {'name': 'armchair.jpg', 'path': 'armchair.jpg'},
    {'name': 'rocking_chair.jpg', 'path': 'rocking_chair.jpg'},
    {'name': 'boat.jpg', 'path': 'boat.jpg'},
    {'name': 'giraffe.jpg', 'path': 'giraffe.jpg'},
    {'name': 'elephant.jpg', 'path': 'elephant.jpg'},
    {'name': 'bus.jpg', 'path': 'bus.jpg'},
    {'name': 'bat.jpg', 'path': 'bat.jpg'},
    {'name': 'cow.jpg', 'path': 'cow.jpg'},
    {'name': 'zebra.jpg', 'path': 'zebra.jpg'},
    {'name': 'OneShotLearning_conditions.xlsx', 'path': 'OneShotLearning_conditions.xlsx'},
    {'name': 'rhino.jpg', 'path': 'rhino.jpg'},
    {'name': 'dromedary.jpg', 'path': 'dromedary.jpg'},
    {'name': 'ArrowLeft.png', 'path': 'ArrowLeft.png'},
    {'name': 'lynx.jpg', 'path': 'lynx.jpg'},
    {'name': 'plane.jpg', 'path': 'plane.jpg'},
    {'name': 'couch.jpg', 'path': 'couch.jpg'},
    {'name': 'lioness.jpg', 'path': 'lioness.jpg'},
    {'name': 'ship.jpg', 'path': 'ship.jpg'},
    {'name': 'ArrowUp.png', 'path': 'ArrowUp.png'},
    {'name': 'horse.jpg', 'path': 'horse.jpg'},
    {'name': 'bed.jpg', 'path': 'bed.jpg'},
    {'name': 'cheetah.jpg', 'path': 'cheetah.jpg'},
    {'name': 'scooter.jpg', 'path': 'scooter.jpg'},
    {'name': 'crocodile.jpg', 'path': 'crocodile.jpg'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var InstructionsClock;
var text;
var key_resp_0;
var RandomizationClock;
var listA;
var trialClock;
var key_resp_1;
var image;
var Arrow;
var total_corr;
var total_all;
var rt;
var fix_crossClock;
var polygon;
var Uncued_trialClock;
var key_resp_2;
var image_2;
var direction_options;
var FinishedClock;
var text_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instructions"
  InstructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Instructions:\n\nYou will see images presented one at a time above an arrow pointing either left, up or right.\nYour task is to memorize the image together with the direction of the arrow. \n\nRespond to each image and arrow using the following buttons:\n1 (index finger) = Left\n2 (middle finger) = Up\n3 (ring finger) = Right\n\nThe second time you see each image there will not be one arrow but three highlighted in orange indicating that you may choose the direction you recall was previously presented below the current image.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([1, 1, 1]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_0 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Randomization"
  RandomizationClock = new util.Clock();
  listA = [];
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.125)], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  Arrow = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Arrow', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.375], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  total_corr = 0;
  total_all = 0;
  rt = 0;
  
  // Initialize components for Routine "fix_cross"
  fix_crossClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.5, 0.5],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Uncued_trial"
  Uncued_trialClock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.125], size : [1, 0.75],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  direction_options = new visual.ImageStim({
    win : psychoJS.window,
    name : 'direction_options', units : undefined, 
    image : 'Gallery_arrowoptions.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.375)], size : [1, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "Finished"
  FinishedClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Well done!\n\nYou have finished the task.\nRemain still and await further \ninstructions by the experiment leader.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_0_allKeys;
var InstructionsComponents;
function InstructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instructions'-------
    t = 0;
    InstructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_0.keys = undefined;
    key_resp_0.rt = undefined;
    _key_resp_0_allKeys = [];
    // keep track of which components have finished
    InstructionsComponents = [];
    InstructionsComponents.push(text);
    InstructionsComponents.push(key_resp_0);
    
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructionsRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instructions'-------
    // get current time
    t = InstructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp_0* updates
    if (t >= 0.0 && key_resp_0.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_0.tStart = t;  // (not accounting for frame time here)
      key_resp_0.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_0.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_0.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_0.clearEvents(); });
    }

    if (key_resp_0.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_0.getKeys({keyList: ['1', '2', '3', 'space'], waitRelease: false});
      _key_resp_0_allKeys = _key_resp_0_allKeys.concat(theseKeys);
      if (_key_resp_0_allKeys.length > 0) {
        key_resp_0.keys = _key_resp_0_allKeys[_key_resp_0_allKeys.length - 1].name;  // just the last key pressed
        key_resp_0.rt = _key_resp_0_allKeys[_key_resp_0_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructionsRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instructions'-------
    for (const thisComponent of InstructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_0.keys', key_resp_0.keys);
    if (typeof key_resp_0.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_0.rt', key_resp_0.rt);
        routineTimer.reset();
        }
    
    key_resp_0.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Randomization_loop;
var currentLoop;
function Randomization_loopLoopBegin(Randomization_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Randomization_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'OneShotLearning.xlsx',
      seed: undefined, name: 'Randomization_loop'
    });
    psychoJS.experiment.addLoop(Randomization_loop); // add the loop to the experiment
    currentLoop = Randomization_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRandomization_loop of Randomization_loop) {
      const snapshot = Randomization_loop.getSnapshot();
      Randomization_loopLoopScheduler.add(importConditions(snapshot));
      Randomization_loopLoopScheduler.add(RandomizationRoutineBegin(snapshot));
      Randomization_loopLoopScheduler.add(RandomizationRoutineEachFrame());
      Randomization_loopLoopScheduler.add(RandomizationRoutineEnd());
      Randomization_loopLoopScheduler.add(endLoopIteration(Randomization_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function Randomization_loopLoopEnd() {
  psychoJS.experiment.removeLoop(Randomization_loop);

  return Scheduler.Event.NEXT;
}


var trials_1;
function trials_1LoopBegin(trials_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'OneShotLearning_conditions.xlsx',
      seed: undefined, name: 'trials_1'
    });
    psychoJS.experiment.addLoop(trials_1); // add the loop to the experiment
    currentLoop = trials_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_1 of trials_1) {
      const snapshot = trials_1.getSnapshot();
      trials_1LoopScheduler.add(importConditions(snapshot));
      const CuedLoopScheduler = new Scheduler(psychoJS);
      trials_1LoopScheduler.add(CuedLoopBegin(CuedLoopScheduler, snapshot));
      trials_1LoopScheduler.add(CuedLoopScheduler);
      trials_1LoopScheduler.add(CuedLoopEnd);
      const UncuedLoopScheduler = new Scheduler(psychoJS);
      trials_1LoopScheduler.add(UncuedLoopBegin(UncuedLoopScheduler, snapshot));
      trials_1LoopScheduler.add(UncuedLoopScheduler);
      trials_1LoopScheduler.add(UncuedLoopEnd);
      trials_1LoopScheduler.add(endLoopIteration(trials_1LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var Cued;
function CuedLoopBegin(CuedLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Cued = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'OneShotLearning.xlsx', Condition_rows),
      seed: undefined, name: 'Cued'
    });
    psychoJS.experiment.addLoop(Cued); // add the loop to the experiment
    currentLoop = Cued;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCued of Cued) {
      const snapshot = Cued.getSnapshot();
      CuedLoopScheduler.add(importConditions(snapshot));
      CuedLoopScheduler.add(trialRoutineBegin(snapshot));
      CuedLoopScheduler.add(trialRoutineEachFrame());
      CuedLoopScheduler.add(trialRoutineEnd());
      CuedLoopScheduler.add(fix_crossRoutineBegin(snapshot));
      CuedLoopScheduler.add(fix_crossRoutineEachFrame());
      CuedLoopScheduler.add(fix_crossRoutineEnd());
      CuedLoopScheduler.add(endLoopIteration(CuedLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function CuedLoopEnd() {
  psychoJS.experiment.removeLoop(Cued);

  return Scheduler.Event.NEXT;
}


var Uncued;
function UncuedLoopBegin(UncuedLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Uncued = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'OneShotLearning.xlsx', Condition_rows),
      seed: undefined, name: 'Uncued'
    });
    psychoJS.experiment.addLoop(Uncued); // add the loop to the experiment
    currentLoop = Uncued;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisUncued of Uncued) {
      const snapshot = Uncued.getSnapshot();
      UncuedLoopScheduler.add(importConditions(snapshot));
      UncuedLoopScheduler.add(Uncued_trialRoutineBegin(snapshot));
      UncuedLoopScheduler.add(Uncued_trialRoutineEachFrame());
      UncuedLoopScheduler.add(Uncued_trialRoutineEnd());
      UncuedLoopScheduler.add(fix_crossRoutineBegin(snapshot));
      UncuedLoopScheduler.add(fix_crossRoutineEachFrame());
      UncuedLoopScheduler.add(fix_crossRoutineEnd());
      UncuedLoopScheduler.add(endLoopIteration(UncuedLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function UncuedLoopEnd() {
  psychoJS.experiment.removeLoop(Uncued);

  return Scheduler.Event.NEXT;
}


async function trials_1LoopEnd() {
  psychoJS.experiment.removeLoop(trials_1);

  return Scheduler.Event.NEXT;
}


var RandomizationComponents;
function RandomizationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Randomization'-------
    t = 0;
    RandomizationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    listA.push(StimFile);
    console.log(listA);
    
    // keep track of which components have finished
    RandomizationComponents = [];
    
    for (const thisComponent of RandomizationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RandomizationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Randomization'-------
    // get current time
    t = RandomizationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RandomizationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RandomizationRoutineEnd() {
  return async function () {
    //------Ending Routine 'Randomization'-------
    for (const thisComponent of RandomizationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Randomization" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_1_allKeys;
var thisA;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    key_resp_1.keys = undefined;
    key_resp_1.rt = undefined;
    _key_resp_1_allKeys = [];
    image.setImage(StimFile);
    Arrow.setImage(ArrowImg);
    thisA = listA.pop();
    if (key_resp_1.corr) {
        total_corr = (total_corr + 1);
        total_all = (total_all + 1);
        rt = key_resp_1.rt;
    } else {
        total_all = (total_all + 1);
        rt = key_resp_1.rt;
    }
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(key_resp_1);
    trialComponents.push(image);
    trialComponents.push(Arrow);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_1* updates
    if (t >= 0 && key_resp_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_1.tStart = t;  // (not accounting for frame time here)
      key_resp_1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_1.clearEvents(); });
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_1.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_1.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_1.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _key_resp_1_allKeys = _key_resp_1_allKeys.concat(theseKeys);
      if (_key_resp_1_allKeys.length > 0) {
        key_resp_1.keys = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].name;  // just the last key pressed
        key_resp_1.rt = _key_resp_1_allKeys[_key_resp_1_allKeys.length - 1].rt;
      }
    }
    
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *Arrow* updates
    if (t >= 0.0 && Arrow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Arrow.tStart = t;  // (not accounting for frame time here)
      Arrow.frameNStart = frameN;  // exact frame index
      
      Arrow.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Arrow.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Arrow.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_1.keys', key_resp_1.keys);
    if (typeof key_resp_1.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_1.rt', key_resp_1.rt);
        }
    
    key_resp_1.stop();
    return Scheduler.Event.NEXT;
  };
}


var fix_crossComponents;
function fix_crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'fix_cross'-------
    t = 0;
    fix_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_crossComponents = [];
    fix_crossComponents.push(polygon);
    
    for (const thisComponent of fix_crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function fix_crossRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'fix_cross'-------
    // get current time
    t = fix_crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of fix_crossComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_crossRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross'-------
    for (const thisComponent of fix_crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var Uncued_trialComponents;
function Uncued_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Uncued_trial'-------
    t = 0;
    Uncued_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    image_2.setImage(StimFile);
    if (key_resp_2.corr) {
        total_corr = (total_corr + 1);
        total_all = (total_all + 1);
        rt = key_resp_2.rt;
    } else {
        total_all = (total_all + 1);
        rt = key_resp_2.rt;
    }
    
    // keep track of which components have finished
    Uncued_trialComponents = [];
    Uncued_trialComponents.push(key_resp_2);
    Uncued_trialComponents.push(image_2);
    Uncued_trialComponents.push(direction_options);
    
    for (const thisComponent of Uncued_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Uncued_trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Uncued_trial'-------
    // get current time
    t = Uncued_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
      }
    }
    
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    
    // *direction_options* updates
    if (t >= 0.0 && direction_options.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      direction_options.tStart = t;  // (not accounting for frame time here)
      direction_options.frameNStart = frameN;  // exact frame index
      
      direction_options.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (direction_options.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      direction_options.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Uncued_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Uncued_trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'Uncued_trial'-------
    for (const thisComponent of Uncued_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        }
    
    key_resp_2.stop();
    return Scheduler.Event.NEXT;
  };
}


var FinishedComponents;
function FinishedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Finished'-------
    t = 0;
    FinishedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    FinishedComponents = [];
    FinishedComponents.push(text_2);
    
    for (const thisComponent of FinishedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FinishedRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Finished'-------
    // get current time
    t = FinishedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FinishedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinishedRoutineEnd() {
  return async function () {
    //------Ending Routine 'Finished'-------
    for (const thisComponent of FinishedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
