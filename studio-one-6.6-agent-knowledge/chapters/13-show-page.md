# The Show Page

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 339–369
> **Slug:** `13-show-page`

**Agent topics:** `live performance`, `setlist`, `players`, `patches`, `performance view`, `show timeline`

---

The Show Page
The Show page is a powerful, fully integrated live performance environment that makes it possible to run complete shows from a single
computer. It combines Setlist management, the playback of backing tracks, virtual and real instrument Players, and Patch management
inside a single window. With assignable Macro Controls and a dedicated full-screen performance view, running a show is simple and reli-
able even in difficult lighting conditions.

## A Tour of the Show Page

The Show page consists of five main sections:
-
Setlist The Setlist adds a clearly defined structure into a live performance by adding and managing Setlist Items (these could be
songs, musical cues, or patch performances). When an Item is added to the Setlist, a color-coded entry also appears in the
Overview. This window displays the Items on a timeline based on their position in the Setlist. Items can be reordered with a
drag-and-drop in either window.
-
Players and Patches The Players column defines the contents of a show with each Player representing a source or artist. The
Show Page provides three different Player types:
-
Backing Track Player for playback of audio files (mixes or stems).
-
Real Instrument Player for external audio sources processed through a mixer channel, such as a guitar player using
Ampire or a singer processing his voice using the Fat Channel.
-
Virtual Instrument Player for any type of virtual instrument, including the Multi Instrument for complex split/layer com-
binations.
Each Player is associated with one or more mixer channels. Any number of Players in any combination can be part of a Show. The cur-
rent state of a Player can be saved into a Patch, including a complete snapshot of all instrument, plug-in and mixer settings.
The Show Page

-
Macro Controls The Controls view is a powerful controller mapping environment. Any parameter of any Player instrument,
plug-in or mixer channel can be mapped to a set of up to 24 controls (knobs, faders, and/or buttons) in predefined con-
figurations. These controls are then mapped to knobs and buttons on a hardware controller such as the PreSonus FaderPort 8
or -16, the ATOM or ATOM SQ, or any other external MIDI controller.
-
Mixer and Browser The Mixer is a streamlined version of the familiar Studio One Console. The familiar Browser provides
access to instruments, effects, audio files and presets of any kind. These can be click-dragged into the Show and placed where
they are needed.
-
Performance Mode The Show Page features a dedicated Performance mode with its own custom view replacing the edit win-
dow when launched. This predefined full-screen view reduces the user interface to just the essential elements needed in a live
performance:
-
Transport controls and a large time/bars counter
-
Setlist and Patch navigation
-
Current player status
-
Realtime controllers
-
Metering
Although a live show may be entirely run off the Show page edit window, the Performance view offers the best visual experience – even
in difficult lighting conditions and when running on a small notebook computer screen.
Show Management
Select a Show
To access the Show Page, select a Show from the Start page or the Studio One toolbar. The drop-down menu in the toolbar contains a
list of existing Shows. If none exist yet, there are two ways to create a Show: Select New Show from the File menu, or create a Show
from a current Song.
Show Management

Create a New Show
To create a new show:
From the Start Page, open the New Document Window by clicking the New… icon or press [Ctrl]/[Cmd]+N on the keyboard.
Choose Rehearse and Perform (New Studio One Show) to create a new Show.
You can set your own title by editing the text in the Name field.
When creating a new Show, Studio One will remember the last folder you used for a new Show and assume you would like to save your
work in the same location. If you would like to restore to the default location, right-click the file path and choose “Reset Folder” from the
drop-down menu.
Sample Rate
Use this field to specify the sample rate for the show. The sample rate should match your audio interface by default.
If you plan to use Backing Track Players, it may make sense to choose the same sample rate the backing tracks used. If the sample rate
doesn't match, the backing track audio files are automatically converted in the background and a new audio file is added to the Pool.
Audio Import
If you have any audio files to import to your project, drag and drop them to the Drop Zone in the New Document window.
Import Mode
Use the Import Mode drop-down to set your imported audio to render as Setlists or Stems.
-
Setlists will import each audio file as a separate Setlist Item.
-
Stems will import all audio files into separate Backing Track Players under a single Setlist Item.
Click OK to create your new Show.
Create a New Show

Show Templates
Show Templates — once you’ve created some — will be found in the User tab of the New Document window.
Create a Template
If you plan to use a Show setup more than once, it can be helpful to create a template. To do this, first create a new Empty Show. Next,
create and configure the basic Setlist, the Players, and add your favorite virtual instruments, effects, and any other aspects of the Show
that are your go-to solutions. Then select Save as Template in the File menu.
Type in a title and description, choose an icon image (512 x 512 pixels) or drag one onto the image icon, and click OK. Your template is
now one of the User templates available in the New Show window.
Replace a Template
If you'd like to replace an existing Show template with the current settings, navigate to File/Save As Template and select Replace Exist-
ing... at the bottom of the window. The Title, Description, and Icon of the older Template are loaded into the Save As Template window.
Click OK to overwrite this file.
Show Location
New Shows are saved to Studio One/Options/Locations/User Data (macOS: Preferences/Locations/User Data). You can choose a dif-
ferent folder by clicking on the [...] button in the New Show window and browsing to the preferred location.
Add an Open Song to a Show
To add a Song you are currently working on to a new or open Show, select Add to Show from the Song menu. Select any open Show
from the list or select New Show. This automatically renders a mixdown and places it in the Setlist and Overview of the selected Show.
Add Content to the Show
Once a Show exists, you can fill it a number of ways:
-
Transfer a mix from the current Song (see the previous section).
-
Export stems from a Song, and then add the stems from the Browser via drag-and-drop.
-
Transfer your favorite Instruments to an open Show with the Send to Show option in the Instrument Slot pop-up menu, which is
found in the Instruments Panel of the Console.
-
Copy and paste Channels from the Console, complete with their levels and Insert/Send effects.
-
Drag items from the Browser into the Show (instruments, FX Chains, etc.).
-
Add Channels to the Console with a [Right]-[Ctrl]-click (Bus, FX, Listen Bus, etc.).
Show Setup
Navigate to Studio One/Options/Show Setup (macOS: Preferences/Show Setup) to access the Show Setup information and settings.
These include the General settings, Audio Input/Output settings, and the Meta Information for the Show.
-
General Settings includes the Sample Rate, which can be changed and applied on this page.
-
Meta Information includes the Title, Artist, Venue, and Logo, which can be changed on this page.
-
Audio I/O Setup allows you to route the Players and other components of the Show through the inputs and outputs of your
audio interface, as described here.

## The Setlist

Add an Open Song to a Show

The Setlist is where you decide the order for the songs, musical cues, and/or patch performances that make up a Show. Each entry in the
Setlist is called a Setlist Item. They are named automatically as they are added ("Item 1", "Item 2", etc.). You can rename each Setlist
Item, assign it a color, and set it to one of three playback modes (Continue, Stop at End, or Loop). Setlist Items can be reordered with
simple drag & drop.
The view size can be set to Small or Normal for all Setlist Items, using the buttons between the Items and the Setlist Inspector. When set
to Normal, the Item length and BPM are also displayed.
The Setlist Inspector is located at the bottom of the Setlist window. It shows specific information about the selected Item, which can also
be edited here.
You can give each Show a unique identity by adding the name of an Artist and Venue at the top of the Setlist window. It's also possible to
add a logo or some other image below the Venue name. The maximum image size is 1400 x 1400 pixels, and the image you select is
automatically scaled to fit. Alternative versions of a Setlist can be made by saving a new version of a Show (File/Save New Version), just
as you would save alternate versions of Songs or Projects.

## The Setlist

Add Setlist Items
At the top of the Setlist is the Add Setlist Item button
. Click this to add an Item to the Setlist. Each Item is given a unique color, which
you can change by clicking the color field to the left of the Item number. To name an Item, double-click the field to the right of the Item
number.
When an Item is placed in the Setlist it also appears in chronological order in the Overview, using the same color as the Setlist Item for
easy identification. You can reorder Items in the Setlist or the Overview with a simple drag-and-drop action.
Working with Setlist Items
There are three ways to select Setlist Items: with a click of the cursor, with the up and down arrows on a computer keyboard, or with the
◄and ►buttons in the Studio One transport.
Set the Playback Mode
The playback mode tells the Setlist what to do when it reaches the end of a Setlist Item. Click the upper-right corner of the Item and
choose whether the Setlist should proceed to the next Item (Continue), wait for you to press Play (Stop at End), or repeat that Item indef-
initely (Loop).
Change the Item Length
When the view size is set to Normal, the Item length is visible. This is automatically set to the audio file length when a Backing Track
Player is used, but a different value can be entered: a shorter value ends the file playback earlier; a longer value leaves a gap between
this Item and the next one. If you want a gap, a better way is to enter a Pause value for the next Item in the Setlist Inspector.
Change the BPM
When the view size is set to Normal, a BPM value is visible. If a backing track audio file includes tempo information, this value will be
imported. You can enter another value if you like. This affects the Metronome click, but it does not affect the length or playback speed of
an Item.
Duplicate, Remove, or Disable an Item
[Right]/[Ctrl]-click on an Item to open a contextual menu with four options:
-
Add Setlist Item provides another way to add an Item to the Setlist.
-
Duplicate Setlist Item adds a copy of the Item to the Setlist. You can set a different Length for each. All Patch assignments are
duplicated as well.
-
Remove Setlist Item deletes the Item from the Setlist.
-
Disable Setlist Item darkens the Item in the Setlist and hides it in the Overview so it is skipped during the Performance. [Right]/
[Ctrl]-click and select Enable Setlist Item to restore the Item to the Show.
Setlist Inspector
The Setlist Inspector shows specific information about the selected Item. You can also change that information here.
-
Color can be changed by clicking the color field to the left of the Item name.
-
Name can be changed by double-clicking the field and adding text.
-
Playback Mode can be set by clicking on the icon or the current Mode name and selecting the desired option.

## The Setlist

-
Start shows the start time of the Item in hours, minutes, seconds, and milliseconds. An Item can begin at the precise moment
you enter here. When running a Show synced to an External MIDI Device via MTC, the start timecode will be the offset at which
a Setlist Item will start playback. The Pause time is adjusted automatically.
-
Length can be entered for an Item. Shorter values end file playback earlier; longer values leave a gap until the next Item. We
recommend using the Pause parameter to create a gap, though (see below).
-
Tempo can be entered here. This affects the Metronome click, but it does not affect the length or playback speed of an Item.
-
Pause can be used to place a gap between the selected Item and the previous one. The pause can be as little as 0.001 seconds
and as much as 30 minutes. A Pause is recognized instantly in the Overview, since it leaves a gap between Items.
-
Time Signature can be entered for informational purposes.
-
Key Signature can be set using the familiar pop-up selector; simply click and select the key for the current Item.

## Players and Patches

The Players column can hold as many Players as you need for a Show. A Player can be a backing track, a virtual instrument, or a live
audio input with its associated Channel, through which a live musician or singer is combined with all of the other Players in your Show.
In addition to its location in the Players column, each Player has its own color-coded "lane" in the Overview. The Overview also displays
the Setlist Items in columns. The intersection between a lane and a column is called a "slot". Each slot in a Virtual or Real Instrument
Player lane can hold one Patch, which will be explained later.
Each Player is associated with one or more Channels in the Console. Use [F3] to show or hide the Console, or double-click an empty
space inside any Player.

## Players and Patches

The Players Column

## Players and Patches

## Players and Patches

The Players column lets you assemble a list of the Players you need for the Show. You can navigate through the Players column with the
left and right arrows on a computer keyboard, or click a specific Player to select it.
The Players column provides these features:
-
Title Click the field once to enter a name for the Player.
-
Add Player This button lets you add a Player to the Players column.
-
Color As Players are added they are assigned a color automatically. This becomes the color for the lane as well. Click the color
field to select a new color.
-
Instrument Editor Click the keyboard icon to open the Editor for a Virtual Instrument Player.
-
Mute/Solo These buttons allow you to silence or solo a specific Player.
-
Patch Automation Each Player can be set to Read or Auto: Off. See the Patch Automation section below for details.
-
Size buttons At the bottom of the Players column are three buttons that let you specify the Player size (Small, Medium, or
Large). This naturally affects the lane size in the Overview.
-
The larger Player sizes show more options, which include:
-
Update Patch Click this button to update the current Patch with any changes you have made to a Virtual Instrument or
an plug-in effect.
-
Patch Menu The arrow opens a menu, which is described in the next section.
-
Save Patch The
button opens the Save menu, which lets you save the current Patch. Give it a new name if you like,
and click OK.
-
Input/Output These menus provide the same options you see when adding a similar Player.
Note that an asterisk next to the Patch name means the Patch has been changed. Use Update Patch or Save Patch to
preserve any changes you want to keep.
Patch Menu
Each Player in the Players column has a drop-down menu with the following options:

## Players and Patches

-
Patch list If you have saved Patches for this Player they appear at the top of the menu. To reselect "None" for the Default Patch,
use the Reset Default Patch option described below.
-
Default Patch tells you which Patch is the current default for the Player. The default Patch is automatically applied to all slots in
the Player lane. You can select a different Patch for each Item using the menu for that slot.
-
Set (Patch name) as Default Patch sets the current Patch as the default for the Player.
-
Reset Default Patch clears the Default Patch selection but retains the Patch in the Patch list for the Player.
-
Save Patch... opens the Save menu so you can name the Patch and save it.
-
Update Patch updates the current Patch with any changes you have made.
-
Rename Patch opens a window that allows you to give the Patch a new name. Click OK to save it.
-
Remove Patch deletes the current Patch from the Patch List for the selected Player.
Remember, an asterisk next to the Patch name means the Patch has been changed. Use Update Patch or Save Patch to pre-
serve any changes you want to keep.
Contextual Menu per Player
[Right]/[Ctrl]-click on a Player inside the Players Column to open a contextual menu containing these features:
-
Save/Update/Rename Patch These features are described in the previous section.
-
Duplicate Player This adds another Player of the same type below the selected Player.
-
Remove Player This option deletes the selected Player from the Players column, and removes its lane from the Overview.
-
Add Player... Use this to open the Add Player window, which provides specific assignment options for the Player. Or if you want
to add a Player with the default settings, select Add Backing Track Player, Add Real Instrument Player, or Add Virtual
Instrument Player.
Add a Player
Click the
at the top of the Players column to add a Player to the Show. Each Add Player window type has slightly different options, but
they are similar to what you see when adding a Track.
-
The options for the Backing Track and Real Instrument Players are similar to the ones you see when Creating an Audio Track:
-
-
Name Click here and type in a name for the new Player.
-
Count Choose the number of Players you would like to create.
-
Color Choose a color.
-
Auto-Color Check this box if you would like your Players auto-colored.

## Players and Patches

-
Preset Choose an FX Chain to be pre-loaded on the Players.
-
Input Assign an audio Input to the new Player(s). When creating multiple Players, you can engage the Ascending
option to assign Inputs to each Player in ascending order (Player 1, Input 1, Player 2, Input 2, etc.).
-
Output Assign an audio Output to the new Player(s). When creating multiple Players, you can engage the Ascending
option to assign Outputs to each Player in ascending order (Player 1, Output 1, Player 2, Output 2, etc.).
-
The options for the Virtual Instrument Player are similar to the ones you see when Creating an Instrument Track:
-
-
Name Click here and type in a name for the new Player.
-
Count Choose the number of Players you would like to create.
-
Color Choose a color.
-
Auto-Color Check this box if you would like your Players auto-colored.
-
Input Assign a MIDI input Device to the new Player(s). Choose All Inputs | Any to accept input from any connected MIDI
Device. When creating multiple Players, you can engage the Ascending option to assign inputs to each Player in
ascending order of device and MIDI channel.
-
Output Assign an Instrument to the new Player(s). To create a new instance of a software instrument for each new
Player, choose New Instrument and select an instrument from the provided list. To assign the new Players to a hard-
ware instrument or to a software instrument already in use in the Song, choose Existing Instrument, and select from the
provided list.
When creating multiple Players, you can engage the Ascending option to assign Outputs to each Player in ascending
order of Instrument and MIDI channel.
Each of the Player types has features of its own.
Backing Track Player
The Backing Track Player is for playing mono or stereo audio files. These can be Song mixes, stems, .wav, .mp3, etc. You can drag
what you need directly into the Players column from the Browser. Note that individual stems require individual Backing Track Players.
-
When you drag a file to the blank space under an Item, it adds a new Player and adds the audio file to that Item, all at the same
time.
-
If you drag a file onto an empty slot in the lane of an existing Player, the file becomes part of the Item at that location.
-
When you drop the file onto a slot that already has an audio file, the new file replaces the old one.
-
If you drop a file at the end of the timeline, it adds a new player and a new Item to the Setlist. The new Setlist Item is given the
name of the file.
Real Instrument Player
The Real Instrument Player is designed for external audio sources that are processed through a Channel in the Console. This could be
a live guitar or bass routed through Ampire, for example, or a singer's voice routed through his signature FX Chain. You can drag FX pre-
sets or entire FX Chains from the Browser onto a Player, if you like, or drag them onto a Console Channel.
Virtual Instrument Player
The Virtual Instrument Player can be used for any type of virtual instrument. Options include the Studio One Multi Instrument, which
allows more complex combinations like splits and layers. You can drag an instrument from the Browser to add a new Player or replace
the instrument for an existing Player. You can drag specific presets, too, which saves a step later.
This Player can also be used for external MIDI devices, which is described below in the External Instruments section.
If an instrument or preset is dragged onto a specific slot in a Virtual Instrument Player lane, it becomes the selected Patch in that slot. If it
is dragged into the Players list on top of a non-empty Player, two options are available:
-
Insert adds the preset with a new instance of the instrument (recommended).
-
Load/Replace adds the preset using the same instance of the instrument (if it’s the same) or replaces the existing instrument
with the new instrument and preset.
Insert is the default option. Press [Alt] when dragging the instrument or preset to choose Load/Replace.
We generally recommend the use of separate instrument instances per Patch, especially when working with samplers. This allows for
faster switching during a performance.
For example, if you plan to use two multi-sampled Presence instruments in the same Player, here's the best way:
1.
Drag the first preset onto a slot in a Virtual Instrument Player lane.
2.
Drag the second preset onto the next slot in the same Player lane.

## Players and Patches

This adds separate instrument instances for each preset. Now when the Show crosses from the first Setlist Item into the second, the
Player switches instantly from the first Presence instrument to the second Presence instrument, rather than loading a new set of samples
into the first Presence instrument.
Note FX and the Players List
Dragging one of the Note FX or a Note FX preset from the Browser/Instruments tab onto an empty spot in the Players List creates a new
Player and a new Multi Instrument, to which you can add other instruments. If you drag one of the Note FX or a Note FX preset onto a
Player with an existing Multi Instrument, the effect is added to that Multi Instrument.
External Instruments and the Players List
Dragging an External Instrument from the Browser/Instruments tab onto an empty spot in the Players List creates a new Player. The
Large view displays a checkbox to enable or disable MIDI Program changes, and two fields are available to enter Bank and Program
numbers. These are transmitted to the external instrument when a slot that uses this Patch is selected in the Player lane. For more
information, see the Set Up Your MIDI Devices and Set Up External Hardware Instruments sections.
For the curious: If you drag a virtual instrument preset onto a Player with an existing External Instrument, for example, the new instru-
ment is added as a Patch to that Player. We recommend using separate Players for virtual and external instruments, though.
Patches
The current state of a Player can be saved into a Patch, including a complete snapshot of all instrument, plug-in and mixer settings.
There are two ways to save a Patch:
-
All views [Right]/[Ctrl]-click and select Save Patch... from the menu.
-
Medium / Large views You can also click
to open the Save Patch window.
In either case, give the Patch a name and click OK to confirm.
Working with Patches
Here's a quick description of some of the ways Patches can be used:
-
When you drop an instrument preset into an empty slot in an existing lane, this loads the instrument and preset and auto-
matically creates a new patch with the same name as the preset.
-
After saving a Patch you can make this Patch the default for every unassigned slot in the lane. A slot that already has a Patch
assignment will not change.
-
If the Player has a default Patch, you can add another preset to the same Player and save it as a Patch too. After this you can
select it as the Patch for any Item slot in that lane instead of the default preset.
-
For a Virtual Instrument Player you can simply drag the new preset from the Browser to the desired slot and it is substituted for
the existing Patch without altering the default Patch selection.
-
If you change an instrument parameter, you can save that edit as a new Patch inside the current slot without the need to store it
as a preset for the instrument.
Creating Patches with Drag and Drop
You can create Patches for Virtual Instrument, Real Instrument, or Backing Track Players by dragging and dropping Instrument Presets,
Effects Presets, or Effects Chains from the Browser to your lane.

## Players and Patches

-
Dragging a single virtual instrument Preset from the Browser to a Patch slot of a Virtual Instrument Player adds the instrument,
selects the Preset, and creates a new Patch with the same name.
-
Dragging an Ampire preset from the Browser to a Patch slot of a Real Instrument or Backing Track Player adds the plug-in,
selects the Preset, and creates a new Patch with the same name.
-
Dragging a complete FX Chain to a Patch slot of a Real Instrument or Backing Track Player adds all of the plug-ins, and their set-
tings, and creates a new Patch with the same name.
This can be used to quickly and easily set up and automate patch changes for guitar tones or synth patches that better suit more dynamic
or relaxed passages during the flow of a song.
Patch Automation
As stated previously, each slot in a Virtual or Real Instrument Player lane can hold one Patch. Having Read mode enabled for a Player
means that when a Setlist Item is activated, either manually or during playback, the Patches that were assigned to each slot for that
Player lane are recalled. If Patch Automation is disabled (i.e., set to Auto: Off), Patches are not recalled unless they are selected from the
Patch menu or from the Patch List in Performance Mode.
Because an entire instance of a virtual instrument or effect is created for every Preset you place in an Arranger section, transitions from
one Preset to another across Arranger sections will result in non-audible, seamless patch changes.
The Show Page Toolbar
The toolbar provides quick access to all of the Show Page features.
-
Overview Select this button to display the Overview window. This reveals the Setlist Items and their locations on the timeline,
with a lane for every Player in the Show. This is the view where Patches can be assigned to a Player for each Setlist Item.
-
Controls This opens the page where you can select the control configuration and assign the Macro Controls you want to use
during the Performance. Details are in the Controls View section.
-
Macro This button opens the Macro Toolbar. From the Macro Toolbar, you have easy access to often-used functions and cus-
tom command combinations.
-
Snap When Snap is engaged, the current Snap setting is applied as you adjust the Loop range or the size of a Setlist Item.
-
Toggle Snap Press [N] to toggle Snap mode on and off.
-
Autoscroll This determines if the Overview window follows the playback cursor. Click this button or press the [F] key to toggle
Autoscroll on and off.
-
Info View Click the question mark icon to open the Info View bar. It shows which options are available depending on where you
hover the cursor.
-
Perform takes you to Performance View. You can also use [Ctrl]/[Cmd]+[Enter], where “Enter” is the Enter key on an extended
keyboard.
The Show Timeline
The Overview window
The Show Page Toolbar

The Overview displays the Setlist Items in vertical columns and the Players in horizontal lanes. The columns and lanes are color-
coded: the columns are outlined by the Item color, and the lanes are filled with the Player color.
Item Columns
The head of a column shows the Item name, its Playback Mode, as well as the time signature and tempo for the Item. Each of these is
described in the Setlist section. Note that the Item name and Playback Mode can be changed here (see context menu section below),
but the time signature and tempo must be changed in the Setlist.
Beneath the column head are the slots where the column intersects with the lane for each Player in the Show.
Click-and-drag the column head to reorder Setlist Items in the Overview window, which also changes their order in the Setlist. Drag an
Item in either place, it affects the other.
Click-and-drag the left edge of the column head to the right to add or increase a Pause (this value changes at the same time in the Setlist
Inspector window). If a Pause exists, drag the left edge of the column head to the left to reduce the Pause value. A small window appears
while dragging the left edge and shows the new Start Time, the amount of deviation from the previous Start Time, and the Pause length.
Double-click an item column to set the Horizontal Zoom to fit the screen.
Click-and-drag the right edge of the column head to the left or right to change the Setlist Item length. A small window appears while drag-
ging the right edge to show the Item length.
Note that you can change the size of the Players with the buttons at the bottom of the Players list. (The term was "column" in the Players
file. Change?).
Contextual Menu per Column
The Show Timeline

[Right]/[Ctrl]-click the head of an Item column to open a contextual menu. From this window you are able to select the Item color, change
its Playback Mode, or Add, Duplicate, Remove or Disable the Setlist Item. The changes made here are also made in the Setlist.
Player Lanes
The intersection between a column and a lane is called a "slot".
Patch Selection per Slot
Automated Patch changes for each Player can be applied per Setlist Item or Arranger Section, and any number of additional Patches can
be recalled manually during a Performance. A Player can have a list of Patches, one of which can be designated as the default Patch for
the entire lane. You can override the default Patch for any slot; simply click the arrow at the top of a slot to open the Patch list and make a
selection.
There are two other options in the Patch list for each slot in addition to the Patches:
-
None means that no automatic Patch change happens for this Player when the Setlist Item begins.
-
Mute silences the Player during that Setlist Item. This also activates the Mute button for that Player in the Player list for the dur-
ation of the Setlist Item. The Player is unmuted by the next slot that has a Patch assignment.
If your Show uses backing tracks then the Patch you assign to a slot is recalled automatically during playback. However, if your Show
does not use backing tracks then you'll need to navigate the Setlist manually. This can be done using a mouse, keyboard shortcuts, pre-
assigned buttons on a hardware controller, or with the Studio One Remote app.
Contextual Menu per Slot
[Right]/[Ctrl]-click on an Item slot to open a contextual menu. The options available in this window depend on the Player type.
For the Backing Track Player type only, [Right]/[Ctrl]-click the audio file inside the slot. The options in this contextual menu can
-
Delete the file from the slot;
-
Duplicate the file in the next slot in the lane, or
-
Select in Pool, which opens the Browser/Pool tab with the audio file selected.
If you [Right]/[Ctrl]-click a different slot in any lane after selecting an audio file inside a slot, you have the additional options of Select All,
Deselect All, and Undo/Redo last action.
If you [Right]/[Ctrl]-click a slot in the lane for a Virtual or Real Instrument Player, only Undo and Redo are available. The other options are
grayed out.
The Show Timeline

## Chord Track

Chord track is available per Setlist item (column) on the Show Page. Chord Track is automatically included with any Song imported to the
Show Page.
To show or hide the Chord Track, click this button,
above the Players list.
Chord Track functionality in the Show Page is display-only, intended as a helpful visual chord reference for musicians to follow live in Per-
formance View that displays the current and next Chord. Unlike in the Song Page, the Show Page’s Chord Track will not pitch-manip-
ulate musical information in Backing Track, Real Instrument, or Virtual Instrument Players.
When a Song is imported to the Show Page using Add to Show, the Song’s Chord Track information will be carried over on import.
Alternatively, a new Chord Track can be created from scratch if none was available on import.
See the main section on Chord Track for more information on its robust compositional functionality in the Song page.

## Lyrics Track

Lyrics Track is available for Lyrics editing and display for any Setlist Item on the Show Page. ideal for audience participation. You can
even move the Lyrics Display to a separate monitor to act as an automated teleprompter!
Enter Lyrics directly into the Global Track or via the Lyrics Display , just like in the Song Page.
To show or hide the Lyrics Track, click this button
, above the Players list.
Global Lyric Track content is automatically included with any Song imported via the “Add to Show” command on the Song Page. Lyrics
created in the Lyrics Lane of the Note Editor for specific Instrument Tracks are ignored.
The Show Page also supports Lyrics Display , which can be accessed from View >> Lyrics.
See the main section on Lyrics Track for more information.

## Arranger Track

Arranger track is available per Setlist item (column) on the Show Page. Arranger Track is automatically included with any Song imported
to the Show Page—or you can set up a new Arranger Track from scratch.
Simply [Double-click] on your Arranger Track to create a new Section. Right-clicking a Section will bring up a contextual menu where you
can change a section’s color, loop behavior, and more. For more information on editing the Arranger Track in the Song page, click here.
To show or hide the Arranger Track, click this button,
above the Players list.
As in the Song Page, The Show Page’s Arranger Track allows you to create verse/chorus-style arrangements in your Player Events,
while also providing the following functionality:
Patch changes can be assigned coincident with Arranger Track sections. This allows for virtual instrument patch changes to auto-
matically occur, for example, at the transition point from a chorus to an outro. When double-clicking the Arranger Track to create a new
Arranger section, Players will receive a drop-down menu within the slot, aligned to the new Arranger Track section, to select a Patch. You
can also use this option to automate effects Patch changes on Real Instrument Players, or selectively Mute backing tracks. Note that
Patch Automation must be set to “Read” in your Players for these changes to take effect.
Triggering Arranger Sections manually
The Show Timeline

The Show Page allows you to trigger Arranger sections manually during performance, jumping your playback to any section of the
Arranger Track with musical timing and without breaking rhythm. This is ideal for improvising new song arrangements on-the-fly during
live performance! If you discover that the chorus of your new song is a hit during your live show… now you can choose to double it, live.
Simply double-click an Arranger Track Section to prompt a jump to it. A triangular “pending jump marker” will appear at the head of the
Arranger Track Section to indicate that it is the next to play. The timing of the jump will adhere to the Sync Mode option setting chosen in
the Setlist inspector.
Sync Modes govern the timing of a Jump from one Arranger Section to another. Options include:
-
Off: Jump occurs immediately upon double-clicking an Arranger Section with no Sync.
-
1 bar: Jump occurs at the next bar start after the current play position
-
2 bars: Jump occurs at the end of a 2-bar section, relative to section start
-
4 bars: Jump occurs at the end of a 4-bar section, relative to section start
-
End: Jump occurs at the end of the currently-playing Arranger section, regardless of how long the selected Arranger section is.
Performance overrides
Additional useful performance override commands are also available during playback. Most of these can be triggered by a user-defined
keyboard shortcut or via Studio One Remote.
-
Jump immediately, bypassing sync: [OPTION + Double-click]
-
Toggle Section Playback Mode Loop/Continue [User-definable]
-
Stop at end of Section [User-definable]
-
Stop at end of Bar [User-definable]
Playback Modes allow you to set automated loop points in each Arranger track section. These can be used to repeat individual Arranger
sections indefinitely or a specified number of times, before playback proceeds to the following section.
The Show Timeline

-
Continue: Section playback proceeds normally to the next section
-
Stop at End: Playback stops at section end
-
Loop: Current Arranger Track section loops indefinitely
-
Loop And Continue: Current Arranger Track section loops X times before proceeding to the next section. X is specified in
“Number of Repeats” field of the [Right-Click] contextual menu of the Arranger Track.
-
Skip: Arranger Track section will be bypassed entirely for the next section in the sequence.
Note that the Show Page does not support grouped relocation of musical content by clicking-and-dragging Arranger sections. We recom-
mend using the Song Page to set up and the Chord Track and Arranger Track to your liking before importing your finalized Song to the
Show Page.
See the main section on Arranger Track for more information on its functionality in the Song page.
Arranger Track sections can also be viewed and navigated from the Performance View’s Sections View.
Show Controls
Show Controls

The Controls view lets you map the parameters of any Player instrument, plug-in or mixer channel to a set of up to 24 controls (knobs,
faders, and/or buttons), which are available in four predefined configurations. These controls then can be mapped to similar controls on a
hardware controller such as the PreSonus FaderPort 8 or -16, the ATOM or ATOM SQ, or any other external MIDI controller.
Select a Configuration
The four buttons at the top of the Controls view window are used to select a configuration. From left to right the configurations are 8 But-
tons + 8 Knobs + 8 Faders, 16 Knobs, 16 Faders, and 16 Buttons. Select one of these configurations to use it in the current Show.
The arrow opens a window so you can preview the configurations. Up to 16 of the controls you see can be assigned to control multiple
parameters. These customized Macro Controls play a prominent role in the Performance View.
Configuration 1: 8 of Each
Show Controls

This configuration shows 8 of each type of control (Knobs, Faders, and Buttons). Choose up to 16 of those controls and assign them as
needed. Their individual behaviors can be adjusted in the "Trans." area of the Targets column.
Configuration 2: Knobs
This configuration shows 16 assignable knobs. You can assign them as needed. Their individual response curves can be shaped in the
"Trans." area of the Targets column.
Configuration 3: Faders
Show Controls

This configuration shows 16 assignable faders. You can assign them as needed. Their individual response curves can be shaped in the
"Trans." area of the Targets column.
Configuration 4: Buttons
This configuration shows 16 assignable buttons. You can assign them as needed to toggle parameters on and off. Their performance
can be inverted by selecting that behavior in the "Trans." area of the Targets column.
The Preview Window
Click the arrow to open the preview window. Here's a quick description of how it works.
-
As each configuration is selected the window changes to display the selected configuration.
-
You can click-and-drag the variable Macro Controls (knobs, faders) to change their values, and you can click anywhere inside a
fader to jump to a new value. The status of a button can be toggled by a click.
-
Hover the cursor below a Macro Control until an arrow appears. You can then click to open the color selection menu for that con-
trol.
-
Double-click the name field under a Macro Control to rename it. Double-click the value field to enter a specific value.
Show Controls

-
[Right]/[Ctrl]-click to view the current assignment, enter a new value, or clear the connections for that Macro Control.
-
As a Macro Control is activated the response is also visible in the Control Link view on the left side of the Studio One toolbar.
This is true of the selected control in the Targets column as well.
It's easy to make a Macro Control assignment. We'll describe that in the next section.
Assigning a Macro Control
The Macro Controls Mapping view shows three columns of information. The left column lists all available Macro Controls and their cur-
rent assignments (if any). The right column shows all plug-ins that are currently part of the Show. Expand any plug-in in the list to show all
assignable parameters for that plug-in. The central Target column is a place where Macro assignments can be made, configured, or
broken.
You can assign an unlimited number of parameters to the same Macro Control, each with its own range and polarity, to create powerful
“morphing controls”. As more parameters are assigned to a Macro Control, plus signs (+++) are added to the right of the default name in
the Title column. You can rename the Macro Control if you like; just double-click the name in the Title column.
You also can choose a specific color for a Macro Control. To do this, click the box between the Control and Title columns for that Macro
Control. Select a color and the menu will close. You'll see that color whenever this Macro Control has a non-zero value.
When working with the built-in PreSonus plug-ins, assigning parameters to Macro Controls is very easy—simply [Right]/[Ctrl]-click the
control of choice, select "Connect (name of control) to Channel Macro Control" from the pop-up menu, then choose the desired Macro
Control from the secondary pop-up list.
Add/Remove Targets
The simplest way to map a parameter to a Macro is to drag the parameter from the right column onto the Macro Control of your choice in
the left column, or into the central Target column when a Macro Control is selected. You can also do this by selecting a Macro Control
and a parameter, and clicking the [Add Targets] button. Alternatively, you can drag the parameter directly onto a Macro Control in the Pre-
view window. However you do it, once the assignment is made, the parameter of your choice is displayed in the Target column.
To remove an assignment from a Macro Control, select the Macro in the left column, select the assignment you wish to remove in the Tar-
get column, and click the [Remove Targets] button.
Transform Window
You can shape the relationship between the movement of a Macro Control and the settings of its assigned parameters quite extensively.
With a Macro Control selected in the left column of the Macro Controls Mapping view, the current mappings for that control are displayed
in the Target column. Next to the name of each parameter is a button that gives you access to the control transform settings.
Show Controls

This graph traces the response curve from the beginning of the control's travel (the draggable point on the left end of the curve) to the
end of its travel (the point on the right end), with a handle in the middle that you can drag to set the shape of the curve. Dragging these
points up and down the control scales on the left and right of the graph lets you set the effective range of motion for that Macro Control.
For example, the whole range of a Macro knob could be set to affect just a quarter of a parameter's range, for fine-tuning purposes. You
can also move the right point below the left, reversing the action of the knob, according to whatever scale you wish.
Located above and below the graph are buttons that let you Reset the graph to its default setting, Invert the shape of the curve, or Copy
the curve setting and Paste it onto another parameter.
Note that because Macro buttons are a binary control, they have no curve setting. However, clicking in the Trans. column next to a button
assignment inverts its response, causing the parameter to be enabled when the Macro button looks disabled, and vice-versa.

## Control Link

Click the Control Link button to enable or disable the connection to your controller. Click the arrow above the button to open a menu of
available controllers and make a selection. For more details on how to map a hardware controller, see the Control Link chapter.

## Performance View

## Performance View

It's possible to run a live show from the Show Page edit window, but Performance View offers the ideal combination of factors – large con-
trols, a basic layout, easy to read onstage, and a screen that tells you instantly what's happening now and what's happening next. It's per-
fect for a notebook computer, which invariably has a smaller screen than what people use in their studios.
To enter Performance View from the Show Page, click the Perform button in the toolbar or navigate to Show/Perform. You also can use
[Ctrl]/[Cmd]+[Enter], where “Enter” is the Enter key on an extended keyboard.
Holding [Alt]/[Option] and clicking onto the Perform button will open Performance View in a separate, re-sizable window suitable for use
on a secondary monitor. When this window is closed, its size and position will be recalled by Studio One the next time you open it.
Visibility and Control
The Performance View display is remarkably uncluttered for all the features it contains. Depending on the size of the screen used, the
text and controls are scaled to make the best use of the available space.
Performance View contains three unique Views of its own: Controls, Patches, and Sections. We will address each of these in greater
detail farther on—but first, we’ll discuss the critical performance features that are shared by all Views when running Studio One in Per-
formance View.

## The Setlist

Most Shows revolve around a Setlist, so we made it easy to find by placing it in a drop-down menu on the top left The Setlist Items are lis-
ted from top to bottom.
If your Setlist has multiple Setlist Items, you can select them directly from the list in Performance View. After selecting a Setlist Item from
the Setlist, you can then use the up and down arrows on your computer keyboard to move through the Setlist.
As each Setlist Item is selected, it triggers the Patches on all the Players to change their sounds and mix snapshots. If no backing tracks
are used, this is the way to navigate the Setlist (instead of using the transport controls). You can also select Patches manually. If you
don't want Patches to change automatically at all, just set the Patch Automation of the respective Players to Off. This is done inside the
Players Column in the Show page edit view.
Note that automatic Patch selection is also affected by the "None" and "Mute" settings for each Player in each Setlist Item. For more
information about this, see Patch Selection per Slot.

## Performance View

## Players and Patches

A list of Players and the Patches they use for each Setlist Item is displayed on the top right. After selecting a Player from the menu, you
can then use the navigation arrows on your computer keyboard to select the Players: the up and left arrows move upward through the
list, and the down and right arrows move downward.
After selecting a Player, you can switch Patches manually for that Player. At the top of the list of Patches, there is a Mute setting which
can be used to silence that Player for the duration of the Setlist Item. Your choices are remembered for each Setlist Item.
Selecting a Patch returns focus to the Setlist, so you can use the up and down arrows to move through the Setlist again. This makes it
easy to change which Patch the selected Player uses for any Setlist Item: click the desired Patch, change the Setlist Item, click the
desired Patch, etc. This can be done within seconds while the curtain is rising, without leaving Performance View.
Performance and Timeline Information
The area below the Setlist, Player, and Patches interface displays vital information about what is happening right now in the Show and
what is next in the queue.
-
The Title of the Setlist Item currently playing displays at the top left of the Timeline, followed by its Playback Mode (Contin-
ue/Stop at End/Loop). If the Setlist Item contains an audio file, a blue progress bar under the Setlist Item name indicates the cur-
rent location inside the Setlist Item.
-
The large Time/Bars counter tells you where you are in terms of Seconds or Bars, depending on the Timebase setting for the
Show. This selection is made in the Show page edit view by clicking under the numbers immediately to the left of the Transport.
-
Time/Total Select the Time button if you want to view the elapsed time of the current Setlist Item. Select the Total button when
you want to know the time that has elapsed since the Show began.
-
Remaining This displays the amount of time that remains for the current Setlist Item.
-
Next This shows the name of the next Setlist Item.
Transport
The transport provides three buttons: Stop, Play, and Loop/Continue. You can also use the spacebar on your computer keyboard to start
and stop playback.
-
Loop/Continue affects playback behavior of the current arranger section.
-
Continue will direct the Show to play on to the next section.
-
The Loop function will Loop the current Arranger section until Loop/Continue is clicked again or the playback is stopped. This is
a temporary override that will not change your Show’s original settings. Clicking it changes the Sync Mode of the currently play-
ing section for a single section; it returns to the original setting when the next section plays.
Utility Buttons
The two buttons at the bottom right of Performance View are there to help you to manage the unexpected.
-
The Mute button mutes all output from all Players.
-
Use the All Notes Off button if you get a stuck note on one of your MIDI instruments.
Level Meter
Performance View provides a level meter that stretches vertically almost the entire height of the screen. It shows the combined output of
all Players at any given moment during the show.
Performance View Views: Controls, Sections, and Patches
At the bottom center of Performance View, you’ll find three small buttons that control the current View setting for Controls, Sections, and
Patches. Click them to choose between the following views. You can also click and drag the screen left or right to scroll to these views.

## Performance View

Controls View
The default view for Performance View; it contains all of the knob, fader, and button controls currently mapped to your Player instru-
ments, plug-ins, and console controls.
Performance Controls
The majority of the Controls View is occupied by huge, color-coded controls that are visible from across the stage. You can adjust the
controls with your mouse as needed, but it's much faster with a controller like the PreSonus FaderPort 16 or a controller keyboard.
As in the Show page edit view, you can double-click the name field under a control to rename it. Double-click the value field under a con-
trol to enter a specific value. You can also click-drag knobs or faders to change their values, and you can click inside a fader to jump to a
value. The status of a button can be toggled by a click.
If you’re looking for more information on setting up your Controls, visit Show Controls.

## Performance View

Patches View
Patches view gives you ready, one-click activation of any of the Patches you’ve set up in the Show Page for both real and virtual instru-
ments via a simple, easy-to-read button interface. Use this View to make live changes to your instrument presets, mute status, and more
during a show. Patches can be used to control your Console settings as well.
Note that the Patch buttons displayed in Patches View are Player-dependent; to change the group of Patches displayed, choose the
desired Player from the drop-down menu on the top right. Then, simply click on the desired Patch to activate.
Note that regardless of which Player you’ve chosen to navigate on the Patches View, you will always find a button here for the handy
Mute setting.
For more on setting up your Show’s Patches, read up on Players and Patches.

## Performance View

Sections View
Sections View allows you rearrange a Setlist Item live. You may find during a live performance that your audience really likes the new
chorus you wrote. With live arranging via Sections View, you can choose to double that hit chorus on the fly.
The Sections displayed here are populated by a Setlist Item’s Arranger Track—note that any Songs brought into the Show page will have
their Arranger Tracks brought with them.
Single-Click a Section to schedule a jump to it. The Section will receive a jump indicator icon at the far left of its position in the Arranger
Track in anticipation of the jump.
The jump will occur based on the Sync Mode chosen for the Section in the Show Page Edit View: Off, 1 Bar, 2 Bars, 4 Bars, or End (For
more on these Sync Modes, visit Arranger Track).
Don’t forget that if you decide to change a Sync Mode setting while running a Show in Performance View, you can go back to the Show
Page Edit View by clicking the X on the top right or pressing [ESC]. The Show won’t stop, and you can make the necessary changes and
then re-enter Performance View. You can also use the Loop/Continue button.
Once an Arranger section is playing, it will adhere to the rules of its Playback Mode, as set in the Show Page Edit View:
-
Continue: Section playback proceeds normally to the next Section.
-
Stop at End: Playback stops at section end (be careful with this setting in live performance!)
-
Loop: Section loops indefinitely.
-
Loop And Continue: Section loops X times before proceeding to the next section. X can be specified in the Show Page Edit
View.
-
Skip: Section will play normally when clicked in Sections View, but will be otherwise bypassed. The icon for Sections set to
“Skip” are greyed out in Sections View to reflect this behavior.

## Performance View

Lyrics View
Lyrics View makes it easy to display the Lyrics of the currently-playing Setlist Item in teleprompter-style, suitable for reminding your
band/choir of the current song’s lyrics. Lyrics View can be displayed on a separate monitor and in Studio One Remote.
The familiar appearance features available in Lyrics Display are available in Lyrics View as well. Font size and alignment are freely cus-
tomizable, as well as the read-ahead timer, measured in quarter notes.
During playback, upcoming lyrics are rendered in blue, past lyrics are rendered in grey, and current lyrics are rendered in bold white.
Performance overrides
Additional useful performance override commands are also available during playback. Most of these can be triggered by a user-defined
keyboard shortcut or via Studio One Remote.
-
Jump immediately, bypassing sync: [Double-click a Section button]
-
Toggle Section Playback Mode Loop/Continue: [User-definable]
-
Stop at end of Section: [User-definable]
-
Stop at end of Bar: [User-definable]
We’re really excited to see what you come up with using Sections view and live arranging!
Let the Show Begin!
Press Play or hit the spacebar on your computer keyboard to start the Show. Instantly, the Bar/Time counters start counting, and the pro-
gress bar starts progressing. Note that while the Show is in playback, Performance View will only let you select Players, Patches, and
Views. This way you can’t accidentally relocate to another part of the Show by clicking the progress bar, clicking a different Setlist Item,
or using the up and down arrows.
Remember, each Setlist Item has a Playback Mode that can be set to Stop at End, which means the Show stops automatically when
playback reaches the end of the longest audio file in that Setlist Item. But you can stop the Show at any time, if needed. Simply click the
Stop button or hit the spacebar.

## Performance View

During Playback: The Show Must Go On!
If you need to make a change in the Show page edit view without stopping playback, you can. Simply click the X to close the Per-
formance View, or use [Esc] and then click the X. The show keeps playing unless you hit the spacebar or the Stop button in the transport.
Once you are on the Show page edit view, you can disable Setlist Items, rearrange them, etc. This allows you to be as responsive as pos-
sible to the mood of the crowd, broken guitar strings, or any number of impromptu decisions you might need to make on the fly.
Performance View and Studio One Remote 1.6
Performance View can also be used from Studio One Remote for mobile devices, allowing for tablet control of your Show! Performance
View functions identically on both Studio One Remote and Studio One; there are no interface changes.
There are a number of applications for Performance View on Studio One Remote, including but not limited to:
-
A great touchscreen controller for live re-arranging and remixing
-
Multi-touch control of backing track volume, panning, etc.
-
Guitarists can get one-touch patch changes for Ampire and Stompbox
-
Keyboardists can get one-touch patch changes for Presence or their virtual synth(s) of choice and control effects with Controls
View
-
Instrumentalists can follow the Chord Track live on a tablet to improvise in key while anticipating future chord changes
Furthermore, you can even connect multiple mobile devices to the same computer running Studio One, granting multiple users sim-
ultaneous access to their individual Patches. This opens the door to exciting live collaboration possibilities.
Note this also means that anyone in your group running Studio One Remote with access to your Studio One network can change anyone
else’s Patches… or jump to a new Arranger Section... or perhaps even stop the show—so be sure to share this access to people you
trust!

## Performance View
