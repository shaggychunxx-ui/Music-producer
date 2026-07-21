# Recording

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 71–91
> **Slug:** `06-recording`

**Agent topics:** `audio tracks`, `instrument tracks`, `metronome`, `loop recording`, `step record`, `track layers`, `cue mix`, `low-latency monitoring`, `print effects`, `monitor mix`

---

Recording
The following chapter discusses aspects of recording in Studio One, including Audio and Instrument Tracks, recording modes and
formats, and recording tips.

## Audio Tracks

Before recording can take place, you need at least one Track on which to record. Studio One has two types of Tracks for basic recording:
the Audio Track and the Instrument Track. Audio is recorded to Audio Tracks, while musical performance data is recorded to Instrument
Tracks.
Creating an Audio Track
To create an Audio Track, navigate to Track/Add Tracks or press [T] to open the Add Tracks menu.
The following options are available in this menu:
-
Name Click here and type in a name for the new Track.
-
Count Choose the number of Tracks you would like to create.
-
Type Choose Audio.
-
Color Choose a color.
-
Auto-Color Check this box if you would like your Tracks auto-colored.
-
Format Choose mono, stereo, or one of many available surround formats. (For more on mixing in Spatial Audio, visit the Spatial
Audio topic.)
-
FX Chain Choose an FX Chain to be pre-loaded on the Tracks.
-
Input Assign an audio Input to the new Track(s). When creating multiple Tracks, you can engage the Ascending option to assign
Inputs to each Track in ascending order (Track 1, Input 1, Track 2, Input 2, etc.).
-
Output Assign an audio Output to the new Track(s). When creating multiple Tracks, you can engage the Ascending option to
assign Outputs to each Track in ascending order (Track 1, Output 1, Track 2, Output 2, etc.).
-
Load Track Preset… Choose from a list of your stored Track Presets. Track Presets
Once these options are configured, click on OK, and the Tracks appear in the Arrange view, below the currently selected Track.
Navigate to Track/Add Audio Track (mono or stereo) to quickly add an audio Track.
Recording

[Right]/[Ctrl]-click in blank space in the Track Column and select Add Tracks For All Inputs to quickly add a Track for every configured
input in Audio I/O Setup.
Alternatively, you can [Right]/[Ctrl]-click in any blank space in the Track Column of the Arrange view and select Add Audio Track (Mono)
or Add Audio Track (Stereo) to quickly add an audio Track.
Use and Create Presets
In Studio One, you can store presets of an entire chain of effects plug-ins as an FX Chain, allowing quick recall of complex effects setups
on any Track. Any factory preset or user-created FX Chain can be selected as a Preset when creating a Track. For more information,
refer to the FX Chains section of the Mixing chapter.
Configuring an Audio Track
This section describes the editable Audio Track parameters.
Input/Output Selection
An Audio Track’s I/O channel(s) can be selected from three places: the Track Column, the Console, and the Track Inspector.
To select an Input Channel from the Track Column:
-
If needed, expand the Track's control area to expose the input selector.
-
Click the Input Selector immediately below the horizontal Track fader to choose from any configured Input Channel.
To select an Input or Output Channel from the Console:
-
Open the Console by clicking the [Mix] button, or press [F3] on the keyboard.
-
Click the selectors above each Track’s Fader and Pan controls to choose an Input and/or Output Channel. The Input Channel
selector is on top, with the Output Channel selector beneath.
To Select an Input or Output Channel from the Inspector:
-
Open the Inspector window by clicking on the [I] button above the Track Column or pressing [F4] on the keyboard.
-
In the Channel area of the Inspector window, you can find the currently selected Track’s Channel Mode toggle (mono or stereo)
and Input and Output Channel selectors.
-
Click on the Input or Output Channel selector to choose a Channel.
Stereo Tracks can select from both mono and stereo Input Channels, while Mono Tracks can only select from mono Input Channels.
A Track’s Channel Format (mono or stereo) can be switched with a single click of the single-circle (mono) or double-circle (stereo) icon.
You can toggle many Tracks’ Channel Format simultaneously by selecting multiple Tracks before clicking this icon.
Multichannel surround formats are available from the drop-down menu to the right of the Channel Format icon.
Tempo Mode
The Tempo mode, found in the Inspector, affects the way in which Audio Events are handled on any audio Track.

## Audio Tracks

There are three Tempo modes:
-
Don’t Follow Audio Events on the selected Track are not affected by Song tempo.
-
Follow The start position of Audio Events on the selected Track is adjusted with tempo changes, so the Events stay in sync with
their Bars (bars and beats) position. The length of the Event is not affected.
-
Timestretch Assuming that the Song file contains tempo information, tempo changes cause Audio Events on the selected
Track to be dynamically stretched so that the Events’ start and end times stay in sync with their Bars (bars and beats) positions.
The length and internal timing of the Event is affected in the stretching process but the pitch of the audio remains unaffected.
If the Stretch Audio Files to Tempo option is selected when creating a new Song, Timestretch is set as the default tempo mode for all new
Audio Tracks.
Re-Recording
Instrument Output and Bus channels can be selected as the input to any stereo Audio Track. These Channels are grouped in branches in
the input selection menu for the Audio Track.

## Audio Tracks

This is very useful in a number of situations in which you would like to “print” the live output of one of those Channel types (live virtual
instrument recording to audio, hybrid analog mixing, etc.).
Record-Enabling an Audio Track
To record to an Audio Track, the Track must be record-enabled. To record-enable an Audio Track, click on the Track’s Record Enable
button once or select the Track and press [R] on the keyboard. Select multiple Tracks and record-enable any of them to record-enable all
selected Tracks. The Record Enable button turns red when active, and the Track’s meter begins to move up and down if there is live
audio input on the Track’s selected Input Channel.
Alternatively, if you press and hold [Alt]/[Option] on the keyboard, and then click on Record Enable, you both record-enable the related
Track and disarm record-enable for all other Tracks.
You can find the Audio Input Follows Selection in the Studio One/Options/Advanced/Console options list (macOS: Prefer-
ences/Advanced/Console). Engaging this automatically record-enables the last Track selected in the Arrange view. Monitor-enable is, by
default, automatically engaged when Record Enable is engaged.
When an Audio Track is record-enabled, a clip indicator appears at the top of the input-level meter for that Track in the Arrange view. If
clipping occurs at the input, the clip indicator turns on. When clipping occurs, you should adjust the input gain/level on your audio inter-
face, as once the distorted signal is recorded, it cannot be fixed.
Once an Audio Track is record-enabled, you are ready to record. Refer to Activating Recording for more on this topic.
Software Monitoring
To monitor (listen to) live audio input on an Audio Track, click on the Monitor enable button once. This button should turn blue, and you
should begin to hear your live audio input and see its input level on the Track meter. You can also hold [Alt]/[Option] on the keyboard and
then click on the Monitor enable button to simultaneously engage monitoring on a Track and disengage monitoring on all other Tracks.
It may be helpful to picture the signal path to understand exactly what is happening. For example, if you are listening to a guitar plugged
into channel 1 on your audio interface, then Studio One receives the guitar input on Hardware Input 1.

## Audio Tracks

In Audio I/O Setup, you will have created a mono Input Channel with Hardware Input 1 as its source. Your Audio Track has that Input
Channel selected as its input. The Output of your Audio Track is likely to be the Main Output, which is a stereo Output Channel. The Out-
put Channel sends to a designated stereo pair of outputs on your hardware audio interface, which presumably are connected to your
monitor speakers or headphones.
When monitoring live audio input from a microphone, avoid listening with speakers that are in close proximity to the microphone. Other-
wise, you might create a feedback loop that could quickly generate dangerously loud audio levels, possibly harming your ears and your
speakers.
Hardware Monitoring
Some audio interfaces feature the ability to monitor the hardware inputs and outputs directly, as opposed to monitoring through software.
This is referred to as “hardware monitoring” or “zero-latency monitoring.” When using this type of interface, we recommend that you mon-
itor live audio input via the hardware, rather than through the software. This can help you to avoid common problems that result from soft-
ware latency, such as hearing a delay when you record vocals, or recording off-beat.
Setting Input Levels
Setting good input levels is critical to making a good recording. This begins with the hardware audio interface. If the hardware’s input
level is set too low, and you increase the level later in Studio One to compensate, you also raise the level of any noise in the signal. If the
level is too high, you can overload the hardware input, causing unpleasant clipping distortion that cannot be fixed. Therefore, you should
set the input gain on your audio interface as high as possible without overloading the input. There is usually a clip indicator for each input
on the audio interface to assist you in detecting overloads.
As long as the input levels are not clipping in your audio interface or on the Track to which you are recording in Studio One, you can
always adjust the levels of recorded material after the recording is made. To visually monitor the input levels for any input in Studio One,
it is best to view the Input Channels in the Console by clicking on the Inputs tab in the Console.
Disabling an Audio Track
When working in large Songs with high Audio and Instrument Track counts, it can be useful to disable certain Tracks that are not cur-
rently in use, to free up CPU and RAM resources for use elsewhere. Disabling an Audio Track disables and unloads any Insert effects
used. To disable an Audio Track, [Right]/[Ctrl]-click the Track in Arrange view, and choose "Disable Track" from the pop-up menu. To re-
enable a disabled Audio Track, [Right]/[Ctrl]-click the Track and choose "Enable Track" from the pop-up menu.

## Instrument Tracks

Instrument Tracks are where performance data is recorded, drawn, and edited. This data usually comes from a Keyboard, which is used
to play a virtual instrument or hardware sound module. Performance data is not audio; the virtual instrument or sound module is the audio
source.
In Studio One, MIDI controllers are referred to as Keyboards. If you have not set up a Keyboard, refer to the Set Up Your MIDI Devices
section of the Setup chapter.
Creating an Instrument Track
To create an Instrument Track, navigate to Track/Add Tracks or press [T] to open the Add Tracks menu.

## Instrument Tracks

The following options are available in this menu:
-
Name Click here and type in a name for the new Track.
-
Count Choose the number of Tracks you would like to create.
-
Type Choose Instrument.
-
Color Choose a color.
-
Auto-Color Check this box if you would like your Tracks auto-colored.
-
Input Assign a MIDI input Device to the new Track(s). Choose All Inputs | Any to accept input from any connected MIDI Device.
-
When creating multiple Tracks, you can engage the Ascending option to assign inputs to each Track in ascending order
of device and MIDI channel.
-
Output Assign an Instrument to the new Track(s). To create a new instance of a software instrument for each new Track,
choose New Instrument and select an instrument from the provided list. To assign the new Tracks to a hardware instrument or to
a software instrument already in use in the Song, choose Existing Instrument, and select from the provided list.
-
When creating multiple Tracks, you can engage the Ascending option to assign Outputs to each Track in ascending
order of Instrument and MIDI channel.
Once these options are configured, click OK, and the Tracks appear in the Arrange view, below the currently selected Track. It is import-
ant to note that Instrument Tracks do not appear directly in the Console, as they do not output audio. The virtual instruments generate
sound and are represented in the Console by Instrument Channels.
Alternatively, [Right]/[Ctrl]-click in a blank space in the Track Column of the Arrange view and select Add Instrument Track from the pop-
up menu to quickly add an Instrument Track.
Configuring an Instrument Track
An Instrument Track can only receive input from a Keyboard that has been set up in the External Devices menu. To set up a Keyboard,
refer to the Set Up Your MIDI Devices section of the Setup chapter. If you have a Keyboard set up as the default Instrument Track
input, all Instrument Tracks default to using that Keyboard.
An Instrument Track can trigger a virtual instrument that has been set up in a Song or an external instrument. The Instrument Track Input
and Output can each be selected in one of two places:
Selecting an Instrument Track Input or Output from the Track Column:
-
Set the Arrange view Track size to medium or larger to be able to access the current Instrument Track Input.
-
There are two I/O selectors on each Instrument Track. Click the top selector to choose an output to any previously set up virtual
or external instrument. Click the bottom selector to choose from any configured Keyboard input.
Selecting an Instrument Track Input or Output from the Inspector:

## Instrument Tracks

-
Open the Inspector window by clicking on the [I] button above the Track Column or by pressing [F4] on the keyboard.
-
Click the Input or Output selector to select from any configured Keyboard input or to trigger any previously set up virtual or
external instrument.
-
Press [F11] to open the instrument editor for the selected Instrument Track.
Note that it is possible to select All Inputs as the input for Instrument Tracks, which combines the input of all defined keyboard devices. If
Default Instrument Input is not checked for any Keyboard device, new Instrument Tracks automatically use All Inputs.
This item is always in the inputs list, even if no keyboard device is defined. However, for any MIDI input to be received on an Instrument
Track, your MIDI input device (Keyboard Controller, etc.) must first be set up in the External Devices menu as a Keyboard.
Set Up a Virtual Instrument
Studio One supports VST and AU virtual instruments, and Studio One's Native virtual instruments. The difference between these types
of virtual instruments is transparent to the user in Studio One, as they are all handled in the same manner. To use any VST or AU virtual
instrument, you need to be sure Studio One knows where they are installed on your computer. Refer to the VST Plug-ins section of the
Setup chapter for more information on locating your plug-ins.
Add a Virtual Instrument from the Browser
To add any VST, AU, or built-in virtual instrument to your Song, open the Browse view and click on the Instruments tab to view your vir-
tual instrument. Then do one of the following:
-
Click on and drag any virtual instrument to an empty space in the Arrange view to simultaneously add the virtual instrument to
your Song and create an Instrument Track with its output routed to the virtual instrument. The Instrument Track conveniently
inherits the name of the virtual instrument.
-
Click on and drag any virtual instrument on top of an existing Instrument Track to replace the Track’s current virtual instrument.
-
Click and drag any virtual instrument from the Instruments tab to the Console to simply add the virtual instrument to your Song.
In order to control or play this virtual instrument, you need to select it as the output for an Instrument Track.
-
The virtual instrument is now set up and ready to play and has one or more dedicated Audio Channels in the Console.
Once a virtual instrument is added to your Song, be sure that an Instrument Track is routed to it so that the instrument can be played.
Set Up Multiple Virtual Instrument Outputs
Many virtual instruments have the capability to send audio on more than one channel. In Studio One, only the first output or output pair of
any virtual instrument is active by default.

## Instrument Tracks

To activate the other possible virtual instrument Output Channels in the Console:
-
Open the Console by pressing [F3] on the keyboard, then open the Instruments panel (open by default) by clicking the [Instr.]
button to the far left of the Console.
-
Click once on the virtual instrument in the Instruments panel, and the Output Channel activation menu expands.
-
Click on the checkbox next to any output to activate that output for the virtual instrument.
-
Each active virtual instrument output has a dedicated Audio Channel in the Console, as well as a level meter preview inside the
Output Channel activation menu.
You can also activate virtual instrument outputs in the plug-in window. Any virtual instrument plug-in that offers multiple Output Channels
has an Outputs button near the top of the plug-in window. Click on this button to view and activate the available outputs.
Record Enabling an Instrument Track
To record musical performance data to an Instrument Track, the Track must be record-enabled. To record-enable an Instrument Track,
click on the Record Enable button once; it should turn red.
Also, note that monitor-enable is, by default, automatically engaged when Record Enable is engaged. This behavior can be configured in
the Studio One/Options/Advanced/Devices menu (macOS: Preferences/Advanced/Devices). If note data arrives from the Track’s selec-
ted Keyboard, the Instrument Track’s meter moves up and down, corresponding to that input.
Once an Instrument Track is record-enabled, you are ready to record musical performance data to that Track. Refer to Activating
Recording for more on this topic.

## Instrument Tracks

Monitoring an Instrument Track
Instrument Tracks record and output musical performance data, not audio. The virtual or external instrument to which the Instrument
Track is routed generates the audio. The following describes how virtual and external instrument audio output is monitored.
Disabling an Instrument Track
When working in large Songs with high Audio and Instrument Track counts, it can be useful to disable certain Tracks that are not cur-
rently in use, to free up CPU and RAM resources for use elsewhere. Disabling an Instrument Track also disables and unloads any Insert
effects used. To disable an Instrument Track, [Right]/[Ctrl]-click the Track in Arrange view, and choose "Disable Track" from the pop-up
menu. To re-enable a disabled Instrument Track, [Right]/[Ctrl]-click the Track and choose "Enable Track" from the pop-up menu.
Monitoring a Virtual Instrument
Virtual instruments usually load with a default sound; however, you should be sure that the virtual instrument you wish to monitor is set up
correctly to generate audio. With the Output of an Instrument Track routed to the virtual instrument you wish to monitor, click on the Mon-
itor button, and it turns blue.
You should now be able to play the Keyboard that you selected as the input to the Instrument Track and should see the Track meter mov-
ing, as well as hear the audio output of the virtual instrument. If you cannot hear the audio output of the virtual instrument, make sure that
your virtual instrument is set up correctly and that the corresponding Audio Channels in the Console are not muted.
If you select the Instrument Input Follows Selection option in the Options menu, any Instrument Track you select automatically has Mon-
itor and Record enabled, and all other Instrument Tracks have these disabled.
Monitoring an External Instrument
You can use an Aux Channel to monitor the audio output of an external instrument if you don't want to record the audio to your hard drive.
This is useful when working with an external MIDI hardware synthesizer, for example, as you can make changes to the MIDI data on an
Instrument track without needing to record another take to your hard drive. Audio from the device returns through your audio interface
into an Aux Channel in the Console, where it becomes a part of the mix like any other track.
Remember, if your external instrument is also a controller (such as a keyboard workstation), you need to set it up twice. First, set it up as
an External Instrument without a Receive From selection, and then set it up as a Keyboard, without a Send To selection. This allows the
keyboard-controller section of the workstation to be used as a source for Instrument Tracks, while allowing the synthesizer section to be
used as an external instrument.
Here's how to set up an Aux Channel for an external instrument:
1.
If you haven't already done so, set up the external instrument as a MIDI device.
2.
Press [F3] to open the Console.
3.
Click [External] in the Console Navigation column to open the External Devices panel.
4.
Click the menu arrow for the external device.
5.
Select Edit from the menu to open the control mapping window.
6.
Click the Outputs button (
).
7.
Select Add Aux Channel at the bottom of the window. An Aux Channel appears in the Console.
8.
If your external instrument has multiple outputs connected to your audio interface, add as many Aux Channels as you need.
9.
Important: Click Save Default before closing the window. This makes it easy to create new instrument tracks with the Aux Chan-
nels already mapped. See Make an Instrument Track for the Aux Channel to learn more.
10.
Route the Aux Channel to the desired output. Your external device is now available the Console.
Remember that the external instrument needs to be physically connected to one or more inputs on your audio interface, since its audio
will always be "live".
Note also that running external audio signals through the Console means that bouncing, rendering and mixdown automatically switches
to real-time.
Rendering Note FX
If you wish to make the effects of Note FX processing permanent (part of the note data, rather than a real-time process), select the Track
and navigate to Event/Render Instrument Tracks, or [Right]/[Ctrl]-click the desired Part in Arrange view and choose Instrument
Parts/Render Instrument Tracks from the pop-up menu.
This also makes permanent any transposition or velocity changes you've made within the Inspector view for the track.

## Instrument Tracks

## Activating Recording

Once you have the desired Tracks created, setup, and record-enabled, the next step is to record. The following illustrates several ways
to activate recording, each associated with a different purpose.
Manually
Manually activating recording is the most basic way to record. Recording starts at the current playback-cursor position and continues
until you manually stop recording. To manually activate recording, click on the Record button in the Transport or press [NumPad *] on the
keyboard.
The Record button in the Transport turns red, the playback cursor starts to scroll from left to right, and new Events are recorded to any
record-enabled Tracks. Recording continues until you manually stop it.
Precount and Preroll
When recording audio or Instrument Parts, it is often useful to give the performer a count-in before recording begins, to alert them that
recording is starting, and present the tempo of the Song so that they can play on-beat from the start. Studio One offers two ways to do
this: Precount and Preroll.
Engaging Precount lets you specify a number of bars of metronome clicks to be played before recording begins. Preroll lets you specify a
number of bars in the Song to play before recording begins. Choose the mode that best meets your needs as you record.
Follow these steps to use Precount or Preroll:
1.
Click on the Metronome Setup button to open the Metronome Setup menu.
2.
Select Precount or Preroll in the Metronome Setup menu, and enter a number in the Bars field for the number of bars you wish to
play before recording begins.
-
You can also enable the selected mode by clicking on the Precount or Preroll button in the Transport, or by pressing
[Shift] + [C] on the keyboard to engage Precount, or [O] to engage Pre-Roll.
3.
Set the playback cursor to the timeline position at which you wish to begin recording.
4.
Click on the Record button in the Transport or press [NumPad *] to begin recording.
-
In Precount mode, the Metronome clicks for the specified number of bars. The number of beats remaining before record-
ing starts is displayed in the Record button in the Transport.
-
In Preroll mode, playback begins a specified number of bars before the position you chose, with the playback cursor
moving from left to right.
5.
Recording automatically activates at the position you chose. The Record button in the Transport turns red, the playback cursor
scrolls from left to right, and new Events begin recording to any record-enabled Tracks.
6.
Recording continues until you manually stop it by pressing [Space Bar] on the keyboard or clicking Stop in the Transport.
Auto Punch
It is sometimes useful to automate the point at which recording begins and ends. For example, if you wish to record over a specific
phrase of a vocal part, but not before or after that phrase, you can automatically begin and end recording at specified points. This pro-
cess is commonly referred to as “punching in and out,” and the resulting new Audio Event is referred to as the “punch-in.”

## Activating Recording

In Studio One, punching in/out is achieved with the Auto Punch feature. Follow these steps to engage Auto Punch:
1.
Set the Left Locator in the Timeline Ruler of the Arrange view at the position you wish to punch in—that is, where recording
should begin.
2.
Set the Right Locator in the Timeline Ruler of the Arrange view at the position you wish to punch out, that is, where recording
should stop.
3.
Click on the Auto Punch button in the Transport, or press [I] (the letter ‘i’) on the keyboard.
4.
With Tracks record-enabled, begin recording at any point before the Left Locator position.
5.
Playback begins and recording automatically activates at the Left Locator position. The Record button in the Transport turns red,
the playback cursor continues to scroll from left to right, and new Events begin recording to any record-enabled Tracks.
6.
Recording automatically stops at the Right Locator position. However, playback continues beyond the Right Locator position
until you manually stop it by pressing [Space Bar] on the keyboard or by clicking Stop in the Transport.
If you use the Auto-Punch feature in Studio One to record your punch-ins, or if you punch in manually, the newly recorded audio is auto-
matically crossfaded at its edges with the existing Audio Event, so the transition between the old and new audio is not audible. The cross-
fade time is very small and not audible; however, you can edit the crossfade manually.

## Metronome Control

A metronome makes audible clicks or other sounds that correspond to beats at a selectable tempo, providing the musicians with a tempo
reference while recording. This is especially useful when recording drums or other rhythm-intensive tracks, as the editing and arranging
processes are made much easier when the recorded audio lines up with musical bars and beats.
In Studio One, the metronome can be engaged and disengaged both globally and for each hardware output in the Console, including the
Main Out and any Sub Outs.
Turn the Metronome On/Off Manually
In the Transport, the Metronome button is to the left of the Master Volume fader and meter. Click on the Metronome button, or press [C]
on the keyboard, to globally engage and disengage the metronome. The metronome is globally disengaged by default.
The Output Channels in the Console also feature Metronome buttons and level controls above the volume fader. These controls allow
you to choose, for each output, whether or not the metronome is heard, and its level.
Metronome Setup
Click the Metronome Setup button (next to the Metronome button in the Transport) to access the Metronome Setup menu. In this menu,
you can configure sounds and behavior for the metronome, as well as Precount and Preroll.

## Metronome Control

Here, you can choose an individual sample and volume level for Beats, Accents, and Offbeats. Accents play on the downbeat, or first
beat, of each new bar. Offbeats play in the space between each Beat. You can choose from seventeen default samples for each, includ-
ing Click, Clave, Rim Shot, and Tambourine. By default, the Accent Level setting is higher than the Beat Level setting, as most musicians
like to have the downbeat of each bar emphasized to help keep time.
Metronome Presets
Once you have configured the Metronome, you can save the current setup as a preset by clicking the [Store] button.  These presets can
be recalled at any time by clicking the [Load] button.
Precount and Preroll
Precount and Preroll are two methods you can use to signal the start of recording and give a sense of the song's tempo to a musician
before recording begins. When you click Record with Precount enabled, the metronome clicks for the number of bars specified in the
Bars parameter, before recording starts. When you click Record with Preroll enabled, Studio One starts playback behind where the
cursor is placed, by a number of bars specified by the Bars parameter. When playback passes the cursor position, recording starts.
When Precount is enabled, pressing record shows a countdown in the record button, of the number of beats remaining before recording
starts.
Precount can also be enabled by clicking the Precount button, to the left of the Metronome buttons in the Transport, or by typing [Shift] +
[C]. Preroll can also be enabled by typing [O].
Repeat Accent
This setting repeats the Accent sound when using a time signature with more than one accent per bar, such as 12/8. You can try this out
by doing the following:
1.
Open the Metronome settings, and chose a sound for the Accent that is different from both the Beat and the Offbeat.
2.
Leave the Repeat Accent checkbox empty.
3.
Make sure the Click in Play option is active, so that you can hear the Metronome during playback.
4.
Set the time signature to 12/8, and either click the Play button or press the Space Bar.
You’ll notice the Accent is only heard every 12 beats. However, if you go through steps 3 and 4 with the Repeat Accent function switched
on, the Accent is heard every 3 beats.
Click in Precount Only
When recording is triggered with Pre-Roll engaged, as discussed in the Precount and Preroll section of this chapter, a specified num-
ber of Precount bars play before reaching the current playback cursor position. The number of Precount bars is specified in the Met-
ronome Setup menu. In this same menu, there is a checkbox to engage the Click Only in Precount option, which is disengaged by
default.

## Metronome Control

With Click Only in Precount engaged, the metronome provides a traditional count-in during the Precount bars and is not heard beyond
those bars.
Click in Play
The Click in Play option in the Metronome setup menu allows you to enable/disable the Metronome during playback, as opposed to while
recording. Disabling Click in Play allows you to leave the Metronome engaged in the Transport at all times, so that if you are recording,
you hear a click, but if you are playing back, you do not hear the click. Click in Play is engaged by default; click on the Click in Play check-
box to disengage the Metronome during playback.
Render Metronome
You can create an Audio Track of the Metronome by clicking the [Render] button located in the upper-right corner of the Metronome
Setup window, and choosing one of the Render range options. These options allow you to create a click track that is either the full length
of your Song, or just the length of a looped range within it, such as 4, 8, or 16 bars.

## Loop Recording on Audio Tracks

It can be very useful to loop a specific section while recording in order to capture multiple performances or takes of the same musical pas-
sage. In Studio One, this is called “Loop Recording.”
Follow these steps to accomplish Loop Recording:
1.
Set the Left and Right Locators in the Timeline Ruler at the beginning and end, respectively, of the area in which you wish to
record.
2.
Click on the Loop button in the transport or press [NumPad /] on the keyboard to engage Looping.
3.
Activate recording manually or via Pre-Roll or Auto Punch.
4.
When the playback cursor reaches the Right Locator position, it loops back to the Left Locator Position.
5.
Recording continues until you manually stop it by pressing [Space Bar] on the keyboard or clicking Stop in the Transport.
When Loop Recording with Audio Tracks, multiple Takes are created. These Takes represent each recorded pass over the looped
region. If Record Takes to Layers is engaged in the Record panel, opened from the View menu or with [Shift]+[Alt]+[R] on the keyboard,
the takes are automatically placed in separate layers which are expanded when recording is stopped. Refer to the Comping section of
the Editing chapter of this manual for more information.
Selecting Takes of an Audio Event
When there are multiple Takes available for an Audio Event, the Take icon appears in the lower left corner of the Event in the Arrange
view.
By default, the last recorded Take is selected. To select any other take, [Right]/[Ctrl]-click on the Audio Event to expose a list of Takes.
Click on any numbered Take to select it. Takes are edited as a single Audio Event, so sizing or splicing any Take splices all of the Takes
contained in the Audio Event.
It is possible to splice an Audio Event that contains multiple Takes, then select a different Take for each splice of the original Event. For
example, if you recorded three Takes for a vocal verse, you could split that Audio Event in between each vocal phrase, and then, for each
phrase, select the best of the three Takes.
Unpack Takes
When two or more Takes exist for an Audio Event, it is possible to unpack the individual takes to separate Events on new Tracks, new
Layers, or existing Layers. To do this, [Right]/[Ctrl]-click on the Event and click on Unpack Takes in the contextual menu.

## Loop Recording on Audio Tracks

Choose Unpack to Tracks to place each Take at the appropriate time on its own new Track. Note that the settings of the originating Track
are not duplicated for the new Tracks.
Choose Unpack Takes to New Layers to place each Take on its own Layer. This is usually done for comping, discussed in detail in the
Comping section of the Editing chapter. Choose Unpack Takes to Existing Layers if you would like to unpack the Takes to existing Lay-
ers.
Set and Shift Loop
Several key commands that you may find helpful when loop recording are available in the Keyboard Shortcuts menu and by default have
no key command assigned.
Set Loop Start and Set Loop End allow you to place the left and right locators at the current playback-cursor position. The same com-
mands might be used when setting left and right locators for a punch-in using Auto Punch.
Shift Loop and Shift Loop Backwards allow you to move the loop range to the next or previous range of equal time. For instance, if you
have eight bars looped, Shift Loop would move the loop range to the next eight bars.

## Instrument Track Recording Modes

There are several modes for recording to an Instrument Track. To switch between these modes, navigate to the View menu and select
Record panel, or press [Shift]+[Alt]+[R] on the keyboard. In the Record panel, you can choose between a range of recording modes, and
access creative recording tools. The following describes each of the Record Panel modes and functions.
Record Mode Options
Replace and Overdub
When in the Replace recording mode, recording over any existing Instrument Part results in the new material being recorded to a new
Event, which replaces that portion of the original Event. While recording, you do not hear the previously recorded Event playing back, as
the purpose of this mode is to replace the existing material.
When Replace is disabled, you are in Overdub recording mode. In this mode, recording over any existing Instrument Part results in the
newly recorded material being overdubbed, or added to, the existing material. While recording, you hear the previously recorded Event
playing, along with the material currently being recorded, assuming that you are monitoring the Instrument Track.
Takes to Layers
Engage the Record Takes to Layers option to move the contents of each Take created while recording in loop mode to its own Layer
below the current Track. If you engage this option while Record Takes is enabled, the notes from each run-through of the loop are
moved to their own new Layer. Engaged while Record Mix is enabled, a new Layer is created each time recording is started and
stopped, containing all notes from the entirety of the most recent recording pass.
Input Quantize
Engage Input Quantize to snap recorded notes to the rhythmic value set by the Quantize parameter. When recording parts that are
destined to be heavily quantized (such as synth arpeggios or drum-machine-style beats), this saves you the step of later Quantizing the
contents of your loop.
Instrument Loop Record Options
Record Takes and Record Mix
If Loop is engaged in the Transport while recording, the recording mode changes either to Loop Record Takes or Loop Record Mix,
depending on the selection in the Record panel. These modes are functionally similar to the regular Record Mode Overdub and Record
Mode Replace.
When Loop Record Takes is selected, each pass through the looped region is recorded to a new Take within a single new Instrument
Part. When recording is stopped, each Take is individually selectable by [Right]/[Ctrl]-clicking on the Instrument Part and choosing one of
the numbered takes from the top of the pop-up menu. Only one Take can be selected at a time for any Instrument Part.
Takes on Instrument Parts can be unpacked to new Instrument Tracks, as with Audio Event Takes, described in the Unpack Takes sec-
tion of this chapter.

## Instrument Track Recording Modes

When Loop Record Mix is selected, each pass through the looped region is added to the existing material within a single new Instrument
Part. For instance, if you loop a four-bar region to record a new drum part, this would allow you to play one piece of the drum kit during
each pass until you have recorded the whole part.
Instrument Recording Tools
Undo Last Loop and Undo All Loops
The standard Studio One Undo/Redo functions do not apply to individual record passes in Loop mode. Instead, use these two special
Undo buttons. Once you have some note information in your loop, you can click Undo Last Loop to erase only the notes added in the
most recent run-through of the loop. Click Undo All Loops to erase all notes in the current loop, and start fresh.

## Note Repeat

With Note Repeat active, any notes played retrigger according to the current Rate setting. This can be set to QT (to follow the current
quantize value) or to any specific rythmic value.
For example, when Rate is set to 1/16, held notes create a series of 16th notes at those note values. This can come in handy when
recording drum fills or rhythmic synth parts. Note that this mode cannot be combined with the Note Erase mode.
If your MIDI keyboard or controller supports aftertouch, you can vary the velocity of repeated notes by applying pressure to the keys or
pads when the Aftertouch feature is enabled. The higher the pressure, the greater the velocity of the recorded notes.
Note Repeat Options
Note Repeat is highly configurable, and can be controlled extensively using MIDI, which unlocks a wealth of real-time creative options.
To reach the options window for Note Repeat, click on the wrench-shaped icon in the Note Repeat section of the Record Panel. You can
also open this window by enabling Key Remote mode.
-
Active When enabled, Note Repeat is turned on.
-
Rate Sets the rhythmic rate of Note Repeat.
-
Gate Sets the length of each note.
-
Quantize When enabled, all repeated notes snap to the main Song grid, even if a note is played off-beat. Disable this option to
allow free play of note repeat without rhythmic correction.
-
Aftertouch When enabled, key or poly pressure can be used to control note velocity as a note is held.

## Instrument Track Recording Modes

-
Single Mode When enabled, a range of keys on your MIDI controller play one note at different rates. By default, this note is the
last note played before this mode was enabled.
-
Change the Base parameter to move the range of Single Mode keys to a different octave on the keyboard.
-
Change the Pitch parameter to change the note that is played in Single Mode
-
Key Remote Enabling this option allows MIDI control of both Note Repeat rate (as in Single Mode), as well as the active state of
Note Repeat, Note Erase, Gate times, Single Mode, Quantizing, and Aftertouch.
-
Change the Base parameter to move the starting note of the Key Remote control key range to a different octave.
-
Change the Range parameter to expand or contract the range of keys used to control in Key Remote mode. The larger
the Range, the more controls can be accessed via MIDI.
Note: While a range of keys is reserved for control of Note Repeat when in Key Remote mode, the rest of the MIDI controller's notes are
free to change the pitch of the repeated notes. This allows radical changes in Note Repeat behavior to be made with one hand as single
notes and chords are specified with the other.
Look at the keyboard display in the Note Repeat options window to see the control assignments for each note in the designated set of
keys for Key Remote mode.
Note Erase
If Note Erase is selected in the Record panel, any notes played during the current recording pass erase existing notes of the same note
value. For instance, if you start recording a drum pattern, and the kick pattern is on C1 and has an extra eighth-note hit on beat four, you
could switch to Note Erase while recording and play C1 on beat 4 for one eighth-note, and that would erase the previously recorded note.
It is only possible to engage this mode if Record Mix is engaged and Note Repeat is disengaged; engaging Record Takes or Note Repeat
disables this mode.

## Step Record

Step Recording is a special, note-by-note method of recording musical note data. Rather than playing in real time, or drawing in notes
with the Paint tool, you can simply specify a rhythmic value and press keys on your MIDI controller to enter notes and chords with ease
and precision.
Step Record Toolbar
To access Step Record mode, click to select the Instrument Track you wish to record to, open the Editor by clicking the [Edit] button, then
click the [Step] button in the Editor toolbar to display the Step Record toolbar. When you're finished, you can hide the Step Record con-
trols by clicking the [Step] button again.
The Step Record toolbar contains the following controls:
-
Enable Toggle this on to enter Step Record mode. When enabled, playing notes on the keyboard adds notes and chords to the
currently-selected Instrument Part. Toggle Enable off to exit Step Record mode.
-
Follow Q Enable this to link the Step Length setting to the current Quantize setting. If you change the Quantize value, the Step
Length value changes to match it.
-
Step Length With these selectors, you can choose a Step note length between whole notes and 64th notes, in the following
musical note groupings: Straight, Triplet (3 notes in the space of 2), Quintuplet (5 notes in the space of 4), Septuplet (7 notes in
the space of 8), or Dotted (notes are increased in length by 50% from the chosen rhythmic value).
-
Back Click this button to erase the most recently added note or chord and move the cursor back to where that note or chord star-
ted. Press Back multiple times to erase multiple notes.
-
Rest Click this button to move the cursor forward in time, according to the currently selected Step Length, in effect, creating a
musical rest for that step.
Recording in Step Mode
To record a Part in Step Mode, follow these steps:

## Step Record

1.
Place the cursor at the point within the chosen Instrument Track that you wish to record to.
2.
Open the Step Record toolbar by pressing the [Step] button in the Editor toolbar.
3.
Press [Enable] to enable Step Recording.
4.
Choose a rhythmic value from the Step Length selectors. You can change this value at any time as you create the Part.
5.
Play a note on a connected MIDI controller to create a note with the specified length at the cursor location. When you release the
note, the cursor moves ahead according to the Step Length setting, and you're ready to enter the next note. If you wish to enter a
chord, simply play and hold the notes that make up the chord, then release.
6.
When you're finished, press [Enable] again, to exit Step Record mode.

## Track Layers

In Studio One, both audio and instrument Tracks have optional layers that can be used to record multiple different ideas to a single Track.
For instance, you might want to compare one set of lyrics for a vocal Track to another set of lyrics. In this case, you could record two dif-
ferent performances to two separate layers on a single Track and quickly switch between the two without needing a second Track.
To create a new layer on any Track, [Right]/[Ctrl]-click the Track's control area in the Arrange view, and choose Add Layer from the Lay-
ers menu. Another way is to open the Inspector by pressing [F4] on the keyboard, then selecting Add Layer from the Layer selection box.
The new layer is effectively like having a whole new Track without duplicating Inserts, Sends, and I/O setup. You can also duplicate lay-
ers by selecting Duplicate Layer from the Layer selection box, which enables you to try out and compare two different edits of the same
Events on two layers.
To remove a Track Layer, [Left]-click to select the Layer at the Track header (not on the Layer Event itself) and then [Right]/[Ctrl]-click
and choose Remove Layer from the contextual menu. You can also group-select several layers via [Shift+Left]-click, and choose
Remove Selected Layers from the contextual menu to delete several layers at a time.
Note that you cannot group select (or group Remove) multiple layers across multiple Tracks. One track at a time.
Unpack Layers to Tracks
You may wish to have several layers unpacked into normal Tracks from time to time, which will grant full mixer control of pan, level, etc.
to each Layer.
You can do it in three clicks. [Left]-click to select the desired track; [Right]-click to bring up the contextual menu; then choose “Unpack
Layer to Track.” You can also group-select and unpack selected Layers only using [Shift-Left click] followed by choosing or “Unpack
Selected Layers to Tracks” from the contextual menu. Alternatively, holding Option/Alt while dragging a Layer will allow you to convert it
into a Track.
Combine this feature with Loop Record and Record Takes to Layers for a quick and powerful way to stack vocal parts!
There are several ways to switch between layers:
-
Click the arrow between the Track name and the layer name in the Track control area, then select the desired layer from the
pop-up menu. After this you can use the 4-way navigation arrows on your keyboard to switch quickly between the layers.
-
Click the Expand Layers button on the left side of the Track control area (
), then click one of the Activate Layer buttons to
make that layer the active layer for the Track. This swaps the two layers and keeps the previous Track contents as an alternate
layer.
-
Press [F4] to open the Inspector, click the Layers field, and select the desired layer from the pop-up menu.
Layers are also used in the comping system of Studio One, as described in the Comping section of the Editing chapter of this manual.
Audio Recording Format
Studio One records in the Broadcast Wave file format. This is the only format supported, as it is the most widely used format, and it con-
tains timestamps that mark when recordings start within a Song. When recorded Broadcast Wave audio files get bigger than 4 GB, the
RF64 file format is automatically used as the standard file format.
The recommended file system for the recording partition on your computer is NTFS for Windows and APFS for macOS.
Creating a Good Monitor Mix
When recording any performance in the studio, take the time to build a great monitor mix for the performers. It’s critical that they clearly
hear their performance and that of the other musicians, and a good monitor mix helps inspire a better performance. Ideally, each per-
former should feel like they are playing on a finished record.

## Track Layers

For instance, it is common in many styles of music for the lead vocals to have some reverb so that they sit well in the space of the overall
mix. Therefore, when recording vocals, it is sometimes a good idea to include reverb in the vocalist’s monitor mix. This way, the vocal will
sound more like a finished production. This approach often helps when recording guitars, keyboards, and other instruments, as well.
If your audio device supports zero-latency hardware monitoring, use that as the primary monitor source, so that no delay is heard. In addi-
tion, you can use Sends and FX Channels in the Console, as you normally would in a mix, to build a better monitor sound. For instance,
on the audio Track to which you are recording, you could add a Send to an FX Channel with a reverb. You could then route the FX Chan-
nel Output to a Sub Out Channel and back to your audio interface, where it can be mixed with the zero-latency dry signal.
When adding time-based effects, such as reverb or delay, you generally don’t have to be concerned about plug-in delay and latency that
could result from using software plug-ins on a live input source. A few milliseconds of processing delay on a reverb will probably not be
audible.

## Cue Mixes and Low-Latency Monitoring

Studio One features a powerful Native Low-Latency Monitoring system that provides low-latency monitoring for audio recording and
virtual instruments, without compromises in system performance. Hardware Low-Latency Monitoring is also available when using a com-
patible DSP-enabled audio interface. In this section, we will discuss how to take advantage of these features to create low-latency cue
mixes for monitoring while recording or composing.
Creating a Cue Mix Output
In Studio One, it is possible to quickly and easily create multiple cue mixes. A cue mix is separate from the main mix and is usually
provided to musicians for monitoring purposes during recording.
For instance, when recording vocals, the engineer and vocalist often need to hear different mixes. Many vocalists want to hear their vocal
boosted in the mix, possibly with some reverb to make it sound natural, while the engineer might want to focus on how the performance
balances with the rest of the mix. The cue mix functionality in Studio One makes this task easy.
The first step in building a cue mix is to create an additional Output Channel. To do this, open the Song/Song Setup/Audio I/O Setup win-
dow in a Song, switch to the Outputs tab, and add a new Stereo Output Channel. Next, specify that this output is a Cue Mix output by
clicking on the Channel’s Cue Mix checkbox. You can create as many cue mixes as your audio interface has available stereo outputs.

## Cue Mixes and Low-Latency Monitoring

Now that you have created a Cue Mix output, you can see special Send objects (called Cue Mix objects) in the Channels of the Console.
In the Small Console view, Cue Mix objects appear in the right column when a Channel is expanded. In the Large Console view, Cue Mix
objects appear below the Send Device Rack on each applicable Channel.
Each Cue Mix object features an Activate button, horizontal level and pan faders, and a Lock to Channel button.
The “Cue mix mute follows channel option" has to be engaged in the preferences in order to use Cue Mixes for FX Channels.
Mixing the Cue Mix
Cue mixes are built using Cue Mix objects. By default, the level and pan values are locked to the channel level and pan faders. This
means that each Cue Mix is identical to the main mix in the Console. Changing the level or pan in the Cue Mix object unlocks both set-
tings, allowing independent control of level and pan for each Channel in each Cue Mix. Thus, the level and pan for Channels in a Cue Mix
can be completely different from the related level and pan in the main mix.
At any time, you can toggle the lock state of the Cue Mix level and pan back to the Channel settings by clicking on the Lock to Channel
button. (The lock icon.) To completely remove any Channel from a cue mix, simply deactivate the Cue Mix object for that Channel.

## Cue Mixes and Low-Latency Monitoring

Double-clicking the Cue Mix object will bring up a larger pop-up interface for fine adjustments.
These pop-ups display The Cue Mixes for the currently-selected channel. With the left/right arrow keys you can navigate to the Cue
Mixes of other channels across the console.
Monitoring Live Input in a Cue Mix
Cue mixes are normally used in a recording situation in which one or more live inputs need to be monitored. This is where the Cue Mix
feature in Studio One is very useful. Monitoring with very low latency can be achieved using the Native Low-Latency Monitoring sys-
tem in Studio One.
You can also achieve low-latency cue mixes by using Hardware Low-Latency Monitoring with a compatible audio interface that
provides that feature, such as a PreSonus Studio 192, Studio 1810, or Studio 1824 interface. These interfaces feature internal hardware
mixers that provide low-latency monitoring. While these mixers are easy to use, Studio One makes it even easier by allowing you to con-
trol the mixers from within the software.
Let’s return to our example of recording live vocals. For a vocalist to be comfortable and perform well, it is important that the performance
sound as natural and as polished as possible. Vocalists need to hear themselves well, with no audible delay of their voices in the mix.
Adding some reverb provides a little ambiance so the voice is not dry and lifeless.
Here’s how this scenario would look in Studio One:
1.
Set up a Cue Mix output for the vocalist.
2.
Record-enable and monitor-enable the vocal Track.
3.
Engage the Enable Low-Latency Monitoring (or "Z") button below the level fader on the Cue Mix output being used by the vocal
channel. This enables Native or Hardware Low-Latency Monitoring for that Cue Mix output (depending on what is in use).
-
Note: Channels that are able to be monitored using Native or Hardware Low-Latency Monitoring display a "Z" mark at
the bottom of their channel strip.
4.
Create a Send on the vocal channel to an FX Channel with your favorite reverb effect.
5.
The vocalist hears the live low-latency input, as well as the rest of the cue mix, including the output of the reverb. Adjust the level
of the vocal and other Channels in the Cue Mix to the vocalist’s liking, and you’re ready to record.
In a few seconds, you can ensure that vocalists hear their voices with low latency, in a custom mix that includes effects. Simultaneously,
you can listen to a completely independent main mix, allowing you to focus on engineering while the artist focuses on the performance.
Note that when monitoring with Hardware Low-Latency Monitoring engaged, you do not hear Insert FX on that channel, as you are mon-
itoring the signal before it is processed in software. If you need to hear Insert FX, use Native Low-Latency Monitoring instead. To do this,
navigate to Studio One/Options/Audio Setup/Processing (macOS: Preferences/Audio Setup/Processing) and enable the "Use native low
latency monitoring instead of hardware monitoring" option.
Low-Latency Monitoring on the Main Output
The Main output always acts as a Cue Mix, and any Audio or Instrument Channels routed to it can be monitored using Native or Hard-
ware Low-Latency Monitoring (if enabled). To engage Native or Hardware Low-Latency Monitoring for the Main output, enable the
"Enable Low-Latency Monitoring" (or "Z") button, found below its volume fader. When enabled, the "Z" button is green (when using Nat-
ive Low-Latency Monitoring) or blue (when using Hardware Low-Latency Monitoring).

## Cue Mixes and Low-Latency Monitoring

## Print Effects While Recording

Some people prefer to place Insert effects on Input Channels so that those effects may be printed to the Track while recording. For
instance, you might place a compressor, EQ, or other effect on a vocal Input Channel in order to save time and computer resources later,
when mixing. This is easy to accomplish in Studio One. It may be helpful to review the Mixing chapter in order to better understand these
instructions.
To insert an effect on an Input Channel, open the Console and click on the Inputs tab on the far left to view the Input Channels. If you’re
working in the Small Console view, double-click on the Input Channel to open its Insert Device Rack.
Insert an effect in the Insert Device Rack on any of the Input Channels, and those effects are recorded at the input of any Track that uses
that source. Studio One automatically compensates for any latency caused by the Insert effects.
Note that when Insert effects are used on Input Channels, and effects are recorded to a Track, there is no way to go back and change the
sound of the recording. To avoid this scenario, you might consider placing effects on the Audio Channels to which you are recording for
monitoring purposes only and printing with effects at mixdown.

## Print Effects While Recording
