# Setup

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 12–42
> **Slug:** `03-setup`

**Agent topics:** `system requirements`, `audio device`, `MIDI`, `I/O setup`, `content management`, `new song`, `Notion`, `colors`, `customization`, `recovery`, `options`

---

Setup
This chapter contains information about Studio One system requirements, hardware device setup, and software setup. A thorough know-
ledge of this information is helpful before attempting to work in Studio One.

## System Requirements

The following are the system requirements to run Studio One.
macOS® (10.14 or higher) systems
macOS® 10.14 or higher (64-bit only)
Intel® Core™i3 or better
4 GB RAM minimum (8 GB or more recommended)
Windows 10 (64-bit only) systems
Intel® Core™i3/AMD A10 processor or better
4 GB RAM minimum (8 GB or more recommended)
Studio One 6.2 requires Windows 10 20H1 or later (64-bit only”
Additional Requirements (all Systems)
-
Internet connection (needed for installation and activation)
-
Monitor with 1366 x 768 resolution (Retina display recommended)
-
Multi-touch enabled monitor with TUIO support is required for touch operation
-
Content storage:
-
40 GB free hard drive space (Studio One Professional)
-
20 GB free hard drive space (Studio One Artist)
-
2.5 GB free hard-drive space (Studio One Prime)

## Set Up Your Audio Device

Studio One automatically selects an audio device to use for audio input and output, pulling from a list of devices currently installed on
your computer. If you have a PreSonus audio interface, it is selected automatically.
Setup

Then follow these steps to configure your audio device for use in Studio One:
1.
Navigate to Studio One/Options/Audio Setup/Audio Device (macOS: Preferences/Audio Setup/Audio Device) to open the Audio
Device settings window.
2.
Select your audio device:
-
macOS: Select your chosen playback (output) device from the Playback Device menu. Select your chosen recording
(input) device from the Recording Device menu.
-
Windows: Select your device for audio input and output from the Audio Device menu.
3.
Some devices offer a selection of configuration options. If your connected device has those controls, you can click on the [Con-
trol Panel] button next to the device selection drop-down menu and make your changes within the device’s control panel. If your
device does not offer these options, the Control Panel button is grayed out.
4.
Set Device Block Size to fit your needs. Lower settings minimize latency, which is useful when tracking. Higher settings bring
more latency, but give you additional processing power for effects and instrument plug-ins. Generally, you want to pick the low-
est block size that still lets your system perform correctly. If you require higher performance but want to keep latency low, you
can increase the level of Dropout Protection and employ Low-Latency Monitoring, as described here.
5.
When the aforementioned settings are selected, your system’s current total input and output latency, sample rate, and bit depth
are reported below the Audio Setup menus.
6.
Release Audio Device in Background (Windows only) is disabled by default. When engaged, the current audio device is made
available to other applications when Studio One is minimized.
Import/Export Device Configurations
If you have already created a device configuration on a different setup, you can import that configuration into Studio One. You can also
export your device configuration from Studio One and use it on a different setup. Those features are available on the Song Setup page
and are described in the Audio Device Input/Output Setup section of the manual.
Audio Dropout Protection and Low-Latency Monitoring
When you are working with a large amount of audio tracks and virtual instruments, computer performance can limit your capabilities. You
can increase the amount of buffer to help free up computer resources, but this traditionally comes at the cost of greater latency (or delay)
when monitoring audio inputs or playing virtual instruments. Set the buffer too low, and audio dropouts and glitches can occur.
To remedy this, Studio One features Audio Dropout Protection and an advanced Native Low-Latency Monitoring system. Under this sys-
tem, the tasks of audio playback and monitoring of audio inputs and virtual instruments are handled as separate processes. This, in
effect, lets you use a large processing buffer to handle heavy audio playback and effects processing tasks, while keeping latency low for
audio input and virtual instrument monitoring.

## Set Up Your Audio Device

Device Block Size Vs. Process Block Size
The latency that you hear when monitoring audio inputs or playing virtual instruments is based primarily on the Device Block Size that
you specify in the Studio One/Options/Audio Setup/Audio Device (macOS: Preferences/Audio Setup/Audio Device) window. For the low-
est latency, Device Block Size should be set to the lowest setting that provides the performance you need.
The Audio Dropout Protection system uses its own buffer for playback and processing of audio tracks, distinct from the Device Block Size
setting. The size of this buffer (also known as the Process Block Size) depends on the Dropout Protection level that you specify in the Stu-
dio One/Options/Audio Setup/Processing (macOS: Preferences/Audio Setup/Processing) window. If you use Native or Hardware Low-
Latency Monitoring, the Dropout Protection level has no effect on audible latency, though higher levels can affect the responsiveness of
onscreen meters and displays.
As long as the Process Block Size is larger than the Device Block Size you've specified, you have the option to use Native Low-Latency
Monitoring.
Monitoring Latencies
The Monitoring Latencies display shows you the latency values for audio inputs (round-trip, from input to output) and virtual instruments,
based on the current Device Block Size and Dropout Protection settings. The "Standard" column shows the latency for the current set-
tings if you choose not to use Low-Latency Monitoring, while the "Low Latency" column shows values for the Native Low-Latency Mon-
itoring system.
Plug-in Use with Native Low-Latency Monitoring
When monitoring an audio input or virtual instrument through the Native Low-Latency Monitoring system, any inserted FX on the cor-
responding Channel continue to function and can be heard in real time, provided that they add 3 ms or less of latency. Plug-ins that meet
this latency requirement show a green power button in the Console (rather than blue or gray). Any inserted plug-ins that introduce more
than 3 ms of latency are not audible in the monitoring path while a Channel is armed for monitoring or recording under Native Low-
Latency Monitoring. They begin functioning again when recording/monitoring mode is disengaged.
The following plug-in types and configurations are not supported on Channels that utilize Native Low-Latency monitoring:
-
External effects, routed into the system using the Pipeline plug-in
-
Analyzer plug-ins
-
FX Chains that incorporate Splitter devices
Configuring Audio Dropout Protection and (Native or Hardware) Low-Latency Monitoring
To configure Audio Dropout Protection and Low-Latency Monitoring, do the following:

## Set Up Your Audio Device

1.
Navigate to the Studio One/Options/Audio Setup/Processing (macOS: Preferences/Audio Setup/Processing) settings window.
2.
Choose your desired level of protection, if any, from the Dropout Protection drop-down menu. The Process Block Size display
shows you the corresponding processing buffer size. If you want to use Native Low-Latency Monitoring, choose a Dropout Pro-
tection level that sets the Process Block Size to a value that is higher than the Device Block Size you have selected.
3.
For low-latency performance when playing virtual instruments, enable the "Enable low latency monitoring for instruments"
option. If you run into performance issues when using a virtual instrument with particularly high CPU usage, you may want to dis-
able this option.
4.
If using a supported DSP-enabled audio interface, you have the choice to use its onboard Hardware Low Latency Monitoring
(and hardware DSP-based effects when available, as with the PreSonus Studio 192) for incoming audio inputs, or to use the Nat-
ive Low Latency Monitoring that Studio One provides. Enable "Use native low latency monitoring instead of onboard DSP" to
use Native Low-Latency Monitoring, or disable it to use Hardware Low-Latency Monitoring.
-
Note that when using Hardware Low-Latency Monitoring to monitor an audio input, Insert FX do not function on the
related Channel, since the audio input is being monitored before it reaches Studio One. If Insert FX are needed while
tracking, use Native Low-Latency Monitoring instead. To do this, navigate to Studio One/Options/Audio Setup/Pro-
cessing (macOS: Preferences/Audio Setup/Processing) and enable the "Use native low-latency monitoring instead of
hardware monitoring" option.
-
Note that setting Dropout Protection to “Off” allows for the lowest latency possible at the risk of introducing dropouts
when this setting is combined with very small block size settings.
Enabling Low-Latency Monitoring in the Console
Once you've configured your system to use Native or Hardware Low-Latency Monitoring, you can toggle low-latency monitoring on and
off for the Main output as well as any Cue Mix outputs you've specified, by clicking the Enable Low-Latency Monitoring button ("Z", short
for Z-Mix) below the volume fader for the related output. When low-latency monitoring is disabled, the "Z" button goes dark. When Native
Low-Latency Monitoring is enabled, the "Z" button turns green. When Hardware Low-Latency Monitoring is enabled, the "Z" button turns
blue.
Monitoring Mode Attributes
This table describes the primary monitoring methods available in Studio One, and the conditions that must be met to use them.
Type
Z-Mix
Necessary Condi-
tions
Monitoring
Insert FX
Send FX
Standard Software
Monitoring
Disabled
Large Device Block
Size, low Process
Block Size (Dropout
Protection)
Standard
latency
All function
All function
Native Low-Latency
Monitoring
Enabled
Process Block Size
(Dropout Protection)
must exceed Device
Block Size
Native low-
latency
Plug-ins with
3ms or less of
latency func-
tion normally,
all others are
disabled
All function
Virtual Instrument
Low-Latency Mon-
itoring
Enabled
Process Block Size
(Dropout Protection)
must exceed Device
Block Size
Native low-
latency
Plug-ins with
3ms or less of
latency func-
tion normally,
all others are
disabled
All function
Hardware Low-
Latency Monitoring
Enabled
"Use software low-
latency monitoring
instead of hardware
monitoring" option
must be disabled
Hardware low-
latency
No Insert FX
function
All function

## Set Up Your Audio Device

Process Precision
By default, Studio One’s process precision is set at Single (32-bit). If using Studio One Professional, you may choose double precision
(64-bit) from the Process Precision drop-down menu.
Supported Devices
Studio One supports most audio devices, including those that run on ASIO or WASAPI (Windows) or Core Audio (macOS) drivers.
When using a WASAPI audio device in Windows, note that WASAPI offers Exclusive and Shared modes of operation. Shared mode is
the default setting. In Exclusive mode lower latency can be achieved, but other applications (such as Windows Media Player) cannot use
the audio device at the same time. On your Windows computer, navigate to Windows Control Panel/Hardware and Sound/Sound to con-
figure the options for your WASAPI device.

## Performance Monitor

When setting up your audio device (specifically when determining appropriate Internal or Device Block Size, or selecting Single or
Double Process Precision), you should take into account the related performance demands on your computer.
Open the Performance Monitor by selecting it from the View menu, or by clicking on the [Performance] button in the Transport. This mon-
itor displays the current relative overall CPU and disk performance, as well as the performance of instruments and automation.
When these meters approach or reach the top of their range, you may need to consider altering your audio device settings (or changing
the Song, Project or Show) to avoid audible clicks and pops or possible instability. For instance, it is common to lower the Device and/or
Internal Block Size while recording to keep monitoring latency low but then to increase Block Size while mixing to provide as much CPU
headroom as possible for effects processing.
If any playback issues are encountered with third-party virtual instrument or effect plug-ins that have their own multiprocessor support
implementation (e.g., NI Kontakt, FL Studio), it is recommended that this support be disabled in the plug-ins. In this case, Studio One
manages all processor scheduling.

## Set Up Your Audio Device

## Audio Device Input/Output Setup

Software I/O Channels
In most recording applications, audio tracks are directly correlated to the channels of your hardware audio device. In Studio One, there is
a layer of software I/O (input and output) channels between your hardware audio device channels and your Tracks. This setup affords
many advantages over the traditional method.
For instance, let’s say you produce a Song in your studio, using a multi-channel interface, then take your Song file to your friend’s studio,
where you use a different audio interface. Simply connect your friend’s hardware audio device channels to the correct software I/O chan-
nels. When you get back to your studio, the original I/O configuration for the Song is automatically loaded for you, as if you never left. You
can do the same thing if you need to open the Song on your laptop using its built-in audio hardware.
This is possible because Studio One stores I/O configurations with your Song, per computer and per audio device driver, ensuring that
your Song remains highly portable and is never “broken” by changing audio devices.
Audio I/O Setup Menu
Each Track in a Song receives a signal from an input source and routes to an output destination. The input sources and output des-
tinations made available to each Track are determined by the software I/O channel configuration created in the Audio I/O Setup menu.
To view this menu and set up a default I/O configuration for each Song, create a new Song by clicking on Create New Song in the Start
Page and navigate to Song/Song Setup/Audio I/O Setup.
The configuration of the Audio I/O Setup is done within each Song, so that it is possible for each Song to have a separate I/O setup. As
discussed below in Default Device I/O Setup, a default I/O setup can be created so that each new Song defaults to a particular I/O setup
if you desire.
In the Audio I/O Setup menu there are two tabs: one for input configuration and one for output configuration. In each tab a Matrix Routing
view shows the current configuration, with the vertical columns indicating hardware audio device channels (hardware I/O) and the hori-

## Audio Device Input/Output Setup

zontal rows indicating created software I/O channels. Software I/O channels function as the input sources and output destinations avail-
able to individual Tracks in Studio One.
Add or Remove Software I/O Channels
Click on the [Add (Mono)] or [Add (Stereo)] button to add an Input or Output Channel, depending on which tab you are currently viewing.
When a new channel is added, the next unassigned hardware inputs or outputs are assigned to the new channel by default.
Click on the [Add...] button to choose from Studio One’s multichannel options, and also set the new Input or Output’s Label, Format, and
Color. Use the Number option to create many Inputs or Outputs at once. Studio One supports multichannel input formats up to 9.1.6. If
you are adding more than one channel the names will increment automatically (Name, Name+1, etc.). Then click OK to create the chan-
nel(s), and they will be added to the configuration.
You can also use the drop-down field to the right of an Input source or Output destination to choose the desired format, then drag the indi-
vidual channels ( L, C, R, etc.) to the desired interface Input or Output assignments.
To remove any channel, click on the channel to select it and then click the [Remove] button. To rename any channel, double-click on the
name of the channel, type a new name, and press Enter.
Finally, in order for these software I/O changes to occur, be sure to click [Apply] before exiting this menu. If you decide you want to start
over with the original configuration for your device, click [Reset to Default].
Assigning Hardware I/O to Software I/O Channels
Hardware inputs and outputs are assigned to software I/O channels in a matrix router, which is a visual representation of the routing. Soft-
ware channels (mono and stereo) are each given a horizontal row, and hardware inputs and outputs are given vertical columns. The
points at which these rows and columns intersect represent potential connections, or routes, between the hardware I/O and software I/O
channels.
By default, Studio One creates three Input Channels: one stereo and two mono. These channels are labeled Input L+R (stereo), Input L
(mono), and Input R (mono). By default, the stereo Input Channel receives input from the first stereo hardware input pair of your selected
audio device. The two mono Channels receive input from the same stereo hardware input pair.
The Output Channel is labeled Main Out (stereo) and is routed by default to the first stereo hardware output pair of your selected audio
device.
To create a route between software I/O channels and hardware I/O, click on the empty square at the intersection of the desired hardware
input or output and the software channel input or output. A colored square appears with an M, L, or R label, indicating whether the route is
a mono route (M) or the left or right side of a stereo route (L or R).
While it is uncommon for Audio I/O Setup changes to be required in the middle of Song production, the audio I/O routing can be changed
at any time. However, you should be aware that routing changes affect all associated Tracks, possibly switching inputs for audio Tracks,
changing the hardware output for the Main Output, and so on.
When making new routes in the Audio I/O Setup menu, notice the meters to the left of the software I/O channels. By displaying signal
levels on each channel, these meters help you ensure that the appropriate routings have been made.
Default Device I/O Setup
We recommend that you create a default Audio I/O Setup that can be a starting point for all new Songs. This lets you immediately begin
working in your new Song, with little or no preliminary setup.
To do so, create software I/O channels for all of your audio device’s commonly used inputs and outputs and name them appropriately.
Then, click on the [Make Default] button in the Audio I/O Setup menu, and a pop-up window appears to confirm that you wish to make the
current I/O setup the default for new Songs. Click Yes, and from that point forward all new Songs are created with this audio I/O setup.
You can always use the [Reset to Default] button to apply this configuration to a song.
Import/Export Device I/O Configurations
If you have already created a device configuration on a different setup, you can import that configuration into Studio One. You can also
export your device configuration from Studio One and use it on a different setup.
There are two ways to access these features: either navigate to Song > Song Setup, or use [Ctrl]/[Cmd]+, to access the Option-
s/Preferences page. If it is not already selected, click the Song Setup button at the bottom of the page and select the Audio I/O Setup
menu at the top.
The Import/Export buttons are located on the lower right side of the page. To import a device configuration, click Import, navigate to the
location of the file, and click Open. The I/O configuration will replace your current one then.

## Audio Device Input/Output Setup

You can also simply drag-and-drop the device configuration file onto the Audio I/O Setup window. Then the I/O setup will be added to
your current configuration.
Be sure to click [Apply] to confirm the configuration change before you exit the menu.
If you want this configuration to be the starting point for every new Song, click the [Make Default] button. A pop-up window will appear
and ask you to confirm your choice. Click Yes, and from that point forward all new Songs will begin with this audio I/O setup.
To export the configuration of the current device, click the Export button. The default location for the file is *Documents\Studio One\IO
Configurations, but you can navigate to a different location. Click the Save button and the file will be exported with the extension
.ioconfig. You will only need to do this once; the .ioconfig file contains the data for both the Input and Output tabs.
Audition Channel
The Preview Player in the Browser and in the Import File menu uses the Audition channel for audio playback. Any stereo Output Channel
can be used as the Audition channel, allowing you to audition sounds from an output other than your main output.

## Set Up Your MIDI Devices

All MIDI-capable hardware devices are collectively referred to as External Devices in Studio One. There are three types of External
Devices: Keyboards, Instruments, and Control Surfaces. While each device type functions in a slightly different way, there is one menu to
add and configure any External Device. The menu can be found by navigating to Studio One/Options/External Devices/Add Device
(macOS: Preferences/External Devices/Add Device).
Set Up MIDI Keyboards
A MIDI keyboard controller is a hardware MIDI device that is generally used for playing and controlling other MIDI devices, virtual soft-
ware instruments, and software parameters. In Studio One, these devices are referred to as Keyboards. Before recording a performance
with a Keyboard, the MIDI keyboard controller must first be set up in Studio One. Once a Keyboard is set up, it is available at all times for
use in Studio One.

## Set Up Your MIDI Devices

To set up your Keyboard, navigate to Studio One/Options/External Devices (macOS: Preferences/External Devices) and follow these
steps:
1.
In the Options/External Devices menu (macOS: Preferences/External Devices), click on the [Add...] button.
2.
Choose your device from the predefined device list or set this to New Keyboard if you do not see your device in the list.
-
If set to New Keyboard, you may wish to type in a Manufacturer Name and a Device Name in the appropriate fields. This
makes identifying your Keyboard easier.
3.
Specify which MIDI channels to use to communicate with this Keyboard. All MIDI channels are selected by default.
-
If you are unsure of the appropriate MIDI channels to use, just leave this at the default setting.
4.
Engage Split Channels if you would like to create a separate Instrument Track input for each MIDI channel from the Keyboard.
5.
Specify the device to which the Keyboard is sending and the device from which it is receiving via Studio One. Select your device
driver name from the drop-down menu for both Receive From and Send To.
6.
You can choose to use this Keyboard as your Default Virtual Instrument Input by checking the appropriate box. If you are using
only one Keyboard with Studio One, you should check this box.
7.
Enable MPE if your Keyboard is able to transmit MPE data (MIDI Polyphonic Expression). Use the Pitch Range field to specify
the range of the keyboard (the number of keys in chromatic steps). Note that when the Enable MPE box is checked, the MIDI
Channels and Split Channels fields are disabled.
Also, Enable MPE must be active for a virtual instrument if you want to take advantage of this feature. This is done in the Instru-
ment Editor window.
Your Keyboard is now ready for use in Studio One.
-
Click on the "+" button in the External window of the Console to quickly set up a new Keyboard or other External Device.

## Set Up Your MIDI Devices

MPE Data Reduction
Since Note Data Reduction applies to MIDI Polyphonic Expression (MPE) data, some MIDI recording may sound different with reduced
data applied. To avoid issues with MIDI track playback, pull up the Advanced Options dialogue window (Studio One/Options/Advanced
Options) and select the Automation tab. From there, make sure the Reduction Level is set to 0%.
Set Up External Hardware Instruments
In Studio One, an External Instrument is an external MIDI hardware synthesizer, workstation, or other device that can generate or manip-
ulate sound. External instruments are set up globally and then are available for use in any Song. The audio output of an external instru-
ment can be routed through one or more Aux Channels in the Studio One Console, where its volume can be controlled with sample-
accurate automation, its live signal can be processed by the effects plug-ins, and its performance can be included in a Track bounce, an
exported Stem, or the mixdown of a Song.
To set up your Instrument, navigate to Studio One/Options/External Devices (macOS: Preferences/External Devices) and follow these
steps:
1.
In the Options/External Devices menu, click on the [Add...] button.
2.
In the left-hand browser, choose your device from the predefined device list. Set this to New Instrument if you do not see your
device in the list. If set to New Instrument, you may wish to type in a Manufacturer Name and a Device Name in the appropriate
fields. This makes identifying your New Instrument easier.
3.
Specify which MIDI channels to use to communicate with this Instrument. MIDI Channel 1 is selected by default. If you are
unsure of the appropriate MIDI channels to use, just leave this at the default setting.
4.
Specify the device to which Studio One is sending MIDI and the device from which the software is receiving MIDI. Select the
appropriate MIDI device from the drop-down menu for Send To and (optionally) Receive From. It is likely your external instru-

## Set Up Your MIDI Devices

ment is not connected directly to your computer. In this case, your external instrument must be physically connected to another
MIDI device (such as a MIDI interface) that does connect to your computer; you need to select the driver for that device.
5.
You can choose to send MIDI Clock to this Instrument and/or use MIDI Clock Start by checking the appropriate boxes. You
should send MIDI Clock to your Instrument if it has a built-in sequencer or components (such as LFOs) that need to sync to Stu-
dio One. Enabling MIDI Clock Start sends MIDI Clock Start signals to your Instrument.
6.
You can choose to send MIDI Time Code to this Instrument. You can set a Display Offset under Song/Song Setup/General to
correct for time-code variances with external devices.
7.
You can vary the speed at which Automated MIDI CC messages are transmitted, using the CC Automation Interval slider. You
can vary the value between 10-100 ms, with the default value being 10 ms.
8.
Enable MPE if your Instrument has is able to receive MPE data (MIDI Polyphonic Expression). Use the Pitch Range field to spe-
cify the range of the instrument (the number of chromatic steps it can reach). Note that when the Enable MPE box is checked,
the MIDI Channels field is disabled.
Your external instrument is now available for use in any Song. The easiest way to use an external instrument in a Song is to set up an
Aux Channel. This is described in the next section.
Note that if your instrument is also a controller (such as a keyboard workstation), you need to set it up twice. First, set it up as an External
Instrument without a Receive From selection, and then set it up as a Keyboard, without a Send To selection. This allows the keyboard-
controller section of the workstation to be used as a source for Instrument Tracks, while allowing the synthesizer section to be used as an
external instrument.
Linking Aux Channels to Instruments
If you want to sequence and control an external instrument from Studio One, you will need to connect your instrument’s MIDI and Main
Outputs to your interface. MIDI allows you to sequence your instrument, while connection through the main outputs allow you to capture
the actual recording of your instrument. In previous Studio One versions, you had to handle MIDI sequencing and audio recording in two
separate tracks. Fortunately, Studio One now offers a true single track workflow for external instruments.
To actually hear the external instrument as you play, you will need to connect the audio output(s) of your instrument to the available input
(s) of your audio interface. You also need to assign this input within Studio One:
1.
In Song Settings, click onto the Audio I/O Setup tab.
2.
From this window, add Mono or Stereo inputs (depending on the nature of your instrument).
3.
Name and assign a color to the input.
4.
Then, click onto the input(s) that you used to connect the instrument and click Apply.
An Aux Channel allows an external audio source to be monitored through the Console without the need for an associated track. The
incoming audio can be processed by the native plug-in effects, and its volume can be controlled through the sample-accurate automation
provided by Studio One.
An Aux Channel is also useful when working with an external MIDI hardware synthesizer, for example, as you can make changes to the
MIDI data on an Instrument track without needing to record another take to your hard drive. Audio from the device returns through your
audio interface into an Aux Channel, where it becomes a part of the mix like any other track.
Here’s the process:
1.
Click onto the External Devices tab in the Console Navigation settings to open the External Devices panel.
2.
Click the menu arrow for the external device.
3.
Select Edit from the menu to open the control mapping window.
4.
Click the Outputs button.
5.
Select Add Aux Channel at the bottom of the window. An Aux Channel appears in the Console.
6.
If your external instrument has multiple outputs connected to your audio interface, add as many Aux Channels as you need.
7.
Important: Click Save Default before closing the window; we’ll explain in the section below.
8.
Once linked, simply navigate to the Instrument section within the Browser, open the folder labeled “External Instruments”, and
drag your saved External Instrument into the Song Page.
You can now play and sequence your External Instrument just like you would with a Virtual Instrument. Note that since you’re recording
with an External Instrument rather than a Virtual Instrument, you will have to do a real-time export when exporting the song. Running
external audio signals through the Console means that bouncing, rendering and mixdown automatically switches to real-time.
Also, keep in mind that different versions of the Audio I/O setup can be saved for different use cases.

## Set Up Your MIDI Devices

Make an Instrument Track for the Aux Channel
Here's why it was important to click Save Default after adding the Aux Channel. After following the steps in the previous section, the new
Instrument becomes available in the “External Instruments” folder in the Browser / Instruments tab. This enables you to create a new
instrument track with AUX inputs in one step: Simply drag-and-drop the instrument from the Browser onto an empty Track. This auto-
matically creates the Instrument Track with the AUX channels already mapped.
Of course, you can always create an audio Track to record the output of the external instrument if you like. The easiest way to do this is
to use the Bounce Track command, which creates the Audio Track and bounces the audio in one step.
Set Up Control Surfaces
In Studio One, a Control Surface is a hardware device that includes transport controls, faders, and other specialized controls. The control
surface might use MIDI directly or via a special control layer such as Mackie Control.
To set up a Control Surface, do the following:
1.
In the Options/External Devices menu (macOS: Preferences/External Devices, click on the [Add...] button.
2.
Choose your device from the predefined device list. Set this to New Control Surface if you do not see your device in the list. If set
to New Control Surface, you may wish to type in a Manufacturer Name and a Device Name in the appropriate fields. This makes
identifying the Control Surface easier.
3.
Specify the device to which the Control Surface is sending and the device from which it is receiving via Studio One. Select your
MIDI device driver name from the drop-down menu for both Receive From and Send To.
4.
You do not need to specify the MIDI channels your Control Surface should use, as control surfaces use alternative protocols,
such as Mackie Control, to communicate with Studio One.
5.
Your Control Surface is now ready for use in Studio One.
For more information on using Mackie Control devices with Studio One, see Mackie Control.
Custom Placement of Control Surfaces
If you are using multiple surfaces with motorized faders, you can customize the placement of the fader banks so that Channels in the Stu-
dio One Console are spread across your surfaces in the desired order.
To customize this placement, click on Placement in the Options/External Devices menu after adding your surfaces. All ungrouped sur-
faces appear under the Ungrouped tab. To place a surface in a group, select a Group tab, then click-and-drag the surface from the
Ungrouped area to the selected group area. To adjust the order of the grouped surfaces, click-and-drag them left or right. Channels in the
Console appear in order across the surfaces from left to right.
Up to four Groups can be created, to allow for mirroring of Channels across multiple surfaces. This is helpful if you have more than one
location in the studio where you wish to use control surfaces (e.g., an A room and B room or a control room and live room).
Only supported and predefined Control Surfaces appear in the Placement window. User-defined devices do not appear in this window.

## Set Up Your MIDI Devices

Use Your Computer Keyboard as a MIDI Keyboard
You can use your regular QWERTY computer keyboard as a MIDI Keyboard to play virtual instruments and record note data in Studio
One. To do this, add a new device in the Studio One/Options/External Devices/Add Device menu (macOS: Preferences/External
Devices/Add Device), choosing the QWERTY Keyboard device from the PreSonus device folder.
With the device added, to use your keyboard as a MIDI Keyboard, open the interface for the QWERTY Keyboard device by double-click-
ing on it in the External panel of the Console. Any record-enabled Instrument Track then receives input from the QWERTY Keyboard, as
shown in the QWERTY Keyboard device interface. Your keyboard only transmits data to Instrument Tracks while the QWERTY Key-
board device interface is open.
Using the PreSonus FaderPort
If you have a PreSonus FaderPort connected to a computer running macOS or Microsoft Windows, Studio One automatically recognizes
it and configures it for use. Just open a Song, Project or Show to use the FaderPort immediately.
Reconnect Devices
In most applications, when MIDI devices become disconnected while the application is running, you usually have to restart the applic-
ation, and the software may crash. In contrast, if an external MIDI device becomes disconnected while Studio One is running with a Song
or, Project or Show open, the device can be reconnected without restarting Studio One.
If this occurs, navigate to Studio One/Options/External Devices (macOS: Preferences/External Devices) and click on Reconnect at the
bottom of the menu. Then, reconnect your devices and click OK. The devices should now work normally in Studio One.
If an external device is not present when Studio One is started—for instance, if you’re traveling and don’t have some of your gear with
you— the application still runs normally. You should see a warning message that makes you aware of the situation. If your setup fre-
quently changes, you may wish to turn off this warning message by disengaging the Notify Me If Devices Are Unavailable When Studio
One Starts option.
Later, when you start Studio One with the device connected to your computer, Studio One recognizes the device automatically, and it
can be used exactly as before with no further setup required.

## Managing Your Content

Content management and file management can become unwieldy when working with digital audio workstation software due to the sheer
volume of loops, effects, song ideas, individual tracks, and so on. In Studio One, you only need to locate your preexisting content once,
after which all of the locations are remembered. Any content you create using Studio One is similarly managed. In Studio One, your con-
tent is kept in distinct categories.

## Managing Your Content

The following describes the process of managing your content using the Studio One/Options/Locations (macOS:
Preferences/Locations) menu.
User Data
Any content you create using Studio One is automatically stored in the location you specify. This includes Songs, Projects, Shows,
Effects Presets, and all of the files these categories contain. All of your creative output can be logically organized and kept in a single
place, which makes future location and backup a breeze.
When creating a new Song, Project, or Show, the User Data folder is the default save location. While we recommend using this location,
you can specify any save location when a new one is created.
Engage the Enable Autosave option to automatically save any open document at a specified interval of time.
Engage the Use cached plug-in data on save option to make sure that any changes that have been made to the plug-in parameters
are saved when the Song is saved.
Engage the Ask to Copy External Files when Saving Song feature to be given the option to consolidate any outside files to the cent-
ral data folder when saving a Song.
File Types
All supported file extensions are listed in the Studio One/Options/Locations/File Types (macOS: Preferences/Locations/File Types)
menu. Only these supported file types are displayed in the Browser.
It is possible to add file extensions to this list by clicking on the [Add...] button. In the pop-up menu, you can choose an icon, enter the file
extension, and provide a description for the file type. Select a user-added extension from the list and click on Remove to remove it.
Sound Sets
Preconfigured packages of loops and samples are bundled with Studio One. The Browser’s Sound Sets folder makes finding this content
quick and easy. These packages also contain information about each content vendor, which is displayed in the Browser when a package
is selected. Click on the Visit Website link in the Browser for more information about the vendor and the content they supply.
Instrument Library
Studio One includes a native virtual instrument called Presence XT that utilizes a cross-platform sample library format, as well as stand-
ard libraries in Giga, EXS, Kontakt (version 4 and below), and Sound Font (SF2) formats. Using the Instrument Library function, you can
tell Studio One where your sound sets are located, giving you access to them as presets in Presence XT.
To add sound library file locations to your Instrument Library, in the Studio One/Options/Locations/Instrument Library (macOS: Prefer-
ences/Locations/Instrument Library) menu, click on the [Add...] button and specify a file location, then click OK. You can specify as many
locations as you need.
For more information on the Presence XT built-in virtual instrument, refer to the Presence XT section.
VST Plug-ins
When Studio One starts for the first time, most of your plug-ins are located automatically and are ready to use immediately. If Studio One
fails to find certain plug-ins, adding them is easy.
To add any missing VST plug-ins, navigate to the Studio One/Options/Locations/VST Plug-ins (macOS: Preferences/Locations/VST
Plug-ins) menu and click on the [Add...] button, then specify a location and click OK. You can also drag-and-drop any folder from the
Explorer/Finder into the Locations list. Studio One then scans these locations at startup, including searching for new plug-ins you’ve
added. You can always add more locations if needed.
AU and VST 3 have their own pre-set file path in the OS, and for this reason, they are not included in alternative path options.
Failed Plug-ins
If any plug-in fails to start correctly when scanned at startup, a notice appears next to its name in the startup message list, and a warning
message is shown. If the plug-in continues to fail at startup—for instance, if it is not authorized correctly or a required iLok key is not
present—Studio One puts the plug-in in a blocklist and ignores it at startup from that point on.
To reset this blocklist and force Studio One to scan missing plug-ins again at startup, navigate to Studio One/Options/Locations/VST
Plug-ins (macOS: Preferences/Locations/VST Plug-ins) and click on [Reset Blocklist]. The next time you start Studio One, the previously
blocklisted plug-ins are scanned again. If the issues that caused the plug-ins to fail the scan have been resolved, the plug-ins are made
available.

## Managing Your Content

It’s also possible that a third-party plug-in may fail to function correctly while not causing a crash. In this instance you should receive the
error message: "The following plug-ins didn't work as expected: <Plugin_Name.vst3>. Please save your work and restart Studio One."
You’ll then be presented with an option to add the malfunctioning plug-in to Studio One’s blocklist.
VST Format Support
Studio One Producer and Professional support VST 2.4 (including VSTXML for hierarchical parameter structure) and VST 3.
Backup and Restore
If you’re a Studio One+ member, you can use your available Studio One+ cloud storage to backup your complete user settings. You may
create individual backups for different computers, artists or projects. The number of backups is only limited by the available cloud storage
space.
To backup your settings to Studio One+, select Backup and Restore from the Studio One menu. In the Backup and Restore window click
the [Backup Now] button to initiate the backup process. Backups already saved to Studio One+ will be listed in the Restore section of the
window.
To Restore any or all settings from a cloud backup to the current computer, first select a backup from the list, then check which parts of
the backup to restore in the Restore Options list. These include program settings, plug-in thumbnails, I/O configurations, presets, tem-
plates and macros. Any options unchecked will remain unchanged. With a backup and options selected, click the [Restore] button to ini-
tiate the download and restore process.

## Managing Your Content

When restoring a backup that originates from another system and contains Sound Set paths that cannot be resolved on the current sys-
tem, the path is reset to default.

## Creating a New Song

A Song is where all recording, editing, arranging, and mixing takes place. To create a New Song, do one of the following:
-
From the Start page, click on the New Song... button [+].
-
Navigate to File/New Song.
-
Press [Ctrl]/[Cmd]+N on the keyboard.
The New Document Window appears.
Choose Record and Mix (New Studio One Song).
The default name of each new Song is derived from today's date and the Artist name you've selected in the Artist Profile on the Start
page. You can set your own title by editing the text in the Name field.
Song Location
New Songs and all related data are saved to your User Data location, set in Studio One/Options/Locations/User Data (macOS: Prefer-
ences/Locations/User Data). If you like, you can choose a different file location by clicking on the [...] button in the New Document dialog,
and browsing to your chosen location.
When creating a new Song, Studio One will remember the last folder you used for a new Song and assume you would like to save your
work in the same location. If you would like to restore to the default location, right-click the file path and choose “Reset Folder” from the
drop-down menu.

## Creating a New Song

Sample Rate
“Sample rate” refers to the rate at which incoming analog audio is sampled per second during conversion to a digital signal. The most
common setting is the standard sample rate for audio CDs: 44.1 kHz, meaning 44,100 samples per second. Studio One supports sample
rates up to 768 kHz.
The Studio One sample rate should match the sample rate of your audio interface, so by default, the sample rate is set to your current
audio interface’s sample rate, and changing this setting initiates a sample rate change in that device. If the sample rates don’t match, Stu-
dio One resamples all audio files to match the sample rate of the hardware, but this can cause performance problems and should be
avoided. Studio One is capable of recording at any sample rate your hardware audio device offers.
Not all devices allow a third-party software application to change the hardware sample rate. The desired sample rate should be set
before creating a New Song.
File size is directly proportional to the sample rate and bit depth. The higher the sample rate and bit depth, the larger the resulting audio
file is.
Resolution
“Resolution” refers to the bit depth of digital audio, which is related to the audio’s dynamic range. Standard CD audio has a 16-bit res-
olution, which results in roughly 96 dB of dynamic range. Thus, with “CD-quality” audio, the difference between the quietest and loudest
sounds possible is 96 dB. The most common resolution setting in professional recording is 24-bit, which produces a dynamic range of
approximately 144 dB.
Studio One can record audio with 16, 24, 32, or 64-bit (floating point) resolution. Which resolution to use is a matter of preference. If you
are unfamiliar with these concepts, try experimenting with recording at each resolution and comparing your results.
Timebase
The timebase of your New Song determines the way the timeline is represented. The timebase selection can be changed at any time.
You have the option of the following:
-
Seconds The timeline division is an expression of hours : minutes : seconds : milliseconds.
-
Samples The timeline division is an expression of samples.
-
Bars The timeline division is an expression of musical bars and beats.
-
Frames The timeline division is an expression of frames.

## Creating a New Song

Song Length
Here you can specify a length for your new Song, or go with the default setting of five minutes. If you wish to change the length of a Song
once in progress, you can move the Song End marker to the desired end point, as detailed in the Song Start and End Markers section.
You can also change the length of the currently open Song by opening the Song/Song Setup dialog and setting the Song End parameter
to your desired end point.
Tempo
Here you can specify a starting tempo for your Song, or go with the default setting of 120 BPM.
Time Signature
Here you can specify a starting time signature for your Song, or use the default setting of 4/4. A Song can change time signatures as
many times as needed. To learn more, see the Signature Track chapter.
Key Signature
Use this field to specify a global key signature for your Song. If no selection is made, a key signature is not assigned. A Song can change
key signatures as many times as needed. To learn more, see the Signature Track chapter.
File Import
If you have any audio and/or video files you would like to import to your new Song, drag and drop them to this field. Each will receive its
own Track when the Song is created, with video being placed appropriately in the Video Track. If multiple videos are imported, they will
be placed one after another horizontally with no overlap. Note that video import is supported only in Studio One Professional.
Create a Song Template
If there is a particular Song setup you use again and again, it can be helpful to create a template. To do so, first create a new Empty
Song. Next, configure the I/O and create and configure all Tracks, and virtual instruments, effects plug-ins, and any other aspects of the
Song that you need in your template. Then, in the File menu, select Save as Template.
Type in a title and description, choose an image for the Template icon, if you like, and select OK. You can also drag an image from Win-
dows Explorer or Mac Finder onto the image icon to use that image. The exact current state of the Song is now available as a template in
the User Templates tab of the New menu.
Stretch Audio Files to Song Tempo
Enable this option to automatically timestretch imported audio files (that have tempo information) to match your Song’s current tempo.
This is highly recommended to avoid having to manually stretch audio or place Tracks in Timestretch mode.
However, if you do not intend to work with Timestretching in your Song and want to ensure that nothing gets timestretched automatically
by mistake, make sure this option is deselected.
Only audio files with encoded tempo information are stretched automatically with this option engaged. Studio One remembers tempo
information you specify within the Inspector view for any audio file.
Apply Customization
Choose a Customization Preset from this list, if desired. Customization Presets allow you to show/hide specific Studio One features to
optimize your tool set and are covered in greater detail here.

## Working with PreSonus Notion Software

PreSonus Notion is our musical notation application for macOS and Windows. With Notion, you can create full-fledged musical scores for
composing new work or transcription of existing music, working with both note data and audio. Notion can exchange note data and audio
freely with Studio One. Together, they create an ideal tool set for fusing the worlds of composition and production in your musical pro-
jects. This section describes the workflow for sending data between Studio One and Notion.
Sending Note Data and Audio from Studio One to Notion

## Working with PreSonus Notion Software

In Studio One, when you have a Song open that contains note data or audio content you wish to send to Notion, navigate to Song/Send
to Notion to bring up the Send to Notion window. In this window, you have the following choices:
-
Computer Selector This lets you choose to send note data and audio to an instance of Notion running on your own computer
("This Computer"), or to a Notion instance on another computer on your network. If any computers currently running Notion are
on your network, they are listed in this drop-down menu for access.
-
Send Note Data of Entire Song This option sends the note data for all Instrument Tracks in the current Song to the chosen
instance of Notion. A new Score is created in Notion, with instrument parts that mirror the Instrument Tracks in your Studio One
Song.
-
Send Note Data of Selected Tracks This option works similarly to the option above, but only sends note data from the cur-
rently selected Instrument Tracks in Studio One.
-
Send Audio Mixdown This option mixes your Song down to a stereo audio file, and sends the file to Notion, where it opens in a
new Score.
-
Create lead sheet If you have chords in your Chord Track, you can check the box in the dialog, to apply lead sheet formatting to
imported note data.
-
Merge into open document Select this option whether to merge into an existing document (overwriting a previous transfer) or
to create a new document.
You can also send audio files to Notion from the Browser in Studio One. To do so, [Right]/[Ctrl]-click the audio file, choose "Send to
Notion" from the pop-up menu, and follow the on-screen instructions to complete the action. This option is available for 16-bit/44.1 kHz
WAV files only.
Note that upon sending MIDI and/or audio to Notion, Studio One also sends tempo map information, ensuring that tempo and time sig-
nature changes remain in sync between the two applications.
Sending Note Data and Audio from Notion to Studio One

## Working with PreSonus Notion Software

In Notion, if you have a Score open that you wish to send as score, MIDI or rendered audio to Studio One, navigate to File/Send to Studio
One to open the Send to Studio One window. In this window, you have the following choices:
-
Computer Selector: This lets you choose to send score, MIDI & audio to an instance of Studio One running on your own com-
puter ("This Computer"), or to a Studio One instance on another computer on your network. If any computers currently running
Studio One are on your network, they are listed in this drop-down menu for access.
-
Send Audio This option renders audio files from each instrument part in your Notion Score (using internal sounds or 3rd-party
instruments, as appropriate). It then creates a new Song in your chosen instance of Studio One, and creates Audio Tracks within
it, containing the rendered audio for each part in Notion.
-
SendScore This option transfers the score information to Studio One where you can now assign sounds.
-
Send MIDI This option creates a new Song in Studio One and creates Instrument Parts within it, each containing the note data
from the corresponding instrument parts in your Notion Score. If VST instruments are used in your Notion score, instrument and
preset information is also sent to Studio One, to keep your sounds consistent across both platforms.
-
Merge into open document Select this option whether to merge into an existing song (overwriting a previous transfer) or to cre-
ate a new document.
Note that upon sending MIDI and/or audio to Studio One, Notion also sends tempo map information, ensuring that tempo and time sig-
nature changes remain in sync between the two applications.
Updating Audio and MIDI Between Studio One and Notion
If you've already transferred MIDI or audio between Studio One and Notion, and something is changed in either program, feel free to fol-
low the sending procedure again. Repeating the sending procedure from the application in which the change was made to the other
application updates all previously sent MIDI and audio files to match the new information.
Sending a song from Studio One to Notion also sends Lyrics in your Lyrics Lanes, but not Global Lyrics Track content. When sending a
Notion project to Studio One, Lyrics are no longer read-only, but can be fully edited in Studio One.

## Custom Colors

Studio One allows for custom colorization of Tracks, Channels, Players, and more, all via a robust and intuitive Color Selector. To open
the Color Selector:
Song Page
-
Track: Click the leftmost tab of a Track header.
-
Channel: Click and hold on any Channel name at the bottom of the Console.
-
Event: Right-click the Event and click on the colored bar in the pop-up menu.
Show Page
-
Player: Click the leftmost tab of a Player.
-
Setlist Item: Click the leftmost tab of a Setlist Item.

## Custom Colors

Project Page
-
Track: Click the color field on the far left of a Track in the Track List.
Applying a color to a Track will color all Events on that Track, excluding Events that have been colored manually.
The Color Selector’s default view lets you choose any of the below 128 colors by a quick left-click.
Clicking the drop-down arrow at the bottom of the Color Selector opens the Advanced Color Selector.
The Advanced Color Selector contains the following features:
-
+/-: Add or remove new color swatches to the Color Selector.
-
Store/Load Preset: Store and Load Color Selector Presets. These presets contain select sets of swatches. Several custom
themes are included; you may also create and save your own.
-
Reset: Resets the Color Picker Preset to the last loaded Preset.
-
Hex Value: The selected color’s hex value is rendered here. You can copy out of this field to match a color in another applic-
ation, or enter your desired color’s hex value here to choose a color by hand.
-
HSL: Click the HSL button to choose a color by the HSL model of Hue, Saturation, and Lightness. Hue is determined by the rota-
tion of the triangle’s point marked on the color circle; Saturation and Lightness are determined by the placement of the pip inside
the triangle itself. HSL values can also be entered directly into their fields.

## Custom Colors

-
RGB: Click this button to Choose a color by the additive RGB color model using the primary colors of light: Red, Green, and
Blue. Move the pips along the sliders to blend Red, Green, and Blue to create your desired color. RGB values can also be
entered directly into their fields.
Edits to Studio One’s overall color scheme are managed in Studio One >> Options >> General >> Appearance.

## Customization

Customization allows you to selectively toggle the visibility of specific Studio One features from its user interface to create a streamlined
Studio One experience best-suited to your work.

## Customization

While Studio One’s robust feature set allows you to do nearly anything you could want with music and sound, not every task requires
every feature. Both new and experienced users can work more efficiently when presented with a streamlined, non-distracting toolset.
Studio One’s default toolbar
A minimal Studio One toolbar, thanks to the Customization Editor.
Customization Settings can be edited and recalled from the View >> Customization menu.
To create a new Customization Setting via the Customization Editor, choose View >> Customization >> Edit Customization from the
drop-down menu.
To recall an existing Customization Setting, choose it from the list.
Note that Customization is only available for the Song Page.
You can also open the Customization Editor by right-clicking on an area you wish to customize (Toolbar, Inspector, Transport, or
Browser) and selecting Customize… from the context menu.

## Customization

Customization Edit Window
The four tabs across the top of the Customization Edit Window allow you to select which area of Studio One you wish to customize.
Check or un-check the tickboxes to toggle the visibility of the desired features. Any change made immediately is stored in user Settings.
If a factory Setting was selected, a new user Setting is generated based on the factory Setting name.
-
Toolbar The toolbar at the top of Studio One’s Arrange Window.
-
Inspector The Track Inspector located on the left of the Arrange Window.
-
Transport The Transport interface at the bottom of Studio One.
-
Browser The Browser on the right of Studio One.
Once you’ve created a Customization Setting, you can save it for later use or to create a starting point for a new Setting. Use the drop-
down menu at the top of the Customization Edit Window and select Store... From here, you can also Rename and Delete existing Set-
tings.
Choose Delete User Customization to restore all Customization Settings to their factory defaults. Note that this will remove any Set-
tings you have created yourself!
Note that Appearance (color) preferences are available in the General Options menu.
Reverting or Keeping Customization Presets
When loading a Document that has had a Customization Preset applied from a Smart Template via the Apply Preset checkbox, you may
be asked to Keep or Revert the Customization Preset if it is different than the one you are currently using.

## Customization

-
Choose Keep to use the Preset chosen when the Document was created.
-
Choose Revert to use the previously selected Preset.

## Recovery Options

While we pride ourselves in building Studio One in a manner that provides the best possible stability for all users, sometimes plug-ins—
particularly older ones—can introduce conflicts that may result in an unfortunate crash. That’s also why we have auto-save.
In the event that you encounter a crash, you’ll be presented with this Safety Options dialog box:
With it, you can choose to select or deselect startup activations of Plug-ins by type in an effort to troubleshoot what might be causing your
crash. This will help you isolate problematic plug-ins; removing them from your workflow can ensure that they won’t cause a crash again.
You can also force loading of the Safety Options dialog box by pressing and holding <SHIFT> during Studio One’s startup.
Additionally, in the event that you encounter a hard freeze that requires a force quit command to close Studio One, The Safety Options
dialog box will also appear the next time you launch Studio One.
Diagnostics Reporting
In the event that you’d like assistance with a Studio One issue from PreSonus Support, one of the best things you can do is click the
Create Diagnostics Report button on the bottom left of the Recovery Options dialog. This will compile a report for you to attach to a sup-
port ticket, giving your support agent the best information to assist with your issue as efficiently as possible.

## Recovery Options

Your report will be created as a .Zip file that you can attach to the support ticket when you create it at my.presonus.com. Depending on
the options selected, the .Zip will contain:
-
Information about crashed and unexpected behavior
-
Operating system and hardware information
-
A list of installed plug-ins
-
Application log files
You can also access Diagnostics Reporting from the Help drop-down menu at any time.
Open with Options
Right-clicking any document in the Start Page will present a contextual menu that includes “Open with Options.” From here, you can
choose to enable or disable any plug-ins that might be causing issues.

## Recovery Options

Document Profiling
-
Choosing “Profile Document Loading” will open the document with safety options and provide insights into plug-in load times.
-
Choosing “Profile Document Saving” will provide similar insights related to the document’s save.

## General Options

The following options give you a variety of controls over how Studio One looks and operates. Click on each tab in the Studio One/Op-
tions/General (macOS: Preferences/General) menu to access these options.
General
-
Language Choose your language from the list.
-
When Studio One starts Choose the default action to be done upon startup.
-
Do Nothing No Song, Project or Show opens by default.
-
Open Last Song/Project/Show The most recent Song, Project or Show opens.
-
Open Default Song/Project/Show The default Song, Project or Show opens. To set the Song, Project or Show to
open by default, set up the desired item and save it, with the name “default,” to the appropriate folder located at the cur-
rent User Data location set in Options/Locations.
-
Create a New Song A new Song is created and opened.
-
Check for Updates Check for software updates on startup.
-
Enable graphics hardware acceleration (macOS only) This setting is enabled by default. We do not recommend disabling
this mode unless it is necessary to improve downward compatibility between Studio One and third-party plug-ins.
-
Enable High-DPI Mode (Windows only) This setting is enabled by default. We do not recommend disabling this mode. Enabled
improves the look and feel of Studio One on high-DPI monitors when running on Windows.
Note: When running Windows with a high-DPI display, you may find that certain older plug-ins appear quite small on screen, as they
have not been updated for use with high-resolution displays. To change this for individual plug-ins, open the plug-in settings menu in the
plug-in editor tab and enable the Enable System DPI Scaling option (requires Windows 10 version 1803 or higher). Scaled-up plug-in
interfaces will appear blurry when blown up to size, which is expected. Certain plug-ins may not be compatible with this option. Avoid
using this option on plug-ins that offer their own scaling options.
Appearance
Set the color balance for the user interface in Studio One, with separate controls for Background and Arrangement elements.
Independent settings for Plug-Ins and the Score View let you choose between Dark and Light viewing modes. Note that these options
only affect certain Studio One plugins, not third-party plugins. They also do not affect Studio One plugins with a custom interface
(Ampire, Fat Channel, Analog Delay, etc.). The “Colored” option links the Studio One plugin color to the Background and Arrangement
settings.
Your settings can be stored as Presets and shared with other users or archived for personal use. Dozens of presets are provided so you
can customize the appearance of Studio One quickly. Press [Reset] to set the color balance and viewing modes back to factory the set-
tings.
Keyboard Shortcuts
This panel lets you assign and change keyboard shortcuts for features and functions in Studio One. For more information, see Key Com-
mands.
Network
Toggle the "Allow remote control apps to discover this DAW" option on to let compatible networked controllers connect to Studio One.
Touch Input
Here, you can enable multi-touch operation (if you have a compatible display attached to your system), as well as specify which monitor
is to be used for touch input. To specify the current monitor, click the [This] button.

## Additional Options

If you'd like information about the other tabs within the Options dialog window, check out the topics cross-referenced below:

## General Options

-
Locations: Managing Your Content
-
Audio Setup:  Set Up Your Audio Device
-
External Devices: Set Up Your MIDI Devices
-
Advanced:  Advanced Options

## Advanced Options

Studio One offers the following ways to customize your workflow. Click on each tab in the Studio One/Options/Advanced (macOS: Prefer-
ences/Advanced) menu to access these options.
Many of the following options that pertain to editing in Arrange view can be accessed and toggled on or off by clicking the Options button
in the Arrange view toolbar.
Editing
Click on the Editing tab to access the following options:
-
Enable Crosshair Cursor for Tools is engaged by default. It enables a large, white, vertical-and-horizontal crosshair in the
Arrange view that aids in displaying the exact position of the various mouse tools.
-
Locate When Clicked in Empty Space is disengaged by default. When engaged, it allows the timeline cursor to be located
based on clicking in empty space or clicking where there are no Events.
-
Expand Layers After Recording Takes is engaged by default. When this and the Record Takes To Layers options are both
engaged, the layers of each recording take are shown as soon as recording stops. If you prefer for this not to happen, disengage
this feature.
-
Track/Channel names follow active Layer is disengaged by default. When engaged, the name of the active Layer is dis-
played instead of the track name in the Track Header and corresponding Channel.
-
Apply Folder Track Color to Content is disengaged by default. When engaged, it causes all content contained in a Folder
Track to be color-coded with the same color you choose for the Folder Track.
-
Colorize Track Controls is disengaged by default, and in that state, the color you choose for each Track is shown in a small
area in its controls in Arrange view. When Colorize Track Controls is engaged, it causes the whole control area of each Track to
be color-coded with assigned color, for better visibility.
-
Auto-colorize Tracks and Layers is engaged by default. This option applies to importing files, when tracks are created without
using the “Add Tracks” dialog.
-
Show Channel Numbers in Tracks is disengaged by default. Some Tracks do not have corresponding Channels in the Con-
sole (and vice versa). Because of this, Tracks and Channels are assigned numbers separately to avoid gaps in Track or Chan-
nel numbering. This means that in some cases, a Track and its corresponding Channel may be numbered differently. If this
bothers you, enable the Show Channel Numbers in Tracks option to mark each Track with its corresponding Channel number,
avoiding this mismatch.
-
No Overlap When Editing Events is disengaged by default. When engaged, moving or pasting an Event over another Event
deletes whatever is buried beneath, so there is no overlapping data (only the audio crossfades are preserved). If the range being
copied includes data outside an Event, the range selection is treated as if it were part of the Event. So when the range selection
is pasted, it overwrites the identical range at the destination.
Note that the "No overlap" setting only works for note data if "Cut long notes at part end" is enabled at Studio One/Op-
tions/Advanced/MIDI (macOS: Preferences/Advanced/MIDI).
-
Show Event Names shows the name labels inside each Event in the Arrangement view. This is purely an aesthetic difference
and does not change any functions.
-
Show Envelopes on Instrument Parts overlays a graphic representation of controller activity (volume, sustain, etc.). This
does not change any functions. Disengage this to display only the notes.
-
Show Chords on Events adds an overlay to Audio Events in the Arrangement showing detected chords. This requires the
track height to be set to Small or higher.
-
Draw Events Translucent is disengaged by default. It enables the Timeline grid in the Arrange and Edit view to be seen in the
background, through Events. Seeing the grid may help with various editing tasks.
-
Draw Smooth Waveforms adds smoothing to audio waveforms throughout the application. Disable this option if you exper-
ience any degradation in graphics performance or user interface responsiveness (which depends on your specific graphics
engine and hardware).
-
Draw Event Badges is engaged by default. When engaged, a darker field is added around the Event name in the Arrangement
view so they're easier to read.

## Advanced Options

Automation
Click on the Automation tab to access the following options:
-
Automation Follows Events is engaged by default. This means that automation envelopes lock to Events so that moving an
Event with automation “under” it also moves the automation.
-
Disable Events Under Automation Envelopes is also engaged by default. This makes Events unavailable to the mouse tools
while viewing an automation envelope, which helps prevent you from unintentionally editing underlying Events while editing auto-
mation.
-
Automatically Create Automation Tracks for Channels is disabled by default. Engaging this option automatically adds an
automation Track for every new FX Channel, Bus, or VCA Channel that you create in the Console. This helps to retain parity
between the structure of Tracks in Arrange view, versus Channels in the Console.
-
Automatically Add Envelopes for all Touched Parameters is enabled by default. Engaging this option adds an automation
envelope for any automation-friendly parameter when you touch its control.
-
Reduction Level allows you to control the density of new automation data as it is written. This helps reduce the CPU load dur-
ing playback. Since Note Data Reduction also applies to MIDI Polyphonic Expression (MPE) data, some MIDI recording may
sound different with reduced data. To avoid this issue, make sure the Reduction Level is set to 0%. Note that this setting has no
effect on existing automation envelopes.
-
The Default Envelopes for new Audio Tracks selectors let you specify which types of automation envelopes are created for
each new track by default. You can enable or disable Volume, Pan, and Mute.
Audio
Click on the Audio tab to access the following options:
-
Enable "Play Overlaps" for New Audio Tracks is disengaged by default. When engaged, the "Play Overlaps" feature will be
enabled automatically for every audio track you create. For more information, see the Track Inspector section of the Editing
chapter.
-
Enable "Layers Follow Events for New Tracks" is engaged by default. New Tracks will default to having the audio on under-
lying Layers follow the related Event above when moved along the timeline. When disabled, moving an Event with one or more
Layers beneath it detaches that Event from the layers below, making it a permanent part of the primary Layer. This feature can
also be enabled/disabled on a per-Track basis via the Inspector.
-
Use Cache for Timestretched Audio Files is engaged by default. It is described in depth in the Using Timestretch Cache
section of the Editing chapter.
-
Record Tempo Information to Audio Files is engaged by default. When engaged, this option enables tempo tagging for any
audio file recorded in Studio One. The Song tempo at the time position of the recording is saved with the file, so that automatic
timestretching can be accomplished. If another application has issues reading audio files from Studio One, try disabling this
option.
-
Use Dithering for Playback and Audio File Export is engaged by default, and means that PreSonus’ triangular dithering is
applied when the audio signal’s bit depth is reduced from a higher bit depth by a device or during file export. Turn this off if you
would like to use a third-party dithering solution, such as a limiter Insert effect on the Main Output that has built-in dithering with
characteristics you prefer.
-
Use Realtime Processing to Update Mastering Files ensures that real-time processing is used when the mastering file for a
given Song is automatically updated. This is necessary when Songs utilize certain devices, such as External Instruments, that
require a real-time mixdown in order to be included in the mix.
-
Pre-record Audio Input creates a buffer of a length you can specify, which records continuously, even when the transport is
stopped. This saves the audio you create before recording begins. Once recording concludes, the number of seconds of audio
you've specified are available before the point at which recording started.
-
The recorded data is collected in the Input Channels as long as physical inputs are connected. After recording with Pre-
Record enabled, you can reveal the pre-recorded data by pulling the Event-start handle to the left.
-
If recording restarts on the same Track, the Pre-Record data is limited to the last recording’s end, so that data is not
repeated and a seamless join between the two recordings is possible.
-
Record Offset allows you to input a value, in samples, by which any recorded audio should be offset in the arrangement,
thereby compensating for device/driver latency.
-
Ignore Audio Device Timestamps (Windows only). Studio One uses the system clock by default, because some ASIO drivers
have incorrect timestamps. This setting can be disengaged, but if you experience erratic behavior such as a jumping playback
cursor, re-enable this setting.

## Advanced Options

MIDI
Click on the MIDI tab to access the following options:
-
Timecode Follows Loop is engaged by default and allows MIDI Timecode to remain in sync when Loop is active in a Song, Pro-
ject or Show. With this disengaged, MIDI Timecode continues to run linearly (counting up) while Studio One's transport is loop-
ing.
-
Reveal Precount Notes is disengaged by default. Engage this option to retain any MIDI notes played during the count-in when
Precount is enabled. This can be helpful when playing in parts that start just before the downbeat.
-
Chase Long Notes is engaged by default. When engaged, if playback starts after a note start, the note is played as though its
start time were at the position at which playback started. For instance, if a synth pad note starts at bar 1 and lasts through bar 8,
and playback is started at bar 4, the note plays from bar 4 as it would normally from bar 1. With this option disengaged, in the
above example, the note would not play at all.
-
Cut Long Notes at Part End is not engaged by default. When engaged, this means that notes are cut at the end of a Part
where it would otherwise extend beyond the Part end. This effectively places the note-off at the Part End.
-
Enable Retrospective Recording is engaged by default. When engaged, all incoming MIDI data is captured for each Track,
even when not recording. This buffer can be recalled and placed at the desired location in the Song.
-
Record Offset allows you to input a value, in milliseconds, by which any recorded musical performance should be offset in the
arrangement, thereby compensating for device/driver latency.
Console
Click on the Console tab to access the following options:
-
Enable Undo Enable this option to allow undo for changes in the Console, such as fader moves and channel mutes.
-
Colorize Channel Strips Enable this option to apply channel color coding to full channel strips in the Console. Normally the
color only shows on the channel labels. This sort of enhanced visual reference can be helpful when trying to navigate large
Songs.
-
Colorize Plug-in Header Enable this option to apply channel color coding to the open editor window of a plug-in. This is handy
when the same plug-in is being used for several Console Channels (the PreSonus Compressor, for example).
-
Auto-expand Selected Channel When enabled, this option makes it easier to view expanded Channels in the Console one at
a time. Double-click the first Channel to expand it, and when the next Channel is selected, two things happen: The currently
selected channel auto-expands, and the previously selected channel collapses. If you hold [Alt]/[Option] and click the second
Channel, the previous Channel does not collapse.
-
Fader Mode This sets the mouse behavior for channel faders in the Console. Choose Touch to require clicking on the fader
handle itself before dragging it to the desired position. Choose Jump to allow clicking anywhere on the travel of the fader to set
its position.
-
Plug-In Menu This changes the style of the local Plug-In menus everywhere in the Console, the Inspector and the Channel
Editor. Choose Basic for a simplified list of Plug-Ins sorted by folder (including custom user folders). Choose Advanced for an
expanded browser-style view with search and sort options (similar to the Plug-Ins tab of the Browser). Changing this option
changes the appearance of all local Plug-In menus throughout the Console.
-
Audio Input follows SelectionEnable this option to automatically engage Record and Monitor mode for any Audio Track you
select.
-
Instrument Input follows Selection Enable this option to automatically engage Record and Monitor mode for any Instrument
Track you select.
-
Solo Follows Selection With this option enabled, once a track is soloed, selecting a different track causes the newly selected
track to be soloed. When this option is disabled, tracks stay soloed until solo is disengaged.
-
Channel Editor follows Selection is engaged by default and causes currently viewable channel devices, such as virtual
effects or instruments, to automatically switch when a Channel is selected. This ensures you are only viewing the devices
related to the selected Channel.
-
If you would like Audio or Instrument Track monitoring to be enabled automatically when recording is enabled on a Track,
engage the Audio Track Monitoring Follows Record and Instrument Track Monitoring Follows Record options.
-
Audio Track Monitoring Mutes Playback (Tape Style) mutes playback of any pre-existing audio on Audio Tracks that have
monitoring enabled.
-
Cue Mix Mute Follows Channel Enable this option to mute all other tracks within a Cue Mix when a channel in that mix is
soloed. Disable this option to cause other channels in the Cue Mix to continue playing when a channel within that mix is soloed.
-
NOTE When this option is disabled, Cue Mix sends are not available in busses and FX channels. In this state, Cue Mix
sends on channels are routed directly to the Cue Mix output

## Advanced Options

Synchronization
Click on the Synchronization tab to access the following options:
-
Sync to External Devices Click this box to make Studio One follow incoming MIDI Time Code (MTC). Note that some
MIDI devices only transmit MIDI clock data, not MTC. Studio One requires a greater degree of accuracy than a simple
MIDI clock can provide. For conversion from SMPTE, an outboard synchronizer is required. For additional accuracy, using an
external word clock (master) is recommended.
-
MIDI Time Code Select the device that will receive MIDI Time Code (MTC). The gray field to the right of the device name indic-
ates the current status of MTC transmission.
-
MIDI Machine Control Select the device that will receive MIDI Machine Control (MMC).
Services
Studio One gives you the ability to selectively enable and disable particular services, or modules, that enable specific features. This may
be helpful when troubleshooting. For instance, if an ARA plug-in seems to be causing a problem, you can disable the ARA service to see
if that resolves the issue. This kind of troubleshooting enables the technical-support team to quickly locate and resolve specific issues
with your computer system and to identify any previously unknown problems in the program.
All services are enabled by default. To disable any service, click on the Services tab in the Studio One/Options/Advanced menu
(macOS: Preferences/Advanced) and click on the confirmation button, paying special attention to the disclaimer message. Then click on
any service in the list and click on the Disable button to disable that service. You must restart Studio One for these changes to take effect.
If a service has been disabled, follow the instructions above, and click on the Enable button for the service in order to re-enable it. Again,
Studio One needs to be restarted for any of these changes to take effect.
Video
Click on the Video tab to access the following options:
-
Set song frame rate to video frame rate when importing video file is an especially helpful option when you want to com-
pose a soundtrack while viewing the video.
-
Automatically create audio track for sound from video gives you the option to edit the video audio like any other audio
event in the arranger window. Otherwise, the video’s audio file is restricted within the Audio Sub-Track.

## Advanced Options
