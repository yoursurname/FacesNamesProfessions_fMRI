/*************** 
 * Recall Test *
 ***************/


// store info about the experiment session:
let expName = 'Recall';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color('white'),
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
const Recall_NameLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Recall_NameLoopBegin(Recall_NameLoopScheduler));
flowScheduler.add(Recall_NameLoopScheduler);
flowScheduler.add(Recall_NameLoopEnd);
flowScheduler.add(fix_crossRoutineBegin());
flowScheduler.add(fix_crossRoutineEachFrame());
flowScheduler.add(fix_crossRoutineEnd());
const Recall_ProffessionLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Recall_ProffessionLoopBegin(Recall_ProffessionLoopScheduler));
flowScheduler.add(Recall_ProffessionLoopScheduler);
flowScheduler.add(Recall_ProffessionLoopEnd);
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
    {'name': 'Images_Faces/O20.jpg', 'path': 'Images_Faces/O20.jpg'},
    {'name': 'Images_Faces/SH12.png', 'path': 'Images_Faces/SH12.png'},
    {'name': 'Images_Faces/O30.jpg', 'path': 'Images_Faces/O30.jpg'},
    {'name': 'Images_Faces/O10.jpg', 'path': 'Images_Faces/O10.jpg'},
    {'name': 'Images_Faces/O12.jpg', 'path': 'Images_Faces/O12.jpg'},
    {'name': 'Images_Faces/O29.jpg', 'path': 'Images_Faces/O29.jpg'},
    {'name': 'Images_Faces/O17.jpg', 'path': 'Images_Faces/O17.jpg'},
    {'name': 'Images_Faces/O22.jpg', 'path': 'Images_Faces/O22.jpg'},
    {'name': 'Images_Faces/SH8.png', 'path': 'Images_Faces/SH8.png'},
    {'name': 'Images_Faces/SH15.png', 'path': 'Images_Faces/SH15.png'},
    {'name': 'Images_Faces/O18.jpg', 'path': 'Images_Faces/O18.jpg'},
    {'name': 'Images_Faces/O27.jpg', 'path': 'Images_Faces/O27.jpg'},
    {'name': 'Images_Faces/SH29.png', 'path': 'Images_Faces/SH29.png'},
    {'name': 'Images_Faces/O19.jpg', 'path': 'Images_Faces/O19.jpg'},
    {'name': 'Images_Faces/O21.jpg', 'path': 'Images_Faces/O21.jpg'},
    {'name': 'Images_Faces/SH25.png', 'path': 'Images_Faces/SH25.png'},
    {'name': 'Images_Faces/SH3.png', 'path': 'Images_Faces/SH3.png'},
    {'name': 'Images_Faces/SH6.png', 'path': 'Images_Faces/SH6.png'},
    {'name': 'Images_Faces/SH27.png', 'path': 'Images_Faces/SH27.png'},
    {'name': 'Images_Faces/O5.jpg', 'path': 'Images_Faces/O5.jpg'},
    {'name': 'Images_Faces/O3.jpg', 'path': 'Images_Faces/O3.jpg'},
    {'name': 'Images_Faces/O26.jpg', 'path': 'Images_Faces/O26.jpg'},
    {'name': 'Images_Faces/SH23.png', 'path': 'Images_Faces/SH23.png'},
    {'name': 'Images_Faces/SH24.png', 'path': 'Images_Faces/SH24.png'},
    {'name': 'Images_Faces/SH5.png', 'path': 'Images_Faces/SH5.png'},
    {'name': 'Images_Faces/SH9.png', 'path': 'Images_Faces/SH9.png'},
    {'name': 'Images_Faces/O23.jpg', 'path': 'Images_Faces/O23.jpg'},
    {'name': 'Images_Faces/SH7.png', 'path': 'Images_Faces/SH7.png'},
    {'name': 'Images_Faces/SH21.png', 'path': 'Images_Faces/SH21.png'},
    {'name': 'Images_Faces/SH2.png', 'path': 'Images_Faces/SH2.png'},
    {'name': 'Images_Faces/SH22.png', 'path': 'Images_Faces/SH22.png'},
    {'name': 'Images_Faces/O9.jpg', 'path': 'Images_Faces/O9.jpg'},
    {'name': 'Images_Faces/O4.jpg', 'path': 'Images_Faces/O4.jpg'},
    {'name': 'Images_Faces/O28.jpg', 'path': 'Images_Faces/O28.jpg'},
    {'name': 'Images_Faces/O6.jpg', 'path': 'Images_Faces/O6.jpg'},
    {'name': 'Images_Faces/O14.jpg', 'path': 'Images_Faces/O14.jpg'},
    {'name': 'Images_Faces/O8.jpg', 'path': 'Images_Faces/O8.jpg'},
    {'name': 'Images_Faces/O15.jpg', 'path': 'Images_Faces/O15.jpg'},
    {'name': 'Images_Faces/O16.jpg', 'path': 'Images_Faces/O16.jpg'},
    {'name': 'Images_Faces/SH28.png', 'path': 'Images_Faces/SH28.png'},
    {'name': 'Images_Faces/SH10.png', 'path': 'Images_Faces/SH10.png'},
    {'name': 'Images_Faces/SH1.png', 'path': 'Images_Faces/SH1.png'},
    {'name': 'Images_Faces/O13.jpg', 'path': 'Images_Faces/O13.jpg'},
    {'name': 'Images_Faces/O7.jpg', 'path': 'Images_Faces/O7.jpg'},
    {'name': 'Images_Faces/SH17.png', 'path': 'Images_Faces/SH17.png'},
    {'name': 'Images_Faces/O24.jpg', 'path': 'Images_Faces/O24.jpg'},
    {'name': 'Images_Faces/O25.jpg', 'path': 'Images_Faces/O25.jpg'},
    {'name': 'Images_Faces/O2.jpg', 'path': 'Images_Faces/O2.jpg'},
    {'name': 'Images_Faces/SH30.png', 'path': 'Images_Faces/SH30.png'},
    {'name': 'Images_Faces/SH20.png', 'path': 'Images_Faces/SH20.png'},
    {'name': 'Images_Faces/SH14.png', 'path': 'Images_Faces/SH14.png'},
    {'name': 'Images_Faces/O1.jpg', 'path': 'Images_Faces/O1.jpg'},
    {'name': 'Images_Faces/SH19.png', 'path': 'Images_Faces/SH19.png'},
    {'name': 'Images_Faces/SH13.png', 'path': 'Images_Faces/SH13.png'},
    {'name': 'Images_Faces/SH4.png', 'path': 'Images_Faces/SH4.png'},
    {'name': 'Images_Faces/SH18.png', 'path': 'Images_Faces/SH18.png'},
    {'name': 'Images_Faces/O11.jpg', 'path': 'Images_Faces/O11.jpg'},
    {'name': 'Images_Faces/SH26.png', 'path': 'Images_Faces/SH26.png'},
    {'name': 'Images_Faces/SH16.png', 'path': 'Images_Faces/SH16.png'},
    {'name': 'Recall.xlsx', 'path': 'Recall.xlsx'},
    {'name': 'Images_Faces/SH11.png', 'path': 'Images_Faces/SH11.png'}
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
var trialClock;
var key_resp_1;
var image;
var text_4;
var jitter;
var fix_crossClock;
var polygon;
var CircleClock;
var polygon_3;
var key_resp_3;
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
    text: 'Instruktioner:\n\nDu kommer att se bilder presenterade en i taget.\nDin uppgift är att avgöra om det är första gången du ser bilden (New) eller om du har sett bilden tidigare (Old).\n\nSvara på varje bild med hjälp av följande knappar:\n1 (pekfinger) = New\n2 (långfinger) = Old\n\nVid senare tillfälle under uppgiftens gång kommer du att se bilder presenterade en i taget ovanför tre pilar markerade i orange som pekar åt vänster, uppåt och höger.\nDin uppgift är att välja den riktning som du minns tidigare har presenterats under den aktuella bilden.\n\nSvara på varje bild och pil med hjälp av följande knappar:\n1 (pekfinger) = Vänster\n2 (långfinger) = Upp\n3 (ringfinger) = Höger\n\nI början och i mitten av uppgiften kommer du att se brusiga bilder.\nTitta bara på de brusiga bilderna utan att trycka på någon knapp.\n\nTryck med pekfingret och meddela när du är redo att börja.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_0 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  key_resp_1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.125], size : [0.743, 0.75],
    color : new util.Color('white'), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.375)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  jitter = np.arange(2.5, 10, 0.25);
  util.shuffle(jitter);
  
  // Initialize components for Routine "fix_cross"
  fix_crossClock = new util.Clock();
  polygon = new visual.ShapeStim ({
    win: psychoJS.window, name: 'polygon', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 0.1, lineColor: new util.Color(undefined),
    fillColor: new util.Color('black'),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "Circle"
  CircleClock = new util.Clock();
  polygon_3 = new visual.Polygon ({
    win: psychoJS.window, name: 'polygon_3', 
    edges: 4, size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('black'),
    fillColor: new util.Color(undefined),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Finished"
  FinishedClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Bra jobbat!\n\nDu har slutfört uppgiften. \nFortsätt ligga stilla så kommer vi prata med dig alldeles strax.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
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
    
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    InstructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    InstructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_0.stop();
    // the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Recall_Name;
var currentLoop;
function Recall_NameLoopBegin(Recall_NameLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Recall_Name = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Recall.xlsx', '0:30'),
      seed: undefined, name: 'Recall_Name'
    });
    psychoJS.experiment.addLoop(Recall_Name); // add the loop to the experiment
    currentLoop = Recall_Name;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Recall_Name.forEach(function() {
      const snapshot = Recall_Name.getSnapshot();
    
      Recall_NameLoopScheduler.add(importConditions(snapshot));
      Recall_NameLoopScheduler.add(trialRoutineBegin(snapshot));
      Recall_NameLoopScheduler.add(trialRoutineEachFrame());
      Recall_NameLoopScheduler.add(trialRoutineEnd());
      Recall_NameLoopScheduler.add(fix_crossRoutineBegin(snapshot));
      Recall_NameLoopScheduler.add(fix_crossRoutineEachFrame());
      Recall_NameLoopScheduler.add(fix_crossRoutineEnd());
      Recall_NameLoopScheduler.add(CircleRoutineBegin(snapshot));
      Recall_NameLoopScheduler.add(CircleRoutineEachFrame());
      Recall_NameLoopScheduler.add(CircleRoutineEnd());
      Recall_NameLoopScheduler.add(endLoopIteration(Recall_NameLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Recall_NameLoopEnd() {
  psychoJS.experiment.removeLoop(Recall_Name);

  return Scheduler.Event.NEXT;
}


var Recall_Proffession;
function Recall_ProffessionLoopBegin(Recall_ProffessionLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Recall_Proffession = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Recall.xlsx', '30:60'),
      seed: undefined, name: 'Recall_Proffession'
    });
    psychoJS.experiment.addLoop(Recall_Proffession); // add the loop to the experiment
    currentLoop = Recall_Proffession;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    Recall_Proffession.forEach(function() {
      const snapshot = Recall_Proffession.getSnapshot();
    
      Recall_ProffessionLoopScheduler.add(importConditions(snapshot));
      Recall_ProffessionLoopScheduler.add(trialRoutineBegin(snapshot));
      Recall_ProffessionLoopScheduler.add(trialRoutineEachFrame());
      Recall_ProffessionLoopScheduler.add(trialRoutineEnd());
      Recall_ProffessionLoopScheduler.add(fix_crossRoutineBegin(snapshot));
      Recall_ProffessionLoopScheduler.add(fix_crossRoutineEachFrame());
      Recall_ProffessionLoopScheduler.add(fix_crossRoutineEnd());
      Recall_ProffessionLoopScheduler.add(CircleRoutineBegin(snapshot));
      Recall_ProffessionLoopScheduler.add(CircleRoutineEachFrame());
      Recall_ProffessionLoopScheduler.add(CircleRoutineEnd());
      Recall_ProffessionLoopScheduler.add(endLoopIteration(Recall_ProffessionLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function Recall_ProffessionLoopEnd() {
  psychoJS.experiment.removeLoop(Recall_Proffession);

  return Scheduler.Event.NEXT;
}


var _key_resp_1_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(4.000000);
    // update component parameters for each repeat
    key_resp_1.keys = undefined;
    key_resp_1.rt = undefined;
    _key_resp_1_allKeys = [];
    image.setImage(StimFile);
    text_4.setText(((((Letter1 + ("\t" * 6)) + Letter2) + ("\t" * 6)) + Letter3));
    jitter = np.arange(2.5, 10, 0.25);
    util.shuffle(jitter);
    psychoJS.experiment.addData("Jitter", jitter[0]);
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(key_resp_1);
    trialComponents.push(image);
    trialComponents.push(text_4);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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

    frameRemains = 0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
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
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    // update component parameters for each repeat
    // keep track of which components have finished
    fix_crossComponents = [];
    fix_crossComponents.push(polygon);
    
    fix_crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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

    frameRemains = 0.0 + jitter[0] - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
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
    fix_crossComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function fix_crossRoutineEnd() {
  return async function () {
    //------Ending Routine 'fix_cross'-------
    fix_crossComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var CircleComponents;
function CircleRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Circle'-------
    t = 0;
    CircleClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    CircleComponents = [];
    CircleComponents.push(polygon_3);
    CircleComponents.push(key_resp_3);
    
    CircleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function CircleRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Circle'-------
    // get current time
    t = CircleClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_3* updates
    if (t >= 0.0 && polygon_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_3.tStart = t;  // (not accounting for frame time here)
      polygon_3.frameNStart = frameN;  // exact frame index
      
      polygon_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (polygon_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_3.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
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
    CircleComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CircleRoutineEnd() {
  return async function () {
    //------Ending Routine 'Circle'-------
    CircleComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
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
    
    FinishedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    FinishedComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    FinishedComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
