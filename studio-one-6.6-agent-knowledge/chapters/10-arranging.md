# Arranging

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 232–267
> **Slug:** `10-arranging`

**Agent topics:** `arranger track`, `chord track`, `signature track`, `tempo track`, `lyrics track`, `scratch pad`, `bounce`, `folder tracks`, `track list`

---

Arranging
Arranging encompasses repositioning recorded or imported audio and note data to change the song structure, inserting tempo or time
signature changes, and many other processes. The following chapter discusses various aspects of arranging in Studio One, including
importing files, working with loops, the Tempo Track, and more.
Arranging encompasses repositioning recorded or imported audio and note data to change the song structure, inserting tempo or time
signature changes, and many other processes. The following chapter discusses various aspects of arranging in Studio One, including
importing files, working with loops, the Tempo Track, Arranger Track, Scratch Pads, and more.
Arranger Options
Click the Options button (shaped like a wrench) to bring up a menu with options that let you shape the behavior of the Arranger to suit
your needs and organizational style. The following options are available:
Selection Options
-
Solo follows Section With this option enabled, once a track is soloed, selecting a different track causes the newly selected
track to be soloed. When this option is disabled, tracks stay soloed until solo is disengaged.
-
Instrument Input follows Selection Enable this option to automatically engage Record and Monitor mode for any Instrument
Track you select.
-
Audio Input follows Section Enable this option to automatically engage Record and Monitor mode for any Audio Track you
select.
Editing Options
-
Enable crosshair cursor for tools Enables a large, white, vertical-and-horizontal crosshair in the Arrange view that aids in dis-
playing the exact position of the various mouse tools.
-
Locate when clicked in empty space allows the timeline cursor to be located based on clicking in empty space or clicking
where there are no Events.
-
Cursor follows Edit Position With this engaged, the playback-cursor position jumps to the beginning of any Event or group of
events you select, any note being selected or moved, or to the position of any marker being moved.
-
Automation follows events Enables automation envelopes to lock to Events so that moving an Event with automation “under”
it also moves the automation.
Arranging

-
No overlap when editing events When enabled, moving or pasting an Event over another Event deletes whatever is buried
beneath, so there is no overlapping data (only the audio crossfades are preserved). If the range being copied includes data out-
side an Event, the range selection is treated as if it were part of the Event. When the range selection is pasted, it overwrites the
identical range at the destination.
-
Note that the "No overlap" setting only works for note data if "Cut long notes at part end" is enabled at Studio One/Op-
tions/Advanced/MIDI (macOS: Preferences/Advanced/MIDI).
Visibility Options
-
Colorize track controls causes the whole control area of each Track to be color-coded with assigned colors for better visibility.
-
Show channel numbers in tracks Some Tracks do not have corresponding Channels in the Console (and vice versa). This
means that in some cases, a Track and its corresponding Channel may be numbered differently. Enable this option to display
each Track with its corresponding Channel number.
-
Show event names Shows the name labels inside each Event in the Arrangement view. This is purely an aesthetic difference
and does not change any functions.
-
Show instrument part envelopes Overlays a graphic representation of controller activity (volume, sustain, etc.). This does not
change any functions. Disengage this to display only the notes.
-
Show track notes Enable this option to display Track notes on each Track in the Arranger Page. When enabled, you can
double-click the small window and add more information about the Track.
-
Show track icons Enable this option to display Track Icons on each Track in the Arranger Page. When you click onto the empty
Track Icon box, a window will appear with many different icon options (Brass, Drums, Guitars, etc.). Including an icon for each
Track can be handy if you’d like to quickly navigate between channels without reading the Track names.
-
Show chords on events Adds an overlay to Audio Events in the Arrangement showing detected chords. This requires the track
height to be set to Small or higher.
Audio Options
-
Ignore Plug-In Latency Some plug-ins cause latency issues that disrupt the recording process, especially as you’re sequen-
cing external hardware. Enabling this option bypasses your plug-in latency issues so that you have no latency while sequencing.
-
To ensure that the plugin delay compensation works as intended, make sure to turn this feature back off after using it.
-
Monitoring follows record This option makes it so monitoring is enabled whenever a track is Record armed.
-
Monitoring mutes playback (Tape style) Enables a “Tape Style” behavior while recording. Normally, you can only monitor
with the monitor button enabled. Pushing the Record button enables both monitoring and recording at once. When you hit play-
back with this option enabled, monitoring is muted. The monitoring button can also be used during playback to mute the record-
ing and test other recording ideas without recording.
Quickly Duplicating Events
Events are often copied and pasted across a certain region to quickly build an arrangement. For instance, you might want a one-bar
drum loop to continue for 8 bars, or you might want a four-bar synth melody to continue for 12 bars. You can use the Duplicate function to
quickly copy and paste any Event in this fashion.
To Duplicate an Event, select it and press [D] on the keyboard. The results are affected by the current Arrange view Snap and Timebase
settings. With Snap disengaged, the Event is copied, and a new instance of the Event is placed precisely at the end of the original Event.
With Snap engaged, when an Event is duplicated, the new instance of the Event is placed at the next logical Snap position. For example,
an Event approximately one bar in length is placed at the beginning of the next bar, whereas an Event one-half bar in length would be
placed at the next half-bar.
Press [D] on keyboard multiple times to quickly copy and paste a selected Event across any region. If multiple Events are selected, they
can all be duplicated simultaneously in the same way as a single Event. For instance, you could duplicate an entire verse and chorus for
24 Tracks in a few seconds. This is often done to build a rough arrangement of a Song, after which unique parts for each section are
recorded.
When working with Instrument Parts, you can use a special type of duplication called Duplicate Shared, in which copies are made of a
Part, that are linked to the original Part, reflecting any changes made to the original or any Shared duplicates. For more information, see
the Duplicate Shared section.
To understand the Duplicate function in Studio One, experiment with Events of various lengths and with various Snap and Timebase set-
tings in the Arrange view.
 Quickly Duplicating Events

Duplicating Tracks
Tracks can also be easily duplicated, with or without the Events they contain. To duplicate a Track, select the Track or any Event it con-
tains and then select Duplicate from the Track menu. This duplicates the Track and all of its settings, including Inserts and Sends.
If you want the Events the Track contains to be duplicated, as well, select Duplicate (complete) from the Track menu. If multiple Tracks
are selected when the Duplicate function is used, each of the selected Tracks is duplicated. To select multiple Tracks in order, select a
Track, hold [Shift], and then press the Up or Down Arrow keys to select adjacent Tracks.
You can also duplicate a Track by [Right]/[Ctrl]-clicking its control area and choosing Duplicate Track or Duplicate Track (complete) from
the pop-up menu.
Alternatively, you can duplicate selected Tracks by holding [Ctrl] on the keyboard and clicking-and-dragging the Tracks up or down in the
Track Column. Holding both [Ctrl] and [Alt] lets you duplicate Tracks along with their Events. A horizontal blue line appears in the Track
Column while dragging the Tracks to indicate the Duplicate function, as opposed to simply reordering Tracks in the Track Column.
Duplicating Instrument Tracks
By default, duplicating an Instrument Track creates a second Instrument Track that sends its note data to the instrument on the original
track. This comes in handy when you wish to have several Tracks of note data, all addressing the same Instrument (discrete Tracks for
each drum type in an instance of Impact, for example).
If you want to completely duplicate an Instrument Track (including its instrument and effects plug-ins and settings), use the Duplicate
(Complete) command in the Track menu, or Duplicate Track (complete) in the contextual menu reached by [Right]/[Ctrl]-clicking the con-
trol area of the Track in Arrange view.
Global Tracks
The Global Track buttons sit in the area above the track controls in the Arrange view. They open dedicated tracks that span the full length
of the Arrangement. Each Global Track provides a unique and essential function, and can help you know at a glance what is happening
during the Song.
Global Track Visibility button
 Duplicating Tracks

When the Arrange view is wide enough, all of the Global Track buttons are visible. But when screen area is at a premium, the area that
contains the track controls and Global Track buttons can be made smaller by clicking and dragging the dividing line between them and
the Arrangement. As this happens, the Global Track buttons collapse into a single Global Track Visibility button.
You can use this button to access all six of the Global Track buttons: simply click the Global Track Visibility button to view them in a ver-
tical list, and then make a selection. A check mark indicates the Global Tracks that are currently open.
Ruler Track
The Ruler Track provides a secondary timeline ruler with a different format, allowing you to view the Song position in two different formats
at the same time. For example: bars/beats and timecode (frames). The options match those of the primary timebase setting:
-
Seconds The timeline division is an expression of hours : minutes : seconds : milliseconds.
-
Samples The timeline division is an expression of samples.
-
Bars The timeline division is an expression of musical bars and beats.
-
Frames The timeline division is an expression of frames.
As with the primary timeline, click anywhere on the secondary timeline to locate the playback cursor to that position in the Song. Use
[Right]/[Ctrl]-click to access Timebase settings, Song Markers, Loop settings, and more.
Marker Track
The Marker Track allows you to define section divisions within the Song, as well as the Song start and end points. Click this button to
view its contents, and use the plus and minus buttons to add or delete markers. For more information, see  Using the Marker Track.

## Arranger Track

This button opens the Arranger Track, which enables you to view and rearrange sections of the Song as if they were individual Events.
For more information, see the Arranger Track section.

## Chord Track

Click this button to open the Chord Track, which displays the chord progression for the Song. This can be constructed manually or detec-
ted and extracted from one or more Events. For more information, see the Chord Track section.

## Lyrics Track

Click this button to open the Lyrics Track, which displays and allows you to enter and edit lyrical content for your Song.
The Global Lyrics Track is found on both the Song and Show pages. For more information, see the Lyrics Track Note that the Global Lyr-
ics Track is an independent but related entity to the Lyrics Lanes
Global Tracks

## Video Track

The video track allows for placement of a video, useful for scoring to motion pictures. Videos can be moved across the timeline and lightly
edited, and you can even extract their audio to a separate track. Video Track is a more complex topic covered in greater detail in the
Video Playback and Sync topic.

## Signature Track

This button opens the Signature Track, which contains the settings for the Time Signatures and Key Signatures of the Song. It also
allows you to view, add, edit, or remove changes to those items. For more information, see the Signature Track section.

## Tempo Track

Click this button to open the Tempo Track, where all tempo settings for the Song can be viewed and adjusted. Tempo changes may also
be added and deleted. There's a full description in the  Tempo Track section.
Global Tracks in Audio / Music Editors
There's also a Global Track Visibility button in the Audio and Music Editor windows (with the exception of the Score view). You can use
this button to access four of the six Global Track buttons: Marker, Arranger, Chords, and Signature. The Secondary Ruler and the Tempo
Track buttons are reserved for the Arrange view.
The Global Tracks can also be viewed and toggled in these Editor windows with a [Right]/[Ctrl]-click on the time ruler. The timebase
options can be selected at the same time.
Note that the Global Tracks can't be changed inside the Editor windows. To add, edit, or remove items, use the Global Tracks in the
Arrange view.

## Arranger Track

The Arranger Track is an arrangement tool that lets you work with portions of your entire Song as though they were individual Events,
and rearrange them quickly and easily. This saves you the time and challenge of traditional editing, which can be difficult when dealing
with many Tracks at once.
Using the Arranger Track
The Arranger Track sits at the top of the Arrange view, and you can show or hide it by clicking the Open Arranger Track button, which
looks like this:
At first, the Arranger Track is empty, showing that no Arranger Track sections have been defined in your Song.
Once you define sections, you can freely move them along the timeline, insert them between other sections, copy/cut and paste, or
delete them.
These actions are performed across all Tracks in your Song that exist in the time covered by the section, including all Events, Parts, Mark-
ers, tempo changes, and automation data.
Defining the Sections of Your Song
To define a section in the Arranger Track, follow these steps:
1.
If the Arranger Track is not visible, click the Open Arrangertrack button to show it.
2.
Enable the Paint tool, or press and hold [Ctrl]/[Cmd] to temporarily switch to the Paint tool while leaving a different tool selected.
3.
Click-and-drag in the Arranger Track, over the part of your Song you wish to define as a section. A section of the Arranger Track
is marked, signifying that the section of the Song is now defined in the Arranger Track.

## Arranger Track

Each new Arranger Track section is given a default title, but you can enter a new title by [Right]/[Ctrl]-clicking the section and double-click-
ing its title in the pop-up menu, then typing the new title into the provided text field.
To change the color of a section, [Right]/[Ctrl]-click the section, then click on the colored square in the pop-up menu to choose a new
color.
To remove the Arranger Track definition from a section of your Song, select the section and press [Backspace] or [Delete], or [Right]/
[Ctrl]-click the section, and choose Delete from the pop-up menu.
To remove an Arranger Track definition as well as the time on the timeline that it covers (along with any Events or Parts that lay within it),
[Right]/[Ctrl]-click the section in the Inspector or Arranger Track and choose Delete Range from the pop-up menu that appears.
Timebase Button
Notice the Timebase button to the right of the Arranger Track in the Track column. The musical-note icon on the Timebase button indic-
ates that Arranger Track sections will adhere to their position based on bars and beats, so if the tempo changes, the sections move for-
ward or backward in time in relation to their musical position.
If you click on the Timebase button, it switches to a clock icon, indicating that the sections will adhere to their absolute position in time. If
the tempo changes, the sections do not move, as they are locked to an absolute time position in the timeline.
Editing Sections in the Arranger Track

## Arranger Track

Once you've defined the sections of your Song, you can begin working with them. Using the Arrow tool, you can accomplish the following
actions:
-
Move Click-and-drag a section to move it to a new location on the timeline.
-
Move Arranger Track Section Only Click-and-drag a section, then press and hold [Ctrl]/[Cmd] and [Alt]/[Option] to move only
the Arranger Track section, without any of the content that sits within it, to a new location on the timeline.
-
Insert Click-and-drag a section between two other sections. When a line appears between the sections, let go of the mouse but-
ton to insert the section there. This automatically moves the sections to the right of the insertion point forward in time, to make
space for the inserted section.
-
Replace Click-and-drag a section over another section. Let go of the mouse button to delete the existing section and replace it
with the new section.
-
Partially Replace Click-and-drag a section over another, longer section while holding [Shift]. Position the section at your loc-
ation of choice within the larger section, and let go of the mouse button to replace that portion with the new section.
-
Copy/Cut and Paste Select a section and copy or cut it, using the standard keyboard shortcut ([Ctrl]/[Cmd]-[C] to copy, [Ctrl]/
[Cmd]-[X] to cut) or by [Right]/[Ctrl]-clicking the section and choosing Copy or Cut from the pop-up menu. Place the cursor in
your chosen place in the timeline, and either press [Ctrl]/[Cmd]-[V] to paste the section, or [Right]/[Ctrl]-click on the timeline and
choose Paste from the drop-down menu. You can also click-and-drag a section while holding the [Alt]/[Option] key to create a
copy of the section. Let go of the mouse button to place the copy in your location of choice.
-
Create Markers from Arranger Sections [Right]/[Ctrl]-click a section in the Arranger Track and choose Create Markers from
Arranger Sections from the pop-up menu to create markers in the Marker Track that coincide with the titles and placements of
the sections in the Arranger Track.
-
Select Events in Section [Alt]/[Option]-double-click a section to select all Events and Parts across all tracks, within the bounds
of the section. You can also do this by [Right]/[Ctrl]-clicking a section in the Arranger Track and choosing Select Events in Sec-
tion from the pop-up menu.
-
Delete Range[Right]/[Ctrl]-click a section and choose Delete Range from the pop-up menu to delete the range of time that the
section covers, and all content within it, from the Song. Any content to the right of the deleted section is moved to meet the con-
tent in the preceding section.
-
Zoom Double-click a section in the Arranger Track to locate the transport to the start of that section, and zoom the view to show
the section in full.
Arranger Track Sections and Scratch Pads
You can drag defined sections of your Song from the Arranger Track into a Scratch Pad for safe keeping or for later use, much like you
can with normal Events and Parts. Simply clicking-and-dragging a section into a Scratch Pad creates a copy of that section in the Scratch
Pad, with all elements and data intact. If you would rather move a section to a Scratch Pad, rather than copy it, hold [Alt]/[Option] while
dragging.
You can also [Right]/[Ctrl]-click any section in the Arranger track and choose Copy to new Scratch Pad from the pop-up menu to create a
new Scratch Pad containing a copy of the section. Alternately, choose Move to new Scratch Pad to remove the section from the main
timeline, and create a new Scratch Pad containing the section.
For more information on working with Scratch Pads, see the Scratch Pad section.
Arranger Track Inspector View
When you've selected an item or area in the Arranger Track, the Track Inspector shows a list of all defined sections in your Song, as well
as any sections currently contained in a Scratch Pad. You can perform actions on the sections in this list much like you can in the
Arranger track.
To locate the transport to the start of a section, click the section in the Inspector list, or double-click to the left of the section to locate the
transport and start playback from the start of the section. A playback cursor appears to mark the section that is now playing. To rename a
section, double-click its name in the list and enter the new name into the provided field.
To copy a section to a new location, drag the section from the list to the location of your choice in the main timeline or onto a Scratch Pad.
[Right]/[Ctrl]-click any section in the list to access a pop-up menu with other section-editing commands as outlined in Editing Sections
in the Arranger Track.
Arranger Track Sections and Marker Track Markers
For flexibility, you can automatically create Arranger Track sections based on currently placed Marker Track markers, or vice-versa. To
create Markers based on Arranger sections, [Right]/[Ctrl]-click an Arranger Track section and choose Create Markers from Arranger Sec-
tions from the pop-up menu. Markers are created marking the start and end of each Arranger section.

## Arranger Track

To create Arranger sections based on currently placed Markers, [Right]/[Ctrl]-click in the Marker Track and choose Create Arranger Sec-
tions from Markers from the pop-up menu. Arranger sections are created, beginning at each Marker location, and ending at the location
of the next Marker in the timeline.
Triggering Arranger Sections Manually
You can trigger Arranger sections manually on the Song page, jumping your playback to any section of the Arranger Track with musical
timing and without breaking rhythm. This is ideal for prototyping the sound of new song arrangement on-the-fly during your production
process, but before committing to your changes by reordering the Arranger Sections manually. With this you may discover that a second
bridge after the third chorus is just what your song needed—and the discovery is just a double-click away!
With the Arranger Track selected and Studio One’s Inspector open [F4], simply [double-click] an Arranger Section in the Inspector to
prompt a playback jump to it. The chosen Section will receive a jump indicator icon. The timing of the jump will adhere to the Sync Mode
option setting chosen in the Arranger Track Inspector: 1 bar, 2 bars, 4 bars, or after the Arranger Section’s End. You can also trigger a
jump by a [double-click] on a Section in the Arranger Track itself.
Sync Modes govern the timing of a Jump from one Arranger Section to another. Options include:
-
Off: Jump occurs immediately upon double-clicking an Arranger Section with no Sync
-
1 bar: Jump occurs at the next bar start after the current play position
-
2 bars: Jump occurs at the end of a 2-bar section, relative to section start
-
4 bars: Jump occurs at the end of a 4-bar section, relative to section start
End: Jump occurs at the end of the currently-playing Arranger section, regardless of how long the selected Arranger section is.
A specialized version of the Arranger Track is also available on the Show Page. Visit Show Page Overview for more info.

## Chord Track

The Chord Track is a global track (similar to the Arranger track) that provides the ability to perform "harmonic editing" of both Instrument
and Audio Parts. This restructuring of chord progressions can affect an entire song, or only the Tracks of your choice. This lets you write
musical content with a chord progression that appeals at the time, and make sweeping changes later, without exhaustive editing or re-
recording of Parts.
Want to modulate that final chorus for a little extra push of energy, or rethink the harmonic structure of a composition in progress? The
Chord Track lets you try these sorts of changes on a whim.
While the Chord Track is capable of very powerful effects, it does have its limits, primarily in that audio cannot be pitch-shifted without
some level of artifacts added. We recommend that once you're done experimenting and "prototyping" your song, you re-record any audio
parts to fit the new chord progression, especially if they are critical parts.
To show or hide the Chord Track, click this button above the Arrange view:
To toggle the effect of the Chord Track on or off for all
affected Tracks, click the [Follow: On/Off] button
Getting Started with the Chord Track

## Chord Track

First, set a key signature for the song to ensure proper chord display in the Chord Track. The simplest way to do this is to click the [Key]
button in the Transport and select the key of your choice from the pop-up selector that appears.
It is also possible to derive the key signature automatically. There are two methods:
-
From an Instrument Part Select the Part, then navigate to Event/Detect Key Signatures (or [Right]/[Ctrl]-click the Part and nav-
igate to Instrument Parts/Detect Key Signatures in the pop-up menu that appears).
-
From an Audio Event [Right]/[Ctrl]-click the Audio Event, navigate to Audio Operations/Chords, and select Extract Key Sig-
natures from Event. When the Editor is open this is available in the Action/Chords menu. Note that the Audio must have its
Chords detected via Melodyne first.
A Song can change key signatures one or more times. See the Signature Track section to learn more about this.
Once you've set a key signature you can begin to populate the Chord Track with chords. This can be done manually, or by automatically
detecting the chord structure of your song from its Instrument or Audio Parts.
If any one Instrument or Audio Part in your Song contains musical content that spans the entire length of the Song, you can use that Part
alone to auto-detect the chord progression. Otherwise, you may find it useful to export a mixdown of your song, re-import the mixdown to
an Audio Track, and use that track as the basis for chord detection. Once that's done, you can remove the mixdown Track.
Next we'll learn how to add, delete, and edit chords in the Chord Track.

## Chord Track

Entering and Editing Chords Manually
To add chords manually, select the Paint tool (or hold [Ctrl] to select it temporarily) and click inside the Chord Track. You can also add a
chord by double-clicking in the Chord Track with the Arrow tool.
Each new chord section you add is one bar long by default, or the length of the current selection in the timeline. You can change the
length of a chord by clicking one of its ends and dragging it to the desired length. If adding chords with the Paint tool, you can also click-
and-drag in the Chord Track to create longer chords.
Once you've added a chord, you can change it to a different chord or variation in a variety of ways. Try double-clicking a chord to open
the Chord Selector. This window lets you choose from all of the main chord types and extensions. Keep in mind that the Chord Track can-
not add notes to chords played in affected Parts. It can only shift the notes that exist. If you want to select a chord with 7, 9, 11 or other
extensions, you will only hear those notes if the chords in your Parts contain four or more notes.
If you enable the Instrument Input option by clicking this button
you can play a chord on any connected MIDI keyboard to change
the selected chord. The Chord Selector then shows you the name of the chord you've played, and the current chord changes to match.
With Instrument Input enabled, you also can select one or more chords in the Chord Track and play any chord shape on a MIDI keyboard
to change all selected chords.
Next to the Instrument Input button is the Audition Chords button. When enabled, each chord you select will be played for you. This is a
great way to audition different chords to hear how they sound. A Gmaj7sus4 chord might be perfect right there.
Here are some other features you may want to try:
-
See if adjacent chords work well together by clicking the Chord Track arrows in the upper left corner of the Chord Selector win-
dow.
-
Build complex chords quickly by holding [Alt]/[Opt] and clicking more than one of the following Interval buttons: b9, 9|2, #9, 11,
#11, or b13. this will add the tensions/extensions accordingly.
-
Build complex chords by holding [Alt]/[Opt] and clicking more than one of the Intervals buttons. If a song calls for a Gm13 add 11,
it's yours.
-
If you want to see a C# chord somewhere instead of a Db chord, for example, click the Root note in the Chord wheel to toggle
between the two. This may be faster sometimes than selecting it in the dropdown Root menu on the right.
-
b5 and #5 can be combined with other intervals, allowing you to shift the 5th within a chord up or down.

## Chord Track

-
9|2 is indicative of different octaves of the same tone. You can choose the octave of a 9|2 interval by clicking the icon to cycle
through high octave, low octave, or none. The selected interval will be underlined. Note that the “9|2” demarcation is an indicator
of the interval options, and not a slash chord.
-
Simply double click the chord name in the center of the Chord Selector to enter the chord manually via your qwerty keyboard—
tensions, slash chords, and all.
When you're done editing a chord, you can close the Chord Selector or select another chord in the Chord Track and continue editing.
To delete one or more chords from the Chord Track, select them and press the [Delete] or [Backspace] key on your keyboard.
Extracting Chords from Instrument Parts
One simple way to become familiar with the Chord Track is to populate it with the chord structure from one or more Instrument Parts.
[Right]/[Ctrl]-click on a Part (or multiple selected Parts) in the timeline, then choose [Extract to Chord Track]. This function analyzes the
musical relationships of the notes in the selected content, and fills the Chord Track with the chords it recognizes.
You can also simply drag selected Instrument Parts (single or multiple, across as many Tracks as you like) onto the Chord Track to
extract their shared chord progressions. This is one easy way to detect chords across a large area of your Song, especially if you're using
different Instrument Tracks (with distinct instruments and sound) in each section.
Some types of note data can cause the Extract to Chord Track algorithm to choose chords inaccurately. If you notice any errors, feel free
to edit or replace chords using the methods described in Entering and Editing Chords Manually.

## Chord Track

Extracting Chords from MIDI files
You can also drag and drop a MIDI file from Studio One’s Browser or your OS’s Finder/Explorer directly onto the Chord Track to detect its
Chords. This is an ideal way to get a quick start on a song from a MIDI chord pack. Note that complex songs with many instruments
and/or lead melody elements may cause inaccuracies in chord detection.
Extracting Chords from Audio Parts
You can also extract chord information from Audio Parts. To do this, select an Audio Part and navigate to Audio/Detect Chords (or
[Right]/[Ctrl]-click the Part and navigate to Audio/Detect Chords in the pop-up menu) to analyze the harmonic structure of the Part. Once
completed, you can see the detected chords along the bottom edge of the Part.

## Chord Track

To apply the detected chords to the Chord Track, select the Part and navigate to Audio/Extract to Chord Track (or [Right]/[Ctrl]-click the
Part and navigate to Audio/Extract to Chord Track in the pop-up menu).
The extracted chords are then visible in the Chord track, and can be changed and edited as needed. As with Instrument Parts, some
types of audio information can result in incorrect chord detection. If you notice any errors, feel free to edit or replace chords using the
methods described in Entering and Editing Chords Manually.
Apply Chords from Chord Track
Some audio data doesn't lend itself easily to automatic chord detection, and if the wrong chords are detected, harmonic changes made in
the Chord Track may not bring the desired result. If you find that one or more of your audio tracks do not show the proper chords after
using Detect Chords, here is a good way to get around that.
First, detect the chords for that section of the song from another source that detects more accurately. If no Instrument or Audio Parts
seem to work, you can try entering the chords manually or with a MIDI keyboard. Then, select the Audio Part that you could not accur-
ately analyze, and navigate to Audio/Apply Chords from Chord Track (or [Right]/[Ctrl]-click the Part and navigate to Audio/Apply Chords
from Chord Track in the pop-up menu). This applies the chord designations from the Chord Track to that Audio Part, ensuring that when it
is pitch-shifted during harmonic editing, its notes are shifted more accurately.
Create Note Events from Chord Track

## Chord Track

Any or all Chord events on the Chord Track can be converted to Note Events in Instrument Tracks by simply dragging the Chord Events
from the Chord Track to an Instrument Track. This will create Note Events with the same duration as the Chord Events that created them.
These are basic chords, where the lowest note will always be the root note of the chord.
These extracted notes can now be edited or processed just like any other Note Events.
Create Chord Note Events from Audio Events
Chord Track notes can be extracted directly from an Audio Event once its chords have been detected as described in “Extracting Chords
from Audio Parts,” above.
Simply drag and drop a Chord-detected Audio Event to an Instrument Track to render the desired Note Events in place.

## Chord Track

The Chord Inspector

## Chord Track

While working in the Chord Track, you can open the Chords Inspector (by clicking the "i" button above the timeline). This reveals a wealth
of features and information, including the Instrument Output for the Chord Track and the chord progression of the Song. Working from
top to bottom:
-
Instrument Specify the default instrument for the Chord Audition feature by selecting one from the menu. You can use the Pre-
view instrument, any instrument in the Song, or choose an Instrument or Preset from the Browser and drag-and-drop it onto
header of the Chord Track. This will become the new default preset for auditioning chords. Click the small keyboard icon to
open/close the Instrument view.
-
Audition Chords This button is linked to the "speaker" button in the Chord Selector window; toggle one and the other will toggle
also.
-
Play Track Enable this to hear the Chord Track play along with the Song. This will help confirm whether the chords entered
manually match the Audio Events, for example.
-
Octave Select the center octave for the Audition Chords.
-
Velocity Click-and-drag or double-click the field to set the velocity at which the Audition Chords will play. The range is from 0 to
100.
-
Key Signature This menu is linked to the Key Signature in the Transport, and opens an identical window.
-
Chord Progression All of the chords in the Song are listed in order here. It's a quick way to select a Chord near the end of the
Song, for example, without having to locate it in the Chord Track.
-
Chord Color Use this field to select a different color for the selected Chord in the chord progression. It's faster and more specific
than finding that Chord in the Chord Track and using [Right]/[Ctrl]-click, although that method also provides other features (see
Replacing Chords below).
-
Start/End You can set the duration of the selected chord with great precision using these fields.
-
Chord Selector This button opens and closes the Chord Selector window.
Quantizing the Chord Track
Once you've populated the Chord Track with chords, you may find it helpful to quantize the start positions of those chords. To do so,
select the chords you want to quantize, and navigate to Event/Quantize/Quantize on Track.
Often, chord changes do not happen precisely on-beat, especially when working with live recorded audio. After quantizing chords, you
may find it helpful to subtly shift the start and end positions of each chord to minimize unnatural shifting behavior and better match the
movement of the performance.
Replacing Chords

## Chord Track

Let's say you like a particular chord better than the one you've been using and want to replace it throughout the Song. [Right]/[Ctrl]-click
any one of those chords in the Chord Track to open a menu. You can quickly change the chord root, type, bass note, and intervals here,
along with the following options:
-
Chord Color Use this field to select a different color for this Chord wherever it appears in the Song.
-
Select all "Dm" Chords Note: D minor is used here as an example, but the actual name will be that of the selected chord. This
field allows you to substitute a new chord for the old one throughout the Song. Select this option and the menu will close, then
use the Chord Selector to select the chord you prefer.
-
Transpose Chords Enter the number of chromatic steps by which the selected chord should be transposed throughout the
Song.
-
Clear Chord Track This option will delete every chord in the Chord Track.
-
Cut, Copy, Delete These are standard functions. A chord can be pasted elsewhere in the Chord Track by selecting a new loc-
ation in the timeline, using [Right]/[Ctrl]-click, and selecting Paste.
-
Duplicate This option will place the selected chord in the next measure, overwriting any chord that is already there.
Quick Chord Tricks
You can cut, copy, paste, and delete one or more chords from the Chord Track the same way you'd perform other Studio One functions
with your computer keyboard. To paste a chord elsewhere in the Chord Track, select a new location in the timeline, use [Right]/[Ctrl]-
click, and select Paste from the menu.
The [D] key can be used as a quick way to paste multiple copies of the selected chord or chords in a row. Then minor adjustments can be
made to each without having to define the root note, for example. This method will overwrite any chords in its path, so proceed with cau-
tion.
Holding [shift] while double-clicking the Chord Track will quickly select all of the Chord Events, which can then be easily dragged and
dropped to an Instrument Track.
Setting Chord Follow Behavior
By default, the Tracks in your Song are unaffected by the Chord Track. To allow a Track to change its harmonic structure along with the
Chord Track, you must enable one of the Follow Chords modes for that Track.
Follow Chords

## Chord Track

If you select a Track with the Inspector shown, you'll see its Follow Chords selector. This selector offers the following modes, each with
its own style of operation:
-
Off The default mode. The Chord Track has no effect on a Track in this mode.
-
Parallel In this mode, chords in the affected Track are shifted in parallel, aligning the root note of the musical content with the
root of the target chord. This maintains chord note relationships in the musical content, which may result in some out-of-key
notes.
-
Narrow In this mode, notes in the affected Track are shifted to the nearest note in the current chord in the Chord Track.
-
Bass This mode behaves the same as "parallel," but with special rule for the bass note: the source Chord's bass note (or root if it
has no bass note) is mapped to the target bass note or root.
-
Scale (Audio Tracks only) In this mode, notes in the affected Track are snapped to the nearest scale note in the target chord.
-
Universal (Audio Tracks only) This mode does not require the use of the Detect Chords feature before use. In this mode,
notes in the affected Track are forced to follow the scale notes of the target chord.
Tune Modes (Audio Tracks only)
Each type of audio material reacts to pitch shifting in a different way. For this reason, you have a choice of Tune Modes that help to optim-
ize the algorithm for each type of source: Bass Guitar, Guitar, Piano, Brass, Lead, and Strings. Whatever your source, feel free to try
different modes until you get the most pleasing result. The Tune Mode selector can be found in the Inspector when an Audio Track is
selected.

## Chord Track

Keep in mind that Tune Modes do not affect the way that the Chord Track shifts the harmony of a Track. They only affect the way the shif-
ted audio sounds.
Harmonic Editing with the Chord Track
Now that you have chords in the Chord Track, and some Instrument and Audio Parts to go with them (with Follow Chords modes selec-
ted), it's time to get into some harmonic editing. To do this, simply select one or more chords in the Chord Track and change them in one
of the ways described in Entering and Editing Chords Manually . You can enter a chord using a connected MIDI keyboard, double-click a
chord to change it with the Chord Selector, or change its parameters in the Inspector. You can add, delete, and change the lengths of
each chord to suit the changes you wish to make.
You can also shift the root note of one or more chords by selecting the chords, holding [Alt]/[Opt], and moving the scroll wheel on your
pointing device (or using the scroll gesture on your trackpad).
As you experiment with harmonic editing you may notice that certain chords cause undesired results on certain tracks, whether simply
creating unpleasant note movement, or with audio, unwanted pitch-shifting artifacts. To help alleviate these issues, feel free to try the
various Follow Chords and Tune Modes, or simply tweak the chords in the Chord Track. Sometimes adding additional intervals or chan-
ging to a different Bass note can make all the difference.
Remember that you can always switch the effects of the Chord Track on or off for the entire song at once by toggling the [Follow: On/Off]
button, to the left of the Chord Track.
A special version of the Chord Track is also available on the Show Page.
Chord Display
The floating, resizable Chord Display View presents several options for viewing Chords. Useful for easy sight-reading while practicing
your instrument of choice... particularly when used in conjunction with loop points!
This window has three options:
-
Chord Track displays the chord from the Chord Track at the current playback position, as well as the next upcoming Chord (in
blue.)
-
Input Chord displays the chord currently being played on an external keyboard
-
Editor mirrors the current/selected Chord display in the Note Editor inspector. When multiple tracks are visible in the editor, all
of them contribute to the chord displayed. When no instrument editor is open, it displays the chord of a currently selected instru-
ment track at the current playback point.
Chord Display can be accessed from the View drop-down menu, or via the contextual menu found by right-clicking on the Chord Track
itself.

## Chord Track

## Signature Track

Studio One has a dedicated Signature Track which can be used to define the global time signature and key signature for the Song. You
can also use it to change the time signature or key signature for any bar in the Song, as well as edit or remove them.
Click the Signature Track icon above the Arrange view to open the Signature Track. This reveals the time / key signature markers.
Time Signature
The time signature is a convention used in Western music notation to specify how many beats are in each bar and what note value con-
stitutes one beat. The time signature is notated as a fraction, where the numerator (the upper number) equals the number of beats in the
bar, and the denominator (the bottom number) equals the note value for each beat.
By default, the time signature is set to 4/4 for all new Songs. This means there are four quarter-notes per bar. To change the time sig-
nature for your Song, do one of the following:
-
Click on the upper or lower number of the time signature in the Transport and select a new value from the pop-up menu.
-
Click the Signature Track icon above the Arrange view to open the Signature Track. Then double-click or [Right]/[Ctrl]-click the
first time signature on the left and select new values from the pop-up menu.
Metronome behavior is affected by the time signature. The downbeat and other beats determine the sample and level used for the
Accent and Click, respectively.
Inserting Time Signature Changes
If your Song requires more than one time signature, Studio One allows for that. Note that the time signature can only change on the first
beat of a bar.
Here's how to insert a time signature change into your Song.

## Signature Track

-
Open the Signature Track.
-
[Right]/[Ctrl]-click inside the Signature Track within the first half of the bar where the change should be.
-
Select Insert Time Signature from the contextual menu.
-
Enter the values for the new time signature in the pop-up menu.
-
Click OK, and a new Time Signature marker is inserted at the start of that bar.
You can click-and-drag a Time Signature marker to any bar-line position in the Ruler where a marker doesn't already exist. To change
the time signature of an existing Time Signature marker, double-click the marker and choose new values.
Your Song can contain any number of time signature changes, and the current time signature is always displayed in the Transport.
Edit or Remove Time Signature Changes
To edit or remove a time signature, open the Signature Track, click the desired Time Signature marker, then [Right]/[Ctrl]-click to open
the contextual menu and select the option you want.
-
Select Edit Time Signature to change the time signature, then enter the desired values in the pop-up menu and click OK.
-
Select Remove Time Signature to delete the marker. You can also press the [Delete] key on your keyboard.
Key Signature
The key signature of a Song specifies which notes are part of the scale and which are not (i.e., the accidentals). This affects which notes
can be selected when editing the Score in Score View. It does not affect which notes can be selected in Piano or Drum views.
The key signature is not assigned when a new Song is created. To establish the key signature for your Song, do one of the following:
-
Click the [Key] button in the Transport and select the key of your choice from the pop-up selector.
-
Click the Signature Track icon above the Arrange view to open the Signature Track. Then [Right]/[Ctrl]-click the first time sig-
nature on the left, select Insert Key Signature from the menu, and then select the desired key from the pop-up selector.
Inserting Key Signature Changes
Changing the key signature within a Song can help build intensity or even change the mood of the Song. Studio One allows you to har-
ness this powerful creative element through the Signature Track.
To insert a new key signature into your Song, follow these steps:
-
Click the Signature Track icon above the Arrange view to open the Signature Track.
-
Locate the Timeline cursor to the bar where you want the key signature to change.
-
[Right]/[Ctrl]-click a blank section of the Signature Track to open the contextual menu.
-
Select Insert Key Signature from the menu, and then select the desired key from the pop-up selector.
Note that the key signature can only change on the first beat of a bar.
Edit or Remove Key Signature Changes

## Signature Track

To edit or remove a key signature, open the Signature Track, click the desired Key Signature marker, then [Right]/[Ctrl]-click to open the
contextual menu and select the option you want.
-
Select Edit Key Signature to change the key signature, then select a new key signature from the pop-up selector.
-
Select Remove Key Signature to delete the marker. You can also press the [Delete] key on your keyboard.
You can also edit the key signature of a section of your Song using the Key window in the Transport. Locate the Timeline to one of the
measures inside the section with the key signature you want to change, then click the Key window in the Transport and select a new key
signature from the pop-up selector. The key signature changes for the area of the song between the previous marker and the next
marker.
Detecting Key Signatures
Studio One makes it possible to derive the key signatures automatically from an Event. There are two methods:
-
From an Instrument Part Select the Part, then navigate to Event/Detect Key Signatures (or [Right]/[Ctrl]-click the Part and nav-
igate to Instrument Parts/Detect Key Signatures in the pop-up menu that appears).
-
From an Audio Event
-
First use Melodyne to analyze the key signatures. You can also use any ARA plug-in which is capable of chord detec-
tion. Please refer to the appropriate documentation to learn how to do this.
-
[Right]/[Ctrl]-click the Audio Event and navigate to Audio Operations/Chords.
-
Select Extract Key Signatures from Event. When the Editor is open this is available in the Action/Chords menu.
The Signature Track now displays the extracted key signatures.

## Tempo Track

Many modern recordings sound mechanical, like a machine playing music. This is often because the recording has a single, static
tempo, whereas the tempo in a natural performance tends to drift slightly. Interesting and musical results can be achieved by varying the
tempo in your recordings. Tempo changes do not affect your ability to sync recordings to the tempo, as the click track and all other ele-
ments in Studio One follow the tempo dynamically as it changes.
Inserting Tempo Changes
To insert a tempo change, open the Tempo Track by clicking on the Tempo Track button above the Track Column. Then select the Arrow
or Draw tool in the Arrange view. Click at any position in the Tempo Track to insert a tempo change and drag up or down to adjust the
Tempo value at that position, in much the same way you can with other automation types in Studio One.

## Tempo Track

To change an existing tempo value in the Tempo Track, click-and-drag your chosen point with the Arrow tool. To enter a specific tempo,
[Right]/[Ctrl]-click a point and type a number into the value field.
Tempo smoothly changes between points on the Tempo Track. To create a curve, hover the mouse pointer over the middle of a line seg-
ment until a small handle appears. Drag the handle up or down to change the shape of the curve. You can also click-and-drag any point
left or right across the Timeline to reposition the tempo change in the Tempo Track.
The value set by the tempo change continues for the rest of the Song or until the next tempo change. Also, the tempo value in the Trans-
port is immediately updated at the appropriate time, according to each tempo change.
If the related Audio Tracks are in Timestretch mode, Audio Events are stretched dynamically to reflect any tempo change on the fly, with
no need to split or otherwise edit the Events.
Beat-Linear vs. Time-Linear Timebase
Given this flexibility with smooth tempo changes over time, you may appreciate these two visualization options, accessible by right-click-
ing in the time ruler above the tempo track and navigating to Timebase/Beat-Linear or Timebase/Time-Linear.
When Beat-Linear is selected, all bars in your Song are shown with the same length, while the time scale of the timeline shifts to match
your tempo changes. For example, with the timebase set to Seconds, as the tempo changes, the spacing between seconds changes
even as the space between bars remains the same.

## Tempo Track

When Time-Linear is selected, bars in your song change their visual length to represent the shortening or lengthening effect of tempo
changes. With the timebase set to Seconds, you'll see that the spacing of seconds remains the same, even as the space between bars
changes.
Set Tempo Range
By default, Studio One shows you a range from 60-240 BPM in the Tempo Track. However, in most cases, Songs do not require that
amount of tempo range, and you may find it useful to narrow the scope of the display. This makes fine-tuning tempo changes easier and
more accurate.
To set the range of the Tempo Track, double-click in the "max" and "min" fields to the left of the Tempo Track. Enter your new maximum
and minimum BPM values, and watch the display focus in on your chosen tempo range. Changes to these settings are saved with the cur-
rent Song.
Time Scale Tool
The Time Scale Tool lets you quickly match a section of your tempo map with the tempo of an imported song or other audio file. This
makes manual tempo mapping easier, especially when the imported file contains many shifts in tempo.
To use the Time Scale Tool, first place your audio file so that its first beat (or the first beat of any bar) is aligned with the start of a bar in
your timeline. If there is not yet a tempo change marker at the first beat, create one. This becomes your starting point for the tempo map.
Then, with your cursor in the tempo track, press and hold [Ctrl]/[Cmd] to switch to the Time Scale Tool. You'll see the cursor change to
look like the image above. While this tool is shown, click and drag from the start of a defined barline in the timeline (such as four bars
ahead of the previous tempo marker) to the point in the timeline that aligns with that amount of bars in the audio file. Then, let go of the
mouse button.
By doing this dragging motion between those two points with the Time Scale Tool, you adjust the tempo for that section to match that of
the audio file. You can often visually determine the correct place to let go, but if that's not possible, you can use the Listen tool before-
hand to find the right spot in your audio file.
By default, a new tempo marker is automatically inserted when you let go of the mouse button after using the Time Scale Tool. This lets
you simply move on to the next set of bars you want to match with and use the Time Scale Tool again. If you'd rather not insert a marker
when you release the mouse button, hold [Alt]/[Opt] along with [Ctrl]/[Cmd].

## Lyrics Track

Studio One’s Global Lyrics Track allows you to enter and edit Lyrics via a dedicated Track in the Song Page. These Lyrics can be option-
ally rendered in the Lyrics Display , which will highlight the current lyrics in time with your music.
Lyrics can be entered and edited either directly on the Lyrics Track itself, or via the Lyrics Display interface, discussed in greater detail
below.

## Lyrics Track

Adding Lyrics to the Global Lyrics Track
Open the Lyrics Track by choosing the [L] icon from the Global Track List.
To enter Lyrics directly into the Lyrics Track, double-click in the desired location and begin typing.
-
Press [Spacebar] to advance to the next word.
-
Press [Return/Enter] to start a new line (visible in Lyrics Display ) and advance to the next bar.
-
Press [TAB] to advance to the next Lyrics entry point without starting a new line.
-
Press [Alt+Return/Enter] to align the currently-selected Lyric Event with the Play Cursor and select the next Lyric Event. This
can be used during playback to quickly align Lyrics Events to your music.
You can also paste copied text directly into the Global Lyrics Track from your clipboard. Press [CMD/CTRL+V] to paste into either the Lyr-
ics Track or Lyrics Display. Lyric Events pasted will be separated line by line.
Lyrics Editing
Once entered, Lyrics can be edited similarly to Note Events. They can be dragged and dropped, copy/pasted, group-selected, and duplic-
ated. Lyric Events follow Studio One’s global quantize and snap settings when moving Events.
Creating Note Events from Lyrics
You can click and drag a Lyrics Event (or several Lyrics Events) from the Lyrics Lane to the Note Editor to create new Notes. By default,
the Note placement will align vertically with the chosen Lyrics. Hold [shift] while dragging left or right to freely position the generated
notes.
Lyrics Import
Lyrics in .TXT, .MID or .MIDI format can also be imported directly from Studio One’s Browser. Simply drag and drop your file from the
Browser to the Lyrics Track.
Lyrics Track Options

## Lyrics Track

The Lyrics Track can be used to enter, display, and edit content from the Global Lyrics Track or from the Lyrics Lane of a selected Instru-
ment Track. Use the drop-down menu to select the Lyrics source.
Timebase
Click the timebase icon (
/
) to toggle between a beat- or second-based timebase.
-
A beat-based Timebase indicates that Lyrics will adhere to their position based on bars and beats, so if the tempo changes,
the Lyrics move forward or backward in time in relation to their musical position.
-
A second-based Timebase indicates that the Lyrics will adhere to their absolute position in time. If the tempo changes, the
Lyrics do not move, as they are locked to an absolute time position in the timeline.
Lyrics Options
Right-click a Lyric to view the Lyric Options menu:
-
New Line: This Lyric will start a new line in Lyrics Display
-
New Paragraph: This Lyric will start a new Paragraph in Lyrics Display .
-
Cut, Copy, Delete, and Duplicate function identically to their counterpart commands for Note Events.
Lyrics Display
To open Lyrics Display , Navigate to View >> Lyrics Display or click the
icon in the header of the Lyrics Track.

## Lyrics Track

Lyrics displayed here are highlighted in-time with your Song on playback; the View will autoscroll to keep the current Lyrics in the center
of the display.
Lyrics Display is available in the Song Page and The Show Timeline.
Lyrics Display Options
-
Edit Mode Click the pencil icon (
) to toggle Edit Mode in Lyrics Display . When activated, you can click in the Lyrics Display
window and begin typing to enter your Lyrics.
-
Show Ruler Click the ruler icon to toggle the visibility of the Lyric Track ruler, useful for determining musically-relevant
timing for your Lyrics.
-
Grid Options Click the drop-down menu to choose the Grid spacing for your Lyrics. This determines the space entered
between your lyrics when pressing the spacebar or hyphen key during lyrics entry.
-
Setup Click the wrench icon (
) to open this menu to choose from several Lyrics Display options:
-
Ahead (in quarters) sets the time offset for the Lyrics highlight in quarter-note values.
-
Alignment lets you center- or left-align the Lyrics displayed.
-
Font Size determines the size of the Lyrics displayed in Lyrics Display .
-
Track Use this drop-down menu to choose Lyric View’s source — it can render Lyrics content from the Global Track, or from any
Lyric Lanes populated in your Instrument Tracks.
Lyrics Display Edit Mode
Click the pencil icon (
) to toggle Edit Mode in Lyrics Display . When activated, you can click in the Lyrics Display window and begin
typing to enter your Lyrics.
When editing text in the Lyrics Editor, the following keyboard/mouse commands are available:
-
[Arrow keys] to navigate the caret
-
[Shift + Arrow keys] to make a selection
-
[Option / Alt + left / right] to jump between words
-
Home to jump to the start of a line
-
End to jump to the end of a line
-
Double-click to select a word
-
Triple-click to select a line
-
Backspace at the beginning of a word or syllable moves the word or syllable backwards on the time grid by the selected grid
value
-
If the event is on the same position as the previous event after moving it, it is merged with the previous event
-
Space at the beginning of a word or syllable moves the word or syllable forward on the time grid by the selected grid
value
-
If the caret was not at the beginning of a word or syllable, the word or syllable is split into two words
-
[-] at the beginning of a syllable moves the syllable forward on the time grid by the selected grid value
-
If the caret was not at the beginning of a syllable, the word or syllable is split into two syllables
Useful Lyrics Display Tips
-
Clicking on Lyrics in the Lyric View (with Edit Mode off) will jump the playback cursor to the Lyric’s location in the Lyric Track; you
can use this to navigate around your Song.
-
Lyrics Display can even be displayed on a second monitor separate from Studio One; great for vocal recording or performances
that encourage audience participation or group learning of songs.
-
When entering Lyrics, the [spacebar], [tab], or [-] (hyphen) will advance Lyrics entry to the next Grid point. The hyphen is useful
for spreading multisyllabic words across multiple notes. Hyphens will render in the Lyrics Lane of the Note Editor and Score
View, but not in Lyrics Display .
-
Entering lyrics from the Lyrics Display creates new events automatically when you hit [Return/Enter].
-
Lyrics Track and Lyrics Display are also supported on The Show Timeline
-
You can also use the Lyrics Lanes to add Lyrics to Instrument Tracks.

## Lyrics Track

Lyrics Lanes
Lyrics Lanes differ from the Global Lyrics Track in that Lyrics Lanes are instrument-specific. They are accessed in the Lanes section of
the Note Editor for any Instrument Track, and can be edited in both the Piano View and Notation View. Every Instrument Track can have
its own Lyrics Lane with different Lyrics!
Lyrics populating the Lyrics Lane.
Adding Lyrics to the Lyrics Lane
-
Double-click any Instrument Part to open the Note Editor.
-
In the Note Editor, click on the Show/Hide Automation Lanes icon. (
)
-
Click on “Lyrics” to select the Lyrics Tab.
You’ll notice an empty Lyrics Event for each Note Event; think of these as Lyric containers. This is where you’ll enter your Lyrics.
Double-click a Lyrics Event and begin typing your lyrics. Type naturally, just as using a word processor - the spacebar will jump your pos-
ition from one Note Event to the next. Double-click in an empty space of the Lyrics Lane to enter a Lyric Event independent from a Note
Event.
-
[spacebar] automatically moves the cursor to the next edit position.
-
[-] splits a word into syllables. (This dash will not render in the Lyrics Display window)
-
[_] extends a word across multiple notes (melisma)
You can also paste copied text directly into a Lyrics Lane from your clipboard. With the Edit Window in focus and the Lyrics Lane open,
press [CMD/CTRL+V] to paste. Lyric Events pasted from the clipboard to a Lyrics Lane will be separated word by word in alignment with
the existing Note Events. Syllables, melismas, line breaks, and paragraphs are all supported.
Lyrics Import
Lyrics in MID or MIDI format can also be imported directly from Studio One’s Browser. Simply drag and drop your file from the Browser to
the Lyrics Lane. TXT files can be dragged from your OS file system directly to the Lyrics Lane.
Lyrics Display
To render Lyrics from the Lyrics Lane in the Lyrics Display window, choose the desired Instrument Track from the Lyrics Display drop-
down menu.
Lyrics Lanes

## Scratch Pad

The Scratch Pad is an editing tool in Studio One. Scratch Pads act as quick storage to hold Events, Parts, Lyrics, and entire Song sec-
tions for later use or re-use, reducing clutter in the Arrange view as you assemble your Song. Scratch Pads look and act much like the
Arrange view timeline, sharing the same editing capabilities and displaying the same set of Tracks.

## Scratch Pad

When a Scratch Pad is visible, it is displayed to the right of the Arrange view. Because they act like alternate timelines, clicking the ruler
above a Scratch Pad changes the focus of the transport to the Scratch Pad. Playback then begins inside the Scratch Pad when you
press Play. To switch back, click on the ruler above the Arrange view. This can be done even during playback.
Scratch Pads and the content placed within them are stored with the current Song.
Creating a Scratch Pad
To create and display a Scratch Pad for you to work with, click the Scratch Pad button, which looks like this:
Once a Scratch Pad
exists in the current Song, the Scratch Pad button changes to reflect that fact, and looks like this:
You can click the Scratch Pad
button to show or hide the Scratch Pad display.
You can delete or create additional Scratch Pads as needed by clicking the triangle next to the Scratch Pad button and choosing the Add
Scratch Pad or Delete Scratch Pad option from the pop-up menu.
Just one Scratch Pad can be displayed at a time, but you can switch to any other by clicking the triangle next to the Scratch Pad button,
and selecting the Scratch Pad of your choice from the pop-up menu.
To rename a Scratch Pad, double-click its name in the Arranger Track Inspector, and enter the new name into the provided text field.
Working with Content in a Scratch Pad
To copy Events, Parts, Lyrics, or Arranger Track sections to a Scratch Pad, simply click-and-drag them into the Scratch Pad window. To
copy content from a Scratch Pad to the main timeline, click-and-drag it into the Arrange view. If you wish to move an Arranger Track sec-
tion into a Scratch Pad, removing it from the main timeline, hold [Alt]/[Option] as you click-and-drag the section.
Editing within a Scratch Pad works very much like within the Arrange view, as outlined in Editing.
Loop Playback within a Scratch Pad
Each Scratch Pad has its own loop cycle range setting, distinct from the main timeline. The default loop length is four bars, but you can
shorten, lengthen, or move the loop range within the Scratch Pad timeline as needed, as described in Looping During Mixing.
Using the Listen Tool with Scratch Pads
You can use the Listen tool to audition Events and Parts in Arrange view, in sync with content playing back from the Scratch Pad. To do
so, while the transport is playing, select the Listen tool and click on the desired Event or Part in Arrange view.
Scratch Pads and Score View
The Full Score and Single Track page layouts are not available within a Scratch Pad; only the Continuous mode is available. Note that a
Scratch Pad cannot be printed, so the Printer icon is grayed out.
To learn more about Score View, see The Score Editor chapter.
Bouncing
Bouncing Instrument Parts
When working with musical performance data, users often want to print the audio being generated by external MIDI and internal virtual
instruments to audio so that the Part can be treated like a normal Audio Track. Studio One offers a special feature to accommodate this.
To quickly bounce any Instrument Part to an Audio Track, select the Instrument Part, and then select Bounce Selection in the Event
menu or simply press [Ctrl]/[Cmd]+[B] on the computer keyboard. This renders the selected Instrument Part to a new Audio Event and
places it at the correct Timeline position on a new Audio Track. Note that the Instrument Part's active Insert Effects, as well as Volume
and Pan settings, are rendered to the new bounced audio file. The new Audio Track is created without Inserts, and with Volume and Pan
set to their defaults.
 Bouncing

When an Instrument Part is bounced, the Part is muted, since the new Audio Event is taking its place. The Instrument Part is grayed out
to indicate this. To toggle the mute on the Part, select the Part and press [Shift]+[M] on the keyboard.
Any number of Instrument Parts can be selected and bounced to audio at once, even across multiple Instrument Tracks. A new Audio
Track is created for each Instrument Track whose Part is bounced to audio.
If you want to create a single Audio Event, you should first merge various Instrument Parts on an Instrument Track to create a single con-
tinuous Instrument Part. To do this, select the desired Parts and choose Merge Events, or press [G] on the keyboard.
Bouncing Audio Events
When many edits have been performed across an Audio Track to one or multiple Audio Events, the arrangement can become difficult to
look at and hard to work with. For instance, if a drum loop has been cut into many slices, with some parts duplicated, other parts deleted,
and so on, moving or rearranging the Events can become difficult.
In this case, it may be helpful to render some or all of the contents of a Track to a single, continuous, new Audio Event. To do this, select
the desired Audio Events and press [Ctrl]/[Cmd]+[B], or select Bounce Selection from the Event menu. A new Audio Event is created for
each Track that has an Event selected. The new Audio Events is created and placed according to the position and range of the selected
Events for each Track.
Note that Bounce Selection is unaffected by Track Volume, Pan, and Insert settings, as it is only dealing with the Audio Events exactly as
they exist in the Arrange view. Thus, the result of this process does not affect what you hear; it is simply an organizational tool.
Similarly, drag-and-drop any Audio Event or selected range of audio to a location in the File Browser to export an audio file to that loc-
ation.
Creating Audio Parts
It is also possible to clean up the arrangement by using Audio Parts, where multiple separate Audio Events can be placed into a single
container in the arrangement, while keeping the separate Events accessible in the Audio Editor. To do this, select multiple Audio Events
in the arrangement and then press [G] on the keyboard, or [Right]/[Ctrl]-click and select Event/Merge Events from the contextual menu.
 Bouncing

If you drag-and-drop an Audio Part from the arrangement to the File Browser, an Audio Loop is exported. For more information on Audio
Loops, refer to the Editing chapter.
To dissolve an Audio Part so that the separate Audio Events are again accessible in the arrangement, [Right]/[Ctrl]-click on the Audio
Part and select Audio/Dissolve Audio Part from the contextual menu.
Bounce to New Track
You can create a new Audio Track from a selected Instrument or Audio Track which includes all Insert effects, by selecting Bounce to
New Track from the Event menu, or pressing key command [Ctrl]+[Alt]+[B] in Windows, or [Option]+[Cmd]+B in macOS.
You can also right/[Ctrl]-click on an Event and chose the function from the Events sub-menu.
Bounce File Management
Every Bounce operation creates new audio files that are placed into the Pool for the current Song.
Mixdown Selection
Sometimes, it can be useful to mix down Events from multiple Tracks to a new Track within your Song, such as when you want to con-
solidate a group of backing vocals or drum elements to a single Track. To do so, first select the Events you want to mix down, across as
many Tracks as needed. Then choose Mixdown Selection from the Events menu, or [Right]/[Ctrl]-click one of the selected events, and
choose Mixdown Selection from the pop-up menu.
The resulting mixed-down Track is placed after the last selected Track.
Adding Time to the Arrangement
It is often useful to insert a range of silence into an arrangement, effectively adding time to a section. To do this, select the Range tool in
the Arrange view, then select a range across any Tracks on which you wish to insert silence. With the range selected, press [Ctrl]/[Cmd]+
[Alt]+[I] on the keyboard to insert silence in that range.
Any Events that were in the range where silence was inserted are split, if necessary, and moved to the right across the timeline. If auto-
mation data is present, it is moved to follow the Events. Hidden Tracks are not affected, in this case.
If your chosen range of Tracks spans all Tracks in the arrangement, global parameter settings (such as tempo changes, time signature
changes, and markers) follow the Events, as well. Hidden Tracks are not affected, in this case.
Mixdown Selection

You can also add time to the arrangement without making a selection. Simply place your cursor at the time in the arrangement that you
want the silence to be inserted, and press [Ctrl]/[Cmd]+[Alt]+[I]. A window appears which lets you specify a range of time to insert silence.
Hidden Tracks are split and moved just like visible Tracks, in this case.
Deleting Time from the Arrangement
It can be very useful to remove a section of the arrangement, while simultaneously moving any material that comes after the removed
section back in time, rather than leaving a gap of silence. To do this in Studio One, select a range with the Range tool and then select
Delete Time from the Edit menu or press [Ctrl]/[Cmd]+[Alt]+[D] on the keyboard. You can Delete Time from a single Track, or from any
number of Tracks you select across using the Range tool. Automation data for all affected Tracks is split, trimmed, and moved to match
the new Event position. Hidden Tracks are not affected by this operation.
If no range is selected in the timeline, the Delete Time command brings up a dialog that lets you specify start and end times for the time
deletion.

## Folder Tracks

Keeping the Arrange view organized can be critical to workflow, and Folder Tracks have traditionally helped in this area. Studio One's
Folder Tracks also include Grouping and Busing options, extending improvements to editing and mixing workflow.
Create a Folder Track
If organizing existing Tracks, the simplest method of placing the Tracks into a new Folder Track is to select them all in the Track Column,
then [Right]/[Ctrl]-click and choose Pack Folder from the contextual menu. This creates a new Folder Track and places all of the selected
Tracks in it. Alternatively, you can drag-and-drop any Track onto an existing Folder Track. It is also possible to create a Folder Track from
the Tracks/Add Tracks dialog, just like any other Track. Folder Tracks can contain Audio, Instrument, Automation, and even other Folder
Tracks.
Click the Folder icon in the Track control area to show or hide the Tracks within the Folder in the Arrange view. If Link expansion and vis-
ibility of Folder Tracks is enabled in the Console Visibility Options, the related Channels are shown and hidden in the Console as well.
Note that Folder Tracks also have Mute, Solo, Record, and Monitor Enable buttons. Clicking on these engages the appropriate action for
any Track within the folder.
Folder Track Grouping
Deleting Time from the Arrangement

Clicking the Group icon on a Folder Track creates a Group with the name of the Folder Track and places all Tracks it contains into the
Group. This is exactly the same as selecting all of the Tracks and grouping them with [Ctrl]/[Cmd]+[G]: The Tracks are selected together
in the Console and Arrange views, and the Events on the Tracks are edited together. If the Group icon is engaged on a Folder Track,
clicking it again removes the Group.
If a Track is already in a Group prior to being placed in a Folder Track, and the Folder Track Group is engaged, the Track is placed in the
Folder Track Group when it is placed in the Folder Track. If removed from the Folder Track, a Track retains its Group setting.
Folder Track Editing
When a Folder Track is collapsed, a single "Event” with lanes representing each Track in the Folder across the arrangement is displayed.
It is possible to directly edit this consolidated Event, including Size, Move, Cut, Copy, Paste, and Duplicate. This ability saves time in
cases where simple edits do not require viewing a particular Track in the Folder or even grouping the Tracks within.
Folder Track Busing
Clicking on the Bus selection box to the left of the Group icon on a Folder Track allows the selection or creation of a Bus Channel.
Choose from an existing Bus Channel, or add a Bus, to switch the output for all Tracks contained in the Folder Track to a Bus Channel. If
adding a new Bus Channel, the Bus takes the name of the Folder Track.
If a Bus selection is made, the Folder Track acts as an effects-drop target for the Bus Channel when dragging effects from the browser
onto the Folder Track.
As with Folder Track grouping, if the Folder Track has a Bus Channel selection, any Track added to the folder is routed to that Bus when
placed in the Folder Track. If removed from the Folder Track, a Track keeps the Bus as its Output Channel selection.
For Instrument Tracks, the Track's related Audio Channel is routed to the Folder Track Bus Channel. The related Audio Channel is the
one shown in the Inspector under the Out and In selections for an Instrument Track. As noted elsewhere in this manual, the Audio selec-
tion for an Instrument Track is purely organizational and allows Studio One to accomplish workflow enhancements like the afore-
mentioned. If a virtual instrument is using multiple Output Channels, you should take the time to organize which Instrument Tracks routed
to that virtual instrument are related to which Output Channels in the Inspector.
Folder Track Nesting
When Folder Tracks are nested—that is, when one Folder Track is placed inside another—the Folder Track Grouping and Busing
options still only apply for the Tracks within each folder. Here is an example:
Tracks 1 through 8 are in Folder Track A, which has Group enabled and is routed to Bus A. Tracks 9-12 are packed to a new Folder B,
Group is enabled there, and a new Bus B is created. Folder B is then dragged into Folder A. The Tracks in Folder B are still grouped in
Group B, and are still routed to Bus B. The only difference is organizational: Hiding Folder A Tracks also hides Folder B.
Track List
The Arrange view Track list is opened by clicking on the Track List icon in the upper left corner of the Song page. The Track list gives an
overview of all existing Tracks. Each Track has a drop-down arrow that, when clicked, displays related Tracks, Envelopes, and Layers.
Level meters to the far left of Track names indicate levels during playback for every Track. You can click-and-drag the Track icon next to
the Track name to change the Track order. If any Track is in a Group, the Group name is displayed next to it in the Group column of the
Track List.
Tracks can be hidden or shown by clicking the round button to the left of the Track name. Click-and-drag quickly through the round but-
tons to hide or show any number of Tracks. Hiding a Folder Track also hides all of the Tracks it contains. Hidden Tracks are not visible in
the Arrange view, but they remain faintly visible in the Track List.
View only the Tracks you want to see by typing in the Filter field near the bottom of the Track List, placing a comma between search
terms. For example, to view only Tracks named "Piano" and "Organ", you could enter "pia, org" in the Filter field. Clear the Filter field by
clicking the X. Preset filter options are available through the Track Visibility button, described below.
 Track List

To find a specific Track, use [Ctrl]+[Alt]/[Option]+[T] to open a dialog box, then type the Channel name or number. This method works
whether the Track List is open or not.
Icons for each Track type are visible at the bottom of the Track List. Click them to hide or show all Tracks of that type.
The Track List can be synced to the Console Channel List, so that any Tracks hidden or shown in the Track List have their related Audio
Channels hidden or shown in the Console, and vice versa. This is done inside the Channel List Options window (see Visibility Options).
The Track Visibility button
The Track Visibility button in the lower right corner (...) opens a menu of useful Track List filters. Options include:
-
Show All Tracks
-
Show Selected Tracks
-
Show Tracks with Events under Cursor
-
Show Tracks with Events in Loop Range
-
Show Soloed Tracks
-
Hide Empty Tracks
-
Hide Disabled Tracks
-
Undo/Redo Visibility Change
An independent Undo/Redo history is maintained for up to 10 Visibility changes. This includes Tracks that are shown or hidden manually
using the round buttons in the Track List, Layers that are expanded or collapsed, etc.
There are many more assignable Track visibility commands in the Keyboard Shortcuts menu at Studio One/Options/General/Keyboard
Shortcuts (macOS: Preferences/General/Keyboard Shortcuts). For more information, see  Mapping Custom Key Commands .
The Track List and Groups
Tracks can be placed in a Group so that any edits done to an Event on one Track in the Group are automatically done to all Events for
each Track in the Group. For instance, you may wish to group all of your drum Tracks together so that when the Events are cut and
moved, the relative timing between the Tracks remains intact.
The quickest way to create a Group is to select the desired Tracks and use [Ctrl]/[Cmd]+G. For additional details on working with Track
Groups, see Edit Groups.
The Track List and Scenes
Scenes provide an easy way to save and recall different configurations of Tracks and Channels, as well as different settings for the FX,
etc. For example, let's say you have defined a Scene called "Drums." Selecting that Scene recalls the show/hide settings, which shows
the selected drum Tracks and Channels and hides all of the others. You can then make as many changes as you like to this Scene, save
those as another Scene, and then go back and forth between them to see which you prefer. Any number of Scenes can be saved and
recalled within each Song.
Scenes can be accessed through the Show Scenes button at the top of the Track List. There's also a Show Scenes button available in
the Console navigation panel.
Alternatively, use [Ctrl]+[Alt]/[Option]+[S] to open a dialog box, then type the Scene name or number. This method is available whether
the Scenes list is open or not.
For more details, see the Scenes section of the Mixing chapter.
 Track List

Track and Channel Icons
Track and Channel Icons offer a quick and convenient way to label your Tracks and Channels with simple Icons. Activate them by open-
ing the options (wrench) menu in the Arrange Window or Console.
Activating Show Channel Icons in the Console Options menu will render the icons in the Console and Inspector. Activating Show Track
Icons in the Arrange Window Options menu will render the Icons in the Arrange Window.
Once activated, Track Icons can be chosen by clicking on the left
end of the Track header, the bottom of a Channel, or the Icon slot
in the Inspector to open an Icon navigator categorized by instru-
ment type.
Track icons can be applied to any Track or Channel type.
To remove a Track Icon, open the Icon navigator and click
“Reset.”
Studio One’s Track Icons are identical to those used in Capture
sessions; Capture sessions opened in Studio One will import all
Track Icons.
 Track and Channel Icons
