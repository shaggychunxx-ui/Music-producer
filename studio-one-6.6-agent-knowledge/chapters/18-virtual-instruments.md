# Built-In Virtual Instruments

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 478–532
> **Slug:** `18-virtual-instruments`

**Agent topics:** `Sample One XT`, `Presence XT`, `Impact XT`, `MaiTai`, `Mojito`, `Multi Instruments`, `Note FX`

---

Built-in Virtual Instruments
Studio One has five built-in virtual instruments: SampleOne XT, Presence XT, Impact XT, Mai Tai, and Mojito. These instruments provide
a solid foundation for music production in any style. The following sections describe each instrument in detail.
SampleOne XT
A sampler is a bit like a synthesizer. However, instead of generating sounds using oscillators or operators, samplers start with an audio
clip, or “sample,” and then play and process that sample based on how the instrument is configured.
SampleOne XT is a full-featured sampler that builds on the strengths of our original SampleOne instrument. It features triggered
sampling, automatic time-stretching, a full range of tone-shaping tools, and flexible onboard effects. The following section describes how
to use SampleOne XT.
Interface Overview
The main display features four "tabs" along the top, each of which gives you access to a distinct set of tools and parameters:
-
Wave is where you do the bulk of your sample and loop editing.
-
Mapping is where you map the loaded samples across the span of the MIDI range.
-
Envelopes gives you access to graphical representations of the Pitch, Filter, and Amp envelopes, for easy shaping.
Built-in Virtual Instruments

-
Record lets you record audio directly into SampleOne XT from nearly any audio input, send, output, or Instrument track, includ-
ing a mode where samples are split automatically based on amplitude.
To the right of the tabbed interface is the Samples list, which shows the samples that make up the current patch. In the lower half of the
plug-in interface, you'll see controls for sample Pitch (playback frequency), Filter (tone shaping), Amp (amplitude shaping), LFO (mod-
ulation), and effects. Rounding things out are the global settings in the Master module, and a playable onscreen keyboard.
Wave View
Wave view is where you do the bulk of your sample and loop editing. To select the range of the sample that plays when you trigger it,
click-and-drag the blue triangles below the waveform. To fine-tune the start-and-end points, you can click-and-drag or click and type a
value into the Start and End fields.
Trigger
Open the Trigger menu to choose the method by which to play the currently selected sample, from the following choices:
-
Normal In this mode, the sample starts playing when you trigger it, and stops when you let go of the key (or when the recorded
note that triggers it ends).
-
One Shot In this mode, the sample plays through in its entirety when triggered. This is often used for drum sounds.
-
Toggle In this mode, the sample begins playing when triggered, and stops playing when triggered a second time. This is most
useful for loops and continuous, droning sounds.
Reverse Enable this option to reverse the current sample.
Normalize Enable this option to boost the amplitude of the current sample until its highest peak reaches a point just below full scale.
Load Next/Previous Sample in Folder These buttons let you quickly swap the current sample for its neighbor in the enclosing folder.
This allows for quick auditioning of a range of samples, to find just the right candidate.
Root, Low, and High These selectors let you set the root note and note mapping for the current sample. You can also set these para-
meters in the dedicated Mapping view.
Loop a Sample
To loop playback of a sample, open the Loop selector and choose a looping mode:
-
Sustain In this mode, when a note ends, playback continues beyond the selected loop range until the end of the release phase
of the Amp envelope.
-
Release In this mode, when a note ends, playback continues to loop until the end of the release phase of the Amp envelope.
-
Ping-Pong In this mode, loop playback proceeds to the end of the loop range, then the sample is played in reverse until it
reaches the beginning of the loop range, and so on.
When a looping mode is selected, the Loop Range bracket appears above the sample waveform, indicating the section of the sample to
be looped. If the loop range begins after the initial playback range begins, the sample plays from the beginning of the playback-range pos-
ition to the end of the loop-range position; then it plays from the start of the loop range to the end of the loop range and back for as long as
the sample is triggered.
X-Fade Click-and-drag or click and type in this field to specify a number of samples of crossfade to apply to the loop points, to assist in
removing audible clicks.
SampleOne XT

Follow Song Tempo Enable this option to automatically timestretch the current sample to fit the tempo of the Song. This is most effect-
ive when using rhythmic loops, such as drum samples. The sample must be tempo-tagged to enable this feature. Note that timestretched
stereo samples will replay in mono.
All Notes Off Click this button to stop playback of all currently enabled voices.
Mapping View
Mapping view shows each currently loaded sample as a Keymap Range selector that occupies a certain range of MIDI notes. The bright
mark within each selector shows the current root note of the sample.
To change the root note of a sample, click-and-drag the sample's root-note handle left or right across the keyboard display. The notes on
your keyboard that trigger the sample are indicated in the Keymap Range selector, which is the blue bar extending to the right and left of
the note handle. To restrict the range of notes that can trigger the sample, click-and-drag the left or right edge of the Keymap Range
selector.
Envelopes View
Envelopes view gives you graphical representations of the Pitch, Filter, and Amplitude envelopes that you can freely shape using the
mouse. Click-and-drag the handles on each envelope to change the shape. The Attack, Decay, Sustain, and Release values are shown
as numeric selectors below each envelope. These can also be changed by click-and-drag or click-and-type. Below them are the curve
controls for each applicable envelope value ("AC" for "Attack Curve," "DC" for "Decay Curve," and so on), which let you precisely set the
curve of each envelope segment.
SampleOne XT

Record View
Record view lets you record audio directly into SampleOne XT, for immediate use as new samples. To do this, first select the Input to
record, which can be any hardware audio input, send, output, or Instrument output. The Monitor selector lets you choose which bus
should receive the cue signal for monitoring as you record.
There are two main ways you can record:
-
Record Press Record to begin recording immediately. Press the button again to conclude recording. The resulting audio is
shown in the Samples list, and is then available for use.
-
Gate Record Press Gate Record to enable amplitude-based recording, in which each distinct region of audio (as specified by
the Gate Threshold controls) is recorded as a separate sample. This is a great way to record a set of drum samples, for
example.
Gate Threshold The Open setting specifies the signal level at which recording begins while in Gate Record mode. The Close setting
specifies the signal level at which recording ends. You can also set these ranges by clicking-and-dragging the triangle-shaped markers in
the signal level display.
Name This field lets you specify the name of the next recorded sample. If more than one sample is recorded before the name is changed,
the samples will share the specified name, followed by a numeric identifier.
Resolution This selector lets you set the bitrate of the recorded samples.
Insertion Key This selector lets you choose the initial root note of the recorded samples. If more than one sample is recorded before the
Insertion Key is changed, the samples are assigned to the next-higher note each time.
Samples List
SampleOne XT

To add a sample to SampleOne XT, drag any audio clip from the Browser, or any Audio Event or selected range from the Arrange view,
into the Samples list. The waveform for the audio clip appears in the main display. If you drag in a selected range from the Arrange view,
the range is bounced to a separate audio file and then added to SampleOne XT.
Note you can quickly access samples that are in the same file location as a loaded sample by using the [Previous] and [Next] button to
switch to the previous or next sample in that file location.
By default, the keymap range is set from C0 to B5, with C3 set as the sample’s root note. With the SampleOne XT instrument Track prop-
erly set up, and Monitor engaged, press any key within the default keymap range on your keyboard to play the loaded sample. C3 is set
by default as the sample’s root note, so playing the C3 (middle C) key on your keyboard plays the sample at its original pitch and speed.
Playing the keys above C3 shifts the sample pitch higher, and playing below C3 shifts the sample pitch lower and slows down playback
speed.
When adding a REX file to SampleOne XT from the Browser with the Send to New SampleOne XT command, the REX file’s individual
slices are mapped across the keymap (starting at C3 by default, dependent on number of slices), with each slice given its own note.
Playing Multiple Samples
Up to 96 samples can be loaded into SampleOne XT at once, with each loaded sample displayed in the sample list. Select any sample in
the list to edit its playback, loop, and keymap range, as well as its root note and loop status. All loaded samples are triggered sim-
ultaneously, depending on the keymap range for each sample. For instance, if C3 on your keyboard is set to trigger every sample, press-
ing C3 triggers every sample at once. In this way, multilayered, or multitimbral sample-playback can be achieved.
Replace a Sample
To replace a sample in SampleOne XT, select the sample that you wish to replace in the Samples list. Then drag any audio clip from the
Browser, or any Audio Event from the Arrange view, into the main display. The sample replaces the previous one in the sample list, and
the previously displayed sample waveform updates to reflect the new sample.
Edit Sample This button lets you specify individual envelope settings for the currently selected sample, rather than changing those para-
meters for all samples, as done by default. If after you've made custom alterations to one sample, you wish to reunify all samples under
the same settings, press Reset.
Edit Pitch, Filter, and Amplifier Parameters
The output of each sample loaded in SampleOne can be modified with pitch, filter, and amplifier parameters. Note the [Edit All] button,
which allows the simultaneous editing of all sample parameters at once when engaged. The following describes the use of these envel-
opes.
Pitch
The Pitch controls modify the pitch characteristics of the audio output. Click the button in the upper left corner of the module to activ-
ate/deactivate the effects of the Pitch controls.
-
Transpose Transposes the pitch of the sample in semitones. Variable from -48 to +48 semitones.
-
Tune Adjusts the tuning of the sample. Variable from -100 cents to 100 cents.
-
LFO Adjusts the range within which the LFO affects pitch. Variable from -4 octaves to +4 octaves.
-
Env Adjusts the range within which the envelope affects pitch. Variable from -4 octaves to +4 octaves.
-
Attack (A) Adjusts the amount of time it takes to reach the Env value from the original pitch of the sample once a sample has
been triggered. Variable from 0 to 20 seconds.
-
Decay (D) Adjusts the amount of time it takes to reach the sustain level after reaching full volume. Variable from 0 to 20
seconds.
-
Sustain (S) Adjusts the Sustain level. Variable from -∞dB to 0 dB. The sustain period continues until the sample trigger stops.
-
Release (R) Adjusts the amount of time it takes to reach the original pitch after sample trigger has stopped. Variable from 0 to 30
seconds.
SampleOne XT

Filter
The Filter parameters modify the frequency characteristics of the audio output. Click the button in the upper left corner of the module to
activate/deactivate the effects of the filter.
-
Cutoff Adjusts the filter cutoff frequency. Variable from 20 Hz to 20 KHz.
-
Vel Adjusts the maximum range, in octaves, within which note velocity can affect the maximum filter range (the value
used when velocity equals 127).
-
Press Adjusts the amount that Note Controller Pressure affects the filter cutoff. Positive values will raise the cutoff fre-
quency as pressure increases. Negative values will lower the cutoff frequency as pressure increases.
-
Mod Adjusts the range, expressed as distance in octaves, within which the modulation wheel on your Keyboard can
adjust the instantaneous filter cutoff frequency (the value used when the mod wheel value equals 127).
-
LFO Adjusts the range within which the LFO affects the cutoff frequenecy. Variable from -8 octaves to +8 octaves.
-
Env Adjusts the range within which the envelope affects the cutoff frequency. Variable from -8 octaves to +8 octaves.
-
Res Adjusts the relative resonance of the filter. Variable from 0 % to 100 %.
-
Type Selects the filter type. Choose from LP24 Ladder, LP24 Zero-Latency, LP12 Ladder, BP12 Ladder, HP12 Ladder, LP12
State, BP12 State, HP12 State, and Eco Filter (lowest CPU use).
-
Attack (A) Adjusts the amount of time it takes for the filter cutoff frequency to move from the frequency value to the envelope
value once a sample has been triggered. Variable from Variable from 0 to 20 seconds.
-
Decay (D) Adjusts the amount of time it takes to reach the sustain level after reaching the envelope value. Variable from Vari-
able from 0 to 20 seconds.
-
Sustain (S) Adjusts the sustain level, which is the mix of the signal filtered at the envelope value with the signal filtered at the fre-
quency value. Variable from -∞dB to 0 dB. The sustain period continues until the sample trigger stops.
-
Release (R) Adjusts the amount of time it takes the filter to reach the frequency value after the sample trigger has stopped. Vari-
able from Variable from 0 to 30 seconds.
-
Drive This lets you specify an amount of filter overdrive, to add fullness and saturation artifacts to your sound.
-
Punch This control lets you add a range of percussive attack to the start of each note. At the lowest setting, dynamics are
unchanged. At higher settings, the sound becomes more aggressive and more readily pops through the mix.
-
Key This control sets the relationship between incoming note Pitch and filter Cutoff. In physical instruments, higher notes tend to
produce higher harmonics, brightening slightly as you go up the scale. On a synthesized instrument, if the filter stays static, set-
ting the proper tone in the lower note ranges may cause inappropriate dullness in the higher notes. So, with the Key parameter,
we can compensate for this, and create a more natural-sounding range of timbres up and down the keyboard.
-
Soft This control lets you switch between two differing analog-modeled processing circuits within the filter. Engage Soft for a
mellower, darker tone. Disengage it for a brighter, more aggressive sound.
Amp
SampleOne XT

The Amp controls modify the amplitude characteristics of the audio output. Click the button in the upper left corner of the module to activ-
ate/deactivate the effects of the Amp controls.
-
Gain Adjusts the maximum volume of the audio output. Variable from -144 to +20 dB.
-
Vel Adjusts the relative amount that note velocity affects the maximum amplitude. Variable from 0 to 1.
-
Press Adjusts the amount that Note Controller Pressure affects the maximum amplitude. Positive values will raise the
volume as pressure increases. Negative values will lower the volume as pressure increases.
-
Mod Adjusts the relative amount that the modulation wheel on your Keyboard can adjust the instantaneous amplitude
at any time. Variable from -1 to 1.
-
LFO Adjusts the range with which the LFO affects playback volume.
-
Pan Adjusts the stereo pan of the audio output. Variable from full L to full R.
-
Attack (A) Adjusts the amount of time it takes to reach full volume once a sample has been triggered. Variable from 0 to 20
seconds.
-
Decay (D) Adjusts the amount of time it takes to reach the sustain level after reaching full volume. Variable from 0 to 20
seconds.
-
Sustain (S) Adjusts the sustain level. The sustain period continues until the sample trigger stops.
-
Release (R) Adjusts the amount of time it takes to reach a level of -∞after the sample trigger has stopped. Variable from 0 to 30
seconds.
LFO
Various parameters of SampleOne can be modulated, or varied over time, with the LFO. The following describes how to use the LFO to
modulate parameters.
-
LFO Click the Activate button to activate/deactivate.
-
Sync/Free Choose to sync the modulation speed to tempo (variable from 1/64T to 4 bars), adjust the speed freely as frequency
(variable from 0.01 Hz to 500 Hz), or sync to note-on by selecting neither Sync nor Free (variable from 0.01 Hz to8 KHz).
-
Rate Set the modulation speed of the LFO, in either rhythmic subdivisions of the Song tempo (Beats), or milliseconds (Speed),
depending on Sync/Free status.
-
Type Click to select, from top to bottom, the sine, saw, triangle, square, or sample and hold LFO waveform.
-
Delay Adjusts the amount of time before the LFO affects anything once a sample is triggered. Variable from 0 to 2 seconds.
-
Mod Adjusts the peak amplitude amount with which the modulation wheel controls the LFO signal strength (LFO strength when
mod wheel value equals 127). Variable from -1 to 1.
Master
The Master controls act on a global level, affecting all samples in the current patch.
Master Sets master volume for the entire patch. Variable between -∞and +10 dB.
Mono Turn on this option to enable monophonic playing (one voice at a time only).
Glide Enable this option to introduce Glide, and adjust the relative amount of Glide using the Glide Time knob below. Glide creates
gradual shifting over time between consecutive notes, as opposed to the usual immediate switch from one note to the next.
SampleOne XT

Polyphony By default, up to 32 voices can play simultaneously, meaning you can play 32 separate notes before the first note you played
are cut off to allow more voices to play. Click and drag on the blue number to add or subtract total voices. 64 voices is the maximum.
Effects (FX A & FX B)
SampleOne XT offers seven built-in effects processors to add dimension to your sounds. They are arranged in two banks: FX A (Mod-
ulation, Delay, and Reverb) and FX B (Gater, EQ, Distortion, and Pan). You can enable or disable each effect by clicking its name. You
can show or hide the FX section of the plug-in window by clicking the [FX] button.
FX A
Modulation
This processor creates time-based modulation effects. Choose from the following modes by clicking the [Chorus], [Flanger], or [Phaser]
button:
-
Chorus This processor creates effects similar to that of multiple identical instruments playing the same part simultaneously. The
synth signal is fed through a short, modulated delay, which is then mixed with the dry signal. Chorus offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay. Higher settings create full-bodied chorusing effects,
while lower settings create more pronounced harmonics, akin to the effects of a Flanger.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler chor-
using effects, while higher settings produce more pronounced changes in timbre over time.
-
Depth This control lets you blend between the dry signal (all the way left) and the chorused signal (all the way right).
-
Flanger This processor creates resonant, hollow-sounding sweeping effects. The synth signal is fed through a short, modulated
delay, which is mixed with the dry signal. While similar to the workings of a Chorus effect, Flangers get their signature sound by
employing smaller delay times than those used in chorusing, combined with a feedback system that can add extra resonance to
the sweep. Flanger offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay (in ms), which changes the pitch of the resultant res-
onance. Higher settings create lower-pitched resonance, while lower settings create resonances at a higher pitch.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler flanging
effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Flanger. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Flanger modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the flanged signal (all the way right).
-
Phaser This processor creates dreamy, otherworldly sweeping effects. The synth signal is fed through a series of all-pass filters
that alter its phase. When mixed with the dry signal, this creates a series of peaks and valleys in the frequency response that
changes depending on the degree of phase shift applied. Phaser offers the following controls:
SampleOne XT

-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Shift This control lets you specify the amount of phase shift to apply. Lower settings focus the phasing effect in the
lower frequencies, while higher settings focus the effect in higher frequencies.
-
Speed This control lets you set the speed of modulation applied to the phase shift amount. Lower settings create slow,
sweeping effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the phase shift amount is modulated. Lower settings produce
subtler effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Phaser. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Phaser modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the phase-shifted signal (all the way
right).
Delay
This processor creates an echo effect, either as a single delayed repeat of the input signal, or a trailing series of echoes. The Delay effect
offers the following controls:
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the delayed signal.
-
Delay Time This control lets you specify the length of the delay effect, in rhythmic values (such as 1/8th-note or 16th-note) rel-
ative to the tempo of the Song.
-
Feedback (FB) This control lets you set the amount of effected signal that is fed back into the Delay effect. At zero, there is just
one repeat. As you increase the value, the trail of repeats grows.
-
Mix This control lets you blend between the dry signal (all the way left) and the delayed signal (all the way right).
-
Ping-Pong Mode This menu lets you enable and configure the stereo Ping-Pong delay mode. You can choose from the fol-
lowing modes:
-
Off The delay works as normal, without ping-pong functions.
-
Panned Using a multi-tap delay structure, this mode pans each delay repeat to the right or left, in sequence.
-
Dotted and Double These modes work similarly to Panned mode, but employ staggered spacing of the delay taps to
produce a dotted-note or syncopated straight rhythm in the delay repeats.
-
Reverb Enable this option to route the output of the Delay effect to the Reverb effect, enabling further diffusion and abstraction
of the delay signal.
Reverb
This effect places the synth signal within a synthesized reverberant physical space, ranging from short reverbs that emulate smaller
rooms, to long reverbs that evoke the sounds of large spaces, such as halls and cathedrals. Reverb offers the following controls:
-
Pre-Delay (Pre) This parameter lets you specify an amount of delay applied to the reverb-processed signal, in a range between
zero and 500 ms. This emulates the delay inherent in large spaces between the impact of a sound and its audible reverberation.
Lower settings are best suited to shorter reverb times, and longer settings with longer reverb times, but let your own taste be the
judge.
-
Damping (Damp) This control lets you set an amount of high-frequency attenuation to apply to the reverb signal. Spaces with
soft surfaces tend to lose treble quickly as the sound reverberates, resulting in a short bright reverb followed by a progressively
darker tail. Spaces with harder surfaces retain high-end more efficiently over time. Set Damp to its lower range to emulate hard
surfaces, and to the higher ranges to enable further damping, to emulate softer surfaces.
-
Size This control lets you set the length of reverberation from the moment a sound starts, in a range between 100 ms and 10
seconds. The larger the size, the longer the tail of the reverb, and the larger the emulated space sounds.
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the reverb signal.
-
Mix This control lets you blend between the dry signal (all the way left) and the reverb signal (all the way right).
SampleOne XT

FX B
Gater
This is a rhythmic gating effect, able to create a series of syncopated breaks in the synth signal. A variety of presets are provided, each
with a different rhythmic gating pattern. However, the fun really begins when you create your own. Gater offers the following controls:
-
Beats This control lets you set the length of the gating cycle, in rhythmic values (such as 1 bar or 1/2-note) relative to Song
tempo. For example, at a setting of 1 bar, the 16 steps in the cycle repeat every bar, effectively representing 16th-notes. At a
1/2-note setting, the 16 steps repeat each half-bar, representing 32nd-note values.
-
Beat Steps This grid lets you specify which steps in the cycle let signal pass through, and which gate the signal to silence. Click
on a step to enable or disable gating for that step.
-
Stereo Engaging this option creates a separate beat grid for each side of the stereo field. When engaged, you'll see two rows of
beat steps, the top row specifying gate steps for the left channel, and the bottom row gating the right channel.
-
Depth This control lets you blend between the gated and dry signals, allowing for rhythmic gating effects while retaining the con-
tinuity of the synth sound.
EQ
This is a graphic equalizer effect, perfect for quick tonal shaping. Set the EQ bands to emphasize or attenuate bands of frequencies to
suit your needs. When a band is in the center of its range, it neither adds nor subtracts. When moved above the center, it emphasizes the
chosen frequency. Moved below the center, it attenuates that frequency.
Choose between Lead mode, with frequencies chosen to suit aggressive, up-front sounds, or Bass mode, with wider-ranging fre-
quencies that work better for basses and mellower chordal parts.
Distortion
This is a variable distortion effect, which adds grit and character to your sounds. Choose from a variety of distortion types, from fizzy tran-
sistor fuzzes to thick, warm tube overdrives. Set the amount of distortion with the Drive knob.
Pan
This is an auto-pan effect, which pans the synth signal left and right over time. Pan offers the following controls:
-
Speed This control lets you set the speed at which the signal is panned left and right.
-
Sync Enable this option to set pan speed to a rhythmic value (such as 1/4-note or 16th-note) relative to Song tempo. Disable
this option to set pan speed along a continuous range.
-
Depth This control lets you set the degree to which the signal is panned. Lower settings give a subtly panned effect, while higher
settings pan the signal more radically, all the way to fully left and right in each cycle.
Virtual Keyboard
SampleOne XT

The virtual keyboard lets you easily click to play notes or manipulate the Pitch and Mod wheels, while auditioning or editing patches when
you're away from a MIDI keyboard. The keyboard display also shows you which notes are currently being played, as well as the root note
and pitch mapping span of the currently selected sample. You can show or hide the virtual keyboard at any time by pressing the [Keys]
button.
Note that for a more playable keyboard experience when away from your MIDI controller, you can also use Studio One's QWERTY Key-
board Device to play notes using your computer's keyboard.
Next to the virtual keyboard is the Bend parameter, which lets you set the pitch bend range of the Pitch wheel, in semitones.
Working with .multisample and .soundx Files
Given that it's so easy to create new sample libraries in SampleOne XT, you may find that you want to exchange them with other people,
or use them in different instruments, such as Presence XT. To export the current set of samples as a .multisample file, click the menu but-
ton and choose Export Multisample File... To export the current patch as a .soundx file for other SampleOne XT users to try, click the
menu button and choose Export Preset... To import a multisample or soundx preset file into SampleOne XT, simply drag-and-drop it
onto the plug-in window.
Export to Impact XT
Once you've created some samples you love, you can always import them to Impact XT using drag-and-drop. To do this, click and drag
your chosen sample from the sample list in SampleOne XT, and hover your cursor over an Impact XT tab at the top of the Instruments
window. Impact XT is then shown, and you can drop your sample onto any pad. You can also select multiple samples in SampleOne XT,
then click and drag the group into Impact XT as described above.
By default, when multiple samples are dropped onto a pad, they are all assigned to that pad and are played interchangably, according to
the current Layer Mode. To distribute multiple samples across multiple pads, press and hold [Shift] before dropping them. The first
sample is assigned to the selected pad, and each subsequent sample is assigned to subsequent pads in ascending note order.
Color Themes
Looking for a little personalization? Try clicking the PreSonus logo at the top right corner of the SampleOne XT window for a selection of
new color themes.
SampleOne XT

## Presence XT

Presence XT is a virtual sample-player instrument that enables you to play an endless variety of sounds. Presence XT uses a generic
multisample format (also supported by Bitwig Studio) packaged into Sound Sets, and can also load and play presets in EXS, Giga, Kon-
takt (version 4 and below), and SoundFont formats. You can shape your sounds with the provided filter, LFOs, envelopes, mod matrix,
and effects. Make sure to download the sound sets that came bundled with your edition of Studio One. The bundled Sound Sets
include a variety of high-quality instruments, and Presence XT requires the sound set download for sounds and presets to work as inten-
ded within the virtual instrument.
While Presence XT is, by default, limited to playing sounds from existing libraries, by purchasing the Presence XT Editor Option, you can
upgrade it to a full-featured sampler. With this option installed, you can create your own sample-based instruments, with powerful lay-
ering and scripting features. For more information, see Presence XT Editor.
Presence XT employs a high-performance disk-streaming sample playback system, enabling the use of presets that use very long
samples. Up to 128 sample voices can play simultaneously. One voice is often equivalent to one note. However, some sounds have ele-
ments (such as layers and articulations) that can consume more than one voice per note played.
The central preset display shows the number of sample voices being used at any moment, as well as the name and size of the loaded
preset. The Voice Limit parameter lets you set the level of polyphony you want (1-128, 64 by default).

## Presence XT

Loading and Playing Sounds
You can locate and load presets from Studio One Sound Sets in the following
ways:
-
Click the Preset menu in Presence XT, browse to your preset of
choice, and click the preset to load.
-
With the Presence XT window open, choose a Presence XT preset in
the Instruments section of the Browser, and double-click the preset to
load.
-
Drag a preset from the Sounds section of the Browser onto the Pres-
ence XT plug-in window or the Track on which Presence XT resides.
-
Create a new Instrument Track with Presence XT and your choice of
preset already loaded, by dragging the preset between two Tracks (or
next to the top or bottom Track) in the Arrange view.
Once loaded, the preset is immediately playable with your MIDI controller, or
by clicking the virtual keyboard at the bottom of the plug-in window.

## Presence XT

Working with Presence Content
Presence XT takes the place of the Presence sample playback instrument, featured in previous versions of Studio One. Songs that use
the Presence instrument open as expected in Studio One 6.6, with Presence XT replacing any instances of Presence.
However, Presence XT features an improved Reverb effect algorithm, so songs created using Presence (and its built-in reverb) show a
difference in sound when played with Presence XT in place. This difference can be minimized by adjusting the settings of the new
Reverb effect.
You may still notice some slight sound differences between presets played through Presence and the same presets played through Pres-
ence XT. You can always open affected songs in a previous version of Studio One and transform the affected tracks to audio. Songs
saved in this state sound exactly the same when opened in Studio One 6.6.
Find More Sounds in the PreSonus Shop
Sample libraries created especially for Presence XT are available in the PreSonus Shop. For more info on purchasing content from the
Shop, see PreSonus Shop.
Using 3rd-Party Sample Formats
Sounds in EXS, Giga, Kontakt (version 4 and below), and SoundFont formats can be loaded directly, with no conversion required. You
can load these presets by dragging from the Windows Explorer or macOS Finder onto the plug-in window, or onto a Track with Presence
XT loaded. You can create a new Instrument Track with Presence XT and your choice of preset already loaded, by dragging the preset
between two Tracks (or next to the top or bottom Track) in Arrange view.
You can also locate and access 3rd-party presets using the Files tab in the Browser. If you have an established directory for sampler con-
tent, you can create a new Browser tab pointing to that directory, for quick access. For more on setting up new tabs in the Browser, see
Make Finding Your Favorite Files Easy.
We recommend storing your sampler presets and any needed sample collections together, in the same directory. If needed samples can-
not be found when loading a preset, you are given the chance to locate them in your file system.
Relative Parameter Control
Multiple samples are used to create sounds in a single instrument, and presets can potentially comprise multiple instruments. Each
sample in any given preset can have different absolute settings. Expressive control of such complex presets is achieved by the use of rel-
ative controls, that can modify all samples simultaneously. Changes are made relative to the absolute settings within the loaded preset.
Script Controls
Some sounds offer additional controls that interact with a control script built into the sound. When Script Controls are available in a
loaded sound, they appear in the central display. You can tweak and automate these special controls just as you would the built-in con-
trols in Presence XT.
In some cases, Script Controls can replace the functionality of one or more of the standard controls (such as envelope settings). When
working with sounds such as these, use the provided Script Controls to affect those parameters.
Articulation Key Switches
Some sound libraries are built with a special area of the keyboard that acts as a set of switches between different versions of the sound.
For example, a guitar sound might offer open notes, muted notes, slides, and so on. These different articulations are instantly available
as you play or program a part, by pressing a key (or programming a MIDI note) in that special range.

## Presence XT

When Articulation Key Switches are available in a sound, the name of the currently selected articulation is shown at the upper-right
corner of the central display of Presence XT. Click this name to toggle a list of available articulation switches and their places on the key-
board. These keys are also marked with red bars on the virtual keyboard.
When you play one of these keys, the new articulation is shown in the central display, and the character of the sound changes according
to the way the sound was designed.
Controls Overview
The main control panel lets you control the Filter, LFOs, Envelope Generators, and sample playback parameters. These are the primary
controls you'll use to sculpt your sound. To the right of these controls are the Global parameters: Volume, Velocity, and key mode (Poly,
Mono & Glide).
Along the bottom of the window, you'll see the Mod/FX section (which gives you access to the modulation matrix and effects) and the vir-
tual keyboard. You can hide or show each of these elements by pressing the [MOD/FX] and Keyboard Icon buttons.
LFO 1 and LFO 2
LFO stands for Low Frequency Oscillator, and Presence XT has two of them. LFOs create slow-moving regular cycles of control signal
that are useful for modulating other parameters over time. One common example is the way many keyboard patches respond when you
move the Mod Wheel up from zero; the pitch of the oscillators wavers up and down in an expressive manner, much like the sound of
vocal vibrato. This is simply an LFO modulating oscillator pitch to a degree set by the position of the mod wheel.
LFO 1 and 2 have identical controls, so the following explanations apply to both:
-
Bypass Click the [LFO 1] or [LFO 2] button to turn the selected LFO on or off.
-
LFO Type Choose between Sine, Triangle, Sawtooth, Square, and Random shapes for the oscillation of the LFO.
-
Rate Sets the rate at which the LFO oscillates, from inaudibly low (0.01 Hz) for long, sweeping changes, all the way to higher
ranges (up to 8 kHz) useful for FM and AM techniques. When the LFO's [Sync] button is engaged, Rate can be set in terms of
rhythmic values relative to Song tempo, such 1/8th-note and 1/4-note.
-
Sync Engage this option to enable setting LFO Rate to a rhythmic value (such as 1/8th-note or 1/4-note) relative to Song tempo.
Disengage to set Rate by Hz.
-
Key Engage this option to bind LFO speed to incoming note pitch. Higher notes result in higher LFO speeds, while lower notes
result in lower LFO speeds.
-
Free Engage this option to let the LFO run continuously, resulting in a differing LFO start point for each note played. Disengage
to restart the LFO waveform at the start of each note.
-
Delay This control lets you specify an amount of time (in milliseconds) for the LFO to wait before becoming active after a note is
played. This lets you do things like adding a bit of expression to held notes, or creating layers of modulation that start at different
points in each note by setting distinct Delay values for each LFO.
Sample Playback Parameters

## Presence XT

This set of controls lets you manipulate the way that Presence XT plays the samples in the currently loaded preset.
-
Sample Start Mod Lets you specify an amount of negative or positive velocity-controlled offset, applied to the point in the
sample at which playback begins. At settings above and below the default of 0, lower-velocity notes trigger a smaller amount of
sample offset, and higher-velocity notes trigger a larger amount of offset.
-
Pitch Fine Tune Lets you tune sample pitch in a range of -100 to +100 cents (equaling one semitone up or down).
-
Sample Shift Lets you manipulate sample playback speed with no change in pitch. While pitch is not affected, the range of
Sample Shift is -36 to +36 semitones, which references the amount of transposition that would normally be needed to shift a
sample's speed the specified amount. When playing one-shot (non-looping) samples, this control varies the length of the
sample. When playing looped samples, this control enables useful textural and harmonic changes.
-
Transpose Lets you transpose incoming note pitch in a range of -12 to +12 semitones.
Filter
Presence XT offers a versatile multi-mode Filter, which lets you shape and enhance your sounds. The filter is often one of the most
important defining elements to the sound of an analog synthesizer, and likewise, this filter's unique characteristics have much to do with
the sound of Presence XT. The Filter offers the following controls:
-
Bypass Click the [Filter] button to turn the filter on or off.
-
Filter Mode Choose from the following filter modes, each with its own sound-shaping characteristics.
-
LP 24 dB Ladder This mode emulates a classic 24-dB-per-octave low-pass filter based on a transistor-ladder con-
figuration, as found in many classic synthesizers. This type of filter allows frequencies below the chosen Cutoff fre-
quency to pass through, which cutting frequencies above Cutoff at a rate of 24 decibels per octave—a fairly aggressive
slope.
-
LP 24 dB Zero This is a 24-dB-per-octave low-pass filter, based on a zero-delay-feedback architecture that closely
models the tone and modulation behavior of analog filters.
-
LP 12 dB Ladder This is a low-pass filter with a 12-dB-per-octave curve, which cuts frequencies less aggressively than
the 24 dB filters.
-
BP 12 dB Ladder This is a high-pass and low-pass filter in series, known collectively as a band-pass filter. It allows a
selected band of frequencies to pass through, then cuts frequencies above and below that band at a rate of 12 decibels
per octave.
-
HP 12 dB Ladder This is a high-pass filter with a 12-dB-per-octave slope. This lets frequencies above the chosen
Cutoff frequency pass through, while cutting frequencies below Cutoff at a rate of 12 decibels per octave.
-
LP 12 State, BP 12 State, HP 12 State, Eco Filter These are a set of simple, clean digital filter models, in low-pass,
band-pass, high-pass, and eco (low-CPU low-pass) modes. You can access these filter types in the drop-down menu at
the end of the row of Filter Mode switches.
-
Cutoff This lets you set the corner frequency of the filter—the point in the slope of the filter at which the filter cuts incoming audio
by 3 dB. In the case of the Band-Pass filter, this sets the center frequency of the passed frequency band.
-
Soft This control lets you switch between two differing analog-modeled processing circuits within the filter. Engage Soft for a
mellower, darker tone. Disengage it for a brighter, more aggressive sound.
-
Drive This lets you specify an amount of filter overdrive, to add fullness and saturation artifacts to your sound.
-
Punch This control lets you add a range of percussive attack to the start of each note. At the lowest setting, dynamics are
unchanged. At higher settings, the sound becomes more aggressive and more readily pops through the mix.
-
Resonance (Res)This lets you set the amount of resonance in the filter, which is an emphasis centered on the chosen cutoff fre-
quency. At lower settings, the filter cuts frequencies smoothly. As you increase Res, the emphasis at the cutoff frequency

## Presence XT

becomes more pronounced, able to mimic resonances such as those in voices or acoustic instruments, as well as many classic
synthesis effects. At the highest settings, the filter can self-oscillate, emitting a pitched tone at the current cutoff frequency. This
filter oscillation can be treated somewhat like an extra oscillator, especially in conjunction with the Key parameter.
-
Velocity (Vel) This control sets the relationship between incoming note Velocity and filter Cutoff. When set at the center, velo-
city does not affect cutoff. When moved to the right, cutoff rises as note velocity increases. When moved to the left, cutoff lowers
as note velocity increases.
-
Key This control sets the relationship between incoming note Pitch and filter Cutoff. In physical instruments, higher notes tend to
produce higher harmonics, brightening slightly as you go up the scale. On a synthesized instrument, if the filter stays static, set-
ting the proper tone in the lower note ranges may cause inappropriate dullness in the higher notes. So, with the Key parameter,
we can compensate for this, and create a more natural-sounding range of timbres up and down the keyboard.
-
When Key is set all the way to the left, the filter is unaffected by note pitch. In the middle, cutoff follows note pitch subtly,
allowing high notes to shine. When set all the way right, filter cutoff follows note pitch closely in a relative fashion, mov-
ing upward and downward in semitone values as notes are received. This lets you use the filter as an additional pitched
oscillator or resonator when filter Res is set high.
Envelopes
Envelope generators are a vital part of sound synthesis, giving us the ability to shape the amplitude and timbre of our sounds within the
time-scale of each note. Presence XT has two envelope generators, labeled Amp Env (so named because it is hard-wired to amplitude),
and Env 2 (which is often routed to filter cutoff, for timbral shaping).
Both Env modules are triggered when a note is played. Each Env then outputs a control signal that follows the shape set by the following
controls:
-
Attack (A) This control lets you set the time required for the envelope to go from zero (silence) to full amplitude, in a range from
0 ms to 20 seconds.
-
Decay (D) This control lets you set the time required to drop from full amplitude to the sustain level, in a range from 0 ms to 20
seconds.
-
Sustain (S) This control lets you set the signal level that is maintained from the end of the decay period, until the key is
released, in a range from -∞dB (silence) to 0.0 dB (full amplitude).
-
Release (R) This control lets you set the time required to fall back to silence after the key is released, in a range from 0 ms to 30
seconds.

## Presence XT

-
Delay (△- Env 2 only) This control lets you specify a length of time (in ms) for the Env to pause before starting its attack phase
after a note is played. This can assist in creating evolving sounds, where cycles of modulation occur at differing times over the
length of a note.
Envelope Graphical Display
Each envelope has a corresponding graphical display that represents the shape created by the settings of its parameters. There are
handles on the corners and slopes of each envelope that you can click and drag, letting you shape the ADSR envelope and the curve
between its points visually. If you wish to lengthen any phase of the envelope beyond the time limits of the current display, simply drag
the point toward the right of the graph, and the time scale adjusts to properly display the new setting.
Global Settings
The following Global parameters let you configure Presence XT's overall behavior and capabilities, to meet your needs.
-
Volume This control lets you set the total output volume, in a range from -∞dB (silence) to +10.0 dB (ten decibels above unity
gain).
-
Velocity This control lets you set the degree to which Presence XT's volume is affected by note velocity, from zero (no velocity
sensitivity) to 1.0 (full velocity sensitivity).
-
Poly, Mono, and Glide Enable Poly mode to allow polyphonic playing (more than one note at a time). Enable Mono mode to
play just one note at a time. When in Mono mode, you can enable Glide to cause the pitch to sweep smoothly from that of the cur-
rently held note to that of the next note, when played legato (one note played while the previous note is held). The Glide knob
lets you set the rate of pitch change over time, from 1 ms to 1 second.
Effects
Presence XT offers seven built-in effects processors to add dimension to your sounds. They are arranged in two banks: FX A (Mod-
ulation, Delay, and Reverb) and FX B (Gater, EQ, Distortion, and Pan). You can enable or disable each effect by clicking its name. You
can show or hide the Mod/FX section of the plug-in window by clicking the [Mod/FX] button.

## Presence XT

Modulation
This processor creates time-based modulation effects. Choose from the following modes by clicking the [Chorus], [Flanger], or [Phaser]
button:
-
Chorus This processor creates effects similar to that of multiple identical instruments playing the same part simultaneously. The
synth signal is fed through a short, modulated delay, which is then mixed with the dry signal. Chorus offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay. Higher settings create full-bodied chorusing effects,
while lower settings create more pronounced harmonics, akin to the effects of a Flanger.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler chor-
using effects, while higher settings produce more pronounced changes in timbre over time.
-
Depth This control lets you blend between the dry signal (all the way left) and the chorused signal (all the way right).
-
Flanger This processor creates resonant, hollow-sounding sweeping effects. The synth signal is fed through a short, modulated
delay, which is mixed with the dry signal. While similar to the workings of a Chorus effect, Flangers get their signature sound by
employing smaller delay times than those used in chorusing, combined with a feedback system that can add extra resonance to
the sweep. Flanger offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay (in ms), which changes the pitch of the resultant res-
onance. Higher settings create lower-pitched resonance, while lower settings create resonances at a higher pitch.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler flanging
effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Flanger. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Flanger modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the flanged signal (all the way right).
-
Phaser This processor creates dreamy, otherworldly sweeping effects. The synth signal is fed through a series of all-pass filters
that alter its phase. When mixed with the dry signal, this creates a series of peaks and valleys in the frequency response that
changes depending on the degree of phase shift applied. Phaser offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Shift This control lets you specify the amount of phase shift to apply. Lower settings focus the phasing effect in the
lower frequencies, while higher settings focus the effect in higher frequencies.
-
Speed This control lets you set the speed of modulation applied to the phase shift amount. Lower settings create slow,
sweeping effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the phase shift amount is modulated. Lower settings produce
subtler effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Phaser. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Phaser modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the phase-shifted signal (all the way
right).

## Presence XT

Delay
This processor creates an echo effect, either as a single delayed repeat of the input signal, or a trailing series of echoes. The Delay effect
offers the following controls:
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the delayed signal.
-
Delay Time This control lets you specify the length of the delay effect, in rhythmic values (such as 1/8th-note or 16th-note) rel-
ative to the tempo of the Song.
-
Feedback (FB) This control lets you set the amount of effected signal that is fed back into the Delay effect. At zero, there is just
one repeat. As you increase the value, the trail of repeats grows.
-
Mix This control lets you blend between the dry signal (all the way left) and the delayed signal (all the way right).
-
Ping-Pong Mode This menu lets you enable and configure the stereo Ping-Pong delay mode. You can choose from the fol-
lowing modes:
-
Off The delay works as normal, without ping-pong functions.
-
Panned Using a multi-tap delay structure, this mode pans each delay repeat to the right or left, in sequence.
-
Dotted and Double These modes work similarly to Panned mode, but employ staggered spacing of the delay taps to
produce a dotted-note or syncopated straight rhythm in the delay repeats.
-
Reverb Enable this option to route the output of the Delay effect to the Reverb effect, enabling further diffusion and abstraction
of the delay signal.
Reverb
This effect places the synth signal within a synthesized reverberant physical space, ranging from short reverbs that emulate smaller
rooms, to long reverbs that evoke the sounds of large spaces, such as halls and cathedrals. Reverb offers the following controls:
-
Pre-Delay (Pre) This parameter lets you specify an amount of delay applied to the reverb-processed signal, in a range between
zero and 500 ms. This emulates the delay inherent in large spaces between the impact of a sound and its audible reverberation.
Lower settings are best suited to shorter reverb times, and longer settings with longer reverb times, but let your own taste be the
judge.
-
Damping (Damp) This control lets you set an amount of high-frequency attenuation to apply to the reverb signal. Spaces with
soft surfaces tend to lose treble quickly as the sound reverberates, resulting in a short bright reverb followed by a progressively
darker tail. Spaces with harder surfaces retain high-end more efficiently over time. Set Damp to its lower range to emulate hard
surfaces, and to the higher ranges to enable further damping, to emulate softer surfaces.
-
Size This control lets you set the length of reverberation from the moment a sound starts, in a range between 100 ms and 10
seconds. The larger the size, the longer the tail of the reverb, and the larger the emulated space sounds.
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the reverb signal.
-
Mix This control lets you blend between the dry signal (all the way left) and the reverb signal (all the way right).
Gater

## Presence XT

This is a rhythmic gating effect, able to create a series of syncopated breaks in the synth signal. A variety of presets are provided, each
with a different rhythmic gating pattern. However, the fun really begins when you create your own. Gater offers the following controls:
-
Beats This control lets you set the length of the gating cycle, in rhythmic values (such as 1 bar or 1/2-note) relative to Song
tempo. For example, at a setting of 1 bar, the 16 steps in the cycle repeat every bar, effectively representing 16th-notes. At a
1/2-note setting, the 16 steps repeat each half-bar, representing 32nd-note values.
-
Beat Steps This grid lets you specify which steps in the cycle let signal pass through, and which gate the signal to silence. Click
on a step to enable or disable gating for that step.
-
Stereo Engaging this option creates a separate beat grid for each side of the stereo field. When engaged, you'll see two rows of
beat steps, the top row specifying gate steps for the left channel, and the bottom row gating the right channel.
-
Depth This control lets you blend between the gated and dry signals, allowing for rhythmic gating effects while retaining the con-
tinuity of the synth sound.
EQ
This is a graphic equalizer effect, perfect for quick tonal shaping. Set the EQ bands to emphasize or attenuate bands of frequencies to
suit your needs. When a band is in the center of its range, it neither adds nor subtracts. When moved above the center, it emphasizes the
chosen frequency. Moved below the center, it attenuates that frequency.
Choose between Lead mode, with frequencies chosen to suit aggressive, up-front sounds, or Bass mode, with wider-ranging fre-
quencies that work better for basses and mellower chordal parts.
Distortion
This is a variable distortion effect, which adds grit and character to your sounds. Choose from a variety of distortion types, from fizzy tran-
sistor fuzzes to thick, warm tube overdrives. Set the amount of distortion with the Drive knob.
Pan
This is an auto-pan effect, which pans the synth signal left and right over time. Pan offers the following controls:
-
Speed This control lets you set the speed at which the signal is panned left and right.
-
Sync Enable this option to set pan speed to a rhythmic value (such as 1/4-note or 16th-note) relative to Song tempo. Disable
this option to set pan speed along a continuous range.
-
Depth This control lets you set the degree to which the signal is panned. Lower settings give a subtly panned effect, while higher
settings pan the signal more radically, all the way to fully left and right in each cycle.
Modulation Matrix

## Presence XT

Presence XT provides 16 configurable modulation routings, in two banks of eight (Mod A and Mod B). Modulation signals can be routed
from a selection of incoming MIDI controller signals including MPE data (such as Pitch Bend, Mod Wheel, Aftertouch, Poly Pressure,
Note Timbre, and Pitch Control), modulation generators (such as the LFOs and envelopes), or the pitch or velocity of played notes.
These modulation signals can be used to vary most of the parameters throughout Presence XT, including modulation sources them-
selves (such as LFO 2 modulating the rate of LFO 1, or the Decay of Env 2).
Each modulation slot has a bypass button at the top, which lets you enable or disable the flow of modulation signal. Below that are the
input selector and modifier selector. If you assign a modulation source to the input selector only, that signal is routed directly to the
chosen destination. In some cases, you’ll want to govern the flow of one mod source before it reaches its destination, using the signal
from another mod source. For example, you may want to control the output level of LFO 1 (routed to a parameter such as oscillator pitch)
with the Mod Wheel. In this case, you'd choose Mod Wheel with the input selector, and LFO 1 with the modifier selector below.
Below that is a slider that controls the amplitude and polarity of the modulation signal. Set at its center, no modulation occurs. Move the
handle right of center to send an increasing amount of the modulation signal, at its normal (positive) polarity, to the chosen destination.
Move it left of center to send the signal to its destination with a negative value.
If the parameter you wish to modulate is set to a high value, you may want to send a negative modulation signal to it, driving the setting
downward and causing more audible effects. Positive-going modulation signals are more efficient when modulating parameters set to
low values.
A selector at the bottom of each modulation slot lets you choose the destination of the chosen modulation signals.
Virtual Keyboard
The virtual keyboard lets you easily click to play notes or manipulate the Pitch and Mod wheels, while auditioning or editing patches when
you're away from a MIDI keyboard. The keyboard display also shows you which notes are currently being played.
Note that for a more playable keyboard experience when away from your MIDI controller, you can also use Studio One's QWERTY Key-
board Device to play notes using your computer's keyboard.
Next to the virtual keyboard is the Bend parameter, which lets you set the pitch bend range of the Pitch wheel, in semitones. The upper
value sets up-bend range, and the lower value sets down-bend range.
Presence XT Editor
By default, Presence XT is a sample player, which lets you play (and tweak) sounds from existing libraries. If you want to create your own
sample-based instruments, you can purchase and install the Presence XT Editor Add-on, available from the PreSonus Shop. This
option upgrades Presence XT to full sampler functionality, with powerful scripting and layering features.
This editing function can also be used to deeply change and further optimize programs from imported sound libraries (such as those in
EXS or Giga format), or Presence XT libraries created by other users. Commercial Presence XT libraries (such as those included with
Studio One or bought separately) are protected, and cannot be edited.
Purchasing the Presence XT Editor Add-on
To purchase this Add-on, head to the Studio One Add-ons section of the PreSonus Shop. Add the option to your cart, and complete the
purchase. You are now ready to install.
Installing from Within Studio One
To install this option from within Studio One, ensure that your Studio One machine is connected to the internet, then navigate to Studio
One/Studio One Installation... Click the box next to the option in your "My Purchased Items" list to select it, then click [Install] to complete
the installation.
Presence XT Editor

Installing from the Web
To install this option using our web site, download the installer from your my.presonus.com account (in the Add-ons section of the My
Products page). If you wish to install the option on a different computer than the one you used to download the file, move the installer file
to the desired computer. Then, double-click the installer file and follow the instructions as prompted to complete the installation.
Editor Overview
Once you've installed the Presence XT Editor Add-on, when you open a Presence XT window, you'll see a new button, marked "Editor."
Press this button to open the editing interface. To return to the normal view, click the [Player] button. You'll notice there are four main sec-
tions in the editing interface:
Program
This area shows you the saved name and disk size of the program you're editing. If you click the menu button next to the [Program] but-
ton, a pop-up menu appears. Choose from the following functions:
-
New Program Resets Presence XT to a default state, with a blank program loaded. If you've begun to create a program and
have not yet saved it, you'll receive a warning, telling you that your samples and parameter settings will be lost if you go through
with creating a new program.
-
Pack Program Lets you package your program, with all its samples and settings, into a single file, for easy storage and sharing.
Packed programs are created with a ".soundx" file extension.
-
Set Program Password Lets you set a password that Presence XT prompts for if a person attempts to edit this program. This
lets you keep a program from being edited, even when sharing it with others.
To the right of the program area, you'll see three buttons that control the editor display. They look like this:
Presence XT Editor

The first button shows or hides an information drawer at the top of the editor window. Here, you can edit the program's name, set its cat-
egory, and add a description and information about yourself, as author of the program. The information you enter here is shown in the
Player view when your program is loaded, so we recommend you always fill in these fields.
The second and third buttons arrange the Layers and Zones areas either side-by-side, or vertically stacked, according to your pref-
erence.
Finally, you'll see the [Script] button, which opens the scripting view, in which you can write scripts in JavaScript, for greater creative con-
trol and interface flexibility in your programs. For more information on working with JavaScript in Presence XT, see Scripting.
Layer
This area deals with Layers, which are entire sample sets, arranged in Zones (as discussed below) across the range of MIDI key and
velocity values. These layers can be combined to create fuller sounds and textures, or to set up one or more MIDI-switchable
variations for a given sound.
For example, a layer could be a single variation, such as "Pizzicato," in a string sound (made up of many layers), with multiple sample
zones spread across the keyboard, horizontally. Or, a layer could be a single drum instrument, such as a snare drum, containing multiple
velocity zones, stacked vertically on a single MIDI note. For more information on working with the layer functions, see Layers.
Zones
This area deals with Zones, which are areas in which a single sample is placed across the range of MIDI key and velocity values. These
sample zones are the pieces that make up a layer (as discussed above), letting you decide exactly how your samples are placed, played,
and processed.
For example, a high-quality piano sound may have a group of separate samples for every note on the piano, arranged to be played at
low, mid, or high velocity. In the Zones area, you can make decisions like this with your own samples, setting up the range of the key-
board and key velocity in which each sample plays, along with many other options. For more information on working with zones, see
Zones.
Parameters
This area gives you access to a wide variety of modulation, tonal, and behavioral options for each layer and the zones within them. The
parameters available in this area can pertain to the program as a whole, to the currently selected layer, or the currently selected zone.
Clicking the [Program], [Layer], or [Zones] button changes the focus of the Parameters area to address each of those categories, as
needed. You can also switch the mode of the parameters area between these three settings by clicking the [Parameters] button. You can
easily keep track of which mode you're in, because the Parameters area is color-coded: Program mode is blue, Layers is red, and Zones
is turquoise.
For more information, see Parameters.
Creating a New Program
To get started creating a new program, open an instance of Presence XT and click the [Editor] button to open the editing interface. A
blank preset is shown by default. It has a single layer, and no samples yet placed in zones. You can then begin dragging samples from
the Browser into the Zones area on the Presence XT window.
Looking at the Zones area, you can see the samples you add to your new program. By default, they are displayed in a list-style view,
showing the sample name and a variety of available parameters for each. If you click the [Grid] button, you'll see the samples displayed
along a grid that represents the full range of MIDI notes (horizontally) and velocity values (vertically). You can get back to the list view at
any time by clicking the [List] button.
The first sample you add defaults to playing on MIDI note C-1, the second defaults to C#-1, and so on, in ascending order. This can be
helpful when creating drum programs or heavily multisampled sounds, where each key may have a sample of its own. If you intend for a
sample to cover a larger span of keys, you can specify the desired span using the Key Low and Key High parameters for each sample (if
looking at zones in list view) or by dragging the edges of each sample to the beginning and end of the desired range (if looking at zones in
grid view).
Once you have the start to a new sound in place, you'll probably want to save the preset, to preserve your work. To do this, follow the
instructions shown in Creating and Managing Effects Presets.
Presence XT Editor

For more detailed information on the available functions and parameters to help you develop sounds, see the following sections: Layers,
Zones, and Parameters.
Layers
The Layers area of the Presence XT editor window is used to establish sound layering in your program. Layers are entire sound sets,
with samples placed in zones, and most of the necessary sample-by-sample decisions already made (such as key and velocity ranges,
processing details, and so on). You can add multiple layers to your program, to create hybrid sounds that play together, or provide MIDI-
selectable variations on a given sound, such as different bowing and plucking styles in a violin sound.
If you're just getting started creating a new program and you want to import samples and get them placed and configured, you'll be doing
most of that work in the Zones area of the Presence XT window. See Zones for more info to get you started.
Once you've added and configured your first set of samples in the Zones area, you've put together your first layer. If you look at the Layer
area in the Presence XT editor window, you'll see "Layer 1" listed, along with a set of editable parameters for that layer. For more info on
parameters available when editing layers, see Layer Parameters.
Managing Layers
To add a new layer, [Right]/[Ctrl]-click in the layers list or click the menu button next to the [Layers] button. Choose "Add Layer" from the
pop-up menu. A new layer is created and added to the layers list. This pop-up menu also offers the following options:
-
Remove Layer Removes the currently selected layer from the program. This also removes all samples placed in zones within
that layer.
-
Duplicate Layer Creates a duplicate of the currently selected layer, with all sample placements and parameters the same.
-
Merge Layers Combines the sample placements and related parameter settings for all selected layers, into one new layer.
-
Copy Page Parameters Copies the parameter settings shown on the current visible page for the currently selected layer, so
that they can be pasted to a different layer.
-
Paste Page Parameters Pastes the copied parameter settings to the currently selected layer.
If you select more than one layer at a time, you'll see all of the zones in all selected layers shown in the Zones area below, whether in list
or grid mode.
Layer Parameters
Each layer in your program has several pages of parameters available for editing, to help you shape the sound to your liking. By default,
the Main page of parameters is shown. When navigating through a layer's parameters, you can use the cursor keys on your keyboard to
move between them, as well as up or down from layer to layer. To edit a selected parameter, press [Enter] on your keyboard, then edit
the parameter, and press [Enter] again to lock in the new value.
The Main page contains the following parameters for each layer:
-
Title Lets you set the title for the layer.
-
Variation Lets you designate a layer as a key-switched variation of the sampled sound set (such as different styles of picking or
strumming on a guitar sound). If enabled, this layer becomes active when the MIDI note specified in the Trigger parameter
(described below) is played. When another variation is activated by its own MIDI key trigger, this layer stops playing. To des-
ignate one variation as the default, leave its Variation box unchecked, but still provide a note for the variation in the Trigger
column.
Presence XT Editor

-
Trigger Lets you specify the MIDI note that activates this layer, if it has been enabled as a Variation.
-
Note Off Trigger Enable this to trigger sounds within this layer only when a MIDI note ends. This is most useful for adding
release sounds to a sample program, such as piano hammers falling back into place after a note is played.
-
Gain Sets overall gain for an entire layer.
-
Pan Shifts overall pan placement for an entire layer, relative to the pan settings for each zone in that layer.
-
Zone Shift Moves all zones contained within a layer up or down the MIDI key range. When you do this, the range of playable
notes for each zone is moved up or down, and the base note for each zone shifts with it.
-
Tune Adjusts tuning of all samples contained in a layer.
If you click the menu button next to the button currently marked "Main," you can access the following sets of modulation and processing
parameters for each layer:
-
LFO 1 & 2 These settings mirror the LFO settings in the Player view of Presence XT, setting LFO parameters for all zones in a
layer.
-
Amp Env & Env 2 These settings mirror the Envelope settings in the Player view, setting envelope parameters for all zones in a
layer.
-
Filter These settings mirror the Filter settings in the Player view, setting filter parameters for all zones in a layer.
-
Other These settings mirror the Glide Time, Velocity Strength, and Velocity Curve controls in the Player view, setting con-
figuration options for all zones in a layer.
When you make changes to parameters in these pages, those changes are applied to all zones in that layer. If any affected zones have
differing settings for those parameters, their values are shifted in a relative fashion as you change the corresponding layer parameter.
Zones
The Zones area is where you do most of the work when sound designing with Presence XT. You drag samples here from the Browser for
inclusion in your program, and then you set the parameters for each sample zone. This lets you place the sample in the desired area of
the MIDI key and velocity range and make all the necessary decisions about sample behavior, modulation, and processing.
By default, the sample zones you create by adding samples are shown in a list. This shows the name and parameters for each sample.
You can search for a zone by name within the currently selected layer by typing into the Search bar above the Zones display.
Managing Zones
You add zones to a layer by selecting that layer and dragging samples into the Zones area. If you click the menu button next to the
[Zones] button, a pop-up menu appears with the following functions:
-
Apply Parameters from File Updates zone parameters to match those found in source file (such as root note, tuning, and loop
mode).
-
Remove Zone Removes the currently selected zone from the program.
Presence XT Editor

-
Copy Page Parameters Copies the parameter settings shown on the current visible page for the currently selected zone, so
that they can be pasted to a different layer.
-
Paste Page Parameters Pastes the copied parameter settings to the currently selected zone.
-
Refresh Selected Zone(s) Lets you re-import samples in the selected zones, if the original samples have been changed or
edited since you originally imported them.
-
Show in Finder/Explorer Opens an Explorer (Windows) or Finder (macOS) window, showing you the location of the currently
selected sample.
Zones Area Options
There are a set of buttons at the top of the Zones area that change how you see and interact with it.
-
List Shows the zones in the currently selected layer in a list view, along with pages of parameters for fine editing of each zone.
For info on the available parameters, see Zone Parameters.
-
Grid Shows the zones in the currently selected layer as regions in a grid that represents the span of MIDI notes (horizontally)
and MIDI velocity values (vertically). For more information on placing samples in grid mode, see Zones in Grid View.
-
Input Triggers Selection Enable this option to select zones by playing keys on a MIDI keyboard. When a key is played, all
zones that play within its note range are selected in the zones list.
-
Audition Focus Zone Enable this option to audition a sample whenever its zone is selected when looking at zones in grid
view.
-
Rel. Enable this option to enter relative editing mode. When this mode is off, if you select multiple zones and change a para-
meter value in one of the zones, that parameter is set to the chosen value in all selected zones. When this mode is enabled, if
more than one zone is selected, and you change a parameter in one zone, that parameter is changed in all selected zones, but
in a relative fashion, up or down from the current setting.
Zone Parameters
Looking at zones in list view, you see the list of samples in the currently selected layer, and several columns of parameters with values
for each zone. By default, the Main page of parameters is shown.
When navigating through the parameters for a zone, you can use the cursor keys on your keyboard to move between them, as well as up
and down, from zone to zone. To edit a selected parameter, press [Enter] on your keyboard, then edit the parameter, and press [Enter]
again to lock in the new value.
The following parameters are available in the Main parameter page:
-
Root Sets the root note for the current sample zone. Generally, it's best to set this to the actual note at which the sample plays,
ensuring that it plays at the proper pitch when triggered by MIDI notes.
-
Tune Fine-tunes the pitch of the sample, in cents.
-
Fix Lets you set a defined pitch at which the sample plays, regardless of what MIDI note triggers it. This can be helpful for per-
cussion kits or other non-pitched sample sets, where MIDI notes should not transpose a sample from its intended pitch.
-
Key Low & Key High Lets you set the low and high limits of the MIDI note range in which a sample zone should play.
-
Fade K-Low & Fade K-High Lets you specify the degree to which a zone fades down in volume as you play notes closer to the
top or bottom of its note range. This can be helpful when you want a smooth transition between two zones, each blending into
the other.
-
Velo Low & Velo High Lets you set the low and high limits of the MIDI velocity range in which a sample zone should play.
-
Fade V-Low & Fade V-HighLets you specify the degree to which a zone fades down in volume as you play notes closer to the
top or bottom of its velocity range.
-
Start & End Lets you specify the point within a sample that playback begins and ends.
-
Loop Mode Lets you choose the loop mode for a zone. Off disables looping, Sustain enables looping while a MIDI note is held,
and Release enables looping when a MIDI note is released, and the release portion of the sound is playing.
-
Loop Start & Loop End Lets you specify the start and end of the looping range of the sample (if applicable).
-
Loop XFade Lets you specify a length of fade to apply at the transition point between the end of a loop and its subsequent begin-
ning. This is often helpful when working with sustained sounds, which may need some smoothing.
-
Gain Lets you set gain for an individual zone.
-
Pan Lets you pan a zone across the stereo field.
Presence XT Editor

-
Round Robin By default, samples that are placed in overlapping zones play concurrently when a note in the proper range and
velocity is played. When you select Round Robin values for overlapping zones, they switch places with successive plays of a
note, according to the order of the numbers you specify. This can help to introduce natural-sounding variations from note to
note, especially in sounds made from samples of live instruments. Type "random" into this field for any set of overlapping key
zones, and those samples will play in random order as keys are struck, rather than numerical.
-
Play Lets you specify the play mode for a zone. Normal is the default mode, with zones playing and stopping according to the
length of incoming MIDI notes. One-Shot plays the whole specified range of a sample when a note is played. Toggle mode lets
long or looped samples play indefinitely, until the same note is played again.
-
Follow Tempo Allows samples with a rhythmic component to be timestretched as needed in order to follow the Song tempo.
This feature can be activated per zone and per sample, but it should be used sparingly because real-time timestretching is CPU-
intensive.
-
Path Shows the disk path in your file system where the sample for each zone is stored.
If you click the menu button next to the button currently marked "Main," you can access the following sets of modulation and processing
parameters for each zone:
-
LFO 1 & 2 These settings mirror the LFO settings in the Player view of Presence XT, setting LFO parameters for a zone.
-
Amp Env & Env 2 These settings mirror the Envelope settings in the Player view, setting envelope parameters for a zone.
-
Filter These settings mirror the Filter settings in the Player view, setting filter parameters for a zone.
-
Other These settings mirror the Glide Time, Velocity Strength, and Velocity Curve controls in the Player view, setting con-
figuration options for a zone.
Zones in Grid View
When you look at zones in grid view, you see them as labeled regions, filling a certain space within the range of MIDI notes (horizontally)
and velocity values (vertically). You can click and drag the top, bottom, and side edges of each zone to select the desired range in which
that zone will play. If you select multiple zones (by holding [Shift] or [Cmd]/[Ctrl] and clicking the desired zones), you can edit their ranges
or move them as a group.
If you click one of the "keys" in the keyboard display at the bottom of the grid, all zones triggered by that note are selected.
Presence XT Editor

Parameters
There are a great many available layer and zone parameters that you can access in the Layer and Zones areas of the editor window.
While editing in this "spreadsheet" style can be fast and precise, sometimes it can be helpful to use the type of knobs, buttons, and dis-
plays you're used to in the Player mode to help set and visualize these parameters. The Parameters area of the editor window lets you
set many of the available parameters in this way.
The Parameters area can show controls for the program as a whole (all layers and zones, together), or for one or more selected layers
(and the zones they contain), or for one or more selected zones. You can choose to display parameters for each by clicking the [Pro-
gram], [Layer], or [Zones] button, or cycle through them by clicking the [Parameters] button. You can easily keep track of which mode
you're in, because the Parameters area is color-coded: Program mode is blue, Layers is red, and Zones is turquoise.
Whatever mode is selected, parameters pertaining to modulation, filter, and mode-specific settings for that level in the program are
shown
Zone Waveform Display
When the Parameters area is in Zones mode, a [Wave] button appears. Clicking this brings up a waveform display for the sample in the
selected zone. Click and drag along the top edge to set the loop range for the displayed sample. Click and drag at the beginning or end of
the sample to move the play start or end point for the displayed sample.
While loop editing is possible in this fashion, it lacks the control and accuracy of a dedicated wave editor. As a result, clicks and pops may
appear when changing loop start and end points in this display. Adding a loop crossfade may solve this problem. This waveform display
is mainly meant for monitoring or reference. If in-depth loop editing is required, a dedicated wave editor software should be used.
If you want to replace the sample in a zone with a new sample, simply select the zone, and drag the new sample onto the waveform dis-
play. This retains any parameter settings you made for the previous sample.
Scripting
Presence XT offers powerful scripting functions, based on JavaScript. We chose this language because it is well supported and doc-
umented, and known by many. Scripting can be used to affect many functions in a program, most notably to assign macro knobs and but-
tons to your choice of parameters. Once script controls are assigned here, these controls appear in the central display in the Player mode
of the Presence XT window.
You may have seen these sorts of controls in some of the included Presence XT programs. Scripting is the way to make this happen.
To access scripting for a program, click the [Script] button in the editor view. This brings up a window in which you can enter your
JavaScript code, with some helpful structure added by default. To return to the editor view, press the [Edit] button. There are two buttons
at the top of the Script view, that look like this:
The first button shows or hides a drawer that displays the eight scriptable control knobs and buttons for the program. By default, it looks
blank. To enable a control, click the dot-shaped button in its lower left corner. To rename a control, click the pencil-shaped button that
appears when you hover the mouse cursor over the control. The functions that these controls relate to are set in the script that you cre-
ate.
The second button opens our documentation for the JavaScript structure you can use to script within Presence XT. It goes through the
various entry points, objects, and parameters that you can use to interface with Presence XT's engine.
Presence XT Editor

Between this information and the wide range of info resources available on the internet, you can soon dig into scripting for your pro-
grams, unlocking many useful functions.
You can click the [Reset] button to return the code window to its default (blank) state, or press [Apply] to apply your script and try out its
functions.

## Impact XT

Impact XT features a grid of pads into which samples are loaded and played back independently, as with many popular hardware drum-
sample players. Each pad has its own pitch, amplifier, and filter controls with accompanying envelopes. There are multiple stereo and
mono outputs for each pad, making sophisticated output busing simple.
Make sure to download the sound sets that came bundled with your edition of Studio One. Impact XT requires the sound set download
for sounds and presets to work as intended within the virtual instrument.
Interface Overview
Impact XT is arranged as a 4x4 grid of pads, with controls for each pad. There are eight selectable banks of 16 pads, labeled A through
H. Below each pad are Solo and Mute controls, as well as an Output Channel assignment. Click on any pad to select it and view its para-
meters, located on the right side of the interface. At the top of the window is the waveform display, which shows the currently selected

## Impact XT

sample along with controls for setting start and end points. To the right of the waveform display are the sample controls, which let you set
playback behavior for the samples on each pad.
Add and Play Samples
To add a sample to a pad, drag any audio clip from the Browser, or any Audio Event or selected range from the Arrange view, directly
onto the desired pad. If you drag in a selected range from the Arrange view, the range is bounced to a separate audio file and then added
to Impact XT. Dragging a sample to a pad that already contains a sample replaces the old sample with the new one, by default.
To mute a pad, click the Mute button beneath the pad. To solo a pad, so that you hear only its sound, click the Solo button beneath the
pad. Note that each pad has its own Pitch, Filter, and Amplifier controls.
To import a drum loop and automatically split its hits across multiple pads, hold [Shift] while dragging the loop onto Impact XT.
To copy a pad to another pad, hold [Cmd/Ctrl] and drag from one pad to another. Hold [Shift]+[Cmd/Ctrl] to swap two pads. If you would
like to copy a pad from one bank to another, use the copy and paste options from the right-click menu described below. Filter, Amp, and
other control settings are retained on a pad copy or swap.
A variety of useful actions can be taken by right-clicking a pad and choosing from the drop-down menu:
-
Replace Sample Replace the currently loaded sample with a new one.
-
Add Sample Add a sample to the pad.
-
Rename Pad Assign a new name to the pad.
-
Copy Pad Copy a pad to the clipboard.
-
Paste Pad Paste a copied pad from the clipboard.
-
Clear Pad Clear all samples from the pad.
-
Clear Bank Clear all samples from all pads in the current bank.
-
Play One Shot Change the Trigger mode for the pad to One Shot.
-
Play Loop Change the Trigger mode for the pad to Loop.
-
Play Normal Change the Trigger mode for the pad to Normal.
Multiple Velocity Layers
It is possible to add more than one sample to a pad, enabling you to trigger different samples based on velocity. For instance, you may
want to have three different samples for a single snare drum pad: one soft, one medium, and one loud. This way, when you play Impact
XT, the snare drum sounds much more realistic than if you use a single sample.
To do this, select multiple samples in the browser or in your computer's file system, and drag them to a pad.
Waveform Display
When you select a pad, its currently loaded sample is shown in this display. Here, you can set sample start and end by moving the tri-
angle-shaped markers. If more than one sample is loaded in the pad, you can switch between them by clicking the numbered buttons
above the waveform display. You can click-and-drag the demarcations between the sample selector buttons to set the velocity-switching
values (for use with the Velocity Layer Mode).
Add Sample (+) Choose this option to add an additional sample to this pad.

## Impact XT

Reverse Enable this option to reverse the current sample.
Normalize Enable this option to boost the amplitude of the current sample until its highest peak reaches a point just below full scale.
Load Next/Previous Sample in Folder These buttons let you quickly swap the current sample for its neighbor in the enclosing folder.
This allows for quick auditioning of a range of samples, to find just the right candidate.
Start and End Sets the sample start and end, in samples.
Sample Controls
These controls let you fine-tune sample behavior for each pad:
Color Choose a color with which to mark the pad.
1st and 2nd Note Assignment Choose two MIDI note values to trigger this pad.
Trigger Choose One Shot to play the loaded sample once when a pad is struck, no matter how long it is held. Chose Loop to con-
tinuously loop the sample as long as the pad is held. Choose Toggle to begin playing the sample when the pad is struck, and continue
playing it (even if looped) until the pad is struck a second time. Select Normal to begin playing the sample when the pad is struck and held
down, and continue playing it until the pad is released.
Layer Mode This parameter lets you choose how multiple samples are treated if loaded onto a single pad. Choose Velocity to switch
between the samples depending on pad velocity. Choose Round Robin to step through the samples one by one each time the pad is
struck. Choose Random to choose a sample at random each time the pad is struck. Choose Stack to play all loaded samples sim-
ultaneously.
Choke This parameter lets you specify the relationship between different pads, such as those set up to play closed and open hi-hat cym-
bals. Choose Self to allow a pad's playback to be stopped when the pad is played a second time (rather than continue to ring out).
Choose a Choke group (1-32) to tie the playback of this pad to all other pads also assigned to that choke group.
Quantize This parameter lets you limit your ability to play a pad to a preset rhythmic value. Choose from Off (no rhythmic limits), Bars
(once at the start of each bar), Beats (once per quarter note), 1/2-Beats (once per eighth-note), and 1/4-Beats (once per 16th note).
Follow Tempo Enable this option to automatically timestretch the current sample to fit the tempo of the Song. This is most effective
when using rhythmic loops, such as drum samples.
Offsets Introduce a playback offset of up to 2.5 seconds at the start or end of the loaded sample.
All Notes Off Press this button to end playback for all currently playing samples.
Edit Sample This button lets you specify individual settings for the currently selected sample, rather than changing those parameters for
all samples, as done by default. If after you've made custom alterations to one sample, you wish to reunify all samples under the same
settings, press Reset.

## Impact XT

Pitch Controls
You can modify the pitch for each pad’s sample using the Pitch controls.
-
Transpose Adjusts the transposition in semitones for the selected pad. Variable from -48 to +48.
-
Tune Adjusts the tuning, in cents, for the selected pad. Variable from -100 to 100 cents.
-
Pitch Envelope (One-Shot Trigger Mode Only)
-
Attack Adjusts the amount of time from when the pad is triggered to when the envelope value is reached. Variable from
0 s to 20 s.
-
Hold Adjusts the amount of time the envelope value is held after the attack period and before decay begins. Variable
from 0 s to 20 s.
-
Decay Adjusts the amount of time it takes after the hold period to return to the envelope value. Variable from 0.98 ms to
20 s.
-
Pitch Envelope (Loop and Normal Trigger Modes Only)
-
Attack Adjusts the amount of time it takes to reach the Env value from the original pitch of the sample once a sample
has been triggered. Variable from 0 to 20 s.
-
Decay Adjusts the amount of time it takes to reach the sustain level after reaching full volume. Variable from 0 to 20 s.
-
Sustain Adjusts the Sustain level. Variable from -∞dB to 0 dB. The sustain period continues until the sample trigger
stops.
-
Release Adjusts the amount of time it takes to reach the original pitch after sample trigger has stopped. Variable from 0
to 30 s.
-
Env Adjusts the detune range of the pitch envelope in cents. Variable from -4 to +4 octaves. (The default value is 0, meaning the
pitch envelope has no effect.)
-
Vel Adjusts the maximum detune value, in cents, that pitch is affected by velocity (the maximum detune value when triggered
note velocity equals 127). Variable from -4 to +4 octaves.
Filter Controls
Each pad features a variable filter to allow anything from subtle tonal shaping to heavily processed filter sweeps.
-
Cutoff Adjusts the cutoff frequency of the filter. Variable from 20 Hz to 20 kHz.
-
Res Adjusts the resonance of the filter. Variable from 0 to 100.

## Impact XT

-
Filter Env (One-Shot Trigger Mode Only)
-
Attack Adjusts the amount of time it takes for the filter cutoff frequency to move from the frequency value to the envel-
ope value once a sample has been triggered. Variable from 0 s to 20 s.
-
Hold Adjusts the amount of time the envelope value is held after the attack period and before decay begins. Variable
from 0 s to 20 s.
-
Decay Adjusts the amount of time it takes to return to the cutoff level after reaching the envelope value. Variable from 0
s to 20 s.
-
Filter Env (Loop and Normal Trigger Modes Only)
-
Attack Adjusts the amount of time it takes for the filter cutoff frequency to move from the frequency value to the envel-
ope value once a sample has been triggered. Variable from 0 to 20 seconds.
-
Decay Adjusts the amount of time it takes to reach the sustain level after reaching the envelope value. Variable from 0 s
to 20 s.
-
Sustain Adjusts the sustain level, which is the mix of the signal filtered at the envelope value with the signal filtered at
the frequency value. Variable from -∞to 0 dB. The sustain period continues until the sample trigger stops.
-
Release Adjusts the amount of time it takes the filter to reach the frequency value after the sample trigger has stopped.
Variable from 0 to 30 seconds.
-
Env Adjusts the range of the filter envelope in octaves, relative to the cutoff value. Variable from -8000 to +8000. (The default
value is 0, meaning the filter envelope has no effect.)
-
Vel Adjusts the maximum value in octaves affected by velocity . Variable from -100 % to + 100 % (the maximum value when
triggered note velocity equals 127).
-
Filter Type Selects the filter type. Choose from LP24 Ladder, LP24 Zero-Latency, LP12 Ladder, BP12 Ladder, HP12 Ladder,
LP12 State, BP12 State, HP12 State, and Eco Filter (lowest CPU use).
-
Drive This lets you specify an amount of filter overdrive, to add fullness and saturation artifacts to your sound.
-
Punch This control lets you add a range of percussive attack to the start of each note. At the lowest setting, dynamics are
unchanged. At higher settings, the sound becomes more aggressive and more readily pops through the mix.
-
Soft This control lets you switch between two differing analog-modeled processing circuits within the filter. Engage Soft for a
mellower, darker tone. Disengage it for a brighter, more aggressive sound.
Amplifier Controls
To adjust the amplitude for each pad, use the following parameters:
-
Gain Attenuates or boosts the amplitude, in dB, of the sample assigned to the selected pad. Variable from -144 to 20 dB.
-
Pan Adjusts the sample’s stereo pan for the selected pad. Variable from fully left to fully right.
-
Amp Env (One-Shot Trigger Mode Only)
-
Attack Adjusts the amount of time from when the pad is triggered to when maximum amplitude is reached. Variable
from 0 s (no attack, sample starts at maximum amplitude) to 20 s.
-
Hold Adjusts the amount of time the maximum velocity is held after the attack period, before decay begins. Variable
from 0 s to 20 s.
-
Decay Adjusts the amount of time it takes after the hold period to reach an amplitude of -∞from the maximum amp-
litude. Variable from 0 s to 20 s.
Amp Env (Loop and Normal Trigger Modes Only)
-
-
Attack Adjusts the amount of time it takes to reach full volume once a sample has been triggered. Variable from 0 to 20
seconds.

## Impact XT

-
Decay Adjusts the amount of time it takes to reach the sustain level after reaching full volume. Variable from 0 to 20
seconds.
-
Sustain Adjusts the sustain level. Variable from -∞to 0 dB. The sustain period continues until the sample trigger stops.
-
Release Adjusts the amount of time it takes to reach a level of -∞after the sample trigger has stopped. Variable from 0
to 30 seconds.
-
Vel Adjusts the maximum amplitude value, in dB, affected by velocity (the maximum amplitude value when triggered note velo-
city equals 127). Variable from 0 to 1.
Pad Focus
By default, the Pitch, Filter, and Amplifier controls act on the pad you most recently selected. To make editing easier when working on
multiple pads, you can enable Pad Focus by clicking the [Pad Focus] button at the top of the plug-in window. When this mode is enabled,
"focus" shifts to whatever pad you most recently played, letting you edit parameters for that pad.
Pad Focus and Control Linking
When in Pad Focus mode, if you use  Control Link to assign a hardware control to a Pitch, Filter, or Amplifier control in Impact XT, that
hardware control is linked in Focus mode. This means that the hardware control acts on the assigned parameter not only for the originally
assigned pad, but for whatever pad is most recently played. Using Control Linking under Pad Focus mode can make editing many pads a
faster and easier process.
Using Multiple Outputs
Impact XT provides 16 stereo outputs and 16 mono outputs for each pad. To change the output routing, click on the Output selection box
below the desired pads and choose the desired Output Channel for each pad. If the Output Channel does not already exist in the Con-
sole, it is added automatically. Alternatively, Output Channels can be chosen from the Inspector (F4).
If you are using a single instance of Impact across multiple Tracks, you can quickly assign its outputs by group-selecting the Impact chan-
nels and using the “Assign in Ascending Order” option from the Output routing menu of the Inspector.
This is very useful if you would like to program each of your drum sounds on a separate Track!
Working with .soundx Files
Given that it's so easy to create new sample kits in Impact XT, you may find that you want to exchange them with other people. To export
the current patch as a .soundx file for other Impact XT users to try, click the menu button and choose Export Sampler File... To import a
multisample or soundx preset file into Impact XT, simply drag-and-drop it onto the plug-in window.
File Sharing with SampleOne XT
Once you've created some samples you love in SampleOne XT, you can import them to Impact XT using drag-and-drop. To do this, click
and drag your chosen sample from the sample list in SampleOne XT, and hover your cursor over an Impact XT tab at the top of the

## Impact XT

Instruments window. Impact XT is then shown, and you can drop your sample onto any pad. You can also select multiple samples in
SampleOne XT, then click and drag the group into Impact XT as described above.
By default, when multiple samples are dropped onto a pad, they are all assigned to that pad and are played interchangably, according to
the current Layer Mode. To distribute multiple samples across multiple pads, press and hold [Shift] before dropping them. The first
sample is assigned to the selected pad, and each subsequent sample is assigned to subsequent pads in ascending note order.
Color Themes
Looking for a little personalization? Try clicking the PreSonus logo at the top right corner of the Impact XT window for a selection of new
color themes.
Mai Tai
Mai Tai is a polyphonic analog modeling synthesizer with a simple and straightforward interface. It excels at pad sounds, leads, rhythmic
chords, and many other synth duties. Mai Tai includes the following features:
-
32 synth voices with up to 8x oversampling
-
2 oscillators (sine, triangle, saw, square) with sub osc
-
Osc spread, sync, PWM & Random Phase
-
Noise generator
-
Character processor (for creative tonal effects)
-
Multi-Mode Filter
-
24 dB Ladder Filter
-
24 dB Zero Delay Feedback Filter
Mai Tai

-
12 dB Low-Pass, Band-Pass, and High-Pass Filters
-
2 LFOs (with sync, free run, and sample & hold)
-
3 ADSR Envelopes (two with pre-attack delay)
-
16-slot modulation matrix
-
Effects: Chorus, Flanger, Phaser, Delay, Reverb, Gater, EQ, Distortion, Pan
Make sure to download the sound sets that came bundled with your edition of Studio One. Mai Tai requires the sound set download for
sounds and presets to work as intended within the virtual instrument.
Interface
The central control panel contains controls for the Oscillators (Osc 1 and 2) and Noise generator, the Character processor and Filter, and
the LFOs and Envelope Generators. These are the primary controls you'll use to sculpt your sound. You can enable or disable each of
these modules by clicking the module's name. To the right of these controls are the Global parameters, which let you tune the overall
behavior and capabilities of the synth to your needs.
Along the bottom of the window, you'll see the Mod/FX section (which gives you access to Mai Tai's modulation matrix and effects) and
the virtual keyboard. You can hide or show each of these elements by pressing the [MOD/FX] and Keyboard Icon buttons.
Oscillators
Two oscillators are available, per voice, allowing for rich sounds with a wide tonal palette. Each Osc has its own set of parameters, which
differ in small but significant ways. In both Osc 1 and Osc 2, you'll see the following controls:
-
Bypass Click the [Osc 1] or [Osc 2] button to disable or enable each oscillator. This can be helpful when you want to create a
one-oscillator sound, or to temporarily disable an oscillator, so that you can focus on shaping the sound of the other.
-
Oscillator Waveform Choose between Sine, Triangle, Sawtooth, or Square.
-
PWM Only available when Square Wave is selected, this control lets you vary the pulse width of the square wave, changing the
distribution of harmonics, and thus, the tone of the oscillator.
-
Octave Lets you set the frequency range, in octaves, for the current oscillator. Range is set in number of feet (like a pipe in a
pipe organ), so the lower the number, the higher the pitch.
-
Random Phase (RP) Enable this option to set the oscillator to Random Phase mode, in which, when a note is played, the oscil-
lator starts its waveform at a random start point. This establishes a varying phase relationship between both oscillators
whenever a note is played (if both oscs are enabled), which creates pleasing shifts in tone over time. Disable this option to
Mai Tai

restart the waveform at the beginning when a note is played, which can be preferable when creating percussive sounds,
because it allows a uniformity of attack, from note to note.
-
Semi and Fine These controls let you set the center pitch of the oscillator, in semitones (Semi) and cents (Fine).
-
Spread (Osc 1 only) This control lets you layer in additional oscillators that follow Osc 1 pitch, with increasing amounts of detun-
ing as more oscillators are blended in. This creates a richer, fuller sound. With Spread all the way to the left, you hear a single
oscillator. As you turn Spread to the right, more oscillators are added, with greater detuning and stereo spread.
-
Sync (Osc 2 only) Enable this option to restart Osc 2's waveform each time Osc 1's waveform repeats. This is a classic analog
synthesis technique, creating rich harmonics and a sharp and strident sound. This is further expanded when pitch modulation is
applied to one or both of the oscillators with an LFO or envelope.
-
Sub Each of Mai Tai's oscillators has an attached sine wave sub-oscillator, which plays the same relative pitch as the main osc,
but an octave down. This control lets you blend in the signal from the sub-oscillator, which is a nice way to add additional thick-
ness and fullness to your sound, without having to dedicate the second main oscillator to the task.
-
Level This control lets you set the volume of each oscillator, to blend their tones to your liking.
-
Pan This control lets you position each oscillator separately in the stereo field, from left to right.
Noise Generator
The Noise section is a noise generator that can add texture and character to your sounds. The Noise module offers the following con-
trols:
-
Bypass Click the [Noise] button to turn Noise on or off.
-
Level Lets you set the volume level for the noise generator.
-
Pan This control lets you position each oscillator separately in the stereo field, from left to right.
-
Color Lets you set the timbre of the noise from dark to bright.
Character
The Character processor is one of the unique features of Mai Tai, offering a range of waveshaping effects that broaden its tonal range.
The Character module offers the following controls:
-
Bypass Click the [Character] button to turn the Character processor on or off.
-
Mode Menu Choose from a range of different spectral and formant processing modes.
-
Analog Color These character modes emulate a variety of characterful analog audio circuits. In the following modes,
the Sound knob blends between two different circuits, with distinct effects on sound.
-
Ardency
-
Bassmoderator
-
GrandClass
-
Formant These character modes effect the sound using formant-shifting techniques. In the following modes, the Sound
knob sweeps through the range of formants.
Mai Tai

-
CharacterSaw
-
Subvox
-
Talky
-
Voxil
-
Harmonics These character modes generate harmonics and spectral effects. In the following modes, the Sound knob
sweeps through the range of harmonics.
-
Ampog
-
Fuzzarmonics
-
Harmonia
-
Harmson
-
Spherical
-
Subharmonium
-
Sound Lets you vary the effect of the Character processor. Each Character mode responds to this control in a unique way, so
feel free to experiment.
-
Amount Lets you blend between the dry signal and the signal from the Character processor.
Filter
Mai Tai offers a versatile Filter, which lets you shape and enhance your sounds. The filter is often one of the most important defining ele-
ments to the sound of a subtractive synthesizer, and likewise, this filter's unique characteristics have much to do with the sound of Mai
Tai. The Filter offers the following controls:
-
Bypass Click the [Filter] button to turn the filter on or off.
-
Filter Mode Choose from the following filter modes, each with its own sound-shaping characteristics.
-
LP 24dB Ladder This mode emulates a classic 24dB-per-octave low-pass filter based on a transistor-ladder con-
figuration, as found in many classic synthesizers. This type of filter allows frequencies below the chosen Cutoff fre-
quency to pass through, which cutting frequencies above Cutoff at a rate of 24 decibels per octave—a fairly aggressive
slope.
-
LP 24dB Zero This is a 24dB-per-octave low-pass filter, based on a zero-delay-feedback architecture that closely mod-
els the tone and modulation behavior of analog filters.
-
LP 12dB Ladder This is a low-pass filter with a 12dB-per-octave curve, which cuts frequencies less aggressively than
the 24dB filters.
-
BP 12db Ladder This is a high-pass and low-pass filter in series, known collectively as a band-pass filter. It allows a
selected band of frequencies to pass through, then cuts frequencies above and below that band at a rate of 12 decibels
per octave.
-
HP 12dB Ladder This is a high-pass filter with a 12db-per-octave slope. This lets frequencies above the chosen Cutoff
frequency pass through, while cutting frequencies below Cutoff at a rate of 12 decibels per octave.
-
Cutoff This lets you set the corner frequency of the filter—the point in the slope of the filter at which the filter cuts incoming audio
by 3dB. In the case of the Band-Pass filter, this sets the center frequency of the passed frequency band.
-
Soft This control lets you switch between two differing analog-modeled processing circuits within the filter. Engage Soft for a
mellower, darker tone. Disengage it for a brighter, more aggressive sound.
-
Drive This lets you specify an amount of filter overdrive, to add fullness and saturation artifacts to your sound.
Mai Tai

-
Punch This control lets you add a range of percussive attack to the start of each note. At the lowest setting, dynamics are
unchanged. At higher settings, the sound becomes more aggressive and more readily pops through the mix.
-
Resonance (Res) This lets you set the amount of resonance in the filter, which is an emphasis centered on the chosen cutoff fre-
quency. At lower settings, the filter cuts frequencies smoothly. As you increase Res, the emphasis at the cutoff frequency
becomes more pronounced, able to mimic resonances such as those in voices or acoustic instruments, as well as many classic
synthesis effects. At the highest settings, the filter can self-oscillate, emitting a pitched tone at the current cutoff frequency. This
filter oscillation can be treated somewhat like an extra oscillator, especially in conjunction with the Key parameter.
-
Velocity (Vel) This control sets the relationship between incoming Voice Velocity and filter Cutoff. When set at the center, velo-
city does not effect cutoff. When moved to the right, cutoff rises as note velocity increases. When moved to the left, cutoff lowers
as note velocity increases.
-
Key This control sets the relationship between incoming Voice Pitch and filter Cutoff. In physical instruments, higher notes tend
to produce higher harmonics, brightening slightly as you go up the scale. On a synthesized instrument, if the filter stays static,
setting the proper tone in the lower note ranges may cause inappropriate dullness in the higher notes. So, with the Key para-
meter, we can compensate for this, and create a more natural-sounding range of timbres up and down the keyboard.
-
When Key is set all the way to the left, the filter is unaffected by note pitch. In the middle, cutoff follows note pitch subtly,
allowing high notes to shine. When set all the way right, filter cutoff follows note pitch closely in a relative fashion, mov-
ing upward and downward in semitone values as notes are received. This lets you use the filter as an additional pitched
oscillator or resonator when filter Res is set high.
LFO 1 and LFO 2
LFO stands for Low Frequency Oscillator, and they work very much like Osc 1 and 2 in Mai Tai, only slower. Standard oscillators are
used mainly to create audible pitched tones, LFOs create slow-moving regular cycles of control signal that are useful for modulating
other parameters over time. One common example is the way many synth patches respond when you move the Mod Wheel up from
zero; the pitch of the oscillators wavers up and down in an expressive manner, much like the sound of vocal vibrato. This is simply an
LFO modulating oscillator pitch to a degree set by the position of the mod wheel.
LFO 1 and 2 have identical controls, so the following explanations apply to both:
-
Bypass Click the [LFO 1] or [LFO 2] button to turn the LFO on or off.
-
LFO Type Choose between Sine, Triangle, Sawtooth, Square, and Sample & Hold shapes, for the oscillation of the LFO.
-
Rate This control lets you set the rate at which the LFO oscillates, from inaudibly low (0.01 hz) for long, sweeping changes, all
the way to higher ranges (up to 8 kHz) useful for FM techniques. When the [Sync] button is engaged, Rate can be set in terms of
rhythmic values relative to Song tempo, such 1/8th-note and 1/4-note.
-
Sync Engage this option to enable setting LFO Rate to a rhythmic value (such as 1/8th-note or 1/4-note) relative to Song tempo.
Disengage to set Rate by Hz.
-
Key Engage this option to bind LFO speed to incoming note pitch. Higher notes result in higher LFO speeds, while lower notes
result in lower LFO speeds.
-
Free Engage this option to let the LFO run continuously, resulting in a differing LFO start point for each note played. Disengage
to restart the LFO waveform at the start of each note.
-
Delay This control lets you specify an amount of time (in milliseconds) for the LFO to wait before becoming active after a note is
played. This lets you do things like adding a bit of expression to held notes, or creating layers of modulation that start at different
points in each note by setting distinct Delay values for each LFO.
Mai Tai

Envelopes
Envelope generators are a vital part of sound synthesis, giving us the ability to shape the amplitude and timbre of our sounds within the
time-scale of each note. Mai Tai has three envelope generators, labeled Amp Env (so named because it is hard-wired to amplitude), Env
2 (which is often routed to filter cutoff, for timbral shaping), and Env 3.
All three Env modules are triggered when a note is played. Each Env then outputs a control signal that follows the shape set by the fol-
lowing controls:
-
Attack (A) This control lets you set the time required for the
envelope to go from zero (silence) to full amplitude, in a range
from 0 ms to 20 seconds.
-
Decay (D) This control lets you set the time required to drop from
full amplitude to the sustain level, in a range from 0 ms to 20
seconds.
-
Sustain (S) This control lets you set the signal level that is main-
tained from the end of the decay period, until the key is released,
in a range from -∞dB (silence) to 0.0 dB (full amplitude).
-
Release (R) This control lets you set the time required to fall
back to silence after the key is released, in a range from 0 ms to
30 seconds.
-
Delay (△- Env 2 and 3 only) This control lets you specify a
length of time (in ms) for the Env to pause before starting its
attack phase after a note is played. This can assist in creating
evolving sounds, where cycles of modulation occur at differing
times over the length of a note.
Envelope Graphical Display
Each envelope has a corresponding graphical display that represents the shape created by the settings of its parameters. There are
handles on the corners and slopes of each envelope that you can click and drag, letting you shape the ADSR envelope and the curve
between its points visually. If you wish to lengthen any phase of the envelope beyond the time limits of the current display, simply drag
the point toward the right of the graph, and the time scale adjusts to properly display the new setting.
Global Settings
The following Global parameters let you configure Mai Tai's overall behavior and capabilities, to meet your needs:
Mai Tai

-
Volume This control lets you set the total output volume, in a range from -∞dB (silence) to
+6.0 dB (six decibels above unity gain).
-
Velocity This control lets you set the degree to which Mai Tai's volume is affected by note velo-
city, from zero (no velocity sensitivity) to 100% (full velocity sensitivity).
-
Poly, Mono, and Glide Enable Poly mode to allow polyphonic playing (more than one note at
a time). Enable Mono mode to play just one note at a time. When in Mono mode, you can
enable Glide to cause the pitch to sweep smoothly from that of the currently held note to that of
the next note, when played legato (one note played while the previous note is held). The Glide
knob lets you set the rate of pitch change over time, from 1 ms to 1 second.
-
Voices This parameter lets you set the level of polyphony (number of available simultaneous
voices) for Mai Tai, in a range from 1 to 32. Note that this control has no effect when in Mono
mode (in which there is only one voice available, by default).
-
Quality Choose from a variety of sound quality modes to suit the power of your CPU and your
taste in synth timbres. The following modes are available:
-
80s The simplest and most CPU-efficient of the modes. High-frequency modulation
can create harsher, more typically "digital" artifacts in this mode, much like some early
digital synths of the 1980s.
-
Normal The default mode, Normal makes a good compromise between CPU load
and sonic complexity. This mode is useful in most standard synthesis tasks.
-
High This mode budgets additional CPU power to handle high-frequency modulation
(such as that used in FM synthesis) smoothly.
-
Supreme This mode strives for the most realistic simulation of analog synthesis; rich
and complex. CPU usage is high, but the results can be worth it.
Effects
Mai Tai offers seven effects processors to add dimension to your sounds. They are arranged in two banks: FX A (Modulation, Delay, and
Reverb) and FX B (Gater, EQ, Distortion, and Pan). You can enable or disable each effect by clicking its name. You can show or hide the
Mod/FX section of the plug-in window by clicking the [Mod/FX] button.
Modulation
This processor creates time-based modulation effects. Choose from the following modes by clicking the [Chorus], [Flanger], or [Phaser]
button:
-
Chorus This processor creates effects similar to that of multiple identical instruments playing the same part simultaneously. The
synth signal is fed through a short, modulated delay, which is then mixed with the dry signal. Chorus offers the following controls:
Mai Tai

-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay. Higher settings create full-bodied chorusing effects,
while lower settings create more pronounced harmonics, akin to the effects of a Flanger.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler chor-
using effects, while higher settings produce more pronounced changes in timbre over time.
-
Depth This control lets you blend between the dry signal (all the way left) and the chorused signal (all the way right).
-
Flanger This processor creates resonant, hollow-sounding sweeping effects. The synth signal is fed through a short, modulated
delay, which is mixed with the dry signal. While similar to the workings of a Chorus effect, Flangers get their signature sound by
employing smaller delay times than those used in chorusing, combined with a feedback system that can add extra resonance to
the sweep. Flanger offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Delay This control lets you set the length of the modulated delay (in ms), which changes the pitch of the resultant res-
onance. Higher settings create lower-pitched resonance, while lower settings create resonances at a higher pitch.
-
Speed This control lets you set the speed at which the delay line is modulated. Lower settings create slow, sweeping
effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the delay line is modulated. Lower settings produce subtler flanging
effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Flanger. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Flanger modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the flanged signal (all the way right).
-
Phaser This processor creates dreamy, otherworldly sweeping effects. The synth signal is fed through a series of all-pass filters
that alter its phase. When mixed with the dry signal, this creates a series of peaks and valleys in the frequency response that
changes depending on the degree of phase shift applied. Phaser offers the following controls:
-
Mono Engage this option to sum the wet (effected) signal to mono.
-
Shift This control lets you specify the amount of phase shift to apply. Lower settings focus the phasing effect in the
lower frequencies, while higher settings focus the effect in higher frequencies.
-
Speed This control lets you set the speed of modulation applied to the phase shift amount. Lower settings create slow,
sweeping effects, while higher settings create faster, more aggressive modulation.
-
Width This control lets you set the degree to which the phase shift amount is modulated. Lower settings produce
subtler effects, while higher settings produce more pronounced changes in timbre over time.
-
Feedback (FB) This control lets you set the amount of output signal to feed back into the Phaser. Higher amounts of
Feedback add to the resonance of the sweeping effect.
-
Sync Engage this option to enable setting Phaser modulation speed to a rhythmic value (such as 1/8th-note or 1/4-
note) relative to Song tempo. Disengage to set Rate on a continuous scale.
-
Depth This control lets you blend between the dry signal (all the way left) and the phase-shifted signal (all the way
right).
Delay
This processor creates an echo effect, either as a single delayed repeat of the input signal, or a trailing series of echoes. The Delay effect
offers the following controls:
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the delayed signal.
Mai Tai

-
Delay Time This control lets you specify the length of the delay effect, in rhythmic values (such as 1/8th-note or 16th-note) rel-
ative to the tempo of the Song.
-
Feedback (FB) This control lets you set the amount of effected signal that is fed back into the Delay effect. At zero, there is just
one repeat. As you increase the value, the trail of repeats grows.
-
Mix This control lets you blend between the dry signal (all the way left) and the delayed signal (all the way right).
-
Ping-Pong Mode This menu lets you enable and configure the stereo Ping-Pong delay mode. You can choose from the fol-
lowing modes:
-
Off The delay works as normal, without ping-pong functions.
-
Panned Using a multi-tap delay structure, this mode pans each delay repeat to the right or left, in sequence.
-
Dotted and Double These modes work similarly to Panned mode, but employ staggered spacing of the delay taps to
produce a dotted-note or syncopated straight rhythm in the delay repeats.
-
Reverb Enable this option to route the output of the Delay effect to the Reverb effect, enabling further diffusion and abstraction
of the delay signal.
Reverb
This effect places the synth signal within a synthesized reverberant physical space, ranging from short reverbs that emulate smaller
rooms, to long reverbs that evoke the sounds of large spaces, such as halls and cathedrals. Reverb offers the following controls:
-
Pre-Delay (Pre) This parameter lets you specify an amount of delay applied to the reverb-processed signal, in a range between
zero and 500 ms. This emulates the delay inherent in large spaces between the impact of a sound and its audible reverberation.
Lower settings are best suited to shorter reverb times, and longer settings with longer reverb times, but let your own taste be the
judge.
-
Damping This control lets you set an amount of high-frequency attenuation to apply to the reverb signal. Spaces with soft sur-
faces tend to lose treble quickly as the sound reverberates, resulting in a short bright reverb followed by a progressively darker
tail. Spaces with harder surfaces retain high-end more efficiently over time. Set Damping to its lower rage to emulate hard sur-
faces, and to the higher ranges to enable further damping, to emulate softer surfaces.
-
Size This control lets you set the length of reverberation from the moment a sound starts, in a range between 100 ms and 10
seconds. The larger the size, the longer the tail of the reverb, and the larger the emulated space sounds.
-
Low and High These controls let you set the cutoff frequencies of the provided high-pass and low-pass filters, which effect only
the reverb signal.
-
Mix This control lets you blend between the dry signal (all the way left) and the reverb signal (all the way right).
Gater
This is a rhythmic gating effect, able to create a series of syncopated breaks in the synth signal. A variety of presets are provided, each
with a different rhythmic gating pattern. However, the fun really begins when you create your own. Gater offers the following controls:
-
Beats This control lets you set the length of the gating cycle, in rhythmic values (such as 1 bar or 1/2-note) relative to Song
tempo. For example, at a setting of 1 bar, the 16 steps in the cycle repeat every bar, effectively representing 16th-notes. At a
1/2-note setting, the 16 steps repeat each half-bar, representing 32nd-note values.
-
Beat Steps This grid lets you specify which steps in the cycle lets signal pass through, and which gates the signal to silence.
Click on a step to enable or disable gating for that step.
-
Stereo Engaging this option creates a separate beat grid for each side of the stereo field. When engaged, you'll see two rows of
beat steps, the top row specifying gate steps for the left channel, and the bottom row gating the right channel.
Mai Tai

-
Depth This control lets you blend between the gated and dry signals, allowing for rhythmic gating effects while retaining the con-
tinuity of the synth sound.
EQ
This is a graphic equalizer effect, perfect for quick tonal shaping. Set the EQ bands to emphasize or attenuate bands of frequencies to
suit your needs. When a band is in the center of its range, it neither adds nor subtracts. When moved above the center, it emphasizes the
chosen frequency. Moved below the center, it attenuates that frequency.
Choose between Lead mode, with frequencies chosen to suit aggressive, up-front sounds, or Bass mode, with wider-ranging fre-
quencies that work better for basses and mellower chordal parts.
Distortion
This is a variable distortion effect, which adds grit and character to your sounds. Choose from a variety of distortion types, from fizzy tran-
sistor fuzzes to thick, warm tube overdrives. Set the amount of distortion with the Drive knob.
Pan
This is an auto-pan effect, which pans the synth signal left and right over time. Pan offers the following controls:
-
Speed This control lets you set the speed at which the signal is panned left and right.
-
Sync Enable this option to set pan speed to a rhythmic value (such as 1/4-note or 16th-note) relative to Song tempo. Disable
this option to set pan speed along a continuous range.
-
Depth This control lets you set the degree to which the signal is panned. Lower settings give a subtly panned effect, while higher
settings pan the signal more radically, all the way to fully left and right in each cycle.
Modulation Matrix
Mai Tai provides 16 configurable modulation routings, in two banks of eight (Mod A and Mod B). Modulation signals can be routed from a
selection of incoming MIDI controller signals, including MPE data (such as Pitch Bend, Mod Wheel, Aftertouch, Poly Pressure, Note
Timbre, and Pitch Control), modulation generators (such as the LFOs and envelopes), or the pitch or velocity of played notes.
Mai Tai

These modulation signals can be used to vary most of the parameters throughout Mai Tai, including modulation sources themselves
(such as LFO 2 modulating the rate of LFO 1, or the Decay of Env 2)
Each modulation slot has a bypass button at the top, which lets you enable or disable the flow of modulation signal. Below that are the
input selector and modifier selector. If you assign a modulation source to the input selector only, that signal is routed directly to the
chosen destination. In some cases, you’ll want to govern the flow of one mod source before it reaches its destination, using the signal
from another mod source. For example, you may want to control the output level of LFO 1 (routed to a parameter such as oscillator pitch)
with the Mod Wheel. In this case, you'd choose Mod Wheel with the input selector, and LFO 1 with the modifier selector below.
Below that is a slider that controls the amplitude and polarity of the modulation signal. Set at its center, no modulation occurs. Move the
handle right of center to send an increasing amount of the modulation signal, at its normal (positive) polarity, to the chosen destination.
Move it left of center to send the signal to its destination with a negative value.
If the parameter you wish to modulate is set to a high value, you may want to send a negative modulation signal to it, driving the setting
downward and causing more audible effects. Positive-going modulation signals are more efficient when modulating parameters set to
low values.
A selector at the bottom of each modulation slot lets you choose the destination of the chosen modulation signals.
Virtual Keyboard
The virtual keyboard lets you easily click to play notes or manipulate the Pitch and Mod wheels, while auditioning or editing patches when
you're away from a MIDI keyboard. The keyboard display also shows you which notes are currently being played.
Note that for a more playable keyboard experience when away from your MIDI controller, you can also use Studio One's Use Your Com-
puter Keyboard as a MIDI Keyboard to play notes using your computer's keyboard.
Next to the virtual keyboard is the Bend parameter, which lets you set the pitch bend range of the Pitch wheel, in semitones.

## Mojito

Mojito is a simple, monophonic, subtractive synthesizer with effects that is capable of generating a wide range of sounds. It models a clas-
sic analog synthesizer and features a low-aliasing oscillator and a 24 dB filter emulation. Mojito can generate killer bass sounds, lead
sounds, and special effects.
Make sure to download the sound sets that came bundled with your edition of Studio One. Mojito requires the sound set download for
sounds and presets to work as intended within the virtual instrument.
Interface
Mojito is organized into Oscillator (OSC), Amplifier (AMP), Filter (FLT), and FX sections, with easy-to-use, yet powerful controls.

## Mojito

Oscillator
Mojito’s Oscillator section is on the upper left of the plug-in window. Here you can set up the harmonic content of the sound source. The
basic controls are the three large knobs on top: Pitch, Wave, and Width.
-
Pitch Adjusts the frequency from one octave below to one octave above the played note. Note that this affects the cutoff fre-
quency only via key tracking. Pitch is modified by the pitch-bend wheel (± 2 semitones).
-
Wave Selects between a sawtooth wave and a pulse wave. These two waveforms have a rich and regular harmonic content,
making them classic sources for subtractive synthesis. Sawtooth waves contain the fundamental and all harmonics whereas
pulse waves have only the fundamental and odd harmonics. Mixed settings effectively adjust the level of the even harmonics.
-
Width Adjusts the pulse width of the pulse wave from almost zero to square. This adjusts the balance between the fundamental
and the higher and lower harmonics.
Below the three main OSC controls is a smaller row of knobs that adjust how much the oscillator settings are modulated. The speed of
the modulation is adjusted using the LFO Speed controls, located to the right of these knobs. The LFO can be synced to tempo or it can
oscillate with a freely adjustable period. Use the modulators to create chorus-like or string-like sounds, vibrato, and other familiar mod-
ulated sounds.
There is also a Sub Oscillator knob, which can be adjusted from 0 to 100% to add more low frequency content to the sound.
The Portamento section lets you control pitch slewing between notes. Using the mode selector, you can choose between three modes:
-
Off A note that is played while another note is playing silences the previous note and trigger the new one.
-
Legato An overlapped note does not trigger a new envelope but the pitch slowly changes to the pitch of the new note.
-
Retrigger An overlapped note retriggers the current envelope, starting at its volume at the moment it is retriggered. This also
slowly changes the note’s pitch. Note velocity is not applied or updated for overlapped notes.
The Time knob adjusts the glide speed (that is, the duration of the pitch change) when using portamento. The range is from 5 ms to 1 s.
Amplifier
Below the Oscillator section is the Amplifier section. This consists of a Gain control, which responds to MIDI Volume messages, and a
Velocity-to-Volume control, which modulates the volume of a note in response to key velocity.
The most important part of this section is the ADSR envelope. (“ADSR” stands for “Attack, Decay, Sustain, Release.”) With these four
sliders, you can adjust the amplitude characteristics over time. These characteristics play a huge role in defining the overall sound. The
ADSR envelope can control the volume of a played note and can also control the filter cutoff.
-
A Adjust the attack time, which is the time required for the sound’s amplitude to go from zero (silence) to full amplitude. The
range is from 2 to 500 ms.
-
D Adjusts the decay time, which is the time required to drop from full amplitude to the sustain level. The range is from 2 ms to 1 s.
-
S Adjusts the sustain level, which is the level that is held from the end of the decay until the key is released. The range is from -
96 dB (silence) to 0 dB (full amplitude).
-
R Adjusts the release time, which is the time required to fall back to silence after the key is released. The range is from 2 ms to 2
s.
Filter
The section on top of the right side of Mojito only affects the resonant 24 dB low-pass filter.
-
Reso Controls the resonance of the filter, which is an amplification, or emphasis, of the signal at the cutoff frequency.
-
Note: If the amount of resonance of a filter is raised high enough, the filter begins oscillating at the cutoff frequency, thus
generating its own waveform. Be careful: this can be loud!
-
Drive Controls the amount of filter drive from 0 to 100%.
-
Cutoff Knob Controls the corner, or cutoff, frequency, which is the point above which frequencies are attenuated. The range is
from 20 Hz to 16 kHz.
The other controls affect the modulation of the cutoff frequency.
-
Key Controls how much the played note scales the cutoff frequency.
-
Velo Controls how much the velocity of the played note shifts the cutoff frequency up or down.
-
Envelope Controls how much the ADSR envelope shifts the cutoff frequency up or down.
-
LFO Controls the amount of shifting that the filter LFO applies to the cutoff frequency. The LFO can either be synced to tempo or
it can oscillate with an adjustable period.

## Mojito

FX
On the bottom right is a small effects section where you can apply a modulation effect to enliven or broaden the sound. Mod Depth con-
trols the amount of this effect. Using Mod Color, you can adjust the timbre from a flanger-like to a chorus-like effect. The modulation util-
izes an LFO that has the same speed as the filter LFO.
Finally, there is an Overdrive, the amount of which is controlled by the Drive control.

## Multi Instruments

Sometimes, just one instrument isn't enough to get the sound or functionality you're looking for. You might want each half of the keyboard
to trigger a different instrument, or to create powerful layered sounds with multiple instruments responding to your touch simultaneously.
Creating flexible, playable instrument configurations with multiple plug-ins, keyboard splits, layers, and real-time Note FX processing is
easy using the Multi Instrument function in Studio One.
To simplify the process of controlling multiple instruments and effects at once, we've included a page of Macro Controls you can assign
to parameters in any plug-in hosted in the Multi Instrument, giving easy access to vital parameters without the need to open multiple plug-
in windows.
Creating a Multi Instrument
To get started making your own Multi Instrument, open the Instruments tab in the Browser, expand the Multi Instruments folder within,
and create a Multi Instrument in one of the following ways:
-
Drag the New Multi Instrument preset to an existing Instrument Track.
-
Drag the New Multi Instrument preset to the top or bottom of the track list or between two existing tracks to create an Instrument
Track containing a new Multi Instrument.
This procedure also applies when creating a new instance from a non-default Multi Instrument preset.
Once the new Multi Instrument is created, its editor window opens. Here, you'll find a device routing matrix, instrument inspector, and key-
board range settings. You can click-and-drag the corner of the window to re-size it to your needs.

## Multi Instruments

Adding Devices to the Routing Matrix
Each instance of Multi Instrument can host multiple plug-in instruments and Note FX processors. Before any devices are added, the rout-
ing matrix in the center of the main control window is empty. To add an instrument, click the [Add Instrument] button and select the instru-
ment of your choice from the menu. Once the instrument is loaded, its editor window is displayed. You can also simply drag instruments
from the Instruments tab of the Browser directly into the routing matrix.
The chosen instrument appears as a module in the routing matrix, with a line leading to it, signifying the flow of note and control data to
that instrument. If you add additional instruments, the line splits, to show the flow of data to each instrument.
To bypass or enable an instrument or Note FX module, press its Activate button.
To open the editing interface for an instrument, double-click on its name, or click the small triangle on the right of the module and choose
Edit... from the pop-up menu. To rename an instrument or Note FX module, choose Rename... from its pop-up menu. To remove an mod-
ule, choose Remove from its pop-up menu.
Adding Note FX to the Routing Matrix
Using Note FX within a Multi Instrument can add dimension and animation to your sound. You can use them to affect note data feeding
all instruments at once, or use different Note FX on each instrument, or on pairs of instruments, using the Splitter function.
To add a Note FX processor to your Multi Instrument, click the Add Note FX button and choose a processor from the menu. You can also
do this by clicking-and-dragging the processor of your choice from the Note FX folder in the Instruments tab in the Browser onto the rout-
ing matrix. Once the Note FX module is loaded, its editor window is displayed.
Where you place a Note FX module in the routing matrix determines how the module is routed. If you want a Note FX to affect all instru-
ments within the Multi, drag its module to the top of the routing matrix. In this case, all data flows through the module before splitting off to
feed the instruments. To affect just one instrument, drag the Note FX module just above the instrument module of your choice.
Note FX Splitters
To affect two instruments in tandem with one Note FX module, you'll want to use a Splitter. To add a Splitter to the matrix, click-and-drag
the Drag Splitter button, and place your Splitter between the two chosen instruments. Any Note FX placed above the Splitter affects all
note data running to the two instruments, for simultaneous chord generation, arpeggiation, and so on.
Note that FX Splitters are only available (and needed) when three or more instruments are present in the current Multi Instrument. If just
two instruments are present, you can affect both instruments with a single Note FX by dragging the Note FX module onto the top of the
signal flow diagram.
To remove an instance of Note FX or a Note FX Splitter, click the triangle on the right side of the module, and choose Remove from the
pop-up menu.
Keyboard Splits and Layers
By default, each instrument in a Multi Instrument receives note data from the full range of the keyboard. If you want to split the keyboard
into distinct ranges (such as synth bass on the left side, and piano for the right hand), or simply specify an instrument's playable range,
you can use the range sliders, just above the virtual keyboard display.
Each instrument in a Multi Instrument has a range slider that specifies the range of keys in which that instrument is allowed to play. Click-
and-drag the ends of each range slider until the desired range of keys is selected for each instrument.
If two or more instruments overlap in their ranges, those sounds are layered when keys in overlapping ranges are played. Layering can
be useful for building rich, complex tones from multiple sources.
Multi Instrument Inspector
When you select an instrument module in the matrix, the Multi Instrument Inspector shows a mix of parameters you would normally see
in the Track and Instrument Inspectors elsewhere in Studio One. Here, you can set transposition and key range, as well as get access to

## Multi Instruments

audio settings, Inserts, and Sends for the selected instrument.
You can color-code Instrument or Note FX modules by selecting them and clicking the color picker to the left of the name of the module in
the inspector.
Because Inserts and effects settings are saved as part of Multi Instrument presets, you may find it helpful to use Multi Instruments to save
complex single-instrument configurations with many Insert effects, for later use.
When you select a Note FX module in the matrix, its controls are made available in the Inspector.
Macro Controls
Given that a Multi Instrument may contain several instruments and a selection of Note FX and audio effects, we've included a set of
assignable Macro Controls in each Multi Instrument (much like the Channel Editor and Macro Controls controls you'll find in the Con-
sole). This lets you assign often-used parameters throughout all devices in your Multi Instrument to a single page of knobs, buttons, and
X/Y pads.
To show the Macro controls, click the Instrument Macro button in the Multi Instrument editor window. To assign an instrument or effect
parameter in your Multi Instrument to an Instrument Macro control, [Right]/[Ctrl]-click the control element in the plug-in, and choose Con-
nect [parameter name] to Instrument Macro Control [control of choice]. Your choice of assignments is displayed next to each Macro con-
trol.
[Right]/[Ctrl]-clicking a control that is already assigned to a Macro gives you the option to break that connection.
For more on the use of Macro Controls, see Channel Macro Controls.
Audio Routing and Insert Effects
Each instrument in a Multi Instrument routes its audio to a Channel in the Console as usual, all of which are encapsulated in a group Bus,
titled "Multi Instrument" by default. To access individual mixing controls for instruments within a Multi, click the folder icon at the bottom of
the Multi Instrument channel strip in the mixer. All individual routing and processing flexibility remains, while the Bus keeps the instru-
ments together and easier to manage as a group, especially in larger sessions. If you wish to send an instrument to the Main bus or other
bus (rather than run it through the Multi Instrument bus), you can make these changes in the Console or in the Inspector view in the Instru-
ment Editor window.

## Multi Instruments

Storing and Loading Multi Instrument Presets
Once you've set up a satisfying Multi Instrument, you may want to store it as a preset, so that you can call it up for use in other projects.
You can also export your preset as a file, or import a preset from a previously exported file. Click the Preset Actions button in the menu
bar of a Multi Instrument window, and choose from the following preset management functions:
-
Store Preset... Choose this to save a preset to your library in the Browser. You can enter a title and description for the preset,
as well as specify a subfolder within the preset list to store the preset.
-
Replace Preset Choose this option to update the currently loaded preset with any new settings made since loading the preset.
-
Store as Default Preset Choose this option to make the current preset load whenever a new Multi Instrument is created.
-
Load Preset File... Choose this option to load an exported Multi Instrument preset file from your file system into your current
Song.
-
Import Preset... Choose this option to load an exported Multi Instrument preset file from your file system into the current Song,
and import the preset into your Studio One library, for later use.
-
Export Preset... Export the current Multi Instrument configuration as a preset file, for use by others or for storage. This does not
save audio effects assignments or settings used within the Multi Instrument.
-
Export Instrument+FX Preset... Export the current Multi Instrument configuration as a preset file, including all audio effects
inserted for each instrument, and the corresponding effects settings.
-
Show in Browser Locates the currently loaded preset in the Browser.

## Note FX

Note FX are real-time effects processors that change and reinterpret incoming note data before it reaches your choice of plug-in instru-
ment or external MIDI device. Arpeggiator, Chorder, and Repeater are most useful for creative expansion and adaptation of note data.
Input Filter is a utility processor that limits note output to a selected range of note and velocity values. You assign Note FX to Instrument
Tracks in the Note FX section of the Track Inspector. For more information, see Track Inspector.
Once you've loaded one or more Note FX processors onto an Instrument Track, you can quickly access the related settings by clicking
the Note FX Editor button
on the control area for that Track in Arrange view. You can also access these settings by double-click-
ing one of the processors in the Note FX section of the Track Inspector.
You can save and load Note FX settings as presets, just as you can with other instruments and effects. For more information on saving
and loading presets, see the Signal Routing chapter.
Rendering Note FX
If you wish to make the effects of Note FX processing permanent (part of the note data, rather than a real-time process), select the Track
and navigate to Event/Render Instrument Tracks, or [Right]/[Ctrl]-click the desired Part in Arrange view and choose Instrument
Parts/Render Instrument Tracks from the pop-up menu.
This also makes permanent any transposition or velocity changes you've made within the Inspector view for the track.

## Note FX

Arpeggiator
Arpeggiator turns chords (as well as single notes) into arpeggios—rhythmic cycles of single notes, derived from the notes currently held.
Like the arpeggiator functions found in many synthesizers, Arpeggiator creates repeating patterns of notes that can travel upwards in
pitch, downwards, up-and-down, down-and-up, or in a randomized pattern. You can also use Arpeggiator to play repeated patterns of
whole chords, or note patterns that follow the order in which notes are played.
Going beyond the basics, you can use the Pattern function to create rhythmic patterns of velocity and note length that the arpeggio fol-
lows as it plays, opening many creative options for repeating musical articulations.
The following parameters and functions are available in Arpeggiator:
-
Arpeggio Direction Choose the note direction that creates the pattern you want, from the following options:
-
Up The arpeggio starts at the lowest held note and travels upward through the held notes, then returns to the lowest
note as the arpeggio begins again.
-
Down The arpeggio starts at the highest held note and travels downward through the held notes, then returns to the
highest note as the arpeggio begins again.
-
Up/Down The arpeggio starts at the lowest held note, travels upward to the highest, then travels back down to the low-
est note, and the arpeggio begins again.
-
Down/Up The arpeggio starts at the highest held note, travels downward to the lowest, then travels back up to the
highest note, and the arpeggio begins again.
-
Random The arpeggio plays the currently held notes in a random pattern.
-
Chord Mode The currently held chord (or single note) is repeated as long as it is held.
-
From Input The arpeggio pattern is derived from the order in which notes are played and held.
-
Octave Range Lets you extend the range of the arpeggio by mirroring the currently held notes an octave above (at a setting of
2), the two octaves above (at 3), or the three octaves above (at 4). At 1, no mirroring occurs and the arpeggio plays according to
the held notes. Setting Octave Range above 1 when in Chord Mode causes an upward-rising cycle of repeated chords, an
octave apart, its length determined by the Octave Range setting.
-
Rate Lets you select a rhythmic value, determining the length of each arpeggio step. Range is from a bar to a 64th-note, in all
triplet and dotted varieties.
-
Swing Lets you add swing to the timing of the arpeggio, creating a range of rhythmic feels. For more information on swing tim-
ing, see Swing.
-
Gate Acts as an overall note-length control. Lower settings create shorter notes, and higher settings create longer notes. When
a Pattern is active, Gate works relative to the gate settings in the Pattern.
-
Hold Enable this to hold all currently played notes. Each new chord or single note that you play replaces the previous memory
and holds until the next note input is received.

## Note FX

-
Velocity Acts as an overall note-velocity control. When a Pattern is active, Velocity works relative to the velocity settings in the
Pattern.
-
Pattern/Fix Switches Choose Pattern to allow Velocity data from the Pattern to control note velocity (in tandem with the Velo-
city control). Choose Fix to set a fixed velocity for all notes, with the Velocity control.
-
Pattern This is a 32-step pattern sequencer you can use to create repeating patterns of note velocity and gate (length) that are
applied to the control output of the Arpeggiator. The Pattern area contains the following controls:
-
Activate Pattern Toggle this on or off to enable or disable the Pattern sequencer.
-
Pattern Sequencer This series of sliders is where you'll create your velocity/gate pattern. You can click and drag each
step in the sequence vertically (to set velocity) and horizontally (to set gate length). 16 steps are shown at any one time.
To reach the second set of 16 steps, click the right-arrow to the right of the pattern. To return to steps 1-16, click the left-
arrow to the right of the pattern.
-
Pattern Length Lets you choose the length of the pattern.
Chorder
Chorder is an intelligent chord generator that lets you trigger chords by playing single notes. You can specify intervals in the chord manu-
ally, or capture chord shapes played on the keyboard. Each key can trigger a different chord of your choice, or you can choose a single
chord shape, to play across multiple keys. You also have control over the area of the keyboard that triggers these chords, letting you, for
example, trigger chords in the upper part of the keyboard, while playing single-note bass parts in the lower half.
The central interface shows two rows of piano-style keys. The lower row is used to audition chord shapes; click and hold a key to play. In
Learn Mode, the lower row lets you select a keyboard key for chord assignment (selected key turns orange). The upper row displays the
notes being played (both by MIDI input and the chord generator), and which keyboard keys have been assigned chord shapes (small
square at the bottom of each key turns orange). In Learn Mode, the upper row displays the currently assigned chord shape for the selec-
ted key (chosen notes turn orange).
Assigning Chord Shapes
Chorder defaults to an example chord setting that you can play with. The next thing you'll want to do is assign your own chord shape to
one or more keyboard keys. You can do so by following this procedure:
1.
Press the [Learn Mode] button to put Chorder into Learn Mode.
2.
Select a keyboard key for chord assignment by clicking it in the lower row of keys. The selected key turns orange. C3 is selected
by default.

## Note FX

3.
Build the chord shape of your choice by selecting notes in the upper row of keys with the mouse, or by playing notes on a con-
nected MIDI controller. Selected notes turn orange. Click or play a note a second time to deselect it.
4.
If you want to assign custom chord shapes to other keyboard keys, select each chosen key in the lower keyboard, and assign
chord shapes to each, as described in step 3.
5.
Press [Learn Mode] again to disengage, and begin playing.
The following parameters and functions are available in Chorder:
-
Learn Mode Enables Learn Mode. When Learn Mode is active, the following controls appear:
-
Clear All Clears all chord assignments for all keyboard keys.
-
Clear Clears chord assignments for the currently selected keyboard key.
-
Copy Copies the currently shown note pattern, for pasting into other keys.
-
Paste Applies copied note pattern data to the currently selected key.
-
Selected Keyboard Key Shows the pitch of the currently selected keyboard key. To specify a particular note value,
click this field to select it and type in the note name and octave number (such as C3). You can also click-and-drag in the
note field, or click on the note field and select with your mouse's scroll wheel.
-
Chord Range Drag the ends of this slider to select the portion of the MIDI keyboard that triggers chords.
-
Transpose Lets you transpose the chord output, in a range of -12 to +12 semitones. Notes outside the Chord Range are unaf-
fected.
-
Auto Fill Enable this to automatically assign any unassigned keyboard keys in the Chord Range to the chord shape mapped to
the lowest keyboard key. Disable to ensure that only assigned keyboard keys trigger chords.
-
Filter Outside Enable this to stop all notes that fall outside of the Chord Range. Disable to allow playing notes outside the
range.
Repeater
Repeater works just like it sounds—it creates rhythmic repetitions of the notes you play. These repetitions can be simple copies of incom-
ing notes, or can change in velocity, gate length, and pitch as the pattern plays.
The following parameters and features are available in Repeater:
-
Individual Velocity & Gate Engage to enable individual setting of note velocity and gate length for each step.
-
Individual Pitch Engage to enable individual setting of note pitch for each step.
-
Sequencer This lets you specify velocity, gate, and pitch values for each step in the sequence of repetitions. The following con-
trols are available for each step:
-
Level/Gate Slider With Individual Velocity and Gate enabled, you can click and drag the upper edge of this slider up or
down to set note velocity for the current step. You can also click and drag the right edge of the slider left or right to set

## Note FX

note gate length for the current step. With Individual Velocity and Gate disabled, moving velocity or gate sliders manip-
ulates that setting for all steps (equivalent to turning the Velocity Level and Gate knobs).
-
Pitch With Individual Pitch enabled, you can click and drag this slider up or down to apply a positive or negative pitch
transposition to the current step. With Individual Pitch disabled, moving a pitch slider changes pitch transposition for all
steps simultaneously. At 0, no transposition occurs.
-
Rate Lets you set the rate of repetition. When Sync is enabled, you can choose a tempo-synced rhythmic value between one
bar and one 64th-note, in all triplet and dotted varieties. When Sync is disabled, you can choose a repetition frequency between
2 and 25 Hz (repetitions per second).
-
Sync Enable Sync to snap the Rate control to rhythmic values, in sync with Song tempo. Disable to set repetition speed in Hz.
-
Steps Select your desired number of repetitions (and sequencer steps), from just two steps, to 32.
-
Velocity Level Acts as an overall velocity level control, scaling every step's velocity, relative to its custom setting.
-
(Velocity Relative to) Input Enable this to derive overall repetition velocity from note input, attenuated or boosted by the set-
ting of the Velocity Level control.
-
Velocity Scale Turn this to introduce a sloping change in velocity in the sequence over time, relative to each step's setting. At
center, no slope is added. Turned left of center, a downward slope is introduced. Turn to the right for an upward slope.
-
Gate Acts as an overall gate length control, scaling every step's gate length, relative to its custom setting.
-
Gate Scale Turn this to introduce a sloping change in gate length in the sequence over time, relative to each step's setting. At
center, no slope is added. Turned left of center, each step in the sequence is shortened more than the last. Turn to the right, and
each step is lengthened more than the last.
-
Pitch Scale Turn this to introduce a sloping change in pitch in the sequence over time, relative to each step's setting. At center,
no slope is added. Turned left of center, you get a range of downward pitch shift slopes. Turn to the right for upward slopes.
Input Filter
Input Filter lets you filter out unwanted notes before they reach your instrument or MIDI device. You can specify a range of note pitches to
allow, and a range of note velocities to allow, and all notes that fall outside of either of those ranges are stopped. The following para-
meters are available in Input Filter:

## Note FX
