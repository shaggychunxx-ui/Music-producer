# Spatial Audio

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 321–338
> **Slug:** `12-spatial-audio`

**Agent topics:** `Dolby Atmos`, `spatial audio`, `renderer`, `immersive`, `ADM`

---

Spatial Audio
In Studio One, the term ”Spatial Audio” is used to describe any format that involves output channels beyond traditional 2-channel
(left/right) stereo. Spatial Audio formats supported by Studio One include Surround and Dolby Atmos.

## Spatial Audio Formats

In Studio One,the term "Spatial Audio" is used to collectively describe the following formats:
Surround
In Studio One, “Surround” refers to multi-channel audio configurations that use traditional, channel-based panning to control the place-
ment of sounds within a multi-speaker array soundscape. Unlike Stereo or Mono channels with simple left-right panning, Surround Chan-
nels feature a spherical panner for positioning a sound anywhere around a listener. A Song created in Surround will create a generic
multi-channel audio file at its Output and on export.
Dolby Atmos
Dolby Atmos is Dolby’s proprietary spatial audio format, first popularized in audio for cinema. A Song in Dolby Atmos format will feature
the Dolby Atmos Renderer within the Main Out Channel, which handles the final mix encoding.
Dolby Atmos Songs include three important concepts not found in Surround: Bed, Objects, and Metadata.
-
A Bed is composed of multiple Channels utilizing traditional Surround Panners, just like the Channels in Surround, and serves
as the foundation of a spatial audio mix. Mono, stereo, and multi-channel sources up to 9.1.6 are mixed into a Bed in the Dolby
Atmos Renderer. The Dolby Atmos bed supports formats up to 7.1.6.
Spatial Audio

-
Objects utilize the Object Panner to position a sound object in 3D space. Dolby Atmos allows for up to 118 Objects to be posi-
tioned in this manner. Objects are limited to mono and stereo sources and must be routed to the Main Output to be processed by
the Dolby Atmos Renderer. Objects cannot be sent to an LFE (Low Frequency Effects) output.
-
Metadata Dolby Atmos productions also feature metadata, responsible for the panner automation of objects, binaural encoding,
and downmixing.
Binaural
A Binaural audio signal renders a spatial audio mix down to a two-channel mix in a way that conveys spatial audio imaging to head-
phones, without the need of a multi-speaker installation. This is accomplished through the Dolby Atmos Renderer that is discussed in
greater detail below.
Spatial Audio is supported in Studio One’s Song Page, not on the Project or Show page.
Speaker Configuration Nomenclature
Spatial Audio speaker configurations are typically described in an X.Y.Z  nomenclature, where:
-
X=the number of speakers in the horizontal surround array
-
Y=the number of subwoofers, or Low-Frequency Effect (LFE) speakers
-
Z=the number of height, or vertical speakers
A common speaker configuration for home theater use is 5.1; five horizontal speakers (Left, Center, Right, Surround Right, and Surround
Left) and one subwoofer.
With the increase in popularity of Dolby Atmos, 7.1.2 configurations employ seven horizontal speakers, a subwoofer, and two vertical-
throwing speakers, typically ceiling-installed.
Requirements for Working in Spatial Audio
Spatial Audio hardware requirements
You don’t need an expensive 7.2.2 speaker setup in your studio to work in Dolby Atmos. Select the Binaural headphone option in the
Dolby Atmos Renderer, and the renderer will take care of the Object positioning and downmixing before sending the binaural signal to
your headphones.
For work in Surround, there is no Dolby Atmos Renderer. As such you will need an audio interface and speaker setup in your studio that
matches or exceeds the speaker configuration of your Song(s) in order to hear any signals panned to speakers outside of basic L/R ste-
reo. Use the Line Outputs of your audio interface to connect your speakers. More info on that follows below.
Sample rate and block size requirements
-
Surround Songs do not have any sample rate or block size requirements.
-
Dolby Atmos Songs require a sampling rate of 48 kHz or 96 kHz and a device block size of 512 48 kHz and 1024 for 96 kHz.
The Dropout Protection size may be changed automatically to allow a smooth workflow.
Creating a new Song in Spatial Audio
From Studio One’s Start Page, click “New,” followed by the “Mix in Surround” Template.
You’ll be presented with three options:
Requirements for Working in Spatial Audio

Dolby Atmos Choose this to create a Song in the Dolby Atmos configuration. Choose from the following sub-options:
-
Bed Format to choose the configuration of your traditionally-panned elements
-
Monitoring Format to choose your speaker configuration. Choose the configuration that best matches the speaker array in
your studio.
-
Sample Rate Choose from 48 kHz or 96 kHz.
Surround Choose this to create a Song in Surround. You’ll be presented with the following options:
-
Output Format Choose the configuration that best matches the manner in which you want your music to be listened to. You’ll
need a matching speaker configuration in your studio.
-
Sample Rate Choose from 44.1 kHz to 192 kHz.
Dolby AtmosTutorial Choose this to open the Dolby Atmos Tutorial, an interactive guide we’ve created to help you learn the Dolby
Atmos workflow!
Song setup
If you’ve created a new song from the Mix in Surround Template, your Song is already configured for Spatial Audio.
You can change the Spatial Audio configuration of a Song at any time by navigating to Song Setup > General > Spatial Audio.
From here you can configure your Spatial Audio Mode, Bed Format, Output Format, and Sample Rate.
Speaker mapping
Once you've created a new Song in Spatial Audio, you’ll need to map your speakers so that each speaker receives its appropriate output
signal from Studio One.
To configure your speaker mapping, go to Song Setup > Audio I/O Setup > Outputs.
Click the field to the right of the Main Out listing to select the Main Output format to choose the option suitable for the intended format of
your Song. The default speaker mapping for your chosen format will populate the Outputs.
Here’s an example of typical speaker mapping for a 5.1.4 Dolby Atmos setup with two headphone outputs. Individual output channels
(such as L, C, R, etc.) can be dragged in this setup menu to route them to the desired audio interface outputs.
Creating a new Song in Spatial Audio

For Dolby Atmos binaural monitoring, running a separate headphone output is recommended, but not required.
Once you’ve set up your speaker mapping for your studio/interface, you may opt to click “Make Default” or “Export” so you don’t have to
repeat this process for every song!
Input Mapping
To configure your input mapping, go to Song Setup > Audio I/O Setup > Outputs.
Studio One supports multichannel input formats up to 9.1.6. You can use the drop-down field to the right of an input source to choose the
desired format, then drag the individual input channels ( L, C, R, etc.) to the desired interface inputs.
Creating a new Song in Spatial Audio

You can also use the “Add…” button to add additional multichannel inputs.
Creating a new Song in Spatial Audio

Mapping Audio File Channels
To easily customize Speaker File Mapping from multichannel Events (3 channels and above), [Right]/[Ctrl]-click onto an Audio Event and
click onto the display next to the “Speakers” option from the drop-down window.
You can also access the Speaker File Mapping window by clicking onto the wrench icon next to the “Speakers” option from the Event
Inspector.
The “Map Audio File Channels” window serves two purposes:
1.
Confirm the speaker format: Most channel counts match to one known speaker format, but in some cases, the configuration may
need revision. For instance, "5.1.2” and "7.1" have the same channel count. In these situations, Studio One uses the most likely
format and a “?” is displayed behind the format in the browser and the inspector. The Map Audio File Channels pop-up editor
enables you to define the correct speaker format. Once you press “Confirm,” the “?” beside the speaker configuration format will
disappear.
2.
Remap Audio File Channels to Speakers: The mapper also allows you to define how the audio file channels are mapped to each
individual speaker. To remap the Audio File Channels, click and drag your Audio Files on the right side of the window up or down
until they are beside the speakers you wish to map them to.
Note: by default, the items are sorted by speakers. It is also possible to swap sides and sort the items by Audio File Channels. To do this,
click onto the two way arrow icon above the list of Audio File Channels items.
Creating a new Song in Spatial Audio

Track Format Configuration
Tracks in Studio One support mono, stereo, and multichannel content up to 9.1.6. You can set a Track Format when creating a new
Track, or change it at any time from the Track Configuration drop-down menu on the Track’s header.
Mono and stereo Tracks are indicated with single-circle or two-cirlce icons, respectively. Mono and Stereo format can be toggled with a
single click of this icon.
All other surround formats are indicated by the established speaker count convention of 5.1.2, 7.0, etc.
Tracks are covered in more detail in the Audio Tracks topic.
Mixing in Spatial Audio
Surround and Dolby Atmos both employ robust panners to support spatial audio. To change a Channel’s Panner, right-click on the Chan-
nel’s Panner Micro View and choose the desired format from the drop-down menu.
Note that when converting a mono or stereo channel to an Object, Studio One conveniently preserves the current pan position.
Bed and Objects
Channels in a Dolby Atmos mix are defined as either a Bed or Objects. To change a Channel’s type from a Bed to an Object, make sure
it’s routed directly to the Main Output Channel, where it will be processed by the Dolby Atmos Renderer. Then, select “Spatial Object Pan-
ner” from the Channel’s Panner Micro View menu.
Surround Panner
The Surround Panner is responsible for positioning your Channels in a Surround setup or a Dolby Atmos bed. The top half of the panner
displays the horizontal speaker configuration and signal positioning. The bottom half displays the vertical. The human head graphic in the
center represents the position of a person listening to your music. We’ll call it “The Listener.”
Mixing in Spatial Audio

Mixing in Spatial Audio

At the top left of the Surround Panner, you’ll find the current upmix/downmix information. The number on the left is that of the channel’s
speaker format; the right is that of the Dolby Atmos bed. In this example, a 7.1.2 .WAV file is being panned into a matching 7.1.2 bed, but
the formats are not required to match.
On the top half of the Surround Panner, Click and drag the arrowhead left or right to position the primary signal source. Click and drag the
arrowhead toward or away from The Listener’s head to affect the signal’s size. Size can be locked using the lock icon on the top right;
hold [Alt/Opt] to lock the current direction. Click the Snap button on the top right to toggle snapping the Direction to its nearest speaker.
Speaker channels are represented in the Surround Panner via labeled bubble icons.The number of bubbles you see will be dependent
upon the Channel configuration; two bubbles for stereo and up to 14 bubbles for 9.1.6. Click and drag the bubbles to affect the signal’s
spread. You can click any of the bubbles on the outside of the circle to toggle a mute function, removing them from the output of the selec-
ted Channel.
Speaker outputs are represented by speaker icons. Click any of them to mute, or [Opt/Alt] click to mute all speakers. A note on LFE mut-
ing: When the input configuration doesn't have a LFE channel but the output does, LFE send mix routing is muted by default. It can be
toggled with the LFE button on the button right.
The bottom half of the Surround Panner will only be available if your Output Format includes height speakers. Click and drag the bubbles
to control the Elevation.
The bottom of the Surround Panner hosts three other options:
-
Disable Center to disable the Center speaker output
-
Center Level to adjust the overall level of the Center speaker
-
LFE Level to directly control the amount of signal sent to the Low-Frequency Effect output.
Direction, Elevation, Size, and Spread values can all be entered manually by double-clicking on their respective values.
Note that setting the Elevation value to 100% doesn't exclusively pan the signal to top speakers only.
Changing the Channel format (from Stereo to 5.1 or similar) will re-load the Default preset for the Surround Panner, and new Channels
will also be loaded with the Default preset.
Balance View
The Surround Panner’s Balance View provides additional control over Balance Amount and Direction and can be used to shift the com-
bined source signal horizontally in any direction. To access it, right-click the Channel Panner and select Balance View, or click the Bal-
ance button on the top right of the Surround Panner.
Click and drag the blue bubble to move it to the desired position around The Listener. Activate Snap and drag the bubble to the outermost
perimeter of the display to snap it to a single speaker.
Mixing in Spatial Audio

Spatial Object Panner (Dolby Atmos)
The Spatial Object Panner is used to position the currently-selected Channel’s sound in 3D space. The top half of the Object Panner
depicts the position of the Object on the X and Y axes, the bottom half depicts position of the Object on the Z and X axes.
Click and drag the Object bubble to move it to the desired location in 3D space. All axes are independently automatable.  Bubble colors
match the colors assigned in The Console.
Mixing in Spatial Audio

Click the Snap button on the top right to auto-snap the Object to the nearest speaker. X,Y, Z, and Size values can all be entered manually
by double-clicking on their respective values.
Third-party Panners
Studio One also supports third-party panner plug-ins. If you’ve got any installed, they will appear in the Channel panner Micro View’s
right-click menu. Please note that some third-party effects may display here that are not suitable for this purpose.
Mixing in Spatial Audio

Sends in Spatial Audio
Sends can take advantage of Spatial Audio panning. Click on the send panner in the Micro View to access a full-sized panner for editing.
Note that “Lock Pan to Channel” is only available if the source Channel format matches the target Channel format.
Any time a Send is routed to a surround FX or Bus Channel, the Send Panner is replaced with a Surround Panner. This allows for accur-
ate FX placement of any source. Note that the Channel and Send Panner formats need to match for the “Lock Pan to Channel” option to
work.
A send panner cannot be a Spatial Object panner.
Remapping Effect Channels in Spatial Audio
Any effect can be used in the surround audio format. For any mono, stereo and surround plug-in, the available processing channels can
be individually mapped to outputs or muted.
The current effect speaker configuration is displayed on the top center of the plug-in header next to the wrench icon. Note that effects that
are natively capable of surround adapt to the song configuration (e.g. 7.1.2). When effect configuration is below song configuration (e.g.
when effect is configured to Stereo and the song is configured to 7.1.2), click onto the wrench icon to access speaker channel mapping.
From within the "Speaker Mapping'' dialog, channels can be reordered by dragging from their handle (right hand side). Simply click and
drag the desired outputs vertically to re-assign their speaker channels. You can also click the buttons in the FX column to bypass output
to individual speakers.
The plug-in output automatically reverts to Studio One’s routing so the signal flow is correct. Additionally, the mapping settings for each
plug-in speaker format combination are automatically stored and restored when a new plugin instance is inserted. As long as the speaker
formats of the source and destination channels are the same, you can copy plug-ins with custom plug-in speaker mapping settings to
another track.
Mixing in Spatial Audio

In this example, Analog Delay - a stereo effect - has had its Left and Right outputs mapped to the Left Surround and Right Surround out-
puts.
Special Multichannel Functionality
Phaser, Flanger, MixTool, Level Meter, and Spectrum Meter all offer special functionality for Spatial Audio that varies per plug-in. For
more on these specific plug-ins, visit Built-in Effects.
Mixing in Spatial Audio

## The Dolby Atmos Renderer

## The Dolby Atmos Renderer

The heart of Dolby Atmos is its renderer. It will be automatically added to its own special slot on the Console’s Main Output Channel if
Dolby Atmos is selected in the Song Setup Menu. All audio and pan information that is routed to the Main Output of the Console is pro-
cessed by the Dolby Atmos Renderer before being passed to your speakers and headphones. Click “Dolby Atmos” in the Main Output
channel to show/hide the renderer.
The Dolby Atmos Renderer also provides essential options for export and monitoring in Dolby Atmos. Here you can set the bed format
and monitor speaker configuration of your Song, as well as change the headphone output format (Stereo or Binaural).
-
Volume sets the output level of the renderer.
-
Bed Format determines the speaker format for Bed Channels. Changing this option will immediately reconfigure all Bed Chan-
nels to match.
-
Speakers set this to match the speaker configuration of your studio for the most accurate monitoring possible.
-
Headphones choose from two headphone monitoring modes:
-
Stereo creates a simple stereo downmix, bypassing the renderer’s binaural mode settings for Bed and Object Chan-
nels.
-
Binaural employs the Dolby Atmos Renderer’s binaural mode settings to virtualize a multi-speaker setup to deliver the
perception of space and dimensionality through two stereo channels in headphones or earbuds.
-
Note: “Enable Additional Headphone Output” must be selected in the Renderer Options menu for the Stereo
and Binaural options to appear.
-
3D Room Display This section displays the 3D positioning of Objects in relation to The Listener’s perspective. Click and drag to
rotate in 3D space, or click any of the icons at the top of this section to select from preset views.
-
Dolby Atmos Channels The list of Channels processed by the Dolby Atmos Renderer, with metering.
-
When working in Stereo mode (accessed via the Headphone drop-down menu), Object Channels will be displayed
here. Click on any of them to access their panner.
-
When working in Binaural mode, both Object and Bed Channels will be displayed here, each with their own Binaural
Mode drop-down menu.
-
The Bed channels can be soloed or muted in the Renderer. Each Dolby Atmos Channel has its own mute/solo button.
When an object is muted from the Dolby Atmos Renderer or the channel itself, it is indicated by its representation in 3D
view.
-
Note that the Mute/Solo state of the Renderer is meant to be used for real time monitoring, allowing you to focus on indi-
vidual channels of the bed as you mix. It is not included in master file exports!
-
Binaural modes Click to the right of any Channel in the renderer to access the drop-down menu to choose from three binaural
modes. These Near/Mid/Far settings are measures of a virtualized distance between an Object or Bed and the listener's head.
The Binaural mode metadata is applied to headphone output during monitoring, recording, or playback of a master. This
metadata is not included with speaker processing and is solely intended for mixing and listening on headphones.
-
Note: Since the Dolby Atmos Renderer contains its own dedicated headphone output, you may wish to mute any Output
Channels in Studio One’s Console that are also routed to your interface’s headphone outputs. Otherwise, you could
end up hearing a redundant copy of Studio One’s Main Out on top of your Binaural headphone mix!
-
Metering The Dolby Atmos renderer provides three sets of meters:
-
Bed Thelevels (in dB) of the Bed channels, located on the left of the renderer.
-
Loudness meter The loudness of signals passing through the renderer. It can be configured among the following
options from the drop-down menu at the top of the meter:
-
Loudness in LU or Loudness in LUFS (must be enabled in options menu)
-
EBU+18 Scale (togglable.)
-
Out The final levels (in dB) output by the renderer, located on the right.
Dolby Atmos Renderer Options
The Renderer options are accessed by clicking the wrench icon at the top right of the renderer.
-
Enable Additional Headphone Output Tick to enable/disable the dedicated headphone output. Required for using Binaural
Mode, this option allows you to monitor from speakers and headphones simultaneously and independently!
-
Loudness Metering Tick to toggle display of the Loudness Meter in the renderer.
-
Downmix and Trim Options These options grant you fine control when downmixing a Dolby Atmos Song to a non-Dolby
Atmos surround format. In general, the downmix options are used to monitor a multi channel mix in a format with a lower channel
count (such as stereo) as it would be played if the Dolby Atmos track is played through a more basic speaker setup (at home, on

## The Dolby Atmos Renderer

a mobile device, etc.). You get independent controls for
-
5.1 and 5.1.x Downmix
-
Standard Lo/Ro - default Downmixes to 7.1 and then to 5.1 using the coefficients:
-
Ls = 0 dB × Lss + 0 dB × Lrs
-
Rs = 0 dB × Rss + 0 dB × Rrs
-
Dolby Pro Logic IIx Downmixes to 7.1 and then to 5.1 using the coefficients:
-
Ls = Lss + (–1.2 dB × Lrs) + (–6.2 dB × Rrs)
-
Rs = Rss + (–6.2 dB × Lrs) + (–1.2 dB × Rrs)
-
Direct Render with Room Balance Renders from Dolby Atmos to 5.1 (without downmixing via 7.1) by apply-
ing an updated Dolby rendering algorithm that reduces the comb filter effects associated with phantom imaging
of objects positioned halfway between the front and rear of the room.
-
Direct Render Renders from Dolby Atmos to 5.1 (without downmixing via 7.1) by using the rendering engine in
the Dolby Atmos Renderer to accurately recreate the sound field at the central listening position using phantom
imaging between the surround speakers and front speakers.
-
5.1 to 2.0 Downmix
-
Lo/Ro - default
-
Lt/Rt (ProLogic II)
-
Lt/Rt (ProLogic II) w/Phase90
-
Manual Trimming Tick to access manual control of trimming, which is available independently for 5.1 and 2.0, 5.1.2, and 7.1.
Click and drag the level indicators to manually Trim the Surround and Height levels and the Overhead and Listener plane pos-
itioning as desired.
Apple Spatial Audio
macOS users have the opportunity to use Apple’s Spatial Audio to monitor through their Apple headphones and earbuds. To access
Apple Spatial Audio, open the Dolby Atmos Renderer and change the monitoring format to “Apple Spatial Audio”. Additional features that
can be configured in the drop-down menu for the headphone options within the Renderer. From there, you’ll find these options:
-
Standard (the minimum requirement for Apple Spatial Audio is macOS 12)
-
Head Tracking (available on Apple silicon with macOS 12.3 or higher) allows the sound to move with the movement of your
head. This works only with compatible Apple headphones.
-
Personalized (available on Apple silicon with macOS 13 or higher) allows you to shape the sound with a personalized HRTF
(head related transfer function). This works only when the spatial audio experience is personalized (set up using a compatible
iPhone) and compatible Apple headphones are connected.
-
Personalized + Head Tracking (available on Apple silicon with macOS 13 or higher) is a combination of the two upper options.
Note: For Apple Spatial Audio to work as intended, your macOS must meet the following system requirements: Monterey 12 (for Stand-
ard + Head Tracking options) and Ventura 13 or Sonoma 14 (for Standard + Head Tracking + Personalized options).

## The Dolby Atmos Renderer

The Dolby Atmos Renderer Remote Panel
In order to access critical monitoring controls directly from the Console, the following controls are displayed in the
Console Output section for quick access. Click any to edit these parameters without opening the full Dolby Atmos
Renderer:
-
Bed Format (up to 7.1.6)
-
Speaker Format (up to 9.1.6)
-
Headphone Output Format Stereo, Binaural, Binaural (Apple Spatial Audio), or Binaural (Apple Spatial
Audio with Head Tracking)
-
Volume knob (attenuation across all sources, including bed and objects)
-
Bed and Loudness meters
Exporting and Importing Dolby Atmos Master Files
Exporting a Dolby Atmos Master File
Choose Song > Export Spatial Audio to export a Dolby Atmos ADM BWF file. Various other mixdown formats are provided here, includ-
ing Stereo, Binaural, Apple Spatial Audio (macOS only), 5.1, 5.1.2, 5.1.4, 7.1, and 7.1.4. You can export as many formats as you like sim-
ultaneously by ticking the relevant boxes.
Exporting and Importing Dolby Atmos Master Files

Note that while the exported Dolby Atmos Master File will have a .WAV extension, it still contains all relevant metadata. As such, it cannot
be treated like a more typical .WAV file (it cannot be dragged and dropped onto an Audio Track, for example).
Importing a Dolby Atmos Master File
To Import a Dolby Atmos Master File, simply drag and drop it into Studio One or choose File > Open from the drop-down menu and
choose your desired file. Note that dragging and dropping a Dolby Atmos Master File into an open Song will open it as a separate doc-
ument rather than creating an Audio Track.
This new document will contain the original Bed sources rendered to one track in its respective format. All objects are rendered to be
mono or stereo tracks with their panning information retained.
Exporting and Importing Dolby Atmos Master Files
