# Automation

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 370–378
> **Slug:** `14-automation`

**Agent topics:** `automation envelopes`, `automation modes`, `instrument part automation`

---

Automation
Automation is a critical part of modern mixing. The following chapter discusses aspects of automation in Studio One, including Track and
Part automation, automation modes, and automation envelopes.

## What is Automation?

Automation lets you record changes in parameter values; thereafter, Studio One can perform these value changes for you. For instance,
you can record level changes in a Track by capturing your fader movements during playback; from then on, Studio One can perform the
level changes.
Before the advent of automation, mixing was very much a performance. Sometimes it took many pairs of hands on the mixing console to
accomplish all of the fader, mute, solo, and other movements to achieve a mix. Automation makes it possible to record the mixing per-
formance in any way you desire and endlessly tweak every parameter until the desired mix is achieved.
In Studio One, automation is recorded in automation envelopes, which are a series of data points connected by lines that represent the
changing values of the parameter being automated.

## Automation Types

Nearly every parameter in Studio One can be automated. Several ways to automate parameters are provided, including Track auto-
mation, Automation Tracks, and Part automation. The following sections describe these automation types.
Track Automation
Track automation allows you to automate any parameter related to an Audio or Instrument Track and the Events it contains. Automation
can be viewed via the Show Automation button at the top of the Track Column in the Arrange view or by [Right]/[Ctrl]-clicking on a Track
and selecting Expand Envelopes. Note that for Instrument Tracks (which do not have automation enabled on any parameters by default),
Expand Envelopes does not show automation unless one or more parameters have been enabled for automation.
Note that automation envelopes on Instrument Tracks control the parameters of the virtual instrument to which the Instrument Track is
routed. All other aspects of Instrument Track automation envelopes work in the same way as with Audio Track automation.
Automation Envelopes On the Track
To view automation envelopes one at a time, superimposed on top of Events on the Track, Press [A] on the keyboard or click on the
Show Automation button at the top of the Track column in the Arrange view. With this engaged, the Track column of the Arrange view
changes to reveal automation parameters, including an On/Off button, the parameter name for the currently shown Envelope, and auto-
mation mode selection.
Click on the Automation Parameter display, which is labeled “Display: Off” by default, to reveal the available automation envelopes for a
Track (“Display: Off” indicates that the Events on the Track are displayed, instead of an automation envelope). Volume and Pan auto-
mation envelopes are available by default on every Audio Track. Select a parameter from the list to view and edit the automation envel-
ope, or click on Add/Remove to open the Automation dialog for the Track.
 Automation

Automation Envelopes In Lanes
To view multiple automation envelopes at once, with each in a lane under the Track, [Right]/[Ctrl]-click on a Track and select Expand
Envelopes. Alternatively, you can click the drop-down arrows for a Track in the Track List to expose its automation envelopes in the same
way. To hide the automation envelopes, deselect Expand Envelopes in the Track contextual menu.
Turn Automation On/Off
Automation envelopes can be turned on and off, so you can decide when they affect the controlled parameter. To turn an envelope on or
off, click on the On/Off button for that Envelope. Each automation envelope can be turned on/off independently. Turning an automation
envelope on/off during playback has different results depending on the current Automation Mode for the Track.
Add Automation Envelopes to a Track
Any number of automation envelopes can be added to a Track. The fastest way to add an automation envelope to a Track is as follows:
1.
Modify any parameter for an Track or its Inserts or Sends, and that parameter is displayed in the Software Parameter window in
far left of the Arrange view toolbar in the Song window.
2.
Click on the Hand icon in the Software Parameter window, and drag it to the Track to add an automation envelope for that para-
meter to the Track. If the envelope already exists, it is displayed, and a new envelope is not added.
An alternative way to add automation envelopes to a Track is described as follows.
1.
Press [A] on the keyboard to show automation.
2.
Click on the Parameter window on the Track in the Track column of the Arrange view and select Add/Remove from the list. This
opens the Automation dialog for that Track.
3.
On the left side of the Automation dialog, the existing automation envelopes are listed, along with their associated automation
mode and device. On the right side of this dialog are the parameters for which new automation envelopes can be added.
4.
Select any parameter on the right and click on Add to create a new automation envelope. Click on any parameter on the left and
click on Remove to remove the existing automation envelope.
At the top of the Automation dialog, you can browse through all Tracks in your Song to view and edit the automation envelopes for any
Track. You can also click on the Add Automation Track button to add a new Automation Track.
Automation Tracks
Studio One features a Track type dedicated to automation that only contains automation envelopes. An Automation Track can contain
automation envelopes related to any Track and any plug-ins. To add an Automation Track, press [T] on the keyboard to open the Add
Track dialog, and select Automation. Note that at least one envelope on Automation Tracks is always visible, and the envelopes can be
viewed on the Track itself or in lanes, just as with the other Track types.

## Automation Types

Only those parameters for which an automation envelope does not already exist are available for automation. However, you can drag
and drop an automation envelope from any other Track to an Automation Track. All other aspects of Automation Track automation envel-
opes work in the same way as with Track automation.
You can use Automation Tracks to automate Bus, FX, and Output Channel parameters and Inserts and to keep critical automation envel-
opes organized in one place and easily accessible.
Clicking the Show Automation option (or pressing [A] on the keyboard) toggles the visibility of Automation Tracks on and off, along with
automation lanes associated with audio and instrument Tracks.
Editing Automation Envelopes
Automation envelopes can be edited directly, using the mouse, as well as with external hardware controllers. The following section
describes editing automation envelopes with the mouse. Refer to the Automation with Hardware Controllers section of the Control
Link chapter for more on editing envelopes with external hardware controllers.
To edit an automation envelope, you first need to show automation by clicking on the Show Automation button at the top of the Track
column or by choosing Expand from the Track contextual menu. A Track must also be selected in order for the automation envelope
points to appear.
Arrow Tool
Editing an automation envelope with the Arrow tool lets you add new points to the envelope, move existing points, and select and delete
existing points. Be sure to select the Arrow tool in the Arrange view before attempting the following processes.
Add a New Automation Point
To add a new point to an automation envelope using the Arrow tool, float the mouse above the envelope in the Track Lane so that the
Hand cursor appears. Click-and-drag the envelope to create a new point and move it to your desired position.
Move an Automation Point
To move any point on an automation envelope, use the Arrow tool to click-and-hold any existing point on the envelope. While holding,
moving the selected point vertically changes its parameter value, and moving the point horizontally changes its time position. Hold [Ctrl]/
[Cmd] while dragging an automation point to lock the time (horizontal movement) or value (vertical movement), depending on the dis-
tance from the point.
Automation points can also be nudged left and right on the timeline by holding [Alt]/[Option] and using the left and right arrow keys. It is
also possible to float the Arrow tool over an envelope point and then hold [Alt]/[Option] and scroll the mouse wheel up or down to increase
or decrease the value of the point (that is, move it along the vertical axis).
To make very precise automation moves, hold down [Shift] while moving an automation point. This moves the point at a slower rate than
normal as you move the mouse, enabling finer control.
When moving an automation point, notice the pop-up value indicator.
 Editing Automation Envelopes

This displays the current parameter value. The range and the type of value depend on the parameter being automated and on the current
time value displayed in the Timebase selected in the Arrange view.
[Right]/[Ctrl]-click on any automation point to bring up the contextual menu, where the point value and envelope color can be changed.
In Studio One, you can drag an automation point as far beyond the position of other automation points as needed. Moving an automation
point beyond other points on the envelope causes the other points to move as well. The other points being moved are restored to their ori-
ginal positions on the timeline if the point that caused them to be moved is moved back beyond their original positions.
Note that when Audio Events or Instrument Parts are moved, any underlying Track automation is moved along with the Events by
default. To disengage this option, see the Studio One/Options/Advanced (macOS: Preferences/Advanced) menu and uncheck the Auto-
mation Follows Events option.
Change the Segment Curve
When you hover the cursor over an Automation segment between two points, a curve handle appears on the white line. Click-and-drag
the handle up or down to shape the curve of that segment. For more precision control, [Right]-click the handle to access a contextual
menu that will let you enter the desired curve value and type of your choice.
Delete an Automation Point
To delete an existing point on an automation envelope using the Arrow tool, first click on a point to select it. Then, press [Delete] on the
keyboard to delete the point. Alternatively, [Right]/[Ctrl]-click on any automation point and select Delete from the pop-up menu to delete
it.
Editing Multiple Points at Once
It is possible to simultaneously edit any number of points on an automation envelope. Using the Arrow tool, click in the Track Lane, away
from any existing automation point, and then drag to draw a selection box around the points you want to edit. You can also hold [Alt]/
[Option] and click in empty space, or directly on a point, to select all points on the envelope from that point in time forward.
With multiple points selected, click-and-drag, using the Arrow tool, on any of the selected points, in order to move them all. Moving mul-
tiple points vertically to adjust the parameter values adjusts each parameter value relative to the point being moved.
Paint Tool
Editing an automation envelope with the Paint tool allows you to draw many automation points with a single move of the mouse, effect-
ively painting an envelope. However, a single click with the Paint tool adds a single point. The paint tool offers various automation editing
options to fit a wide range of applications:
 Editing Automation Envelopes

-
Freehand lets you automate effects in a freeform way. You can create automated shapes with or without the snap to grid func-
tion enabled.
-
With the Line tool enabled, it is easy to create precise and perfectly straight automation lines, be it horizontal, vertically ascend-
ing or vertically descending.
-
The Parabola tool can be used to create gradual ascending or descending automation curves. The intensity of the curve will
depend on how much time there is between the starting and end points of the automation.
-
The Square, Triangle, Saw, and Sine tools make it easy to include classic synthesizer waveform shapes to your automation
envelope.
You can choose from several figures when using the Paint tool, or you can use the Transform editor, as described in the following sub-
sections. Be sure to Show Automation and select the Paint tool in the Arrange view before attempting the following processes.
Draw an Automation Envelope
To draw an automation envelope using the Paint tool, click-and-drag in the Track Lane. While you are drawing the envelope horizontally,
points are added at different time increments based on the current Timebase. However, when the mouse button is released after drawing
an envelope with the Paint tool, the drawn curves of the envelope are intelligently and accurately approximated to achieve the desired
result with as few points as possible, which may or may not remove some unnecessary points from the envelope. If Snap is engaged in
the Arrange view, the envelope points being drawn snap to the grid accordingly.
Drawing an envelope with the Paint tool over existing points on an automation envelope causes the existing points to be overwritten with
the newly drawn points. These actions can be undone and redone.
Draw with Figures
With your cursor over the Paint tool, scroll the mouse wheel to reveal several figure-drawing tools, including Freehand, Line, Parabola,
Square, Triangle, Saw, and Sine waveform tools. With any of these tools selected, click-and-drag on any automation envelope to draw
the desired envelope. When using the waveform tools, you can hold [Alt] to adjust the frequency of the waveform while dragging, or hold
[Ctrl] to vary waveform phase (amplitude and polarity). Hold [Ctrl]/[Cmd]+[Alt] while dragging, to move the currently defined automation
shape left or right along the timeline.
Transform Automation
 Editing Automation Envelopes

You can choose the Transform tool from the Paint tool drop-down list to alter existing automation, or add new automation. With the Trans-
form tool selected, click-and-drag a selection box around any area of an automation envelope; then adjust the selection box by clicking-
and-dragging one of eight handles (four sides and four corners) to scale the selected automation points.
As a shortcut, you can select a range of automation with the Range tool, and press [Alt]+[T] on the keyboard to automatically create a
Transform selection over the chosen range.
Range Tool
You can use the Range tool to quickly trim select ranges of automation up or down in value. This can be done in two ways.
Trimming a Selected Range of Automation
If you want to trim a certain range of automation data up or down, select a range of automation with the Range tool. Then, hover the
cursor in the upper half of the selected range, until the cursor changes into the Trim Tool. Click-and-drag up or down to trim the selected
automation.
Trimming a Segment of Automation
 Editing Automation Envelopes

If you want to trim a certain segment of automation (the span between two points) up or down, select the Range tool, and hover the
cursor in the upper half of the automation lane, above the segment of your choice, until the cursor changes into the Trim Tool. Click-and-
drag up or down to trim your chosen automation segment.
Duplicating Automation
Automation data can be copied and pasted by selecting a range of Automation curves and pressing [D] to Duplicate, or by pressing
[CTRL+C] to copy and [CTRL+V] to paste. In a paste operation, the data will be pasted on the currently-selected track starting from the
point of the play head. You can copy the automation parameters of an Insert Effect when copying the Effect by holding [Alt/Option] while
dragging the Insert Effect to another track.
Remove Track Automation
To strip all automation from a Track, [Right]/[Ctrl]-click the track in the Arrange view, and select Remove Track Automation from the pop-
up menu. Any previously created automation lanes remain, but all written automation data on the Track is purged.

## Automation Modes

In Studio One, automation modes are specific to devices on each Track. A delay effect on an Audio Track might be in Touch mode, while
the volume, pan, and other effects on that Track are in different modes. This allows a great deal of flexibility.
With Show Automation selected, the current automation mode is visible. To select any mode, click on the Automation Mode window and
select from the list. The following describes the automation modes.
Auto: Off
When Auto: Off is selected in the Automation Mode window, all automation for the current parameter and for all related parameters are
turned off.
For instance, if you are currently viewing the Attack envelope for a compressor inserted on an Audio Track, and you select Auto:Off, all
parameter automation for the compressor is turned off. However, automation envelopes for parameters that do not belong to the com-
pressor can still use a different automation mode.
This is not the same as turning an individual automation envelope on and off, as described in the Turn Automation On/Off section of
this chapter, as that on/off button only affects the currently visible automation envelope.
Read
When you select Read in the Automation Mode window, any existing automation envelopes on the Track for the related device is read,
and these envelopes control their related parameters. Read mode is automatically engaged when you draw a new automation envelope
with the mouse.
-
Press [J] on the keyboard to switch to Read Automation Mode manually on the selected Tracks.
Touch
When Touch is selected in the Automation Mode window, automation envelopes can be affected by touch-sensitive, external hardware
controllers, so that new automation is written when a hardware control is touched, and automation is read when the hardware control is
not being touched. This allows the user to manipulate the control at any time in order to write new automation or overwrite existing auto-
mation. Studio One resumes reading automation when the control is released.
-
Press [K] on the keyboard to switch to Touch mode manually on the selected Tracks.
Touch mode can be used even if your hardware controller does not have touch sensitivity. In this case, automation is written when you
move the hardware controller, and existing automation is read when you are not moving the hardware controller.
Latch
When Latch is selected in the Automation Mode window, automation is read until a hardware control is manipulated, at which point auto-
mation is written continuously until playback is stopped. When playback is resumed, automation is read until a hardware control is again
touched.
Write
When Write is selected in the Automation Mode window, automation is continuously written based on the current position of external
hardware controllers. Existing automation is not read at any point and is instead overwritten with the new automation.

## Automation Modes

Instrument Part Automation
In a feature unique to Studio One, automation envelopes for any given virtual instrument can written and accessed directly within Instru-
ment Parts, just like note data parameters such as velocity and pitch bend. Part automation is integrated into Instrument Parts, so that no
matter where an Instrument Part is moved, or how it is edited, the automation stays in place. In this way, virtual instrument automation
can be kept where it belongs with the Instrument Parts in your Song.
Thus, Instrument Part automation is functionally similar to the Track automation system but is dedicated to Instrument Parts and the vir-
tual instruments they control, offering additional flexibility.
Recording Part Automation
When an Instrument Part is being recorded, and any of a connected virtual or external instrument’s controls are manipulated with the
mouse or with an external hardware controller, those control changes are recorded into the Part as Part automation. At any time, Part
automation can be recorded live to a new or existing Part by enabling Record and manipulating the virtual instrument controls.
The related Instrument Track must be connected to a virtual or external instrument in order for Part automation to be recorded.
View Part Automation
To view and edit Part automation for an Instrument Part, select the desired Instrument Part and open the Edit view by pressing [F2] on
the keyboard, double-clicking on the Instrument Part, or clicking on the [Edit] button.
In the bottom-left corner of the Note Editor there's a small button that looks like a couple of jagged mountain peaks (
). Click that to
show / hide the Automation Lanes. The Parameter tab along the top of the lane shows the parameter currently displayed in the lane.
Manually Add and Edit a Part-Automation Envelope
Click one of the Parameter tabs to choose a parameter to view and edit in the Part Automation Lane. By default, Velocity, Modulation,
Pitch Bend, and Aftertouch (Pressure) are available.
To group-edit note Velocity, choose the Arrow Tool to draw a rectangle around the desired notes in the Piano View, and then click and
vertically drag a highlighted Velocity column in the Velocity Automation Lane to edit the desired velocity up or down. Alternatively, you
can group-select with the Arrow Tool in the Velocity Automation Lane itself; be sure to draw the selection rectangle around the tops of the
desired velocity columns to choose the desired notes. This allows for nuanced selection of only your loudest or quietest notes.
To assign a new automation envelope to its own Parameter tab, click the Add/Remove button (...) or [Right]/[Ctrl]-click an existing Para-
meter tab and select Add.... This opens the Automation dialog, which is identical to the window mentioned in the Automation Envel-
opes on the Track section of this chapter.
Alternatively, you can edit the parameter of the desired instrument, then click on the hand icon in the top left parameter window and drag
the parameter to the Note Editor to add a Part Automation envelope for that parameter to the Instrument Part.
The parameters that you can add to the Part Automation lane are based on the virtual instrument to which the Instrument Track that con-
tains the selected Instrument Part is connected. Only those parameters for which an automation envelope does not already exist are
available.
 Instrument Part Automation

Editing Part automation envelopes is nearly identical to editing Track automation envelopes, as described in the Editing Automation
Envelopes section of this chapter. The one exception is that if you press [Alt]/[Option] on the keyboard when using the Paint tool to draw
an automation envelope, you can draw straight lines of any length, which only use two envelope points.
It is possible to view and edit different parameters in separate Part Automation lanes. You can add and remove lanes using the plus and
minus buttons in the bottom-left corner of the Note Editor window. Click the Show/hide Automation Lanes button (
) to show / hide all
of the Part Automation lanes at the same time. Any written Part automation is read, regardless of whether it is currently being viewed in
either Part Automation lane.
Select Part Automation with Notes
With this option enabled, selecting notes automatically selects any currently visible Part Automation within the selected note range. As a
result, applying any edits to note position will automatically be applied to the selected Part Automation within the same range. This
includes changing the note position manually or using Quantize, as well as cut/copy/paste/duplicate/delete operations. Part Automation
currently not visible won’t be affected.
In order to select all Part Automation associated with a note, first make sure all Part Automation lanes are visible by adding additional
automation lanes and selecting the correct tab to display the automation curves.
This option works with all types of automation, including standard types such as Modulation and Pitch Bend, with the exception of Note
Controllers such as Poly Pressure and MPE. Note Controller automation data is always selected with their associated notes, regardless
of the current state of the “Select Part Automation with Notes” option.
 Instrument Part Automation
