# Fundamentals

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 43–62
> **Slug:** `04-fundamentals`

**Agent topics:** `undo`, `retrospective recording`, `mix engine`, `delay compensation`, `dropout protection`, `transport`, `key commands`, `smart templates`, `Control Link`, `performance monitor`, `note repeat`, `video player`

---

Fundamentals
The following chapter presents important, fundamental design aspects of Studio One. Familiarity with these aspects of Studio One helps
to ensure that your experience is as enjoyable and creatively stimulating as possible.

## Nondestructive Editing and Undo/Redo

Almost every editing and mixing action in Studio One can be undone and redone. There is no limit to how far back actions can be undone
and to how far forward actions can be redone once they have been undone. Most actions that cannot be undone or redone are accom-
panied by verification dialog boxes.
So, feel free to explore without fear that you might permanently alter anything. In fact, playing freely with the controls is a fast way to
learn, and it often leads to unexpected results.
Undo/redo history is cleared when you close a Song, Project, or Show, or exit Studio One.

## Retrospective Recording

We've all had this experience as musicians: Sometimes we perform our best takes or have a phenomenal idea, and then realize we
weren't actually recording. With Retrospective Recording you will never miss another great song idea again!
Retrospective Recording captures every note you play on your MIDI keyboard or controller...even without hitting Record. Even when the
transport is stopped! It works invisibly in the background on a track-by-track basis. Controller activity is captured as well. The moment
something brilliant happens, all you have to do is press [Shift]+[NumPad*] and the last performance will turn into an Instrument Part on
the respective Track.
Fundamentals

It's already active.
The Retrospective Recording feature is enabled by default. If you want to disable it, navigate to Studio OneOption-
s/Advanced/MIDI/Enable retrospective recording (macOS: Preferences/Advanced/MIDI/Enable retrospective recording) and uncheck
the option box.
Play vs. stop
Here's how it works. Studio One maintains an independent buffer for each Track. When a Track is record-armed or monitored, Ret-
rospective Recording captures all notes, controller and parameter changes, whether the transport is playing or stopped.
-
Transport playing (but not recording): Captured events are stored with the correct Song location and Input Quantize is applied
(if that feature is active).
-
Transport stopped: Captured events are stored with times relative to each other.
Note that the buffer does not combine the events that are captured while the transport is playing with events that are captured while the
transport is stopped. As soon as an event is received in one mode, the other mode will always delete the contents of the buffer.
Recalling captured events
When the buffer was captured in play and is recalled, the events are placed with the correct song position on the Track. When the events
are captured while the transport is stopped and then the events are recalled, they are placed on the Track starting with the first event at
the playback cursor position.

## Retrospective Recording

Recalled events are added to the Track using the same options as the standard recording process (Replace, Takes to Layers, Record
Takes, Record Mix, etc.).
The buffer can be recalled in several ways:
-
The default key command [Shift]+[NumPad*] recalls the buffer to the selected Track.
-
[Right]/[Ctrl]-click on the Track control area and select "Recall Retrospective Recording" from the contextual menu.
-
Click the Retrospective Recording button in the Inspector.
Note that the command "Recall Retrospective Recording" can be assigned to a different keyboard shortcut if you like. To learn more, see
 Mapping Custom Key Commands .
Undo
If something unexpected happens when the events are recalled, such as the playback cursor is in the wrong position, the recall com-
mand can be undone (and redone) just like any other command.
Here's another example. Let's say the record mode was not correct when the events were recalled; you recalled the buffer when the
record mode set to Replace, but you wanted it set to Record Mix. The undo functionality removes the events from the Track again and
places them back in the buffer. Now you can change the recording option and recall them again using the new setting. Remember, if the
buffer receives any new event after 'undo' the buffer is deleted.

## Documents

Studio One can create and work with three types of documents: Songs, Shows, and Projects. Each Page of Studio One is dedicated to
one of these document types:
-
Songs are for music and audio creation and production. Recording, editing, arranging, and mixing all take place here. Non-
musical work like podcasts and dialogue editing can be done in the Song page as well.
-
Shows are for live performances and rehearsals, letting you use Studio One as a performance tool. Shows provide functionality
for Backing Tracks, Instrument Players, Setlists, and Performance View.
-
Projects are for mastering and releasing a collection of Songs. Projects allow for track sequencing, advanced metering, online
publishing, CD burning, and more.
Songs, Shows, and Projects are all created from the New Document menu, which allows you to create a new document from scratch or
select one of several Smart Templates. Smart Templates optimize Studio One’s configuration for a specific tasks like beat production,
live performance, rehearsal, and more, while also offering helpful step-by-step guides.
Songs, Shows, and Projects are interactive with one another. Songs can be sent to both Shows and Projects using the Song >> Add to
Show or Song >> Add to Project commands from the drop-down menu. Songs that have been changed after being loaded into Projects
can be updated via the “Update Mastering File” command.
Creating a New Document
To create a new document, do one of the following:
-
From the Start page, click on the New... button [+].
-
Navigate to File/New….
-
Press [Ctrl]/[Cmd]+N on the keyboard.
The New Document window appears:

## Documents

From here, you can create a new Song, Show, or Project, in a few different ways. You can use an empty template, a guided Smart Tem-
plate that optimizes Studio One to your intended task, or a custom User template of your own creation.
More detailed instructions can be found in specific topics as follows:
-

## Creating a New Song

-
Show Management
-

## Creating a New Project

-

## Smart Templates

## High-Precision Mix Engine

Studio One features a cutting-edge high-precision mix engine. A mix engine is the “number cruncher” that does the mathematical sum-
ming required to mix multiple sources of digital audio. Studio One employs a floating point, mixed-mode engine.
64-Bit Mix Engine
Studio One Professional offers both 32-bit and 64-bit mix engine modes. This means that the audio engine can automatically switch
between using 32-bit, single-precision floating-point and 64-bit, double-precision floating-point math on the fly, depending on the cap-
ability of the plug-ins (VST/AU effects, etc.) inserted into the signal chain.
In Studio One/Options/Audio Setup (macOS: Preferences/Audio Setup), set Process Precision to Double (64-bit) to activate 64-bit pro-
cessing. Otherwise, all processing is done in single precision (32-bit).

## Automatic Delay Compensation

Studio One automatically compensates for the time delay that results from some VST and AU processing. This lets you avoid having to
manually realign Tracks to compensate for that delay, and keeps all Tracks perfectly in sync regardless of the number of virtual plug-ins
and effects you run. For more information on this topic, refer to the Automatic Plug-In Delay Compensation section.

## High-Precision Mix Engine

## Audio Dropout Protection

When using a DAW, working with high track and plug-in counts can be challenging. Squeezing the highest performance from your com-
puter generally requires the use of high buffer settings, which can dramatically increase the amount of latency (or delay) you experience
when monitoring audio inputs or playing software instruments. Set the buffer too low, and audio playback can be compromised.
Audio interfaces that employ hardware DSP (such as the PreSonus Studio 192) can provide low-latency audio input monitoring at high
buffer settings. However, they are not able to help keep virtual instruments free of disruptive latency, as those instruments must run
within the DAW's native audio engine.
Next-Level Performance with Low Latency
Studio One now features an improved audio monitoring engine that can provide dropout-free audio playback and Native Low Latency
Monitoring monitoring for audio inputs and virtual instruments, even as track and plug-in counts push the limits of your system.
For more information on working with and configuring the new audio engine, see Audio Dropout Protection and Low-Latency Mon-
itoring.
MIDI—and beyond MIDI.
Studio One works with all the standard MIDI gear you know and love, from controllers to tone modules. But once MIDI data arrives into
Studio One, it’s converted to a high-resolution, 32-bit internal format. That means no zipper noise on instruments, smoother controller
changes and pitch bends, more detailed automation, and other benefits when working in the Studio One environment.
And if you need to drive external MIDI gear, you’re covered there too—Studio One translates its high-resolution format back into stand-
ard MIDI data if it needs to return to the outside world.
Drag-and-Drop
Many functions in Studio One have integrated drag-and-drop support. This means that objects can be clicked on and then dragged to
various locations, and over other objects, in order to accomplish certain tasks. For example, you can find an audio effect in the Browser,
and then click-and-drag it directly onto a Track to insert the effect onto that Track. You can then click-and-drag that effect onto another
Track to copy that effect and its settings to a new Track.
You can drag a virtual instrument from the Browser and drop it into blank space in the Arrange view to create a new Instrument Track with
that virtual instrument. You can also drop the virtual instrument on top of an Instrument Track to replace the existing virtual instrument.
If, while in mid-drag, you decide you no longer want to drag the object in question, press [Esc] on the keyboard to cancel the drag action.
These, and many other drag-and-drop features, allow you to work very quickly, without having to stop for menu navigation or other dis-
tracting processes.

## Transport Controls

The Transport Controls are a central set of buttons that give you control over playback, navigation, and recording in Studio One. Trans-
port Controls are present in the Song, Project and Show pages.
The following controls are available:
-
Play Start playback at the current cursor location. You can also Play by hitting the spacebar on your keyboard, which also works
to stop the transport, when it is in playback.
-
Stop Stop playback. You can also Stop by hitting the spacebar on your keyboard, or [0] on the numerical keypad.
-
Record Begin recording at the current cursor location. You can also activate recording by pressing [*] on the numeric keypad.
-
Loop Press to enable/disable Loop mode. You can also toggle looping by pressing [/] on your keyboard.
-
Rewind and Fast Forward Press these buttons to move the cursor back or forward in time.
-
Go To Previous/Next Marker Press these buttons to shuttle to the previous or next marker on the Marker Track.
-
Return to Zero (RTZ) Return the playback cursor to the beginning of the timeline. You can also zero the transport by pressing
[,] on the keyboard.

## Audio Dropout Protection

## Key Commands

Many operations in Studio One have associated key commands, or keyboard shortcuts, that can be used in lieu of navigating menus with
the mouse. Some key commands use modifier keys, and some modifier keys differ depending on the operating system.
In this manual, key commands with modifier keys are shown with the Windows modifier key first, as follows: [Win modifier key]/[Mac mod-
ifier key]+[key]. For example: [Ctrl]/[Cmd]+[C] means “press [Ctrl]+C in Windows, or press [Cmd]+C in macOS.”
Where there is no difference between the Windows and Mac version of a key command, only one key command is displayed. Example:
[F3].
In several instances, options are located in the Studio One menu in the Windows version but in Preferences in the macOS version. In
these cases, the Windows location is given first, and the Mac location follows in [brackets].
Some key commands open a window that helps locate or recall a specific item by typing a portion of its name or the item number. When
several items begin with similar letters, the up and down arrow keys can be used to scroll through the results. Examples:
-
[Ctrl]+[Alt]/[Option]+[C] to locate a Console Channel
-
[Ctrl]+[Alt]/[Option]+[T] to locate a Track
-
[Ctrl]+[Alt]/[Option]+[S] to recall a Scene
A complete list of key commands is always available via Help/Keyboard Shortcuts, which renders an HTML document and opens it in
your browser with the currently configured key commands.
Find Command
You can also use the “Find Command” feature to search for any command by name and quickly learn its keyboard shortcut. Pressing
[Ctrl]+[K] and type in the name of the Command you’re interested in or a related keyword like Track, Event, etc.
Key Commands for Migrating Users
If you are migrating from another DAW to Studio One, you might find it helpful to switch the key command set to one specifically created
to make the transition from another DAW easier.
In the Studio One/Options/General/Keyboard Shortcuts (macOS: Preferences/General/Keyboard Shortcuts) menu, you can see a head-
ing called Keyboard Mapping Scheme. Here, you can select from keyboard maps for several DAWs; select a map, and Studio One recog-
nizes and applies common key commands from that DAW. You can then customize the key commands to fit your workflow.
The key commands used for each DAW can be viewed in the Key Command menu and can be exported in several file types for external
viewing.
Mapping Custom Key Commands
In the Studio One/Options/General/Keyboard Shortcuts menu (macOS: Preferences/General/Keyboard Shortcuts), you can modify the
existing key commands to be anything you like, as well as adding commands for functions that don’t have default key commands.
Note that all mentions of keyboard shortcuts in this manual refer to the standard settings.

## Key Commands

To modify any key command:
1.
Find the function for which you wish to edit the key command by typing in the name of the function in the Search field.
2.
When the function is found, select it by clicking on it in the list on the left.
3.
Click in the Enter Key field and input any key combination using your computer keyboard. Your key combination is displayed.
4.
Click Assign to assign this key command to the selected function.
5.
If the key command you are trying to assign is already in use, the current use is displayed below the Enter Key field, along with a
Show link that selects that function for you so that you can change it.
6.
Click on the Keyboard Mapping Scheme selection box to choose from the following options:
-
Import Select to import a Studio One Keyboard Mapping Scheme.
-
Export Select to export your Studio One Keyboard Mapping Scheme.
-
Export as Text Select this to export your Studio One Keyboard Mapping Scheme as a text file so that you can create a
reference guide to your custom mappings.
A complete list of key commands can be viewed via Help/Keyboard Shortcuts, which renders an HTML document that shows the cur-
rently configured key commands and opens the document in your browser.
Studio One Help and Information
We have worked to make Studio One as easy to learn and use as possible, but any tool with as many capabilities as a modern DAW is
bound to come with a learning curve. To help you on your way, this manual contains information about every feature in Studio One. You
can access this manual at any time by navigating to Help/Studio One Reference Manual or by pressing the F1 key on your keyboard.
Studio One Help and Information

If you have one of the built-in Studio One plug-ins open and need help with its functions, pressing F1 takes you to the relevant section of
this manual.
Info View
The Info View panel, accessed via the Question Mark icon in the top toolbar on the Song , Project and Show pages, displays all possible
actions for the selected mouse tool, as well as showing the possible modifiers and their related actions. Various controls in the Studio
One interface and included plug-ins also display information in the Info View when you hover the mouse pointer over them. From Info
View, you can press F1 on your keyboard to jump directly to related sections of the Studio One reference manual.
Tooltips
Many controls, tools, and windows in Studio One have associated tooltips that display when you hover your mouse pointer over the con-
trol. These short descriptions can help you quickly orient yourself to the functions available in Studio One.
View Options
Studio One’s core design philosophy is about helping you create while remaining unobtrusive. As such, we’ve made its View settings
highly configurable so that you aren’t distracted by elements you choose not to use, and only see them when you want to. Check the
View drop-down menu for a full list of options. From there, you can even store and recall favored Zoom settings, Reset Window Pos-
itions, and more. Activate Fullscreen at any time from this menu, or by pressing [Shift-F].
PreSonus.com
Our website, http://presonus.com, contains a wealth of information about Studio One and how best to use it. You can also get inform-
ation and answers from fellow users at our forums at http://forums.presonus.com/
Studio One Help and Information

## Smart Templates

What do you want to do today?
Smart Templates are designed to help you create in Studio One as efficiently and immediately as possible. They’re optimized for specific
tasks like Beat Production, Rehearsal, or live performance, and include Track Presets, File Import, optional Customization, and Tutorials
to aid you in Song setup. Smart Templates will also download and install any additional required content that you may not have installed
already.
You’ll find Smart Templates on the left side of the New Document menu, below Record and Mix; Master and Release; and Rehearse and
Perform.
Play Now
Choose this Smart Template to connect a guitar or MIDI controller and make some music right away.
-
Drums Creates a new Song for use with a MIDI drum kit, this Smart Template loads an instance of Impact XT for your drum
sounds.
-
Guitar Creates a new Song for use with an electric guitar, this Smart Template loads an instance of Ampire for creating your gui-
tar tone.
-
Piano Creates a new Song for use with a MIDI keyboard controller, this Smart Template loads an instance of Presence XT with
a lush piano sound.
-
Synth Creates a new Song for use with a MIDI keyboard controller, this Smart Template loads an instance of Mai Tai with a clas-
sic synthesizer sound.
Record Now
Record audio on single or multiple tracks and capture your ideas.

## Smart Templates

-
Full Band Creates a new Song with Tracks set up for lead vocals, two guitars, bass, keyboards, and multi-track drums in a
bussed Folder Track. There are separate FX Channels (with Sends applied) for Drum Room and Vocal Reverb; Ampire and Fat
Channel effects are applied to the appropriate Track Inserts.
-
Guitar and Vocal Creates a new Song with Tracks set up for two vocals, one guitar, and an instance of Impact XT for virtual
drums. There are separate FX Channels (with Sends applied) for Drum Room and Vocal Reverb; Ampire, De-Esser, and Fat
Channel effects are applied to the appropriate Track Inserts.
-
Single Track Creates a new Song with just a single empty Track and Input Channels visible.
Mix in Surround
Create a Song in multichannel or binaural format, including Dolby Atmos.
-
Dolby Atmos Choose this to create a Song in the Dolby Atmos configuration. Choose from the following sub-options:
-
Bed Format Choose the configuration of your traditionally-panned elements.
-
Monitoring Format Choose your speaker configuration. Choose the configuration that best matches the speaker array
in your studio.
-
Sample Rate Choose from 48 kHz or 96 kHz.
-
Surround Choose this to create a Song in Surround. You’ll be presented with the following options:
-
Output Format Choose the configuration that best matches the manner in which you want your music to be listened to.
You’ll need a matching speaker configuration in your studio.
-
Sample Rate Choose from 44.1 kHz to 192 kHz.
Produce Beats
Start building a beat from scratch with Patterns using virtual instruments for drums, bass, and chords.
Produce Beats creates a new Song with an instance of Impact XT, two instances of Mai Tai, an instance of Impact XT for drums, and twi
instances of Mai Tai - one for bass and another for chords and arpeggios. Impact XT and Mai Tai’s Note Events are set up as Patterns for
intuitive, beat-driven workflow suitable for hip-hop and EDM.
Create Content
Record and produce online content such as audiobooks, voice-over, and podcasts - with or without video.
Create Content Creates a new Song with three tracks: Music/FX, Voiceover 1, and Voiceover 2. Video Track is enabled and appropriate
dialogue processing is applied to the Voiceover Channel Inserts — plus a Room reverb FX Channel and Sends. Imported video and
music will be placed appropriately into Video Track and the Music/FX Track. If multiple videos are imported, they will be placed one after
the other.
Import Files
Import files by dragging them on the dropzone and start mixing. You can import various filetypes in whatever combination you like, includ-
ing but not limited to: audio files, MIDI files, AAF, Cubase Track Archives, and more.
Audio Interfaces
Record audio straight from all available inputs of your favorite PreSonus or Fender devices. Interface models are sorted within the “Inter-
face template” dropdown menu. If you own a PreSonus or Fender audio interface, choose it from this list to create a new Song with all of
the inputs and outputs mapped appropriately for the chosen interface. To access Fender Device templates, select the Fender tab next to
the PreSonus tab.
Demos
Choose a Studio One Demo song to listen to, explore, reverse-engineer, and learn from!

## Smart Templates

Tutorials
Most Smart Templates, including Play Now, Record Now, Produce Beats, and Create Content include guided step-by-step Tutorials to
help you through Studio One fundamentals like Track arming, instrument/controller setup, and more.
Tutorials are started automatically if a Smart Template containing a Tutorial is launched. Some tutorial slides will dim the screen to draw
your attention to certain areas of focus. Navigate the Tutorials by clicking the navigation buttons or the arrow keys. Press [ESC] to exit a
Tutorial.
The Getting Started Tutorial
Getting Started Tutorial will display the first time you launch Studio One, and will guide you through the basics of the Start Page including
Artist Profile, Audio Interface setup, and adding External Devices. You can re-launch it at any time from the drop down menu: Help >>
Tutorials >> Getting Started.
New Song Options
For deeper understanding of the New Song options listed under Smart Templates that create a New Song, visit the New Song topic
here.
Apply Customization
Smart Templates leverage Studio One’s Customization feature, which enables or disables features to create optimized workspaces for
specific tasks. (A user working strictly in audio recording would not require loops or Patterns, for example.) Use this option to enable/dis-
able Customization changes.

## Customization

## Smart Templates

Song Information and Track Notes
As you record, mix, or master, you may need to take notes of something pertaining to the song or track you are working on. Studio One
makes this easy with the Song Information window.
One way to access the Song Information window is by clicking onto the Song tab from the menu bar. At the bottom of the drop-down
menu, click Song Information.
The Song Information window will appear, which includes a tab detailing general information about the track, the Song Notes tab, and the
Track Notes tab.
-
The Info tab includes Meta Information related to the song, including the artist name, album name, songwriter credits, year of
release, and other important information.
-
The Song Notes tab may be a good spot to draft promotional copy, make notes about the collaboration process, or provide
more information about the song’s origin or original inspiration(s).
-
The Track Notes tab is a great space for collaborators to detail track revisions, give directions, or leave feedback. Alternatively,
you may find it useful to leave notes for yourself between mixing sessions.
Clicking on any of the information within the Info tab will pull up the corresponding Song Setup window where you can edit the Meta
Information. You can also access this window by clicking onto the Song tab from the menu bar. From the drop-down menu, click Song
Setup. Alternatively, the preset quick command to open Meta Information is [Ctrl]/[Cmd]-[.].
To navigate directly to the Track Notes, right click onto any of the tracks within the Mix Console. From this drop-down menu, click Edit
Note. Notes can also be edited by clicking on the notepad icon ("Edit Note") in the Inspector channel.
You can easily add track and channel notes into Arrangement or Mix Console areas by customizing the display options. To do this, click
onto the wrench icon (“Options”) in either area. From the option drop-down menus, Track and Channel Notes can be enabled. When
enabled, each Track or Channel will have its own notepad where you can enter text.
Flexible Parameter Control
Many controls and parameters throughout Studio One let you adjust their settings with the mouse and keyboard in several useful ways:
Song Information and Track Notes

-
Scrollwheel Hover your mouse pointer over the desired control or parameter and move the scrollwheel (or other scrolling
mechanism) on your pointing device. In this way, you can smoothly adjust variable controls (such as mixer faders or plug-in para-
meters) and scroll quickly though lists of options (such as setting Quantize Value or channel I/O assignments).
-
Click and Drag While moving knobs and linear faders by clicking and dragging may seem obvious, also note that many numer-
ical settings (such as Transpose or Start and End times) can be adjusted by clicking the center of the setting's display, and drag-
ging up or down to the desired value.
-
Double-Click and Type Many numerical parameters can be precisely set by double-clicking the currently set value and typing
in the desired value. Press [Enter] to lock in the new value.
-
[Right]/[Ctrl]-Click and Type Many parameters of the instruments and effects included with Studio One can be automated or
assigned to a Macro. Select a control, use [Right]/[Ctrl]-Click to open the Automation/Channel Macro window, and note the
parameter name and value field. Values can be entered there: just double-click the value field, type in the desired value, and
press [Enter] to lock it in.

## Control Link

Controlling DAW software with hardware MIDI controllers can sometimes be a complex task. To make things simpler, Studio One
provides the Control Link system, a clear and easy MIDI mapping protocol. With minimal configuration, you can achieve effective control
over your software and external equipment.
For more on the Control Link System, refer to the Control Link chapter.
PreSonus Hardware Integration
Studio One offers integrated control for the following PreSonus audio hardware products:
-
StudioLive ARc-series mixers
-
StudioLive Series III Console Mixers
-
Quantum Series Interfaces
When you connect one of these supported units to Studio One, many of the hardware control features you know from the included Univer-
sal Control software are then available directly within Studio One.

## Control Link

Basic Setup Procedure
To connect your PreSonus Quantum-series interface or StudioLive mixer to Studio One, do the following:
1.
Connect your interface or mixer to the computer running Studio One, using the included data cable (USB or Thunderbolt).
2.
Install and launch the included Universal Control software on the computer running Studio One.
3.
Launch Studio One. The control features for your hardware are now enabled in Studio One.
For more detailed information about the setup process and Studio One hardware integration, see the owner's manual for your interface
or StudioLive mixer.
View Options
View Menu
Studio One’s core design philosophy is about helping you create while remaining unobtrusive. As such, we’ve made its View settings
highly configurable, so that you aren’t distracted by elements you choose not to use, and only see them when you want to.
Check the View drop-down menu for a full list of options. From here, you can even store and recall favored Zoom settings, Reset Window
Positions, and more. Additionally, views can be accessed via Studio One’s configurable Keyboard Shortcuts, which many power users
find to be the fastest, most efficient method of using Studio One.
Basic Studio One views like Pages, the Editor, the Console, etc. are located in the top two sections of this menu, and each are covered in
detail in their respective sections of this manual.
View Options

The third section of this menu pertains to Studio One’s Browser. Here you’ll find your Instruments, Effects, Loops, and more. The
Browser also has its own topic here.
The fourth section of this menu offers several Views useful to specific use cases:
Record Panel
The Record Panel offers control over several modes for recording to an Instrument Track, including Replace and Overdub, Record takes
to Layers, Input Quantize, and more. The Record Panel is covered in greater detail here.
Time Display
View Options

The floating, resizable Time Display View gives you an at-a-glance look at the current playback position of your Song. Supported units
include Seconds, Bars, Samples, and Frames, and can be configured by using the smaller Time Display to the left of the Transport Bar at
the bottom of Studio One.
Remaining Record Time
The floating, resizable Remaining Record Time View gives you a look at how much recording time is available, based on your current
track count, sampling rate, and available disk space.
Kindly note that “Remaining Record Time” is not a countdown to the expiration of your Studio One+ membership.
Chord Display
The floating, resizable Chord Display View presents several options for viewing Chords. Useful for easy sight-reading while practicing
your instrument of choice... particularly when used in conjunction with loop points!
This window has three options:
-
Chord Track displays the chord from the Chord Track at the current playback position, as well as the next upcoming
Chord (in blue.)
-
Input Chord displays the chord currently being played on an external keyboard
-
Editor mirrors the current/selected Chord display in the Note Editor inspector. When multiple tracks are visible in the
editor, all of them contribute to the chord displayed. When no instrument editor is open, it displays the chord of a cur-
rently selected instrument track at the current playback point.
Chord Track is covered in greater detail here.
View Options

MIDI Monitor
MIDI Monitor grants you filterable visibility to all MIDI data entering or leaving Studio One. It’s very useful for mapping external controllers
and instruments, as well as for troubleshooting devices that are not sending or receiving MIDI data as expected.
Mapping a controller with the help of MIDI Monitor is covered in greater detail here.

## Performance Monitor

The Performance Monitor displays the current total CPU and disk usage, as well as specific usage data for Insert effects and Instru-
ments. This is useful for determining which demanding Instrument Tracks may be worth rendering to Audio Events, for example. You’ve
also got control over Dropout Protection settings and Plug-in Nap from the Performance Monitor.
Performance Monitor is covered in greater detail in the Metering and Audio Device Setup topics.

## Performance Monitor

Dropout Protection
Dropout Protection allows you to select the right balance between processing power and latency for your current workflow. Generally
speaking, low latency is preferred for live tracking, so choose a lower setting for such applications; and higher buffer settings are prefer-
able for working with many virtual instruments simultaneously. Dropout Protection is covered in greater detail here.
Plug-in Nap
Plug-in Nap improves overall CPU performance and reduces the risk of audio dropouts by temporarily pausing the processing of plug-ins
that don’t pass audio at the current playback point. The status of each plug-in can be seen in the Performance Monitor (look for the cres-
cent icon in the in CPU display). Plug-ins of your choice can be selectively excepted from Plug-in Nap—handy for isolating any plug-ins
that are giving you trouble. Click the tickboxes on the right of Performance Monitor to select the desired plug-ins; note that this option dis-
ables Plug-in Nap’s influence on the plug-in and does not disable the plug-in itself.
Note that the maximum number of simultaneously processed plug-ins will still be limited by the available CPU power. Plug-in Nap is also
available in the Audio Setup menu.
If you are experiencing issues with some of your plug-ins and want to disable them altogether, you can do this from the Plug-in Manager.
Plug-in Nap can also be selectively enabled/disabled on a per Plug-in from the Plug-in Editor drop-down menu, the Rack Slot Menu in the
Console, or from the right-click contextual menu in the Browser.
Plug-in Manager
Plug-in Manager allows you to search, view, sort, remove, block, and show/hide your plug-ins from a single window. You can also check
your plug-in versions here. You can also reset the Blocklist for any plug-ins that failed Studio One’s plug-in scan, and you can even manu-
ally add a plug-in to the Blocklist by dragging and dropping it from Studio One’s Browser. Right-clicking on any plug-in will allow you to
open it in your OS’s Finder/Browser.
Click “Update Plug-in List” to refresh the list for any new plug-ins you may have installed while Studio One is open.
The Statistics Tab provides useful information concerning frequency of plug-in use, and each plug-ins affect on load times, save times,
and average preset size.
Plug-in Manager is discussed in greater detail here.

## Performance Monitor

## Note Repeat

Note Repeat is a tool that allows you to produce several selectably quantized notes from a single key press of your MIDI controller.
Note Repeat is highly configurable, and can be controlled extensively using MIDI, which unlocks a wealth of real-time creative options.
Not to be confused with Repeater.
Note Repeat is covered in greater detail here.

## Video Player

Video Player allows you to play a video in sync with Studio One. Ideal for scoring video/film productions. You can even extract audio from
your imported video clip to mix.
Video Player is covered in greater detail in its own topic here.

## Note Repeat

Additional Views:
-
Info View Use this View to display a context-sensitive window at the top of Studio One that contains useful feature descriptions
as well as tips for using the modifier keys (Shift, Control, etc.)
-
Audio Bend Use this View to display the Audio Bend menu at the top of Studio One.
-
Strip Silence Use this View to display the Strip Silence menu at the top of Studio One.
-
Quantize Use this View to display the Quantize menu at the top of Studio One.
-
Macros Use these Views to display your Macros in several places: the Arrangement Window, Note Editor, or Audio Editor.
Read more about powerful Macros here!
-
Chord Selector Use this option to toggle visibility of the Chord Selector.
Windows:
-
Toggle Floating Windows Use this option to toggle visibility of floating windows like your plug-ins.
-
Toggle Optional Views Use this option to toggle optional views like the Browser, Console, or Edit Windows on and off.
-
Toggle Detached Console Use this option to detach the console and relocate it wherever you like. Useful if you use multiple
monitors.
-
Toggle Detached Editor Use this option to toggle detachment of the Editor Window.
-
Fullscreen Use this option to run Studio One in Fullscreen mode. [Shift+F].
-
Reset Window Positions Use this option to reset all windows to their default positions. Useful for when complex projects get a
little too busy, or when a document was saved on a different computer with a larger monitor setup and windows are positioned
outside of the visible range. This will fix the problem.
Zoom:
-
Zoom In/Out Use these options to Zoom the Edit Window in or out horizontally.
-
Zoom In/Out Vertical Use these options to Zoom the Edit Window in or out vertically.
-
Zoom to Loop Use this option to maximize the Zoom on your Loop points.
-
Zoom to Selection Use this option to Zoom the currently-selected Events to maximum vertically.
-
Zoom to Selection Horizontally Use this option to Zoom the currently-selected Events to maximum vertically.
-
Zoom Full Use this option to fit the entire contents of the Edit window.
-
Undo / Redo Zoom Use these options as dedicated Undo/Redo for your Zoom settings.
-
Toggle Zoom Use this option to alternate between your last two Zoom settings.
-
Store Zoom State Use this option to save your favored Zoom state for later use.
-
Restore Zoom State Use this option to recall your favored Zoom state.
Visibility
Undo Visibility Change and Redo Visibility Change. Visibility changes are not tracked by Studio One’s normal Undo/Redo func-
tionality, so a separate set of dedicated visibility undo/redo options are available.

## Video Player
