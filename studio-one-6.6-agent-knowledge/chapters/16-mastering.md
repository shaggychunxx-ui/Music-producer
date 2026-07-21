# Mastering (Project Page)

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 389–409
> **Slug:** `16-mastering`

**Agent topics:** `Project page`, `mastering`, `track sequencing`, `master device rack`, `publishing`, `song integration`

---

Mastering
Mastering is the process of preparing and transferring the final mix to a master copy from which all distribution copies are made. In the
mastering process, the source material is usually processed using equalization, compression, and so on. Editing, level adjustments,
fades, noise reduction, and other signal restoration and enhancement may also be done during mastering. Individual Songs are put into
their final order at this stage, a process commonly called “assembly” or “track sequencing.” The mastered material is then ready for
CD/DVD replication, vinyl pressing, web distribution, etc.
Studio One Professional features the Project page, a complete integrated mastering solution. This creates a tight, easy-to-manage cre-
ative workflow that spans all the way from recording to mastering.
The Studio One Professional Project page redefines this process into one that is smart, simple, and efficient. In the Project page, your
Songs can be mastered and arranged on a single timeline and then published to many professional formats. The following chapter
describes the mastering process, Project workflow, and how Songs and Projects are integrated to provide a total solution not available in
any other DAW.
Many of the capabilities of the Song page are available in the Project page, such as Control Link. As such, you should become familiar
with the Song page. The following section describes the Project page workflow in detail.

## Creating a New Project

To create a new mastering Project:
From the Start Page, open the New Document Window by clicking the New… icon or press [Ctrl]/[Cmd]+N on the keyboard.
Click on Master and Release (New Studio One Project).
If you’ve run “Save as Template” operations on previous Projects, you can find your saved Project templates under the “User” tab in the
New menu. Mastering templates are ideal for storing specific mastering chains or pre-defined generic ID tags.
 Mastering

When creating a new Project, Studio One will remember the last folder you used for a new Project and assume you would like to save
your work in the same location. If you would like to restore to the default location, right-click the file path and choose “Reset Folder” from
the drop-down menu.
Project Setup
In the New Project dialog, you can specify a Project Title and save a location, as well as the Project sample rate. Click on OK to create
the New Project.
Audio Import
If you have any audio files to import to your project, drag and drop them to the Drop Zone in the New Document window.
DDP Import
If you'd like to base your new Project on an existing DDP image, do the following:
1.
Enable the "Import Tracks from DDP Image" option in the New Project window.
2.
Click OK to create the new Project, and navigate to your DDP image in the file browser that appears.
3.
Select the folder that contains your DDP image, then press [Open], and the image is imported, with all metadata and media
intact.
This ability to import, edit, and export DDP images, often reserved for high-end standalone CD mastering systems, helps to make Studio
One a powerhouse mastering tool. For information on exporting DDP images, see DDP Export.
Album Title and Artist Name
You can enter a title for the album in the Album field, and an artist name (if applicable) in the Artist field. A drop-down arrow below these
fields gives you access to a variety of additional metadata fields (such as EAN, songwriter, and genre) that you can fill out as needed.
Meta-information is used when publishing your Project to any medium. You should fill in this information so your production is accurately
labeled when published and distributed to your adoring fans. When selecting artwork, the image size is limited to 512 x 512 pixels, and
can be automatically scaled to fit.
You can use the right-click context menu to copy the metadata to all tracks.
Project Page Tools
To get the most out of the Project Page, it would be helpful to review the many tools available to you via the Project Page toolbar and
Track Lane tools.
Audio Import

Project Page Toolbar
The Project Page Toolbar provides quick access to some of the Project Page’s most important tools.
-
Update Click onto this button if you would like to update the tracks in your mastering project to their most recent mixes.
-
Burn Click here to burn your finished project to CD.
-
Image Click onto this button to create a Disk Image of your Project.
-
DDP This creates a Disc Description Protocol (DDP) image of your Project.
-
Digital Release Select this release option to publish your Project to a single folder containing all Tracks in your Project, properly
tagged with the appropriate meta-information.
For more information about these options, check out the Publishing Your Project page.
Beside the release options, you'll find the Macro button, Time Display, and Info View button:
-
Macro This button opens the Macro Toolbar. From the Macro Toolbar, you have easy access to often-used functions and cus-
tom command combinations.
-
Time Display The Time Display specifies the exact run time of your project.
-
Info View Click the question mark icon to open the Info View bar. It shows which options are available depending on where you
hover the cursor.
Track Lane Tools
The Project Page features a subset of the familiar tools from the Song Page with similar functionality; streamlined to mastering-specific
needs. They can be found in a vertical toolbar on the bottom left of the Project Page.
From top-to-bottom, they are:
Project Page Tools

-
Automation Button: Press this to toggle visibility of the Automation Lane in the Project Page. (Note that
this does not enable/disable Automation itself.) Automation in the Project Page is comparable to Auto-
mation in the Song Page, detailed here.
-
Inspector: Click this to toggle visibility of the Inspector, allowing for changes to your tracks including
Normalization, Gain, Event FX, and more. The Inspector in the Project Page is comparable to the Inspector
in the Song Page, detailed in Track and Event Inspectors.
-
Autoscroll Button: As in the Song Page, press this toggle button if you would like the Track Lane view to
follow the current playback-cursor position or press [F] on the keyboard.
-
Arrow Tool: As in the Song Page, this multipurpose tool can be used to select, group-select, move, and
size Events—and adjust Event fades and envelopes. (Note that hovering the Arrow Tool over the top half of
an Event does not invoke the Range Tool in the Project Page.)
-
Paint Tool: Similar to its equivalent on the Song Page, the Paint Tool can be used to create and modify
complex Clip Gain Envelopes and Automation curves using seven sub-tools, including: Freehand, Line,
Parabola, and several wave-shaped subtools.
The Paint Tool being used to draw a Clip Gain Envelope in Freehand mode.
Adding Tracks
The first step in the mastering process is to place the desired source material into a Project.
The Browser
Just as on the Song page, the Project page has an integrated Browser, allowing you to browse for audio effects and files to add to your
mastering Project, including files in the current Browser Pool. Press [F5] on the keyboard, or click on Browse in the lower right hand
corner of the Project page interface, to open the Browser.
Add a Song
Any Song created in Studio One Professional can be added directly to a Project by importing the Song file into the Project. There is no
need to create a mixdown of the Song first, as this process is automated.
By default, your Song files are contained in the Content/Songs folder of the File Browser, with each Song file contained in its own Song
folder. To add a Song to your Project, browse to the desired Song in the File Browser and then click-and-drag the Song file to the Track
column or Track Lane.
Adding the Song to your Project places it in the Track column. If no master file exists for the Song, you are asked if you would like to cre-
ate a mix of the current state of the Song, which can then be rendered and added to the Track Lane.
When Studio One renders a mix of the Song you added, the length of the mix is determined by the Song Start and End markers, as seen
in the Marker Track of the Arrange view. Be sure these markers are set to the desired locations in the Song.
Adding Tracks

Track Time
As you edit Songs within your Project, it is useful to be able to keep track of where you are in time within each Song, as well as the
entirety of your Project. When you place the cursor along the timeline, the Track Time display in the transport shows you the position of
the cursor within the current Song, and the main time display shows the cursor position within the whole Project.
Add an Audio File
Of course, any Wave, Ogg Vorbis, AIFF, REX, or MP3 audio file can also be added to the Project by dragging it into the Project from the
Browser, just as you would with a Song. Imported MP3 files are converted to Wave format using the sample rate of the current Project.
Track Column
All Songs and audio files in your Project are listed vertically in the Track column, with the name of the Song or audio file clearly displayed.
Meta-Information
At the top of the Track column, you can see Album and Artist meta-information fields. To edit these fields, click in the space next to the
field, type your text, and then press Enter. If you want to enter further metadata for the album as a whole, click the small triangle button
below the Artist field, and enter your information as needed.
Adding Tracks

Beneath the color-coding bar to the left of each Track in the Track Column, there is a down-arrow button. Click on this button to reveal all
other meta-information fields for that Track. These fields may be edited on a Track-by-Track basis, or multiple Tracks may be selected
and their fields edited simultaneously.
To copy meta-information from a single Track to all Tracks in your project, [Right]/[Ctrl]-click the Track and choose "Copy Meta-inform-
ation to All Tracks" from the pop-up menu.
Meta-information is used when publishing your Project to any medium. You should fill in this information so your production is accurately
labeled when published and distributed to your fans. When selecting artwork, the image size is limited to 1400x1400 pixels, and can be
automatically scaled to fit.
Meta-information that has been filled in for any Song is automatically imported to any mastering Project that includes the Song, Any
changes made to the meta-information of a Song after import into a Project are not automatically applied to Song meta-information inside
a Project, and must be updated manually.
Auto-Incrementing ISRC Codes
In most cases, ISRC codes are assigned sequentially to each track in an album, increasing by one with each subsequent track. Because
of this, if you enter an ISRC code in the meta-information of the first Track in your Project, a dialog pops up, asking if you'd like to auto-
matically assign incrementing ISRC codes to the rest of your Tracks. Press [Yes] if so, or [No] if you'd rather enter them manually. If track
order or selection changes later on, you can always re-assign the ISRC code for the first Track in your Project to be prompted again to
auto-assign the rest.
Pause
The timing between Tracks is an important creative part of the mastering process. In Studio One, this is managed by your Tracks’ Pause
settings.
To change a Track’s Pause setting, click in the Pause field for a Track in the Track Column and type in a value or click-and-drag the audio
Events in the Timeline. You can also group-select by Shift-clicking multiple Tracks to quickly apply a consistent Pause setting to several
Tracks. If the pause field is not visible on the Track Controls, extend the Track height from "Small" to "Normal" with the buttons on the bot-
tom right.
Adding Tracks

By default, the first Track added to a Project will have a two-second Pause at the beginning of the Project. The Pause settings can be set
to any amount of time between 2 to 10 seconds. In order to stay in compliance with the Red Book CD Format, pauses can't be set to any-
thing shorter than 2 seconds. The Red Book CD Standard specifies that a pause must be a multiple of 1/75 seconds ("CD Frame"), which
is why some manually set values might be rounded insignificantly.
Subsequent Tracks added to the Project have no Pause inserted between them (more accurately, a Pause of zero seconds). This allows
for continuous back-to-back Tracks in a finished album or gapless crossfades from one Song to another.
This pause is ignored when exporting tracks individually using Digital Release.
CD Time Display
This display shows the CD Length of your Project based on the total length of all included audio materials.
Track Sequencing
To sequence the Tracks in your Projects, simply click on the file-type icon for any Track and drag the Track above or below the other
Tracks in the Track column.
Notice that the Tracks are automatically relocated in the Timeline of the Track Lane, with all other Track sequencing still intact, including
Track pauses.
Track Lane and Timeline
The Track Lane is where your Tracks are represented as Audio Events. You may notice that the Tracks are staggered in the Track Lane,
alternating between an upper and lower position across the Timeline. This allows two adjacent Tracks to overlap. By default, the Tracks
are separated by an amount of time dependent on the Pause setting for each Track.
To move any Track manually across the Timeline, click-and-drag the Track left or right. Notice that the sequencing of all other Tracks in
the Project is maintained when any Track is moved across the Timeline.
Editing Tracks
Sizing Tracks
Tracks in the Track Lane can be sized with the Arrow tool, as described in the Size an Event section of the Editing chapter. The relative
sequencing of all other Tracks in the Project is maintained when any Track is sized. Note that a Track cannot be sized to less than four
seconds in length, per the Red Book CD standard.
 Track Sequencing

Volume Envelope Editing
Each Track in the Track Lane features a volume envelope, which can be edited like the volume envelopes of Audio Events, as described
in the Adjust Audio Event Volume Envelopes section of the Editing chapter. A volume envelope lets you create fade-ins and fade-
outs.
Crossfading Overlapping Tracks
When a Track is manually moved across the Timeline so that it overlaps in time with another Track, it is possible to crossfade the two
Tracks so that one fades out as the other fades in. To crossfade overlapping Tracks, select the two Tracks and press [X] on the key-
board. A linear crossfade is drawn that can be edited by clicking-and-dragging on each Track’s fade handle.
Any Track that begins after another Track in time is normally the beginning of a new track on a CD or other medium. Its starting position
serves as the beginning of the track, regardless of the timing of crossfades. If you want to change the point at which the new CD track
begins, simply drag the song marker to a new location within the overlapping range.
Splitting Tracks
To split any Track, set the playback cursor where you want the split and press [Alt]+[X] on the keyboard. The resulting two Tracks can
now be edited like any other, including editing meta-information in the Track column. Splitting a Track for a Song does not adversely
affect the ability to automatically update that Song's mastering file, so it is possible, for instance, to split a long recording into many
Tracks in a Project and still edit the related Song normally.
Note it is not possible to split a Track where the resulting two Tracks would not be at least four seconds in length, per the Red Book CD
standard.
Enabling and Disabling Tracks
Any Track can be disabled at any time. Disabling a Track removes the Track from the Timeline but keeps the Track in the Track column,
with the label “This Track is disabled.” This is helpful if you need to remove a Track from the Project timeline but are unsure of whether
the Track should be removed completely.
To disable any Track, select it in the Track column and choose Disable Track from the Project menu. To enable a disabled Track, select it
and choose Enable Track from the Project menu. You can also enable or disable a track by [Right]/[Ctrl]-clicking the track in the list, and
choosing Enable Track or Disable track from the contextual menu.
Track Markers
All Tracks in a Project automatically have a Track marker attached to the beginning of the Event in the Timeline. It is possible to manually
insert other Track Markers by positioning the playback cursor at the chosen spot in the timeline, then [Right]/[Ctrl]-clicking in the Track
Marker lane and choosing Split Track at Cursor from the drop-down menu.
Editing Tracks

Manually inserted Track Markers are green in color, while automatically placed markers are blue in color. Track Markers can be moved
across the Timeline by clicking-and-dragging left or right. Track Markers can be placed anywhere on the timeline, so long as they're in
numerical order, and are not tied to the limits of any single Event. This lets you create a single Track that encompasses multiple Events,
create hidden tracks, and a variety of other mastering magic tricks.
Note that Track Markers are only used when burning a CD, or exporting an image file or DDP file. When exporting a digital release, manu-
ally placed Track Markers are ignored, and separate files are only rendered for actual Tracks, as listed in the Track column.
Transform Track to Rendered Audio
In the Mastering process it is sometimes necessary to render a Track so that the Insert effects and Automation moves become a part of
the audio waveform on the Track. While this is ideal for removing Insert effects in order to save CPU power, you can also use this feature
to render the processing of any hardware devices you are running via Pipeline; such renders will occur in real-time. You can even use the
same hardware device across multiple Tracks.
Transform is reversible and nondestructive. To Transform a Track, right-click on the desired Track’s Header and choose “Transform to
Rendered Audio” from the bottom of the list.
Check Preserve Realtime State if you would like to be able to transform back to the original Track. It is then possible to switch between
Automatic Tail Detection, with a Max Length property, and a fixed tail of a given length by toggling the Auto Tail option. Auto Tail is useful
if there is a reverb or other effect that you want to render beyond the Event length on the Track.
Click OK, and the Audio Track is bounced with its Insert effects and Automation applied; then the original Audio Track is replaced with the
newly bounced audio. If Auto Tail was engaged, or a Tail amount was specified, fade-outs are applied automatically across the specified
Tail duration for each Event. The Insert effects are removed, as they have been rendered into the audio on the Track.
If you check Preserve Original Track State, it is possible to transform back to the original Track, with effects inserted on the cor-
responding Channel, by [Right]/[Option]-clicking on the Track Header and selecting Transform to Realtime Audio from the contextual
menu.
The effects of Volume settings (including automation) and Clip Gain Envelopes are applied to the Track as it is bounced, so the value of
those settings and their automation data is set to its defaults in the resulting bounced Track.
Note that it is possible to group-select and Transform multiple Tracks at once, in which case they are all rendered simultaneously—
unless you’re running external hardware via Pipeline, in which case renders will occur sequentially in real-time.
Related: The Song Page’s Track Transform feature is covered in greater detail here.
Click-and-Drag Features
-
Move Events Click and drag on the beginning or end of a Track Marker while holding [Alt]/[Option], to move all Events at or after
that Track Marker across the timeline as one. This allows for easier mass-editing of track position and spacing.
Editing Tracks

-
Move only Start/End Marker Click and drag on the beginning or end of a Track Marker while holding [Ctrl]/[Cmd], to set a
pause period between the two Tracks at that split point.
-
Note: Any audio that exists in the pause zone you create between two Tracks will still continue to play during the pause.
If you want silence during a pause, you'll want to accomplish that by editing your Track to suit.
-
Move Track Click and drag in the center portion of a track marker to move Track marker and its related Track to a new location.
This is analogous to dragging tracks up and down the Track List.
-
Duplicate Track Click and drag in the middle of a track marker while holding [Ctrl]/[Cmd] to duplicate that Track Marker and its
primary Track to a new location on the timeline
-
Add (Index) Marker Hold [Alt]/[Option] while hovering over the middle portion of a Track Marker to enable the Add Marker tool,
used for placing additional Index markers within the current Track Marker.
-
Snap on Event Resize Hold [Alt]/[Option] while dragging either end of an Event to maintain an Event’s alignment during a trim
operation; useful for trimming silence without breaking alignment between your Events and Tracks.
-
When the first event of a track is resized left with Alt/Option pressed, the track is resized by the same amount, so that
the event keeps the same offset from the track start as before.
-
When the last event of a track is resized right with Alt/Option pressed, the track is resized by the same amount, so that
the distance to the track end marker stays the same.
-
Dragging files from the Browser Several options are available when dragging files in from the Browser, including adding new
tracks, replacing Events, and more:
-
Drag without any modifier key to add new track with the dragged File
-
Drag a file while holding [Cmd]/[Ctrl] to add the file to an existing track
-
Drag a file onto an existing Event while holding [Alt]/[Option] to replace the Event
-
Drag a file while holding [Alt]/[Option]+[Shift] to replace an Event and constrain it’s length to that of the replaced event.
Fade curves and trims are preserved.
If you click and drag on the beginning or end of a Track Marker while holding [Alt]/[Option], all Events at or after that Track Marker can be
dragged across the timeline as one, for easier editing of track position and spacing. If you click and drag on the beginning or end of a
Track Marker while holding [Ctrl]/[Cmd], you can drag to set a pause between the two tracks at that split point. Note: Any audio that exists
in the pause zone you create between two Tracks will still continue to play during the pause. If you want silence during a pause, you'll
want to accomplish that by editing your Track to suit.
Clip Gain Envelopes
Clip Gain Envelopes are the ideal tool for correcting sections of your Events that are either too loud or too soft, without adding a com-
pressor or limiter plug-in, as they allow you to make nuanced (or drastic) volume changes over time.
Editing Tracks

Clip Gain Envelopes in the Project Page behave identically to their counterparts in the Song page, and can be edited using the same
tools and instructions found on this page.
Note that the Project Page does not support Clip Versions.

## The Listen Bus

A dedicated Listen Bus on the Project Page provides a separate audio feed to the control room monitors or headphones, independently
from the Main Out Channel. The Listen Bus is ideally suited to room calibration plug-ins running as a Listen Bus insert. This will allow a
session engineer to hear the benefits of room correction software while keeping the Main Output unaffected—processing that occurs in
the Listen Bus is not rendered to any Digital Release or burned CD.
To access and use the Listen Bus, Select Listen Bus to the right of the Master Device Rack. Underneath the Post Rack, you’ll need to
choose an Output, as the Listen Bus has no Output selected by default. Options here will vary depending on the capabilities of your con-
nected interface. The Listen Bus receives the output signal of the Master Output; any adjustments to the Master Fader will affect the
audio sent to the Listen Bus.
The Listen Bus enjoys a nearly identical feature set of the Master Bus, including its own Volume Fader, Macro controls, Stereo/Mono
toggle, and Insert- and Post-effect Racks. Effects running on the Listen Bus cannot be automated.
The Listen Bus is also featured in the Song Page and is detailed here.
Using Insert Effects
Insert effects can be used in the Project page in much the same way as on the Song page. Each Track has a dedicated Device Rack, and
there is also a Master Device Rack. Inserts are handled in the Project page as described in the Inserts section of the Mixing chapter,
including the ability to use FX Chains, ARA effects, and the built-in effects Micro Views.
Track Device Rack
Inserts in the Track Device Rack can be used to process each Track individually. The most common use is to achieve a balance with
other Tracks in the mastering Project, so that any Master Device Rack processing affects each Track in a similar way. For instance, each
Track probably requires individual equalization. A Track fader is available in the Track Device Rack to fine-tune the output level of each
Track, and an Insert Device Rack Activate All button enables you to quickly A/B any processing.
Loudness Detection
At the top of the Track Device Rack, a Loudness Information dropdown menu is available. When you first click this menu on a Track, a
Loudness Detection process runs on that Track. Once the detection process finishes, you're provided with readings for EBU-R128 Integ-
rated Loudness (INT) and Loudness Range (LRA), as well as True-peak readings, RMS, and DC levels for the left and right channels. All

## The Listen Bus

measurements are shown both pre-FX and post-FX. This information can help when making level balance decisions from Track to Track
across the Project.
If you make changes to a Song and later wish to re-calculate its loudness, [Right]/[Ctrl]-click the song in the Track column or lane, and
choose Detect Loudness from the pop-up menu. To detect loudness for multiple Tracks at once, select the desired Tracks and [Right]/
[Ctrl]-click one of the selected Tracks, then choose Detect Loudness from the pop-up menu.
Track Editor
Each Track in your Project has a Track Editor, in which you can create a variety of advanced effect configurations, with assignable Macro
Controls. You can open the Track Editor for a Track by clicking the knob-shaped Editor button in its Track Device Rack. For more inform-
ation, see Channel Editor, which explains the equivalent function in the Console in Song view.
Copy a Track’s Effects to Another Track
To quickly copy any effect from one Track’s Device Rack to another, simply click-and-drag the effect from the Device Rack onto another
Track in the Track column. To copy all effects from one Track to another, click and drag the Insert Device Rack header from the source
Track, and drop it onto your chosen Track in the Track Column or Track Lane. To copy all Effect Automation from one Track to another,
hold [ALT/OPT] during the above click-and-drag operation.
You can also save the entire Device Rack as a single preset, called an FX Chain, by clicking on the arrow next to “Inserts” at the top of
the Device Rack and selecting Store Preset. Then locate the FX Chain in the Browser under Audio Effects and drag it onto any Track in
your Project.
Using Hardware Inserts in a Project
As fully discussed in Pipeline, you can use hardware inserts by means of the Pipeline plug-in in Studio One Professional. When using
Pipeline, you may need to access the audio I/O setup for your Project (found in the Project/Project Setup/Audio I/O Setup menu) in order
to configure the inputs and outputs your hardware insert uses.
Note that when Pipeline is inserted anywhere in a Project, it is no longer possible to render audio exports offline for CD burning, disc
image creation, or digital release creation. Real-time processing is used, as this is required to incorporate your hardware insert into the
audio export.
Bouncing Tracks
If you feel the need to free up computer resources or external processors (used through Pipeline), you can bounce a Track in place,
retaining the effects of any plug-ins or external gear in use. To do so, [Right]/[Ctrl]-click the Track in the Track Column, and choose
"Bounce Track" from the pop-up menu. If an external hardware effect is in use on the Track (via Pipeline), the bounce must occur in real
time.
Master Device Rack
Inserts in the Master Device Rack affect every Track in the mastering Project. Peak limiting, multiband dynamics processing, and other
similar processes are commonly used in the Master Device Rack to finely adjust the overall sound of the Project. Generally, a certain
amount of balance and equalization between all Tracks in the mastering Project should be achieved before applying Master Device Rack
processing. Effects and FX Chains can be dragged to and from the Master Device Rack, just as with other types of Device Racks.
Pre- and post-fader Insert Racks are provided, each with Activate All buttons, for ultimate flexibility in adding and auditioning any pro-
cessing. If you plan to use a third-party plug-in to provide dithering, place the Insert post-fader and be sure to disable the Use Dithering
for Playback and File Export option in the Studio One/Options/Advanced/Audio pane (macOS: Preferences/Advanced/Audio). Note that
by default, Studio One only dithers when necessary (e.g., for reducing bit depth within a device or during file export) and always uses tri-
angular-type dither with no noise-shaping.
A Master Channel output fader is available to dial in the master output level of your Project, and you can select the output for your audio
device (audio interface). Note that this directly affects the output level of your Project for all export mediums. All of the output pairs
provided on your audio interface can be accessed by clicking on the currently displayed audio output.
Automation in the Project Page
Automation refers to automatic changes to control parameters over time. You can Automate nearly any plug-in parameter in real time,
with the mouse or via an external hardware controller, or by using the Paint Tool.
Automation in the Project Page functions similarly—but not identically—to Automation in the Song Page, which is covered here. We
advise you familiarize yourself with the fundamentals of Automation in the Song Page, including Automation Types, Automation Modes
and creating, writing, and editing Automation Envelopes before working with Automation in the Project Page.
Master Device Rack

Automation Lanes
The Project Page provides two Automation Lanes: the top Lane is for Track Automation, and the bottom Lane for the Master Automation.
Click the Automation button on the top of the bottom-left toolbar, or Press [A] to toggle between Track View and Automation Lane View.
The Track Automation Lane
In the Project Page, Automation of a Track’s control parameters and effects controls are managed on a per-Track basis. While Track
Automation curves will run the length of your entire Project, only the Automation Curves tied to the currently-selected Track are visible at
one time. Note that this means any reverb or delay effect applied that includes a tail that extends beyond the end of a Track Marker could
still be audible outside of a Track’s range.
From the Automation Lane View, click on a Track Marker at the top of the Lane or in the Track List to bring a Track and its respective
Event into focus and see its Automation curves. Doing so hides the Automation curves of other Tracks, and collapses the alternating
Event display to a single lane for Events.
Use the Track Automation Lane to automate parameters as required on a per-song basis—you can create and edit Automation for any of
your Track’s Insert effects and Volume.
Unlike the Song page, you cannot create your own Automation Tracks on the Project Page.
The Master Automation Lane
Use this Lane to automate parameter changes required across the entire Project, like volume or compression adjustments.
Metering
High-quality metering is critical during the mastering process. The Project page offers three types of meters, each visible at all times, to
help you make creative and technical decisions while processing your material.
Metering

Spectrum Meter
The Spectrum Meter is a flexible audio-spectrum meter that offers octave, 1/3-octave, 12th-octave, FFT, Waterfall (WF), Sonogram
(Sono), and Segments display modes. The Spectrum Meter displays standard peak levels and can be adjusted to display Peak Hold
levels for Short, Medium, and Long time intervals, as well as average (RMS) levels within Fast, Medium, and Slow time intervals. As you
move the cursor around the frequency display, the note value of the current frequency is displayed.
The visible range of the meter can be changed in any mode, to help focus in on the range you're interested in. Do this by setting the Level
and Frequency Range controls, or simply by clicking and dragging vertically within the meter.
To disable the Spectrum Meter, click the "power" button under the upper left corner. Click again to re-enable the meter. To temporarily
"freeze" the current state of the Spectrum Meter, click the snowflake button below the meter.
Spectrum Meter Display Modes
-
Octave: Octave Band displays frequency content divided into octaves, useful for determining broad balance across the fre-
quency spectrum.
-
3rd Octave: Third-Octave Band displays frequency content divided into 1/3 of an octave, useful for determining balance with
good precision across the frequency spectrum.
-
12th Octave: The bands in the 12th-octave meter correspond to the 12 musical tones in an octave, each in its appropriate place
on a piano-like keyboard. This allows for easy reading of the pitch or note value of a given signal.
-
FFT: A Fast Fourier Transform, or FFT, displays frequency content divided into many bands. It’s useful for accurate metering of
a specific range of the frequency spectrum.
-
When FFT is selected, you can select the FFT window size (FFT size = time vs. frequency resolution). You can choose
from 16,384; 8,192; 4,096; and 2,048. The default setting is 16,384.
-
As FFT measurements are divided into bands, exact frequencies across the entire spectrum are not measured.
-
When using the FFT display, a -3 dB/octave line is displayed in addition to the frequency and level crosshair. This line
represents compensation for the shrinking frequency-width of the FFT bands toward the higher end of the spectrum,
which leads to a lower energy content. A well-balanced mix should somewhat approximate the slope of this line.
-
FFT Curve: This performs the same analysis as the FFT mode, but displays the result as a single white line.
-
Waterfall & Sonogram: Two modes that graph changes in frequency content and dynamics over time.
-
Segments: Closely resembles the output of an FFT display. However, the X/Y grid is split up in uniform segments, rather than
varying in resolution depending on frequency. Switchable amplitude segment sizes of 0.5, 1, and 2 dB.
Metering

Level/Loudness Meter
The Level/Loudness Meter is located directly beneath the Spectrum Display and is capable of displaying high-resolution Peak/RMS
levels, three K-System scales (as described in K-System Metering), as well as the more recent EBU R128 standard. To choose a stand-
ard to view, click the selector below the Level Meter or [Right]/[Ctrl]-click within the meter and make your selection from the drop-down
menu.
Nowhere is it more important to accurately meter levels than at the mastering stage of production. It is critical to be sure that the levels
across all Tracks are as consistent as desired and that the signals are never clipped. When any amount of clipping occurs in your Project,
a red clip indicator illuminates at the bottom of the Level Meter display, which can only be cleared by clicking on the indicator.
When Peak/RMS mode is selected, you can [Right]/[Ctrl]-click on the meter display to show additional metering options, such as RMS
Length, VU Hold, and Hold Length.
When EBU R128 mode is selected, note that the top bar represents the “short term” level value while the bottom bar represents the
“momentary” value. The short term values measure loudness every 1 second on an audio block of 3 seconds, providing information
about the loudest audio passages. The momentary values give instantaneous feedback, measuring loudness every 100 ms.
To disable the Level Meter, click the "power" button under the lower left corner. Click again to re-enable the meter.
Loudness Display
Real-time numerical loudness information for the final output is displayed here, in LUFS (Loudness Units Full Scale, for absolute loud-
ness measurements), or LU (Loudness Units, for relative loudness measurements). In either mode, you can see the Integrated loudness
(INT), Loudness Range (LRA), and True-peak (inter-sample peak meter) reading. To reset the measurements, click [Reset].
The Level/Loudness meter will be quickly reset every time the Play button is pressed or if a new Track is selected during playback of
another. This ensures that the Loudness values of one track are not taken into account when measuring another.
Phase Meter
The Phase Meter, located to the right of the Level Meter, is helpful when checking stereo playback issues and mono compatibility. There
are two components to this meter: a Goniometer at the center of the plug-in window and a Correlation Meter at the very bottom.
The Goniometer displays left- versus right-channel amplitude on an X/Y oscilloscope. A vertical line in the Goniometer represents a
mono signal. The horizontal Correlation Meter compares the amount of in-phase and out-of-phase audio signal in the left and right chan-
nels. The parameters of the Correlation Meter range from +1 (mono signal) to -1 (reversed-phase mono signal), with 0 indicating the pres-
ence of totally independent signals (true stereo).
For more information about Studio One's metering tools, check out the Analysis and Tools page.
Metering

## Publishing Your Project

When your Project has been mastered, the next step is to publish it. The Project page offers many options, categorized into three main
operations, including burning an audio CD, making a disc image file, and making audio files.
Burn an Audio CD
You can burn your mastered Project to a standard Red Book audio CD directly from the Project page. Red Book is the most widely adop-
ted technical standard for audio CDs, and it includes specifications for minimum and maximum track durations, maximum number of
tracks, and how audio is encoded to the CD. Since the Project page adheres to this standard, you can be sure your audio CDs are com-
patible with almost any CD player.
To burn your Project to an audio CD, click on the [Burn] button at the top of the Project page. In the Burn Audio CD dialog, you can select
the device you wish to use to burn the CD, as well as the speed of the burning process. In general, using slower speeds in the burning
process reduces the chance for errors.
Burn Options
Several options in the Burn Audio CD dialog are intended to prevent common CD-burning errors: Test Write, Use Burnproof, and Use
Temporary Imagefile. These options usually increase the time it takes to burn a CD in the Project page but they help to prevent wasting
time and blank CDs on failed attempts.
The Test Write option runs tests before attempting to burn the CD in order to be sure the necessary computer resources are available.
Burnproof is a technology capable of preventing buffer under-run errors with some CD burners, in which the CD-writing process is inter-
rupted, and the CD writer is forced to stop burning the CD before it is finished.
The Use Temporary Imagefile option changes the burn process so that an image of the CD to be burned is created before attempting to
burn the CD. This helps to eliminate potential problems related to data not being made available fast enough while writing to the CD.
Make a Disc Image
Publishing your Project might require a disc-image file. For instance, sending your Project to a professional CD duplicator might require
digital transmission of the content of your CD, rather than sending a potentially imperfect physical copy. Also, you may wish to use a dif-
ferent application to burn your CDs, in which case you need an image file. There are many file formats for disc images, some better
suited to audio CD creation than others. Studio One uses a continuous audio Wave file and a cue file to achieve the most universal sup-
port.
To create an image of your Project, click on the [Image] button at the top of the Project page. Options are available for file format, res-
olution, and sample rate, as well as the ability to toggle Realtime Processing and simultaneously upload the Project to a linked
SoundCloud account. In making an image, Studio One creates a cue file and a single, continuous audio file of your entire Project and
places them in your Project folder. The cue file contains all of the necessary information to create the separate audio tracks for your CD
by referencing the continuous Wave file. Many third-party CD-burning applications can create a CD using the Wave and cue files
together.
DDP Export
DDP images are quickly becoming the standard method of getting a disc image from mastering to disc manufacturing. The DDP image
contains all the contents of your master disc, plus formatting information that ensures your replicas exactly match your master. To create
a DDP image of your Project, click on the [DDP] button at the top of the Project page.
All of the DDP image data is exported to a single folder with the name of the Project appended with "DDP." This folder can be delivered to
a duplicator.
Digital Release
It is possible to publish your Project to a single folder containing all Tracks in your Project, properly tagged with the appropriate meta-
information. A common use for this would be to quickly create an MP3 album in one folder and then upload it to a Web site or online
retailer for distribution. This process is similar to creating a mix on the Song page, as described in the Create a Mixdown section.
Click on the [Digital Release] button at the top of the Project page to open the Digital Release dialog. In this dialog, you can choose from
several formats:
-
Wave
-
AIFF
-
FLAC (16-, 24-, and 32-bit integer)
-
CAF

## Publishing Your Project

-
M4A
-
Ogg Vorbis
-
Opus
-
MP3
Select the formats for your mix file and choose the desired attributes for each. Attribute options will vary by format, but common options
include sample rate and resolution. The MP3 and OGG Vorbis formats also offer an option to export at a Constant or Variable bit rate.
The encoder will vary the bit rate during export, allocating more bits to complex passages and fewer bits to simple ones. This flexibility
allows generating higher quality output files compared to the Constant bit rate mode at the same overall bit rate.
If you want to put your mix on a standard audio CD, create a 16-bit, 44.1 kHz Wave file.
You also have the option to simultaneously upload your Project to a linked SoundCloud account.
The folder to which all new files are written is named according to the Artist and Disc fields in the Project meta-information, at the top of
the Track Column. If the Artist field is disabled, the new folder takes its title from the Disc name field. If the Artist field is enabled, the new
folder title shows the artist name followed by the disc title. If neither the Artist or Disc fields have been filled in, the folder gets its title from
the name of the Project.
The name of each Track in the Track column is used for the name of the new files created. In the Options section of this window, you can
include Track numbers and the artist name in the name of each new file to be created in the album. All other meta-information supplied
for each Track is used to tag the new files appropriately.
You can also choose Realtime Processing, to mix the Project down in real time.
Publishing
Studio One provides options to directly publish your finished project either by uploading to SoundCloud, TuneCore, or Studio One+ for
sharing and collaboration. To publish your project after exporting the Project, select Upload to Studio One+, Upload to TuneCore or
Upload to SoundCloud in the Publishing section.
Target Loudness Options

## Publishing Your Project

The target loudness and peak level requirements of popular online streaming music services vary significantly. Studio One’s Target Loud-
ness Options can save you a great deal of time by optimizing your Tracks for the variety of requirements of these services—while also
ensuring that your mixes won’t be altered by the loudness algorithms employed by these services. Instead, you control how your music
will be reproduced. As it should be.
When using Adjust Loudness, your Tracks are analyzed during export, and loudness and true peak are matched to the selected settings.
Please note that if the dynamic range of the exported file is too big, it's possible to not hit the Target Loudness, since there may be a con-
flict between Loudness and Max True Peak. In these cases Max True Peak always wins.
Simply tick the “Adjust Loudness” checkbox and select the preset for the intended platform of release.
Entering your own Max Loudness and Max True Peak settings will cause the Preset to jump to “Custom”, which will save these settings
for later use. The streaming service Presets like Apple Music and Spotify cannot be edited or saved.
Adjust Loudness performs the following operations on Export:
-
Max Loudness: The loudness of the written file is adjusted accordingly if the analyzed loudness is outside the defined range.
-
Max True Peak: If the detected true peak value of the exported file is larger than the value specified, the gain of the final file is
reduced accordingly.
-
Album Mode: The loudness of the selected Tracks is measured as a whole in order to apply loudness optimization equally. Use
this option if you don’t want all the tracks of an album to have the same target loudness; you will maintain full control over the
loudness of your album tracks while still meeting the required loudness standard.
Studio One+ Integration
If you’re a Studio One+ member, you have access to additional services such as sharing your work with others and even collaborating on
a project with other Studio One+ users. These services are available directly from within Studio One as soon as you're connected to the
Internet and your Studio One+ license is activated.
Upload to Studio One+
When you’re running an active Studio One+ subscription license and your computer is connected to the Internet, uploads can be initiated
directly from within Studio One. First, make sure to check Upload to Studio One+ in the Publishing section of the Digital Release window
on the Project Page, or select Upload to Studio One+ in the Publishing menu of the Export Mixdown or Export Stems window.
For more information on Studio One+, click here.

## Publishing Your Project

As soon as the mixdown or rendering process is completed, the “Upload to Studio One+ ” window will appear. First make sure the mixed
and rendered files in the Files column are complete. Then select a destination Workspace from the Workspaces list. Click the [Upload]
button to initiate the upload to Studio One+ .
To add files to a Workspace, at least one Workspace needs to exist in your Studio One+ cloud storage account. You can manage your
Workspaces by clicking on Manage Workspaces which takes you directly to the Workspaces area of your Studio One+ account. Here
you can manage your storage space, share content with other users, and invite other Studio One+ users to join your workgroup.
SoundCloud Integration
PreSonus has partnered with the popular SoundCloud Web service to make it possible for you to upload your music to SoundCloud from
within Studio One. This integration is the first of its kind.
Connect with SoundCloud
To publish your music to SoundCloud, you first need a SoundCloud account. Visit http://www.soundcloud.com to create your free
account. Then, open the Studio One/SoundCloud Client dialog and click on Connect with SoundCloud. Your Web browser then opens to
a special page to allow Studio One to connect with your SoundCloud account. Log in to your SoundCloud account on this page, click on
Connect.
Studio One is now connected to your SoundCloud account.
Upload to SoundCloud
Once Studio One is connected to SoundCloud, you can upload
music from your Project to SoundCloud directly from Studio One.
To do this, create a digital release from any Project and choose
Upload to SoundCloud in the options, or open the Studio
One/SoundCloud Client dialog.
If creating a digital release, the Tracks from the digital release are
added to the SoundCloud Client window automatically, with the
appropriate meta-information already filled in. If accessing the cli-
ent directly, click on Add Tracks to add any audio file to the list.
SoundCloud supports the upload of any audio file from Studio
One, at any resolution, and at any file size. Any number of Tracks
can be uploaded at once, added from a digital release or manu-
ally.
After adding your Tracks, select any Track in the list to edit its
information in Track Info and More Info. If you want the Track to
be available publicly, meaning any SoundCloud user can see it,
select this option under Track Info. If you want the uploaded file
for Track to be downloadable or streamable, select the corresponding option under More Info.
When finished editing Track information, click on Upload to upload the Tracks to SoundCloud. The Tracks appear in your SoundCloud
account once the upload has completed.
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
-
When exporting a mixdown, select “Upload to TuneCore” from the Publishing options. The “Connect to TuneCore” window will
appear once you finish refining the export options and press “OK”.

## Publishing Your Project

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

## Publishing Your Project

Song and Project Integration
At the center of Studio One Professional’s design is Song and Project integration. This is where the usual gaps between mixing and mas-
tering have finally been eliminated. When Songs are placed in a Project, a link is established that allows the Song and Project to be intel-
ligently aware of each other so that changes to either are known to both. This integration, as described in the following sections, is sure to
change the way you think about mixing and mastering.
Open a Song from Within a Project
During mastering, changes are often needed in various Tracks in a Project, after which changes to the mix are made. Traditionally, this
process can be grossly inefficient, taking many hours, if not days or weeks.
In Studio One, however, you can quickly make changes to the mix of a Song in your Project. To open a Song in your Project, click on the
[Edit] button (labeled with a small icon of a wrench) in any Track in the Track column. Your Song opens on the Song page, where you can
make your changes. When finished, save and close the Song.
When you go back to the Project page, or open the Project in the future, you are prompted with a message informing you that the master
file is no longer current for the Song to which you just made changes, and you are given the opportunity to update the master file. The
Automatic Update of Mastering Files section below explains this option.
Automatic Update of Mastering Files
Of the most common questions that arise when mastering is also one of the most time-consuming: “Are these mixes the most current ver-
sions?” Often, changes are made to multitrack mixes in response to problems found during mastering. When these changes are made,
new mixes have to be created and reinserted into the mastering Project.
There can be many rounds of changes for each track, resulting in a potentially confusing situation in which it is hard to tell which mix is
which, and which is the final version that should be in the mastering Project. When the right mix file is finally found, the old mix is
removed, and the new mix is added back into the Project, usually requiring re-sequencing the tracks in the Project.
Studio One Professional solves this problem with automatic updating of mastering files for any Song in a Project. When you change any
Song included in a Project, and then open the Project, you are asked if you would like to update that Song’s mastering file. If you choose
to do so, the following happens:
-
The Song is automatically opened in its last saved state.
-
A mixdown of the Song is rendered.
-
The new mix file replaces the old one in the Project.
-
The Song is automatically closed.
-
A report is displayed in the Project indicating which files were updated and how long the entire process took.
Note that when Songs are automatically updated, and a new mix is rendered, the length of the mix is determined by the Song Start and
End markers, as seen in the Marker Track of the Arrange view. Be sure that these markers are set to the desired locations in the Song. If
an update of a Song fails, check the Song for missing files and plug-in effects and then try the update again.
Any number of mastering files can be updated in a single process. This way, every time you open a Project, you can be sure you have the
latest mix of each Song.
When a mastering file in a Project is not up to date, a red light appears to the left of the Track name in the Track column, as well as in the
lower left corner of the Track in the Track Lane. You can choose to manually update any of these files by [Right]/[Ctrl]-clicking on the
Track and selecting Update Mastering File. When the file is up to date, a blue light appears.
You can also update every mastering file in the Project at once by clicking on the [Update] button at the top of the Project page. Any files
that need to be updated because saved changes have occurred to the Songs are updated in the same process described earlier.
Add Currently Open Song to a Project
To add a Song you are currently working on to a new or open Project, select Add to Project from the Song menu. Select any open Project
from the list or select New Project. This adds the Song file to the desired Project and automatically renders a mixdown, placing it in the
Project timeline.
Update a Mastering File from the Song Page
To update a mastering file for the currently open Song from within the Song page, select Update Mastering File from the Song file menu.
This updates the mastering file for the Song, which can exist in any number of Projects. The next time any Project that contains the Song
is opened, the new mastering file appears automatically for that Song.
Song and Project Integration
