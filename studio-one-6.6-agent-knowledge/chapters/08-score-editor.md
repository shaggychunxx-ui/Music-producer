# The Score Editor

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 192–210
> **Slug:** `08-score-editor`

**Agent topics:** `score`, `notation`, `staff`, `drum notation`, `tablature`, `lyrics`, `Notion`

---

The Score Editor
Studio One Professional provides the ability to view, enter, and edit notes in standard music notation through its Score Editor. A Score
can display any number of Tracks simultaneously. Notes can be added to the Score and edited in many ways, including the ability to add
musical symbols for articulation and dynamics. The Score can then be printed or output as a file and shared with other musicians.
The View buttons on the left side of the Note Editor toolbar let you transition seamlessly between three approaches of capturing and refin-
ing your creativity. Follow these links for descriptions of Piano view and Drum view. In this chapter we will focus on the Score view.

## Score Editor Overview

Click the "treble clef" Score View button to access the Score Editor. In this view notes can be entered on a musical line (or "staff") using a
mouse and a computer keyboard, or entered in real-time or step recording modes using an external controller. Musical symbols for artic-
ulation and dynamics can be added, and these symbols also enhance the playback of the associated Track.
The Score automatically scrolls during playback, and while editing it jumps instantly to any place you click on the timeline. The window
can be detached, so you can look at it side-by-side with the same note data in Piano view or Drum view.
Grand staff for keyboard instruments is included, which shows two staves for a single instrument. This allows notes to be allocated
between the left and right hands, and you can move pitches between the staves once they have been entered. Note pitches are shown
with the enharmonic ‘spelling’ that conforms to the current key signature (for example, in the key of C minor an Eb is shown, rather than a
D#). Proper formatting is automatic for note spacing, beaming, stem length and direction, ledger lines, etc. Manual formatting options
include trills, 8va/8vb lines, clefs for various instruments, and more.
Furthermore, Tablature Staff Type is available in two variants: Tablature and Standard + TAB. These Staff Types are well-suited to vari-
ous fretted instruments, and includes support for various alternate tunings of guitars, basses, banjoes, and more. Note entry, note edit-
ing, and re-arrangement of chord fingerings are all possible while using the Tablature Staff Types.
 Song Meta-Information can be entered at Song/Song Setup/Meta Information, after which the Title, Album, and Songwriter/Composer
for the Song appear at the top of the Score (Full Score and Single Track page layouts only).
Many options are provided for viewing and printing a Score, including notation size, staff spacing, and bar numbers, to name a few. Each
feature is described in the pages ahead.
Keep in mind that the Score Editor displays and prints only the region between the Start and End markers. Anything beyond those mark-
ers is not included.
How the Views Interact
When note pitch or duration are changed manually in Piano, Drum, or Score view they also change in the others. However, musical sym-
bols added to the Score affect playback but don't affect how notes are displayed in Piano and Drum views (with the exception of adding a
sharp or flat sign to a note, which changes its pitch).
Key Signatures and Score View
The key signature of the current measure determines how the pitches are displayed on the staff in terms of their enharmonic spelling
(e.g., whether a pitch is shown as an Ab or G#). The key signature also dictates what you will hear when you move notes up and down
diatonically, either with the mouse or the up and down arrow keys.
The Score Editor

When working in the key of C major, for example, if you want to add an E-flat to the score, place the note on the E and then select the flat
sign (b) from the Accidentals menu in the Symbols panel.
To set a key signature for the Song, click the [Key] button in the Transport and select the key of your choice from the pop-up selector that
appears. It can also be derived automatically from an Instrument Part or an Audio Event as described in Getting Started with the Chord
Track. If the Song changes key signatures, see Signature Track for more information.
Time Signatures
The time signature of the Song is automatically part of the Score. Note that time signature changes can be added in the Signature
Track, and appear instantly in the Score.
Familiar Actions in Score View
The Score Editor has some of the same recording and editing functions as the Piano and Drum views, with a few changes as noted in this
section.
Three Ways to Enter Notes
As in the Piano and Drum views, you can use three different methods to enter notes in Score view:
-
Real time Notes can be entered in real time using a keyboard controller; just click the Record button in the transport and start
playing.
-
Step time Entering notes in step-time with a keyboard controller is also possible; just click the Step Record button
in the
Score view toolbar and play the keys. Note values and rests can be selected using the computer keyboard as described here.
-
Manually Notes can be entered one at a time using the Paint tool, which is also used to enter articulations and dynamic
markings.
Using the Tools
The Arrow tool is used the same way as in the Piano and Drum views: to select notes, to place the cursor at a specific location, etc.
Selected notes are displayed in orange.
The Paint tool is used to add notes to a staff. Notes are added according to the current key signature, not the Track Scale. Line Drawing
mode is not available.
Remember that you can select the Arrow tool with the [1] key and the Paint tool with the [2] key. This allows you to switch between them
very quickly.
The Cursor
When you click inside the Score with the Arrow tool, a vertical blue line appears on one staff at that location. During playback, the blue
line becomes a bar that moves across the entire Score. This is the playback cursor. When playback stops, the blue line returns to the
selected staff and indicates the current position.
Zoom
In Score view the Time Zoom control zooms both vertically and horizontally. You can also zoom by holding [Ctrl]/[Cmd] and using the
scroll wheel.
Score Editor Toolbar
The Score Editor toolbar makes the creation of a Score fast and intuitive. Using the number keys to select tools and note values, and a
mouse to place notes and symbols, a full Score can be produced very quickly. A keyboard controller is not required, although the process
is even faster with one.
Using the Arrow Tool
Use the Arrow tool to select locations and items inside the Score, including notes, rests, dynamic markings, and articulations. Click an
item inside a staff to select it, and it turns orange. To select multiple items, click a blank spot in any measure and drag across the items
you want to select. Hold [Shift] and then click or drag to select items from multiple staves.
Score Editor Toolbar

The cursor can be placed in front of any note or rest in a measure. Clicking inside an empty measure places the cursor at the beginning of
the bar.
Selected notes can be edited using various commands, or you can cut/copy/paste/delete them using standard computer key com-
binations. Many options are available in the [Right]/[Ctrl]-click contextual menus.
Shifting Notes
To change the pitch of a note using the Arrow tool, click the note and drag it up or down. To change the pitch of a chord or a series of
notes after selecting them, use the following keys:
-
Up/Down arrow shifts the notes within the key signature if one has been selected, or diatonically within the key of C if a key has
not been defined for the Song.
-
[Ctrl]/[Cmd] + Up/Down arrow shifts the notes chromatically.
-
[Shift] + Up/Down arrow shifts the notes by octaves.
Using the Note Tools
Select the desired note value from the toolbar. You are now able to add notes to the score with the cursor. We'll walk through the basics
in this section; follow this link to learn the quick entry method.
When hovering the cursor over the score, the will become a pencil, with a gray note of the selected value linked to it. The gray note
changes its pitch as it is moved up and down the staff.
Click the staff at the desired location to place a note there. The note turns black to indicate that it has been added to the staff. You can
make a chord by placing more notes on different pitches at that location, or move the cursor to another location in the Score and place
some notes there.
If you want to place a rest in the Score instead, select the note value first and the equivalent rest value appears in the toolbar to the right
of the 64th note.
Remember, there's a faster way to do all of this. But here are two things you might want to know now.
-
A red note or rest means you've put too many items in that bar. Try a shorter note value or place the extra item in the next bar.
-
It isn't necessary to fill a measure with notes or rests right away. Just put the notes in the right bars first, if you like. Rests can be
added easily using the Fill with Rests feature, which is described next in the Action menu section.
For more details on using the Note tools, see the Editing the Score section.
The Action Menu
Score Editor Toolbar

Note: Many of the following items are also available in one or more of the contextual menus. [Right]/[Ctrl]-click a selected note for one
menu; [Right]/[Ctrl]-click a group of selected notes for a different menu. Still another menu appears when you [Right]/[Ctrl]-click inside the
Score without any notes selected. See Contextual Menus in the Editing the Score in Notation section for full details.
-
Fill with Rests This option places the appropriate rests in any empty sections of the selected measures, including whole-meas-
ure rests, up to the limit set by the time signature. To use it, click-and-drag across the desired areas of the Score and then select
this option from the Action menu. You can also use [Ctrl]/[Cmd]+[A] to select all measures in the current staff, or use the con-
textual menu option Select All on Tracks to select the entire Score, and then select Fill with Rests from the Action menu. If no
selection is made, then all measures are filled with rests from the beginning up to the current caret position.
-
Fill with Rhythm Slashes This option places a stemless rhythm slash on each beat in the selected measure as long as the
measure is empty of notes and rests. It is also possible to change existing notes to slashes—just select them, right click, and
select Toggle Rhythm Slash from the contextual pop-up menu.
-
Tuplets are notes whose division differs from the normally permitted subdivisions of the current time signature (for example, a
triplet in 2/4 time). They can be made from groups of notes inside a single measure of a single staff. They are not available
across bar lines, or if notes from different staves are selected.
-
-
Make Custom Tuplet... This option allows you to make more unusual tuplets in addition to the standard tuplets such as
triplets, etc. You also have greater control over the notation used to represent the tuplet.
-
-
Fit X Into Y Group the number of selected notes (X) into the space of the specified denominator (Y).
-
Show as ratio If you want to display a tuplet as a ratio instead of a single number, engage this option. The tup-
let will be displayed as 4:3, 6:4, 5:8, etc.
-
Brackets A bracket is often placed around tuplet as a visual aid. If deactivated, the brackets are hidden and
only the number is shown above the grouped notes. The rhythm of the notes is the same, with or without the
brackets.
-
Make Tuplet Use this option when the grouping of notes is fairly standard (triplets, quintuplets, etc.). If you want to spe-
cify the notation as a ratio, etc., use the Make Custom Tuplet option.
-
Switch Staff This action is only available when the Grand staff is used. It allows you to switch a note from the upper staff to the
lower staff, or vice versa.
-
Transpose Use this to transpose the selected notes up or down after you specify the Interval, Interval quality, and Octave range
of the transposition. These options are similar to those described in the Transposing Notes section. They can force notes or
chords to conform to the key (Diatonic), allow them to maintain the same interval relationships, or follow a number of other per-
mutations, all while transposing up or down in specified intervals by as much as three octaves.
Score Editor Toolbar

Note / Rest Values
Note value Seven options from whole note through 64th note. These also can be selected with the number keys on the keyboard, as
described here. For triplets, etc., use the Tuplet options in the Action menu or the contextual menus.
Rest The note value for rest symbol is always the counterpart of the selected note value. These also can also be selected with the num-
ber keys on the keyboard; they follow the same keys as the note values. Simply toggle between the note or rest by pressing the key
repeatedly.
Augmentation Dots A single dot lengthens the note value by half (i.e., a dotted eighth note equals three sixteenth notes). A double dot
lengthens the note by three-quarters of its original value (i.e, a double-dotted quarter note equals three eighth notes plus a sixteenth
note).
Voices 1-4
Up to four voices can be notated in a single staff. Multi-voice input enables simultaneously- sounding notes with different durations—for
example, a quarter note can be notated in Voice 1 and two eighth notes in Voice 2.
-
Voice 1 (Upper Voice)
By default, all notes you enter are considered to be part of Voice 1.Until you add Voice 2, note stems of Voice 1 will point either
up or down, depending on the degree on a staff.
-
Voice 2 (Lower Voice)
Switching to Voice 2 triggers two events: all succeeding notation you enter appears as Voice 2 (stems down). At the same time,
every time you add a Voice 2 note, any Voice 1 note(s) in the same beat that happen to have stems down now have their stems
pointing up.
-
Voices 3 and 4
With three- and four-voice parts, the number of voices determine the stem directions.
-
If you use four voices, then voice 4 note stems point down and all other voices point up.
-
If you use three voices, then voice 3 note stems point down, and voices 1 and 2 point up.
Notehead Symbols
This opens a menu of notehead symbols that you can use with the Note tool:
-
Normal is the one most commonly used for instruments and voices.
-
X-Symbol notes indicate an indeterminate pitch (e.g., a spoken word, a noise, etc.).
-
Triangle represents a note to be played by the eponymous percussion instrument.
-
Slashed notes often indicate a rim-shot played on a percussion instrument.
-
Circle-X can represent an unpitched percussion part or a muted note (triangle, guitar, etc.).
-
Diamond noteheads are often used to indicate a harmonic played on a string.
Step Record / Undo
Step Record Activate this button to enter notes from an external controller in step time.
Move backwards/undo This can be used while step-recording to undo multiple entries without having to move your hand to the com-
puter keyboard and type [Ctrl]/[Cmd]+[Z].
Autoscroll
When this is button is engaged the Score view window follows the timeline position during playback. Disengage this button to freeze the
Score view window at its current location.
Layout Style
The Layout Style buttons determine how the Score is displayed and printed.
-
Continuous Layout displays the Score horizontally with no page breaks, similar to the Arrange view. The Score can't be printed
when this Layout Style is selected. Note also that the Song meta-information is not displayed at the top of the Score (Title, Com-
poser, etc.).
-
Full Score Page Layout can display and print multiple Tracks.
-
Single Track Page Layout shows the Score for the most recently selected Track.
Score Editor Toolbar

These three buttons are linked to the Layout Style options in the Layout panel of the Note Editor Inspector. When a Layout Style is selec-
ted in either location, the change is made in both.
Note that the Full Score and Single Track page layouts are not available within a Scratch Pad; only the Continuous mode is available.
Note also that a Scratch Pad cannot be printed.
If  Song Meta-Information has been entered at Song/Song Setup/Meta Information, the Title, Album, and Songwriter/Composer for the
Song are shown at the top of the Score (Full Score and Single Track page layouts only). This information can be accessed from Score
view; simply click one of those fields inside the Score to open the Song Setup window. Enter the desired information and click OK to
close the window. The new information now appears at the top of the Score.
Print the Score
When you're ready to print the Score, click the Printer icon or navigate to Song/Print Score.... Most recent computer operating systems
also offer an option to save the Score as a PDF file from the print dialog box.
Note that the Continuous Layout can't be printed, so the Score view switches automatically to one of the other Layout Styles when the
Printer icon is selected.
Remember that Score view only prints the region between the Start and End markers. Anything beyond those markers is not included.
Remember also that the contents of a Scratch Pad can't be printed, so the Printer icon is grayed out.
Detach and Pin
Detach This button allows you to detach the Score view window and place it in another area of the screen, or even move it to a different
monitor. You can then select a different Editor view in the main display window if you like.
Pin When the Score window has been detached and placed at the desired location, click the Pin icon to lock its status and position. This
will keep it from closing when [F2] is used to toggle the Editor window status.
Close Click the X to close the Score Editor window. This can also be done with the [F2] key.
Note Editor Inspector (Score View)
The Note Editor Inspector on the left side of the window offers some unique features in Score view. It is divided into two areas, with Track
settings in the top half and three selectable panels in the lower half.
Note Editor Inspector (Score View)

The following settings are located at the top of the Note Editor Inspector. They are available regardless of which panel is selected (Sym-
bols, Track, or Layout).
-
Track List Click this button to open a list of all of the Instrument Tracks in the song. You can show or hide the staves of each
Track in the Score using the Show/Hide buttons to the left of the Track name. It is possible to click-and-drag through many but-
tons and add their Tracks to the Score view very quickly. Click the Lock Track List icon to preserve the Score view Track selec-
tion even if you switch to another Track in the Arrange view.
-
Track Selector To view only one staff and close the others, click the Track name at the top of the Note Editor Inspector and
select the desired Track.
-
Instrument Click the keyboard icon to open the Instrument Editor for the selected Track.
-
Mute/Solo These buttons affect the Console Channel and the Track.
-
Audition Notes Engage this option to hear notes when they are selected with the mouse. To hear a chord, click anywhere on
the stem of the chord.
-
Default Velocity This is the value used when adding notes to the Score with the Paint tool. Dynamic markings that you add
affect the playback velocity, but those changes are made "behind the scenes"; they are not visible in Piano or Drum views.
Symbols Panel
The buttons in this window are used to select dynamic markings and performance articulations and add them to the Score. As with the
Default Velocity setting, these markings affect the playback of the Track, but the changes are made "behind the scenes"; they are not vis-
ible in Piano or Drum views.
Many of the buttons have arrows that appear in their bottom corners as the cursor hovers over them. These indicate the presence of pull-
down menus that allow you to specify the impact or behavior of the selected icon when it is applied to the Score.
Note Editor Inspector (Score View)

After selecting a symbol you must click a note to anchor the symbol. Some of the symbols indicate changes that are made over time, and
in that case you must click-and-drag across a range of notes.
These Symbols can also be assigned to trigger Sound Variations, allowing for a method of assigning these performance techniques in a
manner more intuitive to composers. Visit Sound Variations to learn how to set it up!
-
Accidentals The key signature dictates whether a note is part of the scale or not. Accidentals are used to mark a note that is out-
side the scale, such as an Ab in the key of F major. Single, double, and natural options are available.
-
Enharmonic spelling Use this to change the enharmonic spelling of a note (e.g., from Eb to D#, or vice versa).
-
Tie These are placed between two or more identical pitches that are adjacent, either inside a bar or across a bar line. The notes
can have different values.
-
Slur After selecting this option, click the first note and then drag the slur to the end note in the group of notes to be slurred.
These can be placed above or below the staff, and can be nested inside longer slurs. Once you have placed a slur you can
adjust its overall position, its start and end point, and the curve itself. To do this, use the Arrow tool to select the existing slur, and
then use the slur control points to adjust the slur as desired.
-
Articulation Select the appropriate icon for various types and combinations of staccato and accent.
-
Articulations of force These indicate a sudden, forceful change in dynamics. The fortissimo options tell the musician to play
with even greater forcefulness.
-
Dynamic Select one of ten options that range from pppp (Piano piano pianissimo) to ffff (Forte forte fortissimo).
-
Hairpins These markings indicate a gradual increase or decrease in dynamics. Select the appropriate option, click a note, and
then drag the hairpin to the end note or bar line by which the change in dynamics should be complete.
-
Trill There are three choices: Trill, Trill sharp, and Trill flat. Trills are always above the original pitch, but the width of a trill
depends on the enharmonic relationship of the note to the key of the Song; it could be a half-step higher, a whole step higher, or
as wide as a minor third higher than the original pitch. Click a note to add a trill, or click the note and drag to show a longer trill.
-
Tremolo There are two types and a total of six options. You can use a tremolo marking as a shorthand to represent repeated
rhythmic figures. A single slash tremolo is an eighth note tremolo, a double slash tremolo is a sixteenth note tremolo, and a triple
slash represents a faster 'unmeasured' tremolo.
There are two types of tremolo in Studio One:
Note Editor Inspector (Score View)

-
The single note tremolo (or slash tremolo) affects the single note or chord to which it is applied.
-
The two-note or fingered tremolo (or shake) is a tremolo between two alternating notes or chords. Fingered tremolo is
represented by a unique form of notation, in that the total duration of the tremolo is the count of one of the notes.
-
Arpeggio There are three choices: standard (up), up (with an up arrow), and down (with a down arrow). This only works on a
chord (i.e., notes that are stacked on the same event). Remember this a note effect; it does not change the position of the ori-
ginal notes in Piano view or Drum view.
-
Glissando/Portamento Select the preferred option, then click a note to add the effect between it and the next note.
-
Clef tool There are ten clef options in order to add clef changes throughout your track.
-
Octave signs There are four options: 1 octave up or down, and 2 octaves up or down. Select one, then click-and-drag across
the range to be transposed. This is a note effect; it does not change the original notes in Piano view or Drum view.
-
Bends There are thirteen options for bends! Select the preferred options, then click a note to add the effect. Some options, like
Bend String, support multiple notes at a time. Once added, you can drag the bend to alter either its length or how wide the bend
should be in terms of pitch.
Track Panel
The Track Panel helps you configure the Score quickly and properly for each Track. Its settings only affect Score view for the Track that
is selected in the Inspector, even when more than one Track is visible in the Score. These settings also determine the appearance of the
printed Score, as described below.
-
Apply Staff Preset Click the arrow to open a list of preset staves that are grouped in various categories (Strings, Woodwinds,
Drums/Cymbals, Vocal, etc.). Each preset staff automatically selects the appropriate Transposition value and other settings for
the instrument. For example, when the Alto Sax preset is selected, the Transposition becomes Eb since an alto saxophone is an
Eb instrument. The key signature of the Track is also transposed accordingly; e.g., if the song is in G, the Alto Sax staff is dis-
played in the key of E.
-
Name This field is automatically filled with the name of the Track. It can be edited here, which also edits it there, and vice versa.
-
Abbreviation An abbreviation for the selected Staff Preset is entered automatically, but you can enter a different one if you like.
-
Staff Type Six options: Standard (one staff), Tablature, Standard + TAB, Grand Staff, Drumset, and Single Line. The appro-
priate setting is chosen automatically for the selected Staff Preset, but you can override that if you want.
-
Show Chords Tick the box to show Chords from the Chord Track in the selected staff. Chords will automatically display the cor-
rect transposition if the staff is for a transposing instrument.
-
Tab Type Available only with the Staff Type set to Tablature or Standard + TAB, this field lets you choose from a diverse list of
14 fretted instruments of various string counts and tunings for use with the Tablature editing interface.
-
Tab Strings A non-configurable reference for the string tunings of the Tab Type chosen in the preceding menu.
Note Editor Inspector (Score View)

-
Tab Strings Displays the default tuning for the instrument selected in the Staff Preset, if it’s a stringed instrument. Click to enter
your own alternate tunings via the keyboard, if desired.
-
Circles in TAB Tick to display circles around the fret numbers in the Tablature for half and whole notes.
-
Show Stems in TAB Tick to display stems under the fret numbers in Tablature. These will align with the stems of notes dis-
played in the Standard + TAB Staff Type.
-
Transposition There are two settings available here:
-
Chromatic offset This sets the Transposition root note. The correct setting is chosen automatically for the selected
Staff Preset. For example, a setting of Bb is chosen for a clarinet or a tenor sax, since they are Bb instruments (i.e.,
when the musician plays a C it sounds like a concert Bb). You can change this setting manually if you like.
-
Octave This lets you place the score in the most readable range (i.e., the minimal number of ledger lines). Settings
include Same Octave (no octave shift), or +/- up to 2 octaves.
Layout Panel
The settings of the Layout panel affect what is seen in the Score view and what is printed. The first three settings are separated from the
others because they are always present regardless of which Layout Style is selected.
-
Layout Style lets you select the desired layout for the Score,
and it also changes the number of available parameters
below the Page Layout divider. It is linked to the toolbar but-
tons; change one and the change is made in both places.
-
Continuous displays the Score horizontally with no
page breaks, similar to the Arrange view. The Score
can't be printed when this option is selected, and so
the Page Layout settings are hidden. Note also that
the Song meta-information is not displayed at the top
of the Score (Title, Composer, etc.).
-
Pages can display and print multiple Tracks. The
number of Tracks that can fit on a page is determined
by which Tracks are shown or hidden in the Track
List and the Page Layout parameters described
below.
-
Single Track displays and can print the most
recently selected Track.
-
Tempos lets you specify whether all tempo settings are
shown in the Score (Show Tempos), all are hidden (Hide Tem-
pos), or only the initial tempo is shown (First Only).
-
Enable Transposition allows the key signatures within the
Track to change when the Track is transposed. To prevent
this, uncheck the box.
-
Final Bar lets you specify the exact number of bars you
would like displayed in the score.
Note Editor Inspector (Score View)

Page Layout
All of the settings below this divider let you specify the final printed output (notation size, etc.), and also determine how the Score is
rendered on your display. They are not available for the Continuous page layout. Note that the Multi-Measure Rests setting is only avail-
able for the Single Track page layout.
-
Page Size Click the arrow to open a list of standard printing formats.
-
Orientation Select Portrait or Landscape orientation for the Score. This allows for different sizes of monitors, sheets of paper,
etc.
-
Margins Depending on the printer and whether the final result will be bound or loose leaf, these settings let you specify how
close to the edge the music can be.
-
Notation Size Lets you adjust the size of the notes and other markings in the Score.
-
Staff Spacing This sets the amount of space between the staves in a system.
-
System Spacing This allows you to specify the amount of empty space between systems (i.e., groups of staves). If only a few
instruments are used on one Song, a larger value can make the Score easier to read. But if the Song uses a full orchestra a
lower value helps fit all the instrument parts on a single page. Use in conjunction with the Notation Size and Staff Spacing set-
tings for optimal viewing.
-
Multi-Measure Rests (Single Track only) This consolidates adjacent measures of rests into a single measure, with a number to
indicate how many empty measures should be consolidated into one multi-measure rest. If you want all empty measures to be
shown individually, select None.
-
Bar Numbers Use this to specify whether you want to hide the bar numbers (None), have them appear only over the first bar in
each set of staves (Each System), or over every bar (Each Measure).
-
Text Size This adjusts the size of the font used for the Song Title, Album, and Songwriter/Composer fields. Select No Titles to
hide that information; the rest of the options display those fields in the size you select: Tiny, Small, Normal, Medium, Large, or X-
Large.
-
Font Use this menu to select the text font for viewing and printing the Score. Quite a bit of personalization can be done here, so
your charts are distinctive. You can even use a different font for each Song, if you like.
Editing the Score Using Standard Staff Types
The basics of using the Paint tool to enter notes are covered in the Score Editor Toolbar section. Here we'll describe the advanced fea-
tures of the Score Editor and also provide some helpful shortcuts. Note that the below applies to the following Staff Types as chosen by
the Note Editor Inspector: Standard, Grand Staff, Drumset, or Single Line. See Editing Scores in Tablature for information on editing
your score using the Tablature or Standard + TAB Staff Types for fretted instruments.
Quick Entry Methods
Without a Controller
A combination of keyboard shortcuts and mouse actions can be used for the rapid entry and editing of notes in Score view.
1.
Press the [2] key to activate the Paint tool.
2.
Select the desired note value with keys [3]-[9].
3.
Press the same key a second time to select a rest of the same value. (Steps 3 and 4 can be swapped.)
4.
To select a dotted value for the note or rest, press the [0] key repeatedly to reach the dotted and double-dotted symbols. Press
[0] a third time to remove the dot.
5.
Click the left mouse button to enter the note or rest.
6.
Use the mouse to place the cursor anywhere on the Score, or use the left and right arrow keys to move within the current staff.
The next event can be added between two existing events.
7.
To add notes to a chord, select the matching note value in the tool bar, then click on the staff to add the note.
Controller and Mouse
The process is slightly different when you are using a keyboard controller.
1.
Click the Step Record button. You can play the keys on the controller at any time during the following steps to add an event and
advance the cursor.
2.
Select the desired note values with numbers [3]-[9] on your computer keyboard.
3.
Press the same computer key a second time to enter a rest of the same value.
Editing the Score Using Standard Staff Types

4.
To select a dotted value for the note or rest, press the number [0] on your computer keyboard repeatedly to reach the dotted and
double-dotted symbols. Press [0] a third time to remove the dot.
5.
Play a key on your controller to enter the note or chord and move the cursor to the next location. You can also place the cursor
anywhere on the Score, even between two existing notes. Keep in mind that one or more events to the right of the cursor could
be replaced by the next key you play, depending on the selected note value.
6.
Repeat steps 2-5 while playing the keyboard until you have entered all of the desired events. You can also add ties whilst in step
time, by clicking the tie icon with the mouse in between entering two notes of the same pitch.
7.
Press the [2] key to exit Step Record mode.
You can also enter notes from your controller while recording in real time; just use the recording capabilities of your DAW as you normally
would to capture a live recording.
Change a Rhythmic Value
To change the rhythmic value of an existing note or rest:
-
Click the desired note value in the tool bar, or use the appropriate number key. This automatically selects the Paint tool.
-
If the desired event is a rest, select the rest symbol on the right, or press the same number key a second time.
-
Click over the existing notehead and its value will change to the new value.
To change the rhythmic value of an entire chord:
-
Click the desired note value in the tool bar, or use the appropriate number key. This automatically selects the Paint tool.
-
Click over the existing notehead in the chord. All notes in the chord will change to the new duration.
When Events Are Red
If you see notes or rests that are red, that means you've exceeded the limits of the time signature for that bar. Studio One will add as
many events as possible within the bar, but the current time signature is always maintained. During playback the excess events are
skipped and the next bar plays normally.
There are several ways to eliminate red events:
-
Select a shorter note value and replace the events
-
Place the extra events in a different bar, or
-
Add a time signature change to the Signature Track at that location if those events belong in the same bar.
Staff configuration
Choosing the Initial Clef
Left-click the clef in the Continuous Layout, or the initial clef in the Pages Layout, to view all available starting clefs. You can make clef
changes later on in your Track using the clef tool. There are ten options, including Treble, Bass, C clefs, Octave clefs, and two neutral per-
cussion clefs. Make a choice and the menu will close.
Key and Time Signatures
Key and time signatures can be set in the Transport or in the Signature Track (above the Arrange view). You can change them through-
out the Track, too. Just add a new key or time signature to the Signature track, and it appears immediately in the Score view. Key sig-
natures can be detected automatically, too; see Detecting Key Signatures.
Contextual Menus
Score view has three contextual menus that are accessed inside the Score. Each menu has unique options and ones it shares with the
other menus.
Editing the Score Using Standard Staff Types

The Staff Menu
[Right]/[Ctrl]-click in an empty area of the staff to view the options of its contextual menu.
-
Arrow Tool Use this option to select the Arrow tool.
-
Paint Tool Use this option to select the Paint tool.
-
Select All Use this option to select all events in a single staff, or to select all events in both staves when the Grand staff is being
used for the selected Track.
-
Select All in Staff Use this option to select all events in a single staff when the Grand staff is shown. Click inside the desired
staff first, then select this option from the contextual menu.
-
Select All on Tracks This option selects all events in all staves that are visible in the Score.
-
Deselect All Use this option to deselect every item that is currently selected.
-
Cut/Copy/Paste/Delete These perform the same function as the computer keyboard actions.
-
Recent items Choose from a short list of recently-performed commands, good for quickening repetitive tasks.
-
Score A submenu of context-senstive score-specific commands:
-
Fill with Rests This option places the appropriate rests in any empty sections of the selected measures, including
whole-measure rests, up to the limit set by the time signature. To use it, click-and-drag across the desired areas of the
Score and select this option from the Action menu.
To fill the entire Track with any rests that are needed, click anywhere within the staff and use [Ctrl]/[Cmd]+[A] to select
the entire Track, then open the contextual menu and select Fill with Rests. If no events are selected, rests of the proper
duration are placed in every available location to the left of the cursor, including the measure where the cursor is placed.
-
Rebuild Score This option re-creates the complete representation of the track in focus from the note events of the parts
on the track. This is particularly useful for drum tracks, in order to automatically assign instrument voices.
-
Undo/Redo This option will undo and re-do the most recent action.
Editing the Score Using Standard Staff Types

The Note Menus
After selecting one or more notes, [Right]/[Ctrl]-click to open the contextual menu. The full menu includes the Tuplet options, when appro-
priate; otherwise a smaller menu is shown.
-
Cut/Copy/Paste/Delete These perform the same function as the computer keyboard actions.
-
Recent items Choose from a short list of recently-performed commands, good for quickening repetitive tasks
-
Score A submenu of context-sensitive score-specific commands:
-
Double at Interval: Doubles the current selection of notes at a specific interval either above or below the existing notes
using the following modifiers:
-
Interval: Use this option to select unison, second, third, fourth, fifth, sixth, seventh, or octave.
-
Interval quality: Use this option to select Diatonic, Minor, Major, Perfect, Diminished, or Augmented.
-
Octave: Use this option to select the Same Octave or one to three octaves above.
-
Add Above or Below: Use this option to add intervals above or below the existing notes.
Editing the Score Using Standard Staff Types

-
Fill with Rests This option places the appropriate rests in any empty sections of the selected measures, including whole-meas-
ure rests, up to the limit set by the time signature. See the description in the Staff Menu section above for more details.
-
Make Tuplet/Custom Tuplet... These options appear when notes or chords from different positions within the same measure
and staff are selected. See their descriptions in the Action Menu section
-
Quantize to Notation This action quantizes Note Events to precisely match the note values and rests displayed in the score view
-
Send to Voice 2/3/4 This action will assign selected Notes to the Voices of your choice.
-
Switch Staff This action is only available when the Grand staff is used. It allows you to switch a note from the upper staff to the
lower staff, or vice versa.
-
Transpose Use this to transpose the selected notes up or down after you specify the Interval, Interval quality, and Octave range
of the transposition. These options are similar to those described in the Transposing Notes section. They can force notes or
chords to conform to the key (Diatonic), allow them to maintain the same interval relationships, or follow a number of other per-
mutations, all while transposing up or down in specified intervals by as much as three octaves.
-
Rebuild Score This option re-creates the complete representation of the track in focus from the note events of the parts on the
track. This is particularly useful for drum tracks, in order to automatically assign instrument voices.
-
Select All/All in Staff/All on Tracks See descriptions in the Staff Menu section above for more details.
-
Deselect All Use this option to deselect every item that is currently selected.
-
Undo/Redo This option will undo and re-do the most recent action.
Multitrack Score Editing
It is possible to view and edit the staves for many Instrument Tracks simultaneously. The quickest way to do this is to open the Track List
by clicking its icon in the upper left corner of the Note Editor's Inspector panel. In this list you can show or hide the staves of each Track in
the Score using the Show/Hide buttons to the left of the Track name. It is possible to click-and-drag through many buttons and add their
Tracks to the Score view very quickly.
When the staves for multiple instruments are displayed you can duplicate or move notes from one staff to another using standard key
commands for Cut, Copy, and Paste. These options are also available in the [Right]/[Ctrl]-click contextual menu.
When a Select All action is performed with [Ctrl]/[Cmd]+[A], only the notes in the current staff are selected (both staves when the Grand
staff is used). To select all of the staves that are visible in the Score, use [Right]/[Ctrl]-click inside the Score and choose Select All on
Tracks from the contextual menu.
To select a specific staff within the Score when multiple staves are visible, click on a note or an empty space within the staff you want to
edit. The vertical blue cursor will appear at that location.
To view only one staff and close the others, double-click on an arrangement event inside that staff.
Song / Album / Composer Information
If you would like the Score to display and print the Title, Album, and Songwriter/Composer for the Song, press [Ctrl]/[Cmd]+[.] or navigate
to Song/Song Setup/Meta Information to open the Song Setup window, and then enter this information in the appropriate fields. Note that
it can only be seen and printed from the Full Score and Single Track page layouts, not the Continuous layout.
If this information is already present at the top of the Score and you would like to change it, simply click one of those fields to open the
Song Setup window. Enter the desired information and click OK to close the window. The new information now appears at the top of the
Score.
For more on this topic, see the  Song Meta-Information section.
Editing Scores in Drum Notation
When using the Drumset Staff Type, unique Drumset Instrument options will display in the Staff Inspector; specially designed for drum
notation!
Editing Scores in Drum Notation

When you select a MIDI Event while using the Drumset Staff Type, Studio One will analyze the note and drum name information and
assign the pitches into different displayed notes, voices and noteheads automatically—but you still have the freedom to assign them your-
self, of course, using the following options:
Staffline Here, you can assign desired Staffline positions to create drum notation that renders in a familiar fashion regardless of the true
MIDI Note value of these events. That means that the Staff note values shown are independent of the musical data Studio One is using to
trigger your drum samples. This is an important distinction. You can also use the visual staff interface at the bottom of the Staff Inspector
to drag-and-drop the display note to the desired Staffline.
To map a new pitch:
1.
Select the musical note pitch in the first selection box of the mapping editor. This can also be done by selecting a note in the
score, or by double clicking the pitch name and hitting a key on a connected MIDI keyboard.
2.
Double-click the box to the right of the note selection box to enter a drum name.
3.
Select the Staffline can be entered into the Staffline field. Stafflines are counted from the bottom. .5s represent the spaces
between staff lines. This can also be done by dragging the note in the note preview below
4.
Repeat the above for any new pitch mappings.
To re-map existing pitches:
1.
Select a note within your existing drum score
2.
Drag the note preview in the Staff Inspector to the desired position
All other existing notes in the score will now reflect the new mapping.
Notehead Use this option to choose the notehead display of a selected pitch. Options include symbols popular for percussion notation,
including Normal, X-symbol, Triangle, Slashed, Circle-X, and Diamond.
Technique Use this option to choose from a wide array of percussion techniques including Open, Half Open, Closed, Roll 1/2/3, or a
Cymbal Choke.
Reset Button Click this to reset the mapping of the selected pitch to the default value.
Note that the above options will be saved when you save your Song, and can even be saved separately for use in other tracks as a Pre-
set. A General MIDI drum preset is also included—another time-saving starting point for the naming and mapping of your favorite drum
libraries.
Editing Scores with Tablature and Standard + TAB Staff Types
When you set the Staff Type of the Note Editor Inspector to Tablature or Standard + TAB, you’ll be able to enter and edit notes in a Tab-
lature interface designed for fretted instruments. Although tablature is often associated with guitar, composers/players on other fretted
instruments also make use of this staff.
Editing Scores with Tablature and Standard + TAB Staff Types

About the Tablature Staff Type
Tablature contains just the essence of a guitar part (for example, rests do not appear on a Tablature staff.) Each line in a Tablature staff
represents a different string on the instrument, with the lowest-sounding string on the bottom. Numbers are placed on the horizontal
“strings” to represent fret positions, with “0” referencing an open string.
When using the Standard + Tab Staff type, the work you do in a Tablature staff immediately updates equivalent notation in the notation
staff, and vice-versa. Note that Rhythmic stems are not shown in Tablature when using this dual view.
Note Entry with Tablature Staff Type
When choosing Tablature Staff Type in the Score Editor Inspector, you can directly enter notes into a Tablature staff.
Text Box Method
With this note entry method you will specify a fret number after you place the note on a string.
1.
[Left-click] to choose a note value from the Score Editor Toolbar, such as quarter note.
2.
[Left-click] on the desired string to place a note. The string should sound and a text box will appear.
3.
Enter the desired fret position in the text box and press Enter. The default fret number is “0,” for an open string.
4.
Repeat steps 1-3 for additional notes as desired.
Notice that these Tablature marks are now reflected in the associated Instrument Part.
Pitch Change Method
To directly change the pitch of an existing note (fret number) on the Tablature staff, you have two options:
To keep the note on the same string:
1.
[Left-click] to choose the Arrow tool from the Score Editor Toolbar.
2.
[Double-click] an existing number and enter the desired fret number in the text box that appears.
Editing Scores with Tablature and Standard + TAB Staff Types

3.
Press Enter or click anywhere away from the box.
To move the note to a different string:
1.
[Left-click] to choose the Arrow tool from the Score Editor Toolbar.
2.
[Single-click] an existing fret number on the desired string. It turns orange to indicate that it’s been selected.
3.
Drag the fret number up or down to the desired string (Tablature line). The fret number will automatically update.
4.
If you decide you want a different pitch on this new string, double-click the item and enter the fret number you want in the text
box and press Enter.
Things to consider when dragging notes around the Tablature staff:
If you move a lower note to a higher string, it’s possible a question mark will display in place of a number. This means that the pitch can-
not be sounded by the string in its current tuning.
If you move a higher note to a lower string, the fret number will generally increase to show the same note on a lower-tuned string—
though this can vary depending on the tuning of the instrument selected in the Tab Type option—Ukulele, for example, is an exception.
When moving notes on the Tablature staff, notice that your changes are also now reflected in the associated Instrument Part.
Note Entry with Standard + TAB Staff Type
Techniques used to enter notes as described in the Note Entry with Tablature Staff Type section also work in Note Entry with Standard +
TAB Staff Type, and edits you make in the Tablature staff are interpreted automatically in the standard notation staff and vice versa. The
best of both worlds! Note that as you change the pitch or time value of notes on the notation staff, the equivalent Tablature marking will
be updated automatically.
As you enter notes on the notation staff, (see Score Editor Toolbar for the basics on note entry) low-fret fingering numbers will appear on
the Tablature staff.
To change these notes from their default fingering:
1.
[Single-Click] the new Tablature note so it highlights in orange.
2.
Click and drag this note to a lower or higher string on the Tab staff. The fret number will adjust accordingly and automatically as
in the example below.
Lyrics in the Score View
To assign Lyrics to note values in the Score View, click the Lyr tool from the Symbols palette in the Note Editor Inspector. Click any note
in the Score View to open a lyric entry field associated with the chosen note. Enter lyrics with the keyboard.
Pressing the spacebar or tab key will advance the entry field to the next note. For multi-syllabic words that span several notes, use the
dash (-) key in the middle of your lyric to advance to the next note and render a hyphen between the syllables. Lyric Events pasted from
the clipboard into Score View will be separated word by word in alignment with the existing notes. Syllables, melismas, line breaks, and
paragraphs are all supported.
The display font for Lyrics in Score View can be chosen from the Layout Tab of the Note Editor Inspector.
Lyrics in the Score View

Lyrics entered via the Score View will render in the Lyrics Lane when switching to Piano View and vice-versa. Lyrics created in the Score
or Piano Views are independent of — and not to be confused with — Lyrics created in the Lyrics Track, which you can learn more
about here.
Lyrics entered via Score or Piano Views can be selected for display in sync with Song playback using the Lyrics Display.
Lyrics in the Score View
