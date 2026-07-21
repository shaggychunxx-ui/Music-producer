# Video Playback and Sync

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 547–553
> **Slug:** `20-video`

**Agent topics:** `video player`, `video track`, `sync`, `export video`

---

Video Playback and Sync
Studio One Professional has a built-in Video Player and Video Track that enables you to score to picture by syncing Song and video play-
back. The following chapter describes how to use video features in detail.
Video Player Interface
Open the Video Player by clicking on the Video Player icon in the toolbar, the Video Player icon on the Video Track header, or by select-
ing it from the View menu. When first opened, you see a black screen with the text “Movie Not Loaded” displayed. The bottom toolbar con-
tains controls for the video player as follows:
-
Video Options (wrench icon) Choose to display the video as Tiny, Small, Normal, Medium or Large.
-
Timecode Display Click to toggle the display of timecode on the bottom right of the Video Player. Available timecode
formats include Video Frames, Bars, Seconds, Samples, and Frames. Note that “Video Frames” refers to the framerate
of the video itself, while “Frames” refers to the frames of the Global Ruler Track.
-
Stop/Play Click to stop or start video playback independent of the Song.
-
Mute This is engaged by default and mutes the audio output from the video. Click to disengage if you want to hear the audio out-
put from the video.
-
Size Click-and-drag the lower right corner of the video player to freely size the window.
In the upper right corner of the video player, there are buttons to maximize the video player window and to close the video player.

## Video Track

 Video Playback and Sync

The video track allows for placement of a video for playback in sync with your Song; very useful for scoring to motion pictures. Videos can
be moved across the timeline and lightly edited, and you can even extract their audio to a separate track. The Video Track works in con-
junction with the Video Player.
Add video clips to the Video Track by dragging and dropping from Studio One’s Browser or your operating system’s file browser. Sup-
ported filetypes vary by operating system; some filetypes are supported on Mac or Windows, but not both.
Compatible filetypes are addressed in the Import Video topic.
The Video Track can hold an unlimited number of video clips.
Audio Sub-track
Click the waveform icon at the track header to display the video’s Audio Sub-track. You’ll also find a dedicated Channel for this Sub-track
in the Console. This special Audio Track will always stay aligned with the position and editing of its host video, and cannot be time-
stretched or have Event FX applied to it. If you require this sort of functionality applied to this audio data, drag an Audio Sub-track Event
down into the Arrange Window to create a new Track from this audio.
Video Editing
Studio One’s primary focus is audio production, of course, but rudimentary video editing is possible within Studio One’s Video Track by
use of the same commands and tools used to edit Audio Events, including:
-
Trim
-
Cut/copy/paste
-
Slip
-
Nudge
-
Time locks and edit locks
-
Ripple Edit
-
Duplicate
-
Replace (Useful if a newer edit of the same video becomes available and the current timecode position of the clip needs to
remain unchanged.)
Note that Video Events cannot be split into segments shorter than one second.
Video Track Options
Right-click the Video Track Header for a contextual menu of the following options:
-
Hide Audio Track toggles visibility of the Video Track
-
Link Audio Track Editing toggles the link between the Video and it’s associated Audio Sub-track, allowing you to edit them
independently or together
-
Remove Audio Playback Track lets you remove the Audio Sub-track altogether
-
Use Video Frame Rate in Timeline lets you set your Song to match the Frame Rate of the Video

## Video Track

Video Track Inspector
The Video Track’s Inspector also gives you one-click access to some of the above features, plus:
-
Show Thumbnails Hide/unhide the video thumbnail images in the Video Track
-
Show Frame Numbers Hide/unhide the frame number displays in the Video Track
-
Show Audio Track Hide/unhide the Audio Sub-track
-
Link Audio Track Editing toggles the link between the Video and it’s associated Audio Sub-track, allowing you to edit them
independently or together
Video Metadata
Video metadata, including pixel dimensions, framerate, codec, and more, can be found atop the contextual menu when right-clicking a
Video Event, or at the bottom of the Browser when the video clip is selected in the Pool.

## Import Video

The simplest way to import a video file is to drag-and-drop it from the File Browser into the arrangement. Supported video files appear in
the browser with a Film Strip icon. You can also use the Import Video menu in the Video Player to import any supported video file.
Drag a video file from the File Browser or your OS’ Finder/Explorer to the arrangement to import the video file to the Video Player.
Hold [Ctrl]/[Cmd] while dragging to only extract the audio from the video and place it in the position to which you drag. Hold [Alt] while
dragging to simultaneously import the video file to the Video Player and extract the audio from the video and place it on an audio Track.
Supported filetypes are based on your Operating System and as such will vary between Mac and Windows.
We recommend that all videos imported to the Video Track in a single Song be of the same format and framerate. Using various video
formats and filetypes may lead to unexpected results.
Mac:
Supported codecs by container format:

## Import Video

H.264
HEVC*
MPEG
Apple ProRes
QuickTime
x
x
x
x
MPEG-4
x
x
M4V
x
x
*.MKV are not recognized by Quicktime, and therefore not recognized by Studio One.
Windows
Supported Codecs by container format:
H.264
HEVC*
MPEG
MPEG-PS
x
x
MPEG-4
x
x
M4V
x
x
Hold [Ctrl]/[Cmd] while dragging to only extract the audio from the video and place it in the position to which you drag. Hold [Alt] while
dragging to simultaneously import the video file to the Video Player and extract the audio from the video and place it on an audio Track.
Sync to Video
Once the video has been imported, as long as the Online button in the Video Player is engaged, Song and video playback will be in sync.
When you locate the timeline cursor while stopped or during playback, the video adjusts to the correct frame.
When video playback starts, a small amount of data needs to be pre-loaded. Should there be a resulting timing offset between the video
and Song playback, Studio One syncs the video during playback. This may cause the picture to jump a little after start, which is normal.
For a smooth start of video playback we recommend that you stop, locate, and then start.
Frame Rates
 Sync to Video

In common practice, it is good for you to know the frame rate of the video you are working with, and to set that frame rate in the
Song/Song Setup/General menu. You may choose from the thirteen Frame Rates shown above. Ideally, you should have a reference
timecode burned into the video itself so that you can compare the Song frame position with the video timecode position and ensure accur-
ate frame sync.
Using Follow Edit Position with Video
It is common to use markers to denote hitpoints in the video; that is, time positions where the sound should sync closely with the video.
Refer to Using the Marker Track for information on how to use markers. When adjusting the position of a marker, it is possible to have
the playback position, and thus the current video frame, follow the marker position. To do this, enable Follow Edit Position in the toolbar,
next to Follow Song. This helps you accurately place markers to use as hitpoints while viewing the exact frame to which the marker cor-
responds. Similarly, Follow Edit Position helps when trying to sync Event or Note position with video.
Bar and Time Offset
Studio One offers two options for setting up an offset for your timeline. These allow you to set a time offset relative to the musical (Bars,)
and timecode (Frames), which can be reset to zero at any point in your Song, independent of SMPTE. Options include:
-
Set Bar Offset to Cursor
-
Set Time Offset to Cursor
Set Bar Offset to Cursor and Set Time Offset to Cursor can be accessed via the Song drop-down menu, or the contextual menu when
right-clicking inside the Ruler. You can also trigger it from a Keyboard Shortcut or Macro.
Bar and Time Offset

Set Frames at Cursor…
Set Frames at Cursor… can be used to assign a desired frame value to the current location of the playback cursor.
Frames Enter the desired frame number for the current location of the playback cursor.
Frame Rate Enter the desired frame rate here.
From Video Click this button to match the (supported) frame rate of the Video Event currently aligned with the playback cursor position.
Video Metadata
Video metadata, including pixel dimensions, framerate, codec, and more, can be found atop the contextual menu when right-clicking a
Video Event, or at the bottom of the Browser when the video clip is selected in the Pool.

## Exporting Video Files

The process of importing a video and extracting its audio track is described in the Video Playback and Sync chapter. Extracting the
audio from the video file is an important step, because otherwise the audio from the video will not be exported with the Song.

## Exporting Video Files

To export the Song to a Video file, select Export Video from the Song menu. Choose a file name and storage location in the pop-up win-
dow, and then choose the File Type, Video Codec, and Audio Codec. Note that the codec options are provided by your computer's oper-
ating system, and the options could change when an OS update is released.
Next, choose the Export Range. This can be defined by the length of the video, by the Loop points, or by certain Markers within the Song.
Mixdown Options are provided too, such as the preferred Output, Mono export, and whether to include the master effects when the file is
rendered. Select Use realtime processing if external devices are part of the mix.
Once those decisions are made, click OK or Save to export. The Video file will be created and given the appropriate file extension.
Video Format options include:
File Type:
-
Quicktime Video
-
MPEG-4 Video
-
M4V Video
Video Codec:
-
JPEG
-
H.264
-
HEVC
-
Apple ProRes 4444
-
Apple ProRes 422 HQ
-
Apple ProRes 422
-
Apple ProRes 422 LT
-
Apple ProRes 422 Proxy
-
Audio Codec:
-
AAC
-
ALAC

## Exporting Video Files
