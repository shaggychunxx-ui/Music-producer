# Saving, Import and Export

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 554–559
> **Slug:** `21-saving-import-export`

**Agent topics:** `import song data`, `export audio`, `export MIDI`, `AAF`, `zip`, `import other DAWs`

---

Saving, Import and Export
Studio One provides several ways to save your work, and even more methods of exchanging data with other applications.
This is done by importing or exporting of various format types.

## Import Song Data

There are many situations in which importing data from one Song to another can be useful. Whether you want to create an alternate ver-
sion, re-use musical content in a new composition, or bring in useful non-musical content, you can make that happen with the Import
Song Data function. Apart from Audio and Instrument tracks, you can also import the Tempo Track, Marker Track, and Chord Track from
one Song to another.
To begin, navigate to Song/Import Song Data and choose a .song file from your file system to open the Import Song Data window. You
can also reach this function by navigating to the song of your choice in the Files tab of the Browser, [Right]/[Ctrl]-clicking a .song file and
choosing Import Song Data from the pop-up menu.
The Tracks column on the left lists the available tracks in the Song. Click the check boxes next to the Tracks of your choice to mark them
for importing.
The Track Options section lets you choose whether or not to import the Events, Layers, or Automation from the selected tracks. This lets
you do things like reusing the track structure of a Song as a template for a new Song without bringing in any note data, or for stripping
extensive automation data when starting an alternate mix.
In the Media Options section, you can choose whether or not to copy the related media files from the original Song to the new one.
In the Console Options section, you can choose whether to bring over Volume & Pan settings, Inserts, Sends, and Instruments to the
new song. Feel free to exclude any of these elements if you want to start fresh.
Tick the boxes to select your desired Tracks and options — you can also click and drag vertically to select / de-select multiple items very
quickly. Once you've selected your desired Tracks and selected your chosen options, click [OK] to import the Tracks to the current Song.

## Exporting Audio and MIDI Files

Follow the procedures below to export selected Audio Events as audio files, or Instrument Parts as Standard MIDI files or
MIDI Musicloops.
Saving, Import and Export

Exporting Audio Files
To export an Audio Event to an Audio File, [Right]/[Ctrl]-click on the Event and select Export Selection. Choose a file name and storage
location in the pop-up window and click OK or Save to export.
You can also drag-and-drop any Audio Event to a location in the File Browser to export it as an audio file to that location. As you hover
over the Browser, you can press [Alt] to choose between rendering the Audio Event with or without its associated Insert FX.
Exporting MIDI Files
You can export an entire Song as a .MID file using the Save As… or Convert To… command from the File menu. All tempo information,
tracks, and track names will be retained.
Audio Events will, of course, be ignored.
To export an Instrument Part to a MIDI file, [Right]/[Ctrl]-click on the Part and select Export Selection. Choose a file name and storage loc-
ation in the pop-up window, and choose a file type (Musicloop or Standard MIDI file). Then click OK or Save to export. A file will be cre-
ated with the appropriate file extension (.musicloop or .mid).
Multiple Instrument Parts can be exported at once to a single file. To do this, select the desired Parts and use the same process as
above, choosing the Standard MIDI option in the save window. One MIDI file is created that includes individual MIDI clips for each Part, in
the correct sequence, with a common start time.
You can also drag-and-drop any Instrument Part to a location in the File Browser to export a Musicloop or MIDI file to that location. As
you hover over the Browser, you can press [Alt] to choose between Musicloop and MIDI file formats. If you drag-and-drop multiple parts
at once, they are written to one MIDI file with multiple Parts.
Standard MIDI Files exported from Studio One can be used by virtually any application that supports MIDI.

## AAF Import and Export

AAF (or Advanced Authoring Format) is a professional cross-platform file interchange format supported by many DAWs, non-linear video
editors, and other media authoring tools. Given that most major software platforms are unable to read the project files created by other
platforms, it is useful to be able to employ a neutral format that many tools can use.
The AAF support in Studio One is particularly robust, allowing the import and export of mono and stereo audio files, automation data,
fades, and crossfades.
Exporting AAF
To export a Song in AAF format, navigate to File/Save As... or File/Convert To... and choose "AAF File (*.aaf)" from the [Save as type:]
selector. Select a target location and choose a name for your new AAF file, then press Save. Then, you have a few useful options to
choose from:
-
Embed audio Store WAV and AIFF files from your Song within the exported AAF file. If disabled, references to files are used
instead.
-
Split stereo tracks Convert stereo tracks to mono pairs. This ensures compatibility with applications which do not support
import of stereo tracks.
-
Convert audio files Create copies of all audio data in a different format for export.
-
Trim audio files Discard silent regions in audio files to reduce the file size of your AAF project.
-
Export pan Include pan automation in your AAF export. Some DAWs do not accept pan automation in AAFs, so if you have
trouble importing your AAF, try re-exporting it with this option disabled.
-
Legacy mode Enable to improve compatibility with older applications.
Note that AAF only recognizes standard audio files, so you may want to render your Audio and Instrument Tracks as continuous audio
files before exporting the AAF. One easy way to do this is to save a copy of your song to use for export, then select all of your Song con-
tent and navigate to Event/Bounce Selection (or [Right]/[Ctrl]-click one of the selected Parts and choose Bounce Selection from the pop-
up menu). Then, just remove any Instrument Parts that were bounced, and your Song is ready to export.
Importing AAF
To import an AAF into Studio One, open or create a Song, then simply drag-and-drop the AAF file onto the timeline. You can also import
an AAF by navigating to File/Open and choosing the AAF file, or by double-clicking the AAF file in your file system. Any available audio
tracks and one video track referenced in the AAF are added to your Song.
Note that only one video file can be imported, so if the source project contains multiple video clips, they should be consolidated in the ori-
ginal NLE or DAW before the AAF is exported. Only the raw video is imported, without any filters or VFX.

## AAF Import and Export

Importing Project Files from Other Applications
Studio One can open several other application project file types. These include PreSonus Capture™Sessions (.capture), DAWproject
(.dawproject), Steinberg Cubase Track Archives (.xml), Steinberg Sequel Projects (.steinberg-project), Kristal Audio Engine Projects
(.kristal), and Open TL (.tl). To open any of these project file types in Studio One, navigate to File/Open, and select the desired file, or
drag and drop the file onto Studio One itself.
StudioLive/Capture Mix Import
When a Capture session containing StudioLive mix data is opened in Studio One, all fader, pan, and mute settings are imported along
with any Fat Channel XT settings, and a Fat Channel XT plug-in is inserted on each Channel. All Submix Busses (including their channel
routing) are imported into Studio One as well. Empty FX Busses are created for each Send effect and send levels per Channel are impor-
ted. Pick any suitable reverb or delay plug-in and manually adjust the FX Bus level and plug-in settings to your taste.
See Fat Channel XT for more information about working with Fat Channel XT presets.

## Export to Zip

From the File menu, you’re able to export Studio One documents—Songs, Shows, and Projects—with all of their referenced media files
to a Zip file for easy backup and sharing. In addition, all unused files are removed from the exported Zip to keep it as small as possible.
You can access this via either the “Save as” or “Convert to” options.
When doing so, you’ll be presented with this dialogue box:
Importing Project Files from Other Applications

Options:
-
Lossless audio file compression (FLAC) When ticked, the audio files in the exported Zip will be converted to .flac. This does
not apply to audio files used in an instrument like Sample One)
-
Upload to Studio One+ When ticked, your new Zip file will be uploaded to your Studio One+ account, if you have one. You’ll
be prompted with a dialogue box showing your list of available Workspace locations for upload. Your new Zip file will still be avail-
able saved locally.
You’ll also receive a list of packages (Sound Sets, etc.) and plug-ins that are used in the document. Note that these packages and plug-
ins are commercial and copyrighted and will not be included in your Zip for copyright reasons. This is useful information in the event that
you want to share a Song with a collaborator who does not own the same plug-ins that you do.
The Zip file created will only contain files referenced by the document. Files in the Pool will only be added if they are used in Zipped Song.
Additionally, alternate Versions of Songs will not be included in the Zip.
Opening Zip Files
Zip files created with Studio One’s Zip exporter can also be opened using File >> Open. These documents will then be imported to your
Songs/Shows/Projects folder before the Song, Show, or Project is opened.
Alternatively, if the Zip file had been uploaded to Studio One+ , these Zip files will be shown in the Browser—and can be downloaded and
unpacked with simple drag and drop.
Saving Options
Studio One offers you multiple ways to save the work in progress of your documents (Songs, Shows, or Projects), backup your files, auto-
mate your work saves, and export to multiple formats. Each is a different tool for a different job.
Save
Saves the active document, overwriting it with the original name and filepath. All related media (Audio clips, MIDI, etc.) are stored in the
document’s Media subfolder and linked to the .Song, Show, or Project file.
Save As…
Saves the current document with the options to choose a new file path and/or a new filename. Save As… only saves the .Song,
.Show, or .Project file to a new location, and does not create a new Media subfolder or copies of linked media like Audio clips and MIDI.
Media is linked from this new document to its original file path location. This new document file becomes the active working document in
Studio One.
The Save As… command can also be used for exporting your document to various formats including:
-
AAF File - Advanced Authoring Format. More details here.
-
Capture Session - A proprietary PreSonus format for use with PreSonus Capture.
-
MIDI File - a .MID file. More details here.
-
OpenTL - Tascam’s Open Tracklist format.
-
Zip File - Compresses your entire document and all of its related media into a single Zip file for easy sharing and backup.
Unused files are excluded from the Zip, as are alternate Song Versions. More info on Zip Export here.
Save to New Folder
Saves the current document with the options to choose a new file path and/or a new filename. Save to New Folder saves the .Song file to
a new location and creates a new Media subfolder and copies of linked media. This is a good way to create a new “working copy” of all of
the files required to continue work on a Song, Project, or Show. In addition, all unused media files are not included in this new folder to
save on disk space.
This new document file becomes the active working document in Studio One.
Save New Version
Saving Options

A special save option that gives you the option to create an alternate version of a document while continuing your work on the original.
Save New Version will store a new file in your original working folder, and will not create a new Media subfolder.
Incremental version:
-
Tick this box to save your document as an incremental version and update your document file and continue to work on the new
incremental version.
-
Leave unticked to save your document as an alternate version located in your documents History subfolder and continue work-
ing on the original document.
Use the “Restore Version” option from the File menu to access previously saved Versions of a currently open document.
Save as Template
Saves your .Song, .Project, or .Show file to Studio One’s “templates” subfolder, causing it to appear in the New Song or New Show
menus under the “User” tab. Media subfolders are not copied to this location.
Convert To
Convert To allows you to quickly save your currently-opened Studio One document (Song, Show, or Project) to another file format.
Options include:
-
AAF File - Advanced Authoring Format. More details here.
-
Capture Session - A proprietary PreSonus format for use with PreSonus Capture.
-
MIDI File - a .MID file. More details here.
Saving Options

-
OpenTL - Tascam’s Open Tracklist format.
-
Zip File - Compresses your entire document and all of its related media into a single Zip file for easy sharing and backup.
Unused files are excluded from the Zip, as are alternate Song Versions. More info on Zip Export here.
Autosave
Autosave is located in Studio One’s Preferences under Locations >> User Data. You can set the frequency with which it automatically
runs a typical Save command as described above. Note that Autosaves are not performed during playback to avoid producing any aud-
ible artifacts or interruptions.
Options include:
-
Used cached plug-in data on save Tick this box if you would like to avoid Studio One requesting to save your plug-in settings
on each Autosave. When this box is ticked, Studio One will refrain from querying plug-ins to for all of their settings on each Auto-
save, and instead their last state will be used from thecache. When using plug-ins that have a lot of parameters, this can
decrease the saving time of your documents.
-
Ask to copy external files when saving Song tick this box if you would like to be prompted to make copies of linked media
when Autosave runs.
Ask to Copy External Files when Saving Document
This option, located in Studio One’s Preferences under “Locations,” will prompt Studio One to ask if you would like it to make local copies
of any external files in the save operation.
In this context, “External Files” are any files that are not already a part of the current document’s folder structure. A common example of
External Files could be a new sample pack that you excitedly saved to your desktop and brought into Studio One before filing it with your
other samples.
This also allows you to move a document’s folder without worrying about the inclusion of content stored in other locations.
Ask to Copy External Files works with Songs, Projects, and Shows.
Saving Options
