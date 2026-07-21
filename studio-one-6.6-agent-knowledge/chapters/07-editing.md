# Editing

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 92–191
> **Slug:** `07-editing`

**Agent topics:** `events`, `mouse tools`, `clip gain`, `grid`, `comping`, `timestretch`, `transient detection`, `track transform`, `inspector`, `presets`, `Sound Variations`, `patterns`, `Melodyne`, `macros`, `edit view`

---

Editing
After recording, the next step in production is usually editing the recorded Events to achieve a desired sound. The following chapter dis-
cusses aspects of editing in Studio One, including Arrange view and Edit view editing, mouse tools, Event envelopes, edit groups,
timestretching, comping, integrated Melodyne pitch correction, and transient detection and editing.

## Events

All audio and note data that exists within the timeline of your Song are visually represented by Events. Events that contain audio are
called Audio Events and can only be located on Audio Tracks. Audio Events are distinct in that they display audio waveforms. Audio
Parts are Events that contain multiple Audio Events.
Events that contain note data are called Instrument Parts and can only be located on Instrument Tracks. Instrument Parts are distinct in
that they display musical performance information.
Audio Events and Instrument Parts are referred to collectively as Events in this manual. Event editing can take place both in the Arrange
view and the Edit view. Audio Events and Instrument Parts can be edited in similar ways, but each has special considerations.
[Right]/[Ctrl]-clicking on any Event displays the Event contextual menu, which contains all related Editing actions, logically grouped. At
the top of the contextual menu, you can find the Event Name, which can be edited by double-clicking on it and entering a new name. You
can rename all Events on a Track by renaming the Track and holding [Shift] while pressing [Enter] after typing in the new name. You can
also change the Event color by clicking on the color bar next to its name and selecting a color or scrolling through the colors with the
mouse wheel.
Common editing actions are listed under the Event name, as well as a Recent Items list that contains the five most-recently used actions.
In this way, you have instant access to the editing actions you most likely want to use.
Note that the available actions listed in the Event contextual menu depend on whether you are working with an Audio Event or an Instru-
ment Part, and the actions may vary slightly depending on your version of Studio One.
Tool and Event Snapping
Snapping allows editing actions to occur only at specified divisions in time (such as bars and beats), making editing easier when working
with tempo-specific material. For instance, Snapping makes it possible to rearrange specific beats from a bar of a drum loop while keep-
ing the rest of the loop in time. Snap is engaged by default and can be disengaged by clicking on the Snap to Grid button. You can also
temporarily defeat Snapping by pressing the [Shift] key while moving the mouse.
If Snap is engaged, the current Snap setting affects the behavior of tools and Event editing by snapping the tool or Event to nearby time
values, as follows:
 Editing

-
Adaptive The default setting, where snapping occurs at the nearest logical subdivision of the current Timebase, based on the
current timeline zoom level.
-
Bar Snapping occurs at the nearest musical bar line.
-
Quantize Snapping occurs at the nearest musical subdivision of the current Quantize Setting.
-
Frames Snapping occurs at the nearest frame subdivision.
There are six optional behaviors that can be selected and applied to any of the four modes above:
-
Snap to Cursor and Loop This option enables snapping to the playback cursor and Loop locators.
-
Snap to Events This option enables snapping relative to Events in the Arrangement.
-
Snap to Zero Crossings This option ensures that the audio data in an Event will snap to a zero crossing point. This will help
avoid an unnatural click at the beginning of the audio data when the Event is moved or split.
-
Snap to Grid This option is engaged by default, allowing tool and Event snapping to the grid.
-
Snap Event End This option enables snapping on both the start and end of the moved Event. (When disabled, only the event
start snaps.)
-
Relative Grid This option maintains the time relationship relative to the grid for any Event, so that when the Event is moved, the
snap position maintains the original position relative to the grid, instead of snapping directly to the grid.
Spot
The Spot command, found in the right-click contextual menu of Events and Parts, allows you to precisely relocate Events and Parts via
numeric entry. While Studio One prides itself on drag-and-drop, there are times when this level of control and precision are advant-
ageous; particularly when syncing audio events to video.

## Events

The timebase for a Spot operation is selectable from Samples, Seconds, Bars, or Frames, regardless of the Timebase configuration of
your Song. Click on any numerical field in the Start, Sync Point, or End fields to enter values by hand, or click-and-drag on the numerical
fields to edit with the mouse.
Spot works on Instrument Parts, Pattern Parts, and Audio Events. When applying Spot to several Parts or Events at once, note that their
positional relationship to one another will be maintained. If adjusting the Start point, the start point of the earliest-beginning Event will be
used. If adjusting the End point, the end point of the latest-ending Event will be used.
Imported files that contain timestamp information can be restored to their original position by clicking the icon to the right of the “Original
Position” field.
You can also apply a Spot command on import when dragging to the Arrangement window and holding [Opt+Shift] on Mac or [Alt-Shift]
on Windows.
Stretching Parts
Any Instrument Part or Audio Event can be stretched to fit a desired space in the Arranger.
Instrument Parts
Hold ALT while clicking and dragging from the left or right edge of an Instrument Part to stretch the Part. Note that any Automation points
within the Part will also be stretched in kind. This can be disabled by de-selecting “Select Part Automation with Notes”
in the Note
Editor toolbar.
Audio Events
Hold ALT while clicking and dragging from the left or right edge of an Audio Event to stretch the event. Stretching of Audio Events is more
complex than Instrument Parts, and is covered in greater detail in Timestretching.
Sync Points
A Sync Point is a marker within an Audio, Video, or Instrument Event (including Patterns) used as a reference position for Studio One’s
Snap functionality. Ordinarily, Events will snap to position based on the start or endpoints of the Events themselves. Sync Points allow
you to set this Snap position wherever you would like in an Event rather than relying on its endpoints.
This is useful for some Audio Events that may benefit from being snapped to a peak or transient that is not located at an event endpoint.
Examples could include percussion loops with a transient in the middle of the loop; EDM riser samples that need to be snapped near their
endpoint but not precisely at it; etc.
Sync Points’ snap behavior is determined by the option chosen in the Snap drop-down menu in the Toolbar (Bar, Quantize, Relative
Grid, etc.).

## Events

Sync Points can also be used to snap two Events to each other using their Sync Points; "Snap To Events" must to be enabled in the Snap
options.
Sync Points are non-destructive and flexible, meaning a Sync Point’s position is maintained if an Event is Reversed or Bounced!
Adding and moving a Sync Point
To add a Sync Point to an Event:
-
Choose the desired Event.
-
Click the timeline to position the cursor (playback head) where you would like the Sync Point to be placed. Zoom in for precision
placement if necessary.
-
Right-click the desired Event and choose Events >> Set Sync Point to Cursor.
-
The Sync Point will be placed at the cursor position, visible as a white vertical line. A small yellow diamond appears on
mouseover.
A riser sample with its Sync Point set at its point of maximum energy with a reverb tail falling to the right of the Sync Point. Notice how the
Sync point snaps to bar 200 while the start and end points of the event do not snap to the grid.
To move a Sync Point, click and drag the small yellow diamond icon to the desired sync position within the Event. When zoomed out,
Sync Points will automatically snap to transients when moving. Zoom in to bypass this behavior. This behavior can be bypassed by dis-
abling Snap [N], or by holding shift while moving the Sync Point.
Use the “Toggle Sync Point” command to disable/enable Sync Points on the currently-selected Event.
Sync Points also influence the behavior of the “Cursor Follows Edit Position” option. The cursor will snap to the Sync Point of an Event
rather than its start point.
Event Icons
There are various Event Icons that you will likely encounter while using Studio One, and in some cases, the icons can serve multiple func-
tions. These icons appear at the bottom left corner of Events.
The following section describes what each icon represents.
Gear Wheel Icon
When the Gear Wheel Icon appears, this can mean one of three things:
-
Time stretching has been enabled.
-
The clip has a different sample rate than the rate your song is set to.
-
You have changed the transpose or tune value of the clip.
If you would like to ensure the clip is set at the same sample rate as your song, follow these steps:

## Events

1.
To check the song’s sample rate, navigate to Song/Song Setup or press [Ctrl]/[Cmd]+[.] on the keyboard to open the Song Setup
window.
2.
Within the Song Setup window, confirm the song’s sample rate.
3.
To check the Event’s sample rate, [Right]/[Ctrl]-click onto your Event, and from the drop-down menu, click onto the “Select in
Pool” option.
4.
The clip details will be displayed at the bottom of the Pool page.
5.
If the sample rates are different, you can edit the sample rate of the clip from here to match the sample rate of the song. [Right]/
[Ctrl]-click onto the clip and choose the “Convert Files” option from the drop-down menu.
6.
From this window, you can easily edit the chosen clip’s file format, resolution, and sample rate.
Mute Icon
The Mute Icon simply indicates when an Event has been muted. To toggle the mute function, you can either use the mute tool in the tool
bar or use the key commands [M] to mute or [shift]+[M] to unmute.
Time Lock and Edit Lock Icons
The Time Lock icon appears on an Event when the Time Lock feature has been enabled. Time Lock keeps the Event from being moved
to a different time position within the Track.
Similarly, the Edit Lock icon appears when the Edit Lock feature has been enabled. Edit Lock prevents the contents of the Event from
being altered in any way. To toggle the Time or Edit Locks, [Right]/[Ctrl]-click onto the Event you would like to lock and click onto the Time
Lock or Edit Lock checkboxes from the Event contextual menu.
When you use both features at the same time, a padlock icon will appear on the Event:

## Events

For more information about the Time or Edit Lock feature, check out theLock Tracks or Events page.
Event FX Icon
In Studio One, you can apply an effect on a single Event rather than the entire track. To do this, you can simply drag an effect from the
Browser section, hold down [Alt]/[Option], and drop it onto the chosen Event.
Note that when you are working with ARA (Audio Random Access) effects, like Melodyne or VocAlign, the same icon will appear, as they
are essentially Event effects. Adding a second ARA to an Event will replace the previous effect with the second.
For more information about applying effects to individual Events, check out the Track and Event Inspectors page.
Chain Icon
The Chain Icon represents Audio Events that have been consolidated into a nestled unit. To merge Events, select the Audio Events that
you would like to consolidate and click the key command [G].

## Events

Ghost Icon
When you duplicate merged Events, the Ghost Icon appears next to the Chain Icon. Duplication not only creates an identical Event. Any
changes made to the original merged Event will also be made to the duplicated Events. In this way, you can easily modify duplicated
snare hits or guitar parts placed throughout your song at once.
To duplicate your merged Event, [Right]/[Ctrl]-click onto the Event you would like to duplicate and click onto the “Duplicate Shared”
option from the Event contextual menu or use the key command [Shift]+[D].
Folder Icon
When you see the Folder Icon on an Event, that means it belongs to a folder with other Events. Creating Folders can be helpful when you
would like to group similar Events together, like drums or vocal harmonies. Placing these Events into folders can make the Arranger Win-
dow much easier to navigate.
To create a Folder, select the tracks you would like to place into one folder, [Right]/[Ctrl]-click, and select the option “Pack Folder” from
the drop-down menu.
Layer Icon
This icon will appear on your Event if you have recorded several layers (or “takes”) of the Event. Alternatively, this icon can mean you
have several pattern variations to choose from.
If you have various takes to choose from and would like to expand the Event to see all of the takes, [Right]/[Ctrl]-click, select the option
“Unpack Takes” from the drop-down menu, and choose to unpack the takes to tracks, new layers, or to existing layers. For more inform-
ation about recording and editing takes, check out the  Comping page.

## Events

If you’ve created several variations of a drum pattern, you change the variation from the pattern editor or click onto the Layer/Pattern Icon
and click onto the variation you wish. For more information about creating patterns and pattern sequencing in Studio One, check out the
Patterns page.

## Arrange View Mouse Tools

The mouse tools allow direct interaction with Events, using the mouse. It is helpful to remember that the mouse tool actions can be
undone at any time, so feel free to explore them. [Right]/[Ctrl]-click in any open space in the Arrange or Edit views to open a list of mouse
tools and editing commands. Use the left mouse button to make a selection. You can also click the middle mouse button or the scroll
wheel in the open space to display an expanded list of tools, including all of the Paint tool shapes.
In the Arrange view, the following mouse tools and related functions are available from left to right in the toolbar.
Link Button
The bracket-shaped button on the left side of the toolbar is the Link button. Click it to combine the Arrow and Range tools. When it is
engaged, the mouse operates as Range tool in the area above the horizontal center line of the Event, whereas the Arrow tool is available
in the area below the center line. This combination of tools is available at track heights of Normal or higher.
Arrow Tool
This tool is selected by default. Click on the Arrow tool button or press [1] on the keyboard to select the Arrow tool. The Arrow tool can be
used for the following purposes:
Move an Event
To move an Event using the Arrow tool, click anywhere on the Event and drag left, right, up, or down. Dragging the Event left or right
moves the Event backward and forward in time, relative to the current Timebase and Timeline zoom. When dragging an Event left or right
beyond the viewable arrangement, hold [Space Bar] on the keyboard to speed up the scrolling.
Dragging the Event up or down moves the Event to another existing Track of the same type. If the Event is dragged to a position where
no Track currently exists, Studio One creates a new Track of the same type.
When dragging an Event from one Track to another (up or down), the position of the Event is constrained within an automatic snapping
range to make it easy to keep the Event at the same time position. To defeat this snapping, hold Shift while dragging the Event up or
down.
Size an Event
Events can be thought of as windows into audio files and musical performances, where what you see is what you hear. Sizing is a fun-
damental technique wherein Events are made shorter or longer, so that only a portion of the audio or note data they contain is seen and
heard. To size any Event using the Arrow tool, float the mouse to the left or right edge of the Event to reveal the Sizing tool. When this tool
appears, click-and-drag left or right to size the Event. Events can be sized and resized nondestructively any number of times.
Two adjacent Events can be sized simultaneously so that no gap is created between them. To do this, float the Arrow tool to the bottom
of where the two Events meet in the Timeline, where you can see the sizing icon with both left and right arrows illuminated, and then
click-and-drag left or right.
Holding [Alt]/[Option] on the keyboard and then sizing an Event from the right edge results in the Event being freely timestretched. Refer
to the Timestretching section of this chapter for more information.
Adjust Audio Event Volume Envelopes
All Audio Events feature a basic volume envelope that allows the volume of the audio to be shaped in several ways. Using the volume
envelope, you can create a fade-in and fade-out, as well as set a constant volume level between the fades. The volume envelope applies
gain changes to the audio clip in the Event and is therefore at the front end of the audio signal path.

## Arrange View Mouse Tools

To create a fade-in or fade-out, click-and-drag left or right on the Fade Flag in the upper left or right corner of an Audio Event. By default,
a linear fade is created over the length you have moved the Fade Flag. Fade times, as well as Event gain, can also be edited in the
Inspector for any selected Event.
To change the curve of the fade, click on the Fade Curve box in the middle of the fade curve and drag up or down. The fade curve determ-
ines how quickly or slowly the fade occurs and changes over time. If you press and hold [Shift] while editing the fade length or the curve,
you can edit both at once. Dragging up or down edits the curve, and dragging left or right changes the length.
It is also possible to drag a complete crossfade left or right, or up or down, in order to change the location and characteristics of the fade.
Float the mouse to the center of the crossfade until the Hand icon appears, then click and drag to adjust. Dragging left or right adjusts the
location of the fade, extending or shortening the crossfaded Events. Dragging up or down alters the shape of the crossfade.
To adjust the overall volume level of an Audio Event, click on the volume box in the center of the volume envelope and drag up or down.
As you adjust the volume envelope, the audio waveform is redrawn to approximate the effect of the adjustment.
You can also create complex envelopes anywhere inside an Audio Event using Clip Gain Envelopes.
Select Multiple Events
Multiple Events can be selected in order to edit them all at once, with a single action. To select multiple Events with the Arrow tool, do one
of the following:
-
Click outside of the range of an Event, and then drag over any other Events; a gray box is drawn while you drag over the target-
selection area. Release the mouse button once the box is drawn over all of the Events you wish to edit, and these Events are
selected for editing.
-
Click on any Event, then while holding [Shift] on the keyboard, click on any other Events to select them. This allows you to select
multiple Events that are not in close proximity to each other. All selected Events can then be edited at once.
-
Click on any Event, then press [Alt]/[Option]+[Shift]+[Home] or navigate to Edit/Select/Select from Start to Event, to select all
Events on all Tracks that lie between the start of the Song and the current Event.
-
To select all Events on the currently selected Track that lie between the start of the Song and the current Event, press
[Shift]+[Home].
-
Click on any Event, then press [Alt]/[Option]+[Shift]+[End] or navigate to Edit/Select/Select from Event to End, to select all
Events on all Tracks that lie between the current Event and the end of the Song.
-
To select all Events on the currently selected Track that lie between the current Event and the end of the Song, press
[Shift]+[End].
-
Double-click on the timeline of a Track in the Arrange or Edit view while holding [Shift], to select all Events present on that Track.
Normally, when you select multiple Events and adjust volume or fade in/out shape on one of them, all selected Events change to match
the new setting. If you want to adjust an individual Event without losing your selection, hold [Alt] while making your changes.
Select a Range
Like the Range tool, you can use the Arrow tool to select a range, or area, within Tracks and their contents, without switching tools. Do
this by hovering the Arrow tool in the upper half of a track. The cursor changes to a crosshair shape. Click-and-drag to select your chosen
range.
You can enable or disable this feature by clicking the Link button to the left of the Arrow tool in the toolbar.

## Arrange View Mouse Tools

Alternate Arrow Tool Uses
For speed and efficiency when editing, a selection of modifier keys can be applied while the Arrow tool is selected, giving temporary
access to the following alternate tools and editing modes:
-
Alternative Tool Hold [Ctrl]/[Cmd].
-
Slip Editing Hold [Ctrl]/[Cmd]+[Alt] while floating the Arrow tool over an Event.
-
Define Tempo Hold [Ctrl]/[Cmd]+[Alt]/[Option] while floating the Arrow tool over the edge of an Event.
Alternative Tool
The Alternative Tool feature allows you to quickly access an alternate tool of your choice when using the Arrow tool by holding [Ctrl]/
[Cmd]. The Range, Split, Eraser, Paint, Mute, Bend, and Listen tools can all be used in this way.
You can choose your Alternative Tool from the drop-down menu beneath the Arrow Tool, or by repeatedly pressing the [1] key on your
keyboard to cycle through the options. The currently-active Alternative Tool is highlighted with a blue underline in the Tools list.
Range Tool
The Range tool is used to select a range, or area, within Events. Click on the Range tool button or press [number 2] on the keyboard to
select the Range tool.
To select a range within an Event, using the Range tool, click-and-drag over the area to be selected; a gray box is drawn over the target
selection area. Release the mouse button when the box is drawn over the range of the Events you wish to select. The range you have
selected is now treated as a single, consolidated Event. Clicking once with the Range tool on a Track moves the play cursor to that loc-
ation.
For instance, you can use the Range tool to select the content of several Audio Events across multiple Tracks in bar 12, and then use the
Arrow tool to move that section of audio to bar 14. Another common use of the Range tool is to quickly select and delete a range of audio
within an Event, rather than using the Split tool to make two splits, then select and delete the section with the Arrow tool.
When you float the mouse cursor over a selected range, the Arrow tool temporarily appears. This makes it easy to quickly select and edit
a range of Events.
To select multiple, non-contiguous ranges across any Event, on any Track, hold the [Shift] key while using the Range tool. Continue to
hold [Shift] and use the Arrow tool to select whole Events. For instance, when using the Arrow tool, if you press and hold [Ctrl], you get
the Range tool. Press and hold [Ctrl] and [Shift] to select multiple ranges, then continue to hold [Shift] but release [Ctrl]; now you have the
Arrow tool and can select whole Events. All of your selections remain selected.
To split an event in half without reaching for the Split tool, double-click at your chosen split point. Double-click a selected range to split the
Events in that range at the left and right borders of the range.
If Snap to Grid is enabled, your selections using the Range tool snap to the value set by the Snap Timebase parameter. To temporarily
reverse the Snap to Grid option while editing, hold the [Shift] key.
Selected ranges can be sized by floating the Range tool at the left/right edge of the selection. You also can split a selected range at the
left and right edges of the selection by choosing Split Range from the Edit menu or by pressing [Ctrl]/[Cmd]+[Alt]+X after selecting a
Range.
To temporarily switch to the Arrow tool while the Range tool is selected, hold [Alt].

## Arrange View Mouse Tools

Split Tool
Using the Split tool, single Events can be split into multiple Events. Click on the Split Tool button, or press [number 3] on the keyboard to
select the Split tool.
With the Split tool selected, a vertical and horizontal line is drawn near the current mouse-cursor position. The vertical line indicates the
exact time position of the Split tool, while the horizontal line underscores the Track on which the Event to be split resides. The Split tool is
directly affected by the current Snap settings.
Click on any Event with the Split tool to split the Event at that position. By splitting a single Event, you create two Events that can be
edited independently. If multiple Events are selected across multiple Tracks, the Split tool affects all of the selected Events in the same
way.
It is also possible to split selected Events at the timeline cursor, without using the Split tool, by pressing [Alt]+[X] on the keyboard. If you
have a range of time selected, pressing [Alt]+[X] will split the selected content into a new Event.
To temporarily switch to the Arrow tool while the Split tool is selected, hold [Alt].
Splitting Instrument Parts
Normally, if you split an Instrument Part at a point that falls within one or more notes, those notes are truncated at the split point, and no
longer play in the newly created Part to the right of the split point. This can be an issue, especially when splitting up Parts in which some
notes are held for long periods, such as pad and string passages.
For example, if you have a four-bar Part in which a chord is played and held throughout, splitting the Part in the middle leaves the Part to
the left of the split point mostly untouched. However, the held notes are now missing from the newly created Part to the right of the split
point.
To split an Instrument Part and split (rather than truncate) any notes that cross the split point, hold [Alt]/[Opt] while you make the split.
Eraser Tool
The Eraser tool is used to delete Events. Click on the Eraser Tool button or press [number 4] on the keyboard to select the Eraser tool. To
delete any Event using the Eraser tool, simply click on the Event. If multiple Events are currently selected, clicking one of the Events with
the Erase tool erases all selected Events.
You can click and drag across multiple Events with the Eraser tool, erasing each Event you touch.
To temporarily switch to the Arrow tool while the Eraser tool is selected, hold [Alt].
Paint Tool
In the Arrange view, the Paint tool can be used in two ways: to create an empty Instrument Part on an Instrument Track, or to create a
complex Gain Envelope for an Audio Event. Click the Paint Tool button or press [number 5] on the keyboard to select the Paint tool.
Create an Instrument Part
To create a new, empty Instrument Part on an Instrument Track with the Paint tool, click-and-drag over any empty area in the Track lane
of the Instrument Track. Clicking once with the Paint tool creates an empty Instrument Part that varies in length according to the current
timebase setting.
Create a Gain Envelope
To view, create, or edit a Gain Envelope, [Right]/[Ctrl]-click an Audio Event and enable the Gain Envelope box. The white line that
appears inside the Audio Event represents the current Gain Envelope. If a Gain Envelope does not already exist, you'll see a white hori-
zontal line running through the zero point of the waveform.
When using the Arrow tool you must click somewhere on that white line to add a Gain Envelope point. Note that the gain of the entire
Audio Event can be raised or lowered after adding the first point: simply click-and-drag that point up or down to adjust the gain of the
Audio Event. When more points exist, the click-and-drag method affects only part of the Audio Event, not the whole thing.
The Paint tool lets you click-and-drag anywhere inside the Audio Event to add new points. The menu arrow under the Paint tool icon
reveals the list of Paint tool shapes: Freehand, Line, Parabola, Square, Triangle, Saw, Sine, and Transform. Select one of the shapes
and experiment with it by click-dragging across the Audio Event. You can always undo those actions.
To bypass a Gain Envelope (i.e., disable it without deleting it), [Right]/[Ctrl]-click the Audio Event and activate the Bypass button. For
more details, see the Clip Gain Envelopes section.
Mute Tool
In the Arrange view, the Mute tool is used to mute Audio Events, Audio Parts, and Instrument Parts. Click on the Mute Tool button or
press [number 6] on the keyboard to select the Mute tool. To mute or unmute any Audio Event or Instrument Part, simply click on it with

## Arrange View Mouse Tools

the Mute tool. When an Event or Part is muted, it appears grayed out, and an “m” icon appears in the lower left corner of the Event or
Part.
Click and drag the Mute tool to select multiple Events to mute. If multiple Events are already selected, clicking one of them with the Mute
tool mutes all selected Events.
To temporarily switch to the Arrow tool while the Mute tool is selected, hold [Alt].
Select Muted Events
Sometimes, you may use Event muting to silence superfluous Audio or Instrument content that you don't intend to use. If you decide you
want to get rid of these unused Events, you can quickly select all muted Events by navigating to Edit/Select/Select Muted Events, then
simply press [Backspace] or [Delete] to delete (and clear away) the unwanted Events.
Bend Tool
In the Arrange view, the Bend tool is used to manipulate, add, and remove Bend Markers. For more information on Bend Markers, refer
to the Transient Detection and Editing section of this chapter.
Listen Tool
In the Arrange view, click and hold on any Track to instantly solo the Track and start playback from the position you clicked. Playback con-
tinues as long as the mouse click is held. When the mouse click is released, playback is stopped, and the related Track is un-soloed.
For more information about the paint tool, see the  Editing Automation Envelopes page.

## Clips and Clip Gain Envelopes

About Clips
In Studio One, a "Clip" is a representation of an audio file that is used in a Song. The audio file itself is typically stored in the Song's Media
folder; though, it can be stored in another location, in which case it's called an "external file."
The reason we use Clips in Studio One is because they also contain metadata describing the processing of the audio file they rep-
resent—its Gain Envelopes, bend markers, Melodyne edit state, chord data, and more. This allows the Clip’s metadata and attributes to
be used in different ways on different Audio Events without the need for bouncing (duplicating) the actual audio file. This lets you get
many different sounds through different processing of the same audio file while keeping your Song folder size under control .
Audio you record or import (depending on the preference setting for "Ask to copy external files when saving Song") are represented as
Clips in the Browser’s Pool, while the actual audio files are stored in your Song’s Media folder. Either can be explored in the Pool tab of
the Browser. You can add Clips to a Track from the Pool via drag and drop.
Clips make nondestructive editing of your sounds possible because most edits made to Audio Events in Studio One are actually affecting
the Clip’s metadata, and not the audio file itself.
Edits made to a single Clip will ordinarily affect every instance of the clip in a Song. This can prove undesirable in some cases—and can
be avoided by using...
Clip Versions
A Clip Version is a completely separate copy of a Clip with its own, independent metadata that can be manipulated independently of that
of its parent audio file. Clip Versions will allow you to apply different Melodyne or Gain Envelope edits to different instances of the same
audio. This means you can make multiple Clip Versions of the same Audio Event with no need to use up hard drive space with extra cop-
ies of the same audio file!
An example use case involves Melodyne and the Chord Track. If you would like to use Melodyne to have an audio loop follow chords on
the Chord Track, each instance of the loop will require different Melodyne edits to manipulate the playback depending on the chord
changes on the Chord Track. Clip Versions solve this issue by letting you create multiple Clips with different pitch corrections from Melo-
dyne.
You could also use Clip Versions to create several different instances of a single drum loop that each contain different Gain Envelopes.
This allows you to create evolving rhythmic patterns over the course of a song without the need for repeated bounces.

## Clips and Clip Gain Envelopes

To create a Clip Version:
1.
[Right-Click] an Audio Event
2.
Choose “Audio”
3.
Choose “New Clip Version”
This will create and apply a new instance of the Clip whose parameters can be modified without affecting other instances of the same
audio. Try editing the new Audio Event’s Gain Envelope, and note that these changes do not affect the original Event.

## Clips and Clip Gain Envelopes

To create multiple Clip Versions simultaneously, you can use “Separate Shared Copies.”
1.
Use the Arrow Tool to group-select several instances of the same Audio Event, such as duplicates of the same loop.
2.
[Right-Click] any of the selected Audio Events
3.
Choose “Event”
4.
Choose “Separate Shared Copies”
(Alternatively, you can group-select Audio Events and press [ALT-C] to apply “Separate Shared Copies.” )
"Separate Shared Copies" then creates one new copy of each Clip Version used by the selected Audio Events. Groups of Events sharing
a Clip Version will still share the new Version.
Clip Versions will be labeled in the Pool tab of the Browser with a small number icon to the left of their waveforms. The version number is
also visible in a small number icon on the lower left of the Audio Event itself in the Arrange Window.
Note that clip versions cannot have individual tempos.

## Clips and Clip Gain Envelopes

Clip Versions can be dragged and dropped from the Pool into the Arrange Window. Hold [ALT] while dragging a Clip Version onto a Clip
to replace it with the dragged Version.
Clip Gain Envelopes
To view the Gain Envelope for the selected Audio Event, [Right]/[Ctrl]-click and enable the Gain Envelope box in the menu. A white line
inside the Audio Event shows the current Gain Envelope. If a Gain Envelope does not already exist, the white line runs horizontally
through the zero point of the waveform.
Note that Clip Gain Envelopes are Clip-based. Any changes made to an Audio Event will affect all shared copies of that Audio Event—
unless you use Clip Versions, of course.
Mouse Tool Access
To open the list of mouse tools when the Gain Envelope is already visible, hover the cursor in an empty space above the zero line. When
it changes into the Trim Tool, use [Right]/[Ctrl]-click to access the mouse tools.
Using the Arrow Tool
The Arrow tool can be used to add new points to a Gain Envelope, move existing points, and select points for deletion. Note that Gain
Envelope points can also be selected using the left and right arrow keys. Multiple points can be selected at once by holding [Shift] or
[Option] and selecting the desired range, and then edited simultaneously as described in the following sections.
After the first point is added, the gain of the entire Audio Event can be changed by dragging that point up or down.
To add a new point, click anywhere on the current Gain Envelope. If other points exist, you can click-and-drag the new one to the desired
position to create a new segment.
Move or Modify a Gain Envelope Point
To move a Gain Envelope point, click-and-drag the point up or down, left or right. Vertical changes affect the value; horizontal changes
affect the timeline position. Moving a point below the center of the waveform reduces the gain, while moving it above the center increases
the gain.
When moving an Envelope Gain point, the pop-up value indicator displays the position, current value, and the amount of change from the
previous value.
If Snap is engaged in the Arrange view, the point snaps to the grid when the cursor is released.
To enter a specific value for an existing Gain Envelope point, [Right]/[Ctrl]-click on the point and type a number into the Value field.
Another way to change a value is to float the Arrow tool over a point, hold [Alt]/[Option], and scroll the mouse wheel to move the point up
or down.
To fine-tune the value or location of a Gain Envelope point, hold down [Shift] while moving the point.
If you drag a Gain Envelope point beyond other points, those points are moved also. The original positions are remembered until the
cursor is released, and then any duplicate points at that position are deleted. To restore the deleted points, undo the action.
Delete a Gain Envelope Point
To delete an existing point on a Gain Envelope using the Arrow tool, select the point and press [Delete], or [Right]/[Ctrl]-click on the point
and select Delete from the pop-up menu.
Change the Segment Curve
When you hover the cursor over a Gain Envelope segment a curve handle appears on the white line. Click-and-drag the handle up or
down to shape the curve of that segment. For more precision control, [Right]-click the handle to access a contextual menu that will let you

## Clips and Clip Gain Envelopes

enter the desired curve value and type of your choice.
Using the Paint Tool
The Paint tool draws a series of Gain Envelope points with a single action. You can click-and-drag anywhere inside the Audio Event to
add new points; you don't have to click on the existing Gain Envelope first.
The menu arrow under the Paint tool icon reveals the list of Paint tool shapes: Freehand, Line, Parabola, Square, Triangle, Saw, Sine,
and Transform.
To switch from the Paint tool to the Arrow tool temporarily, hold [Alt] and then click-drag across the Audio Event.
For more information about the paint tool, see the  Editing Automation Envelopes page.
Draw a Gain Envelope
Using the Paint tool, click-and-drag inside the Audio Event to draw a Gain Envelope. Note that drawing new Gain Envelope points over-
writes any existing points.
Draw with Shapes
With one of the Paint tool shapes selected, click-and-drag across the Audio Event to draw a new envelope.
When using the waveform shape tools, hold [Alt] while dragging to adjust the frequency of the drawn waveform, or hold [Ctrl] to vary the
amplitude and polarity of the waveform. Hold [Ctrl]/[Cmd]+[Alt] while drawing to move the Gain Envelope shape left or right along the
timeline.
Transform a Gain Envelope Segment
The Transform tool can be used to alter existing Gain Envelope segments, or to add a new one. With the Transform tool selected, click-
and-drag a selection box around any area of a Gain Envelope; then, adjust the selection box by clicking-and-dragging one of eight
handles (four sides and four corners) to scale the selected Gain Envelope points.
Using the Range Tool
The Range tool can be used to trim selected areas of the Gain Envelope up or down in value. This can be done in two ways:
Trimming a Gain Envelope Segment
If you want to trim a single Gain Envelope segment, select the Range tool and hover the cursor in the upper half of the segment until the
cursor changes into the Trim Tool. Click-and-drag up or down to change the selected Gain Envelope segment.
Trimming a Gain Envelope Range
If you want to trim several Gain Envelope segments at the same time, use the Range tool to select a range of the Gain Envelope. Then,
hover the cursor in the upper half of the selected range until the cursor changes into the Trim Tool. Click-and-drag up or down to trim the
selected range of the Gain Envelope.
Bypass the Gain Envelope
A Gain Envelope can be bypassed temporarily so you can compare the Audio Event with and without the Gain Envelope. To do this,
[Right]/[Ctrl]-click the Audio Event below its zero point and activate the Bypass button. This technique also allows you to disable the Gain
Envelope without resetting it. The status of the Bypass button is saved with the Song.
Reset the Gain Envelope
To remove all Gain Envelope segments from an Audio Event, [Right]/[Ctrl]-click the Event, scroll down to the Audio Operations menu,
and select Reset Gain Envelope from the menu.
Have Gain Envelope, Will Travel
When an Audio Event is moved its Gain Envelope moves with it because Gain Envelopes are Clip-based. This means the Gain Envelope
also moves when "slipping" the audio within an Event.

## The Grid

The Arrangement grid is comprised of the ticks in the timeline and the vertical lines extending from those ticks through the background of
the Arrangement. This grid uses the Timebase setting as the basis for its display. The Timebase settings are Seconds, Samples, Bars,
and Frames, and they determine the behavior of Event and tool snapping. The Timebase can be changed at any time, without directly
affecting the arrangement.

## The Grid

Perhaps the most common Timebase setting is Bars, which display time in a musical format of bars and beats. With this Timebase set-
ting, the grid is determined by the settings in the Quantize panel.
Quantize Panel
The Quantize panel can be opened from the toolbar by clicking on the Quantize Panel button, or by selecting Quantize from the View/Ad-
ditional Views menu. The Quantize panel can be detached and freely placed on the screen. In this panel, you can edit all settings related
to the Quantize grid that are displayed in the Arrangement. From left to right in the panel, you can see areas for Grid or Groove mode;
note-value selection; note grouping and Swing amount; Start, End, Velocity, and Range percentages; and preset management.
The Quantize panel can be opened from the toolbar by clicking on the Quantize Panel button, or by selecting Quantize from the View/Ad-
ditional Views menu. The Quantize panel can be detached and freely placed on the screen. In this panel, you can edit all settings related
to the Quantize grid that are displayed in the Arrangement. From left to right in the panel, you can see areas for Grid or Groove mode;
note-value selection; note grouping and Swing amount; Start, End, Velocity, and Range percentages; and preset management.
Note that independent Quantize panels are also available for the Note Editor and the Audio Editor. This enables you to define the
rhythmic character of each aspect of the Song and perform those edits quickly without having to adjust the settings each time. You can
show or hide the Quantize panels for each of those by clicking the appropriate Quantize panel button. You can also close the Quantize
panel for the currently selected view by navigating to View/Additional Views/Quantize.
Rhythmic Values
With Grid mode selected, you can choose a note value between whole notes and 64th notes, and the following musical note groupings:
Straight (with a Swing percentage setting), Triplet (3 notes in the space of 2), Quintuplet (5 notes in the space of 4), or Septuplet (7 notes
in the space of 8). These settings also determine the look and behavior of the grid in the Arrange view. For information on the Groove
mode of the Quantize panel, refer to the Groove Extraction and Quantize section.
Swing
Swing is a rhythmic style you can apply, in which off-beats are moved forward in time relative to on-beat notes, creating a relaxed,
bouncy feel. This offset is calculated based on the currently selected Quantize value. For example, at 100% Swing, with 16th-note quant-
ize selected, a pattern of 16th notes play at a 2:1 ratio; On-beat notes play on beat, and offbeats play as though they were the final 16th-
note triplet in a group of three. You can set the amount of swing between 0% (straight timing) and 100% (fully swung).
Quantize Note Starts
The Start percentage defaults to 100%, which means that the start of a selected note, Event, or transient snaps to the grid if quantized.
This is effectively a quantize-strength parameter, where anything less than 100% moves the note, Event, or transient a relative amount
closer to the grid, instead of all the way to the grid.
Quantize Note Ends
The End percentage only affects notes in Instrument Parts. The function is similar to the Start percentage, except that it affects the note
end, effectively making quantized notes shorter or longer. The Velocity percentage also only affects notes and adjusts note velocity
according to an extracted groove if the Quantize mode is set to Groove.
Velocity Sensitivity
The Velocity percentage lets you tie Quantize strength to note velocity, to the degree that you specify.
Quantize Range
The Range percentage sets the relative range from grid lines within which notes, Events, or transients are quantized. Notes, Events, or
transients beyond this relative range are not quantized. As there is no display indicating the Range, quantizing several times while adjust-
ing this setting may lead to the best results.
The presets area of the Quantize panel allows you to quickly switch between up to five Quantize panel settings, so that working with mul-
tiple complex quantization setups is very easy. You can also store and recall Quantize panel settings, just as you would store an effect or
instrument preset.

## The Grid

## Common Editing Actions

Cut, Copy, and Paste
As with most software applications, Studio One supports cut, copy, and paste actions. Once you have selected an Event or a range of
Events, you can perform these actions:
-
Cut Press [Ctrl]/[Cmd]+[X] on the keyboard to cut the current selection.
-
Copy Press [Ctrl]/[Cmd]+[C] on the keyboard to copy the current selection.
-
Paste Once a selection is cut or copied, press [Ctrl]/[Cmd]+[P] on the keyboard to paste the selection. The Events are pasted on
the selected Track, at the current playback cursor position. If you select and copy Events on multiple Tracks, then select another
timeline location on the first Track, and then paste, the copied Events are pasted in the appropriate Tracks and locations, start-
ing with the first (selected) Track.
-
Paste at Original Position If you want to copy and paste an Event from one Song into another Song (or another version of the
Song), and want the Event to be placed at its original location in the timeline, copy the Event and paste by pressing [Ctrl]+[Shift]+
[V].
Audio Event Slip
Often, after an Audio Event has been sized to fit a particular region of time, the audio clip the Event contains needs to be moved ahead or
behind in time without changing the Event’s length and volume envelope. This action is commonly called “slipping” or “slip,” and it is often
used alongside splitting, or splicing, to correct the timing of rhythm tracks. For instance, if one snare-drum hit is off the beat by a little bit,
you could split the Event on either side of that section and then slip the audio into perfect time.
To use Slip, select the Arrow tool, and then press and hold [Ctrl]/[Cmd]+[Alt] on the keyboard, while floating the mouse over an Audio
Event. The Slip tool icon appears. Click-and-drag on the Event to slip the audio left or right across the timeline. Multiple Audio Events can
be selected and slipped at once, even across multiple Tracks.
When slipping the audio in an Audio Event, note that all of the Event characteristics remain unchanged, including the Event size, pos-
ition, Inspector parameters, and volume envelope.
An Audio Event can be slipped only as far as the length of the audio clip it contains.
Audio Event Transpose and Tune
The ability to transpose and fine-tune audio adds a lot of flexibility when working with audio files. For instance, if you have a keyboard
loop collection in which every loop is in the key of C, being able to transpose these loops to any other key opens up many possibilities.
In Studio One, transposing and tuning are a part of the same set of advanced algorithms as timestretching, so the quality is extremely
high.
To transpose any audio Event, select it and open the Inspector by pressing [F4] on the keyboard or clicking on the Inspector button
above the Track Column. Then enter a value in the Transpose field, from -24 to +24 semitones.

## Common Editing Actions

Tuning is similar to transposing but the pitch is changed in cents, rather than semitones. Enter a value from -100 to 100 cents in the Tune
field to fine-tune the audio Event.
Any number of Events can be selected and transposed or tuned simultaneously, but note that this change is not relative to the current set-
ting of each Event. All selected Events are transposed or tuned to the same chosen value.
Nudge
Nudging is an alternative to moving Events and notes across the timeline with the mouse. To Nudge any Event or note, select it and do
one of the following:

## Common Editing Actions

-
Nudge Press [Alt]+[Right Arrow] on the keyboard to move the Event or note forward in time by the current snap value in the
Arrangement or Editor. With Snap disabled, nudging adjusts in milliseconds.
-
Nudge Back Press [Alt]+[Left Arrow] on the keyboard to move the Event or note backward in time.
-
Nudge Bar Press [Ctrl]/[Cmd]+ [Alt]+[Right Arrow] to move the Event or note forward by one bar.
-
Nudge Bar Back Press [Ctrl]/[Cmd]+ [Alt]+[Left Arrow] to move the Event or note backward by one bar.
Any number of Events or notes can be selected and Nudged simultaneously. The Nudge commands are also available in the Edit menu.
Duplicate
The Duplicate action essentially combines the Copy and Paste actions and intelligently places the pasted selection based on the musical
timing of the selection in the Song. Choose Duplicate in the Edit menu or press [D] on the keyboard to duplicate the current selection. The
duplicated Event is always placed after the original Event, and it is automatically selected once duplicated. As with the other editing
actions, Duplicate can apply to any number of currently selected Events.
A good use of the Duplicate command is to quickly create copies of a loop across a region in a Song by selecting an Event and
repeatedly pressing [D] on the keyboard. Another interesting use involves selecting very short regions within a loop, using the Range
tool, and duplicating them several times, consecutively, in order to create a stutter effect that is popular in electronic music.
If you would like to duplicate an Event and push existing material to the right across the timeline to make room for the duplicated Event,
press [Alt]+[D] on the keyboard to use the Duplicate and Insert command.
Duplicate Shared
When you duplicate an Event normally, each duplicate is treated as a separate Event, and edits made to one duplicate are not reflected
in the other copies. If you want to duplicate an Instrument Part and link the content of the duplicates to that of the original Part, select the
Part and choose Duplicate Shared from the Edit menu, or press [Shift] + [D] on the keyboard. A ghost icon appears on the original Part
and any Shared duplicates, to alert you that those copies are now Shared. Any edits made to the original Part or a Shared copy are
applied to all instances of that Part.
If you later decide you wish to edit one of the Shared copies of a Part individually, select it and choose Separate Shared Copies from the
Event menu. The ghost icon disappears from that Part to alert you that the copy is no longer Shared, and can be edited without affecting
the other copies.
Explode Pitches to Tracks
It is sometimes helpful to explode existing pitches within an Instrument Part to new Tracks, placing each pitch within individual Instrument
Parts on separate Tracks. For instance, if you have a MIDI loop to use with a virtual drum instrument, you may want to have each piece of
the drum kit on its own Instrument Track.
To do this, [Right]/[Ctrl]-click on an Instrument Part in the arrangement and select Explode Pitches to Tracks from the Instrument Parts
sub-menu.You can also accomplish this by selecting the Part, and choosing Explode Pitches to Tracks from the Events menu.
Strip Silence
It is quite common that, as the result of continuous recording, some Audio Events may have gaps of silence or relatively low levels
between performances. It may be helpful in these cases to remove the gaps and only keep the desired sections of the recorded Event.
Studio One's Strip Silence function, controlled from the Strip Silence panel, is designed to handle this task.
Open the Strip Silence panel by clicking on the Strip Silence button in the toolbar, or select Strip Silence from the View/Additional Views
menu. Select the Audio Events from which you wish to strip silence, make the desired settings, and then click on [Apply]. Click on the
[Default] button to return all settings in the panel to their defaults.
The result of the Strip Silence process is similar to using a gate processor to only allow the desired signal to be heard, except that the
Event is edited.
When the small light indicator next to the [Apply] button is lit, this means that changing the Detection or Event options and then clicking
Apply automatically undos the previous operation, making it easier to find the right settings by viewing the result of the Strip Silence pro-
cess, then tweaking the settings if needed without having to undo manually. Any change in selection (or other editing operation) ends this
automatic state, and the indicator is no longer lit.
The following describes each setting:
Detection This determines how Studio One identifies silence in the areas you wish to process.
-
Material The first three options set the Open and Close Threshold for the gate algorithm automatically.
-
Lots of Silence Choose this for material that contains lots of silence and single hits—for instance, a clean, typical
single-drum recording (hat, kick).

## Common Editing Actions

-
Little Silence Choose this for material that has some action going on but still has some silence—for instance, minimal
techno/single drum loops, ride, or snare tracks.
-
Noise Floor Choose this for material where there is almost no real silence—for instance, noisy drum recordings, over-
heads, drum mixes, and drum loops.
-
Manual Allows the Open and Close Threshold to be manually edited.
-
Open Threshold Set between -80 and 0.00 dB.
-
Threshold Link Engage to link the Close Threshold to the Open Threshold.
-
Close Threshold Set between -80 and 0.00 dB.
Events This section determines the nature of the Events created after removing silence.
-
Minimum Length Determines the minimum length in seconds for any resulting Event.
-
Pre-Roll Determines the amount of time in seconds that should remain at the beginning of resulting Events from the time at
which the previously detected silence ends.
-
Post-Roll Determines the amount of time in seconds that should remain at the end of resulting Events from the time at which
newly detected silence begins.
-
Fade-In Determines the length in seconds of the linear fade-in applied to resulting Events.
-
Fade-Out Determines the length in seconds of the linear fade-out applied to resulting Events.
-
Link Enable this option to automatically set the Fade-In parameter to match the Pre-Roll setting, and the Fade-Out parameter to
match the Post-Roll setting.
Audio Parts
It is often convenient to merge multiple separate Events into a single object in order to move them all together or simply to clean up the
Arrangement. This is accomplished with Audio Parts.
To create an Audio Part, select the Audio Events and then press [G] on the keyboard. This makes the separate Events appear and func-
tion as a single Event in the arrangement while also appearing and functioning as separate Events in the Editor. It is then much simpler
to, for instance, duplicate a chorus in the arrangement and retain access to the individual Events for editing crossfades and other details.
Note that Audio Parts support shared, or ghost, copies, with the exception of any Event FX which are strictly per Event instance.

## Common Editing Actions

An Audio Part has two options in the Event Inspector:
-
Play mode
-
Normal plays only the topmost Events, and any overlaps are not played.
-
Overlaps allows any overlapping audio to play back mixed, rather than cutting off at the end of each individual slice.
This often happens if individual slices are have been quantized but not timestretched.
-
Slices is optimized for REX and Audio Loop files, and adds short fades to slices during playback. Each slice is triggered
only once, and no overlaps are played.
-
Stretch Events timestretches Events inside the Audio Part to match the Song Tempo.
To dissolve an Audio Part, [Right]/[Ctrl]-click on the Audio Part and choose Dissolve Audio Part from the contextual menu.
Crossfade
Crossfades are useful for blending one Audio Event into another seamlessly.
Select two or more overlapping Events using the Arrow tool and press [x] to quickly apply a linear crossfade to the overlapping portions.
You can also use the Range tool to specify a crossfade’s start and end points; press [x] to apply the crossfade after selecting your Range.
When possible, gaps between Events will be automatically closed when a crossfade is applied.
Editing a Crossfade

## Common Editing Actions

Click and drag the control node in the center of the crossfade and drag the mouse up or down to create exponential crossfades.
Editing Options
The following options are related to Editing workflow.
Transport Options
Loop Follows Selection
With this option enabled, whenever you make an edit selection, the loop markers automatically snap to surround that selection. With
Cycle mode enabled, this allows for instant looping of a selection when editing, without further mouse movements or keystrokes. To dis-
engage this new loop bracket, click the mouse outside the current selection in Arrange view. These actions can only take place when the
Transport is stopped.
To enable this behavior, select Transport/Options/Loop Follows Selection, or [Right]/[Ctrl]-click in the Transport bar and choose Loop Fol-
lows Selection from the pop-up menu.You can also enable this option by pressing [Alt]/[Option]+[Ctrl]/[Cmd]+[P] on the keyboard.
Enable Play Start Marker

## Common Editing Actions

With this option enabled, the playback start marker is made separate from the edit selection, which it normally follows. This lets you
always start playback from a chosen location as you're editing, no matter where the edit selection currently lies. The play start marker
appears as a triangular marker in the timeline. To move this marker (and set a new playback start position), click-and-drag the marker
along the timeline.
To enable this behavior, select Transport/Options/Enable Play Start Marker, or [Right]/[Ctrl]-click in the Transport bar and choose
Enable Play Start Marker from the pop-up menu. You can also enable this option by pressing [Alt]/[Option]+[P] on the keyboard.
Return to Start Position on Stop
Many people prefer that when playback is stopped, the playback cursor returns to the position from which it started. This allows fast audi-
tioning of edits by repeatedly starting and stopping playback from a specific position in the timeline.
To enable this behavior, select Transport/Options/Return to Start on Stop, or [Right]/[Ctrl]-click in the Transport bar and choose Return to
Start on Stop from the pop-up menu. You can also enable this option by pressing [Alt]/[Option]+[Num Pad 0] on the keyboard.
Locate to the Mouse Cursor
To quickly locate the playback position to the mouse-cursor position, press [Ctrl]/[Cmd]+[Space] on the keyboard. This is very useful
when you want to quickly navigate to multiple edits for auditioning or further editing, without clicking in the Timeline.
Ripple Edit
In normal operation, if you delete a Part (or a section of a Part) from the timeline, all other Parts on the timeline remain in position,
and a space is left where the deleted Part was. If you'd like the Parts ahead of the deleted region to move backward to fill that space, say,
when editing spoken word content where gaps are undesirable, enable Ripple Edit mode. To do so, press the Ripple Edit button in the
toolbar.
Apart from automatically filling in gaps when cutting or deleting content, Ripple Edit also introduces a sort of "displacement" behavior
when editing. If you copy a Part and paste it in the middle of another, instead of replacing (or overlapping) that section of the target Part,
the target Part is split at the edit point, and moved forward in the timeline, to make space for the pasted Part. If you move a Part to the
start point of another Part, instead of replacing or overlapping the content below, the two Parts simply switch places.
Similarly, if you trim the end of a part to change its length, the Parts downstream move to maintain their relative position to the end of the
trimmed Part. This behavior extends to other editing operations, such as Crop to Content and Nudge/Nudge Back.
Follow Song and Follow Edit Position
If you would like the Arrange view to follow the current playback-cursor position, engage Autoscroll in the toolbar, or press [F] on the key-
board. This keeps all audible Events in view.
If you would like the playback cursor to follow the current edit position, engage Cursor Follows Edit Position, which is next to Follow Song
in the toolbar. With this engaged, the playback-cursor position jumps to the beginning of any Event or group of events you select, any
note being selected or moved, or to the position of any marker being moved.
Set Bar (or Second) Offset to Cursor
In some situations, it is helpful to set the bar or second offset to the cursor position. The “Set Bar Offset to Cursor” and “Set Second Off-
set to Cursor” options allow you to offset the bars/seconds within the project for lead-ins or sync up with imported stems. This feature is
especially helpful when composing to video.

## Common Editing Actions

To set your bar or second offset:
1.
Place your cursor to the specific bar or second where you would like the offset to occur.
2.
[Right]/[Ctrl]-click onto the timebase ruler and select whichever “Set Offset to Cursor” option from the drop-down menu that you
would prefer.
Note: You can also select this option from the Song drop-down menu.
Lock Tracks or Events
It can be a lifesaver to prevent a Track or Event from being accidentally changed, or worse, deleted. Once a Track or Event has reached
a certain level of completion, you may want to lock it that way while working on something else. This is simple to do.
What Locking Does Not Do
There are some actions that are still allowed after a Track is locked. You are still able to Mute or Solo the Track, change its order in the
Track List, change the color of the Track, and rename it. But every action that is not allowed will be greyed out and inaccessible until the
Track is unlocked again.
Locking an Event provides two options: Time Lock and Edit Lock. You can select one or both when locking an Event. Those options will
be described in the Event Lock section below.
Note that as with any other action, the process of locking a Track or Event becomes part of the Undo/Redo history. It can be undone with
[Ctrl]/[Cmd]+Z. So you may want to use the Save New Version feature as an additional backup after an important Track or Event is
locked.
Track Lock
The Lock Track option is available for Audio Tracks, Instrument Tracks, Automation Tracks, and Folder Tracks. To lock a Track, locate its
name in the Track List, use [Right]/[Ctrl]-click, and select Lock Track from the menu. Use the same action to unlock the Track by select-
ing Unlock Track from the menu.
Locking a Track prevents the addition or deletion of any of the Events it contains. It also will not allow any new Events to be recorded or
pasted into the Track. A locked Track cannot be removed from the Song. It also cannot be used by the Arranger Track.
Lock Tracks or Events

Event Lock
To lock an Event, locate the desired Event and use [Right]/[Ctrl]-click to open the menu. At the very top, under the Transpose and Velo-
city fields, are two options:
-
Time Lock Select this option to keep the Event from being moved to a different time position within the Track. A small circle-
slash clock icon will appear in the lower left corner of the Event window to indicate the Time Lock status of the Event. When an
Event is Time-Locked data can be added, removed, or altered inside the Event. The Event can be copied and pasted to any time
position on any Track (even on top of itself). You can also Duplicate this Event by pressing [D] on the keyboard repeatedly. A
time-locked Event that has been pasted or duplicated will also be time-locked.
Note that the Arranger Track is also not allowed to relocate an Event when the Time Lock option is active for that Event.
-
Edit Lock Select this option to prevent the contents of the Event from being altered in any way. This also locks the Transpose
and Velocity fields at the top of the menu. A small circle-slash pencil icon will appear in the lower left corner of the Event window
to indicate the Edit Lock status of the Event.
Note that it is possible for both Time Lock and Event Lock to be active for an Event. When this is true a small lock icon will appear in the
lower left corner of the Event window.
Convert a Part into a Pattern
Instrument Parts work well for extended passages and recordings of live playing, for example. But for rapid construction of a song where
a brief passage plays many times in a row, such as a synth bass line, it can be very useful to switch to pattern-based editing. Studio One
provides the best of both worlds and allows you to travel instantly between them.
To convert an existing Part into a Pattern, [Right]/[Ctrl]-click on the desired Part and select Convert Part to Pattern from the Instrument
Parts menu. This operation is also found in the Event menu. Studio One determines whether the Pattern should use Melodic Mode or
Drum Mode based on the Instrument, and the Part becomes a Pattern at that spot in the timeline. The maximum Pattern length is 64
Steps, so anything beyond that is truncated during the conversion.
After editing the Pattern as described in the Patterns section, you can convert it back into a Part using the same method: [Right]/[Ctrl]-
click the Pattern in the timeline and select Convert Pattern to Part, or select the operation from the Event menu.
Convert a Part into a Pattern

Audioloops and Musicloops
Studio One features two proprietary file formats, Audioloop (.audioloop) and Musicloop (.musicloop), that greatly enhance your ability to
create and re-use original material in your productions and to share your material with other Studio One users. The following describes
these formats and how to use them.
Audioloops
Audioloops are essentially Audio Parts tagged with a tempo and Song key signature; rendered with lossless compression. To create an
Audioloop, drag any Audio Part to the File Browser. You can then see the Audioloop listed, along with a drop-down arrow in the Browser
that, when clicked, reveals the Slices that the Audioloop contains.
[Screenshot] BrowserAudioLoop - Audioloop in the Browser, expanded to show its slices
Audioloops and Musicloops

Audioloops allow fast creation of flexible Audioloop from any source. For instance, you might take part of a drum recording you just made
and turn it into a loop by doing the following:
-
Export a stem for the drum bus for the desired range to a new stereo Track.
-
Detect transients on the new Track and then apply the Slice action, with the Merge option checked in the Audio Bend panel.
-
Drag the Audio Part to Browser to export an Audioloop you can use in any Song and can share with other Studio One users.
-
Alternatively, use the stem before slicing and drag the Audio Event to the Browser to export an Audioloop that stretches to the
song tempo.
Musicloops
A Musicloop consists of everything required to recreate a musical performance, including the virtual instrument preset, multichannel FX
chain presets for the virtual instrument outputs, the music-performance file, Song key signature, and an Audioloop. Musicloops can be
dragged in from the Browser, just like a MIDI file, but they are much more powerful in that they can re-create the exact setup used to
make the original performance.
To create a Musicloop, drag any Instrument Part into the Browser. You can see a pop-up display indicating whether you are exporting a
Musicloop or a MIDI file. By default, Musicloop is selected. To change this selection, press [Alt]/[Option] on the keyboard. Once exported,
you can see the .musicloop file in the Browser.
You can now drag this Musicloop into any Song to instantly re-create that performance, including creating the Instrument Track, loading
the virtual instrument, and loading any effects on the virtual instrument outputs. A Musicloop can be previewed in the Browser, just like
audio; the Browser plays the rendered audio file.
To see the contents of the Musicloop, [Right]/[Ctrl]-click on the Musicloop and choose Show Package Contents. You can now see a drop-
down arrow that, when clicked, reveals the elements described above. Each element can be dragged in separately; for instance, if you
just wanted to load the instrument preset from the Musicloop. Another nice benefit of Musicloops is that the rendered audio can be used
even if the instrument and effects used to create the Musicloop are not installed.
Note that when creating Musicloops, the related channel volume, pan, send, and busing details are not a part of the rendered audio or
stored preset.
Musicloops are an excellent way to store a personal library of original material very easily and to share that material with others without
worrying about what instruments or effects they have.
Also note that you will also need to set your Song key signature before exporting your Musicloops or Audioloops to have the Song key sig-
nature included in the loop. Learn more about Key Signature here.
Edit Groups
It can be useful to group multiple Tracks together so that any edits done to an Event on one Track in the Group are automatically done to
all Events for each Track in the Group. For instance, you may wish to group all of your drum Tracks together so that when the Events are
cut and moved, the relative timing between the Tracks remains intact.
Creating Edit Groups
There are two ways to create a new Edit Group:
-
Select the Tracks you wish to group.
-
[Right]/[Ctrl]-click on any currently selected Track.
-
Choose Group Selected Tracks from the pop-up menu.
You can also use [Ctrl]/[Cmd]+G after selecting the tracks to create a Group.
Whichever way is used, all Tracks that were selected are now a part of the new Edit Group. A name will be suggested for the Edit Group
based on the selected Tracks. If their names are similar, such as Snare 1 and Snare 2, the suggested name for the Group will be "Snare".
 Edit Groups

If the Track names are nothing alike, new Groups will be named in the order in which they are created (Group 1, Group 2, and so on). The
name of the new Edit Group is shown in the Edit Group selector box under the input selector on all Tracks in the Group. You can rename
an Edit Group by clicking in the Group selection box on any Track in the Group and selecting Rename Group.
There are two ways to add a Track to an existing Edit Group.
-
Click on the Edit Group box (under the input selector) on the desired Track in the Arrange view.
-
In the pop-up menu, choose the Edit Group to which you wish to add the Track.
The second way is to [Right]/[Ctrl]-click the desired Track and select Group Assignment from the menu. A check mark by a Group name
indicates the current Group for that Track. To change its Group assignment, select a different Group name.
When a Track is included in an Edit Group, selecting the Track selects all Tracks in the Group. Edit actions performed on any Event for
any Track in the Group are performed on all Events for each Track in the Group. Selecting a new color for any Track in the Group selects
that color for the entire Group.
Edit Groups also group the faders and several other features for the related Channels in the Group. This topic is discussed further in the
Groups section of the Mixing chapter. Note that it is also possible to create an Edit Group from a Folder Track.
If a Track is in an Edit Group, and an Event from the Track is viewed in the Edit view, the Group icon appears at the top left of the Edit
view, indicating that any edits performed on the Event in view affect other Events.
Dissolving Edit Groups
To dissolve (ungroup) an Edit Group, [Right]/[Ctrl]-click on any Track in the Group in the Arrange view. Then select Dissolve Group (1, 2,
3…), and the Group is dissolved. Grouping and dissolving actions can be undone and redone, as with most user actions.
Temporarily Suspending Edit Groups
Certain actions—such as moving a fader, muting, and soloing—can be performed on a Track within an Edit Group, without affecting the
Group as a whole, by temporarily suspending the Group. To do this, hold [Alt]/[Option] on the keyboard while performing an action on a
Track.
You can suspend an entire Group temporarily if many changes need to be made, and then reactivate the group with the same command.
To do this, hold [Shift]+G and type the first letter of the Group name into the small window that appears, or enter the Group number.
There is more information about this topic in the Groups section of the Mixing chapter.
Timestretching
It is possible to stretch an Audio Event to fit a tempo other than its original tempo, without changing the pitch. This is called Timestretch-
ing, and it can be used to effectively slow down or speed up an Audio Event. For instance, a one-bar drum loop recorded at 120 bpm
(beats per minute) can be stretched to fit into one bar at 100 or 140 bpm without significantly changing the pitch and overall sound of the
original audio.
Timestretching and defining a file tempo are nondestructive, so they can be undone and redone. It is also possible to switch Tempo
modes for any Audio Track, on the fly. For example, switching to Follow or Don’t Follow from Timestretch returns any timestretched
Audio Event that Track contains back to its original state.
When timestretching, if the tempo is drastically changed (by about 30 bpm or more), the audio can become slightly distorted. While this
can lead to interesting effects, you should be aware of the limitation of this technology.
In Studio One, timestretching can occur automatically or manually. The following describes these functions.
Manual Timestretching
With manual timestretching, you can stretch an Audio Event independently of the Song tempo or audio file tempo.
To manually stretch an Audio Event with the Arrow tool, float the mouse cursor to the left or right edge of the target Audio Event and hold
[Alt]/[Option] on the keyboard. The Timestretch tool appears, allowing you to click on the edge of the Event and drag left or right to
timestretch the Event, making it shorter or longer. In this case the length of the Event changes, using the Speedup factor, but the pitch of
the audio remains the same. Only the Event that you selected for timestretching is affected.
 Timestretching

Speedup factor is a timestretching function for making an audio clip shorter or longer while maintaining its pitch. This is used to stretch
Audio Events when you do not wish to define a tempo for the original audio clip, which would affect all Events associated with that clip.
The Speedup factor value changes during manual timestretching, and it also can be entered manually in the Event Inspector. Values
greater than 1 decrease the length of the clip, while values less than 1 make the clip longer.
Note that manual timestretching can not be used on an Audio Event containing a sliced loop.
Automatic Timestretching
Automatic timestretching is based on the relationship between the Song tempo and the audio file’s tempo.
Each Audio Track has a Tempo mode that controls the behavior of the Events on the Track, based on the Song tempo. The Tempo mode
can be selected in the Track Inspector. The following modes are available:
-
Don’t Follow Events on this Track are independent of the Song tempo. They are never moved or stretched automatically.
-
Follow The start positions of Events on this Track are tied to the musical grid. Thus, the Events move when the Song tempo
changes but they are not stretched.
-
Timestretch Event start positions follow the Song tempo, as in Follow mode. In addition, the Events are stretched to fit the Song
tempo.
Audio File Tempo Information
For automatic timestretching to work as described, Studio One needs to know the original tempo of an audio file. The software can then
calculate how to stretch the file to fit the Song tempo. Many audio loops have this information encoded.
Files without tempo information are not timestretched, even if the Track’s tempo mode is set to Timestretch.
Studio One offers two ways to define or change the original tempo information of an audio file.
If the original tempo for an Audio Event is unknown, the Arrow tool Timestretch function can be used to manually fit the Audio Event to a
specific length of time (bars and beats, etc). To do this, set the Tempo mode of the Track to “Timestretch.” Float the mouse cursor to the
edge of the target Audio Event and hold [Ctrl]/[Cmd]+[Alt]/[Option] on the keyboard. The Define Tempo tool appears, allowing you to click
on the edge of the Event and drag left or right to stretch it. In this case, the tempo for the original clip is set based on the musical length to
which the Event is stretched, and all Events in the Song that use this original clip are updated.
If the original tempo for an Audio Event is known but is not encoded in the original file that the Event references, you can easily set the file
tempo for the Event in the Inspector. Click in the File Tempo box, type in a new value and press [Enter] on the keyboard to enter a new
file tempo. If the corresponding Audio Track’s Tempo mode is set to Timestretch, entering a new value in File Tempo stretches all Events
in the Song that use this original clip, based on the entered tempo value.
Tap Tempo
You can use the Tap Tempo function to set the current Song tempo to the tempo that you hear in your Audio Events. To do this,
repeatedly click on the word “Tempo” in the Transport, clicking once on every beat you hear. Studio One determines the Audio Event
tempo based on the timing of your clicks and sets the tempo for the Song accordingly. Be sure that the Tempo mode for the Audio Track
is set to Don’t Follow; otherwise, the Events are stretched or moved while you are using the Tap Tempo function, making it impossible to
find a consistent tempo.
Timestretching Material Modes
Studio One features several optimized timestretching modes that may yield better results with certain types of audio material. To access
these modes, open the Inspector by pressing [F4] on the keyboard and click the Timestretch menu. Click on any mode to select it for the
 Timestretching

currently selected Track. The modes are:
-
Drums Use this optimized mode on any percussion track to achieve the best results when stretching percussive audio. This
mode uses the Elastique Direct algorithm.
-
Sound Use this general mode on any other type of track. This mode uses the Elastique Direct Formant algorithm.
-
Solo Use this optimized mode on any solo instrument or vocal track to achieve the best results. This mode uses the Elastique
Pro Monophonic Formant algorithm.
-
Tape In this mode the track audio follows the song tempo by changing the sample playback rate. This results in the pitch moving
up or down when the tempo changes, sort of like changing the speed control on a tape deck. Try this with drum loops or other
samples when the pitch doesn't need to be exact.
When using Tape mode, note that the Speedup, Transpose, and Tune settings in the Inspector are linked - editing one setting will affect
them all. Note that Tempo Track Automation that results in a pitch change is not reflected in “Transpose” or “Tune,” as these would con-
stantly change over time. See Track and Event Inspectors for more information on these settings.
Note: Some timestretch modes do not support precision timing changes. If you manipulate Bend Markers in an Event set to one of those
modes, Studio One automatically slices and repositions the sections of your audio (rather than timestretching them into place) for the
best results.
Using Timestretch Cache
The Use Cache for Timestretched Audio Files setting is engaged by default. This option also can be selected in the Studio One/Op-
tions/Advanced/Audio Engine menu (Mac: Preferences/Advanced/Audio Engine). Timestretch Cache creates a cache file at the correct
tempo for any files that need timestretching, based on what is currently being stretched in your Song. This improves Studio One’s per-
formance, as the timestretch process no longer needs to occur during playback. Studio One also can use a higher-quality timestretch set-
ting when it creates the cache file.
Using Timestretch Cache requires a certain amount of available space on your hard drive. If you know that space is relatively limited on
your hard drive, or if performance issues arise, disable this feature. When Use Cache for Timestretched Audio Files is deselected, Studio
One timestretches the file in real time during playback, as the file is being read from the computer hard drive.
Default Tempo Mode for New Tracks
When creating a New Song, notice that the New Song setup menu includes a Stretch Audio Files to Song Tempo checkbox. With this
option engaged, any new Track that is created in this Song has the Tempo mode set to Timestretch, and the software automatically
attempts to stretch audio files to the current Song tempo when they are imported into the Song. Otherwise, the default Tempo mode for
new Tracks is Follow.

## Comping

Comping is the process of piecing together multiple performances into a single, continuous performance. For instance, you might record
the vocals for a verse a number of times, then edit the best parts of each pass into a single, hybrid performance that, ideally, sounds as
though it was performed in one pass. Comping and related information are covered in the following sections.
Takes and Layers
The most common comping scenario involves recording multiple takes of audio and then editing those takes. In Studio One, each suc-
cessive recorded take after the first can will be placed in its own layer by enabling the Record Takes To Layers option in the Record
panel, opened with [Shift]+[Alt]/[Option]+[R], or by using the View menu.
With the Record Takes To Layers option engaged, all subsequent recordings are placed on layers, with one layer per take, and the lay-
ers are shown as soon as recording is stopped. The last recorded take is placed on the Track automatically. If only one take is recorded,
no Layers will be created.
Note that this option also applies when recording Instrument Parts if the Record Takes option is engaged in the Record panel. See Instru-
ment Track Recording Modes for a full description of the Record panel.
By [Right]/[Ctrl]-clicking on a Track, you can choose Add Layer to manually add a Layer at any time. You can then drag Audio Parts or
Instrument Parts to the Layer just as you would drag it to the Track. This allows some very interesting creative comping possibilities bey-
ond simply recording and editing. Note that once an Event has been dragged to a layer, it cannot be moved or copied to another location,
so be sure to retain a copy if you plan to use it elsewhere.
To rename an Event within a layer, [Right]/[Ctrl]-click on it and double-click on the name to enter text (e.g., “great,” “not good,” “brilliant,”
and so on). This is very helpful when organizing takes to be comped. Layers are displayed as lanes directly under the Track to which they
belong.

## Comping

To hide or show layers, click the Expand Layers button on a Track (which looks like this
), or [Right]/[Ctrl]-click on the Track, and then
choose Expand Layers from the pop-up menu.
If no layers are available, the layer controls stay at the bottom of the Track control area. When there is least one layer and the Track con-
trols are zoomed horizontally to a certain level, the layer controls move from the bottom of the track to the top beside the track name.
Layers have their own Track controls, including Solo, Activate, Duplicate, and Remove. Click the layer’s Solo button to solo the layer on
the Track. Clicking the Activate button places that layer on the Track, and the current contents of the Track take the place of that layer on
a new layer located under the Track. Duplicate creates a duplicate of the layer on a new layer. Click Remove to remove the layer from the
Track.
If you would like layers to follow the Track Event in the arrangement—for instance, when moved or duplicated—engage the Layers Fol-
low Events option in the Inspector for the Track.
Switching Between Layers
There are several ways to switch between layers:
-
Click the arrow between the Track name and the layer name in the Track control area, then select the desired layer from the
pop-up menu. After this you can use the 4-way navigation arrows on your keyboard to switch quickly between the layers.
-
With expanded layers, click one of the Activate Layer buttons (The up arrow icon) to make that layer the active layer for the
Track.
-
In the Inspector, click the Layers field and select the desired layer from the pop-up menu.
Takes and Layers Menu
Clicking a layered Event’s [≡] icon opens a menu of Layer and Take options.
-
Select Layer Content lists the Layers that contain any Events in the range of the currently-selected Event. Selecting a Layer
copies these Events from the Layer to the Track.
-
Select Take lists the Takes (loop recording passes) of the Event on the Track. Selecting a Take changes the Event range to that
pass.
In cases where a Take is already present on a Layer, the “duplicate” item is now removed from the takes section.

## Comping

Auditioning Takes
When comping, it is helpful to be able to quickly audition the various takes to determine the desired parts of each take. The Listen tool is
well suited to auditioning takes on layers. When floating the mouse over any layer, click anywhere on any layer to hear it instantly, start-
ing from where you clicked. Alternatively, if you've selected a range on any layer with the Arrow tool, hold [Shift] and click on the selected
range within that layer. This solos the layer and automatically loops the selection for playback. If you hold [Shift] and click on part of the
layer that's not selected, the entire layer will loop, starting at the beginning of the layer.
It is also possible to solo entire layers to quickly switch between takes, as only one layer of a Track may be soloed at a time. To do this,
click on the Solo button on any layer, or select the layer and press [S] on the keyboard. Note that Track Solo is independent of this, so
you can solo the Track or not, depending on whether you would like to hear the performances you are comping in the context of the other
Tracks in your Song.
Copying Layer Ranges to the Track
Studio One makes the comping process very simple. With the Arrow tool selected, floating the mouse over any layer switches to a spe-
cial Range tool, indicated with the Range cursor icon. Click-and-drag with this tool to instantly promote any range of a take to the Track.
Once a range has been copied to the Track, it is highlighted in the Track color so that you can always be sure where material on the
Track is coming from. Where a newly copied range overlaps with an existing range on the Track, an automatic crossfade is applied to
help avoid clicks or other undesirable artifacts. This crossfade can be edited, just like any other, and it can be removed.
Any selected range on a layer can be sized left or right by floating the mouse cursor to the edge of the range and clicking and dragging,
which alters the Track accordingly.
Comping with the Range Tool
You can use the Range tool to select areas and ranges within layers, without automatically promoting the selected layer range to the
main track. This can come in especially handy when using the techniques outlined in Comping Keyboard Navigation. Once you have a
chosen range selected within a layer, you can press the Copy Ranges to Track arrow in the controls for that layer, promoting the selected
range to the main track.
Once you’ve selected your ranges, you can fine-tune the take ranges directly within the Track itself using the Arrow Tool.
Layer Editing
Many of Studio One’s familiar audio editing tools can also be used on Layers, including the Range, Eraser, Paint, Mute, and Bend tools.
Note that the Bend Tool can affect several Layers simultaneously if you used the “Record Takes to Layers” option with a Loop.
Sections of Layers can be deleted using the Range Tool in conjunction with the Eraser tool or the Delete key. Note that you’ll want to use
the Range Tool to select this Range, and not the Arrow tool - selecting with the Arrow tool and deleting will delete a section from your
Comped Audio Event, not your Layer.

## Comping

Layers can be moved horizontally and vertically by holding [CTRL/CMD] while clicking and dragging from the center of the Layer Event,
and can be trimmed by holding [CTRL/CMD] while clicking and dragging from a Layer Event’s borders.
Comping Keyboard Navigation
Given that you can select a range within a layer, it can be very useful to be able to quickly move that selection around within the available
layer content, especially when comping tracks with many takes. You can use the following keyboard commands to quickly move and re-
range your selection within the layers in a track:
-
[Arrow Up/Down] Navigates vertically through the stack of layers.
-
[Arrow Left/Right] Moves the Range tool selection to the previous or following range, as determined by the chosen Event ranges
on the main track.
-
[Shift] + [Arrow Left/Right] Extends the Range selection left or right.
The selection you end up with after extending or contracting an existing Range selection with [Arrow Left/Right] can be moved with the
arrow keys just like the original selection.
Quick-Switching Content on the Main Track
Once you've done some comping, you'll notice that the comped sections in the main track have a menu button at the bottom. Click this
button to open a pop-up menu that lets you choose between all available layers for that section of the main track. You can switch
between takes even more quickly by hovering the mouse pointer over the section of your choice, then pressing and holding [Alt] on the
keyboard as you move the mousewheel or press [G] (for up) or [D] (for down).
Comping With Groups
If one or more Tracks are in a Group, and comping is performed on any of those Tracks, identical edits are performed on the other Tracks
in the Group. For instance, comping can be performed on a single Track within a drum Group, and those identical edits are performed
across the other Tracks in the Group. This applies to soloing, activating, and removing layers, as well.
While it may be best to avoid the scenario, comping can be performed across grouped Tracks with a differing number of layers; layer pos-
itions under the Tracks determine the behavior of the edits.
Layer Naming
By default, layers in a Track are given names in ascending order from top to bottom— Layer 1, Layer 2, and so on. Even if you re-order
layers within the stack, their original names stay the same, to avoid confusion. You can rename a whole layer by double-clicking its
name. You can rename content within a layer by [Right]/[Ctrl]-clicking the content, and double-clicking the name shown in the pop-up
menu. As layer content is added to the main track, you'll see that those Events are named with the track name and layer name, or layer
number, if you have not assigned a custom name.
You can choose to re-name your Tracks and corresponding Channels automatically to that of the active Layer by choosing Enable ‘Lay-
ers Follow Events for New Tracks’ in the Advanced Options menu. Changing the active Layer with this feature enabled will again
change the displayed Track name.
Color-Coding Layers
Much like you can with Audio and Instrument Tracks, you can assign colors to layers within a track. This can be helpful when establishing
a color code for take quality, or simply to give more clarity to which layer is used in a given section of the main track. To set the color for a
layer, click the color picker, next to the layer's solo button, and choose a color from the pop-up selector.
What Next?
After comping on an Audio Track, it is common to consolidate, or bounce, separate Audio Events into a single, continuous Event. You
can do this quickly by selecting the Audio Events on the Track and pressing [Ctrl]+[B] on the keyboard. This renders a new audio file and
Event, and places it on the Track at the correct position.
A more flexible way is to merge the separate Audio Events into an Audio Part by selecting the Audio Events and then pressing [G] on the
keyboard. Any comping performed under the range of the Audio part results in the comps being copied directly into the Audio part.

## Transient Detection and Editing

Transient Detection is the process of determining the location of transients within audio material, which can then be used as the basis for
editing. A transient can be defined as a short-duration signal that represents a non-harmonic attack phase of a musical sound or spoken
word. It contains a high degree of non-periodic components and a higher magnitude of high frequencies than the harmonic content of

## Transient Detection and Editing

that sound. When looking at the waveform of a recorded snare drum hit, the first part of the hit—the attack—looks distinctly louder than
the rest of the signal; the “louder” part is the transient, and the rest of the signal is commonly called the “tail.”
Transients usually indicate rhythm in musical material, so that when the positions of transients are known, it becomes possible to quant-
ize, or correct the timing of, recorded audio. For instance, if a drummer was early on the downbeat after a killer fill, you could fix it so that it
is perfectly in time. In fact, it is possible to alter the entire feel of a performance and even extract the feel of one recorded performance
and apply it to another.
Detect Transients
To detect transients in any audio in an arrangement, select an Audio Event and open the Bend panel from the top toolbar, then choose
Analyze from the Detection area. Alternatively, [Right]/[Ctrl]-click on an Audio Event and choose Detect Transients from the Audio/Audio
Bend contextual menu. You can also open the Bend panel by clicking Audio Bend in the View/Additional Views menu.
The original audio clip that the Event uses is then analyzed, as indicated in the lower left of the Event with a “percentage complete” dis-
play. After detection, the Event becomes slightly translucent, and blue Bend Markers—vertical lines the height of the Event—are placed
at every transient.
Two modes can be used for transient detection: Standard and Sensitive. These modes are accessed in the Bend panel.
If you intend to quantize or slice the Audio Event, you don’t need to detect transients first; you can go straight to the Action area of the
Audio Bend panel. Any applied action detects transients.
Tab to Transient
It is possible to tab to transients in both the Arrange view and Audio Editor by pressing [Tab] on the keyboard, even if transients have not
yet been detected for the Event. This moves the playback cursor to the next transient in the Event. The following keyboard shortcuts are
also available when working with Tab to Transient:
-
[Ctrl/Cmd] + [Backspace] Moves the cursor to the previous transient.
-
[Shift] + [Tab] Creates or expands a range selection between transients.
-
[Shift] + [Ctrl/Cmd] + [Backspace] Shortens the range selection.
Bend Markers
Bend Markers are used in Studio One to stretch audio inside an Audio Event, without the need for slicing the Event into multiple pieces.
They are added to an Audio Event when detecting transients from the Bend Panel, and can also be manually added. When detecting tran-
sients, the default Threshold used to place Bend Markers at transients is 80%, which can be adjusted at the top of the Event contextual
menu or in the Inspector, so that Bend Markers are placed only at the transients with which you want to work. It is also possible to manu-
ally insert Bend Markers, before or after detecting transients.

## Transient Detection and Editing

While it is possible to insert and edit Bend Markers with Bend Markers hidden, you may want them to be shown while editing. Check the
Show Bend Markers box in the Bend panel or Event contextual menu to show or hide Bend Markers.
If Bend Markers have been inserted as the result of transient detection, a very short, highlighted range—visible if zoomed in far enough—
precedes the Bend Marker. This range represents the distance between the onset and the peak of the transient, and it is important when
Studio One quantizes audio based on Bend Markers. When cutting, the onset of the transient is used, so as to encompass the whole tran-
sient. When quantizing or snapping a Bend Marker, the peaks of the transient are referenced, for better rhythmic accuracy.
Note that Bend Markers are properties of the audio clip that an Event references, meaning that multiple Events referencing the same
audio clip in the Pool (for example, a drum loop duplicated several times) share the same Bend Markers, and are effected by any Bend
Marker editing. If you want to process duplicated Events differently, for instance to provide rhythmic variation with a duplicated drum
loop, then bounce the Event to a new file prior to editing.
Editing Bend Markers
To manually insert Bend Markers, switch to the Bend tool, then float the mouse over any Audio Event and click where you would like to
insert the Bend Marker. Double-click on any Bend Marker with the Bend tool to remove it; any effect the Marker had on the audio is
undone.
With the Bend tool selected, click-and-drag on any Bend Marker to manually manipulate the audio left or right on the timeline. Doing so
stretches or compresses the audio surrounding the Bend Marker, and the Bend Marker displays a left- or right-facing flag at the bottom,
indicating the direction in which it has been moved. If the audio is stretched, the waveform is colored red, with the intensity of the color
increasing the more the audio is stretched. If the audio is compressed, the waveform is colored green.
Like many other editing operations, when moving a Bend marker with Snap enabled, the marker snaps to the nearest interval dictated by
the current Snap setting. Hold [Shift] while moving a marker to temporarily disable Snap for finer control, or to enable snapping if it's cur-
rently disabled.
If you wish to relocate a Bend marker (without timestretching the surrounding audio), hold [Alt] and click-and-drag the Bend marker to the
desired position.
Note that for audio to be stretched or compressed by manipulating a Bend Marker, at least one other Bend Marker should exist to the left
or right of the one being manipulated, to be used as the basis for stretching or compressing. If no other Bend Marker exists, the beginning
and end of the audio clip for the Event are used. For instance, if you want to change the rhythmic phrasing of a word in a vocal part, add a
Bend Marker to the left and right of the word you want to alter before attempting to move the word itself.
Multiple Bend Markers can be selected for simultaneous editing with the Bend tool by holding [Shift] and clicking on the desired markers,
or selecting a group of markers while holding [Alt].
You can reset a Bend Marker to its original position by [Right]/[Ctrl]-clicking on it and selecting Reset Bend Marker. Multiple selected
Bend Markers can be reset at once, making it possible to easily restore the original timing if editing produced undesirable results.
Use The Bend Panel
When working with Bend Markers, you may find it useful to have the Bend panel displayed, as this is where the most common Bend
Marker-related actions are found. To open the Bend panel, click on the Bend Panel button in the toolbar or select Bend from the View/Ad-
ditional Views menu. The Bend panel can also be detached and freely placed onscreen.
In the Detection section, you can change the transient-detection mode, which is set to Standard by default. If this mode does not accur-
ately locate transients to your liking, switch the mode to Sensitive and analyze the audio again.

## Transient Detection and Editing

In the Bend Marker section, you can remove all Bend Markers or Restore all Bend Markers in the selected Event by clicking on the
respective buttons. You can also adjust the Bend Marker Threshold, using the slider.
In the Track section, you can set the Timestretch mode for the Track on which the selected Event resides and can select Guide Tracks if
that Track is in a Group.
Quantizing vs. Slicing
In the Action section, Quantize is selected by default, and a Strength percentage slider is displayed. Click on Apply to quantize any selec-
ted Event. The Strength setting alters the Start percentage in the Quantize panel, providing a simple way to alter the strength of the quant-
ize process.
Alternatively, you can choose the Slice action, which slices the selected Event into multiple Events, using the Bend Markers as a basis.
This brings differing results, depending on the selected options:
-
Check Autofades if you want the resulting individual slices to each have a short fade-out in order to avoid audible clicking.
-
Check Autofill to fill the spaces between sliced Events that are moved apart with realistic-sounding "tails," emulating the natural
decay between notes. This helps to keep things sounding fluid and avoid a "choppy" sound. Enabling this option also silences
the overlapping ends of Events.
-
Check Merge if you would like the individual slices to be merged into an Audio Part after processing.
-
Check Quantize if you would like to quantize the resulting individual Events, and set the Strength using the percentage field.
Note that in this process, no timestretching occurs; instead, a single continuous Event is sliced at its detected transients, and the
resulting multiple Events themselves are quantized across the timeline.
As with the Strip Silence panel, when the small light indicator next to the [Apply] button is lit, this means that changing certain Detection,
Bend Marker, Track, or Action options and then clicking Apply automatically undoes the previous operation, making it easier to find the
right settings by viewing the result of the Bend Panel process, then tweaking the settings if needed without having to undo manually.  Any
change in selection (or other editing operations) ends this automatic state, and the indicator is not lit.
Quantize Audio
It is very simple to quantize audio in Studio One. Select the Audio Event, then press [Q] on the keyboard to quantize. Transients are
detected for the selected Event, the audio instantly snaps to the current quantize grid, the Bend Markers indicate they have been moved
left or right, and the waveforms are appropriately colored as described in the Editing Bend Markers section.
The same quantize commands are available for transient-detected audio as for Instrument Parts. [Q] quantizes the selected Events, [Alt]/
[Option]+[Q] quantizes at 50% strength, and [Shift]+[Q] restores the original timing.
Note that the Quantize panel for the Audio Editor is independent from the Note Editor and the Arrangement. This enables you to perfect
the rhythmic character of each aspect of the Song and perform those edits quickly without having to adjust the settings each time. You
can show or hide the Quantize panel for the Audio Editor by clicking its Quantize panel button. You can also close the Quantize panel for
the currently selected view by navigating to View/Additional Views/Quantize.
Elastique Pro
Studio One uses the Elastique Pro time-stretching engine from Zplane, for high-quality time-stretching. When quantizing an Audio Event,
Elastique Pro is used to stretch each region of audio between the Bend Markers.
Phase-Coherent Multitrack Quantization
When multiple microphones are used to record the same instrument onto multiple Tracks, as with as a drum set, it is very important that
the phase relationships across the multitrack audio remain unaltered. You can think of phase relationships as the time it takes sound to
reach each microphone from the source, such as a snare drum. How the waveforms align across each Track is critically important to the
sound achieved; if a snare hit is moved in time on one Track and not the others, the resulting collective sound of the snare hit can be
drastically altered.
Therefore, when quantizing or slicing multitrack audio, it is important that all edits are performed across every Track in a way that pre-
serves the phase relationships. This is referred to as phase-coherent editing. In Studio One, all that is required to ensure this happens is
for the Tracks to be grouped. Once the Tracks are grouped, Studio One takes care of phase coherence for you.

## Transient Detection and Editing

For instance, let us consider a scenario with four Tracks of drums: kick, snare, and left and right overheads. Prior to editing on any Track
individually, you would Group the Tracks by selecting them and pressing [Ctrl]/[Cmd]+[G] on the keyboard. If you then quantize audio on
any Track in the Group, Studio One determines the phase relationships between the Tracks and then quantizes or slices the audio
across all Tracks based on transients on the individual Tracks. For instance, where there is a snare hit, the first transient found (within the
range of the snare hit) in the Tracks from top to bottom is used as the basis for quantization for all four Tracks; the other Tracks simply
maintain their existing phase relationships to the quantized Track, and thus are quantized in a phase-coherent manner.
In the above scenario, you can check exactly what Studio One has done by zooming in on any Bend Marker. You can see that the Bend
Marker Range on each Track has been adjusted to a common start time, with the Bend Marker used as the basis for quantization.
Manual Bend Marker edits on grouped Tracks performs the same process.
It is also possible to exclude any Tracks in a Group from transient analysis and therefore not use them as a reference in the quantizing or
slicing process. When Events are selected that are contained on a Track in a Group, a Group selection box appears in the Track area of
the Bend panel, along with a Guides-selection drop-down menu that contains all Tracks in the Group. To exclude Tracks from analysis,
simply uncheck them. As an example, you may only want to use the kick and snare Tracks as the basis for quantization or slicing of the
Group, in which case you would uncheck all Tracks except the kick and snare and then apply the desired action from the Bend panel.
Groove Extraction and Quantize
Groove Extraction is an extremely powerful, yet simple, feature. Let us consider the scenario in which you want a poorly played bass part
to closely follow the kick drum. To make this happen, open the Quantize panel and switch to Groove mode. Next, drag the kick drum
Event into the Groove panel, and then quantize the bass Event. In those few moves you have effectively detected all necessary tran-
sients, extracted the kick drum groove, and quantized the bass to that groove.
Similarly, you could drag an Instrument Part into the Groove panel to extract the groove and then quantize audio to that groove. When
you extract the groove from an Audio Event or Instrument Part, the grid in the arrangement is then based on that groove, and anything in
the arrangement can be quantized to that grid.
This is extremely useful for cleaning up multi-instrument performances, and it’s equally useful for creative purposes, such as extracting a
great groove from a funk loop and applying it to a straight-eighth drum loop.
You can also drag the groove itself to an Instrument Track, which renders the groove as a series of notes, one for each hit in the groove,
even tweaking note velocity according to the relative level of the hits. This allows you to instantly build a virtual instrument bass part, for
instance, that exactly match a drum performance.  Just drag the drum performance into the Groove area, then drag it out to the bass
Track, and change the notes to the pattern you want.
Or, you might prefer to drag in an audio Event, drag it to an Instrument Track to tweak the groove musically, then drag that Instrument
Part in, and quantize the original audio Event to that. The possibilities are endless!

## Track Transform

Audio Track Transform
Audio Tracks always have a directly related Channel in the Console on which Insert effects can be configured. In the editing and arran-
ging process, it is sometimes necessary to render an Audio Track so that the Insert effects and automation moves become a part of the
audio waveform on the Track. You might do this for creative purposes or simply to enable you to remove the Insert effects in order to
save CPU power.
Studio One makes this incredibly simple with the Track Transform feature. With any Audio Track that has effects inserted on its cor-
responding Channel selected, [Right]/[Ctrl]-click on the Track and select Transform to Rendered Audio from the contextual menu.

## Track Transform

Check Preserve Realtime State if you would like to be able to transform back to the original Track. It is then possible to switch between
Automatic Tail Detection, with a Max Length property, and a fixed tail of a given length by toggling the Auto Tail option. Auto Tail is useful
if there is a reverb or other effect that you want to render beyond the Event length on the Track. Note that Auto Tail may not work well with
lengthy delays or extremely long reverbs, as it works by detecting a range of silence at which to cut off and fade out the transformed
audio. In that case, setting a fixed tail is the best option.
Click OK, and the Audio Track is bounced with its Insert effects and mix automation applied; then the original Audio Track is replaced
with the newly bounced audio on a new Audio Track with the same name. If Auto Tail was engaged, or a Tail amount was specified, fade-
outs are applied automatically across the specified Tail duration for each Event. The Insert effects are not inserted on the new Track, as
they have been rendered into the audio on the Track.
If you check Preserve Original Track State, it is possible to transform back to the original Track, with effects inserted on the cor-
responding Channel, by [Right]/[Option]-clicking on the Track and selecting Transform to Realtime Audio from the contextual menu.
The effects of Volume and Pan settings (including automation) are applied to the Track as it is bounced to audio, so the value of those set-
tings and their automation data is set to its defaults in the resulting bounced Track. If you wish to edit those parameters later, be sure to
check the Preserve Realtime State option when Transforming the Track. This allows you to revert the Track back to its original state, with
original settings and automation data intact. Note that send levels, bus assignments, and other mix parameters retain their settings as
normal after Transforming a Track.
Every Track Transform operation creates bounced audio files that are placed into the Pool for the current Song. These files remain in the
Pool (for later access or reference) until you decide to clear them out. As mentioned in the Pool Commands section, you can delete a
file from the Pool view in the Browser by [Right]/[Ctrl]-clicking the file and choosing Remove From Pool (which removes the file from the
Pool but retains it on disk) or Delete File Permanently (which removes the file from the Pool and deletes it from disk). You can also auto-
matically remove all unused copies of files from the Pool by [Right]/[Ctrl]-clicking in the Pool and choosing Remove Unused Files.
Note that it is possible to Transform multiple Audio Tracks at once, in which case they are all rendered simultaneously, which can be a
huge time saver.
Instrument Track Transform
Instrument Tracks contain MIDI music performances that control virtual instruments. The virtual instruments output to one or more Audio
Channels in the Console, and you can configure Inserts, Sends, and Output routings for the Channels. With this approach, it can be dif-
ficult to render Instrument Tracks to audio correctly.
Studio One makes it simple by transforming Instrument Tracks into Audio Tracks in one step. [Right]/[Ctrl]-click on any Instrument Track
and select Transform to Audio Track from the contextual menu. You can then see several options in the pop-up menu:
-
Render All Channels If the connected Instrument has more than one audio output engaged, this option appears. If this option is
disengaged, only the Channel related to the selected Track is rendered, as specified in the Track Inspector.
-
Render Inserts If you would like to render the Insert effects (as well as Volume and Pan settings and automation) on the related
virtual instrument’s Output Channel, check this option.
-
Preserve Instrument Track State If you would like to be able to transform from the new Audio Track back to the original Instru-
ment Track, check this option.

## Track Transform

-
Remove Instrument If you would like to remove the virtual instrument in order to save CPU power after rendering audio and cre-
ating the new Audio Track, check this option.
-
Auto Tail Choose between automatic tail detection and a fixed tail of a given length, as described in Audio Track Transform.
Click OK, and all of the parts on the Instrument Track are rendered to audio and placed on a new Audio Track.
If a Tail amount was specified, fade-outs are applied automatically across the specified Tail duration for each Event. Also, the send con-
figuration and output routing of the new Audio Track is identical to the original Instrument Track.
As with Audio Tracks, it is possible to Transform multiple selected Instrument Tracks at once, in which case they are all rendered sim-
ultaneously, which can be a huge time saver.
Every Track Transform operation creates bounced audio files that are placed into the Pool for the current Song. These files remain in the
Pool (for later access or reference) until you decide to clear them out. As mentioned in the Pool Commands section, you can delete a
file from the Pool view in the Browser by [Right]/[Ctrl]-clicking the file and choosing Remove From Pool (which removes the file from the
Pool but retains it on disk) or Delete File Permanently (which removes the file from the Pool and deletes it from disk). You can also auto-
matically remove all unused copies of files from the Pool by [Right]/[Ctrl]-clicking in the Pool and choosing Remove Unused Files.
External Instrument Track Transform
The Instrument Track Transform command is also suitable for use with external hardware instruments—though due to the real-world
nature of physical hardware, of course, the audio must be rendered in real-time. Choosing this will render the external instrument’s per-
formance to a new Audio track while creating an associated channel in the Console.
External Instrument Track Transforms are non-destructive. After a Track Transform, removing an external instrument will also remove its
associated Aux channel from the Console. Restoring the instrument will also restore its Aux channel.
As with virtual instrument Track Transform, simply right-click on the Track header and select Transform to Audio Track from the con-
textual menu to execute the transformation. Later, you can select Transform to Instrument track from the same menu to restore the MIDI
performance data—it never really left!

## Track Transform

Quick-Convert Instrument Parts to Audio
When working with a virtual instrument, you can drag Instrument Parts directly from the related Instrument Track onto any Audio Track in
your song. The Instrument Part is rendered to audio, and placed in the location you've chosen.
Track and Event Inspectors
The Track Inspector and Event Inspector views offer you fast access to a variety of important per-Track and per-Event parameters and
functions. To show or hide the Inspectors, press [F4] on the keyboard, or the "i" button, located above the Arrange view. Once the
Inspectors are visible, clicking on a Track or Event brings that element into focus in the appropriate Inspector. You'll see differing sets of
controls, depending on if the Track or Event is audio-based or instrument-oriented.
There's also an Inspector for the Marker Track, which is described here.
Track and Event Inspectors

Track and Event Inspectors

Track Inspector
Track and Event Inspectors

Click on your audio Track of choice to give access to the following parameters in
the Track Inspector:
-
Tempo (Mode) Lets you choose how playback of the current Track
relates to Song tempo. For more details, see the Automatic
Timestretching section.
-
Timestretch (Mode) Lets you choose the optimal timestretching
algorithm for the Track. For more details, see the Timestretching Mater-
ial Modes section.
-
Group Lets you assign the current Track to an existing Track Group. For
more information, see the Groups section.
-
Layers Lets you Add, Duplicate, Rename, or Remove a layer from the
Track, as well as set which layer is currently chosen for playback. For
more information, see the Track Layers section.
-
Layers Follow Events Enable this parameter to make audio on under-
lying layers follow the related Event above when you move it along the
timeline. When this parameter is disabled, moving an Event with one or
more Layers beneath it detaches that Event from the layers below, mak-
ing it a permanent part of the primary Layer.
-
Play Overlaps Enable this option to allow any overlapping audio on the
current Track to play back simultaneously, rather than cutting off at the
beginning of the next Event.
-
Delay Lets you apply a positive or negative time delay to the current
Track, to help align it with other elements. Range of -1000 to 1000 ms.
-
Follow Chords Use this menu to specify the Follow Chords mode for
the Track. This defines how the Track interacts with the Chord Track.
-
Tune Mode This setting applies to audio tracks only. With it you can
choose the algorithm that best suits the audio material. It is described in
the Tune Modes section.
-
Automation Lets you choose the Automation mode for each of the auto-
mated parameters associated with the Track, as well as quickly view and
enable or disable the automation for a given parameter. For more inform-
ation, see the Automation Modes section.
-
Edit Note Click the pencil-and-paper icon to open the Track Notes win-
dow.
-
Routing and Mix Controls This area is a duplicate of the parameters
you see when viewing a Channel in the Console. Input and Output rout-
ing, Track Volume, Pan, status, effects Inserts and Sends are all avail-
able. For more information, see The Console.
Click on the Instrument Track of your choice to access the following parameters in
the Track Inspector:
-
Timebase Lets you set the Timebase format for the current Track, in
Beats or Seconds. Set to Beats, the Events on the Track change their
position in time and speed to follow tempo changes in the Song. Set to
Seconds, Events stay in place and maintain their playback speed until
you change them intentionally. This can be useful, for example, in film
audio, in which certain sounds must remain at certain absolute positions
in time, to maintain synchronization with the visuals.
-
Group Lets you assign the current Track to a existing Track Group. For
more information, see the Groups section.
-
Layers Lets you Add, Duplicate, Rename, or Remove a layer from the
Track, as well as set which layer is currently chosen for playback. For
more information, see the Track Layers section.
-
Delay Lets you apply a positive or negative time delay to the current
Track to help align it in time. Range of -1000 to 1000 ms.
-
Transpose Lets you change the pitch of all notes on the current Track, in
a range between -64 and +64 semitones.
Track and Event Inspectors

-
Velocity Lets you boost or attenuate incoming note Velocity, before it
arrives at the current instrument or external MIDI device. Settings
between -100% and -1% attenuate velocity. Settings between 1% and
100% boost velocity. At 0%, velocity is unchanged.
-
Layers Follow Events Enable this parameter to make instrument data
on underlying layers follow the related Event above when you move it
along the timeline. When this parameter is disabled, moving an Event
with one or more Layers beneath it detaches that Event from the layers
below, making it a permanent part of the primary Layer.
-
Retrospective Recording When this button is lit, that means MIDI data
was captured on the current Track while you weren't recording (i.e., dur-
ing playback or with the Transport stopped). Click the button to place that
data onto the Track. For more information, see the Retrospective Record-
ing section.
-
Automation Lets you choose the Automation mode for each of the auto-
mated parameters associated with the Track, as well as quickly view and
enable or disable the automation for a given parameter. For more inform-
ation, see the Automation Modes section.
-
Program Lets you select a MIDI program number (and in some cases, a
bank number) to associate with the current Instrument Track. This pro-
gram change value is transmitted to the instrument, ensuring that the cor-
rect preset is loaded when you open a Song.
-
Note FX Lets you choose and apply real-time Note FX processing to the
note data of the current Track. For more information, see Note FX.
-
Routing and Mix Controls This area is a miniature duplicate of the para-
meters you see when viewing a Track in the Mix view. All Instrument
Tracks display input and output routing options and Mute/So-
lo/Record/Monitor status toggles. If the Track is hosting a virtual instru-
ment, Track Volume, Pan, effects Inserts and Sends are displayed. For
more information, see The Console.
Event Inspector
Click on the Audio Event of your choice to access the following parameters in the Event Inspector.
Track and Event Inspectors

-
Event FX This lets you assign effects to
individual Audio Events, rather than to a
Track as a whole. For more information,
see the Event Effects section.
-
Start and End Lets you specify the
start and end times for the current
Event.
-
File Tempo If you know the tempo of
the audio file associated with the cur-
rent Event, you can specify it here. This
gives Studio One a tempo reference to
work from when timestretching an
Event to match Song Tempo. Studio
One can also try to deduce the tempo of
a file if the BPM is not known—more
info on that below.
-
Speedup Lets you speed up or slow
down the tempo of the current Event,
independent of other tempo settings.
For more information, see the Manual
Timestretching section.
-
Transpose Lets you shift the pitch of
the current Event up or down, in a
range of -24 to +24 semitones.
-
Tune Lets you fine-tune the pitch of the
current Event up or down, in a range of
-100 to +100 cents.
-
Normalize Lets you boost the volume
of the current Event, so that the highest
peak in the audio reaches 0 dBFS. You
can also Normalize an Event by select-
ing the Event and pressing [Alt-N] /
[Cmd-N].
-
Gain Lets you adjust the overall level of
the current Event, in a range of -40 to
+24 dB.
-
Fade-In Lets you specify the length of
the fade at the beginning of the current
Event. At a setting of 0 ms, no fade is
applied.
-
Fade-Out Lets you specify the length of
the fade at the end of the current Event.
At a setting of 0 ms, no fade is applied.
-
Bend Marker Engage this to view the
Bend Markers for the selected Audio
Event.
-
Threshold This field is only active
when Bend Markers are visible. Use it
to adjust the threshold for placing Bend
Markers in the Audio Event. The range
is 0-100%, with a default value of 80%.
-
Gain Envelope Two options are
provided: the Bypass button disables
the Gain Envelope without resetting it,
and the check box lets you show or hide
the Gain Envelope.
-
Time Lock Select this option to keep
the Event from being moved to a dif-
ferent time position within the Track.
Track and Event Inspectors

See Lock Tracks or Events for more
information.
-
Edit Lock Select this option to prevent
the contents of the Event from being
altered in any way. See Lock Tracks or
Events for more information.
Click on the Instrument Part of your choice to access the following parameters in the Event Inspector:
-
Start and End Lets you specify the start and end times for the current Event.
-
Transpose Lets you shift the note pitch of the current Event up or down, in a range of -24 to +24 semitones
-
Velocity Lets you scale the effect of note Velocity, before it arrives at the current instrument or External MIDI device. At 0%, all
notes play at full velocity. At 100%, the full range of note velocity is sent.
-
Time Lock Select this option to keep the Event from being moved to a different time position within the Track. See Lock Tracks
or Events for more information.
-
Edit Lock Select this option to prevent the contents of the Event from being altered in any way. See Lock Tracks or Events for
more information.
File Tempo Approval on Import
If you don’t know the tempo of the audio file
associated with the current Event, Studio
One will attempt to deduce it, and it will do
so based upon BPM data in the filename of
the imported Event. In this example, “Syn-
thBass_120BPM.wav” was imported with a
probationary BPM of 120—listed in red in
the inspector. If this tempo is correct, it can
be approved by the user from the drop-
down menu to the right of the file’s tempo.
From this drop-down menu, you can also
double or halve the event’s tempo.
If the BPM is not contained in the Event’s
header or filename, Studio One will instead
attempt to deduce the tempo of the Event
based on both the file’s length and an
assumption of an evenly-subdividable num-
ber of bars. Tempo Approval on Import is
not available on Events that contain more
than one tempo.
Event Effects
It is possible to insert effects directly on an Audio Event in the arrangement, as opposed to inserting effects on the entire Audio Channel
for the related Track, thereby affecting all Events on the Track. Event Effects are commonly used to add variety to the arrangement or to
insert utility effects, such as pitch correction, into specific Events.
Track and Event Inspectors

Insert Event Effects
To insert an effect on an Event, select the Event and open the Inspector by pressing [F4] on the keyboard. In the Event Inspector area of
the Inspector, you can see an Event FX tab with an [Enable] button. Click on Enable, and an Insert Device Rack opens.
Insert effects or FX Chains here, as you normally would, and the Event is processed accordingly, in real time, during playback. The res-
ulting sound is exactly as if you had inserted the effect on the Track: You can hear all other Tracks play and can make effects parameter
changes while hearing the results in context with the rest of the mix.
You can also add Event Effects by right-clicking an Event and choosing Event FX >> Add Effect… from the contextual menu, where you
will also find a list of the Effects currently applied to the selected Event.
As Event Effects may alter the relative volume of an Event, thereby skewing existing volume fade envelopes, an option has been
provided to process volume envelopes after Event Effects. Click on the Tail check box, in the area above the Insert Device Rack, to
enable this option.
Add Effects to Multiple Events
You can add Effects by dragging them from the Browser onto all selected Events, or by group-selecting several Events and assigning
Event FX via the right-click contextual menu described above.
Render Event Effects
Once the intended sound is achieved via an Event Effect, it is likely a good idea to render the audio in order to conserve CPU resources.
Studio One provides a very flexible way to do this that allows you to revert to real-time processing at any time in order to make changes.
To render any Audio Event with inserted Event Effects, click on Render above the Event FX Insert Device Rack. The Insert Device Rack
collapses, a new Audio Event with the rendered audio replaces the original Event in the arrangement, and the [Render] button is labeled
[Restore]. At any time, click on Restore to replace the rendered Event with the original and restore any inserted effects to their pre-
rendered states.
When rendering Event FX, note that the Tail setting above the Insert Device Rack allows you to specify a length to render beyond the end
of the Audio Event. This is critical to properly capturing reverb tails, delay lines, and other similar audio tails caused by inserted effects.
When a Tail value is given, a volume fade is applied across the entire length of that tail on the rendered Event after rendering to ensure
smooth-sounding results. This fade envelope can then be modified, as usual.
Rendering Event FX creates bounced audio files that are placed into the Pool for the current Song.
Using ARA Effects
Drag and Drop an ARA Effect from the Event Editor folder onto an Event to apply it as an Event FX. Hold [Alt/Opt] while dragging and
dropping to instead apply it as an Insert Effect to the whole Channel. Note that adding a second ARA (Audio Random Access) Effect (like
Track and Event Inspectors

Melodyne or VocAlign) to an Event will replace the previous Effect with the second. ARA Effects are highlighted in blue in theEvent FX
section of the inspector.
Track Presets
Track Presets allow you to save and recall frequently-used Track and Channel configurations so you don’t need to re-create their inputs,
settings, and routing every time you create a new Track for the same purpose.
For example, let’s say you prefer to process and route your background vocal tracks with a particular reverb; a certain set of inputs; and
you want all of these background vocal tracks to follow the Chord Track and utiilze the “Lead” Tune Mode and be placed in a Folder Track
along with a Bus called “BGV.”
Thanks to Track Presets, you only need to set all of that up once — and you can store and recall the “Background Vocal” configuration for
use in future Songs.
To store a Track Preset, right-click on the track header and choose "Store Track Preset" from the contextual menu. When running a
Store Track Preset operation, you can also file your Track Presets within subfolders. Alternatively, you can drag a Track or Folder Track
from its Track Header and drop it in the Browser to quickly store a Preset.
To load a Track Preset, right-click on the track header and choose Load Track Preset from the contextual menu. Alternatively, you can
also apply a Track Preset to a Channel by right-clicking the Channel and choosing Apply Track Preset.
Alternatively, Track Presets can be applied from the Browser via Drag and Drop. By default, Track Presets are stored in Studio One/Pre-
sets/User Presets/Track Presets.
If you’d like to drag and drop multiple Track Presets at once, simply press [Ctrl]/[Cmd]+click onto the presets you’d like from the Browser
and drag the selected presets into the arrangement.
Track Presets can be used to store and recall all aspects of a Track: names, instruments, routing, pan, levels, and any variables that can
be set in the Inspector.
Note that Track Presets do not store Note Events, Audio Clips, Event FX, or Automation.
Track Presets also work with folder tracks, meaning an entire group of Tracks, including their Bus and FX Channels, can be saved as
a single Track Preset! Very useful for multi-channel drums.
Loading multiple Track Presets that contain identical FX Channels will create a single instance of the FX Channel to be shared. This fea-
ture helps you avoid creating redundant FX Channels.
Edit View Event Editing
In many cases, editing actions require a close look at the Events being edited. To perform these edits in the Arrange view would require
zooming in to a level that would make it difficult to retain your sense of the overall Song structure, then zooming back out after the edits
are performed. Edit views allow you to avoid this inefficiency. To open the Edit view for the selected Event, click on the [Edit] button,
Track Presets

press [F2] on the keyboard, or double-click on any Event. You can also open the Editor by selecting Editor from the View menu. While
there is a common Edit view, Audio Events open in the Audio Editor, and Instrument Parts open in the Note Editor.
The Edit view displays the currently selected Event on a timeline that is independent of the Arrange view timeline. By default, the Edit
view timeline is zoomed in further than the default Arrange view timeline. While the Edit view is open, [Alt]/[Option] + double-click an
Event in the Arrange view to zoom the Editor so it contains the full Event. Note that the [Synchronize Editor to Arrangement] button must
be disengaged to use this command.
The Editor can be detached to its own sizable window by clicking on the Detach button at the upper right of the Editor. The window can
then be pinned to the new location by clicking the Pin icon in the upper right corner of the window. This allows you to view the same or dif-
ferent contents in multiple edit windows side-by-side. Any Track can then be selected from the Track drop-down selector to the upper left
of the Editor window, under the toolbar.
The [Action] button (available in both the Audio and Note Editors) gives you quick access to functions you might normally access by
[Right]/[Ctrl]-clicking on an Event and exploring the Audio or Musical Functions sub-menus.
Audio Editor
The Audio Editor display operates independently of the Arrange view and has an independent Timebase setting. Most options that
appear in the Editor are the same as in the Arrange view and affect tools and Events in the same way. Note that the Snap and Timebase
settings are not shared between the Arrange view and Editor; they remain independent. A Snap to Event Hotspots option is found in the
Editor Snap dropdown menu; it allows tool and Event snapping to hotspots such as Bend Markers. The dropdown menu also includes a
Snap to Zero Crossings option, which will help avoid an unnatural click at the beginning of the audio data when the Event is moved or
split.
The displayed level scale to the left of the waveform lane in the Audio Editor can be adjusted by clicking on it and dragging left or right.
This effectively zooms the waveform amplitude, which may be useful when editing audio with relatively low levels. [Right]/[Ctrl]-clicking in
this area allows the selection of a percentage- or dB-based scale. You can also adjust this zoom level by manipulating the Data Zoom
parameter, found to the right of the Time Zoom slider control.
Tools
Most of the tools in the Arrange view are available in the Audio Editor and function there exactly as they do in the Arrange view. (Only the
Paint tool is not available in the Audio Editor.)
Note Editor
Instrument Parts contain notes, which represent musical performance data and are a type of Event. Notes can be moved, cut, copied,
pasted, duplicated, and drawn using mouse tools, key commands, and certain Event menu commands. Multiple notes can be selected
and edited together, as with other Events.
For quick editing of all notes in a Part or on the Track, use [Ctrl]/[Cmd]+[A] to select all of the notes in the focused Part in the Note Editor,
or [Ctrl]/[Cmd]+[Shift]+[A] to select all notes in all Parts on the Track. You can also access the full set of selection actions by navigating to
the Select section of the Edit menu.
The View buttons on the left side of the Note Editor toolbar provide two three different ways of viewing, entering, and editing note
data: Piano view and Drum view.Piano view, Drum view, and Score view.
Edit View Event Editing

-
Piano View displays the note data in "piano roll" style. A vertical keyboard graphic helps visualize notes and scales, and can be
used to trigger the notes.
-
Drum View removes the vertical keyboard and allows more room to display sample names horizontally for each vertical note
position.
-
Score View shows the note data on a musical staff, where you can add musical symbols for dynamics and articulations that also
enhance playback.
We'll describe the following features as they apply to the Piano and Drum views. For details about Score view, see the Score Editor
chapter.
Zoom and Synchronize
You can zoom in or out horizontally in the Piano and Drum views by moving the Time Zoom control, and zoom vertically with the Data
Zoom control. In Score view the Time Zoom control zooms both vertically and horizontally, as does a scroll wheel.
The horizontal zoom and timeline of the Note Editor and Arrange View can be linked. To do this, engage the [Synchronize Editor to
Arrangement] button on the right side of the Note Editor toolbar.
Timebase, Quantize, and Scale
The Note Editor has independent settings similar to those in the Audio Editor. While Quantize affects the horizontal time-value snapping,
the Note Editor also features Scale (vertical note-value) snapping. The Scale settings allow snapping to specific note values within dif-
ferent musical scales.
The Scale function must be enabled in Piano view. First click its toggle switch, then select a scale by choosing the starting note and the
musical scale in the respective selectors. The notes contained in the selected scale are marked on the Note Editor's keyboard display, as
well as in the single-octave keyboard display above the Scale selector.
The Editor background will be highlighted to reflect the notes of the currently-selected scale.
If you want existing notes to conform to a scale you have just selected, first select the notes, then select Apply Scale from the Action
menu in the Note Editor toolbar. This can be done in Piano view or Drum view, and the change is applied instantly in Score view.
Arrow Tools
Studio One offers two Arrow tools for editing Note Events: Extended and Basic. Choose the one you’d like to use by clicking on the Arrow
tool icon, or by pressing [1] with the Note Editor open to toggle between the two.
The Extended Arrow tool in the Note Editor is used with notes in essentially the same way as the Arrow tool in the Arrange view is used
with Events. Multiple notes can be selected and edited together in the same way as Events.
At high zoom factors, The Extended Arrow tool leverages context-sensitive functionality to enact different tasks, depending on which
area of a Note Event you move your cursor over. This allows you to perform various critical tasks without the need to switch tools:
-
Edit Velocity: Click and Drag vertically from the upper area of a Note Event to raise and lower Velocity
-
Mute: [Alt/Option+Click] in the upper area of a Note Event to Mute
-
Cut: Click at the lower area of the Note Event to split it
-
Cut Deep: [Alt/Option+Click] at the lower area of a stack of Note Events in the same location (of the same pitch) to split them all
-
Glue: Click at the lower area between two adjacent Note Events with the same pitch to group them
The Basic Arrow tool can be used to move Note Events or trim them by clicking and dragging their endpoints, disabling the above-listed
features of the Extended Arrow Tool.
Edit View Event Editing

Moving Notes
To move a note using the Arrow tool, click anywhere on the note and drag left, right, up, or down. Dragging the note left or right moves it
backward and forward in time, relative to the current Edit view timebase and timeline zoom. Dragging the note up or down transposes
(changes the pitch of) the note. In Piano view the transposition interval can be determined by using the vertical keyboard display to the
left of the Note Editor.
Creating Notes
To create a note using the Arrow tool, double-click in any empty space in the Edit view. A note is created at the location you've specified,
its length determined by the currently selected Quantize value. Double-click a note with the Arrow tool to delete it.
Resizing Notes (Piano View)
To size any note using the Arrow tool, float the mouse to the left or right edge of the note to reveal the Sizing tool. When this tool appears,
click-and-drag left or right to size the note. As with Events, notes can be sized and resized any number of times. A Part can also be sized
in this way, by floating the cursor near the top of the Part's beginning or end, revealing the Sizing tool.
To change the length of a note while simultaneously resizing the previous or following note to match, hover your cursor near the begin-
ning or end of a note, press and hold [Alt]/[Option] to enable Resize Adjacent Notes mode, and click and drag the note to resize.
When sizing multiple selected notes in the Note Editor with the Arrow tool, three additional behaviors are possible using modifier keys.
Select multiple notes, then click on the end of one note and drag it to the right just a small amount. While still dragging that note, if you
press certain keys on your computer keyboard the following will happen:
-
[Ctrl]/[Cmd] + drag will snap the length of all notes to match the length of the clicked note.
-
[Alt] + drag will stretch the notes across the time grid. If the outer edge of either of the outermost notes is dragged, the stretching
can go on indefinitely. If an inner edge of any note is dragged, the middle notes will eventually end up on top of the outermost
notes.
-
[Alt] + [Ctrl]/[Cmd] + drag the right edge of one note makes all of the notes end at the same time. [Alt] + [Ctrl]/[Cmd] + drag the
left edge of one note makes all of the notes start at the same time.
Duplicating Notes
To duplicate selected notes using the Arrow tool, hold [Alt]/[Option] on the keyboard, click on the selection, and drag left or right. Release
the mouse button when the desired position is reached, and the selection is duplicated to this position.
More Arrow Tool Tips
-
To switch temporarily to the Eraser tool while the Arrow tool is selected, press and hold [Ctrl]/[Cmd].
-
To switch temporarily to the Split tool while the Arrow tool is selected, press and hold [Ctrl+Shift]/[Cmd+Shift].
When multiple Parts are visible in the Editor, only one is actively available for editing at a time. For example, when doing a Select All oper-
ation, only notes in the currently active Part are selected. To activate a Part, click on any note or empty space within it.
Strums
A group-selection of Note Events can quickly be arranged into a Strum. With a group of Note Events selected, begin by clicking and drag-
ging from the middle of one of the group’s Note Events, and then hold [CMD]+[OPT] / [CTRL]+[ALT] to create a Strum. This can be done
from any Note Event in the Group.
Note that Strums are affected by Snap settings. For a more humanistic sound, you may opt to turn off Snap (N) while creating Strums.
Various strums.
Edit View Event Editing

Split Tool
In Piano view, the Split tool allows you to split notes so that they become two separate notes. Clicking on any note directly splits the note
at that position, while selecting multiple notes and then splitting, splits all selected notes. Holding [Alt] when clicking with this tool per-
forms a split of any selected notes, as well as a split of the part itself, so that one part becomes two.
To switch temporarily to the Arrow tool while the Split tool is selected, hold [Ctrl]/[Cmd].
Split at Grid
It is possible in the Piano and Drum views to split a single note into multiple notes based on the current Quantize setting. Select any num-
ber of notes and choose Split at Grid from the Musical Functions menu. Notes are split based on their position relative to the bar line, with
splitting occurring only up to the next bar line after the note start time.
The Split at Grid function can also be applied to whole Instrument Parts and Audio Events.
Paint Tool
The Paint tool in the Note Editor is used to draw notes in an Instrument Part. To draw a note, click at the desired position. The default
length for new notes can be set in the Note Editor Inspector to the right of the keyboard interface. Click the note again to delete it.
To momentarily select the Arrow tool while using the Paint tool, hold [Ctrl]/[Cmd] on the keyboard.
Creating a New Part
To create a new Part in the Edit view with the Paint tool, click and drag in any open area in the Editor timeline. You can resize Parts while
the Paint tool is selected, by floating the cursor near the top of the start or end of the Part, which reveals the Sizing tool.
Painting in Piano View
When drawing in Piano view, the Paint tool snaps to certain vertical and horizontal positions based on the Quantize and Scale settings.
When the cursor hovers over the Note Editor, the note value for the current cursor position is highlighted on the vertical keyboard.
As you enter new notes, click-and-drag to the right to make the note any length you want. To edit the velocity of a note as it is being
drawn, drag up and down after you click to draw the note.
To modify the length of an existing note, hover the cursor at the edge of the note to reveal the Sizing tool, then click-and-drag.
Painting in Drum View
When drawing in Drum view, the Paint tool snaps to specific horizontal positions based on the Quantize setting. When the cursor hovers
over the Note Editor, the Pitch name and note number are highlighted in the Pitch Names list.
Hold [Alt] and then click-and-drag to draw a line of notes at the current Quantize value.
Adjusting Velocity Values
To edit the velocity of an existing note in Piano view, hold [Alt+Ctrl]/[Cmd +Opt] on the keyboard and click-and-drag up or down on the
desired note. Optionally, with sufficient zoom applied in the Edit Window, the Arrow Tool can be used to edit a note event’s velocity by
clicking the top third of the note event and dragging vertically. Finally, you can also edit the velocities of notes in the Part Automation lane
of the Note Editor, which is discussed in the Instrument Part Automation section of the Automation chapter.
Line Drawing Mode
Press and hold [Alt] on the keyboard with the Paint tool selected to enter Line Drawing mode. In this mode, you can draw a line of note
Events in the Note Editor, and you can draw lines in automation envelopes, as discussed later in this manual. This function also works
when the Paint tool has been temporarily invoked by pressing [Ctrl]/Cmd].
Edit View Event Editing

Transform Tool for Note Velocity
If you want to edit velocity for many notes at once, you'll find the Transform Tool very useful. Similar to the way the Transform Tool in
Arrange view is used for scaling and shaping automation curves, the Transform tool in the Note Editor lets you scale and shape note
velocity data.
To use the Transform Tool, click the triangle at the edge of the Paint tool in the Note Editor, and choose "Transform Tool" from the pop-up
list. With this tool, select a range of velocity values in the Velocity display below your chosen notes. The selected values can then be
scaled smoothly up or down by dragging the handles at the top or bottom of the selection.
You can also drag the handles at the corners of the Transform selection, to scale the selected velocities with a sloping action, as shown
above. This makes it easy to create smooth changes in velocity across a range of notes.
Eraser Tool
The Eraser tool in the Note Editor is used to delete notes. With the Eraser tool selected, click directly on any note to delete it. When mul-
tiple notes are selected, clicking any one of them with the Eraser tool deletes all selected notes. Click and drag with the Eraser tool (start-
ing in empty space) to delete all notes you touch.
You can temporarily switch to the Arrow tool while the Eraser tool is selected by holding [Ctrl]/[Cmd].
Mute Tool
The Mute tool is used in the Note Editor much as it is used in the Arrange view. With the Mute tool selected, click on any note to mute it,
and click on any muted note to unmute it. Click and drag with the Mute tool to mute all notes that fall within your selection.
Listen Tool
The Listen tool is a quick way to audition a section of a Track while editing. With the Listen tool selected, click and hold inside the Editor
window to solo the Track and start playback from that position. Playback continues until the cursor is released; then playback stops and
the Track is un-soloed.
Edit View Event Editing

Cut, Copy, Paste, and Duplicate Notes
You can cut, copy, paste, and duplicate notes exactly as you can with Events in the Arrange view, as described in the Common Editing
Actions section of this chapter. It is also possible to cut or copy notes and then paste them (or simply drag-and-drop them) directly into
the Arrangement onto a selected Instrument Track. Doing this creates a new Instrument Part containing the selected notes.
Transposing Notes, Instrument Parts, and Tracks
Transposing notes, or changing a group of notes by a given interval, is a common action that takes advantage of the flexibility of note
data. It is possible at any time to transpose notes, a whole Instrument Part, or all of the contents of an Instrument Track.
To transpose a note or group of notes within an Instrument Part, open the Note Editor by double-clicking on the desired Part, and do the
following:
-
Select all of the notes you wish to transpose.
-
Select Transpose from the Musical Functions sub-menu, which can be accessed from the Event menu, the [Action] button, or by
[Right]/[Ctrl]-clicking within the Edit view.
-
Choose from one of the preset transpositions or use the horizontal fader to set the number of semitones by which the selected
notes are transposed (or simply enter a semitone value into the text field). A positive number results in the notes being trans-
posed up, and a negative number results in the notes being transposed down.
To transpose an entire Instrument Part:
-
Select the Part you wish to Transpose in the Arrange view.
-
Select Transpose from the Musical Functions sub-menu, which can be accessed from the Event menu, the [Action] button, or by
[Right]/[Ctrl]-clicking within the Edit view.
-
Choose from one of the preset transpositions, or use the horizontal fader to set the number of semitones by which the selected
Part is transposed (or simply enter a semitone value into the text field). A positive number results in the Part being transposed
up, and a negative number results in the Part being transposed down.
When transposing notes or Parts, the notes are moved graphically to represent the change. In this case, the notes displayed are the
notes you hear.
You can also use this Transpose function to set all selected notes (or all notes in a selected Part) to the same note value by enabling Set
All To, then selecting your note value of choice, and pressing [OK].
To transpose all of the contents of an Instrument Track:
-
Select the Instrument Track you wish to transpose.
-
Open the Inspector by pressing [F4] on the keyboard.
-
Enter a value in the Transpose field for the number of semitones by which the Track is transposed.
When transposing a Track via the Inspector, the transposition is not reflected graphically. The positions of the notes in all Parts on the
Track remain unaffected. In this case, the notes displayed may not be the notes you hear. This parameter also affects the notes you hear
when you play your Keyboard.
Quantizing Instrument Parts
Quantizing Instrument Parts allows you to realign notes in time to match a given time subdivision or other grid more closely. In practice,
quantizing is generally used to clean up note timing to more closely match the intended timing, although it can also be used creatively.
The results of quantizing are determined with the Quantize settings as found in the Quantize panel. The Quantize panel allows precise
control over all quantize settings. Refer to the Quantize Panel section for more information.
It is possible to extract a groove from an instrument part by dragging-and-dropping it into the Groove section of the Quantize panel, just
as with an Audio Event. Any Instrument Part or Audio Event can then be quantized to that extracted groove.
To enable quantizing notes while recording, open the Record Panel by selecting Record Panel in the View menu (or pressing [Alt]/
[Option] + [Shift] + [R]), then Click on the Input Quantize button. Input quantization can be undone if you want to use the performance as it
was played.
Quantize and Restore Timing
To quantize an entire Instrument Part, select the Part in the Arrange view and press [Q] on the keyboard or choose Quantize from the
Musical Functions menu. To quantize an individual note or notes, select the notes in the Note Editor and then apply quantization, as
before.
Alternatively, if notes are selected in the Note Editor, and then the Quantize value is changed with Auto engaged (toggled with the small
[IQ] button, next to the Quantize value in the Editor toolbar), the selected notes are automatically quantized using the newly selected
Quantize value.
Edit View Event Editing

Furthermore, you can quantize note ends, which adjusts the Note Off time for any selected notes, by selecting Quantize End from the
Musical Functions menu.
To restore the original timing to quantized Instrument Parts or notes, select the Part or notes and press [Shift]+[Q] on the keyboard, or
select Restore Timing in the Musical Functions menu.
Freeze Quantize
It is sometimes very helpful to make note quantization permanent so you can quantize again based on the current quantized positions,
rather than the original note positions. To do this, select the notes and select Freeze Quantize from the Musical Functions menu. You
cannot Restore Timing for these notes, as the newly quantized positions effectively become the original positions.
Humanize
Strictly quantizing every note so that rhythms are perfectly precise can cause notes to sound lifeless and mechanical. The Humanize
function alters note start and end times and velocity within a very small threshold, based on rules modeled on common human per-
formance patterns. This provides just enough variation to make a performance sound more like a human played the parts.
To use this function, select any notes and then choose Humanize from the Event/Musical Functions menu. Note that the exact results
cannot be directly controlled. You can also choose to Humanize Less, which alters the notes in a similar fashion as Humanize but based
on rules designed to result in less-humanized performance patterns.
Note Editor Inspector (Piano View)
When a note is selected, its start and end positions are displayed in the Note Editor Inspector, as are its pitch, velocity, and mute status.
Each of these parameters can be edited directly in the Inspector. When editing notes using the Inspector, all selected notes are affected,
their values changing relative to the initial setting of each note. The one exception is that when Velocity is specified for multiple notes
using the Inspector, all notes snap to the new value, regardless of their previous Velocity value.
Edit View Event Editing

When a note is selected, its start and end positions are displayed in the Note Editor Inspector, as are its pitch, velocity, and mute status.
Each of these parameters can be edited directly in the Inspector. When editing notes using the Inspector, all selected notes are affected,
their values changing relative to the initial setting of each note. The one exception is that when Velocity is specified for multiple notes
using the Inspector, all notes snap to the new value, regardless of their previous Velocity value.
The simplest way to edit start and end positions, pitch, and velocity is to place the mouse cursor over the parameter and scroll the mouse
wheel up or down. Another way to edit a selected note’s velocity is to click-and-drag the Velocity value in the Note Editor's Inspector
panel. When you release the mouse button, the Velocity value is applied to all selected notes. The value currently set by the Velocity
parameter is applied by default to any new notes created with the Paint tool.
Enable the Audition Notes option to hear the pitch of each note that is selected, created, or moved, played through the current instru-
ment.
You can also Mute, Solo, or open the Device Editor for the current Track from within the Note Editor Inspector, using buttons that look
much like their counterparts in the Arrange view.
Both input Chords and the Current Chord position are detailed in the Note Editor Inspector. When multiple tracks are visible in the editor,
all of them contribute to the chord displayed.
To select a different Track for editing, click the Track name at the top of the Note Editor Inspector and select one of the Tracks.
Multitrack Note Editing
It is possible to view and edit more than one Instrument Track at a time in the Note Editor. To do this, hold Shift and select Instrument
Parts on different Tracks in the Arrangement. More Parts can be added at any time by holding Shift and selecting them in the Arrange-
ment.
Edit View Event Editing

Double-click on any Part in the Arrangement to make its Track the only one you see in the Note Editor. To zoom the Editor window so it
shows all of the notes the Part contains, disengage the [Synchronize Editor to Arrangement] button, hold [Alt]/[Option], and then double-
click the Part. Use the lower half of the Part for this command when the Link button is active in the Arrange view toolbar.
The Note Editor also has its own Track List, opened via the Track List icon in the upper left corner of the Note Editor's Inspector panel.
You can show or hide Tracks in this List via the Show/Hide button to the left of the Track name, and can independently set each Track to
Edit Active via the pencil-shaped Edit button to the far right of the Track name. If a Track is shown and Edit Active is not engaged, the
Track’s notes are not selectable. This allows it to be viewed as a reference, and keeps it safe from an accidental alteration.
When multiple Parts are displayed, the notes for each Part are colored with their Track colors and audition normally through their Tracks.
Selected notes are displayed in white.
Also, when multiple Parts are displayed it is possible to transfer notes from one Part to another using the [Right]/[Ctrl]-click contextual
menu item Transfer Notes. This removes the selected notes from the original Part, indicated with a checkmark in the Transfer Notes list,
to the selected Part.
It is possible to preserve the Track List selection so it remains the same even if you switch to another Track in the Arrange view. To do
this, click the Lock Track List icon next to the Track List button. Note that the Piano and Drum views share a Track List selection and the
Score view has its own, which can be locked independently.
To bring a different Track into focus for editing when multiple Parts are displayed, click the Track name at the top of the Note Editor
Inspector and select the desired Track.
Note Color
Clicking the Note Color drop-down menu in the Note Editor presents a menu of several options for Note Color.
You can select any one of the four options at a time:
-
Part colors the notes based on the color assigned to the Instrument Event.
-
Pitch colors the notes based on their chromatin pitch.
-
Velocity colors the notes based on the notes’ velocity value; from purple for low Velocity to red for high Velocity.
-
Scale colors the notes based on if they are compliant with the Track’s Scale setting - blue for in-scale, red for out-of-scale.
Togglable options, selectable independent of the above, include:
-
Velocity Bar toggles rendering of the velocity indicator on the left of each note event, longer for higher velocity and shorter for
lower.
-
Black Selection toggles the black highlighting of currently-selected Note Events.
-
Note Controller toggles rendering of a stripe through Note Events associated with a note controller.
Edit View Event Editing

Drum Editor
Standard piano-roll-style note editing is ideal for melodic and harmonic content, in which notes tend to have differing lengths. Drum pro-
gramming and editing present a different challenge. Percussive sounds often contain their own amplitude envelope that ends at a pre-
determined time, which makes the start of each note the most important part. For added clarity when working on this sort of content, Stu-
dio One features a dedicated Drum view that shows your drum notes as "triggers," marking the start of each note.
To enter the Drum Editor, click the Drum View button at the top of the Note Editor toolbar. You can return to Piano view or Score view at
any time by clicking the appropriate button.
In the Drum Editor you can add, remove, and manipulate notes just as you normally can, with some useful differences. The Note Editor
Inspector on the left side is basically the same as in Piano view, only without the features that don't apply to Drum view.
Tight Integration with Impact XT
While you can use the Drum Editor on any Instrument Part, it shares a special connection with Impact XT. When you view an Impact XT
part in the Drum Editor, instead of seeing the full range of notes, you see each currently loaded sound as a row in the grid. with its name
and color code visible, for easy programming and editing. Any unused notes are hidden.
Enter Strings of Notes with the Paint Tool
When you enter notes with the Paint Tool in the Piano view, you click to begin the note, then drag to set its length. In the Drum Editor,
since note length is not shown, you can click and drag across the grid, entering multiple new notes at divisions set by the current Quant-
ize value. This makes creating drum patterns, fills, and rolls a more fluid process.
Edit View Event Editing

Edit a Drum Map
When using the Drum Editor with an instrument other than Impact XT, you see the full range of MIDI note names, each with its own row in
the editing grid.
If you'd like to exclude certain notes that you don't plan to use, or change note names to match the corresponding sounds, click the
wrench-shaped Edit button near the top of the Pitch Names panel to edit the Instrument List.
To edit the order of notes, click and drag the double line to the left of each note row. To hide a note, click the circular button in the row,
turning it dark grey. To rename a note, click inside its name display, then enter your new name. You can then save the Drum Map to
recall at a later time by selecting Store Preset from the Pitch Names menu.
When you're finished editing the Instrument List, click the wrench-shaped button again to lock in your changes.
Select a Drum Map
Click the drop-down menu arrow in the Pitch Names field to recall your Drum Maps. Simply select any Map from the list to load it. (A Gen-
eral MIDI Drum Map is provided.)
Import Drum Maps
When working with a drum instrument (or drum sample library) other than Impact XT, you can import a list of pitch names into the Drum
Editor, known as a "Drum Map." This lets you auto-assign names to each available note that the instrument or library preset can respond
to, for similar ease of programming as when working with Impact XT.
Drum maps can be downloaded for many commercially available instruments and libraries from http://exchange.presonus.com. To
import a drum map in the Drum Editor, click the wrench-shaped button near the top of the Pitch Names panel, then simply drag the drum
map file onto the list of pitch names in the left column.
Key Switches and Sound Variations
Key Switches and Sound Variations are covered in the Sound Variations topic.
Edit View Event Editing

Note Chase and Cut
In the Studio One/Options/Advanced/MIDI (macOS: Preferences/Advanced/MIDI) menu, you can find two options: Chase Long Notes
and Cut Long Notes at Part End.
Chase Long Notes should be engaged if you would like Studio One to play back a long note even if playback begins after that note's Note
On position, effectively treating the playback position as the Note On. This is very useful when working with long, synthetic drone parts,
for instance, which may have a Note On at bar 1 and then continue throughout the rest of the Song.
Cut Long Notes at Part End should be engaged if you would like a note to stop playback if the related Instrument Part ends before that
note's Note Off position.
Select Notes
Selecting notes with your pointing device is often an efficient way to make changes in Instrument Parts, but sometimes, a bit of auto-
mation may come in handy. The Select Notes function lets you select certain notes within a part based on a range of parameters, such as
"just the highest notes," or "just notes within a certain range of velocity."
To use this function, click the [Action] button in the Note Editor, and choose Select Notes. In the window that appears, you can choose
from the following actions:
-
Select Use this mode to select notes that fall within the chosen range of parameters.
-
Deselect Use this mode to deselect notes that fall within the chosen range of parameters, if those notes are currently selected. If
no notes are selected, using this mode selects any notes that fall outside the chosen range of parameters.
After selecting one of those modes, choose one of the following operations:
-
Highest notes Select the highest notes that exist at any given time in the Part.
-
Lowest notes Select the lowest notes that exist at any given time in the Part.
-
Range... Select the notes that fall within a range of Pitch, Velocity, or Note Length. Select the criteria you want to focus on,
then set the range of selection with the sliders.
-
At interval... Select notes based on intervals according to position on the beat grid, or numeric relationships between notes:
-
Beat Choose this mode to select notes according to their relationship to the grid:
-
Beat grid Sets the rhythmic value at which note selection is calculated.
-
Selection interval Sets the number of beats (the value of which is set with Beat Grid) between note selections.
-
Start offset Sets the number of beats to skip before making the first set of note selections.
Edit View Event Editing

-
Selection tolerance Sets the amount of "slope" allowed in calculating note selections, to allow for selecting
notes that do not conform exactly to the grid.
-
Event count Choose this mode to select notes based on their numerical relationships:
-
Select at every n-th position Sets the numeric spacing between note selections. For example, a setting of 2
selects notes at every second note. This does not necessarily relate to the grid. If there is a space in the notes,
the count between selections continues when the next notes start.
-
Start selection at n-th position Sets the number of note occurrences to skip before making the first set of
note selections.
-
Selection tolerance Sets the amount of "slope" allowed in calculating note selections, to allow for selecting
notes that do not conform exactly to the grid.
-
Muted notes Use this option to select only the notes that are currently muted within the specified range. If a range of notes has
not been specified, all muted notes within the current Event or the current Track are selected.

## Sound Variations

About Sound Variations
Modern sampled instruments often ship with many different articulations, techniques, and expressions. A sampled violin, for example,
might have many different techniques just in bowed sounds: staccato, legato, sul pont, tremolo, harmonics, and so on. Of course, having
this wide variety of techniques and articulations available requires a solution for triggering them during playback or performance—In Stu-
dio One, Sound Variations are that solution.
Sound Variations have been developed and expanded from Studio One’s Key Switches, which are themselves a system of triggering per-
formance articulations via Note Events that lay below or above a virtual instrument’s performance register. For example, a C0 Key Switch
note, outside the musical range of a violin, might be used to trigger a legato variation, and C#0 might trigger a pizzicato variation.
MIDI notes from an external controller keyboard can be used to trigger simple or complex Sound Variations via pre-defined Key
Switches—that's the input side. On the output side (from Studio One to the virtual instrument), an Activation Sequence is then used to
trigger the desired articulation. Activation Sequences can include more than just Note On / Off messages; they can also employ MIDI CC
data and program/bank changes—as well as combinations of all of these.
...but first, a bit about Key Switches.
As of Studio One 5.2, Key Switches have been re-imagined as Sound Variations! No functionality has been lost in this improvement. Any
legacy Songs or Key Switch Maps created in previous versions of Studio One that use Key Switches will enjoy full backward-com-
patibility when opened in 5.2 or later. Note that third-party instruments will likely still use the term “Key Switches” to describe their artic-
ulation functionality. That’s fine, they’ll still work great with Sound Variations.
Assigning Sound Variations to Note Events via Right-click

## Sound Variations

Studio One’s Note Editor offers a quick and easy way for you to enter Sound Variations via a right-click contextual menu.
Stay mindful that Sound Variations display in the Automation Lane, not the Note Editor.
1.
Create an Instrument Track and load “Nylon Guitar Full” from the Presence XT core library.
2.
Add a few notes via the Paint tool, or drag and drop a MIDI file to this new track.
3.
Open the Note Editor [F2] if it’s not already open.
4.
Click the Show/hide Automation Lanes button (
), and then click the Sound Variation Parameter tab at the top of the lane.
This tab is available in the Piano and Drum views, and will display below the Note Editor.
5.
[Right-click] a Note Event in the Note Editor and mouse over “Apply Sound Variation” from the contextual pop-up menu. You’ll
receive a submenu of Variations to choose from. Click “Open” for an open-string sound.
6.
[Right-click] another Note Event. From the contextual pop-up menu, choose “Hammer-on.”
7.
Press the spacebar or [Left-Click] the Play button to play your track. You should hear that any Note Events played coincident
with the “Open” Sound Variation will sound normal, while Notes played coincident with the “Hammer-On” Key Switch will sound
hammered-on.
8.
Experiment! Assign different Sound Variations across your Song, if you like, and listen back. It’s quite addictive.
From the right-click contextual menu, you can also select from an efficient list of up to ten recently-used Sound Variations under “Used.”
This can dramatically speed up your workflow when using vast sound libraries and grants you quick access to your favorite Variations.

## Sound Variations

Be mindful that Sound Variations will be applied to all coincident Notes, and as such you won’t be able to hear multiple articulations sim-
ultaneously. For example, you won’t be able to program a chord where the high notes use “Hammer-on” and the low notes use “Open.”
Assigning Sound Variations using the Paint Tool inside the Sound Variations Automation Lane

## Sound Variations

To view and edit Sound Variations in an Automation Lane, we’ll use the same “Nylon Guitar-Full” Track from the previous example.
1.
Open the Note Editor [F2] if it’s not already open.
2.
Click the Show/hide Automation Lanes button (), and then click the Sound Variation Parameter tab at the top of the lane. This
tab is available in the Piano and Drum views, and will display below the Note Editor.
3.
Using the Paint tool, [Left-Click] in the Automation Lane. You’ll be presented with a contextual menu of Sound Variations for the
Nylon Guitar. Choose “Open.”
4.
Repeat step 3 to the right of your last Sound Variation and select “Hammer-on.”
5.
Press the spacebar or [Left-Click] the Play button to play your track. You should hear that any Notes played coincident with the
“Open” Sound Variation will sound normal, while Notes played coincident with the “Hammer-On” Sound Variation will sound
hammered-on.
You can also [Left-Click] and hold the mouse button in the Sound Variations lane to bring up the menu; then move your cursor to the
desired Variation and release the mouse button to select.
Assigning Sound Variations using the Note Event Inspector
The Note Event Inspector, to the left of the Edit Window, allows you to apply the current Active Sound Variation to a group of notes with a
single click. Simply use the Arrow tool to select a group of Note Events and click the [+] button in the Note Event Inspector to Apply Active
Variation to the selected Note Events.
Clicking the [+] button with no notes selected will apply the Active Sound Variation at the current playback cursor position.

## Sound Variations

Power user tip: The “Apply Active Variation” is an excellent candidate for your Macros, Keyboard shortcuts, or a trigger from Studio One
Remote!
Power user tip: The “Apply Active Variation”command is an excellent candidate for your Macros, Keyboard shortcuts, or a trigger from
Studio One Remote!
Converting Key Switches to Sound Variations

## Sound Variations

It’s easy to convert Key Switches to the Sound Variations format. Be sure to have your mapping set up in the Sound Variations Editor
first, and have it set to “Use Activation Sequence.”
1.
[Right-click] a Note Event in the Piano View.
2.
Choose “Convert Key Switches to Sound Variations”
The notes will disappear from Piano View and reappear as Sound Variations in the Automation Lane. Just two clicks.
Select Part Automation with Notes
Although used in conjunction with Note Events, Sound Variations exist independently of Note Events—hence their home in the Auto-
mation Lane. If you would like to ensure that your Sound Variations stay connected to coincident Note Events when copying or moving
notes, you simply need to enable "Select Part Automation with Notes” via the right-click contextual menu or this icon above the Edit Win-
dow:

## Sound Variations

Sound Variation entries in the Automation Lane remain in effect until another Sound Variation is entered; its colored bar stretches until
the next Sound Variation Event.
To change a Sound Variation you have already placed:
1.
Select the Sound Variation you want to change in the Automation Lane
2.
[Left-Click] and hold to display a contextual pop-up menu.
3.
Select the desired Sound Variation from the menu.
Sound Variations, Transposition, and Note FX
In order to avoid conflicts with musical actions (such as Transpose) or processing with Note FX or the Chord Track, Key Switches in the
Note Editor are filtered and excluded from any type of playback processing. They also do not appear as notes in the Score Editor. Instru-
ments that report their Sound Variations to Studio One (such as Presence XT) display articulations with their names automatically.
For an example, we’ll continue with “Nylon Guitar Full” from the Presence XT Core Library. Notice the highlighted key switches in Piano
View. These keys will be unaffected if the Instrument Track is transposed, and they will not be triggered by Note FX such as an arpeg-
giator. This way you can re-use a particular guitar articulation in other locations—even when the guitar’s notes change to follow the
Chord Track, for example.
The Sound Variations Editor
The Sound Variations Editor is your home for defining, mapping, and organizing your Sound Variations, as well as storing and recalling
their presets. Using this interface, you’ll be able to import and create complex articulation controls suitable for use with robust orchestral
virtual instruments.

## Sound Variations

It can be helpful to think of the Sound Variations Editor as an interpreter between your Song’s Note Events and the virtual instrument it is
working with. The input it receives comes from note information or other control signals; the output it sends is passed on to the virtual
instrument assigned to its respective Track.
Above, we see the Sound Variations Editor loaded with the aforementioned “Nylon Guitar-Full” Presence Preset. Let’s take a look at the
options presented.
The Sound Variations List at the left of the interface displays all Sound Variations for the currently selected Track. Clicking on any of
these to select them also sends an activation sequence command to the connected Virtual Instrument.
The Drop-Down menu at the top of the interface controls the Global settings for Sound Variations on the currently selected Track. Its
options include:
-
Enable Key Switches Choose this option to use the input Key Switches defined in the current map. Pitches tagged as Key
Switches will ignore transposition and Note FX and Key Switch triggers will be sent to the Instrument.
-
Disable Key Switches Use this option to deactivate any input Key Switch assignments and pass all notes to the instrument. A
good choice for use with complex libraries that make use of multi-layered activation sequences that would consume too many
keys if Key Switches were used. To enter or record a Sound Variation, commands on a hardware controller or Studio One
Remote can still be used.
-
Use Activation Sequence Use this option to directly control the instrument from your hardware controller using the Activation
Sequences created in the Editor. In other words: Input from controller=Output to virtual instrument. All notes that are on Key
Switch pitches are sent to the instrument. This is an ideal choice for users who have developed a proven articulation layout that
they would rather not re-map from scratch. More on building this mapping follows shortly.
Be mindful that if you have a Key Switch programmed in the Note Editor AND a Sound Variation programmed in the Automation Lane
simultaneously, the articulation that will be prioritized and heard is determined by these settings.
The Options menu above the keyboard interface and below the Sound Variations list contains the following options:
-
New Variation Use this to create a new Sound Variation. If the instrument supports custom Key Switch querying, all sound vari-
ations will be mapped automatically. When this is the case, “New Variation” will be disabled—the Sound Variations are already
assigned!
-
New Folder Use this to create a new Folder for your Sound Variations to organize and keep things tidy.
-
Remove Use this to remove the currently-selected Sound Variation or Folder. Removing a Folder will not delete its contents. If
the instrument supports custom Key Switch querying, this option will be disabled.
Undo/Redo Icons Use these to Undo/Redo tasks performed in the Sound Variations Editor; these tasks are not affected by Studio
One’s main Undo/Redo functionality.
The Action menu on the bottom right of the Sound Variations list contains various Actions to help you quickly create and map your
Sound Variations:
-
Reload Map from Instrument Use this option to reset your Sound Variations map to the default settings as determined by the
current Instrument. This option is only available with Studio One’s included instruments and third-party VST instruments support
Studio One’s Dynamic Mapping.
-
Assign Default Key Switches Use this option to set the input Key Switches to match the output Key Switches. Useful for maps
with basic single-key Key Switch mappings; particularly if your Key Switch mapping has gotten mixed up somehow and just
needs a clean slate. While similar to the “Use Activation Sequence” Option in the Sound Variations Editor’s drop-down menu,
this offers the advantage of displaying colored Key Switches in the Arrangement View and Note Editor.
It's similar to setting the Sound Variations Editor to "Use Activation Sequence," but has the advantage of showing the marked
keys with colors. Also, it could be used as a starting point if you would ever want to start over with a custom (re)mapping.
This option is only available with Studio One’s included instruments and third-party VST instruments that support Studio One’s
Dynamic Mapping. (More info on Dynamic Mapping farther below.)
-
Assign Key Switches Chromatic Use this option to assign Key Switch Note values ascending chromatically. Choose from a
list of four value ranges starting at C -2.
-
Assign Key Switches White Keys Use this option to assign Key Switch Note values ascending value using only the white
keys. Choose from a list of four value ranges starting at C -2.
-
Shift Key Switches Use this option to nudge all of your Key Switches note values en masse, either by ±1 octave or ±1 note.
-
Clear All Key Switches Use this option to remove all Key Switch note values from the Input column in the Sound Variations list
as well as from the Note Editor.

## Sound Variations

Musical Symbols and the Inspector
Clicking on the “Musical Symbols” button or the “I” icon on the top right of the interface will toggle visibility of the Score Setup view and the
Inspector on the right side of the Sound Variations Editor.
The Inspector contains the following options. Changes to each of these will edit the currently-selected Sound. Note that many of these
options can also be edited directly from the Sound Variation List on the left of the Editor.
-
Color Select the desired color of the Sound Variation by [Left-clicking] on the colored rectangle.
-
Name Enter the desired name of the Sound Variation by [Left-clicking] on the text box and typing.
-
Input Pitch determines the input used to trigger Sound Variations. Select the Note value assigned to this Variation for use with
Key Switches. Notes of this value will behave as Key Switches in Studio One’s Note Editor when the Global (drop-down menu)
option is set to Enable Key Switches.
-
Score Symbols Select the Musical Symbol assigned to trigger this Variation. (More on this later.)
-
Default Score Variation This item denotes that the selected Sound Variations will be used when no Sound Variation is expli-
citly applied to Note Events.
-
Momentary This checkbox controls if the instrument will return to the previous Sound Variation after the Note Off for this Sound
Variation change has been received. When checked, the instrument switches back to the Variation which was active before
when the momentary variation terminates. When unchecked, an articulation will continue to be in effect until a new Key Switch
event is processed.
Activation Sequence The heart of Sound Variations, this powerful menu controls which articulation commands are sent from Studio
One’s Sound Variation engine to the Virtual Instrument assigned to the current Track. These sequences allow for complex multi-key and
controller input commands; quite useful as sophisticated virtual instruments require complex multi-input activation sequences to control
their articulations. If these libraries used a single Key Switch for each articulation available, there would be no keys left to play music on!
Sound Variations support these more demanding instruments while also letting you re-map Sound Variations to control them from a com-
puter keyboard, MIDI hardware controller, or Studio One Remote—as well as via user-defined keyboard shortcuts or Macros. (More on
that follows below.)
Note that any instrument using Dynamic Mapping, including Studio One’s own instruments like Presence XT, has its activation
sequences mapped and locked to the instrument. You cannot change these Activation Sequences, but you can trigger them from Key
Switches.
This workflow will be available while the Global (drop-down menu) option is set to Use Activation Sequences.
-
Note On + Off The standard event item type. Choose this item type to create an Activation sequence step using a full on/off key-
stroke cycle from a MIDI controller.
-
Note On Choose this item type to create an Activation Sequence step using a MIDI Note On message.
-
Note Off Choose this item type to create an Activation sequence step using a MIDI Note OFF message.
-
MIDI CC Choose this item type to create an Activation sequence step using a MIDI Control Change message.
-
Program Change Choose this item type to create an Activation sequence step using a MIDI Program Change.
-
Bank Change Choose this item type to create an Activation sequence step using a MIDI Bank Change.
-
Channel Change Choose this item type to create an Activation sequence step using a MIDI Channel Change. This is ideal for
users who organize separate instances of their instruments on different channels, and would rather trigger them with Channel
switches than Keyswitches.
When you add a Channel Change, the default value is "Reset." This means the original MIDI channel of the track will be used. If
you change this value to any MIDI channel from 1 to 16, you can go back to "Reset" by either entering a "0" or the word "Reset."
The Preset Menu is located at the top left of the Sound Variations Editor. Here, you can:
-
Load a stored Preset by choosing it from the horizontal drop-down menu.
-
Store Preset Use this option to save the current Sound Variations Editor state as a new, named Sound Variation preset in the
subfolder of your choice.
-
Update Preset Use this option to make a one-click update to the currently loaded Preset
-
Note that Key Switches and Sound Variation Editor settings will be saved when your Song is saved, when saving an Instrument
Preset, or when saving an Instrument+FX Preset. You can use Instrument Presets for Instrument-specific Sound Variation set-
tings; use the Sound Variations Editor Presets for mappings that you may want to use frequently with several sample libraries
that follow the same Key Switch layout.

## Sound Variations

Score Setup: Musical Symbols and Dynamic Markings
The Score Setup interface is opened by clicking the Musical Symbols or “i” button on the top right of the Sound Variations Editor.
Once open, Score Setup allows you to assign traditional Musical Symbols as triggers for Sound Variations. Composers may find it more
intuitive to place an Accent or Staccato Symbol in a traditional manner in the Score Editor rather than navigating through a series of nes-
ted Sound Variations to apply the desired effect.
Assigning Musical Symbols to Sound Variations
-
Symbol Click in this column to choose the desired Symbol you would like to use to trigger a Sound Variation and highlight its
row.
-
Sound Variation Click in this column to bring up a context menu; from there choose the Sound Variation you would like
triggered by the Symbol listed in the currently highlighted row.
-
Process When ticked, this box indicates that Studio One will run its own processing of the Musical Symbol applied, independent
of the virtual instrument or Sound Variation currently active on the Track. For example, Studio One will interpret a Staccato sym-
bol to produce shorter notes, or a trill to produce alternating notes.
This can prove undesirable if, for example, your sampled instrument includes specific samples for tremolo performance, which
are then being triggered atop Studio One’s own tremolo performance.
You can also simply drag and drop a Musical Symbol onto a Sound Variation in the list on the left of the editor to apply it as a trigger.
Assigning Dynamics Markings to Sound Variations
Much like the previously discussed Musical Symbols, Dynamics Markings can also be used to trigger MIDI velocity changes in your Note
Events.
-
Dynamics Click in this column to choose the desired Marking you would like to use to trigger a MIDI velocity change, from pppp
to ffff.
-
Parameter Use this column to choose the desired MIDI velocity value assigned per Dynamic Marking. Default values are dis-
tributed from 13-127.
-
Process Dynamics When ticked, Studio One will use Dynamics Markings to trigger MIDI Velocity changes in Note Events.
The Action Menu
Located at the bottom right of the Musical Symbols interface, the Action drop-down menu presents several useful options:
-
Load Default Choose this item to load the default Musical Symbol and Dynamics maps.
-
Store as Default Choose this item to store all current Music Symbol and Dynamics maps as default. Default settings are saved
on a per-instrument basis.
-
Copy From Choose this item to quickly copy all Score Variation settings from another instrument. This option only appears
when the Dynamics map is empty.
-
Auto Assign Symbol Map Choose this item to automatically assign Symbols to the most appropriate Sound Variations based
on the names of the Sound Variations.
-
Clear Map Choose this item to empty all Score Setup options. Useful for starting over from a clean slate.
Applying Musical Symbols and Dynamics Markings
When composing or editing your music, these Dynamics Markings and Musical Symbols can be applied in two different ways:
-
Via the Note Editor Inspector of the Score View
-
Via the Musical Symbols lane in the Note Editor.
Applying a Dynamics Marking or Musical Symbol via either of the above methods will cause it to be visible in both Score View and Note
Editor. Once set up and linked to your Sound Variations, applying them during composition is fast and intuitive. Visit Score View to
learn more.
At higher Zoom levels, Musical Symbols will be rendered directly on Note Events for easy reading.
Also note that Musical Symbols will out-prioritize Sound Variations for processing in the event of a conflict where one of each is placed in
the same position in their respective lanes.
The Musical Symbols Lane

## Sound Variations

The Musical Symbols Lane can be used to apply both Articulations and Directions to your Note Events.
Articulations: Using the Arrow tool, [left-click] in the Articulations lane to select all of its coincident Note Events. Click again to bring up a
list of articulation options to apply to these notes. Click a third time to choose the Articulation from this list that you would like to apply to
these notes.
You can apply multiple articulations simultaneously.
Directions: Using the Paint tool, [left-click] anywhere in the Musical Symbols lane to be presented with a list of Directions. Much like
Musical Symbols, pick the one that you’d like to use with another left click.
Alternatively, you can [right-click] in the Musical Symbols Lane and choose “insert at cursor” to apply a Direction at the cursor point.
Note that, generally speaking, Articulations are intended for use as temporary, expressive changes in performance technique like a trem-
olo or glissando. Directions are typically less momentary in nature, like a pianissimo directing a performer to play quietly over several
bars.
-
Articulations = note-based.
-
Directions = range-based.
Activation Sequences Unpacked

## Sound Variations

Let’s take a look at an example Activation Sequence using Vienna Symphonic Library’s Big Bang Orchestra. In order to trigger the Sound
Variation “Soft low Brass,” several keystrokes must be entered on a MIDI controller in sequence.
The sequence is:
A -1 | C# 0 | G 0 | C6
... all using Note On + Off input event types.
As we can see from the Vienna Symphonic Orchestra interface, each of these commands in sequence is effectively stepping us through
categories and sub-categories of articulations:
-
Instruments (Senza Piccolo and Con Piccolo variations )
-
Articulation (Long Notes and Short Notes variations)
-
Marcato (Marcato and Non-Marcato variations)
-
Type (Various articulations)
This is comparable to navigating deeper into a filing structure on your computer to search for the file you want. In fact, if you were to col-
lapse several of the folders that organize the default Sound Variations for Big Bang Orchestra, you will find a literal folder structure:

## Sound Variations

Note that this structure is also reflected in the right-click contextual menu when “Apply Sound Variation” is applied to a Note Event:
With this configuration, each MIDI keystroke in the Activation Sequence steps through this hierarchy to get you one step closer to the
articulation that you’re looking for. Of course, if you’re producing, you can use “Apply Sound Variations” via the right-click contextual
menu; using Activation Sequences directly from your MIDI keyboard is well-suited to real-time performances.

## Sound Variations

Dynamic Mapping
Complex instruments require sophisticated mapping of Sound Variations that can be very time-consuming to create. Fortunately for you,
we’ve partnered with some of the best orchestral library developers in the world, and given them the tools they need to expose their cur-
rent mapping to Studio One—so manual mapping is no longer needed! So, when you load a preset from a qualifying instrument that sup-
ports Dynamic Mapping into a Studio One Song, the available articulations and their activation sequence is automatically imported into
the Sound Variations editor.
Here’s an example of a fully-mapped Sound Variation from Vienna Symphonic Library. It’s too big to even fit in the Editor!
Note that any instrument using Dynamic Mapping, including Studio One’s own instruments like Presence XT, has its Activation
Sequences mapped and locked to the instrument. You cannot change these Activation Sequences, but you can trigger them from Key
Switches, commands, keyboard shortcuts, macros, or remote controllers—including Studio One Remote.
Beyond the Keyboard: Alternative Activation Sequence Triggers

## Sound Variations

Studio One provides 20 Sound Variation slots that can be accessed from outside the Articulation Lane or Note Editor. You may also
employ the Find and Apply Variation command, which will cause Studio One to look up a Variations by name and apply it to your Note
Events.
With these, you’re able to trigger Sound Variations from a number of different sources, including:
-
Keyboard shortcuts To assign a Sound Variation trigger to a Keyboard Shortcut, visit the Keyboard Shortcuts panel and
search for “Variation.” There, you’ll find slots with which to fill with your desired Keyboard Shortcut triggers and assign them to
the keys of your choice.
-
Macro To assign a Sound Variation to a Macro, use the Macro Editor. In the Macro Editor, you’ll find the Variation slots pre-
viously mentioned, including Find and Apply Variation.
-
Remote Controller To assign a Sound Variation to an external controller like a MIDI keyboard, first open the Console’s [F3]
External Devices menu. For your desired MIDI controller, click Edit. In the following interface, [right-click] on the button, fader, or
knob you would like to use to trigger a Sound Variation, and choose “Assign Command.” From the contextual menu that
appears, choose the Sound Variation slot you would like to trigger from that control.
-
Studio One Remote You can use Studio One Remote to trigger Sound Variations via the Macros described above. Visit Studio
One Remote’s Macro View and tap the Edit button. A new grey button will appear. Click the + sign on it, search the context menu
for Sound Variations category, and pick the Variation trigger you would like to assign. This is another great use case for “Find
and Apply Variation,” as well.

## Sound Variations

Action Menu
When editing in the Note Editor, several editing commands are likely to be used often. We have placed these commands in a menu that
allows quick access, located to the right of the Quantize and Macro icons in the main tool bar of the Note Editor. Click the [Action] button
to reveal a drop-down menu of commands with which you can edit any selected notes in the Note Editor.
Action Menu

The Actions are arranged in groups of related features: Global, Pitch, Velocity, Quantize, Time, Mute, and Process actions. We'll
describe some of the Actions in this section.
Apply Scale
If an existing musical passage is in a major key but you'd like to hear how it sounds in a minor key, the Apply Scale action will do that for
you. After selecting a group of notes in the Editor, select the desired Scale on the left side of the window. Then open the Action menu and
choose Apply Scale from the Pitch section. If you don't like the results, undo the action, select a different scale, and try it again.
Quantize Notes
In addition to the global quantization functions revealed by clicking the Quantize button, the Action menu lets you apply a very specific set
of quantization parameters to a group of selected notes. You can define the resolution of the Quantize grid, select a Quantize type such
as Triplet or Quintuplet, adjust the Swing, Strength and Range parameters, and then select whether you want to quantize the note starts
and/or note ends.
Distribute Notes
Any selection of note events can be equally distributed at a variable percentage. The Amount parameter defines the strength of the
action.
Repeat Notes to Part End
With this action a selection of notes is repeated as many times as needed to fill the length of a Part. This is will save a lot of time when cre-
ating repeating patterns manually.
Mirror Notes
This note action will mirror notes horizontally, vertically, or both. You can choose which note will be the focal point of the mirror action:
first, middle, last, or any custom note within a range of 10 octaves. This can be a useful compositional tool, providing a quick way to invert
or reverse a melody.
Randomize Notes
This powerful creative tool allows you to add some randomness to your music by applying a variable amount of pitch, velocity, or note
length randomization, as well as any combination of those factors. You can use the original pitch range, define a custom pitch range, or
constrain the results to use the original pitches only. You can also select a new Scale first and have the randomize apply that Scale to the
results.
Thin out Notes
Sometimes it's the notes you don't play that make a song work.
This action is a great way to add some space to a busy track. It takes any selection of notes and deletes some of them according to the
parameters you choose.
There are three methods:
Action Menu

-
Simplify The selected percentage of notes is deleted, starting with notes that are less aligned to the grid. In other words, a note
that is located a 64th-note before a grid line is very likely to be deleted. In contrast, a note located on the first beat of a measure
is only deleted if all notes that are not on the first beat of a measure have already been deleted.
-
Randomly delete notes The selected percentage of notes is removed, but all notes have the same probability of being deleted.
-
Grid Removes all notes that do not start on a position within the selected grid.
Fill with Notes
This note action generates note events based on a set of variables to fill a range or Part. When Apply Scale is selected the results will
always be musically meaningful. You can use this to fill the space between two selected notes, specify the length of the generated notes,
and force the generator to use the pitches of existing notes only, among other features. Note that alternatively, pitch values can be
entered by pressing pitches on an external keyboard controller.

## Patterns

Instrument Parts are just the thing for long, evolving passages, recordings of live playing, and other, more linear musical uses. DAW-
style sequencing allows for a level of bar-by-bar flexibility that the step sequencers and drum machines of the past can hardly match.
However, sometimes it can be helpful to return to those older workflows, as evidenced by the recent resurgence of hardware sequen-
cers.
Pattern-based sequencing treats musical phrases as individual elements, to be switched and swapped at will, looped and finessed.
Enabling this kind of freewheeling arrangement and musical state of play is the role of Patterns, a type of musical part you can create in
Studio One.
Patterns have two modes of operation: One is designed for melodic and harmonic parts, showing available notes on a grid, cor-
responding to the related keyboard notes. The other is for drums and other percussive parts, and it offers automatic note/instrument nam-
ing when used with Impact XT, along with variable phrase lengths and note resolution for each note row.
You can enter notes into a pattern by hand with the pencil tool, or by using the Step Record mode, a note at a time with your
MIDI controller of choice (including your QWERTY keyboard). There's also an option to convert an Instrument Part into a Pattern (and
vice-versa), which makes pattern creation a breeze.
Patterns aren't just static blocks of note data, either. You can create endless variations which are stored within the Pattern. This lets you
start with an idea and create iterations that you can easily switch between as you lay out your arrangement, bringing life to your
sequences over time. Repeats and trigger probability can be applied per step, opening further avenues of expression.
Patterns can coexist on the same Instrument Track with standard Instrument Parts (even sitting right on top of them, if desired). This
makes Patterns perfect for peppering your more traditional sequences with fills, turnarounds, and other flourishes.

## Patterns

Creating Patterns
There are two ways to create a Pattern: Convert an existing Part into a Pattern, or create an empty Pattern and fill it.
To convert an existing Part into a Pattern, [Right]/[Ctrl]-click on the desired Part and select Convert Part to Pattern from the Instrument
Parts menu. This operation is also found in the Event menu. Studio One determines whether the Pattern should use Melodic Mode or
Drum Mode based on the Instrument, and the Part becomes a Pattern at that spot in the timeline. The maximum Pattern length is 64
Steps, so anything beyond that is truncated during the conversion.
After editing the Pattern as described below, you can convert it back into a Part using the same method: [Right]/[Ctrl]-click the Pattern in
the timeline and select Convert Pattern to Part, or select the operation from the Event menu.
To create an empty Pattern, select an Instrument Track, and navigate to Event/Insert Pattern or press [Ctrl]/[Cmd]+[Shift]+[P] on the
keyboard. An empty Pattern is created on the selected track.

## Patterns

To begin working with the new Pattern, click to select it. You can then view it in the Note Editor pane.
If you plan use this pattern to create melodic or harmonic content, select Melodic Mode by clicking the keyboard-shaped button shown
above. For drums or other rhythmic parts, click the drumpad-shaped button.
Setting Pattern Length, Resolution, and Other Global Details
When you first create a Pattern its default state is 16 Steps in length, with 1/16th-note Resolution. This and other details can be easily
changed using the parameters above the Pattern Editor window:
Steps Sets the length of the Pattern, in steps. Each step is as long as the note value specified in the Resolution selector. Click the tri-
angle to open a menu of preset lengths. To enter a custom length, click the step number and type in the desired value between 2 and 64
Steps.
Resolution Sets the note value of each step in the Pattern. Defaults to 1/16th-notes, with a range between 1/2-notes and 1/64th-notes,
with triplet ("T") and dotted ("D") variants of each.
Swing Sets the rhythmic relationship of each pair of steps. Defaults to 0%, with each note falling on even divisions. As you increase the
percentage, the second step of each pair (2, 4, 6, and so on) is moved closer to the note to its right.
Gate Sets the length of each note. Defaults to 100%, with each note filling the entirety of its note value. As you decrease the value, each
note becomes shorter and shorter. Values higher than 100% lengthen each note, with a maximum value of 200%. Note that changing the
Gate value of a tied note only affects the duration of the final tied step. For example, a Gate value of 200% applied to two tied 16th-notes
results in a 1/16th note tied to an 1/8th note. Conversely, for this example a Gate value of 50% results in a 1/16th note tied to a 1/32nd
note.
Accent Sets the amount of emphasis placed on Accented notes. Defaults to 30%. As values increase, the effects of Accent increase.
Entering Notes
One easy way to begin fleshing out a pattern is to use the Pencil Tool. Click on a place in the grid to add a note. Click a note again to
erase it. Hold [Shift] while erasing to erase notes on multiple lanes or pitches. You can also click and drag across a row to add multiple
notes in Drum Mode or set the note length in melodic mode in one gesture. Hold [Ctrl]/[Cmd] to enter or toggle the accent.
Tied Notes and Chords
To enter a tied note, hold [Shift] and drag across two or more steps. Use this method to shorten a note, too: hold [Shift] and drag to the left
across a long note until it occupies the desired number of steps. [Shift]-drag to the left inside the first step to reset a long note to a single
step.
When several notes of the same length occupy the same step in Melodic Mode, they are a Chord. To make a Chord longer or shorter,
hold [Ctrl]/[Cmd] + [Shift] and drag to the right or left across one of the notes.
Step Recording

## Patterns

Another way to add notes to a pattern is Step Recording. When you press the Step Record button, shown above on the left, you enter
Step Recording mode. To choose where in the Pattern to begin entering notes, click the step number above the desired column in the
grid. Play a note on a connected MIDI controller, and it is entered into the Pattern. You can play other notes while the first note is held to
enter multiple notes on a single step. When you let go of the notes, the Pattern advances to the next step, and you can enter the next
note or Chord.
Rests and Tied Notes / Chords
To insert a rest, click the double-arrow "Insert Rest" button to the right of the Step Record button. To enter a tied note or Chord, click the
Insert Rest button before releasing the note(s).
When you're finished Step Recording, press the Step Record button again to go back to the standard mode.
Real-time Recording into a Pattern
At times you may prefer to enter a basic idea into a Pattern in real time, and then make precision edits to the notes and their durations
using the features of Pattern mode. Studio One can do this, too.
1.
Create a pattern
2.
Drag across the Ruler and set the loop boundaries to match the Pattern
3.
Enable Loop mode
4.
Press [F2] to open the Pattern Editor
5.
Enable the Record / Step Record button inside the Pattern Editor window
6.
Press Play (or use the space bar) to start the Transport
7.
Play notes on your controller as the Pattern loops.
This method can also be used to record notes into a pattern variation in real time.
Switching Between Patterns on the Timeline
When editing a Pattern, if you'd like to edit another pattern that precedes or follows it on the timeline, click one of the Edit Previous Pat-
tern / Edit Next Pattern buttons (pictured above) to switch between them.

## Patterns

Pattern Editing Operations
When you [Right]/[Ctrl]-click in the Pattern Editor a list of editing operations is shown in a pop-up menu. The size of the list is different for
Melodic Mode and Drum Mode.
-
Melodic Mode: These pattern-level operations are also available in Drum mode.
-
Copy Copies the entire contents of the current Pattern so that it can be pasted into another Pattern, or into another Vari-
ation within the same pattern.
-
Paste Applies the note data in the clipboard to the currently selected Pattern.
-
Duplicate Copies notes from the first half of a Pattern and pastes them onto the second half, but only if there are no
notes there already. To visualize this, enter a note on step 1 of an empty Pattern and Duplicate (use [D] as a shortcut).
Step 1 is duplicated to step 5. Add a note to step 7 and press [D] again: steps 1, 5, and 7 appear at steps 9, 13, and 15.
This is an easy way to populate a pattern with repeating Chords or hi-hat notes, for example.
-
Clear Pattern Removes all notes from the Pattern.
-
Double Resolution Doubles the resolution of the Pattern. This increases the number of steps that exist in the space of
a 1/4-note, resulting in a decrease in the note value of each step. For example, if the default resolution of 1/16 is
doubled, the note value of each step becomes 1/32. Note that the Pattern now runs twice as fast relative to tempo. Stu-
dio Onecompensates by doubling the number of steps in the Pattern, up to the maximum of 64 steps.
-
Half Resolution Reduces the Pattern resolution by half. This decreases the number of steps that exist in the space of a
1/4-note, resulting in an increase in the note value of each step. For example, if the default resolution of 1/16 is cut in
half, the note value of each step becomes 1/8. Note that the Pattern now runs half as fast relative to tempo. Studio
Onecompensates by reducing the number of steps in the Pattern by half.
-
Drum Mode: Listed below are the Selected Lane operations. The Pattern operations are the same ones listed above.
-
Copy LaneCopies the note information in the currently selected lane. To apply it to another lane, select the lane, then
[Right]/[Ctrl]-click and choose Paste.

## Patterns

-
Paste Applies the note data in the clipboard to the currently selected lane.
-
Duplicate Steps Copies the contents of the selected lane and pastes them into place in the next available open space.
-
Fill Lane Adds notes to every available step in the currently selected lane.
-
Set Every 2nd Step / 4th Step Adds notes to every 2nd or 4th step in the currently selected lane, per the selected oper-
ation. This replaces any existing steps. Notes can be added or erased as needed. Use the Shift Lane feature to move
the new steps to the offbeat if you like.
-
Shift Lane Shifts the notes of the currently selected lane to the right by one step. This is a great way to discover unex-
pected rhythms! Do this enough times and the notes re-appear on the left side. Note that tied notes only re-appear once
the entire note value has shifted beyond the end of the Pattern.
-
Clear Lane Removes all notes from the selected lane. [Delete] or [Backspace] can also be used; just be sure you've
selected the lane first.
-
Double Lane Resolution Doubles the resolution of the lane. This increases the number of steps that exist in the space
of a 1/4-note, resulting in a decrease in the note value of each step. For example, if the default resolution of 1/16 is
doubled, the note value of each step becomes 1/32. Note that a lane now runs twice as fast relative to the other lanes.
-
Half Lane Resolution Reduces the lane resolution by half. This decreases the number of steps that exist in the space
of a 1/4-note, resulting in an increase in the note value of each step. For example, if the default resolution of 1/16 is cut
in half, the note value of each step becomes 1/8. Note that the lane now runs half as fast relative to the other lanes.
The tool bar above the Pattern Editor window has shortcut buttons for many of the Drum Mode operations previously described (Set
Every 4th Step, Set Every 2nd Step, Fill Lane, Clear Lane, and Shift Lane). These add even more options to enhance your workflow.
They look like this:
Drum Maps and Names
Drum Mode lets you build and store custom drum maps for later recall. You can name each drum, place them in any order you like, and
hide any drums that aren't being used in the current Pattern. There's also a General MIDI drum map to use as a starting point, if you like.
It all starts with pressing the wrench-shaped Edit button in the Drum Map selection window:
The drum list expands to reveal functions that can only be accessed here. Click a name field and you can name or rename any drum.
To the left of the name fields are three tiny areas that make a big difference:

## Patterns

The gray parallel lines on the left are handles that allow you to click-drag the lanes into any order.
The dots to the right of the lane handles enable and disable the lanes. A disabled lane is hidden when you leave Edit mode.
The vertical bars allow you to select a color for the selected lane.
Once the drums are arranged the way you want, you can save and name your new Drum Map. To do so, click the Pitch Names icon on
the left side of the Drum Map selection window. Seven options are presented:
-
Hide Unused If you only want to see the drums currently used by the Pattern, select this option.
-
Show Default This selects the Drum Map you have stored as the Default Preset.
-
Show All This option reveals the drums the pattern isn't using, as well as the entire MIDI Note range.
-
Reset Order If you've reordered the lanes and want them to be placed according to their MIDI note number, select this option.
-
Remove All This will reset the lane order, clear all name fields, disable every lane, and reset the color selections.
-
Store Preset... Use this to save the current Drum Map for later recall. Give it a name, click OK, and it will appear in the Drum
Map selection menu.
-
Store as Default Preset If there's a Drum Map you like to use as a starting point for other Drum Maps, use this option to des-
ignate it as the Default Preset. This creates a duplicate of the current Drum Map, gives it the name "default", and places it at the
top of the Drum Map selection menu.
The Drum Map selection menu is available both outside and inside Drum Map Edit mode. Simply click the name of the current Drum Map
to see the list and select a new Drum Map, as shown below.

## Patterns

The Pitch Names icon shows a smaller list of options outside of Drum Map Edit mode. They're identical to the first three options that are
shown inside Drum Map Edit mode: Hide Unused, Show Default, and Show All. Please refer to the earlier section to learn what they do.
Drum Mode Lane Options
In Drum Mode you have the option to mute or solo each note individually, using the [M] and [S] buttons on each lane. You can also set a
separate Pattern length and note resolution for each lane. This allows for intricate polyrhythms and a greater sense of movement over
time. To change the pattern length for a specific lane, click the current value and enter the value of your choice. To change note res-
olution, click the current value and choose a new value from the pop-up menu.

## Patterns

Pattern Inspector
If you open the Inspector while editing a Pattern, you see special options and commands that apply to working with Patterns:
Audition Notes Enabling this option causes the notes you enter into your Pattern to play through the connected instrument as you add
them, making it easier to tell whether you're on the right note or instrument.
Editor Follows Cursor Enabling this option causes the Pattern Editor to show whatever pattern is currently being played on the current
Track, as the transport travels along the timeline.
Variations
Each Pattern can hold an unlimited number of Variations. These can contain different note data, and have differing Step lengths and note
resolutions. This lets you try a great many permutations of a Pattern without worrying about disrupting the others. To add an empty Vari-
ation to a pattern, press the plus-symbol button in the Pattern Inspector. To delete a Variation, select it and press the minus-symbol but-
ton in the Inspector. To rename a Variation, click its name and enter the name of your choice. Click-and-drag Variations to change their
order.
At some point you may want to duplicate a Variation to preserve its current state while editing its clone. To do this, select the Variation to
duplicate and press the Duplicate button (which looks like this:
).
To substitute one of a Pattern's Variations for the version currently sitting on the timeline, select the Pattern and double-click a Variation
in the Inspector, or click the drop-down menu next to the Variation name at the top of the Pattern Editor.
Velocity, Repeats, Delay, and Probability

## Patterns

The more rigid step-based nature of Patterns (as opposed to the more free-flowing note placement of Instrument Tracks) enables some
useful creative features. The per-step automation of parameter values is one of them.
In the bottom-left corner of the Pattern Editor there's a small button that looks like a couple of jagged mountain peaks (
). Click that to
show / hide the Automation Lanes. Along the top of this Automation window are the Velocity, Repeat, Delay, and Probability buttons (and
a mysterious button marked "...").
Velocity Click this button to allow setting of velocity for the notes in the selected lane (in Drum Mode) or for all notes on a given step (in
Melodic Mode). Click and drag in the Velocity lane to set the value.
Repeat Clicking this button lets you specify the number of repeats to apply to each note in the selected lane (in Drum Mode) or to all
notes on a given step (in Melodic Mode). All repeats on a note are spaced equidistantly within the span of the note resolution of the Pat-
tern. So, for example, a value of 4 repeats on a note in a pattern with 1/16th-note resolution results in four 1/64th-notes being played.
Delay This is a great way to humanize a Pattern: Click the Delay button and select a value between +/- 50% for one or more Steps. Pos-
itive values make the Step happen later; negative values make it happen sooner. One caveat: it isn't possible to use a negative delay on
the first step; notes before the start point of the Pattern will not play.
Probability Clicking this button lets you specify the percentage of probability that each note in the selected lane will play (in Drum Mode)
or that all notes on a given step will play (in Melodic Mode). Lower settings cause notes to be canceled in greater numbers, creating inter-
esting variations as the Pattern plays.
Step Automation
Pressing the "..." button lets you access any available automation parameter on a step-wise basis, in the same way you can specify note
Velocity throughout a Pattern. In the pop-up window that appears, select the parameters you wish to edit from the column on the right,
and press the [<< Add] button to add it to the available Step Automation parameters. If you wish to remove a parameter, select it in the
left column, and click the [Remove >>] button.
The parameters you add to the Step Automation system appear as additional buttons alongside the Velocity, Repeat, Delay, and Prob-
ability buttons. Click a parameter to access its settings over the steps of the Pattern.
After selecting the desired automation parameter, note the blue columns along the bottom of the Automation Lane. Each of these rep-
resents a step that can be automated for the selected parameter. You can adjust the columns individually or drag the cursor across the
row and edit many of them in a single gesture. Then select another automation parameter and repeat the process until the Pattern is
exactly the way you want it.
Adding Automation Lanes
To add additional lanes, to allow for more complex work with Step Automation, press the plus-symbol button to the left of the automation
area. To collapse a lane, press the minus-symbol button.
Pattern Management
Patterns are automatically saved with the Song in which they are created. But if you'd like to use a Pattern and its Variations in other
songs, there are two ways to do that.
Store / Load Patterns

## Patterns

Open the Pattern Inspector to reveal the Store Pattern Preset / Load Pattern Preset buttons. To store the Pattern, click the Store button.
The window that opens lets you name the Pattern, describe it, and either select a Subfolder or create a new one by typing a name into
that field.
To load a different Pattern into the current song, click the Load button. A drop-down menu reveals the folder names. Open a folder, select
the desired Pattern, and it appears in the Pattern Editor window.
Drag to / from Browser
Open the Browser and drag-and-drop the Pattern from the Arrange view to the desired folder in the Browser window. Studio One stores
Patterns on the Files tab, but you can drag the Pattern to the Loops tab if you like. Use the [Alt] key to specify whether to export it as a
.pattern file or a .musicloop file. The difference is that a .musicloop file also recalls the instrument and its settings, not just the raw note
data contained by a .pattern file. See Audioloops and Musicloops to learn more.
Whichever format you choose, you can drag-and-drop these files into future songs and re-use them wherever they may be useful.

## Pitch Correction with Melodyne Integration

Studio One features a unique pitch-correction solution: It tightly integrates with Celemony’s Melodyne, a high-quality commercial pitch-
correction software. This is accomplished with new co-developed technology and it is only possible with Studio One. Studio One Pro-
fessional includes a fully licensed copy of Melodyne Essential 5, while Studio One Artist features the Melodyne Trial version. If you
already own any version of Melodyne, update to version 1.3 or later for the integrated support to function in Studio One.
For deeper information on using Melodyne, please refer to the Melodyne documentation and to the helpful online materials, such as
tutorial videos and FAQs, found at the Celemony Help Center.
Edit with Melodyne
Any Audio Event can be edited with Melodyne. To do so, select the Event and press [Ctrl]/[Cmd]+[M] on the keyboard, or [Right]/[Ctrl]-
click on an Audio Event and select Edit With Melodyne from the contextual menu. Melodyne is inserted in the Event FX Device Rack for
the Event, and the integrated Melodyne view opens, found in the same location as the Audio and Note Editors.
The audio in the Event is analyzed automatically, and the detected notes are displayed, ready for editing. Note that the Melodyne view
can be maximized and detached in the same way as the Audio and Note Editors.
When the Melodyne Event Effect is active (meaning the Event FX have not been rendered), double-clicking on the Audio Event opens
the Melodyne view. To switch to the Audio Editor, press [F2] on the keyboard, or click on the [Edit] button.

## Pitch Correction with Melodyne Integration

Detection Algorithms
Melodyne offers a selection of detection algorithms to choose from. These let you optimize the detection process to suit the material
you're working with. Melodic mode is best for monophonic melody lines (such as vocals). Percussive mode is best for non-pitched, per-
cussive signals.
Melodyne Essential 5, bundled with Studio One Professional, also offers Universal mode, which lets you perform pitch and rhythm manip-
ulations on polyphonic material (such as guitar or keyboard parts, or whole mixed songs).
You can choose detection modes in the Algorithm menu within the Melodyne editing window.
For more information on the detection algorithms in Melodyne, visit the Celemony Help Center.
Real Time and Render
As with other Event FX, Melodyne runs in real time by default. This allows immediate auditioning of the material being edited alongside
the rest of the mix. However, it is probably best to render the edits once you are finished in order to reclaim CPU resources. To do so,
click on the [Render] button for the Event FX Insert Device Rack in the Event Inspector for the Audio Event.
As with other Event FX, the state prior to rendering is stored, allowing you to return for further editing. Melodyne can also be removed
entirely from the Audio Event by removing it from the Event FX Insert Device Rack for the Event, in which case all edits are lost.
Applying Detected Tempo to the Tempo Track
Melodyne extracts tempo information from the audio you feed it, creating a deatiled "map" of tempo changes over time. The tempo map
can be applied to the Tempo Track in Studio One. By doing this, parts you add in the future can tightly follow this new, fluid tempo, and
the editing tools can easily snap to logical rhythmic subdivisions, even as the tempo changes.
To make a tempo map with Melodyne and apply it to the Tempo Track, do the following:
1.
Set the Arrange view timebase to "Bars."
2.
Ensure that the Inspector panel is visible. To show it, click the "I" button, to the left of the timeline.
3.
Select an audio Event that contains tempo information you wish to detect.
4.
In the Inspector, set Timestretch to "Don't Follow" mode.
5.
Trim the beginning of the Event so that it coincides with the first downbeat in the audio.
6.
Move the Event so that its beginning sits at the first beat of a bar.
7.
Enable Melodyne by navigating to Audio/Edit with Melodyne, or by [Right]/[Ctrl]-clicking the event and choosing Audio/Edit with
Melodyne from the pop-up menu. You can also do this by pressing [Ctrl]/[Cmd]+[M] on your keyboard.
8.
In the Melodyne sub-window that appears, do the following:
a.
Open the Algorithm menu and choose Universal (or one of the Polyphonic modes, if you have purchased and installed
Melodyne Editor or Studio)
b.
Click the "Note Assignment Mode" button, and click the "Tempo Options" button to show the tempo map.
c.
Verify that the detected time signature and tempo seem accurate (and edit them, if necessary).
d.
Click and drag the first beat marker in the tempo map (marked "1") to align it with the first downbeat of your audio.
e.
Click the "Edit Mode" button to close the tempo map. This embeds the detected tempo information in your audio Event.
9.
In the Arrange view in Studio One, drag your Event into the Tempo Track to apply the detected tempo to your Song.
For more information on the tempo features in Melodyne, visit the Celemony Help Center.
Drag Audio to Instrument Track
When an Audio Event is edited with Melodyne, the notes resulting from analysis appear on the waveform, as with Music Loops. In this
state, it is possible to drag the Audio Event to an Instrument Track lane in the Arrangement to extract the notes, resulting in an Instrument
Part that perfectly matches the audio performance. The notes and velocity for the Instrument Part are derived from the Melodyne ana-
lysis and editing.
This makes it possible, for instance, to sing a melody and then drag it to an Instrument Track for a virtual instrument to play, rather than
trying to figure out how to play it on a keyboard controller. You might also wish to replace or enhance an acoustic instrument performance
with a virtual instrument. These techniques and many more are now possible with a single drag-and-drop.
Undo History
The Undo History menu, accessed under Edit/History, enables you to view and step through virtually every editing or mixing function that
has occurred since a document was opened. Simply click on any edit in the list to instantly roll the document back to the point where that
Undo History

edit was made.
Note that the history is cleared when a document is closed but remains intact when the document is saved and kept open.
Navigating with Zoom
When editing or arranging in a Song, zooming in and out on the timeline can be beneficial in both the Edit and Arrange views. Studio
One’s key commands and quick control methods make zooming quick and easy.
You can zoom using the following techniques:
Zoom Horizontally
-
Zoom In or Out Click and drag vertically in the Arrange or Edit view timeline.
-
Zoom In or Out Position cursor in Arrange or Edit timeline and move mouse scrollwheel.
-
Zoom In Press [E] on the keyboard.
-
Zoom Out Press [W].
Zoom Vertically
-
Zoom In (vertically) Press [Shift]+[E].
-
Zoom Out (vertically) Press [Shift]+[W].
-
Zoom In or Out [Ctrl] + mouse scrollwheel.
Other Zoom Commands
-
Zoom to Loop Press [Shift]+[L].
-
Zoom to Selection Toggle (horizontally and vertically) Press [Shift]+[S].
-
Zoom to Selection Toggle (horizontally) Press [Alt]+[S].
-
Zoom by Selecting Hold [Alt]+[Shift], then draw a selection across the Arrange view to zoom in fully to that range. To return to
normal zoom level, hold [Alt]+[Shift] and click in the zoomed area.
-
Zoom Full Press [Alt]+[Z] to zoom out horizontally, as much as possible.
It is also possible to set key commands to directly access the Track Heights available on the Arrange page in the Keyboard Shortcuts
menu.
Zoom History
The most recent horizontal and vertical zoom states in an arrangement or editor are remembered in the Zoom History. You can go back
to the previous state using Undo Zoom [Alt]+[W] and can move forward with Redo Zoom [Alt]+[E].
Toggle Zoom
You can quickly toggle between two zoom states with the Toggle Zoom command [Z]. This command swaps the current zoom state with
a stored zoom setting. The current state is stored, and the state in memory is restored. Pressing [Z] again takes you back to the original
state.
The Store Zoom State command [Shift]+[Z] only stores the current state and does not switch states. This can be used to set an anchor
zoom position that you want to recall later with the Toggle Zoom command [Z].
Auto Zoom
Auto Zoom allows Studio One to automatically apply an optimal Zoom to fit all content of the corresponding view in real-time. Auto Zoom
can dramatically speed up your workflow! It’s available in the Arranger, Audio Editor, and the Piano View and Note View of the Note
Editor.
Any manual window resizing operation that affects a View using Auto Zoom (like resizing the Browser) will dynamically re-zoom the View
in real-time. Adding, duplicating, or deleting Note or Audio Events can also trigger Auto Zoom.
Note that using a manual Zoom command, like a keyboard shortcut or mouse controls, will disable Auto Zoom. Also, Synchronize Editor
to Arrangement and Auto Zoom can't be enabled at the same time.
 Navigating with Zoom

Right-click the Auto Zoom button to choose from the following options:
Vertical Auto Zoom will dynamically zoom vertically as Events are added or removed, keeping all Events visible simultaneously. Avail-
able in Arranger and Note Editor. Manually resizing the Console vertically will dynamically re-zoom the Arranger in real-time.
Horizontal Auto Zoom will dynamically zoom horizontally to fit all Events, Parts, and even your Loop (when enabled.) Stretching or
duplicating Events or Parts will also trigger the auto-zoom so everything fits. Available in Arranger, Note Editor, and Audio Editor
Auto Zoom Full will perform both Horizontal and Vertical Auto Zoom at the same time Available in Arranger and Note Editor.

## Macro Toolbar

The Macro Toolbar is a special control panel that lets you customize your workflow in powerful ways, giving you easy access to often-
used functions and custom command combinations. You can add and change command groups and buttons freely to fit your needs.
Macros are grouped into Pages of related commands. To view the available Pages, click the menu arrow next to the name of the current
Page on the left side of the Macro toolbar. Then make a selection from the menu.
You can create Macros, which string together multiple commands to form a single action. For instance, you might want a quick way to
select multiple events across multiple tracks within the loop range and merge them to form single continuous events. This would normally
involve a number of separate actions, either with the mouse or keyboard, but creating a Macro for this reduces the process to a single
action.

## Macro Toolbar

Independent Macro Toolbars are available for the Arrangement, Note Editor, and Audio Editor views. You can show or hide the Macro
Toolbar for any of the views by clicking the appropriate Macros button or by navigating to View/Additional Views/Macros.
Overview
When you open a Song in Studio One, the Macro Toolbar button is shown next to the Audio Bend, Strip Silence, and Quantize panel but-
tons in the top toolbar. Click this button to expand the Macro Toolbar panel, which is docked to the top panel by default. However, it can
be detached like the other panels by clicking on the detach button to the far right of the panel. When detached, [Right]/[Control]+click in
the panel to adjust for vertical or horizontal orientation.
Several items are in the Toolbar by default for demonstration purposes. Note that any button can be moved or removed, as well as any
entire group of buttons. This toolbar is completely customizable.
To see how Macros are put together, click the gear icon next to the Page name and select Macro Organizer. You can also navigate to Stu-
dio One/Macro Organizer.
From here, you can explore your Macros, create new ones, and edit existing ones. Use the search bar to quickly find the desired Macro
or browse from the list. Click on any of the list headings to sort the Macro list by the desired category.
Select "Select Parts in Between Selection" from the list and then click the Edit button.

## Macro Toolbar

This is the Edit Macro window where you can create and modify your Macros. On the left is the Commands list, which lists all available
commands in Studio One. On the right are the Macro Title, Group, and list of commands that the Macro performs when triggered. Com-
mands are executed in the order in which they are listed here. So, this Macro selects all events, splits them at the left and right locator loc-
ations, then merges the events that are still selected (those within the loop range, in this case).
Close the Edit Macro and Macro Organizer windows and look again at the Macro Toolbar. Click on the Action button in the Edit group,
and a list of all of your Macros is displayed, categorized by the Groups you entered in the Group field for each Macro in the Edit Macro
window. Clicking on any item in this list performs the associated Macro.
Click on the Name button in the Edit group to rename any selected events. The list of predefined names can be customized by clicking on
Edit Names in the Edit group to open the file 'EventNames.txt', which uses a simple syntax to build the menu hierarchy.

## Macro Toolbar

## Macro Toolbar

Customize the Toolbar
It is possible to add new Groups and Buttons to the Toolbar, as well as remove or modify any existing item. [Right]/[Option] + click on the
Edit group in the Toolbar, and a contextual menu is displayed.
Double-click on the name to rename the Group. The Compact toggle makes the interface use as little horizontal space as possible when
engaged. Click on Remove Group to completely remove the Group and all Buttons it contains. Click on New Group, New Menu Button, or
New Button to create one of those items. Groups are named Group by default, and are renamed in the [Right]/[Option]+click contextual
menu by double-clicking on the name. New Buttons are blank but can be named and edited, which is described below.
Modify a Macro Button
[Right]/Option]+click on a Button and choose one of your Macros from the top level list, or navigate to Assign/Assign Command to select
a Key Command to associate with the button. You can associate any Macro or command to a button, or create a new Macro from this
menu.
Buttons can also make use of custom icons. [Right]/Option]+click on a Button and click Icon/Select Image, then choose any 22x22 pixel
PNG image file to use a custom icon.

## Macro Toolbar

Rearrange Buttons and Groups
Buttons and groups of buttons can be placed in any order on the Toolbar. Hold [Ctrl]/[Cmd] and click-drag a Button to the desired loc-
ation, even into another Group. To move an entire Group, hold [Ctrl]/[Cmd] and click-drag on the Group name to move it to the new loc-
ation.
Macro Menu Buttons
These buttons help you to collect and organize your Macros. They can hold many Macros and Submenus of their own, which the menu
arrows reveal. To give the Macro Menu button a name, [Right]/Option]+click the button and select Edit Menu. Then double-click the grey
bar at the top to enter a name.
To add items to the Menu button, [Right]/Option]+click the darker area under the name. This presents three choices:
-
New Menu Item This one adds an empty Menu Item. [Right]/Option]+click the new item and use it like a Macro button: Assign a
Command, an existing Macro, or create a new Macro.
-
New Submenu This creates another menu inside the Menu button. It can do everything a higher-level Menu can do.
-
New Separator This adds a line that can be clicked and dragged anywhere inside the Menu, which can help you find specific
items more easily.
Items inside a Macro Menu can be reordered: just click-drag the items until they are in the desired order.
Make a New Macro
There are two ways to make your own Macro; the first was described above. The second way is to open the Macro Organizer window by
selecting it from the gear menu next to the Page name in the Macro Toolbar, or by navigating to Studio One/Macro Organizer Click on
New to open the Edit Macro window. Give your Macro a Title, which is how it appears in any menu, as well as a Group Name, which
determines how it is organized in the previously mentioned Action list of the Macro Toolbar.
Next, navigate the list on the left to find the first command for your Macro, select it, and then click on Add to add the command to the list
on the right. Repeat this until each command you need is in the list. Note that the commands are performed in the order they are listed, so
be sure the order is set up to achieve the desired result. Select any item in the list and click on Up or Down to move the item in the list.
Arguments
Note that some commands have Arguments associated with them, such as Track|Expand Layers. Commands with Arguments show an
Argument descriptor next to the command in the command list. Arguments provide a specific behavior for commands where multiple
behaviors are possible.
With the Track|Expand Layers command, the Argument 'Expand' should be set to 0 or 1. Setting the Argument to 0 disengages the
Expand Layers option, whereas setting it to 1 engages the option.

## Macro Toolbar

Some commands can have multiple arguments. For instance, Edit Volume has 'Level' and 'Relative' as separate arguments, where
'Level' is a dB value and 'Relative' can be "0" or "1" to either set the event volume to the absolute dB value or to add/subtract it from the
current level.
Edit a Macro
If a Macro needs to be modified, [Right]/[Ctrl]-click on its button in the Macro Toolbar and select Edit Macro from the menu. This will open
the Edit Macro window as described above. Note that some Macro buttons are built-in commands that cannot be altered, so the Edit
Macro window is not available for them.
Duplicate a Macro
There's a quick way to duplicate a Macro. This can be useful if you want to keep an existing Macro the way it is, but also need another
that has a few modifications.
To do this, [Right]/[Ctrl]-click on the button and select Duplicate Macro from the menu. A new Macro button will appear next to the first
one, ready to be edited and named. Note that the Macro buttons for built-in commands do not offer the Duplicate Macro menu option.
Make a Key Command for your Macro
Key commands can be associated with your Macros, just like any command in Studio One. From the Macro Editor, choose your desired
Macro and click “Shortcut” (or double-clicking on the “shortcut” column) to jump to the Keyboard Shortcuts menu. Your chosen Macro will
be automatically selected; enter the desired keystroke(s) in the “Enter Key” field and click Assign, then OK.
Alternatively, open the Studio One/Keyboard Shortcuts... window and type "macros" in the search field to quickly show the Macros sec-
tion. Select any Macro from the list and assign a key command by typing into the Enter Key field and clicking on Assign.

## Macro Toolbar

Map Macros to your MIDI Hardware
As with any command in Studio One, Macros can be mapped to your MIDI hardware. To do this, open the device map for the hardware
you want to map macros by double-clicking on the device in the External panel of the Console. While any control you have learned for the
device can be mapped, buttons are the most logical choice. [Right]/[Option]+click on any button in the map and choose Assign Com-
mand.
Type macros in the search field to quickly find your Macros, select the one you want, and click on OK. Note that even control surfaces
that are not natively supported can have commands assigned, so long as the desired controls transmit MIDI CC values.
Macro Storage
Your individual Macro commands are stored in a single location, reached via the [Show Macros Folder in Explorer/Finder] button at the
bottom of the Macro Organizer window. Each Macro is a unique file in XML format, and it is possible to edit the XML directly if desired.
These files are also portable, so you can share them with other users via the PreSonus Exchange.
Macro Settings
Click the gear icon on the top left of the Macro Toolbar to open the Macro Settings menu.

## Macro Toolbar

-
Go to… Choose from the list of Macro Toolbar Pages to open the desired one.
-
New Group Choose to create a new Group of Macros to the Macro Toolbar.
-
New Page Choose to create a new, empty page for you to populate with Macro Groups.
-
Rename Page Choose to rename the current page.
-
Import… Import a Macro Page from outside Studio One
-
Export… Export the current Macro Page to share with others.
-
Macro Organizer Opens the Macro Organizer.
-
Reset Toolbar Resets ALL Macro Pages to their default settings. Use with caution.
Editing Suggestions
Making Clean Edits
In audio production, the editing process can be unforgiving. Small inaccuracies when splitting, moving, or performing other actions on
recorded audio can lead to unwanted audible artifacts. The following describes some recommended editing practices.
Listen While Editing
Listening to your edits as you make them saves time and frustration in nearly every case. For instance, when sizing the edges of a vocal
part to remove unwanted sounds between words, it is tempting to make edits based on the graphic representation of the waveform.
Sometimes that works, but even when you edit visually, it is a good idea to loop the section you are editing and listen as you size the
Events to be sure you are not removing a critical part of the vocals.
To quickly loop a precise selection, select a range with the Range tool, and then press [Shift]+[P] on the keyboard to set the Left and
Right Locators precisely around that range. Then, click on the Loop button in the Transport, or press [Num Pad /] on the keyboard, to loop
the playback over the selected range.
You can also use the Listen tool to quickly solo and listen to any element in the arrangement.
Eliminating Audible Artifacts
In Studio One, we make every effort to streamline the editing process and avoid tedious tasks. For instance, we apply fades auto-
matically to punch-in recordings to be sure the new audio blends seamlessly with the existing audio. However, inevitably, there can be
cases when editing audio leads to audible artifacts. These artifacts may sound like short clicks or ticks of noise, and they usually occur at
the beginning or end of an audio Event that has been split or cut. When this happens, use the fade envelope provided on every Audio
Event to apply a quick fade-in or fade-out, experimenting until the artifact can no longer be heard.
Editing Suggestions
