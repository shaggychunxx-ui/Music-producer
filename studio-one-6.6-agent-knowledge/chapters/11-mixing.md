# Mixing

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 268–320
> **Slug:** `11-mixing`

**Agent topics:** `console`, `routing`, `fader flip`, `channel editor`, `groups`, `scenes`, `VCA`, `listen bus`, `metering`, `marker track`, `mixdown`, `export stems`

---

Mixing
Mixing is the part of the production process where all recorded and arranged material is balanced in relative volume, frequency, and
dynamic content in order to achieve a desired cohesive sound.
The following chapter discusses basic aspects of mixing in Studio One, including the Console, the different types of Channels, and the
use of Inserts and Sends. Further information on mixing with Studio One can be found throughout this manual.

## The Console

Mixing in Studio One is primarily done in the Console. Open the Console by clicking on the [Mix] button or by pressing [F3] on the key-
board.
Each channel of audio in your Song is represented by a Channel in the Console. Audio Tracks in the Arrange view are directly rep-
resented by Audio Channels in the Console, whereas Instrument Tracks have no direct representation in the Console. Instead, Instru-
ment Channels represent the audio output of virtual instruments. There are several other Channel types discussed below, including
Input, Output, Bus, and FX Channels.
It is important to note that the Console opens by default in Large mode, and the following descriptions assume this mode is engaged
unless otherwise noted. For more on this topic, refer to the Alternative Console Layout section of this chapter.
Channel Features
The following features are common to all Channels.
Input/Output
At the top of each Channel is a display of its configured Input and Output, with the Input shown at the top and the Output below it. All
Channels are configured with Main Out as their Output by default.
Audio Channels show the hardware audio input selection. Instrument Channels display the name of the virtual instrument from which
they get their input. Bus and FX Channels display a graphical count of the number of Tracks assigned or sent to them, rather than a dis-
crete display of input channels, as their input source is usually from multiple Channels. Click on the Input area on a Bus or FX Channel to
display a pop-up list of all assigned/sent Tracks. Clicking on a Track in this list selects and expands that Track in the Mix view.
Click on any Input or Output to display and choose from a list of available routing options for any Channel. If several Channels are selec-
ted they can be assigned instantly to the same Input or Output by making a selection for any one of the selected Channels. It is also pos-
sible to assign all selected Inputs or Outputs in ascending order based on the audio hardware configuration.
Clicking on the Input for an Instrument Channel opens the interface for the source virtual instrument.
Mixing

Panner and Fader
All Channels feature a horizontal panner and vertical volume fader below the I/O-selection display. The panner can be clicked-and-
dragged horizontally, allowing the audio for each Channel to be positioned left or right in the stereo field.
Panning options
Right-click the panner to bring up the contextual menu of panning
options. You can choose from:
-
Balance - The default mode which allows you to position the
Channel’s signal left to right in the stereo image.
-
Dual - A stereo panner that allows for independent left/right pan-
ning.
-
Binaural - A stereo panner that employs mid/side processing to
manipulate the perceived width of stereo signals, from mono to
double the normal width.
Note that Dual and Binaural pans don’t apply to Mono channels.
Double-click the pan interface to pop up a larger panner interface
suitable for fine control over your pan adjustments. These popups
will display for the currently-selected channel when you press the
left/right arrow keys to navigate across the console.
Select “Use Binaural/Dual for New Channels” to set all new Chan-
nels to use your desired pan type.
The volume fader can be click-and-dragged vertically to control the output volume for each Channel. Volume and Pan can be edited on
multiple Channels simultaneously when Channels are Grouped. Numerical values may also be entered for pan and volume.
When using Dual Pan:
-
Click and drag on the middle of the interface to changes the joint balance of both panners. (Alternatively, use the mousewheel.)
-
Click and drag on an endpoint of the interface to balance a single side at a time.
-
Click and drag up or down to widen or narrow the stereo width. (Alternatively, CTRL+mousewheel.)
Note that you are able to drag the stereo width into the negative direction when crossing the zero-width point. This will be indicated by a
red color change in the interface.
When using Binaural Pan:

## The Console

-
Click and drag the panning interface left or right to adjust balance.
-
Click and drag the width control left or right to adjust width. Double-click the width control to enter the width value with the key-
board. Alternatively, mouseover the width control and adjust via the mousewheel.
More advanced stereo panning control can be had by using the Dual Pan and Binaural Pan plug-ins.
Volume and Pan settings
The volume fader can be click-and-dragged vertically to control the output volume for each Channel. Volume and Pan can be edited on
multiple Channels simultaneously when Channels are Grouped. Numerical values may also be entered for pan and volume.
Studio One uses a -3 dB pan law for all channel panning. On stereo Channels, the panner adjusts the balance of left and right signal
levels.
Mute/Solo
Solo mode is also known as Solo-in-Place, or SIP. Channels can be muted or soloed by clicking on their Mute and Solo buttons, respect-
ively. You can also press [M] for Mute or [S] for Solo on the keyboard to mute or solo selected Channels. Muting silences the Channel’s
audio from the Console so you won’t hear it. Soloing silences all except the audio for the soloed Channel, so you only hear the soloed
Channel. Any number of Channels can be muted or soloed at one time.
When using the [M] or [S] keys to mute or solo an Instrument Track that has a virtual instrument attached to it, mute or solo is applied to
the note data Track in the Arrangement view, rather than to the audio Track in the Mix view. [M] and [S] have no effect on Bus or FX Chan-
nels (see Solo Safe below).
You can perform a Global Solo Off, which disengages Solo on any Track that has it engaged, by pressing and holding [Ctrl] on the key-
board and then clicking on any Solo button. Performing the [Ctrl]-click again recalls the previous solo settings, returning any previously
soloed channels to the solo state. This can be useful when comparing a group of soloed Tracks to other Tracks in your mix.
Solo Safe
It is possible to place Console Channels in Solo Safe mode. When any Channel in the Console is soloed, all Channels with Solo Safe
engaged are also soloed, and all other Channels are muted. To engage Solo Safe on any Channel, [Shift]-click on its Solo button in the
Console. The Solo button is green when Solo Safe is engaged.
Note that FX Channels have Solo Safe engaged by default because effects may be critical to how soloed Channels sound in the mix.
Metering Mode
Each Channel has a level meter to provide a visual display of audio levels. Several metering modes are available: Peak, Peak/RMS, and
Pre-Fader Metering. To select the metering mode, [Right]/[Ctrl]-click inside the meter of any Channel.
Peak and Peak/RMS modes are described in the Metering section of this manual. They are mutually exclusive. Note that this selection
does not affect the metering mode of the Main Out or Sub Outs. Either mode can use Pre-Fader Metering.
Pre-Fader Metering is not enabled by default. When it is enabled, the level meters show levels independent of fader position. When it is
disabled, the level meters respond to fader position. This is known as Post-Fader Metering. The selection you make will be applied glob-
ally to all Channels including the Main Out and Sub Outs.

## The Console

Copy/Paste Channel Settings
It is possible to copy the settings of one Channel in the Console and paste them onto another Channel, or multiple channels sim-
ultaneously. This allows you to carry the level, panning, and insert/send effects between Channels in the current Song, the Channels of
other Songs, and even to the Channels on other pages (Song, Project, Show, etc.). Any Channel type can be a source or destination:
Audio, Instrument, Aux, Bus, VCA, or Master, with the exception of the Listen Bus.
This is as simple as using the normal copy/paste commands:
-
Click to select a Channel
-
Use [Ctrl]/[Cmd]+[C] to copy its settings
-
Select another Channel, (or group-select Channels using [Shift] or [Cmd]-click)
-
Use [Ctrl]/[Cmd]+[V] to paste the settings.
These commands are also available in the contextual menu: [Right]/[Ctrl]-click a Channel and you'll see those options near the top of the
list.
Automation Mode
The Automation mode for each Channel is displayed at the bottom of the Channel. By default, this mode is set to Off. Click on this display
to choose an Automation mode or to add and remove automation parameters.
Name
Channel names are shown at the bottom of each Channel in the Console. Double-click on the name, type a new name, and then press
Enter to change the name of any Channel.
To find a specific Channel, use [Ctrl]+[Alt]/[Option]+[C] to open a dialog box, then type the Channel name or number. This method works
whether the Console is visible or not.
Insert and Send Device Racks
Each Channel in the Console can have its own set of Device Racks. Audio, Instrument, FX, and Bus Channels include Insert and Send
Device Racks. Send Device Racks can be hidden or displayed: Open the Console options (the wrench-shaped button) and change the
setting of the Sends/Cue mix option inside Channel Components. Note that the Insert Device Racks are hidden in Small Console mode.
In Large Console mode the Insert and Send Device Racks can be sized vertically by clicking-and-dragging on the divider between them.
Hold [Shift] while dragging the divider to change the size of the Insert Rack for a single Channel. Double-click the divider to unify the
Insert Rack size for all Channels, or hold [Ctrl]/[Cmd] while dragging the divider.
In any Send Device Rack, all Sends can be removed simultaneously by choosing “remove all” from the Send Device’s drop-down menu.
This can be applied to several Channels at once when they are group-selected.

## The Console

Channel Types
Input
Input Channels represent the configured hardware audio inputs. They can be mono or stereo, depending on the configuration of the hard-
ware input they represent. Use the Input Channels to accurately meter inputs or to add effects processing to an input.
Audio
Audio Channels are direct representations of Audio Tracks in the Arrange view. Each Audio Track has a corresponding Audio Channel in
the Console, with corresponding Record Enable, Monitor Enable, Solo, and Mute controls.
Instrument
Instrument Tracks in the Arrange view have no directly corresponding Channels. An Instrument Track outputs to a virtual instrument, and
the virtual instrument then creates sound. Thus, virtual instruments output audio to Instrument Channels in the Console. A virtual instru-
ment might have any number of outputs, as described in the Set Up Multiple Virtual Instrument Outputs section of the Recording
chapter, and each has a corresponding Channel in the Console.
Aux
An Aux Channel allows an external audio source to be controlled by the Console without the need for an associated track. The incoming
audio can be processed by the native plug-in effects, and its volume can be controlled through the sample-accurate automation provided
by Studio One. For more information, see Set Up an Aux Channel.
Bus
The audio output of multiple Channels can be routed directly to a single Bus Channel. This lets you create a submix so that the audio
from several Channels can be processed together before being routed to the main output. Although less common, it is also possible to
use Sends to route audio to Bus Channels.
For instance, several drum Tracks might be routed to a Drum Bus, where the audio is compressed and equalized, and then routed to the
main output. That audio could also be routed to an FX Channel, through a Send, to apply a reverb effect, which would be applied to all
audio routed to that FX Channel.
From the source list of your Bus channel, you can select individual channels or click the “Select All” option to select all subordinate chan-
nels routed to the Bus Channel.
Bus Channels can be mono or stereo. Click the Channel Mode button in the Bus Channel to select the desired option.
FX
FX Channels are what are traditionally known as effects return channels, used to apply effects to multiple signals simultaneously through
the use of Sends. Audio can be routed from any Channel through a Send to an FX Channel, which can have any number of effects inser-
ted in its Insert Device Rack. For instance, several keyboard Tracks and a guitar Track could be routed via Sends to an FX Channel with
a reverb plug-in inserted, so that all of the instruments sound like they are in the same physical space.
Dragging an audio effect or FX Chain to the Send slot of a Channel in the Console creates a new FX Channel with the same name as the
effect or FX Chain, and routes audio from the original Channel to the new FX Channel, via a Send.
Output
Output Channels are routed directly to hardware audio outputs and can be stereo or mono, depending on the configured outputs to which
they connect. Every Song has at least one stereo Output Channel, which is named Main Out by default. The Main Out is, by default,
where the entire Console mix of all other Channels is routed. You generally listen to this output when monitoring your mix, as this is the
output from which exported mixdowns are derived.
The Main Out Channel is always locked to the far right end of the Console and cannot be moved. This output features a stereo Peak-
/RMS Meter, as well as K-System Metering. Other configured hardware outputs are represented in the Console by a type of Output
Channel called a Sub Out. Sub Outs appear to the right of the mixer when the Outputs panel is open.
The Main Out and Sub Out Channels feature Metronome controls, allowing independent metronome on/off and level control for each
hardware output. Note that every stereo Output Channel also features a Mono switch to allow for quick summed-mono monitoring, which
is commonly used to check a mix for mono compatibility.

## The Console

Console Options
Click the Options button (shaped like a wrench) to bring up a
menu with options that let you shape the behavior of the Con-
sole to suit your needs and organizational style. The following
options are available:
Grouping Options
-
Keep FX channels to the right Enable this to
cause all FX Channels to be placed together, at the
right end of the Console. This can aid in keeping
track of FX Channels in a large-scale Song.
-
Keep bus channels to the right Enable this to
cause all Bus Channels to be placed together, at the
right end of the Console. This can aid in keeping
track of Bus Channels in a large-scale Song.
-
Keep VCA channels to the right Enable this to
cause all VCA Channels to be placed together, at the
right end of the Console. This can aid in keeping
track of VCA Channels in a large-scale Song.
-
Preserve order of channels with folder track
Enable this to ensure that any Bus Channels that are
associated with a Folder Track remain next to the
Folder Track's enclosed Channels when the Keep
Bus Channels to the Right option is enabled.
Visibility Options
-
Link visibility of Track List and Console Enable
this to link the show/hide status of the Track List and
the Console. When you hide an item in the Track List
or Console, it is hidden in the other as well.
-
Link expansion and visibility of Folder Tracks
Enable this to hide Console Channels associated
with a Folder Track when the Folder Track is collapsed in the Arrange view.
-
Auto-expand Selected Channel When enabled, this option makes it easier to view expanded Channels in the Console one at
a time. Double-click the first Channel to expand it, and when the next Channel is selected, two things happen: The currently
selected channel auto-expands, and the previously selected channel collapses. If you hold [Alt]/[Option] and click the second
Channel, the previous Channel does not collapse.
-
Colorize Channel Strips Enable this option to apply channel color coding to full channel strips in the Console. Normally the
color only shows on the channel labels.
-
Colorize Plug-in Header Enable this option to apply channel color coding to the open editor window of a plug-in. This is handy
when the same plug-in is being used for several Console Channels (the PreSonus Compressor, for example).
Channel Components
-
Audio device controls This option can be accessed when a suitable PreSonus audio interface is connected. When this is the
case, enabling this option reveals controls on the right side of the Console that are specific to the PreSonus audio interface (e.g.,
Talk button routing and level, headphone options, speaker selection, etc.).
-
Input controls Enable this option to display the Input Gain and Polarity Invert controls at the top of each Channel in the Con-
sole. These are present for every Channel Type except Output Channels and VCA Channels. The controls are described in the
Inputs and Outputs section of this chapter.
-
Sends/Cue mix Use this option to show the Sends above the fader on each Channel in the Console. When enabled, click the +
sign to select an existing destination Channel, add a new one, or make a Sidechain connection. Prefader buttons and Send
Level controls are provided for each Channel.
-
I/O connections Enable this option to display Input / Output routings above the fader on each Channel in the Console.
-
VCA connections Enable this option to display VCA Channel connections beneath the meter on each Channel in the Console.
When enabled, you can click this selector to assign or de-assign a Channel to any available VCA Channels.

## The Console

-
Group assignment Enable this option to display Group assignments above the labels on each Channel in the Console. When
enabled, you can click the Group assignment field and assign the Channel to a different Group.
-
Channel Notes Enable this option to display Channel notes beneath the faders on each Channel in the Console. When
enabled, you can double-click the small window and add more information about the Channel.
-
Channel Icons Enable this option to display Channel Icons beneath the faders on each Channel in the Console. When you click
onto the empty Channel Icon box, a window will appear with many different icon options (Brass, Drums, Guitars, etc.). Including
an icon below each channel can be handy if you’d like to quickly navigate between channels without reading the channel names.
Listen Bus
-
Enable Listen Bus activates the Listen Bus. It can provide an audio feed to the control room monitors or headphones that is
separate from the Main Out Channel. The Listen Bus is completely independent from the other Solo modes.
-
Solo through Listen Bus is independent of the Enable Listen Bus checkbox. After it is engaged, soloed Channels are routed
through the Listen Bus. When it is disengaged, soloed Channels are heard through the Main Out Channel and all other Chan-
nels are muted.
Restore Audio Device Settings
Clicking this icon in the Console will restore the parameters of integrated PreSonus hardware to the states they were in at your last Save
operation. Software-controllable parameters of select PreSonus interfaces vary, and can include Mute, Mono, Dim, Talkback features,
and Headphone source — but the most common application is the editing of preamp gain.(For more on software-controllable hardware
parameters, consult your hardware manual.)
PreSonus hardware that supports this feature includes Studio 192-series interfaces, Quantum, and Quantum 2.
Console Panel Overview
The Console features several panels that can be shown or hidden as needed. Each panel has different functions and is accessed from
the Console Navigation column to the far left of the Console. Click one or more of the buttons to view the desired panels.
Alternative Console Layout
The Console has two viewing modes: Small and Large. Additionally, each mode can be made Narrow. The Console can also be
detached from the rest of the single-screen user interface. The Console layout is strictly a matter of preference: There is no audible dif-
ference between the Small and Large mode, nor does detaching the Console affect its functions.
The Small Console

## The Console

The Console is in Large mode by default. To switch to Small Console mode, click on the Small/Large button at the top of the Console Nav-
igation column. Alternatively, you can press [Shift]+[F3] on the keyboard when the Console is open.
In Small Console mode the Insert and Send Device Racks are hidden, allowing a more efficient use of screen space. To view the Device
Racks for a Channel, click the Expand button that appears above the Channel Editor button next to the Fader in Small mode. This
expands the visible Channel to the right, revealing further Console routing possibilities. Note that the Expand button is only visible in
Small mode when Normal view is selected. It is not visible in Narrow mode.
Narrow Mode
Both the Small and Large Consoles can be made narrow via the Narrow/Normal button to the far left of the Console. Narrow mode has
been designed to maximize the number of visible Channels from left to right in the Console.
When in Narrow mode, the Small Console Channels change so that a volume-fade handle is overlapped on the level meter, with Mute
and Solo controls above the meter. It remains possible to expand a Channel to reveal its Inserts and Sends by double-clicking in open
space on the Channel.

## The Console

The Large Console in Narrow mode replaces the Insert and Send Device Racks with channel level meters, in addition to narrowing the
other controls. To expand any Channel to show its Insert and Send Device Racks while in Narrow mode, double-click on any open space
in the channel display or use its Expand button. Doing so again collapses the display for that Channel.

## The Console

Inputs and Outputs

## The Console

The Inputs panel is closed by default and can be opened and closed by clicking on the [Inputs] button in the Console Navigation column.
The Inputs panel displays Audio Channels in the Console for each configured hardware audio input, as described in the Channel Types
section of this chapter.
The top of each Input Channel has controls for Input Gain and Polarity Invert. For stereo channels there will be two of each control; for
mono channels there will be one. These perform the following functions:
-
Input Gain These controls adjust the Input Gain for the signal before it is sent anywhere else. The range is from -24.0 dB to
+24.0 dB in increments of 0.1 dB.
-
Polarity Invert (Ø) Click this button to invert the polarity of the signal for that Input Channel. When it is lit the polarity has been
inverted. The buttons are independent for stereo Input Channels. Click either Ø icon to invert phase polarity on both sides of a
stereo input; shift-click to invert phase of left/right channels independently.
The Outputs panel is closed by default and can be opened and closed by clicking on the [Outputs] button in the Console Navigation
column. The Outputs panel displays Audio Channels in the Console for each configured hardware audio output.
External
The External panel is closed by default and can be opened and closed by clicking on the [External] button in the Navigation column. The
External panel displays a list of configured External Devices, including Keyboards, External Instruments, and Control Surfaces.
The configuration for each device can be accessed and edited by clicking on the menu arrow for the device (or [Right]/[Ctrl]-clicking any-
where on the device) and selecting one of the following from the menu:
-
Edit for control mapping configuration, and to set up an Aux Channel (external instruments only)
-
Expand/Collapse to show/hide the Aux Channel assignments of a hardware instrument
-
Setup for device configuration (MIDI routing, etc.)
-
Reset to reload the device in Studio One
-
Remove to remove the device from the list.
Click on the Add External Device button to add an external device. To quickly access the Edit dialog for a device, double-click its name in
the External panel.
Instruments

## The Console

The Instruments panel is open by default and is closed and opened by clicking on the [Instr.] button in the Navigation column. The Instru-
ments panel displays all currently loaded virtual instruments, with each occupying an Instrument Slot. If an Instrument is not connected to
an Instrument Track, it is grayed out.
At the bottom of the Instruments panel are two buttons that allow you to decide how much information is displayed for each Instrument
Slot.
-
Compact displays only the virtual instrument, an Activate button to enable or disable the instrument, and an arrow that opens a
pop-up menu (described below).
-
Extended widens each Instrument Slot to display additional information for each virtual instrument: a meter that shows its
CPU load, and the name of the Preset the instrument is using.
Each Instrument Slot pop-up menu offers the following options:
-
Edit... Select this option to open the Instrument Editor window. You can also [Right]/[Ctrl]-click the device name and select Edit,
or simply double-click anywhere inside the Instrument Slot.
-
Expand/Collapse Expand lets you choose from an instrument's available outputs (if applicable). Select Collapse to hide that
information again.
-
Rename... Allows you to rename the instrument, which can be useful when working with multiple instances of the same instru-
ment.
-
Bypass This lets you silence the instrument without deactivating it. The instrument remains attached to its Track, which keeps
the instrument from being affected by the Remove Unused feature.
-
Favorite Use this to designate a virtual instrument as a Favorite. Then it can be located easily in the Favorites folder of the
Browser Instruments tab.
-
Store Preset... Select this option to save the current settings for any virtual instrument as a Preset. You can enter a Name and
Description for the preset, as well as specify a Subfolder within the preset list to store the preset.
-
Disable/Enable Use this to disable an instrument if it is not needed in the Song temporarily, such as after transforming an Instru-
ment Track into an Audio Track. This is one way to reduce the CPU load. Select Enable if you need to make changes to the
Instrument Track.
-
Remove This option removes the virtual instrument from your Song.
-
Copy to Clipboard Use this option to Copy the virtual instrument and its preset to the Clipboard. After this it can be added to the
Instruments panel of another Song or a Show. To do this, switch to the desired Song or Show and use the Add Instrument from
Clipboard command, which is inside the menu at the top of the Instruments list.
-
Send to Song/Show This performs the "Copy/Add Instrument" routines described above with a single action. Note that there
must be an existing target, such as a second Song or a Show, or this command is not visible.
Instruments that have not been used on any Tracks can be removed from the Instruments list. To do this, click the menu arrow at the top
of the Instruments list and select Remove Unused. There is also an option here to disable/enable all instruments with a single action.

## The Console

The Instrument Editor window
Double-clicking inside an Instrument Slot opens the Instrument Editor window. If more than one virtual instrument is present in the Song,
you can switch between them using the tabs above the Instrument Editor window.
The menu at the top of the Instrument Editor window provides unique options such as Enable MPE and Show in Console, and also con-
tains many of the features from the Instrument Slot pop-up menu: Rename, Favorite, Copy to Clipboard, Send to Show, etc.
The Built-in Studio One instruments that support MPE (PresenceXT, Mai Tai, and SampleOneXT) are always MPE-enabled.
Show Scenes
Scenes let you specify which Channels and Tracks you want to work with during a session. For example, you could create a Scene called
"Drums" and recall it whenever you want to focus on the drum mix for a while. You can save multiple versions of the drum mix with dif-
ferent FX and EQ settings, etc., save each as a Scene, and audition them one after the other to see which one you prefer. Any number of
Scenes can be saved and recalled within each Song.
Scenes can be accessed through the Show Scenes button in the Console Navigation column, or by using [Ctrl]+[Alt]/[Option]+[S] to open
a dialog box and typing the Scene name or number. This method is available whether the Scenes list is open or not.
For more details, see the Scenes section.
Show Groups
It is possible to group multiple Channels together so that when one of the faders within the Group is moved, they all move. Their move-
ments are relative to one another, so that the correct dB value relationships are maintained.
Groups are accessed through the Show Groups button in the Console Navigation column. To learn more, see the Groups section.
Channel List

## The Console

Click the Channel List button to view a list of the Channels that can be shown or hidden in the Console. If a Channel is in a Group, the
Group name is displayed next to it in the Group column of the Channel List.
Click the round button next to any Channel name in the list to show or hide that Channel. Click-and-drag quickly through the round but-
tons to hide or show any number of Channels. Hidden Channels are not visible in the Console, but they remain faintly visible in the Chan-
nel List.
View only the Channels you want to see by typing in the Filter field near the bottom of the Channel List, placing a comma between search
terms. For example, to view only Channels named "Bass" and "Guitar", you could enter "bas, guit" in the Filter field. Clear the Filter field
by clicking the X.
Icons for each type of Channel are visible at the bottom of the Channel List. Click them to hide or show all Channels of that type.
The Console Channel List can be synced to the Track List, so that any Tracks hidden or shown in the Track List have their related Audio
Channels hidden or shown in the Console, and vice versa. To do so, click the wrench-shaped Options button in the Channel List and
enable the Link Visibility of Track List and Console option.

## The Console

Remote Bank
The [Remote] button appears when the Channel List is open. The Remote Bank is a special Scene that governs which Channels are
shown and available for manipulation on a connected control surface. Click the [Remote] button to show this scene, then show/hide
tracks as necessary to set which channels are available for control. To hide the Remote Bank, click [Remote] again.
Detach the Console
The Console can be detached from the main window and placed in an independent window so that it can be located freely onscreen or
on a second computer monitor. All of the features described above and in the Groups and Metering sections of this manual are avail-
able when the Console is detached.
To detach the Console, click on the Detach button at the top of the Console Navigation column. The detached Console can be in Small or
Large mode, and in Narrow or Normal mode. The window can also be sized and maximized to fit the computer monitor. To reattach the
Console to the main interface, click on the Attach button at the top of the Console window.

## Effects Signal Routing

Effects processing is critical when mixing. Effects are traditionally applied to audio via an Insert or a Send.
Inserts
Inserts are used to apply an effect directly to a single Channel or Bus. Insert effects are literally inserted into the audio signal chain within
the Channel or Bus.
Adding Inserts
The Insert Device Rack contains all Insert effects on a given Channel and is visible in the Console. To add an Insert effect to any Chan-
nel, drag-and-drop an effect from the Browser into the Insert Device Rack of a Channel in the Console or click-and-drag directly to a
Track or Track Lane in the Arrange view.
When navigating audio effects in the Browser, some effects have a navigation arrow next to them. Click on this arrow to expose the pre-
sets for the effect. Click-and-drag a preset into the Insert Device Rack on any Channel to add the effect with the preset already loaded.

## Effects Signal Routing

Alternatively, you can click on the Add Insert button at the top of the Insert Device Rack to add an Insert effect to a Channel from a pop-up
menu. The plug-in menu functions like a smaller version of The Browser, giving you sorting options, and access to the Favorite and
Recent Plug-ins lists. You can navigate this list using the [Arrow] keys on your keyboard. Click in the search bar and type to find plug-ins
by name.
Alternatively you can choose to browse plug-ins from a basic menu. To change the plug-in menu style, go to the Console Advanced
Options and select the Plug-in Menu style from the popup menu.
Editing Inserts
To edit an Insert, double-click on it in the Insert Device Rack, or click on the menu arrow (or [Right]/[Ctrl]-click anywhere on the
Insert) and select Edit from the pop-up menu. This opens the user interface for the Insert effect, where you can edit the effect’s para-
meters.
When audio effects are inserted on the same Channel, all of the plug-ins appear in tabs at the top of the plug-in header GUI. This makes
switching between effects in the same Insert Device Rack and signal path quick and easy.
The user interfaces for effects from third-party manufacturers vary drastically; for more information, please refer to the documentation for
each effect. Studio One’s built-in effects are discussed in depth in the Built-In Effects chapter.
Reordering Inserts
Inserts affect the audio signal path in the top-to-bottom sequential order in which they are inserted. An Insert can be reordered by click-
ing-and-dragging it above, below, or in between other Inserts. It is helpful to experiment with different signal paths to achieve the best
possible sound or a particular effect. Note that Splitters are a special case, and cannot be re-ordered via drag and drop due to the parallel
manner in which they process the signal chain.
Navigating Inserts
By default, only one window displays the user interface for an open Insert effect. This keeps screen clutter and window juggling to a min-
imum. To quickly switch between Insert effects on a single Channel, click on the chosen effect tab at the top of the plug-in header GUI.
Alternatively, press [F11] on the keyboard to open the effect editor for the selected Audio Track, then press [Ctrl]/[Cmd]+[Page Up]/[Page
Down] to cycle through the effects in that Channel’s Device Rack.
Inserts can be also re-ordered by dragging them from one position to another in the list of Inserts at the top of the plug-in GUI.
The interface for any Insert can be made to stay open in an independent window until you choose to close it by clicking on the Pin button
in the upper right of the Insert Effect window. With an Insert effect pinned, opening another Insert effect opens a new Insert Effect win-
dow. Any number of Insert Effect windows can be pinned and open simultaneously.
Copying Inserts to Other Channels
Copy One Insert to Another Channel
It is often helpful to be able to copy an Insert effect, including its current settings, to another Channel. To do this, click on the desired
Insert effect in the Insert Device Rack and drag it directly onto any other Channel or into the Insert Device Rack on any other Channel.
Dragging an Insert effect to the left or right edge of the viewable Console scrolls the Console left or right to expose any Channels beyond
those currently viewable.
It is also possible to click on the Copy button in the plug-in header GUI, then switch to another instance of the same plug-in and click on
Paste to copy settings from one instance to another.
Copy an Insert FX Chain to Another Channel
You can copy the entire set of Insert effects from one Channel to another, including their current settings. To do so, click the top of the
Inserts Device Rack and drag it to the target Channel.
Moving Inserts to Other Channels
In the event that you want to move, rather than copy, an Insert to another Channel, hold [Alt] as you drag the Insert from one Channel to
the other.
Add An Insert Effect to a Sends Device Rack
You can drag an Insert effect to any Sends Device Rack to create a new FX Channel with that effect inserted (its settings intact), and
route that Send to the new FX Channel.

## Effects Signal Routing

Compare
The [Compare] button in the plug-in header GUI allows you to compare the current settings for a plug-in to the settings stored the last
time the Song, Project or Show was saved.
This makes it possible to freely compare potential changes for a plug-in to existing settings, while retaining a quick way back to existing
settings.
Bypassing, Deactivating, and Disabling Inserts
It is possible to bypass, deactivate, or disable Insert devices. When an Insert is bypassed, the audio signal is simply rerouted around the
Insert, and any CPU or RAM the Insert is using remains in use. When an Insert is deactivated, it is turned completely off, which can free
up CPU resources, but the process remains in RAM, enabling you to instantly turn the plug-in on/off for comparison purposes. When an
Insert is disabled, both CPU and RAM loads are relieved, however, this process is not as instant as bypassing or deactivating an insert.
While Insert bypassing is automatable, deactivation and disabling are not.
To bypass an Insert effect, click on the Bypass button found either in the top left of the effect’s GUI header or within the effect GUI,
depending on the effect.
To deactivate an Insert effect, click on the Activate button for the Insert effect in the Insert Device Rack. There is also an Activate button
at the top left of every Insert Effect window. Deactivating an Insert effect stops all processing related to it, which frees the computer pro-
cessing resources previously dedicated to that Insert effect.
To deactivate or activate all Insert effects in any Insert Device Rack, click on the Activate All button at the top of the Insert Device Rack.
To disable an Insert effect, [Right]/[Ctrl]-click it in the Inserts list, and choose Disable from the context menu. Once an Insert is disabled, it
cannot be activated unless it is re-enabled. To do this, [Right]/[Ctrl]-click the Insert and choose Enable from the context menu.
Activating Inserts Across Multiple Channels
If two or more Channels are selected, pressing the Activate button for any Insert on a selected channel also toggles the activation state of
the Inserts in that same slot on the other selected Channels. Pressing the Activate All button at the top of the Insert list for a selected
Channel makes all other selected Channels follow suit, activating or deactivating their Inserts, as appropriate.
Toggle all Active Inserts Off/On
If you wish to temporarily deactivate all Inserts across all Channels in your song, press the Activate All Inserts button at the bottom-left of
the Arrange view. Press the button again to return all Inserts to their most recent activation state—inserts that were deactivated before
clicking Activate All Inserts will remain deactivated. Hold any modifier key (Shift, Alt/Opt, or Cmd/Ctrl) while clicking Activate All Inserts to
activate these Inserts alongside the rest. In this way, you can instantly compare the sound of your Song with and without all activated
Insert effects. In addition, any Insert effects or Instruments can be deactivated from the expanded Performance Monitor window using
the check-box next to the Plug-in name.
Removing Inserts
To remove an Insert effect from the Insert Device Rack, do one of the following:
-
Click on the menu arrow for the Insert effect in the Insert Device Rack (or [Right]/[Ctrl]-click anywhere on the device) and select
Remove from the pop-up menu.
-
Click on the Insert effect in the Insert Device Rack and drag it into the Trash Bin panel of the Console.
All Inserts can be simultaneously removed from an Insert Device Rack by clicking on the menu arrow at the top of the Rack and selecting
Remove All. When any Insert effect is removed, it is placed in the Trash Bin, where it can be restored to its original state and location at
any time.
Mix Engine FX (Studio One Professional Only)
Mix Engine FX is a plug-in format for Studio One, specializing in processing tasks that affect multiple channels in a song (such as console
emulation). In the case of console emulation, most systems require you to insert a special "channel" plug-in on each channel in the song,

## Effects Signal Routing

and a "bus" plug-in across any busses. This increases the time it takes to set up a new song, and makes managing the process complex,
as any changes desired for the whole mix often must be carried out across multiple channel and bus plug-ins.
Mix Engine FX centralizes this and other similar processes. You simply drop a compatible plug-in onto the Mix Engine FX slot on the
Master Bus, or any other bus you wish to affect. All Channels that feed that Bus are affected by the Mix Engine FX plug-in at their source
(taking the place of the "channel" plug-in), and all parameters are controlled from the one central plug-in interface (which takes the place
of the "bus" plug-in).
Unlike most solutions that rely on multiple plug-ins working together, Mix Engine FX can be bypassed with just a click, allowing for easy
A/B testing between dry and processed signals across the whole mix. Another advantage to this method is inter-channel processing.
Because Mix Engine FX are "aware" of all channels flowing into them, effects like inter-channel console-style crosstalk are made pos-
sible.
Each Bus can have one Mix Engine FX plug-in inserted at a time.
For more information on Mix Engine FX, see Mix Engine FX.
Hardware Inserts
You can insert external hardware processors into Audio Channels in the Console, using the Pipeline XTplug-in (only in Studio One Pro-
fessional). The Pipeline XT plug-in can be found in the PreSonus folder of the Effects Browser when sorted by Folder, Vendor, or Cat-
egory.
The Pipeline XT plug-in routes audio to a hardware processor and then back from that processor through specific inputs and outputs on
your audio interface, while automatically compensating for the round-trip latency incurred in the process. You can insert an instance of
Pipeline XT in any Insert Device Rack.
To learn more about Pipeline, refer to the Pipeline section of this manual.
Channel Editor and Macro Controls
Each Channel in the Console has a special set of effects-related options and controls called the Channel Editor. With it, you can create
complex combinations of insert effects, controlled by easy-to-access Macro Controls. For more information see Channel Editor.
Configuring Sends
Sends are used to route the audio output (pre- or post-fader) from one Channel to another, such as an FX Channel.
Creating a Send to an FX Channel
To simultaneously create a new FX Channel and create a Send to that FX Channel from an existing Channel, click-and-drag an effect
from the Browser into the Send Device Rack on a Channel. This creates a Send for the Channel to a new FX Channel with the selected
effect loaded in its Insert Device Rack. This also works with FX Chains.
You can press [F11] to quickly open the FX view for the currently selected Channel, or press [Shift]+[F11] to open the Instrument window
of a selected Instrument Track.
You can also drag an audio effect into a blank space in the Console to create an FX Channel with that effect loaded into its Insert Device
Rack. To route audio from a Channel to an existing FX Channel, click on the Add Send button in the Send Device Rack and choose the
FX Channel from the list.
Dragging an audio effect or FX Chain to the Send slot of a Track lets you create a new FX Channel with the same name as the plug-in or
FX Chain.

## Effects Signal Routing

You can also create a Send on an FX Channel to route the affected signal to any other Audio, Instrument, Bus, or even another FX Chan-
nel.
Alternatively, you can create an FX Channel by [Right]/[Ctrl]-clicking in blank space in the Console, or on any Channel, and selecting Add
FX. This adds an FX Channel to the Console with no Inserts, which can be the destination for any Send.
FX Channels are routed to the Main Out Channel of the Console by default, but can be routed to any other configured hardware outputs
or Bus Channels, as needed.
To quickly view the effects in the Insert Device Rack of a Send’s destination Channel, double-click on the Send. You can then navigate
the Insert Effect menu as usual.
Send Level and Pre/Post Fader
Once a Send has been added to a Channel, the Send device appears in the Send Device Rack for that Channel. An Activate button, hori-
zontal Level and Pan faders, and a Pre/Post Fader button are available. Click on the Activate button to activate/deactivate the Send; this
does not affect the Send's destination Channel.
Double-clicking the Send device will bring up a larger pop-up interface for fine Send level and pan adjustments.
These pop-ups display The Cue Mixes for the currently-selected channel. With the left/right/up/down arrow keys you can navigate to the
Cue Mixes, Sends, and Panning of other channels across the Console..
Click-and-drag on the horizontal Level fader to adjust the send level between -∞and +10 dB. Click-and-drag on the Pan fader to adjust
the balance of the source material going to the send destination. Click on the Pre/Post Fader button to switch the send source to pre-
fader or post-fader. Pre-fader allows you to set a send level independent of the channel fader so that the level is unaffected by fader pos-
ition.
The send source signal is always post-inserts.
Double-clicking the Send interface will present a larger pop-up interface suitable for fine adjustments.
Channel Pan Lock
By default, a Send’s pan setting in a Bus send, Cue mix send, or FX Send is tied to that of its Channel. Use the Sends drop-down menu
(in either the micro view or the pop-up) to access the option to Unlock Pan for a Channel’s entire send rack, or use the drop-down menu
on each send to assign Pan Lock on a per-send basis. Disabling Pan Lock on either will unhide the panning interface directly below the
Send Level interface.
Note that if a Send is unlocked from a Channel’s panning, all newly-created sends will also be unlocked. This default setting will also
carry over to new Documents.
Sidechaining
Certain virtual instruments and effects can accept an input from an audio source that dynamically changes the behavior of the instrument
or effect. This is called “sidechaining,” and it facilitates processes such as keying, ducking, and de-essing. Sidechaining is accomplished

## Effects Signal Routing

by using a Send to route audio to a special Sidechain input on an Insert on an effect or instrument.
An example of sidechaining is when a gate is triggered by a specific audio signal. In this case, the gate opens and closes dynamically in
response to the audio signal coming in the sidechain, rather than responding to the program signal on the Channel where the gate is
inserted. Several of Studio One’s built-in effects support sidechaining, including the Compressor and Gate. For more information, refer to
the Built-In Effects chapter.
It is possible to send to the Sidechain input of any insert effect, whether or not the sidechain is engaged in the effect.
The sidechain connection can be assigned inside the target instrument or insert effect. Click on the arrow button next to the Sidechain
activation button, then select one or more channels from the popup menu. For the sidechain to work in an effect or instrument, it must be
engaged.
Sidechain-compatible instruments and effects will contain a sidechain menu item. Click the Sidechain button to enable or disable the
Sidechain. The drop-down menu to the right of the Sidechain button allows you to configure the routing to the selected plug-in(s).
-
Tick the Send tickbox to use a Send from the desired Channel to the Sidechain. (If no Send exists, a new one will be created.)
-
Click the pre-/post-fader icon in the middle to toggle between a pre-and post-fader Send to the Sidechain. (This option is only
available when using a send.)
-
Tick the Output tickbox to instead route the desired Channel Output(s) to the Sidechain.
Right-clicking in the routing menu when using a Send will bring up a contextual menu:

## Effects Signal Routing

-
Send Active enables or disables the Send.
-
Send Prefader toggles the pre-/post-fader configuration (same as clicking the icon.)
-
Lock Pan to Channel toggles lock state of the Send pan value to the Channel’s pan value.
-
Show in Console selects to the Send/Output Channel in the Console.
Sending Signals to Busses
It is possible to use a Send to route audio to a Bus Channel. This is done in the same manner that a Send is used to route audio to an FX
Channel, except that the Bus Channel is selected. This can be used, among other things, for “multing”—routing a Channel to multiple
places—which is a convenient way to layer sounds.
Copying Sends to Other Channels
Copy One Send to Another Channel
Sends can be copied from Channel to Channel in the same way as Inserts. To do this, click-and-drag a Send from one Send Device Rack
to another one. This creates a Send to the same FX Channel assigned to the original Track.
Copy a Send Chain to Another Channel
You can copy an entire set of effects from the Sends of one Channel to another, including the current settings. To do so, click the top of
the Sends Device Rack and drag it to the target Channel.
Moving a Send Effect to Another Channel
In the event that you want to move, rather than copy, a Send effect to another Channel, hold [Alt] as you drag the effect from one Channel
to the other.
The FX and Solo Safe
FX Channels have Solo Safe engaged by default, because effects may be critical to how soloed Channels sound in the mix. So when
any Channel in the Console is soloed, the FX Channels remain active.
The Solo button is green when Solo Safe is engaged.
Navigating Effects Presets
To view the available presets for an effect, click on the preset selector in the plug-in editing window, and browse the pop-up list. To select
a preset, click once on the preset in the list. The presets list remains open, to allow for easier switching between presets while audi-
tioning. To close the list, click anywhere other than the preset list. To select a preset and close the list in one action, double-click the pre-
set of your choice.
Once the preset list is open, you can navigate through the presets with the arrow keys. To activate a preset and leave the list open, press
[Space]. To activate a preset and close the list, press [Return].
Creating and Managing Effects Presets
In the upper left area of every plug-in editing window, you'll see the Preset Menu button, which lets you create, load, and import & export
presets. Click the Preset Menu button to choose from the following preset management functions:
-
Store Preset... Saves the current effects setting as a preset, in your library in the Browser. You can enter a title and description
for the preset, as well as specify a subfolder within the preset list to store the preset.
-
Replace Preset Update the currently loaded preset with any new settings made since loading the preset.
-
Store as Default Preset Causes the current preset to load by default whenever a new instance of the current plug-in is added
to a Song.
-
Load Preset File... Loads an exported preset file from your file system into your current Song.
-
Import Preset... Loads an exported preset file from your file system into the current Song, and imports the preset into your Stu-
dio One library, for later use.
-
Export Preset... Exports the current settings as a preset file, for use by others or for storage.
-
Show in Browser Locates the currently loaded preset in the Browser.
You can also store any effect or Instrument preset by dragging-and-dropping the Insert effect or Instrument from the Console to the
Browser. If dragged to a location in the File Browser, the preset is stored in that location. If dragged to the Effects or Instruments Browser,

## Effects Signal Routing

the preset is stored in your User Data location (as set in the Studio One/Options/Locations menu (macOS: Preferences/Locations) and
becomes available in the preset dropdown lists of the Browser and effect or Instrument.
FX Chains
Sometimes, a favorite combination of effects can become a staple of your workflow. For instance, you might regularly apply a com-
pressor, EQ, and chorus to your vocal tracks. FX Chains let you save the exact setup of the Inserts on a Channel, so that the entire chain
of effects, including all settings, can be recalled instantly for later re-use.
To create an FX Chain:
1.
Configure a Channel with the desired Insert effects and settings.
2.
Click on the menu arrow at the top of the Insert Device Rack, next to the Insert label, and select Store FX Chain from the pop-up
menu.
3.
Type in a unique name for the FX Chain and click OK or press [Enter] on the keyboard.
Alternatively, you can drag and drop the Insert Device Rack header to the Effects Browser to instantly create an FX Chain with the name
of the Channel. You can also drag and drop the Insert Device Rack header to the File Browser, to export an FX Chain as a file, with the
name of the Channel. To replicate all Devices currently assigned to a Track on another Track, drag and drop the Insert Device Rack
header from the source Track to the Track of your choice.
FX Chains incorporate any parallel processing you set up in the Routing view of the Channel Editor window. Complex multi-effects con-
figurations with custom Macro Controls can be stored and recalled with ease.
FX Chains can be found in the FX Chains folder in the Audio Effects Browser. To insert the FX Chain in the Insert Device Rack of a
Channel, drag any FX Chain from the Browser to the Channel. To replace an effect in the Device Rack, drag the FX Chain on top of the
device to be replaced. Drag the FX chain between plug-ins or to an open spot in the Device Rack to insert it without affecting existing
device assignments.
Click on the menu arrow next to the FX Chain name in the Audio Effects Browser to view and select the individual effects. Both the indi-
vidual effects and each preset can be dragged to the Insert Device Rack of any Channel.
It is also possible to access FX Chains from the Insert Device Rack by clicking on the menu arrow at the top of the Rack and selecting an
FX Chain from the list. This loads the selected FX Chain in the Insert Device Rack.
Busing

## Effects Signal Routing

Buses can be extremely useful when mixing. You can route Channels directly to buses to help organize a mix into common elements,
such as routing all Drum Tracks directly to a drum bus. Sends are often used to route a channel to multiple buses in order to layer a signal
into various elements of a mix.
To create a new Bus, [Right]/[Ctrl]-click in blank space in the Console, or on any channel, and select Add Bus. You can also select any
number of Channels, then [Right]/[Ctrl]-click on one of the selected Channels and choose Add Bus for Selected Channels to quickly cre-
ate a new Bus and route the selected Channels to that new Bus.
Once you have a Bus with Tracks assigned to it, you can [Right]/[Ctrl]-click the Bus and choose Hide Sources to hide all Tracks assigned
to that Bus in the Console. [Right]/[Ctrl]-click the Bus again and choose Show Sources to make source Tracks visible again.
You can then choose that Bus as the Output or Send destination for any Audio or Instrument Channel in the Console. The Bus sends its
summed signal to the Main Out by default but can also be routed to Sub Out Channels. Buses have Sends that can be used the same
way as other Sends in Studio One.
It is possible to nest buses infinitely (A to B, B to C, C to D, and so on). Feedback prevention is in place so that you can’t create a bus rout-
ing that would cause a feedback loop (e.g., A to B, B to C, C to A).
To remove a Bus and re-route all source Tracks to the Main Out, [Right]/[Ctrl]-click the Bus and choose Remove.
Remapping Effect Channels in Spatial Audio
Any effect can be used in the surround audio format. For any plug-in with mono, stereo and surround options, the available processing
channels can be individually mapped to outputs or muted.
For more information about Remapping Effect Channels in Spatial Audio, check out Mixing in Spatial Audio.
Fader Flip
Studio One’s Console allows you to quickly toggle the function of its faders between control of Channel volume to control of Channel
Sends, via Fader Flip. This allows for a quick and familiar way to control the level of individual sends to FX Channels, Bus Channels, Out-
puts, and of course Cue Mixes for headphone/monitoring mixes.
When Flip is activated, The Console’s faders and panning controls change (Flip) to represent the per-channel Send levels and panning
values to the chosen Send target — including Cue Mix buses and Sidechain Inserts. Faders will change to green to indicate Flip is active;
metering will change from displaying Volume to displaying the Send level. Send rack items of the currently-selected Send target will be
highlighted in green as well.
This can make assigning reverb sends and the creation of monitor mixes much faster and more intuitive by giving you control over send
levels with large faders rather than the smaller horizontal adjustments in the Send elements of the default Console view.
Fader Flip is activated by clicking the Flip button on the top left of the Console.
Fader Flip

The Send target can be chosen by the drop-down menu adjacent to the Flip button. All available Sends will populate this menu.
-
Hide Unassigned Faders will hide Channels with no instances of the Send target when Flip is active. Enabled by default.
If Flip is enabled and unassigned Faders are set to visible, you can add a Send to channels from the Channel Overview or Insert Rack’s
[+] button. The fader of the newly-assigned Channel will Flip (turn green) to indicate Send control.
Fader Flip can also be activated in the drop-down menu of a Send slot or via the right-click contextual menu of any channel that is receiv-
ing Sends.
Channel Editor and Overview
Each Channel in the Console has a corresponding Channel Editor, which has three main views: the Channel Overview, the Routing view,
and the Macro Controls view. Channel Overview gives you a detailed look at a Channel's settings including Pan, inserts, Sends, and Cue
Mixes. The Routing view lets you control the structure and signal flow of effects for the Channel. The Macro Controls view provides a set
of freely assignable knobs, buttons, and X/Y pads that provide easy access to any parameters in any of the plug-ins currently used in the
Channel.
Because the Channel Editor is all about configuring and controlling audio effects, only Audio Channels and Channels associated with
software Instruments have this feature.
You can display the Channel Editor in the following ways:
Channel Editor and Overview

-
Click the Channel Overview button (which looks like this:
on your chosen Channel in the Console.
-
Select a Channel, and click the Channel Editor button (which looks like this:
in the Track Inspector.
-
Click the number of the corresponding Track in the Arrange view.
-
Click the Macro Controls or Routing button in an open effects window.
Channel Overview
The Channel Overview Window provides a single, consolidated view of all Channel parameters, including input controls, Inserts, Sends,
and Cue mix sends for the selected Channel. This view can be accessed at any time by clicking the
icon from a Channel, and is
also available as a tab in the Channel Editor window, next to the Macro Controls, Routing and Insert FX tabs. Channel Overview can be
pinned anywhere and follows the Channel selection.
For more detailed information on the features detailed below, all available from Channel Overview, we recommend first familiarizing your-
self with The Console as the user interface for controlling Faders, Pans, Sends, etc. are identical in the Channel Overview.
Features of the Channel column (left) include:
-
Channel number and name Double-click the name to edit; single-click the area to select Channel color.
-
Hardware Input controls If your connected hardware supports software input controls, they will be shown here.
-
Channel Input controls Gain and Polarity. Click and drag Gain to adjust; click Polarity to toggle.
-
Mute/Solo Click either icon to toggle status.
-
Record Arm/Monitor Click either icon to toggle status.
-
Input/Output routing. Click either to assign Input source our Output destination.
-
Pan mode setting Click the [▼] drop-down menu on the top left to choose from varying pan modes for stereo Tracks.
-
Track Notes are displayed here. Double-click to Edit.
-
Track Icon Click here to choose or change a Track icon.
-
Channel Fader and meter Right-click the meter to choose from several metering options.
-
Group assignment Click to bring up a list of groups and re-assign the Channel, if desired.
-
Automation Click to open a list of Automation options for the Channel.
Inserts
All of the Channel’s Insert Device Racks are shown here. Channel FX Chains can be chosen, stored, enabled, and disabled from the [▼]
drop-down menu icon on the top right of the Inserts column.
Channel Overview

Effects can be added by clicking the [+] drop-down menu icon.
Devices in the Insert Device Racks can be expanded, edited, disabled, replaced, and more from their respective [▼] drop-down menus.
Sends
All of the Channel’s Insert Device Racks are shown here.
Click the [▼] drop-down menu icon on the top right of the Sends column to remove Sends or Effects Signal Routing for all Sends from
the Channel’s pan setting. Alternatively, Sends can have their Channel/Pan lock settings toggled individually from their respective  [▼]
drop-down menus.
Sends (including Sidechain Sends), Buses, and FX Channels can be added by clicking the [+] drop-down menu icon.
Cue Mixes
All of the Channel’s  Cue Mixes and Low-Latency Monitoring are shown here.
Click the [▼] drop-down menu icon on the top right of the Cue Mix column to lock/unlock Cue Mix panning from the Channel Pan setting
for all Cue Mix Sends. Alternatively, Cue Mix Objects can have their Channel/Pan lock settings toggled individually from their respective
drop-down menus.
Macro Controls
A single Channel in the Console can host multiple plug-in effects, and you can control them all one-by-one simply by switching from one
plug-in window to another. However, in some cases, it is convenient to be able to access controls from multiple plug-ins in a central con-
trol panel. The Macro Controls feature in the Channel Editor gives you a blank canvas upon which to place crucial control parameters
from any of the present effects, giving you quick access to often-needed controls. This becomes even more useful when creating
FX Chain presets that are geared toward specific sounds.
For example, let's say you create an FX Chain called "Chorused Crunch Guitar Delay," that includes the Ampire, Chorus, and Analog
Delay plug-ins. You might assign Macros to the gain controls on Ampire, rate and depth controls on Chorus, and the delay length and
feedback on Analog Delay. In this way, as soon as you load up that FX Chain, the vital parts of its functionality become available in a cent-
ral, single window, even though you're really controlling three plug-ins at once.
Channel Overview

There are eight knobs, eight buttons, and two X/Y control pads available for each Channel. You can assign any available plug-in para-
meter (or multiple parameters) to each of these Macro Controls. Each control (and each axis of each X/Y pad) displays the name of the
associated parameter, and the current setting of that parameter. If multiple parameters are assigned to a Macro Control, the name of the
first parameter assigned is shown, with a "+" symbol next to it.
If things get complex, you can get more in-depth info about assigned parameters in the Macro Controls Mapping view.
When working with the built-in PreSonus plug-ins, assigning parameters to Macro Controls is especially easy—simply [Right]/[Ctrl]-click
the control of choice, select "Connect (name of control) to Channel Macro Control" from the pop-up menu, then choose the desired
Macro Control from the secondary pop-up list.
To clear all assignments for any Macro Control, [Right]/[Ctrl]-click the control and choose "Clear (control name) Connections"
Right-click a Macro Control knob or switch to get access to automation for that control.
Macro Controls Mapping
You can bring up the Macro Controls Mapping view by clicking the small wrench-shaped button in the Macro Controls window. This view
gives you the ability to assign 3rd-party plug-in parameters to Macro Controls, and also provides some useful additional features for work-
ing with Macros.
The Macro Controls Mapping view shows three columns of information. The left column lists all available Macro Controls, and their cur-
rent assignments (if any). The right column shows all effects plug-ins that are currently inserted into the Channel. Expand any plug-in in
the list to show all assignable parameters for that plug-in. The central "Target" column is a place where Macro assignments can be made,
configured, or broken.
You can assign an unlimited number of parameters to the same Macro Control, each with its own range and polarity, to create powerful
“morphing controls”. As more parameters are assigned to a Macro Control, plus signs (+++) are added to the right of the default name in
the Title column. You can rename the Macro Control if you like; just double-click the name in the Title column.
The simplest way to map a parameter to a Macro is to simply drag the parameter from the right column onto the Macro Control of your
choice in the left column, or into the central Target column when a Macro Control is selected. You can also do this by selecting a Macro
Channel Overview

Control and a parameter, and clicking the [Add Targets] button. Once assigned, the parameter of your choice is displayed in the Target
column.
To remove an assignment from a Macro Control, select the Macro in the left column, select the assignment you wish to remove in the Tar-
get column, and click the [Remove Targets] button.
Macro Control Transform Settings
You can shape the relationship between the movement of a Macro Control and the settings of its assigned parameters quite extensively.
With a Macro Control selected in the left column of the Macro Controls Mapping view, the current mappings for that control are displayed
in the Target column. Next to the name of each parameter is a button that gives you access to the control transform settings.
This graph traces the response curve from the beginning of the macro control's travel (the draggable point on the left end of the curve) to
the end of its travel (the point on the right end), with a handle in the middle that you can drag to set the shape of the curve. Dragging these
points up and down the control scales on the left and right of the graph lets you set the effective range of motion for that Macro control.
For example, the whole range of a Macro knob could be set to affect just a quarter of a parameter's range, for fine-tuning purposes. You
can also move the right point below the left, reversing the action of the knob, according to whatever scale you wish.
Below the graph are buttons that let you Reset the graph to its default setting, Invert the shape of the curve, or Copy the curve setting and
Paste it onto another parameter.
Note that because Macro buttons are an on-off type of control, they have no curve setting. However clicking in the Trans column next to a
button assignment inverts its response, causing the parameter to be enabled when the Macro button looks disabled, and vice-versa.
Channel Overview

Routing View
Normally, if you add multiple effects to a Channel, they are connected in series; the output of the first effect feeds into the second effect,
which feeds into the third, and so on. If you open the Routing view in the Channel Editor for a Channel with multiple effects, this is what
you'll see.
Each effect in the Routing view is displayed as a module. When they're in series, a line runs through them from top to bottom, signifying
the path of the signal as it runs through the modules. The signal starts at the top, and flows through the effects, to the bottom.
You can click on an effects module to select it. If a selected effect is a built-in plug-in, a selection of the plug-in controls are displayed in
the inspector to the left. You can load patches for the effect from this inspector, as well as set a color for the selected effects module, by
clicking the color picker to the left of the effect's name in the inspector.
Each module in the Routing view has a Bypass button, as well as a drop-down menu that offers the following operations:
-
Edit Opens the editor window for the selected plug-in.
-
Rename Lets you rename the selected effect.
-
Remove Removes the selected effect from the Channel.
Adding and Moving Effects
You can add effects by dragging them into the Routing view window. Drag them into position above or below other effects to change the
order in which they process the signal. You can also add effects by clicking the [Inserts] button, which brings up a menu of available
effects.
Splitting Signals
Channel Overview

The Splitter module lets you split signals, letting you process them through multiple parallel effects paths. These split signals are then
mixed back into a single signal. You can add a Splitter to your effects setup by clicking-and-dragging from the [Splitter] button to your
choice of location in the Routing view.
You can click on a Splitter to select it, and its options are shown in the inspector to the left. The following options are available:
-
Splits Lets you specify the number of independent paths to split the signal into.
-
Mute Output Click the boxes to mute and unmute individual split paths.
-
Levels Lets you set the output level of each split path, from fully off (-∞dB) to +10 dB. To set the level of a split path, simply
move the corresponding slider, or click its numerical dB display to enter a value with your computer keyboard. Split path levels
can also be adjusted in the Routing view. Click-and-drag the small fader icon on your chosen path to set its output level, or click
in the corresponding numerical display to enter a value in dB.
-
Split Mode Select the Splitter mode that suits your needs, from the following choices:
-
Normal Splits the signal into two or more identical copies. This is useful for any sort of parallel processing, such as
"New York" compression or vocal multiprocessing.
-
Channel Split Splits multichannel signals into pairs of mono signals, for independent processing of left and right chan-
nel information. (E.g. With two splits, this turns a stereo signal into a pair of left/right mono signals. With four splits, you
get two sets of left-right mono signals.
-
Frequency Split Splits a signal into isolated bands of frequencies, at the frequencies you specify. With two splits, the
signal is crossed-over into two frequency bands, split at a single frequency. With three splits, there are three bands, split
at two crossover frequencies, and so on. When more than one frequency split is employed, The splits are numbered
from low frequency to high.
Much like you can move effects modules into different places in the signal chain, you can move Splitter modules to the position of your
choice, as well as freely move effects into and out of each split path. To remove a Splitter module, click its triangle to open the pop-up
menu and choose Remove. If you remove a splitter module that has effects inserted within its split signals, those effects are reconnected
in series.
Splitter effects chains are compensated for plug-in delay automatically, retaining the proper time relationship between all split channels.
Quick Access to Main Bus Inserts
To quickly open the Channel Editor for the Main output bus, double-click the main output meters in the Transport bar.

## Groups

As discussed in the Edit Groups section of the Editing chapter, it is possible to group multiple Tracks together so that any edits done to
an Event on one Track in the Group are automatically done to all Events for all Tracks in the Group. These same Edit Groups affect how
their related Channel faders behave in the Console.

## Groups

Create or Dissolve a Group in the Console
To create a Group in the Console, select the desired Channels and then [Right]/[Ctrl]-click and select Group Selected Tracks from the
pop-up menu. Or you can use the shortcut: Select the Channels and then use [Ctrl]/[Cmd]+G to create a Group. Groups can be nested:
two Channels can be part of a smaller Group and also part of a Group with more Channels.
To dissolve (ungroup) the grouped Channels, [Right]/[Ctrl]-click on any Channel in the Group and select Dissolve Group from the pop-up
menu. There's also a shortcut for this: After selecting one the grouped Channels, use [Ctrl]/[Cmd]+Shift+G to dissolve the Group.
When an Audio Channel is in a Group, the Group icon appears inside the Channel above the level meter. Note that the Group icon is not
visible when the Console view is in Narrow mode.
Group Behavior in the Console
When a Channel is placed in a Group its fader is linked to the faders for all other Tracks in the Group, so that if one of them is moved, they
all move. Their movements are relative to one another, maintaining the correct dB value relationships among the faders. Grouped Chan-
nel parameters can still be edited individually by holding [Alt]/[Option] while manipulating their controls.
Solo, Mute, Record Enable, and Monitor Enable controls are also linked for all Channels in a Group. No other aspect of the Channel in
the Console is affected by grouping. Selecting a new Insert effect for one of the Channels will affect the Group, however.
Instrument Tracks in the Arrange view have no direct representation in the Console. The audio outputs of the virtual instruments to which
they are routed have corresponding channels in the Console. Grouping Instrument Tracks in the Arrange view only affects editing Events
on those Tracks, unless the Tracks are routed to virtual instruments. In this case, grouping behavior is applied to the corresponding
Instrument Channels in the Console as well.
Temporarily Suspend Groups
It is possible to suspend a Group temporarily so that, for instance, the fader for a Channel in a Group can be edited without affecting the
other Channels in the Group. To suspend the Group, hold [Alt]/[Option] on the keyboard while clicking on the Fader, Mute, Solo, Record
Enable, or Monitor Enable controls. Note that [Alt]/[Option]-clicking Solo on a grouped Track clears the Solo status of all Tracks in the
Console; if you wish to solo a grouped Track along with other Tracks outside the Group, you must first solo the grouped Track, then
enable solo for any additional Tracks. It is not possible to solo single Tracks from two separate Groups simultaneously, though you can
solo a single Track from one Group and solo all Tracks in a second Group.
To suspend an entire Group, hold [Shift]+G and type the number of the Group or the first letter of its name into the small window that
appears. Use the same command to reactivate the Group. Another way is to hold [Alt]/[Option] and enter a Group number between 1 and
10.
To suspend or reactivate all Groups at once, use [Ctrl/Alt]/[Cmd/Opt]+G. Note that Group suspensions are not saved or remembered
when Studio One is restarted.
Show Groups
When the Track / Channel List is open you can view the list of Groups by clicking the Show Groups button. You can temporarily suspend
a Group from this list by clicking the dot next to its name. You can also suspend all Groups by clicking the bracketed Groups icon in the
upper left corner of the Group list.

## Groups

Nested Groups
Channels can be part of a smaller Group and also part of a larger Group that includes those Channels. In this case the Groups have been
nested. Note that in order to make adjustments to the smaller, nested Group, the larger Group must be temporarily suspended.
Group Attributes
You can specify which controls within a Group will be affected by the other Channels. Features that can be included or excluded from a
Group are Editing, Volume, Pan, Mute / Solo, Record / Monitor, Inserts, and Sends. For example, if you want to disable linked panning of
all of the grouped Channels at the same time, [Right]/[Ctrl]-click the Group name in the list of Groups and disable Pan. The relative stereo
positions of the Channels in the Group are maintained when the Pan control for one of the grouped Channels is moved.
Viewing / Changing Group Assignments
Tracks and Channels can be assigned to more than one Group. Group assignments can be viewed by [Right]/[Ctrl]-clicking anywhere
inside the Channel area and selecting Group Assignment. A check mark by a Group name indicates a Group to which that Channel has
been assigned. To add or remove a Group assignment, select one of the Group names. The change will be made and the window will
close.

## Groups

Groups and Effects
The first time Channels are grouped they keep the individual effects settings and assignments they had. But changes that are made to
the effects of any grouped Channel will cause all of the Channels within the Group to adopt the same changes. Note that this does not
add the new effects to the ones already on the Channels; those will be replaced.
For example, if a new Insert preset is selected for one Channel within a Group, that same preset will be selected for the rest of the Group.
Any changes made to the Sends of a grouped Channel will affect the entire Group also.
If you want to change the effects settings for one of the grouped Channels without affecting the others you can suspend the Group tem-
porarily. You can also specify that the Inserts and the Sends not be affected by other actions within a Group. To ungroup those actions,
disable them in the Group Attributes window.

## Scenes

Scenes provide an easy way to save and recall different configurations of Channels and Tracks, as well as different settings. For
example, let's say you want to audition different FX for the drum Channels: you can create a Scene called "Drums", make as many
changes as you like, save those as another Scene, and then go back and forth between them to see which you prefer.
Recalling a Scene shows the desired Channels and Tracks and hides all of the others, which makes it easier to focus on those items.
You can specify which portions of a Scene are recalled, and for which Channels, etc.
Additionally, Automation data is saved and recalled for the corresponding parameters if checked:
-
Volume: restores Volume automation
-
Pan: restores Pan automation
-
Mute: restores Mute automation
-
Inserts: restores Plug-in automation of Insert effect parameters
Any number of Scenes can be saved and recalled within each Song. They also can be saved as part of a Song Template.
Working with Scenes

## Scenes

Click the Show Scenes button in the Console navigation column to access the Scenes list and Recall Options.
To save the current set of Channels and Tracks as a Scene, click the Plus button at the top of the Scenes window. You can give the
Scene a unique name to help you remember its contents.
To recall a Scene, double-click its name in the Scenes list. Alternatively, use [Ctrl]+[Alt]/[Option]+[S] to open a dialog box, then type the
Scene name or number. This method works whether the Scenes list is open or not.
Link list actions
The following Options can help you construct Scenes quickly. Click the wrench-shaped button in the Console Navigation column to
enable or disable them:
-
Link visibility of Track List and Console Enable this to link the show/hide status of the Track List and the Console. When you
hide an item in the Track List or Console, it is hidden in the other as well.
-
Link expansion and visibility of Folder Tracks Enable this to hide Console Channels associated with a Folder Track when
the Folder Track is collapsed in the Arrange view.
Recall options
All of the Track and Console settings are stored when you Add or Update a Scene. But you can use the Recall Options menu to specify
which aspects of a Scene are recalled. For example, if you want to retain the current Volume setting for the Channels when another
Scene is recalled, disable Volume in the Recall Options menu.
-
Visibility Disabling this option allows you to compare the settings of two Scenes without changing what is displayed in the
Arrange view and the Console. When it is enabled, the Channels and Tracks are shown/hidden according to the Scene settings.
-
Volume This option allows the Volume settings to change when a Scene is recalled. Disable it to prevent these changes.
-
Pan This option allows the Pan settings to change when a Scene is recalled. Disable it to prevent these changes.
-
Mute This option allows the status of the Mute buttons to change when a Scene is recalled. Disable it to prevent these changes.
-
InsertsThis option allows the status, contents, and settings of the Insert effects to change when a Scene is recalled. Disable it to
prevent these changes.
-
Sends This option allows the status, contents, and levels of the Send effects to change when a Scene is recalled, including the
Prefader On/Off settings. Disable it to prevent these changes.

## Scenes

-
Cue Mix This option allows the status and levels of the Cue mixes to change when a Scene is recalled. Disable it to prevent
these changes.
-
Input Controls This option allows the Input Gain and Polarity of the Input Channels to change when a Scene is recalled. Dis-
able it to prevent these changes. The Recall Input Channels option must also be enabled for the changes to be applied.
-
Selected Channels only This option allows you to specify which Channels are modified when a different Scene is recalled. Dis-
able it to allow all Channels to be changed.
-
Recall Input Channels Enable this option to recall the settings for the Input Channels (Input Gain and Polarity). The Input Con-
trols option must also be enabled for the changes to be applied.
-
Recall Output Channels Enable this option to recall the level settings for the Output Channels, including the Main Out Channel
or the Listen Bus.
Scene management
[Right]/[Ctrl]+[Click] one of the Scenes to reveal a menu with the first four options, or click the down arrow next to the [+] symbol inside
the Scenes menu to view all five.
-
Recall Scene This option recalls the selected Scene.
-
Rename Scene... Use this option to rename the selected Scene.
-
Update Scene This option replaces the settings of the selected Scene with the current settings.
-
Remove Scene Use this option to remove the selected Scene from the list of Scenes.
-
Remove Scenes To remove two or more Scenes at the same time, hold [Ctrl]/[Cmd] + click to select the desired Scenes, or use
[Ctrl]/[Cmd] + [A] to select them all. Then select Remove Scenes from the menu to remove the selected Scenes.

## VCA Channels

## VCA Channels

As we touched on in Groups, sometimes it's helpful to tie the volume settings of multiple Channels together, so that they can be easily
controlled as a Group. However, when you create a Group, the volume faders for all included Channels move simultaneously when any
grouped fader is moved. This means that any inter-channel volume balancing involves either temporarily ungrouping the Channels, or
changing the relative gain of a Channel using the gain control on an inserted plug-in.
Also, it can be desirable to write automation that changes volumes for a whole set of Channels, which can be cumbersome when it must
be done on a per-channel basis. A similar effect can be accomplished by routing Channels to a Bus and writing volume automation for
that Bus. However, this means that the audio from all affected Channels must pass through that Bus, which may not be desirable,
depending on your needs.
VCA Channels give you a solution to all these issues. They are special assignable control faders in the Console that allow simultaneous
movement (and automation) of the volume of multiple Channels. The individual volume faders of affected Channels can still be moved
independently—all faders move as one only when you change or automate the setting of the linked VCA Fader.
Creating and Assigning VCA Channels
You can create and assign a VCA Channel in two different ways:
-
Select the Channels you want to control in the Console. [Right]/[Ctrl]-click and choose "Add VCA for Selected Channels" from
the pop-up menu. This creates a new VCA Channel and assigns the selected Channels to it.
-
[Right]/[Ctrl]-click in the Console and choose "Add VCA Channel" from the pop-up menu, creating a new VCA Fader. Assign the
desired Channels to the new VCA Fader by clicking the selector under the meter/fader for each Channel in the Console and
choosing the desired VCA from the pop-up list.
If the VCA Channel selectors are not visible beneath the meters for each Channel in the Console, you can re-enable them by toggling the
"Show VCA Connections" option in Console Options.
Channels may be unlinked from an assigned VCA Channel by clicking VCA selector for the Channel and choosing None from the pop-up
menu.
Automation with VCA Channels
One of the advantages of VCA Channels is that they can be automated, thus automating the volumes of all affected Channels without the
need to route their audio to a bus or write individual volume automation for each Channel. Any volume automation that exists on the indi-
vidual channels continues to be active, along with any changes enacted by movement of the VCA.
To automate the setting of a VCA Channel, [Right]/[Ctrl]-click the fader and choose "Edit Volume Automation" from the pop-up menu. An
automation lane for the VCA Fader appears in the Edit view, and can be edited just like you would for normal Tracks. Any automated
changes in VCA Fader level are applied in a relative manner to the faders for any linked Channels. You can see this reflected in a gray
automation line that sits alongside the volume automation of each affected Track in the Edit view.
Merging VCA Automation

## VCA Channels

Once you've written some automation moves for your VCA Channel, you may decide that you want those changes to be permanently
applied to the automation for the Tracks controlled by the VCA. To do so, [Right]/[Ctrl]-click the VCA Fader Track in the Edit view, and
choose "Merge VCA Automation" from the pop-up menu. This merges the VCA automation with the extant automation on each affected
Track, and returns the VCA automation lane to its default state, for easy manual control.
Controlling VCA Channels with VCA Channels
Another nice feature of VCA Channels is, because they're simply controllers, their effects can be nested. For example, if you have mul-
tiple snare Channels, they could be linked to a snare-specific VCA fader for simultaneous control. Then, all drum-related VCAs (and
drum Channels not yet linked to a VCA) could be linked to a "master" VCA Fader that controls overall drum level. In this way, large
amounts of Channels can be mixed and managed with ease.
Folder Tracks and VCA Channels

## VCA Channels

Much like you can assign a Folder Track (and its associated Tracks) to a Bus, you can also assign them to a VCA Channel. This gives
you simultaneous control over volumes for all tracks in the Folder Track without the need to route the audio from those tracks into a Bus.
To assign a Folder Track to a VCA Channel, click the Bus/VCA selector in the Folder Track's control panel in Edit View, and select the
VCA of your choice from the pop-up menu. This assigns all Tracks in the Folder to your chosen VCA Fader. This assignment can then be
defeated or changed on a per-track basis.

## The Listen Bus

A dedicated Listen Bus is available for monitoring Solo signals, which allows you to solo individual Channels and sources without affect-
ing the Cue Mix busses. It can provide a separate audio feed to the control room monitors or headphones, independently from the Main
Out Channel. When activated, initiating Solo on any Channel sends the solo signal to the designated outputs.
Another potential use is to run a room calibration plug-in as a Listen Bus insert while keeping the Main Output unaffected.
To activate the Listen Bus, [Right]/[Ctrl]-click any Channel in the console. You'll see two options near the bottom of the menu:
-
Enable Listen Bus activates the Listen Bus and adds it to the Console, immediately to the left or right of the Main Out Channel.
It can be dragged to either side. When active, audio passing through the Listen Bus can be routed to any of the output pairs on
your audio interface in the Song Setup window, which can be accessed through the Audio I/O Setup button in the Console Nav-
igation column. The status of the Listen Bus is saved with each Song.
-
Solo through Listen Bus can be toggled independently of the Enable Listen Bus checkbox. After it is engaged, soloed Chan-
nels are routed through the Listen Bus and the other Channels are heard through the Main Out Channel. When it is disengaged,
soloed Channels are heard through the Main Out Channel and all other Channels are muted.
These two options are also found in the Options menu of the Console Navigation column.
Note that the Listen Bus is completely independent from the other Solo modes (Solo Safe and Solo-in-Place).
Listen Bus features

## The Listen Bus

Some of the features of the Listen Bus are similar to other Bus Channels, and others resemble the features of the Main Output Channel.
For example:
-
Insert FX and Post-fader FX can be added as needed.
-
The Output Channel can be selected in the field above the Peak Hold meters.
-
You can specify the Peak Hold behavior of the meters.
The button features are mostly familiar:
-
L stands for Listen Bus. It is highlighted when any Channel is in Solo mode. Use it as a master Solo button to enter and exit Solo
mode for all soloed Channels at the same time.
-
Prefader Listen The Listen Bus offers a dedicated PFL (Pre-Fader Listen) option. Signals soloed in PFL mode are monitored
pre-fader and pre-pan. With PFL disengaged, the solo signal is monitored after fader and pan.
-
Click On/Off Click this button to toggle the Click on and off for the Listen Bus.
-
Click Volume Click and hold this button to reveal the Click volume fader. Use this to adjust the Click volume for the Listen Bus.
-
Channel Mode Click this button to toggle the Listen Bus between stereo and monaural operation.
The Listen Bus is also available on the Project Page.

## The Listen Bus

Metering
Metering is a critical part of the production process. Studio One’s meters visually display audio levels according to your choice of meter-
ing style, and you can meter these levels at various stages in the signal path. The meters automatically display in mono or stereo depend-
ing on the audio source.
Two Metering Mode menus are available: one for the Output Channels and another one for the other
Console Channels. Use [Right]/[Ctrl]-click to access the Metering Mode menu for the desired set of
Channels. Note that the Pre-Fader Metering setting is applied globally to all meters, including the Out-
put Channels. Changing that setting in one menu will change it automatically in the other menu.
The menu for most of the Console Channel Types allows a choice between Peak or Peak/RMS meter-
ing modes. The selection will be applied to all Channels in the Console except the Output Channels.
Peak meters are not available for the Output Channels, which feature Peak/RMS metering with K-Sys-
tem Metering options.
[Right]/[Ctrl]-click on any meter to adjust the Peak Hold and Hold Length settings globally for all Chan-
nels.
Peak Meters
Peak meters measure the instantaneous audio level from moment to moment at a very fast resolution
and display the highest output level at any instant. These meters help ascertain the relationship
between a given audio level and other audio levels in the mix. Many effects plug-ins feature peak
meters at the input and output so that any level attenuation the effect imparts on the audio signal can
be seen.
Peak/RMS Meters
Peak/RMS meters simultaneously show both peak and RMS levels. Whereas a peak meter shows the
highest output level at any instant, an RMS meter shows an average of the peaks and troughs of an
audio signal over time. An RMS meter is intended to indicate the perceived loudness of the audio being
measured by functioning in a way similar to the human ear and is therefore often used as a true meas-
ure of perceived loudness.
Pre-Fader Metering
[Right]/[Ctrl]-click on any meter to access the menu and enable or disable Pre-Fader Metering. When it
is enabled the level meters show levels independent of fader position. When it is disabled the level
meters respond to fader position. This is known as Post-Fader Metering. The selection you make will
be applied globally to all Channels, including the Output Channels.
Main Out Clip Counter
The Main Out Channel features a Clip Counter above its Peak/RMS meter.
The counter turns red when the Main Out signal clips and counts the total number of clips that occur.
Use the counter to help prevent clipping the final stereo mix of your Song. The counter resets when
clicked or when the Main Out fader is adjusted.
K-System Metering
The Peak/RMS meters in the Output Channels also feature K-System metering options. The K-System
is an integrated metering system tied to monitoring gain, and it is intended to standardize the levels at
which sound is mixed and mastered. This metering system features three different meter scales called
K-20, K-14, and K-12. These three scales are meant to be used with different types of audio production
and have been described by K-System inventor Bob Katz in his Audio Engineering Society technical
paper “An Integrated Approach to Metering, Monitoring, and Leveling Practices.” Katz wrote:
“The K-20 meter is for use with wide-dynamic-range material, e.g., large theater mixes, ‘daring home
theater’ mixes, audiophile music, classical (symphonic) music, hopefully future ‘audiophile’ pop music
mixed in 5.1, and so on. The K-14 meter is for the vast majority of high-fidelity productions for the
home, e.g., home theater and pop music (which includes the wide variety of moderately compressed
music, from folk music to hard rock). And the K-12 meter is for productions to be dedicated for broad-
cast.”
Metering

To switch to any K-System meter, [Right]/[Ctrl]-click on an Output Channel meter and choose an option from the menu.
When using any of the three K-System scales, the 0 VU mark should be calibrated to 85 dB SPL from your monitors, which you should
measure with an SPL meter. For instance, playing back a -14 dBFS sine wave in Studio One while using the K-14 scale causes the meter
to read 0 VU for both the peak and average levels, and your monitors should be adjusted so that the SPL meter at the listening position
reads 85 dB SPL.

## Performance Monitor

You can open the Performance Monitor window by navigating to View/Performance monitor. This window displays the current total CPU
and disk usage, as well as specific usage data for Insert effects and Instruments. To open the editing window for an Insert or Instrument,
double-click its name. To deactivate an Insert or Instrument (to free up the associated RAM and CPU), click the check-box next to its
name. To activate a deactivated item, click the check-box again, or click the Activate button on the Insert or Instrument slot in the Con-
sole.
You can also activate/de-activate multiple plug-ins quickly by clicking a tickbox and dragging up or down the entire list.
The Cache section shows you the amount of audio data currently in the Audio Cache, with options to show its contents or clean up
unused items in the cache.
Automatic Plug-In Delay Compensation
Some plug-in effects inherently have some delay, or latency. It takes a certain amount of time for these plug-ins to process the audio
routed to them, which means the resulting output audio is slightly delayed. This especially applies to dynamics processor plug-ins that
feature a look-ahead function, such as the included Compressor.
In Studio One, this delay is managed with plug-in delay compensation through the entire audio path. There are no settings to manage, as
this feature is completely automatic. The sync and timing of every Audio Channel in your Song are automatically maintained, no matter
what processing is being used.
The current total plug-in delay time is displayed in the left-side Transport, below the current sample rate.
Manual Audio Track Delay
It is sometimes necessary to manually delay the playback of audio to keep it in sync with other audio. A classic example is in the case of
recording a live performance, where tracks are recorded directly from the mixing console, while ambient microphones capture the
 Automatic Plug-In Delay Compensation

audience sound from a position well away from the stage. The direct sound from the console arrives at the recorder almost instant-
aneously; it takes longer for the sound to reach the ambient mics from the stage. When the signals are mixed, the time difference results
in audible delay and phase problems. To properly align the recorded audio from the ambient mics with the rest of the recorded mix, you
can apply a negative amount of manual delay to the ambient recording.
Open the Inspector view by clicking on the Inspector button or pressing [F4] on the keyboard. Enter a positive or negative Delay value, in
milliseconds, to apply a delay to the Track.
To calculate the value to apply to ambient mics in the example, do the following:
-
Measure the distance from the stage to the ambient mics.
-
Divide the distance in feet by 1,129, which is roughly the speed of sound (at sea level, at 1 atmosphere of pressure) in feet per
second (divide the distance in meters by 343 for meters per second). The resulting value is the amount of seconds it took for
sound to reach your ambient mics. For example, if the distance was 100 feet, the resulting amount of time is 0.0885 seconds
(100/1,129=0.0885), or 88.5 milliseconds.
-
For the stereo ambient mic Track, or for each mono Track, enter a Delay value of -88.5, which removes the recorded delay and
puts the Tracks in sync with the rest of the recording.
Using the Marker Track
You’ll often want to navigate quickly to various areas of your Song during mixdown. In Studio One the Marker Track is used to place Mark-
ers at desired places in the timeline, after which navigation to the Markers is easy. To open the Marker Track, click on the Marker Track
button above the Track Column in the Arrange view.
Notice the Timebase button to the right of the Marker Track in the Track column. The musical-note icon on the Timebase button indicates
that Markers will adhere to their position based on bars and beats, so if the tempo changes, the Markers move forward or backward in
time in relation to their musical position.
If you click on the Timebase button, it switches to a clock icon, indicating that the Markers will adhere to their absolute position in time. If
the tempo changes, the Markers do not move, as they are locked to an absolute time position in the timeline.
Inserting Markers
To insert a new Marker into the Marker Track, with playback running or stopped, click on the Add Marker button or press [Y] on the key-
board. Each new marker is numbered sequentially by default (1, 2, 3…). To insert a named Marker, press [Shift]+[Y], enter a name in the
pop-up window, and click [OK], or press [Enter]. To rename a Marker, double-click on it in the Marker Track, type in a new name, and
then press [Enter] on the keyboard. Note that, for clarity, the Start and End markers cannot be renamed.
Marker Track Inspector
Open the Inspector by clicking the [i] button above the Track column, or by pressing [F4] on the keyboard. This opens a window on the
left side that shows a list of existing Markers.
A locator icon shows the current location, and always highlights the Marker that was passed most recently. Click the area to the left of the
Marker name to move the playback cursor to that location. Double-click the Marker to rename it.
The plus icon at the top of the Inspector can be used to create a new Marker at the current position, which allows you to enter a name
right away. If there is already a Marker at the current position a new Marker is not added.
Markers can be deleted using the minus sign. Hold [Shift] to select more than one Marker for deletion.
 Using the Marker Track

At the bottom of the Inspector is a window that shows the Marker Start time and a Stop At Marker check box. Click-and-drag the Start
time numbers to adjust the Marker position.
[Right]/[Ctrl]-click any Marker for quick access to the Create Arranger Sections and Stop At Marker features.
Navigating Markers
You can quickly jump the playback cursor between Markers in the Marker Track. Click on the Previous Marker button in the Transport, or
press [Shift]+[B] on the keyboard, to jump to the previous Marker. Click on the Next Marker button in the Transport, or press [Shift]+[N] on
the keyboard, to jump to the next Marker.
Jumping between Markers during playback enables quick comparisons between sections of your Song. To jump to a specific marker,
hold [Ctrl]+[Alt]/[Option]+[M] and enter the Marker number in the Recall Marker window. You can also jump to up to seven different Mark-
ers from the Transport/Goto Marker menu.
Song Start and End Markers
When a new Song is created, you can specify a Song Length. The default length is 5 minutes or 151 bars at the default 120 bpm tempo.
At the beginning and end of the specified region, Song Start and End Markers are automatically placed in the Marker Track. These Mark-
ers can be used to define the timeline region to be exported in the Export Mixdown and Export Stems functions in the Song menu, and
they are used by default in the Update Mastering File process.
Right click the End Marker to assign the “Stop at Marker” feature. Playback will stop when the play head reaches the End Marker.
Cut, Copy, Paste and Delete Markers
You can use standard Cut, Copy, Paste and Delete commands to distribute and manage your Markers. To cut or copy a Marker, select it
by clicking its name flag, and either press [Ctrl]/[Cmd]+[C] to copy or [Ctrl]/[Cmd]+[X] to cut, or [Right]/[Ctrl]-click the Marker to open the
pop-up menu and choose Cut or Copy. To paste a Marker, place the cursor at the desired location and press [Ctrl]/[Cmd]+[V]. To delete a
Marker, select it and press the Delete Selected Markers button in the control area of the Marker Track. Alternately, you can delete a
Marker by [Right]/[Ctrl]-click its name flag and choose Delete from the pop-up menu, or by selecting the Marker and pressing [Delete] on
your keyboard.
You can also access these commands in the Edit menu.
If you have cut a Marker and wish to return it to its original position (and have since done other operations that would make using Undo
impractical), press [Ctrl]/[Cmd]+[Shift]+[V] or select Paste at Original Position in the Edit menu.
Stop Playback with Markers
Markers can optionally stop playback when reached by the playback cursor. To engage this option for any Marker, [Right]/[Ctrl]-click on a
Marker and engage the Stop at Marker option, or select a Marker and engage the same option in the Inspector. Note that this cannot be
enabled for the End Marker.
 Using the Marker Track

Create Arranger Sections from Markers
There's a quick way to populate the Arranger Track with sections while working with Markers. Simply [Right]/[Ctrl]-click on a Marker and
select the Create Arranger Sections from Markers option, and the Markers are instantly translated into Arranger sections.
Looping During Mixing
The blue bar at the top of the Arrange view represents the loop range.
Looping a section of audio (for instance a chorus) while mixing allows you to focus on a particular area of your overall Song without hav-
ing to constantly stop, rewind, and resume playback.
To quickly loop a section of audio, first select the audio you want to loop by either selecting a range with the Range tool or directly select-
ing an Event or multiple Events with the Arrow tool in the Arrange view. Then press [P] on the keyboard to set the Left and Right Locators
around your selection. Alternatively, press [Shift]+[P] on the keyboard to ignore Snap while setting the Locators. Finally, click on the Loop
button in the Transport, or press [Num Pad /] on the keyboard, to loop the playback between the Left and Right Locators.
You can manually set the Left and Right Locators to a desired range and then engage Loop in the Transport. To do this, float the mouse
cursor to the top of the Timeline Ruler until you see the Draw tool appear. Then click-and-drag to draw the loop region (Left and Right Loc-
ators) around the area you wish to loop; a tooltip will pop up displaying your current Loop length. Hold [Alt] on the keyboard while drag-
ging to simultaneously engage Loop in the Transport. Left and Right Locators can also be specified by entering them manually into their
respective fields in the Loop portion of the Transport Bar at the bottom of the screen.
You can also manually move the Left and Right Locators by clicking and dragging them left or right in the Timeline Ruler or by clicking the
L and R icons in the Transport Bar.
Loop Length
To render the Loop Length in the Transport Bar (instead of the Start / End values,) simply click the Bracket icon (]) or right-click the loop
range values and choose Loop Length from the contextual menu.
With Loop Length selected, you are also able to choose the timebase for the Loop Length display. Choose from Seconds, Samples,
Bars, or Frames from the right-click contextual menu.
You can also manually move the Left and Right Locators by clicking and dragging them left or right in the Timeline Ruler. To move the
entire range of the loop along the timeline, click and drag the gray line that connects the Loop start and end locators.
To quickly enable or disable looping, double-click the gray line that connects the Loop start and end locators.
Looping During Mixing

## Mixing Down

In most cases, you’ll record multiple Tracks in a Song, but you'll need to mix these Tracks to a stereo format for distribution online, or on
CD or DVD. With Studio One, this simply means saving your mix to a stereo file.
Create a Mixdown
To create a mix of your Song in Studio One, navigate to Song/Export Mixdown or press [Ctrl]/[Cmd]+[E] on the keyboard to open the
Export Mixdown menu.
Location
The top section of the Export Mixdown menu is where you can select a location and name for the mix file. Click on the [...] button to
choose a file location. Click on the file name, type in a new name, and press [Enter] to choose a name for the file. Location defaults to the
Mixdown folder for your Song, but once you set a new mixdown location, Studio One uses that location for further mixdowns until the next
time you close the Song. Mixdowns are titled "Mixdown" by default, but once you set a name, that name is used by default for any further
mixdowns of the current Song.
The Publishing menu lets you choose to send your mixdown to PreSonus Notion software (choose "Send to Notion"), upload it to PreSo-
nus Studio One+, or upload it to a connected SoundCloud account (choose "Upload to SoundCloud"), once the mixdown is completed.
For more information on working with Notion in combination with Studio One, see this section. For more information on working with
SoundCloud, see SoundCloud Support. For more detailed information on uploading to Studio One+ see Studio One+ Integration.
Formats
Available export formats include:
-
Wave
-
AIFF
-
FLAC (16-, 24-, and 32-bit integer)
-
CAF
-
M4A
-
Ogg Vorbis

## Mixing Down

-
Opus
-
MP3
Select the formats for your mix file in the bottom left section of the Export Mixdown menu, choosing the desired attributes for each. Attrib-
ute options will vary by format, but common options include sample rate and resolution. The MP3 and OGG Vorbis formats also offer an
option to export at a Constant or Variable bit rate. The encoder will vary the bit rate during export, allocating more bits to complex pas-
sages and fewer bits to simple ones. This flexibility allows generating higher quality output files compared to the Constant bit rate mode
at the same overall bit rate.
If you want to put your mix on a standard audio CD, create a 16-bit, 44.1 kHz Wave file.
Export Range
Choose the Between Loop option to only export the range of your Song between the Left and Right Locators. Choose Between Song
Start/End Marker to export the range of your Song between the Song Start and End Markers, as seen in the Marker Track. Choosing
Between Each Marker exports separate audio files for the range between each marker in the Song for each Track, placing them in
folders named after the markers. Choosing Between Selected Markers lets you choose a pair of Markers to export the range between.
The duration of the range to be exported is displayed in the Duration field. Note that when Between Each Marker is selected, the Duration
field still shows the full length of the Song, signifying the total length of audio to be exported rather than the length of any one section as
dictated by the Markers.
Target Loudness
The target loudness and peak level requirements of popular online streaming music services vary significantly. Studio One’s Target Loud-
ness Options can save you a great deal of time by optimizing your Tracks for the variety of requirements of these services—while also
ensuring that your mixes won’t be altered by the loudness algorithms employed by these services. Instead, you control how your music
will be reproduced. As it should be.
When using Adjust Loudness, your Tracks are analyzed during export, and loudness and true peak are matched to the selected settings.
Please note that if the dynamic range of the exported file is too big, it's possible to not hit the Target Loudness, since there may be a con-
flict between Loudness and Max True Peak. In these cases, Max True Peak always wins.
Simply tick the “Adjust Loudness” checkbox and select the preset for the intended platform of release.
Entering your own Max Loudness and Max True Peak settings will cause the Preset to jump to “Custom,” which will save these settings
for later use. The streaming service Presets like Apple Music and Spotify cannot be edited or saved.
Adjust Loudness performs the following operations on Export:
-
Max Loudness The loudness of the written file is adjusted accordingly if the analyzed loudness is outside the defined range.
-
Max True Peak If the detected true peak value of the exported file is larger than the value specified, the gain of the final file is
reduced accordingly.
Options
The bottom section of the Export Mixdown menu has several options that affect how the mix file is created:
Choose an output from which the mix is to be created in the Output selection box. Only the Main Out appears in the list, by default. If
there are any Sub Outs in the Console, they appear in this list as well. Check Import to Track if you would like the mix imported to a new
Track in your Song.
Check Mono to generate a monaural mix. This is useful to check for phase cancellation issues between the left and right channels of a
stereo mix when the user is listening through a single speaker.
Check Bypass Master Effects to bypass the Insert effects on the Main Output Channel of the Console when rendering the mixdown.
This is useful if you have inserted effects to simulate the mastering stage, such as a compressor and limiter, but would like to render the
mixdown without them in order to address this in a mastering Project, or to preserve flexibility for another mastering engineer.

## Mixing Down

Check Realtime Processing if you wish to export your mix in real time. This option should be used if your Song requires External Instru-
ments or external hardware processing so that note data and audio flow to and through these external sources during mixdown.
Check Close After Export if you would like to close the Export Mixdown menu after exporting your mix and open the Export path in
Finder/Explorer.
Check Overlap and specify a duration if you would like to add an overlap to the exported range so you can create crossfades between
them later on.
Song Meta-Information
Certain file formats, such as MP3, can contain additional information about the audio which is referred to as "meta-information". In the
Song/Song Setup/Meta Information menu, there are many fields of data that can be filled in for each Song. These fields are used to tag
audio files so that they are labeled correctly for playback in software and various media players. All audio files exported from a Song that
can contain meta-information are tagged with the meta-information supplied here.
At the bottom of the Meta Information menu, you can choose to display the Song’s meta-information when the Song is opened. The
information can also be viewed at any time by selecting Song Information from the Song menu. The Song Information window also con-
tains a Notes tab, in which you can type in any text information about the Song that may be useful later.
The meta-information displayed represents what listeners see in their media players when playing the Song. Displaying this info could
also be helpful in remembering aspects of the Song production later.
Meta-information filled in for any Song is automatically filled in for that Song when it is imported into a mastering Project. For more on
this, refer to the Meta-Information section in the Mastering chapter.
Some of the meta-information entered here also appears at the top of the Full Score and Single Track page layouts in Score view: the
Title of the Song, the Album name, and the Songwriter/Composer. If those items are edited in Score view, they are also changed in the
Song/Song Setup/Meta Information menu. For more information, see The Score Editor chapter.
SoundCloud Support
When you're done mixing down, you can upload your sounds to SoundCloud, a web-based music sharing service, directly from Studio
One. You can also download sounds from SoundCloud (when available) directly into Studio One.
To upload a new mixdown to a connected SoundCloud account as soon as it is created, choose "Upload to SoundCloud" from the Pub-
lishing menu in the Export Mixdown window. The SoundCloud Client opens when the new mixdown is complete. In this dialog, you are
able to upload audio straight to SoundCloud, and set various SoundCloud-specific options as you do so. You can also access the
SoundCloud Client directly by navigating to Studio One/SoundCloud Client.

## Mixing Down

SoundCloud in the Browser
You can find SoundCloud features in the Cloud tab in the Browser.
You can drag and drop audio from the SoundCloud locations listed here just as you would from any other file location, and audio is down-
loaded (if downloads are allowed for the chosen file) accordingly. You can even preview the audio in the Browser.
For instance, you might have a music partner creating beats for you, and he shares that audio directly with you through SoundCloud. You
would browse to that person's SoundCloud folder, listed under the SoundCloud heading in Cloud, and drag the desired audio into the
arrangement. A special Event is placed in the arrangement, and the Transfers menu opens to indicate the download’s progress. When
the download is complete, the waveform appears for the Event and you can proceed as you normally would with any audio material.
TuneCore Integration
PreSonus has partnered with the popular digital music distribution, publishing and licensing service, TuneCore, making the process of
music distribution as seamless as possible within StudioOne.
Create a TuneCore Account
To distribute your music with TuneCore, you first need a TuneCore account. Visit www.tunecore.com to browse their services, compare
available monthly plans, and create your account.
You can easily connect to TuneCore via the TuneCore Client window in Studio One, and TuneCore’s signup web page will appear after
clicking “Connect to TuneCore” from the Client window. You can open the TuneCore Client window from several locations in Studio One:
-
From the “Studio One” dropdown menu, click on the “TuneCore Client” option.
-
Click on the TuneCore button in the navigation bar located on the top left of the start page.

## Mixing Down

-
When exporting a mixdown, select “Upload to TuneCore” from the Publishing options. The “Connect to TuneCore” window will
appear once you finish refining the export options and press “OK”.
-
When selecting “Digital Release…” from the Project dropdown menu, you can choose “Upload to TuneCore” from the Publishing
option here as well.
How to Upload to TuneCore
Once you have an account, you’ll be able to log into your TuneCore account and upload new tracks from the Studio One.
Follow these directions to upload to TuneCore:
1.
Once your song is ready for export, navigate to Song>Export Mixdown.
2.
From the Export Mixdown window, make sure to select the “Upload to TuneCore” option from the Publishing dropdown menu
while you specify the export options you would prefer.
3.
After the export is processed, the TuneCore Client window will appear. Click “Connect to TuneCore”.
4.
Once TuneCore connects, a web browser link will appear where you will be able to sign into TuneCore. After signing in, you’ll be
redirected to Studio One and the TuneCore client window, with your new track included, will appear:

## Mixing Down

Here, you will be able to Add or Remove Tracks and prepare your upload. Once the Song Info / Album Info are included, click
“Upload”.
-
Note, there are two “upload modes” you can choose from: upload singles or upload an album. As you might expect,
choosing “upload singles” will set each song apart as separate single releases after uploading; on the other hand,
choosing “upload album” will group the songs together into one release.
5.
Uploaded tracks will be kept in TuneCore file storage and need to be further prepared via www.tunecore.com before release can
be initiated. For more information about how to finish the upload via TuneCore, check out this help document: https://sup-
port.tunecore.com/hc/en-us/articles/115006689988-How-do-I-create-a-new-release

## Export Stems from your Song

It can be helpful to quickly export individual Tracks from your Song. For instance, you might wish to send the Tracks to someone, to pre-
pare a different mix or remix the Song. The Export Stems feature in Studio One provides an easy way to accomplish this.
Select Tracks and Channels

## Export Stems from your Song

To export stems from your Song in Studio One, navigate to Song/Export Stems to open the Export Stems menu.
Once in this menu, you can see two tabs labeled Tracks and Channels. The list of Tracks reflects the Tracks in the Arrange view, while
the list of Channels reflects the list of Channels in the Console. Muted Tracks and Channels are unchecked by default, and can be iden-
tified by a (Muted) indicator. Select the Tracks and Channels you wish to export by checking each Track or Channel in the list.
You can easily select all Tracks, select only active Tracks, or deselect all Tracks, by pressing the Select All/Active/None buttons below
the Track list.
Note that the audio file created for any selected Track or Channel is the equivalent of soloing the Track or Channel in the Console and
listening to the result. The audio file includes the results of all Inserts and Sends on the Track or Channel. If you don’t want the Inserts or
Sends included in the exported audio, disable them before exporting.
Location
You can select a location and name for the exported files in the top section of the Export Stems menu. Click on the [...] button to choose a
file location. Click on the file name, type in a new name, and press [Enter] to choose a name for the file. The name of each Track in the
Song that is being exported is appended to the user-specified file name.
The Publishing menu lets you choose to send your stems to PreSonus Notion software (choose "Send to Notion"), upload them to Studio
One+ (choose "Upload to Studio One+ ") or a connected SoundCloud account (choose "Upload to Soundcloud"), once the stem export is
completed. For more information on working with Notion in combination with Studio One, see this section. For more information on work-
ing with SoundCloud, see SoundCloud Support. For more detailed information on uploading to Studio One+ see Studio One+ Integ-
ration.
Format
Choose from the Wave, AIFF, FLAC, CAF, Ogg Vorbis, M4A, AAC/ALAC, or MP3 file formats, and then choose the desired resolution
and sample rate. The MP3 format allows the additional option to export at a Constant or Variable bit rate.
Export Range
Choose the Between Loop option to only export the range of your Song between the Left and Right Locators. Choose Between Song
Start/End Marker to export the range of your Song between the Song Start and End Markers, as seen in the Marker Track. Choosing
Between Each Marker exports separate audio files for the range between each marker in the Song for each Track, placing them in
folders named after the markers. Choosing Between Selected Markers lets you choose a pair of Markers to export the range between.
The duration of the range to be exported is displayed in the Duration field. Note that when Between Each Marker is selected, the Duration
field still shows the full length of the Song, signifying the total length of audio to be exported rather than the length of any one section as
dictated by the Markers.

## Export Stems from your Song

Options
The bottom section of the Export Stems menu has several options that affect how the files are created:
-
Check Preserve Mono Tracks if you would like mono Tracks to render mono audio files. If you are using stereo effects with
mono Tracks, you may wish to disengage this option.
-
Check Import to Track if you would like the exported Tracks to be imported to new Tracks in your Song.
-
Check Realtime Processing if you wish to export your Tracks in real time. This option should be used if your Song requires
external MIDI instruments or external hardware processing, so that note data and audio flow to and through those external
sources in real time during the export process.
-
Check Close After Export if you would like to close the Export Tracks as Audio Files menu after exporting your Tracks and
open the Export path in Finder/Explorer.
-
Check Overlap and specify a duration if you would like to add an overlap to the exported range so you can create crossfades
between them later on.
Mixing Suggestions
Before Mixing
The production work done before mixing has a great impact on the mixing process. Here are a few guidelines you may find helpful:
-
Finish the arrangement of your Song before attempting to mix. The addition, deletion, and rearrangement of parts can change
the relationships between all of the parts in your Song, which affects the mix.
-
If any part of your Song is problematic, it is unlikely to work well in a mix. The “fix it in the mix” approach usually leads to a lot of
wasted time, only to achieve poor results. Be sure you are pleased with the individual parts of your Song before attempting to
mix.
-
Some parts of your Song might rely on a certain amount of mixing and effects processing to achieve the desired sound and char-
acter in the arrangement. It is very easy to let this type of “mixing” carry over into mixing the entire Song. If you find yourself work-
ing on many Tracks at once, you are probably mixing the Song, rather than a particular part.
-
If your Song lacks personality, vibe, or feeling before you start mixing, it is unlikely to gain any of these subjective qualities during
mixdown. In this case, take the time to re-record certain parts, rearrange the Song, or even start over from scratch.
Mixing Workflow
While mixing requires an objective knowledge of many tools, the process is an art form. If you were to ask ten mix engineers to mix the
same Song, each mix would sound different. There are no step-by-step or “mix by numbers” instructions you can follow to achieve good
results. The following broad concepts may help guide you in the mixing process.
Balance
Mixing is largely about balance. The various elements in a mix are balanced with each other so that each element can be clearly heard
and contributes as desired to the overall mix. This entails using the faders to vary levels and equalizing sounds so that there is no “com-
petition” between elements with similar frequency content. There is a limited amount of space in the mix, based on individual energy
levels for each frequency in the audible spectrum and the relationships of the sounds within the stereo field.
A popular view on mixing maintains that auditory perception occurs within a three-dimensional space, wherein the principles of mixing
are highly visual. A number of variables determine how we perceive location, including frequency, phase, reflections, and relative amp-
litude (level).
Therefore, while mixing, various elements can be positioned in the 3-D listening space using faders, equalizers, ambient effects, and pan-
ning to achieve appropriate balance across the entire mix.
Busing
Busing can make mixing much easier by creating submixes of certain elements. For instance, a live drum set may be recorded across
eight or more individual Channels. In this case, the drums can first be submixed to their own bus or stereo channel, and then the submix
can be blended into the overall mix. To accomplish this in Studio One, refer to both the Busing and Groups sections of this chapter.
Busing is also used to build on individual Tracks to create a “larger” sound. For instance, a vocal Track might be bused to an FX Channel
with a chorus effect inserted, as well as to a bus where all of the vocals are mixed and sent to a reverb. These various elements are all
mixed using individual faders and add to the overall vocal sound in the mix.
Busing can be used creatively to achieve an endless variety of results. Experiment with this concept to help achieve a unique sound.
Mixing Suggestions

Preparing Your Mix for Mastering
Too often, mixes are sent to the mastering phase of production after they have been compressed, equalized, limited, and generally pro-
cessed to the loudest possible levels. This is usually the result of people comparing their unmastered mixes to finished, mastered, pub-
lished songs. Indeed, it’s tempting to make your mixes as loud as possible while mixing.
However, mixing is mostly about achieving excellent balance. It is not about making the mix loud, especially when compared to mastered
mixes. During mastering, you can bring the overall loudness up without affecting the balance achieved during mixing. But if your mixes
are already as loud as they possibly can be, little can be done during mastering to make the most of the balance you achieved in the mix,
nor can you easily balance one mix with another to create a cohesive album.
Therefore, when listening to reference material (which we highly recommend), try to ignore the overall loudness and just pay attention to
how the individual elements are balanced. Avoid placing compressors or limiters on the master channel of your mix.
Maximizing Computer Processing Power
If you are only listening to playback of previously recorded audio, and not to live inputs being recorded, input and output latency (the time
it takes to get audio into and back out of your computer) is irrelevant. Besides, Studio One’s automatic delay compensation keeps all play-
back Tracks in sync with each other, regardless of plug-in processing. Therefore, during mixdown, the Block Size can be increased to
allow more time for processing to occur before the audio is heard, which enables you to use more plug-ins and other processing.
To adjust the Block Size, navigate to the Studio One/Options/Audio Setup menu (macOS: Preferences/Audio Setup). In Windows, if your
audio interface allows it, as most ASIO devices do, adjust the Hardware Block Size by clicking and dragging the horizontal fader. The
value of the Hardware Block Size is reported next to the horizontal fader. In macOS there is a pop-up menu to adjust Block Size.
In the Windows version of Studio One, the Internal Block Size is locked by default to the same value as the Hardware Block Size. Click on
the Lock selection box to unlock the Internal Block Size. Then click on the Internal Block Size value to choose from the list of available val-
ues.
In macOS there is no difference between Internal and Hardware Block Size.
Rendering and Deactivating Virtual Instruments
Virtual instruments can require a lot of computer resources, which limits the computing power that’s available for other processes. There-
fore, it is sometimes worthwhile to render the audio output of an Instrument Track to an Audio Track and then deactivate the virtual instru-
ment.
The most flexible option you have is to use Track Transform to render Audio and Instrument Tracks and temporarily remove the related
virtual instruments or effects, as described in the Editing chapter.
Alternatively, you can do the following to accomplish this:
1.
Select all of the Instrument Parts on the Instrument Tracks that you would like to render to audio.
2.
Select Bounce Instrument Parts from the Event menu or press [Ctrl]/[Cmd]+[B] on the keyboard. Each Instrument Part is
rendered to an Audio Event and placed appropriately on a new Audio Track.
3.
Click on the Instrument icon on the Instrument Tracks to open the user interface for its virtual instrument and click on the Activ-
ate button to deactivate it. This frees any computer resources previously being used by the virtual instrument.
The same concept applies to resource-intensive Audio Effect plug-ins. You can export audio to a new Track using the Song/Export
Stems function, with the Import to Track option enabled. Then, you can simply remove the original Audio Track, freeing up the resources
formerly used by its effects plug-ins.
Audio Engine Overload
Computers have a limited amount of processing power, and you can reach a point where the system can’t support all of the running pro-
cesses. If this occurs while using Studio One, the Studio One audio engine overloads, causing the application to become unresponsive
or frozen.
If this happens, and Studio One becomes unresponsive for more than 15 seconds, the system is automatically stopped, and the audio
device is suspended. A warning message is displayed to notify you that this has happened.
When you see this message, immediately save your Song , Project or Show. After saving, disable some plug-ins, including audio effects
and virtual instruments, to reduce the amount of computer processing needed to play the Song , Project or Show. When you resume play-
back, the audio engine will function normally. If you see the warning again, try disabling more plug-ins.
This feature is intended to make the experience of using Studio One stable and enjoyable on less-powerful computers. If you are using a
relatively powerful computer, you are unlikely to overload the audio engine.
Mixing Suggestions
