# Control Link

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 379–388
> **Slug:** `15-control-link`

**Agent topics:** `Control Link`, `MIDI controllers`, `mapping`, `Mackie Control`, `hardware`

---

## Control Link

Studio One features Control Link, a cutting-edge system for integrating external hardware controllers with your virtual instruments,
effects, and other software parameters. The following chapter describes this system.

## What is Control Link?

In most DAW software, you can use external hardware devices to control software parameters. For instance, you could map several
knobs on a hardware MIDI controller to the software knobs of an EQ effect, so that when the hardware knobs are turned, the software
knobs are turned. However, in most cases the implementation is limited and difficult to learn.
Studio One improves on this model with the Control Link system, simplifying the control mapping process with no need for knowledge of
MIDI. Control Link is also capable of context-sensitive mapping, so the same hardware controls can control many different things based
on the current area of focus.
The following sections describe how to use the Control Link system.
Mackie Control/HUI Support
Studio One is optimized for use with Mackie Control and HUI-format devices, including Control Link Mapping and Send slot navigation,
with the ability to scroll through, and select from the lists of available plugins and instruments, and their presets. You can also control vari-
ous Channel and Track parameters such as Mute/Solo, and FX Bypass (EQ button). Further information can be found in the Mackie
Control section.
Set Up Your External Devices
To use any external hardware device with Studio One, the device must first be set up so that Studio One recognizes it. Once an external
device is set up, it is available for use in any Song. To set up an external hardware controller, refer to the information in the Set Up Your
MIDI Devices section of the Setup chapter.
Map Your Keyboard
For the Control Link system to work with your Keyboard, a software map must be made of the hardware controls you wish to use. This
simple process works as follows:
1.
Open the Mix view by pressing [F3] on the computer keyboard, and open the External panel by clicking on External in the Con-
sole Navigation column to the far left of the Console.
2.
Double-click on the desired device in the External panel to open the Device Control Map.
3.
In the upper left corner of the Device Control Map window, click on the [MIDI Learn] button to enter MIDI Learn mode.
4.
With MIDI Learn enabled, simply move any hardware control to map it. As controls are mapped, the default Knob object created
for that control is displayed, and it moves in correspondence with its related hardware control.
5.
When editing the control map for a Keyboard device (MIDI Learn enabled), you can select Transmit Value from the contextual
menu for each control. This option sends parameter updates for a given hardware control out of the Keyboard device's MIDI Out
port when the software parameter to which the control is linked changes. This makes it possible for user-created Keyboard
devices that have soft controls (endless rotary encoders with LED indicators, motorized faders, etc.) to reflect the correct current
state of any parameter that is being controlled. (This option is also available for Control Surfaces.)
6.
When you have mapped all of the desired controls, click on the [MIDI Learn] button to exit MIDI Learn mode.

## Control Link

Now that the hardware controls for your Keyboard have been mapped, they can be used to control almost any software parameter, as dis-
cussed in the Control Linking section.
Keyboard control maps are global in Studio One and are used across every Song, so you only need to map your Keyboard once.
When using predefined keyboard devices, it is not possible to map new controls for the device. You must follow the instructions in the
Add Device window (for example, select a certain preset).
Controller Map Object Types
The default Knob object is used when hardware controls are mapped for the first time. This object can be changed for each control to bet-
ter reflect the actual hardware control type, making your mapped controls much easier to recognize. To change the object for any
mapped control, do the following:
1.
Click on MIDI Learn to enter MIDI Learn mode.
2.
In MIDI Learn mode, you can see a description box beneath each control, with an arrow in the upper left corner.
3.
Click on the arrow to expose the Object Selection list, where you can choose a Knob, Fader, Button (On/Off), or Button
(Press/Release).
4.
Choose one of the object types and notice the graphic change for that control.
5.
When you are finished changing the control objects, click on the [MIDI Learn] button to exit MIDI Learn mode.
Note that there is a functional difference between the two button object types. Some hardware controllers send MIDI messages to Studio
One when a button is pressed or released, and some send messages when the button state is toggled between on and off. You must
know how the buttons on your controller behave in order to select the correct button-object type. Use the MIDI Monitor to view this beha-
vior directly.
Map Your Keyboard

To use the MIDI Monitor, choose MIDI Monitor from the View menu. Use the boxes in the MIDI Filter section to specify which incoming
MIDI messages you want to view. For example, to see which MIDI CC data is sent by the knobs on a MIDI controller, engage the
"Received" and "Controllers" boxes. Then activate the controls on the MIDI device to view their behavior so you can choose the correct
map-object type.
It is highly recommended that the control objects be made to look similar to the controls they represent, using the map-object types, as
this helps make the relationship of the software object to the related hardware control easier to recognize.
Control Linking
With a Keyboard set up, and its control map created, you are one click away from controlling almost any software parameter using Con-
trol Link. The following describes the various ways to use Control Link.
Parameter Windows
To the far left of the Arrange view toolbar in the Song window, you can see two windows separated by a button. The windows are empty
by default. The left window displays the name, value, and other related information regarding the last-changed software parameter; the
right window displays the MIDI name and value of the last-changed, mapped hardware control.
You also can open Parameter windows in each plug-in window. To do this, click on the Edit Mapping button at the top of the plug-in win-
dow.
Link a Hardware Control to a Software Control
The fastest way to link a hardware and software control is:
1.
Manipulate the desired software control with the mouse.
2.
Manipulate the desired hardware control; for instance, turn a knob. That control should appear in the right parameter window.
3.
Click on the Assign button in the middle of the two parameter windows, or press [Alt]/[Option]+[M] on the keyboard, and the but-
ton should light up.
Control Linking

4.
Your hardware control is now linked to the software control; manipulating the hardware control manipulates the linked software
control.
A second way to link hardware and software controls is:
1.
Open the control map for the desired controller by double-clicking on it in the External panel of the Console.
2.
Manipulate the desired software control with the mouse.
3.
Click on the Hand icon in the left parameter window and drag it over the desired hardware control in the control map, then
release the mouse button.
4.
Your hardware control is now linked to the software control; manipulating the hardware control manipulates the linked software
control.
Finally, you can [Right]/[Ctrl]-click on any knob or fader in the Console, or in a plug-in editor, to link a hardware control to a software con-
trol. To accomplish this, do the following:
1.
Manipulate the desired hardware control; for instance, turn a knob. That control should appear in the right parameter window.
2.
[Right]/[Ctrl]-click on the desired software parameter and choose “Assign X to Y,” where X is the software parameter and Y is the
hardware control you just manipulated.
3.
Your hardware control is now linked to the software control; manipulating the hardware control manipulates the linked software
control.
Global and Focus Mapping
There are two modes for mapping hardware and software controls: Global and Focus mode.
Global Mapping
With Global mapping, hardware and software controls maintain a one-to-one relationship, where a single hardware control is linked dir-
ectly to a single software control. Some controls, such as Track fader, pan, and mute, can only be mapped globally. To map a plug-in con-
trol globally, be sure Focus is disengaged in the plug-in window by clicking on the Focus button for the Keyboard you are using, so that it
is no longer highlighted.
Focus Mapping
While only one software control can be manipulated at a time by a single hardware control, a hardware control can be linked to any num-
ber of software controls, based on context, using Focus mapping. For instance, a single hardware knob could control the release of a
Gate plug-in, or the Gain of a distortion plug-in, or any number of other parameters, depending on which plug-in is in Focus.
The process of Focus mapping is identical to Global mapping, with one critical difference. To see this difference, open the interface for
any virtual instrument or effect. By default, all virtual instruments and effects open in Focus mode, and the Focus button in the plug-in win-
dow’s toolbar is highlighted. The Focus button displays the name of the related Keyboard.
Only one plug-in window can be in Focus at any time. Click on the Focus button to enable Focus in any open plug-in window.
When a parameter has been mapped in Focus, the link icon used in the parameter window is different from the icon used when a para-
meter is mapped globally.
Control maps only apply to the plug-in window that is in Focus. For instance, a hardware knob might be linked to a software knob in an
EQ plug-in that is in Focus. When another plug-in is brought into Focus, the hardware knob no longer affects the software knob in the EQ,
and it is possible to link this hardware knob to a different control for the plug-in that is in Focus.
In this way, Focus mapping allows different control maps to be made for each plug-in, using the same hardware controls for each. Each
Focus map is stored with the plug-in, making it usable in any Song. Thus, you can make Focus maps for each of your favorite plug-ins
and never worry about them again. In practice, this means that your external hardware always controls the plug-in that is currently in
Focus.
Certain parameters cannot be Focus-mapped, including Track controls such as fader, pan, and mute.
Control Link with External Instruments
Using the Control Link system, it is possible to control your MIDI-capable external hardware instrument just like a software instrument.
The first step in this process is to add your hardware instrument as an external device, as discussed in the Set Up Your MIDI Devices
section of the Setup chapter. Once you have the device set up, create a new Song and open the External panel of the Console.
Double-click on your external instrument in the External panel to open the control map for the instrument. If you created a new instrument
(that is, you are not using a predefined device), all possible Continuous Controller commands (MIDI CCs) are active and are represented
by knobs in the control map. If you are using a predefined map, only relevant controls appear. Also, notice the MIDI channel selector
above the control map. Only MIDI channels you enabled for the instrument are selectable.
Global and Focus Mapping

When working with a new instrument, you will want to customize its control map to include only the relevant controls with the appropriate
parameter names. To customize the control map, click on the Wrench icon, which opens the control list. As mentioned, all Continuous
Controllers are enabled by default, and they are labeled by their common uses. To add or remove any CC from the list, click its cor-
responding check box. To edit the title of the CC, click on the title and enter a new one.
Related controls can be grouped together in the control map by placing them in the same folder in the control-map list. Click in the Folder
field of any control in the control list and type a folder name to group that control with other controls that have the same folder name.
Once you have finished editing the control map for the instrument, using the mouse to move any knob in the control map should adjust
the linked parameter on the hardware instrument. The parameter shows up in the left Parameter window, just like any virtual software
instrument parameter. This means the same Control Link functions described previously in this chapter for virtual software instruments
are now available for controlling (and even automating) your hardware instrument.
Using Multiple External Devices
Any number of External Devices can be used simultaneously. As long as the device has a control map with some learned controls, it can
be used with the Control Link system. In each plug-in window, you can see mapping controls to the right of the preset and automation
controls. Only the External Device displayed in the Focus button can be used to Focus-map controls. If the External Device you are using
is not displayed there, the mapping is Global.
To choose a different device with which to Focus-map a plug-in’s controls, click on the down-arrow menu button and choose the External
Device you wish to use.
Automation with Hardware Controllers
As mentioned earlier in the Editing Automation Envelopes section of the Automation chapter, external hardware controllers can be
used to edit automation. When an external hardware controller has been mapped, and controls are linked to various parameters using
Control Link, hardware controller movements, and therefore the movements of the software parameters they control can be recorded as
automation.
Combining Studio One’s automation system with Control Link delivers a powerful integrated hardware-and-software automation plat-
form. The following describes how these systems are used together.
Hardware Controller Capabilities
You need to understand the capabilities of your hardware controllers. For instance, some controllers offer touch-sensitive faders and
knobs, and others do not. Some controllers have endless rotary encoders, and others have fixed-position knobs. These capabilities
affect how the hardware controllers integrate with the automation and Control Link systems.
Touch Sensitivity
Various automation modes are discussed in the Automation Modes section of the Automation chapter. These modes directly relate to
the specific capability of your hardware controllers. Touch automation mode is most effective if the hardware control is touch-sensitive.
However, you can use Touch automation with hardware controls that are not touch-sensitive.
Endless Rotary Encoders and Fixed-Position Knobs
The type of controls offered with hardware controllers varies widely. Many controllers offer knobs called “endless rotary encoders.”
These encoders can be rotated continuously in both directions. They increment and decrement values, rather than sending absolute val-
ues based on fixed positions, as with fixed-position knobs. Therefore, you get different results when automating an endless rotary
encoder versus a fixed-position knob.
For example, if you are using a touch-sensitive, endless rotary encoder to control a software parameter that has an automation envelope
on a Track, setting the Track to the Touch automation mode has the following results:
-
During playback, touching the rotary encoder writes automation until the encoder is no longer being touched. When the encoder
is not being touched, any existing automation is read.
-
If automation is being read during playback, and then the rotary encoder is turned, automation is written by incre-
menting/decrementing from the current automation position. In this way, the new automation effectively picks up from the exist-
ing automation.
If you do the same thing with a touch-sensitive, fixed-position knob, the following happens:
-
During playback, touching the knob writes automation until the control is no longer being touched. When the control is not being
touched, any written automation is read.
 Automation with Hardware Controllers

-
If automation is being read during playback, and then the knob is turned, automation is written, starting at whatever the current
value of the knob is, based on its absolute position. The new automation being written does not pick up from the existing auto-
mation.
Writing Track Automation
There are three Track-automation modes in which automation can be written using external controls: Write, Touch, and Latch. It is recom-
mended you be familiar with these modes, as described in the Automation Modes section of the Automation chapter.
To write Track automation using an external control, first link a control to a software parameter, as described in the Control Linking sec-
tion of this chapter. Then show automation by pressing [A] on the keyboard, add an automation envelope to a Track for the desired para-
meter, and enable Touch, Latch, or Write mode. Finally, start playback and manipulate the hardware control to write the desired
automation.
Automation can be written using hardware controls only during playback.
When overwriting existing automation, the three automation modes give different results.
-
Touch mode allows automation to be read until a touch-sensitive control is manipulated; automation is read again when the con-
trol is no longer being manipulated.
-
Latch mode results in automation being read until a control, touch-sensitive or not, is manipulated, after which automation is writ-
ten until playback is stopped.
-
When in Write mode, no existing automation is read, and automation is written for the duration of playback.
Track automation cannot be written using an external control if Read or Off mode is selected on the Track.
Writing Instrument Part Automation
Using external controls with Part automation is similar to using them with Track automation, except that there are no automation modes.
Existing Part automation is read and can be overwritten, and new automation can be written at all times while recording to a Part, as
explained in the Instrument Part Automation section of the Automation chapter. Part automation is an integral part of the Instrument
Part and therefore is accessible at all times.

## Mackie Control Support

Studio One supports Mackie Control and compatible hardware control devices. The following is an overview of all remote control func-
tions currently supported with the Mackie Control protocol. If you haven’t set up your Mackie Control-compatible devices, you can do so
from Options/External Devices (macOS: Preferences/External Devices). More information about using your controller can be found else-
where in the Control Link chapter.
Mackie Control Setup
Follow this procedure to set up your Mackie Control (or equivalent) main unit, as well as any extender units:

## Mackie Control Support

1.
Put the unit into Mackie Control Universal mode by holding down the Ch. 1 and Ch. 2 Select buttons while powering on the con-
troller. Do not use a lexan overlay.
2.
Add your Mackie Control in the Options/External Devices (macOS: Preferences/External Devices).
3.
Select the Send and Receive MIDI ports of your controller.
4.
Repeat this process for any extender units you plan to use.
Grouping Units

## Mackie Control Support

Use the Surface Placement option to create a Group and define the placement of each unit. Put two or more devices in the same group to
create a connected mixer bank.
Function Overview
Mixer Layout
The channel order follows the Remote Bank in the Studio One Mixer Bank pane. Here you can show and hide channels for the remote
banks.
Channel Controls
-
Record Arms the assigned audio track of the Channel.
-
Solo Solos the Channel (with Momentary mode).
-
Mute Mutes the Channel (with Momentary mode).
-
Select Sets the Channel to the Select state.
-
V-Pot Changes the assigned parameter. Push to set the default value. For more infomation, see Assignment Buttons.
Bank Channel-Type Filter Using Global View Buttons
-
Global View Shows all channels (Send, Console, and Outputs).
-
Inputs is unused.
-
Audio Tracks Displays Audio Channels.
-
Audio Instrument Displays Instrument Output Channels.
-
Aux Displays FX Channel
-
Buses Displays Buses.
-
Outputs Displays Outputs.
-
User Displays all remote back channels.
-
Fader Flip flips the V-Pots with their corresponding faders.
The assignment buttons are used to assign controls to the V-Pots.
Pan Modes
Press Pan repeatedly to toggle between pan overview and pan focus mode.
-
Pan Overview Mode Shows the track names in the LCD strip and assigns V-Pots to Channel Pan.
-
Pan Focus Mode
-
Strips show pan parameters (name + value)
-
Last strip shows selected track
-
Select buttons: select focus track
-
“FLIP” off:
-
Pots control pan parameters
-
Faders control channel volume
-
Last strip pot selects pan mode
-
“FLIP” on:
-
Faders control pan parameters
-
Pots control channel volume
-
Last strip fader selects pan mode
The Pan Mode syncs across multiple devices in a device group and each device can control Pan Modes.

## Mackie Control Support

Sends
-
Sends assigns V-Pot to Sends.
-
"SE" displays all Sends per selected Channel.
-
"S1-8" displays Send slot 1-8 on all channels.
-
Press Sends several times to step through the layers.
-
Track Modifies track parameters of the selected Channel.
-
Bypass all plug-ins.
-
Monitoring on/off.
-
Select Channel Input.
-
Select Channel Output.
-
Bypass Sends 1-4.
-
EQ is a bypass for Insert 1-8 of the selected Channel.
-
Plug-in sets the V-Pots to Control Link mode.
-
Instruments is unused.
Toggle the automation mode for the selected Channel.
Control Link for Plug-ins
In Control Link mode, you can customize the parameters shown in the plug-in mode for each plug-in. This can also be done by dragging
parameters to the Mackie Control device editor from the top left of the toolbar or from the plug-in editor.
Each Mackie Control Universal and Mackie Control Extender is a separate Control Link device.
Transport
The Play, Rec, Stop, FF, and RW buttons control the transport.
With the Marker button enabled, FF and REW jump between markers, and the REC button inserts a marker at the cursor position.
Function Keys
Function keys are predefined but can be modified using the Mackie Control device editor.
-
F1 Show Inputs
-
F2 Show Track
-
F3 Console
-
F4 Open Channel
-
F5 Add Insert
-
F6 Add Send
-
F7 Show Channel Editor
-
F8 Toggle Floating Window

## Mackie Control Support

Utility Functions
-
Save Press the Save button to save.
-
Press Shift + Save button to open the Save As dialog.
-
Undo Press to undo the last edit.
-
Press Shift + Undo to redo edit.
-
Cursor Keys Navigate in the arrangement.
-
Horizontal and vertical zoom when zoom button is enabled, can be used to navigate in the Insert/Send list and can
be combined with Enter/Cancel to add plug-ins or Sends.
Option + Bank Select Selects previous and next device in an open plug-in editor.
-
Option + Channel Select Selects previous and next preset in an open plug-in editor.
Other Functions
-
Cursor Keys navigate the arrangement (depending on current window focus).
-
Wheel jumps to the nearest bar in the Arrangement (no scrub support).
-
SMPTE/Beats button toggles the time display.
-
Name/Value button toggles the value and track name in the display when the assignment is Send 1-8 or Control Link Mode.
-
Momentary mode for Solo and Mute:
-
Press the button to quickly toggle the state.
-
Press and hold the button to switch momentarily.
-
Press the V-Pot to set the default parameter.

## Mackie Control Support
