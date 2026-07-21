# Built-In Effects

> **Source:** PreSonus Studio One 6.6 Reference Manual (EN)
> **Manual pages:** 410–477
> **Slug:** `17-built-in-effects`

**Agent topics:** `plugins`, `effects`, `Pro EQ 3`, `dynamics`, `reverb`, `delay`, `distortion`, `modulation`, `Pipeline XT`, `Mix Engine FX`

---

Built-In Effects
Studio One features a number of built-in, high-quality, 64-bit audio effects and virtual instruments. The following chapter describes each
audio effect in detail. Virtual instruments are covered in the Built-in Virtual Instruments chapter.

## Effect Micro Views

Micro Views are small, expandable control panels within the Insert Device Rack that allow control over the critical parameters of each
effect. Using the Micro View in the Insert Device Rack often prevents having to open the entire effect interface, and it also allows easy
monitoring of compression, gating, splitters, and other effects. Try Effect Micro Views in both the small and large Console views.
To expand the Micro View for any built-in effect, open the Console and click once on the effect in the Insert Device Rack. The Micro View
expands downward, revealing certain parameters of the effect. Not all parameters of each effect are available in the Micro View, only
those you are likely to change frequently.
Built-In Effects

In the large Console view, notice the arrows at the very top and bottom of the Insert Device Rack. Click on these arrows to scroll up and
down in the Insert Device Rack to view any number of open Micro Views. To collapse any Micro View, click once on the effect name at
the top of the Micro View.
A right-click/drop-down menu is available from every Plug-in Micro View. Options include:
-
Edit: Opens the Plug-in Editor.
-
Expand: Expands the Micro View to reveal parameters.
-
Rename: Re-name the Plug-in.
-
Bypass: Bypasses the Plug-in.
-
Favorite: Tags the Plug-in as a Favorite in the Browser.
-
Store Preset: Saves the current parameters as a Plug-in Preset.
-
Disable: Disables the Plug-in.
-
Enable Plug-in Nap: Activates Plug-in Nap. (Only available if Plug-in Nap is enabled)
-
Remove: Removes the Plug-in.
-
Set Up Micro Edit Parameters: (Exclusive to third-party plug-ins) Select this to bring up a configuration menu which allows you
to select which parameters are editable from Micro View. The default setting is for the first five parameters. The parameters on
the left side of the interface can be dragged and dropped to your desired order.
Analysis and Tools
Some of the following metering and analysis plug-ins can switch between Peak/RMS and a range of K-System level metering modes. If
available, you can [Right]/[Ctrl]-click a plug-in's Peak/RMS meter to open a list of alternate metering modes to choose from.
Phase Meter
Analysis and Tools

The Phase meter is helpful when checking stereo-playback issues and mono compatibility. There are two components to this meter: a
large goniometer at the center of the plug-in window and a correlation meter at the very bottom.
The goniometer displays left versus right channel amplitude on several axes. A line in the following directions of the Goniometer display
would mean:
-
M-Axis Mono signal
-
+/-S Axis Mono with one channel totally out-of-phase
-
L/R Axes Mono on one channel (left or right)
-
M/S Axes Channels in a Mid-Side (MS) encoded or recorded signal
The correlation meter shows the average amount of in-phase and out-of-phase audio signal. Correlation meter parameters are:
-
+1 Mono signal
-
-1 Reversed-phase mono signal
-
0 Independent signals (true stereo or dual mono)
Analysis and Tools

Spectrum Meter
Spectrum Meter is helpful when determining the frequency content of an audio signal. For instance, you might know that a drum loop
needs some EQ, but you might not be sure what frequencies to bring up or down. Or there might be an annoying ring in a guitar part that
you want to get rid of but you do not know the frequency of the ring. Spectrum Meter can help diagnose these problems, and many oth-
ers.
Spectrum Meter is fully adjustable using the following parameters at the bottom of the plug-in window:
Channels
When Spectrum Meter is inserted on a stereo Track, you can choose from the following channels to be analyzed in the meter:
-
L Left channel only
-
R Right channel only
-
L+R Sum of left and right channels
-
L-R Difference between left and right channels
When Spectrum Meter is inserted on a multichannel source, the Channel Modes you can choose to analyze from will vary, depending
upon the source material. If inserted on an Audio Channel, the Channel Mode options are based on the Channel’s selected format (5.1,
7.1.2, etc.). If inserted on the Main Out of a Song using Dolby Atmos, the Channel Modes available are determined by the Bed Format
selected in the Dolby Atmos Renderer.
Analysis Mode
-
Octave Octave Band displays frequency content divided into octaves, useful for determining broad balance across the fre-
quency spectrum.
-
3rd Octave Third-Octave Band displays frequency content divided into 1/3 of an octave, useful for determining balance with
good precision across the frequency spectrum.
-
12th Octave The bands in the 12th-octave meter correspond to the 12 musical tones in an octave, each in its appropriate place
on a piano-like keyboard. This allows for easy reading of the pitch or note value of a given signal.
-
FFT A Fast Fourier Transform, or FFT, displays frequency content divided into many bands. It’s useful for accurate metering of a
specific range of the frequency spectrum.
-
When FFT is selected, you can select the FFT window size (FFT size = time vs. frequency resolution). You can choose
from 16,384; 8,192; 4,096; and 2,048. The default setting is 16,384.
-
As FFT measurements are divided into bands, exact frequencies across the entire spectrum are not measured.
Analysis and Tools

-
When using the FFT display, a -3 dB/octave line is displayed in addition to the frequency and level crosshair. This line
represents compensation for the shrinking frequency-width of the FFT bands toward the higher end of the spectrum,
which leads to a lower energy content. A well-balanced mix should somewhat approximate the slope of this line.
-
FFT Curve This performs the same analysis as the FFT mode, but displays the result as a single white line.
-
Waterfall & Sonogram Two modes that graph changes in frequency content and dynamics over time.
-
Segments Closely resembles the output of an FFT display. However, the X/Y grid is split up in uniform segments, rather than
varying in resolution depending on frequency. Switchable amplitude segment sizes of 0.5, 1, and 2 dB.
Level Range
-
Minimum Level Minimum amplitude to be displayed for all frequencies. Variable from -144 dB to 6 dB less than the maximum
level.
-
Maximum Level Maximum amplitude to be displayed for all frequencies. Variable from 0 dB to 6 dB more than the minimum
level.
-
Fixed When engaged, five level ranges are available in the menu to the left: -50 dB, -72 dB, -96 dB, -120 dB, and -144 dB.
Note: You can also quickly change the Level Range by clicking and dragging vertically within the meter.
Frequency Range
-
Minimum Frequency Minimum frequency to be displayed. Variable from 20 Hz to within 10 Hz of the maximum frequency.
-
Maximum Frequency Maximum frequency to be displayed. Variable from 20 kHz to within 10 Hz of the minimum frequency.
The Min and Max Level/Freq values can be changed by typing in a new value, or by clicking-and-dragging up or down on the value.
Sidechain Input
To enable the sidechain feature, click the Sidechain button. This brings up a second spectrum display below the main display, showing
the frequency content of any signal you route to the Spectrum Analyzer's sidechain. This lets you compare the frequency response of
two different signals simultaneously, such as a rough mix and a reference track. For more information on routing signals to effect side-
chains, see Sidechaining in the Effects Signal Routing section.
Tuner
The Tuner proves invaluable when inserted on guitar, bass, and other instruments that require frequent tuning. The Tuner features a
switchable standard/strobe display, with exact Frequency and Difference readouts in the lower left corner. A Calibration knob enables cal-
ibrating the Tuner to a center frequency from 415 Hz to 465 Hz. Click on the [Strobe Mode] toggle switch to enable the strobe display, in
which the rotation speed is a measure of the amount you need to tune.
There is a center-note indicator with an arrow to either side. When the left arrow is displayed, the signal is tuned below the closest note;
when the right arrow is displayed, the signal is tuned above the closest note. When both arrows are displayed, the signal is perfectly
tuned.
Analysis and Tools

Level Meter
The Level Meter plug-in is a level meter that can be sized as a horizontal or vertical display type. The following parameters are available
in the Level Meter:
-
Mode Select True Peak, K-20, K-14, K-12, or R128 (Loudness) metering mode.
-
Corr Engage to display phase correlation.
-
RMS Len Click the field and select an RMS length value from the menu.
-
Hold Len Click the field and select a Hold length value from the menu.
When Level Meter is inserted on a multichannel source, the number of individual channel levels displayed is dependent upon the source
material. If inserted on an Audio Channel, the levels displayed are based on the Channel format. (5.1, 7.1.2, etc.). If inserted on the Main
Out of a Song using Dolby Atmos, the channel levels displayed are determined by the Bed Format selected in the Dolby Atmos Ren-
derer.
Scope
Analysis and Tools

The Scope provides the functions an engineer would expect from a digital oscilloscope and is useful for debugging problems in the stu-
dio, such as analyzing crosstalk and noise levels.
There are three signal channels and one math channel. Each channel can either show the left or right signal of the Insert Channel, or
sidechain input, while the math channel can show the difference between two of the signal channels. (B and C can be inverted to sum
instead, or to do a polarity flip.)
Each of the color-coded channels can be scaled and offset in the Y axis, and scaling is shown as percent of full scale per division. (Full
scale is 1.f, equivalent to 0 dB.) All channels can be activated/deactivated by clicking on the colored channel letter.
The time (x axis) can also be scaled and offset. This setting is for all channels. The offset is shown with a green vertical line.
The units follow the samples/seconds switch above the display, and can be expressed in decibels (dB) or percentages (-100% to 100%).
The scope is triggered from one of the following sources:
-
Slope Triggers when the signal level on the selected channel crosses a threshold level in the right direction. The threshold is
adjusted by the Trigger Level control. Note that this does not apply to the Math channel.
-
Transients This uses the same audio channel, and the Slope and Level controls still apply, but the transient level is usually
much more narrow: somewhere above 0% and typically around 1.5%.
-
External Signals Notes sent to the scope MIDI input or not sent at all (free).
Engaging Oneshot turns triggering off after the first received trigger. Retrig waits for one new trigger in case you get the wrong signal or
change the signal.
The Scope display is latching, meaning that a signal is shown only on the second trigger. Note that the scope does not clear its buffer on
stop, so there may be unwanted signal shown until another display trigger occurs.
Analysis and Tools

The Hold control adjusts the length of time shown for a trigger signal, and during this period, no new signal triggers the scope. This is
adjusted in percent of the display width and is also shown in the selected time unit and as a green vertical line. The display is clipped on a
new trigger.
Finally, there is a crosshair for measuring the signals. It has a tool-tip readout using the units displayed in relation to the selected chan-
nel. Use this for measuring distances/differences for the selection, where dB levels are rectified signal levels, so you can compare pos-
itive and negative peak levels.
Tone Generator
Tone Generator is capable of generating noise, frequency sweeps, and other signal types commonly used for signal-path testing and cal-
ibration. The Scope would commonly be used in conjunction with Tone Generator to analyze return signals at the end of the signal path
being tested or calibrated.
The following parameters are available in Tone Generator:
-
Waveform Choose from sine, saw, square, white noise, and pink noise.
-
Anti-Alias The saw and square waveforms have Anti-Aliasing engaged by default in order to prevent aliasing artifacts
from appearing.
-
Frequency Set the tone frequency from 1 Hz to 22 kHz.
-
Modulation
-
Wobble Engage this to make the tone frequency move from the set frequency to the modulation Target Frequency,
according to the Modulation settings.
-
Log. Sweep Engage to make the frequency sweep logarithmic instead of linear.
-
Length Set the length in time of the sweep from Frequency to Target Frequency; range is from 10 ms to 60 seconds.
-
Phase Shift Set the phase shift that occurs over the chosen Length of time, from 0° to 180°.
-
Target Frequency The end frequency to which the tone is swept during modulation.
-
Gated Gated allows the output to be turned on via a note played on a Keyboard (set the output of an Instrument Track to Tone
Generator).
-
Off/On The default setting is Off. On activates the Tone Generator.
-
Level The output level of Tone Generator, from -144 dB to +24 dB. (Use caution!)
IR Maker
Analysis and Tools

IR Maker is a utility plug-in that allows you to capture your own impulse responses for use with OpenAIR and with the cabinet section of
Ampire. The following describes general guidelines on how to use IR Maker to create impulses:
1.
In the Song/Song Setup/Audio IO Setup menu, create an Output Channel configured with the physical output on your interface
that the IR Maker sweep signal routes through. That output might be connected to a speaker in the space for which you want to
capture an IR, or to the Effects Return on an amplifier connected to a cabinet for capturing a guitar cabinet IR.
2.
Then, create an Input Channel in Song/Audio IO Setup, configured with the physical input on your interface that IR Maker gets
the return signal from. A microphone, or the output of a hardware processor, connects to this input when capturing the IR.
3.
Now create an Audio Track in a Song, set its input and output to the Input and Output you just created, and insert IR Maker on
the Track.
4.
Signal-path latency is important. That latency may vary because of the distance of the mic from the source, for instance, and
may be a part of the impulse response to be captured. So, it is easiest to detect the signal path latency with a loopback from inter-
face output to interface input. To do this, you need to route the physical output directly into the physical input, creating a loop-
back for the I/O you created before. Then, press Detect in the Latency Compensation section. If the latency box still shows zero
after testing, then something is wrong with your audio setup (levels, audio I/O ports, monitors, cables, interface settings, etc.).
5.
After detecting latency in the signal path, disconnect the loopback from before. Connect the output to the device that
receives/outputs the IR Sweep signal (a speaker in a room, a guitar amplifier Effects Return, etc.), and the input to the device
that captures the IR (a microphone in a room or in front of a guitar cabinet, or the output of a hardware device).
6.
The file Output Path is structured as a base part (the path to the folder where your IRs reside), a device part (the subfolder for
that cabinet, space, etc.), and an IR base-name (mic/mic-position).
7.
Select the Sweep Length (longer = higher-frequency resolution and less noise). In general, 60 seconds should be enough for
high fidelity. IR Length can always be shortened later to save CPU resources but it should be long enough to contain the whole
response. As a default for cabinets, we recommend using 0.1 s. Shorter Sweep and IR Lengths get calculated much faster.
8.
Normalizing ensures maximum loudness in IR but can be done later, and can destroy loudness relationships between different
devices.
9.
Usually you need to trigger the sweeping several times to adjust the levels. It helps to show Input and Output Channels in the
mixer to watch the metering closely.
10.
Check the Open checkbox to have your computer's file browser open the newly created impulse response after calculation. You
can then drag that onto a new Track to view the IR and make any edits you desire, such as fades; or drag the IR into OpenAIR or
Ampire for immediate use.
Analysis and Tools

Mixtool
Mixtool provides common track utilities, including independent left- and right-channel inversion, left- and right-channel swap, and MS
transformation of stereo signals. Use Mixtool when inverting channels to correct for phase cancellation and correlation issues, as well as
to provide MS transformation to decode signals recorded with Mid-Side stereo configurations.
The following parameters are available for Mixtool when used on a stereo Track:
-
Gain Set overall output Gain. Variable from -24 dB to +24 dB. Use [Ctrl]/[Cmd]+[Shift] and drag to fine-tune the value.
-
Swap Channels Click to swap left and right Mixtool input channels. Stereo Tracks only.
-
MS Transform Click to perform a Mid-Side transform on the Mixtool input channels. Stereo Tracks only. Generally used to
decode MS-recorded signals or to create MS signals for stereo image processing.
-
Block DC Offset Re-centers the incoming waveform, to remove any DC Offset in the audio signal.
-
Invert Left Click to invert the phase of the left playback channel for a stereo Track.
-
Invert Right Click to invert the phase of the right playback channel for a stereo Track.
MixTool is enhanced for use with multichannel audio. When assigned to a multi-channel source, MixTool will display adjustable faders
with optional phase inversion, Solo, and Mute available for each output.
Analysis and Tools

When used on a mono Track, the Mixtool plug-in has one control to invert the phase of the signal.
Delay
Analog Delay
Delay

Analog Delay emulates a one-head tape delay with optional tempo sync, LFO, filtered feedback, and other features. It can be used to cre-
ate deteriorating echoes, echoes with changing delay and pitch, and flanging/chorus effects. These types of sounds are often used in
Dub Music or ’70s rock.
The following parameters are available in the Analog Delay:
Delay
-
Time The base delay time.
-
Sync Optional Sync mode for Time.
-
Sync disengaged results in speed expressed as time from 1 ms to 3 s.
-
Sync engaged results in time expressed as beats from 4/1 to 1/64, with triplets.
-
Feedback Feedback percentage; that is, the amount of delayed signal to be fed back into the delay input. Variable from 0 to
100%.
-
Boost Enable this parameter to boost feedback levels.
LFO
-
Speed The base LFO speed.
-
Sync Optional Sync mode for LFO Speed.
-
Sync disengaged results result in Speed expressed as frequency, from 0.01 Hz to 5 Hz.
-
Sync engaged results in Speed expressed as beats, from 4/1 to 1/64, with triplet and dotted-time variants.
-
Amount Modifies the effect of the LFO on delay speed. Variable from -50% to 50%.
-
Type The shape of the LFO waveform; select from triangle, sine, sawtooth, and square.
Color
-
Low Cut Filters frequencies below this value from the delayed signal. Variable from Off to 20 Hz to 3.2 kHz. Filter is 6 dB per
octave.
-
High Cut Filters frequencies above this value from the delayed signal. Variable from 400 Hz to 16 kHz to Off. Filter is 6 dB per
octave.
-
Drive Emulates tape saturation with State Space Modeling. Variable percentage from 0 to 100%.
Motor
Delay

-
Factor Modifies tape speed. Variable from 0.5 (double the delay length) to 2 (half the delay length).
-
Inertia Modifies speed of changes over time, based on Factor. Variable from 0 to 5.
Synced LFO and synced delay with LFO slower than delay means that modulation is not perceptible (except with high inertia).
Width
-
Width Regulates the stereo width of the delay feedback. Variable from mono to full stereo width.
-
Ping-Pong Mode
-
Off Select this setting to shut off Ping-Pong Mode. This also can be used to freeze the delay effect to one side, for
example.
-
Sum Select this setting to feed a mono-summed mix of both channels into the delay. Try higher settings of the Width
control to achieve the full ping-pong effect.
-
2-Ch This option feeds the stereo mix into the delay. Try lower settings of the Width control to "monoize" the delay
effect.
-
Swap Click this to swap the left and right sides of the Ping-Pong effect. If Ping-Pong Mode is Mono and Width is 100%, for
example, this determines whether the delay effect starts on the left or right sides.
Global
-
Dry/Wet Adjusts the mix of processed signal and the original dry signal. Variable from 0 to 100%. A setting of 100% is likely to
increase feedback.
-
Locked Engage this switch to prevent changes to the Dry/Wet balance.
Beat Delay
The Beat Delay is a tempo-synced delay with optional cross-delay and filtered feedback. Use this effect for adding/changing the feel of
rhythmic parts (e.g., adding off-beats) or “spatially doubling” parts (for instance, slap-back echo). Beat Delay has the following para-
meters:
Beats Delay time expressed as beats. Variable from 4/1 to 1/64, with triplet and dotted-time variants.
Offset Adjusts a time offset from -30 to  +30% of the specified Beats value.
Feedback Percentage of delayed signal added back into the delay input. Variable from 0 to 99.99%.
Modulation
-
Ping-Pong
-
Off Select this setting to shut off Ping-Pong Mode. This also can be used to freeze the delay effect to one side, for
example.
-
Sum Select this setting to feed a mono-summed mix of both channels into the delay. Try higher settings of the Width
control to achieve the full ping-pong effect.
-
2-Ch This option feeds the stereo mix into the delay. Try lower settings of the Width control to "monoize" the delay
effect.
-
Swap Click this to swap the left and right sides of the Ping-Pong effect. If Ping-Pong is Mono and Width is 100%, for
example, this determines whether the delay effect starts on the left or right sides.
-
Width Regulates the stereo width of the delay feedback. Variable from mono to full stereo width.
-
Cross Delay When not set to Off (center), the input is sent, in mono, to the left or right channel, with a delayed signal sent to the
other channel. Variable from L 50 ms (right channel dry, left channel delayed 50 ms) to R 50 ms (left channel dry, right channel
delayed 50 ms). Extreme left or right settings create a pronounced stereo effect.
Delay

-
In Pan Sets the ratio between the left and right channels of a stereo input signal. When it is set to full Left, for example, only the
left channel of the input signal is delayed.
-
Pong-Factor Applies a multiplier to the delayed signal, with a variety of rhythmic subdivisions.
Color
-
Low Cut Scoops out the low end of the delayed signal using a 6 dB/octave filter. Variable from 20 Hz to 1 kHz.
-
Hi Cut Rolls off the high-frequency content of the delayed signal using a 6 dB/octave filter. Variable from 1 kHz to 20 kHz.
Global
-
Mix Adjusts the blend of the processed signal and the original dry signal. Variable from 0 to 100%.
-
Lock Engage this switch to prevent changes to the Dry/Wet balance.
Groove Delay
The Groove Delay is a four-tap, tempo-synced delay with variable filters and a variable beat grid. Use the Groove Delay to create tempo-
synced delay patterns ranging from simple subdivision taps to intricate evolving grooves or granular effects.
The Groove Delay has the following parameters:
-
Grid Display This display shows the current value for each tap for either Level, Pan, Cutoff, Swing, or LFO, based on the selec-
ted view mode across a grid of beats. The current value for each tap is color-coded and can be edited with the mouse directly
within the display.
-
Filter Controls Click this to show/hide the bottom area of the Groove Delay. This is where the Filter settings and Cutoff LFO
Amount controls are located.
-
Level, Pan, Cutoff, Swing, LFO Click on these buttons to display and edit the respective parameter for each tap in the Grid dis-
play.
-
Level Adjusts the output level and timing for each tap.
-
Pan Adjusts the pan and timing for each tap.
-
Cutoff Adjusts the filter cutoff frequency for each tap.
Delay

-
Swing Adjusts the Groove parameter for all taps that fall on off-beat positions between straight and dotted values, while
simultaneously adjusting Tap 4 and possibly Tap 2 levels (for all on- or off-beat positions). Helps achieve “swing”
grooves.
-
LFO Adjusts the Cutoff LFO Amount for each tap.
Beatlength
Select one of the note icons to adjust the Grid subdivisions by note value. Options range from 1/2 to 1/64.
Tap Parameters
-
Beat Position Adjusts the delay length for the currently select tap, in beats. Variable from one beat to two bars. The number of
positions within a bar is determined by the Beatlength: when set to 1/2 Beats, only 4 positions exist; when set to 1/32 or 1/64, 64
positions exist.
-
Tap Groove Adjusts the delay time relative to the Beat setting as a percentage. Variable from Triolic (= 66.67%, the last note of
the previous triplet) to Dotted (= 150%).
-
Tap Feedback Adjusts the amount of signal fed back into the delay effect.
-
Tap Output Level Adjusts the level of the currently selected tap as a percentage of the input level. Variable from 0 to 100%.
-
Tap Output Pan Adjusts the pan of the currently selected tap. Variable from Left to Center to Right.
Global
-
Feedback
-
Dry/Wet Adjusts the mix of processed signal with the original dry signal. Variable from 0 to 99%. A value of 100% could
cause runaway feedback, so that value cannot be reached.
-
Mix
-
Effect Depth Adjusts the mix of processed signal with the original dry signal. Variable from 0 to 100%.
-
Lock Locks the Effect Depth control position in place.
Filter Controls
The following controls become available when the Filter Controls button above the display is engaged.
-
Filter Click on the [Filter] button to engage the filter for the currently selected tap.
-
Type Mix Drag the red dot around the X/Y grid to adjust the character of the filter (X axis: low-pass to high-pass; Y axis: band-
pass to peak).
-
Cutoff/Reso. These controls adjust the cutoff frequency and resonance of the filter.
-
Cutoff LFO Amount Drag the horizontal fader to adjust the relative amount that the Cutoff Mod LFO can affect the cutoff setting
for the filter. Variable from -1 to 1. (Negative values differ from positive only in phase.)
-
Cutoff LFO The Cutoff LFO is a modulation source that can affect the cutoff value of the filter for each tap, depending on each
tap’s Cutoff LFO Amount setting.
-
LFO Speed-[Beats/Frequency] Adjusts the speed of the LFO. Beats variable from 4/1 to 1/64 with triplet and dotted
time variants. Frequency variable from 0.10 Hz to 30 Hz.
-
Sync Click to engage Cutoff LFO sync. This enables LFO speed adjustment in beats (synced to Song position).
Delay

Surround Delay
The Surround Delay is an eight-Tap, tempo-synced delay with surround panning per-Tap and a variable beat grid. Based on the classic
Studio One Groove Delay, Surround Delay lets you create tempo-synced delay patterns that echo all across the surround spectrum—
including vertically!
The Surround Delay has the following parameters:
Surround display (top left)
Each bubble in the Position Display represents the surround position of a Tap in the delay chain.
-
Click on any one of the bubbles to display and edit the respective parameter for each Tap in the Grid display.
-
Click and drag the bubbles to place their panning position in the surround image.
-
Double click to mute/unmute the chosen bubble.
Hint: these indicator directions, as well as Level and Elevation, are all automatable. Go nuts.
Grid Display (top right) This display shows the current value for each Tap for either Level, Direction, or Elevation, based on the selected
view across a grid of beats. The current value for each Tap is color-coded and can be edited with the mouse directly within the display.
Grid Display Views include:
-
Level Click and drag the nodes vertically to adjust the output level and timing for each Tap.
-
Direction Click and drag the nodes vertically to adjust the horizontal surround location for each Tap.
-
Elevation Click and drag the nodes vertically to adjust the vertical surround location for each Tap.
In all Grid Display Views, clicking and dragging the nodes horizontally will adjust the Tap’s placement in time across the grid.
Beneath the Grid Display are the Tap controls. These settings can be adjusted for each Tap individually.
-
Tap Selectors Click the Tap 1-Tap 8 button to choose the Tap you wish to configure. Click the bubble icon inside the Tap
Selector to toggle Bypass status for the desired Tap.
-
Position Adjusts the delay length for the currently selected Tap. If Sync is activated, the delay length is measured in beats, vari-
able from one beat to two bars. The number of positions within a bar is determined by the Beats control: when set to 1/2 Beats,
only 4 positions exist; when set to 1/32 or 1/64, 64 positions exist.
-
Fine Adjusts the Beat Position with a finer degree of control.
-
Feedback Adjusts the amount of signal fed back into the delay effect for the selected Tap.
-
Level Adjusts the level of the currently selected Tap as a percentage of the input level. Variable from 0 to 100%.
Delay

-
Direction Adjusts the direction of the currently selected Tap.
-
Elevation Adjusts the height of the currently selected Tap.
Time controls (lower left)
-
Sync Mode Optional Sync mode for Time.
-
Free results in time expressed in milliseconds, independent of Studio One’s Tempo setting.
-
Sync results in time expressed by the Beats control and node placement on the Grid, synced to Studio One’s Tempo.
-
Modulation Controls
-
Amount Adjusts the depth of modulation applied to the Taps.
-
Speed Adjusts the modulation speed.
EQ (lower center)
-
Low Cut Filters frequencies below this value from the delayed signal. Variable from Off to 20 Hz to 18 kHz. Filter is 6 dB per
octave.
-
High Cut Filters frequencies above this value from the delayed signal. Variable from 20 Hz to 18 kHz. Filter is 6 dB per octave.
Global (lower right)
-
Feedback Feedback Percentage of delayed signal added back into the delay input. Variable from 0 to 99%.
-
Drive Adjusts the amount of saturation applied to each Tap.
-
Size Adjusts the size of each Tap in the surround image.
-
Mix Adjusts the mix of processed signal with the original dry signal. Variable from 0 to 100%.
-
Lock Icon Locks the Mix control position in place.
Distortion
Distortion effects focus on the creation of a range of audio clipping artifacts that can add character and attitude to sounds—or destroy
them completely. Studio One includes the following distortion-oriented processors:
Distortion

Ampire
Ampire is a powerful and versatile collection of guitar- and bass-amplifier models based on our proprietary State Space Modeling tech-
nology, with precise emulation of every component in the signal path. Convolution-based speaker cabinets and microphones play a vital
role, with variable mic positioning and phase. Signals can be processed pre- and/or post-amplifier by a bevy of effect stompboxes, some
of which employ State Space Modeling of their components. Use Ampire with guitars, basses, or any audio signal to create spot-on emu-
lation of guitar amps and cabinets and a rougher, harmonically-enriched sound.
The Ampire window is divided into four main sections:
-
Toolbar This runs along the top of the Ampire window, and provides the basic functions such as input / output levels, window
configuration, amp / cabinet selectors, and access to the microphone settings and a tuner.
-
Gallery The first section under the toolbar allows visual selection and display of the amps and cabinets models. It can be hidden
to reduce the overall size of the Ampire window.
-
Edit section The next section houses the controls for the selected amplifier model. It is always visible.
-
Pedalboard The bottom of the Ampire window is home to the Pedalboard, which allows you to add up to eight effects units to
the signal path and configure them however you want. These effects units are also known as Stomps.
Note that the Pedalboard is also available as an independent effects plug-in, which can also contain up to eight Stomps. More
about that later.
Each of these four sections is described in the following paragraphs.
Toolbar
The gateway to Ampire is the toolbar, where component selections are made and basic levels are set. Viewing options are available here
too, along with access to a handy tuner and other features.
-
Input Level Trim the input level directly at Ampire’s input to pull up weak instrument signals or to attenuate loud, processed sig-
nals. With a good input level, the signal is in the optimal range for dynamic distortion within Ampire. Variable from -12 dB to 24
dB. This parameter is not saved with each preset. It stays at a static setting for each instance of Ampire until you change it.
Distortion

-
Show / Hide Views This button (
) hides or reveals different sections of the Ampire window so you only see what you
want. Click above the button to toggle the Stage view; click below the button to toggle the Stomps view.
-
Amplifier Model Select an amplifier model by clicking on the Amp name in the toolbar and choosing an amplifier from the
Gallery. Move the cursor over the Gallery images to read a brief description of each amp. You can also use the up / down arrows
in the toolbar or on the left side of the Stage view to select an adjacent amplifier.
Changing the amp model changes the characteristics of the entire amplifier, including preamp and power amp distortion and
amplification, the differences between channels 1, 2, and 3 (where applicable), and tone stack behavior. Select "None" if you
want to bypass the amp head and run the signal directly through the cabinet.
-
Cabinet Model Click the Cabinet Model selection box to choose a cabinet from the Gallery. Move the cursor over the Gallery
images to read a brief description of each cabinet. You can also use the up / down arrows in the toolbar or on the left side of the
Stage view to select an adjacent amplifier. If you want to take the direct output of the amp head, choose the Bypass icon (
).
You can also drag and drop Impulse Response files into the Mic A, B, and C slots for the User Cabinet (see IR Maker). WAV and
AIFF files are supported.
-
Mic Edit Controls Click the Mic Edit Controls button to access the settings for the microphones that were used to capture the
sound of each cabinet.
-
Mic Mix Link Activate this button to link the microphone channel levels. When linked, moving one fader adjusts all
three proportionately, for a combined level of 100%. If a mic level is at 0, moving the other faders adjusts only those
channels. Disengage this button for independent control of each microphone level.
-
Mic A/B/C Mix Adjust these faders to achieve the desired level for each mic. When linked (as described above), adjust-
ing one adjusts all three.
-
Mic Mute Each channel has a Mute button. Use the appropriate button to mute only that microphone. Note that this
does not affect the Link status of that channel.
-
Mic Polarity Each channel has a Polarity switch. Use the appropriate button to invert the phase of that microphone.
-
Mic B/C Delay These controls simulate moving Mic B and Mic C further from the cabinet. Variable from 0 to 2.9ms.
-
Show / Hide Tuner This button reveals or hides the Tuner window.
-
Frequency/Difference When a pitched input signal is detected, several things happen:
-
The name and octave number of the nearest fundamental pitch is shown below the tuning meter (i.e., D#2), with arrows
on either side to indicate whether the note is flat, sharp, or in tune (both arrows lit)
-
Frequency The fundamental frequency of the input signal is displayed in Hertz (Hz)
-
Difference The amount of deviation from center is shown as a positive number (sharp) or a negative number (flat).
-
Strobe Click this switch to toggle the tuner between the standard and strobe tuner views.
-
Calibration Click and drag the knob to set the tuning reference frequency, or enter a value manually in the number
field. [Ctrl]/[Cmd]-click to reset the value to A=440.00.
-
Mute Activate the Mute switch to defeat the input signal temporarily while the instrument is being tuned. The signal is
restored when the Tuner window is hidden. However, if the Ampire Editor window is closed while the Mute switch is still
engaged, the input signal is not restored.
-
Output Level Distortion and amplifier emulation may result in massive level changes. Use Output Level to adjust the signal to
normal levels. Unlike the Input Level setting, the Output Level value is saved with each preset. Variable from -24 dB to 12 dB.
State Space Amplifier Models
PreSonus used our State Space Modeling technology to perform a component-level analysis of every circuit in these sought-after amp-
lifiers. This enables Ampire to recreate the dynamic behavior and non-linearities that are critical to the distinctive tone and character of
tube and semiconductor-based analog circuits.
Distortion

After an amplifier is selected its controls appear in the middle of the Ampire window (the Edit section). Here's a description of each con-
trol.
MCM 800
-
Tone Controls Presence controls the amount of negative feedback; increasing the value changes the high frequencies and
harmonics. Bass, Middle, and Treble are basic tone controls for their respective frequency ranges.
-
Gain Controls Master Volume controls the final output volume. Pre-Amp Volume controls the level of the input signal before
it enters the amplifier circuitry.
-
Sensitivity Click one of the connectors to route the signal into the High sensitivity input or the Low sensitivity input.
Dual Amplifier
The channels of the Dual Amplifier model are numbered from right to left. They have similar EQ and tone controls, but each has different
gain and circuit characteristics.
-
Channel selector This knob selects channel 1, 2, or 3. You can also use the small selector buttons between the toggle switches
to select a channel. The channel indicators have different colors (green, orange, and red) to help you see which is active. The
green channel is "clean", while the orange and red channels are more distorted.
-
Main Power There are two options for the power supply characteristics: Spongy or Bold.
-
Tone Controls These are identical for channels 1-3. Bass, Mid, and Treble are basic tone controls for their respective fre-
quency ranges.
-
Gain Controls These are identical for channels 1-3. Presence controls the amount of negative feedback; increasing the value
changes the high frequencies and harmonics. Master controls the final output volume for the channel. Gain controls the pre-
amp input level.
-
Mode switch: Channel 1 Two positions: Clean and Pushed, each with different sound characteristics. Pushed has a boost, so
the tone controls contribute less to the sound of Channel 1 in that position.
-
Mode switch: Channels 2 and 3 Three positions: Raw, Vintage, and Modern. Each provides sound characteristics that were
modeled after different amplifiers from the same manufacturer.
-
Rectifier switch: All Channels Two positions: Diode and Tube. These determine the basic character of the selected channel,
which changes the output volume, the harmonic response, and the amount of headroom for that channel.
VC30
Distortion

-
Channel Inputs The VC30 has three channels: Vib-Trem, Normal, and Brilliant. Each channel has two inputs on the front
panel, arranged vertically. The low-sensitivity inputs are on the top row, and the high-sensitivity inputs are on the bottom row.
Each channel corresponds to a section of controls on the right side. The active channel is determined by which input is used.
-
Vibrato The controls in this channel are used when one of the Vib-Trem inputs is connected. Use the Speed selector to choose
one of the three speeds. The Vib-Trem selector also has three settings (Vibrato, Off, or Tremolo). Adjust the level with the Vib-
Trem control in the Volume section.
-
Volume Adjust the gain of each channel with the corresponding control in the Volume section. Usually only one channel is act-
ive, depending on which input is connected. But when the Vib-Trem and Brilliant channels are "jumpered" as shown below, the
gain controls for both channels can be used to achieve the perfect blend.
-
Tone The Treble and Bass controls are dedicated to the Brilliant channel. The Cut control attenuates the high frequencies, and
is active for all three channels. 0% = no cut, 100% clockwise = maximum cut.
-
Vib-Trem > Brilliant The Vib-Trem and Brilliant channels can be patched together and used at the same time. To do this, click
input 2 of the Vib-Trem channel, then click it again and a patch cable appears between Vib-Trem input 1 and Brilliant input 2.
This shows that the connection has been made.
This "jumpered connection" sends the signal through both the Vib-Trem and Brilliant circuits, so you have the dirt and tone con-
trol from the Brilliant channel and the vibrato / tremolo effect from the Vib-Trem channel available. The relevant controls in each
channel can be used to modify and blend the two outputs.
Blackface Twin
This well-known amp has two channels (normal and vibrato). Each channel has two input jacks that differ in input volume, as well as a
Bright switch.
-
Normal Channel A simple channel with three EQ knobs and a Bright switch. The EQ knob range is from 1 (maximum cut) to 10
(maximum boost); 5 is neutral (no change). With Bright switched on, high frequencies can pass through the volume stage more
easily. The effect depends on the Volume setting; when the volume is low, the Bright switch makes a bigger difference.
-
Vibrato Channel The features are identical to the Normal Channel, with the addition of Reverb and Vibrato controls. The
Reverb knob controls the amount of spring reverb, with a setting of 1 shutting off the reverb. The Speed and Intensity knobs
control the "Vibrato" effect (it's actually tremolo), with a minimum to maximum range of 1 to 10. An Intensity setting of 1 shuts off
the Vibrato. The Reverb and the Vibrato Intensity can be toggled between their current value and "Off" by clicking below the
appropriate knob.
Distortion

Amp STV
This amplifier was designed for bass instruments. It has two independent channels, with two inputs per channel (Bright and Normal). The
difference between the Normal and Bright inputs is that the Bright input attenuates the low and mid frequencies.
-
Channel One Standard volume and boost/cut EQ controls (treble, midrange, bass), with a set of selector switches that influence
the results in each EQ range. Click the desired switch to change its setting.
-
ultra hi is a two-position switch: flat (0) or boost (+). It has a significant impact on the high frequencies, especially in
combination with the other tone controls.
-
mid frequency is a three-position switch: 220 Hz, 800 Hz, or 3000 Hz. This sets the center frequency of the midrange
EQ band.
-
ultra lo is a three-position switch: cut (-), flat (0), or boost (+). It has a significant impact on the low frequencies, espe-
cially in combination with the other tone controls.
-
Channel Two Identical to Channel One, only without the midrange controls.
Pedalboard and Stomp Boxes
The Ampire Pedalboard features a wide variety of Stomp Box effects, including distortion and modulation of all sorts. Up to eight Stomps
can be used at once and placed in any order you like (pre- or post-amplifier). Several have sync-to-tempo capabilities. You can even use
the same Stomp in several slots if you want.
For added flexibility, the Pedalboard is available as an independent effects plug-in inside the Browser/Effects/PreSonus folder. That way
you can use it as an insert or send effect on any Channel without needing to bypass the amplifier and cabinet models. You can even drag
a favorite Stomp between instances of Ampire and the Pedalboard, and vice versa, as long as there's an empty slot available.
Note that when used with Ampire, all Pedalboard effects are placed prior to the cabinets in the audio chain.
Now let's take a look at the row of buttons beneath the Stomps window. The numbered slots show the names of the selected Stomps in
the order they appear in the window above them. An unused slot has no name. Each slot has an on/off switch, and on the far left is one
switch to rule them all: it toggles the entire Pedalboard on and off.
Pre-/post amp placement
Notice the double blue line between two of the Stomp slots; that's the dividing line between pre- and post-amplifier effects. Click-drag the
blue line to place it between any two Stomps, or even before or after the entire Pedalboard. As it moves you'll see a vertical, silver switch
move to the same location in the Stomps window.
Mirrored actions
Many of the actions performed in the Stomps window are mirrored in the Stomps tray, and vice versa. For example:
Distortion

-
Click-drag the silver switch in the Stomps window and the blue line moves too.
-
Click-drag a Stomp to a new location and its numbered slot does the same below. Remember that this works both ways.
-
Toggle the foot switch of an effect in the Stomps window and the on/off switch in the Stomps tray does it too.
-
Hover over a number in the Stomp tray to identify that effect in the Stomps window. Hover over the top of a Stomp to see its num-
ber.
This is useful if you're using more than one instance of the same Stomp, for example, and you want to know which is which. It
also helps if the Stomps are not located directly above their position numbers in the Stomp tray. Some of them are fat in more
ways than one.
Add or remove a Stomp box
To insert a Stomp, right-click in an empty space in the Stomps window or in the Stomps tray. To remove a Stomp, right-click on the
Stomp itself or on its numbered slot below. Note that a right-click on a Stomp control opens the Macro/Automation menu instead.
Select a Stomp box
Click the name area of any slot in the Stomps tray to open the Gallery and select an effect for that slot. There are too many to fit in the
Gallery window, so be sure to scroll up or down if you don't see the one you're looking for at first.
Now let's take a tour of the parameters, Stomp-by-Stomp.
-
Bypass
-
This selection leaves the Stomp slot empty.
-
Big Fuzz
This is one of the PreSonus State-Space Modeling effects.
-
Volume Controls the level into the Tone circuit.
-
Tone Turn to the left to attenuate high frequencies; turn to the right for more treble, less bass. Tone control is post the
two clipping stages.
-
Sustain A pre-pre-amp stage into the Volume circuit. Adds sustain and fuzz.
-
Compressor
The compressor pedal reduces the dynamic range of your signal for additional shaping of your sound. With its two different
modes you can dial in the exact amount of sustain that you want.
-
Gain Sets the input gain to the compressor.
-
Peak Controls the amount of peak reduction. Higher peak settings result in more gain reduction and more compression.
-
Mode: limit / compress Toggles between two different dynamic ratios. When in limiter mode, peaks are limited more
aggressively.
-
Delay
-
Speed Adjusts the delay speed from 0.01 to 10 Hz.
-
Sync Engage this if you want to sync the delay speed to tempo.
-
Beats Selects a beat value for the synced delay speed.
-
LC Sets the frequency of the low-cut filter from 20 Hz to 1 kHz.
-
HC Sets the frequency of the high-cut filter from 1 kHz to 20 kHz.
Distortion

-
Feed Adjusts the amount of feedback from 0 to 100%.
-
Mix Adjusts the mix of the delayed signal with the original signal from 0 to 50%.
-
Equalizer
-
Guitar/Bass Selects the appropriate style, which adjusts the frequency values for each band of the graphic EQ.
-
Band Sliders Adjusts the level of each EQ band up or down to achieve the desired EQ setting. Click-drag across them
to set a quick curve.
-
Fat
This is one of the PreSonus State-Space Modeling effects.
-
Distortion Turn to the right to increase the amount of distortion.
-
Filter With this control fully to the left, the Filter is open and high frequencies can pass; fully to the right, the high fre-
quencies are attenuated. Tone control is post-Distortion.
-
Volume Controls the final output level.
-
Gate
The gate pedal completely removes unwanted noise in your signal. No more buzzing and humming in your signal chain! This
One-Knob model has the following control:
-
Threshold Adjusts the lower limit at which the Gate starts to work. Variable from -96 dB to 0 dB. All signals above the
threshold setting are passed through unaffected, whereas signals below the threshold are muted (e.g., pickup hum or
noise).
-
Modulation
-
Chorus/Flanger/Phaser Selects the type of modulation.
-
Chorus
-
Delay Adjusts the delay of the chorus signal from 2 to 20 ms.
-
Speed Adjusts the chorus speed from 0.01 to 10 Hz.
-
Width Adjusts depth of delay line modulation, from 0 to 100%.
-
Depth Adjusts the chorus depth from 0 to 100%.
-
Flanger
-
Delay Adjusts the delay of the flanged signal from .2 to 4 ms.
-
Speed Adjust the flanger speed from 0.01 to 10 Hz.
-
Sync Engage this if you want to sync the flanger speed to tempo.
-
Beats Selects a beat value for the synced flanger speed.
-
Feed Adjusts the amount of feedback from 0 to 100%.
-
Width Adjusts the flanger LFO width from 0 to 100%.
-
Depth Adjusts the flanger depth from 0 to 100%.
-
Phaser
-
Phase Adjusts the frequency of the phaser from 240 Hz to 8 kHz.
-
Speed Adjusts the speed of the phaser from 0.01 to 10 Hz.
-
Sync Engage this if you want to sync the phaser speed to tempo.
-
Beats Selects a beat value for the synced phaser speed.
-
Feed Adjusts the amount of feedback from 0 to 100%.
-
Width Adjusts the phaser LFO width from 0 to 100%.
-
Depth Adjusts the phaser depth from 0 to 100%.
-
MP Ninety
-
Speed Controls the phaser speed.
-
PAE Chorus 1
-
High/Low Selects the input sensitivity.
-
Level Control Adjusts the input level.
-
Chorus Intensity Controls the rate and depth of the Chorus effect for Chorus mode.
-
Vibrato Depth Controls the depth of the Vibrato effect for Vibrato mode.
Distortion

-
Vibrato Rate Controls the rate of the Vibrato effect for Vibrato mode.
-
Normal/Effect This foot switch toggles the effect on and off.
-
Mode: Vibrato/Chorus This foot switch toggles the effect between Vibrato and Chorus modes.
-
Pan
-
Speed Adjust the pan speed from 0.01 to 10 Hz.
-
Sync Engage this if you want to sync the pan speed to tempo.
-
Beats Selects a beat value for the synced pan speed.
-
Depth Adjusts the pan depth from 0 to 100%.
-
Reverb
-
Size This control affects several parameters to approximate an overall room size. It adjusts the size of the reverberated
signal from 0 to 100%, with lower percentages representing smaller rooms and therefore shorter reverb tails and higher
percentages representing larger rooms and longer tails.
-
Mix Adjusts the mix of the reverberated signal with the original signal from 0 to 50%.
-
LC Sets the frequency of the low-cut filter from 20 Hz to 1 kHz.
-
HC Sets the frequency of the high-cut filter from 1 kHz to 20 kHz.
-
Damp Adjusts the dampening of the reverberated signal from 0 to 100%.
-
Tremolo
-
Speed Adjusts the tremolo speed from 0.01 to 10 Hz.
-
Sync Engage this if you want to sync the tremolo speed to tempo.
-
Beats Selects a beat value for the synced tremolo speed.
-
Depth Adjusts the tremolo depth from 0 to 100%.
-
Tube Dreamer
This is one of the PreSonus State-Space Modeling effects.
-
Drive Turn to the right to increase the Drive amount.
-
Tone Turn to the left to attenuate high frequencies. The tone control is post-Drive.
-
Level Controls the final output stage.
-
Tube Driver
-
Amount Adjusts the amount of drive from 0 to 11.
-
Wah-Wah
-
Type Selection Box Selects the type of wah-wah desired.
-
Amount Adjusts the amount of the wah-wah effect from 0 to 100%, equivalent to rocking a traditional wah-wah pedal
forward and backward.
Bitcrusher
Perfect for audio abuse, Bitcrusher combines overdrive, bit-depth reduction, downsampling and clipping into a single plug-in. Bit depth
reduction and downsampling are both digital resolution-reduction techniques, but each has its own sonic effect. When used in com-
bination, they create a wide variety of tonal options.
The following parameters are available in Bitcrusher:
Distortion

Wreck
-
Bit Depth Lets you specify the level of Bit Depth reduction to apply, from 24-bit to 1-bit.
-
-
Dirt Enable this to introduce a high-frequency instability in the Bit Depth reduction effect. Good for creating aggressive
sounds.
-
Downsample Lets you specify the level of downsampling to apply.
-
-
Zero Enable this to emphasize the high-frequency ringing effects added by the downsampling process. When disabled,
a smoothing interpolation process is applied to the signal, lessening audible artifacts.
Color
-
Overdrive Lets you apply a warm distortion effect, ranging from clean to fuzzy.
-
Clip Lets you set the threshold for the signal clipping effect. At 0 the signal is unaffected, and at settings below 0 the signal is
clipped in your choice of the following ways:
-
-
Digital Standard digital clipping. Squarely clips the peaks of the waveform at the chosen threshold.
-
Overflow Inverts and offsets peaks at a faster interval.
-
Fold Introduces harmonics by inverting waveform peaks at the chosen threshold (and at zero).
Display The central waveform display shows a rough representation of the wave-shaping effects currently being applied.
-
Sine Click this to switch to a real-time view of the Bitcrusher audio output.
Global
-
Gain Adjusts Bitcrusher output gain. Variable from -24 dB to +24 dB.
-
-
Auto Enable this to set Gain automatically, to match the gain changes created by other Bitcrusher processors.
-
Mix Lets you blend between the dry (0%) and effected (100%) signals.
Red Light Distortion
Red Light Distortion is an analog-distortion emulator with several selectable distortion models.
Distortion

The following parameters are available in Red Light Distortion:
-
In Input gain to the distortion. Variable from -12 dB to 24 dB.
-
Distortion Only for Hard and Bad Tube types, this is the tube working-point adjustment (bias). Variable from 0 to 10.00.
-
Low Freq Filters frequencies below this value from the distorted signal. Variable from 20 Hz to 5 kHz, depending on the High
Freq setting.
-
High Freq Filters frequencies above this value from the distorted signal. Variable from 800 Hz to 16 kHz.
-
Drive Amplification during overdrive. Variable from 0 to 11; drive increases a lot between 10 and 11 for really distorted sounds.
-
Out Adjust the output gain of Red Light Distortion. Variable from -12 dB to 24 dB.
-
Stages Number of overdrive stages used serially in the signal path (including filters). Select from 1, 2, or 3 with the horizontal
fader.
-
Type Select the type of distortion emulation by clicking on the display and selecting Soft Tube, Hard Tube, Bad Tube, Tran-
sistor, Fuzz, or OpAmp from the list.
-
Mix Lets you set a mix between the wet (effected) and dry (unaffected) signals running through the plug-in, allowing for parallel
processing effects.
Dynamics
Dynamics processing is a key aspect of mixing and mastering. Studio One features very high-quality dynamics processors that give you
complete control. The following sections contain fundamental details on the shaping of audio dynamics, as well as the functions of Studio
One’s dynamics processors.
Compressor
The Compressor is a full-featured, RMS-based mono/stereo compression processor with internal and external sidechains. Use this
effect to reduce the dynamic range (signal peaks) of any signal.
The following parameters are available in the Compressor:
-
Threshold Adjusts the lower limit for compression. Variable from -48 dB to 0 dB.
-
Ratio Adjusts compression range. Variable from 1:1 (no compression) to 20:1.
-
Knee Adjusts the soft-knee width. (Width refers to the distance from the threshold to the end of the soft knee.) Variable from 0.1
dB to 20 dB.
-
Look Ahead Click to engage/disengage 2 ms Look Ahead function.
Dynamics

-
Channel Link Click to engage/disengage Stereo Link. Stereo Link sums a stereo input signal to mono for signal-power detec-
tion.
-
Display
-
Input Level Displays input level + RMS.
-
Reduction Displays level of compressor attenuation (-60 dB to +3 dB) and the maximum reduction amount. The
highest peak is held until surpassed by another peak or until parameters are adjusted or clicked on.
-
Compression Curve Click the handles in the display to control the curve settings.
-
Ratio Click the top right handle to adjust the Ratio when Auto-Gain is not engaged.
-
Threshold Click the middle handle to adjust the Threshold when Auto-Gain is not engaged.
-
Knee Use the mouse wheel while floating the cursor over the middle handle to adjust the Knee when Auto-
Gain is not engaged. If you don’t have a mouse wheel, use the Knee knob.
-
Gain Click the bottom left handle to adjust the Makeup gain when Auto-Gain is not engaged.
-
Auto-Gain Engaged Click on the middle handle to adjust the Threshold and Ratio parameters. The X axis con-
trols the Ratio, and the Y axis controls the Threshold. Hover over the handle to control the Knee, as described
above.
-
Output Level Displays output level + RMS.
-
Envelope
-
-
Attack Adjusts attack time for dynamics processing. Variable from 0.1 ms to 400 ms.
-
Release Adjusts release time for dynamics processing. Variable from 1 ms to 2s.
-
Auto Engage Auto to automatically set varying attack and release settings based on signal content.
-
Adaptive Engage to automatically vary attack and release times in order to avoid pumping. This results in less-aggress-
ive but smoother compression.
-
Gain Attenuates or amplifies the compressor input. Variable from -12 dB to 24 dB.
-
Input Gain The name of the Gain control when the Compressor is in Int. Sidechain mode.
-
Side Gain The name of the Gain control when the Compressor is in Ext. Sidechain mode.
-
Makeup When Auto is not engaged, this allows you to control the output gain manually. It is variable from 0 dB to 48 dB.
-
Auto Engage to automatically fix the 0 dB input level to the 0 dB output level (guarantees that a 0 dB input level results
in a 0 dB output level). This button cannot be activated when in Ext. Sidechain mode or when the Filter is engaged.
-
Sidechain (internal)
-
Filter Click to activate internal sidechain filtering (for frequency-dependent gating). Uses 48 dB/octave filters.
-
Listen Click to listen to the filtered control signal of the internal sidechain. Helps find specific target frequency for control
signal when de-essing, transient damping, etc.
-
Low Cut/High Cut Frequency selection for internal sidechain filters. Low Cut variable from Off to 20 Hz to 16 kHz; High
Cut variable from 20 Hz to 16 kHz to Off.
-
Swap Click to swap the frequencies used for Low Cut and High Cut.
-
Sidechain (external) Engage by clicking the [Sidechain] button at the top of the effect window to allow other sources to control
the Compressor. When engaged, you can use the Filter, Listen, Low/High Cut, and Swap controls as described above in the
Sidechain (internal) section.
-
Sources Click to display a list of external sidechain channel sources. A checked box indicates the current source. Mul-
tiple selections can be made.
-
Mix This parameter lets you set a mix between the wet (effected) and dry (unaffected) signals running through the plug-in, allow-
ing for parallel processing effects.
De-Esser
Dynamics

The De-Esser is a full-featured, dynamics processor used to selectively reduce the sibilance (S-sounds) of recordings by selectively com-
pressing only the problematic frequencies. It’s particularly useful for layered vocal recordings, where undesirable sibilance can add up
across multiple tracks — and it’s also a suitable choice for taming harsh frequencies in high-hats and cymbals.
The following parameters are available in the De-Esser:
-
Frequency - Adjusts the center frequency used to target sibilant sounds for reduction. Variable from 2 kHz - 12 kHz.
-
Listen - Similar to the key-listen function on the Compressor. When activated, it allows you to listen to the frequencies being tar-
geted for reduction.
-
Solo - Activate to hear only the signal being reduced by the De-Esser.
-
Meter - This combination meter displays both the input level (blue) and the amount of gain reduction (yellow.)
-
S-Reduction - Controls the threshold point at which the De-Esser begins to reduce the selected frequency. Variable from 0 dB
to -60 dB.
-
Shape
-
Narrow - 3-band mode. Compression is only applied to a narrow band. Signal below and above the active band remain
untouched.
-
Wide - 2-band mode. Compression is applied to the entire high-frequency signal, while the lower-frequency range
remains untouched.
-
Range
-
Full - Compression may cover the entire dynamic range of a signal.
-
Gentle - Prevents the compression from reducing the signal beyond -6dB.
Expander
Dynamics

Expander is a fully variable downward expander with range control. It features sidechain capability, including an internal sidechain filter
with variable low-cut and high-cut. Expanders increase the dynamic range of a signal such that low-level signals are attenuated while the
louder portions are neither attenuated nor amplified. This is effectively the opposite of compression. Use Expander to decrease the levels
of unwanted noise or bleed from other sources in the desired signal or to restore dynamic range to a compressed signal.
The following parameters are available for the Expander:
-
Threshold Adjusts the maximum amplitude at which processing occurs. Variable from -60 dB to 0 dB.
-
Ratio Adjust the ratio of the Expander. Variable from 1:1 to 1:20.
-
Display
-
Reduction Meter Displays the maximum reduction amount (-72 dB to +0 dB).
-
Expansion Curve Click the handles in the display to control the curve settings.
-
Threshold Drag the top handle to adjust the Threshold when Auto-Gain is not engaged.
-
Ratio/Range Drag the bottom handle to adjust the Ratio and Range simultaneously.
-
Look Ahead Click to engage/disengage 2 ms Look Ahead function.
-
Reduction Range Adjust the maximum amount of attenuation applied to the signal. Variable from -72 dB to 0 dB.
-
Envelope
-
-
Attack Adjusts attack time for dynamics processing, reaction speed to falling signal. Variable from 0.1 ms to 500 ms.
-
Release Adjusts release time for dynamics processing, reaction speed to rising signal. Variable from 50 ms to 2 s.
-
Sidechain (internal)
-
Filter Click to activate internal sidechain filtering (for frequency-dependent gating). Uses 48 dB/octave filters.
-
Listen Click to listen to the filtered control signal of the internal sidechain. This helps find a specific target frequency for
the control signal when de-essing, transient damping, etc.
-
Low Cut/High Cut Frequency selection for internal sidechain filters. Low Cut variable from Off to 20 Hz to 16 kHz; High
Cut variable from 20 Hz to 16 kHz to Off.
-
Swap Click to swap the frequencies used for Low Cut and High Cut.
-
Sidechain (external) Engage by clicking the [Sidechain] button at the top of the effect window to allow other sources to control
the Expander. When engaged, you can use the Filter, Listen, Low/High Cut, and Swap controls as described above in the Side-
chain (internal) section.
-
Sources Click to display a list of external sidechain channel sources. A checked box indicates the current source. Mul-
tiple selections can be made.
-
Ducking Engage this button at the bottom of the effect window to invert the external sidechain source signal.
Dynamics

Gate
Gate is a noise-gate processor with range control. It features a large display with grid lines to indicate the Threshold setting relative to 0
dB.
It also has sidechain capability with an internal sidechain filter that includes variable low cut and high cut. Gating is an extreme form of
expansion that severely attenuates the processed signal or silences it entirely. Use Gate to eliminate unwanted noise or low levels in any
Track or to creatively control the level of a given Track using another Track via the sidechain.
The following parameters are available for the Gate:
-
Threshold Adjusts the signal level threshold at which the Gate switches between closed and open. You can also click and drag
the dot in the Gate display to adjust the Threshold value. Variable from -60 dB to 0 dB.
-
Reduction Range Adjusts the maximum amount of reduction. Variable from -72 dB to 0 dB.
-
Display
-
Reduction Meter Displays the amount of reduction, from -72 dB to 0 dB.
-
Gate Curve Click and drag the handle in the display to adjust the Threshold.
-
Look Ahead Click to engage/disengage the 2 ms Look Ahead function.
-
Envelope
-
Attack Adjusts the amount of time it takes for the gate to open and let signal through. Variable from 0.05 ms to 500 ms.
-
Hold Adjusts the amount of time the gate is held open once the signal has dropped below the Threshold setting. Vari-
able from 1 ms to 1 s.
-
Release Adjusts the amount of time it takes for the gate to close after the Hold period. Variable from 50 ms to 2 s.
-
Trigger
-
Send Trigger Notes Click to engage sending a trigger when the gate opens. Select the gate as an input on any Instru-
ment Track.
-
Note Click the field and enter a note name, or click-drag the field to adjust the MIDI note to send.
-
Velo Click the field and enter a number, or click-drag the field to adjust the MIDI velocity value to send.
-
Sidechain (internal)
-
Filter Click to activate internal sidechain filtering (for frequency-dependent gating). Uses 48 dB/octave filters.
-
Listen Click to listen to the filtered control signal of the internal sidechain. Helps find specific target frequency for control
signal when removing narrow-band noise.
Dynamics

-
Low Cut/High Cut Frequency selection for internal sidechain filters. Low Cut variable from Off to 20 Hz to 16 kHz; High
Cut variable from 20 Hz to 16 kHz to Off.
-
Swap Click to swap the frequencies used for Low Cut and High Cut.
-
Sidechain (external) Engage by clicking the [Sidechain] button at the top of the effect window to allow other sources to control
the gate. When engaged, you can use the Filter, Listen, Low/High Cut, and Swap controls as described above in the Sidechain
section.
-
Sources Click to display a list of external sidechain channel sources. A checked box indicates the current source. Mul-
tiple selections can be made.
-
Ducking Engage this button at the bottom of the effect window to invert the external sidechain source signal.
Limiter²
Limiter² is a brickwall limiting processor with optional K-System Metering. Use it to prevent your output signal from clipping or to max-
imize signals with very dynamic peaks.
The following parameters are available for Limiter²:
-
Input
-
Gain Adjusts the input level into the limiter. Variable from 0 dB to 18 dB.
-
Ceiling Adjusts the maximum output of the limiter. Variable from -12 dB to 0 dB.
-
Threshold is relative to Ceiling. Variable from Ceiling value to 12 dB below Ceiling value. Automatic make-up gain is
applied as the Threshold is lowered.
-
Mode Toggles between Modes A and B. With Mode A the limiter is always clean with no distortion. However, in Mode A
the limiter response is a bit slower. With Mode B the limiter reacts more quickly to the signal, but depending on the set-
tings a small amount of distortion may occur.
-
Envelope
-
Attack Select Fast, Normal, or Slow attack for the limiter.
-
Release Adjust the amount of time it takes for the limiter to stop processing once the input level falls below the Ceiling
setting. Variable from 1 ms to 3 s.
-
Metering
-
Peak/RMS Click to engage Peak/RMS metering.
-
K-14, K-20, K-12 Click one of these to select a K-System metering option.
-
Reduction Displays the amount of signal reduction, from -36 dB to 0 dB.
Dynamics

-
True Peak Often the sample that represents the "peak" of a waveform is not truly at the peak, but rather just near it. This can cre-
ate inter-sample peaks, in which the true outputted amplitude can surge past the limiter threshold. Enable True Peak to detect
and protect from these inter-sample peaks.
-
Soft Clip Reduces square wave clipping characteristics when the limiter is clipped. Click to engage Soft Clip.
-
Sidechain Engage by clicking the [Sidechain] button at the top of the effect window to allow other sources to control the limiter.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Multiple
selections can be made.
Pro EQ3
Pro EQ3 is an eight-band parametric equalizer1 with optional spectrum metering; variable low-cut, high-cut, low-frequency, and high-fre-
quency multimode filters; band soloing; dynamic mode controls; and an optional Auto-Gain output gain setting. Use Pro EQ3 on any
mono or stereo Track to accurately apply highly musical equalization to any signal.
The following parameters are available for Pro EQ3:
-
Input Meter Peak/RMS meter shows the unmodified input signal level. The RMS level is represented by a white horizontal line.
-
Display Click-and-drag frequency-band handles in the display to edit Gain (up/down) and Freq (left/right) parameters. If you
click on a handle, the mouse wheel edits the Q. (If you don’t have a mouse wheel, adjust the desired Q knob or type in a value
below the knob.) Note that LLC frequency must be selected with the buttons. Holding [CTRL/CMD] before clicking and dragging
a handle will allow you to adjust the dynamics Range by using the mouse.
-
Band Controls Click to show/hide the bottom half of the Pro EQ3 window. This is where all controls, buttons, and options for
each EQ band are located.
-
Dynamics Click to show/hide the Dynamics controls (Thresh/Range) for all frequency bands.
1A filter or group of filters that adjusts the volume level of a frequency, or range of frequencies, within an audio signal. Studio One includes the Pro EQ native
effect.
Pro EQ3

-
Level Range Click this field to select one of three level range options for the Pro EQ3 display: 6 dB, 12 dB, or 24 dB. This affects
the vertical scale within the display only; it does not affect the audio output.
-
Show Curves Click to display all EQ curves or only their combined curve, which is white. When the individual curves are hidden
you can hover over a band-handle to view its curve, and as any band is adjusted its curve is displayed temporarily.
-
Spectrum Display Type Click this field to select one of four output-spectrum metering modes: Third Octave, 12th Octave, FFT
Curve, or Waterfall. Select None to deactivate spectrum metering.
-
The bands in the 12th Octave meter correspond to the 12 notes in each octave on a piano keyboard. A keyboard
graphic below the spectrum display helps identify the pitch or note value of a given signal.
-
A second signal can be routed into the spectrum display using the included Sidechain input, for comparison.
-
The Spectrum display is fixed at 20 Hz to 20 kHz and -24 dB to 24 dB.
-
Sidechain Spectrum Peak Hold The snowflake button is only available for the Sidechain input when the FFT Curve is selec-
ted. When engaged, the highest peaks of the sidechain input spectrum are held indefinitely. To clear or release the peak curve,
click the snowflake button again.
-
High Quality Click to engage High Quality mode, allowing more accurate equalization. This is achieved using 2x oversampling
and requires more computer processing power. Note that when High Quality is enabled, due to oversampling, the signal is
slightly altered, even when all controls are set to neutral settings.
-
Sidechain Toggle on to use the spectrum analyzer in Pro EQ3 to display the characteristics of another Channel (routed in using
a send to Pro EQ3's Sidechain input). This can come in handy for comparing the frequency makeup of two channels you're try-
ing to match or balance against one another.
With Sidechain mode on, Pro EQ3’s frequency bands can employ Dynamic Mode, creating reactive EQ adjustments based on
the Input from the Sidechain source. Both Sidechain and at least one frequency band’s Dynamic Mode must be active to use this
functionality; it’s covered in further detail below.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Mul-
tiple selections can be made.
-
Bands Click Activate button to engage/disengage each band.
-
LLC Phase-linear Low-cut filter.
-
80 Hz, 50 Hz, 20 Hz Select frequency at which filter cut begins.
-
Soft When engaged, this band has a 12 dB per octave slope. When disengaged, the slope is 24 dB per octave.
This affects the shape of the filter curve.
Note: High-quality phase-linear filters like the LLC band are CPU-intensive and should be used with caution. If CPU
load is an issue, try using a conventional low cut filter instead. Another option is to render the insert FX using Track
Transform, which preserves the FX settings in case changes are needed later. Find this at Track/Transform, or [Right]/
[Ctrl]-click the Track in the Track List and select Transform to Rendered Audio.
-
LC, HC Low-cut and high-cut filters.
-
Freq Adjust point at which filter cut begins.
-
Slope Select from 6, 12, 24, 36, and 48 dB per octave. This affects the shape of the filter curve.
-
LF, HF Selectable low-frequency and high-frequency, shelf or peaking filters.
-
Q Adjust the Q of the frequency band. Q = the ratio of center frequency to bandwidth. When the center fre-
quency is constant, Q is inversely proportional to bandwidth (i.e., higher Q = narrower bandwidth).
-
Gain Attenuate/amplify frequency band.
-
Filter Mode Select from Peaking and Shelf, with 6, 12, or 24 dB per octave slope.
-
Solo Click to solo the currently-selected active band. LF and HF band soloing respects the bands’ peak/shelf
setting.
-
Dynamic Mode is supported on LF, LMF, MF, HMF, and HF bands. When engaged, the selected band’s level adjust-
ments will be triggered dynamically as the inbound signal surpasses the amplitude threshold.
-
Threshold Set the signal level at which the dynamic adjustment will trigger. Variable from 0 to -90 dB.
-
Amplitude Set the amount of dynamic adjustment applied. Variable from -24 to +24 dB.
-
Monitor the small reduction meters for a visual indication of the amount of reduction applied per band.
-
Freq Adjust the center frequency of the band.
Pro EQ3

-
LMF, MF, HMF Peaking filters.
-
Q Adjust the Q (center-frequency:bandwidth) of the frequency band.
-
Gain Attenuate/amplify frequency band.
-
Freq Adjust the band center frequency.
-
Auto Click to engage Auto-Gain, which adjusts Pro EQ² output level to match the original input-signal power (guarantees a 0 dB
input signal equals a 0 dB output signal).
-
Output Meter Peak/RMS meter; RMS level is represented by a white horizontal line.
Mix Engine FX (Studio One Professional Only)
The CTC-1 Mix Engine Effect operating in “Classic” mode.
Mix Engine FX are a unique category of Native Effects within Studio One. Rather than being applied to a single Channel or Event like
more typical plug-ins like Compressor or Pro EQ, Mix Engine FX can be applied to a Bus to cross-process multiple channels sim-
ultaneously—using only a single plug-in instance. The Mix Engine FX will then cross-apply to all of the Channels that flow into the Bus.
Mix Engine FX allow for robust emulation of vintage console characteristics like Crosstalk. In the analog realm, channels could bleed into
one another laterally across a console—much unlike a modern digital console. It’s this sort of cross-channel interaction that makes Mix
Engine FX special, allowing for more analog-style “glue” to bind your mixes together.
Furthermore, Mix Engine FX leverage PreSonus’ proprietary State Space Modeling technology, which has allowed us to digitally re-cre-
ate the sonic behavior of analog circuits on a per-component basis—including specific tolerances and nonlinearities. Thanks to State
Space Modeling, we’ve been able to create incredibly authentic-sounding digital models of venerated analog console behavior including:
drive, crosstalk, noise, saturation, and more!
It’s as true to analog as digital can get.
Adding a single Mix Engine FX plug-in to the Main Out of Studio One is the equivalent of adding multiple instances of the same plug-in to
all of the channel inserts, as well as the bus insert.
Note that Mix Engine FX are intended for use on Songs in the stereo 2-channel format. Mix Engine FX applied to multichannel songs will
render their processing in the Left and Right channels only.
Mix Engine FX (Studio One Professional Only)

Mix Engine FX plug-ins include a Mix Processor and a Sum Processor inside a single plug-in.
Controls common to most Mix Engine FX
While the following controls are available on most Mix Engine FX plug-ins, some—like those included in Retro Mix Legends, for
example—also have some of their own specific controls. See the individual plug-in manuals for these products for details on those fea-
tures.
Drive: The Drive stages in Mix Engine Effects faithfully recreate the characteristic dynamic behavior of the input preamps of the modeled
hardware. Each plug-in’s Drive stage is independently modeled, so expect Drive to behave differently depending on the Mix Engine
Effect you’re using.
Typically, Increasing the Drive amount first adds subtle harmonics to the signal, then goes into saturation or analog distortion when the
amount increases above a certain level. The character and sonic quality of Drive varies significantly between each plug-in, and the vari-
able Input Gain also affects the amount of Drive on a per-channel basis.
Pro Tip: Use Studio One’s Input Controls—available via the Console options menu (wrench icon on the top left of the Console)—to
adjust the amount of gain inbound to the Drive stage without manipulating your Channel faders!
Mix Engine FX (Studio One Professional Only)

Boost. With Boost engaged, 18dB of gain are added to all signals routed into Mix Engine FX. This helps with compensating for low
recording levels. An already “hot” signal won’t require additional gain, but for those recording by the rule of “-18dB ceiling” will benefit
from the additional input gain available.
Noise: Inherent signal noise plays an important role in defining the sonic character of an analog console. It adds to the perception of a
mix that sounds like it’s glued together. The noise of each console modeled as a Mix Engine Effect was State-Space Modeled indi-
vidually, so expect them to sound and behave differently from one another.
In fact, just as in the real hardware, the modeled analog noise isn’t just different for every Mix Engine Effect plug-in—it’s actually different
on every channel! Add a small amount of noise to any mix and it will give the overall sound a more analog character.
Noise Gate: For songs that have a fade at the end, activate the Noise Gate to fade out the noise automatically, avoiding any unwanted
noise tails.
Additionally, Noise Gate automatically creates a smooth fade to the end of the audio file when rendering. Unless the song ends with a
sharp cut, this option should always be enabled when rendering mixes or stems.
Crosstalk: Just like harmonic distortion and noise, crosstalk plays an important role in recreating the sound of an analog mixer.
Crosstalk is always present and also adds to the effect of a mix being “glued together.”
The crosstalk generated by Mix Engine FX spills over naturally into adjacent channels, with decreasing amounts the further a channel is
away from the source. Implementing this feature goes way beyond just developing a DSP plug-in. This goes deep into the DAW mix
engine and required extensive research and development, so we really hope you like it!
Character: On top of the three components already introduced here (Drive, Noise, Crosstalk), each analog console or summing mixer
has a unique sonic signature. Even without any equalization or compression applied to the signal, each console has its own sonic fin-
gerprint that makes it recognizable in the mix. The effect may be subtle but it’s always there.
Mix Engine FX not only capture the unique character of the consoles modeled, it also allows you to increase this character by a variable
amount. Even with the “Character” control at zero, the characteristic fingerprint of the modeled console is present in the signal chain.
Depending on
the style, mix, and source material it may be desired to have a higher amount of this unique signature, which in this case can be easily
achieved by adding more “Character” to the mix. This can be compared to running the signal through the same console multiple times.
Character is processed on the bus the Mix FX is inserted to.
Master Level Control: With multiple gain stages and variable routing (see below) it may be required to adjust the overall signal level
before leaving the plug-in. This is particularly important if further dynamics processing (compressors, limiters, noise gates) is applied to
the signal after a Mix Engine FX Plug-in. In this case, the Master level should be adjusted so no actual gain change is applied—unless
desired.
Gain Compensation: Adding high amounts of Drive to a signal can result in extreme gain offsets inside the console which in turn could
have a negative impact on subsequent plug-ins by offsetting dynamics threshold levels or creating distortion. Mix Engine FX are
equipped with special gain compensation algorithms to avoid this effect.
Two settings are available:
-
Bus: master gain compensation is applied inside the bus Mix Engine FX is inserted to, before any bus insert effects.
-
Channel: individual gain compensation is applied in each channel routed into the bus the Mix Engine FX is inserted to.
Channel is the default setting, and in most cases the preferred one. It helps to avoid distortion inside the channel, as well as unwanted
gain offsets on dynamics plug-ins
ECO Mode: Since Mix Engine FX plug-ins apply processing to many sources individually—every individual channel routed into the bus
the plug-in is inserted to—CPU load can easily get out of control, particularly with some heavy non-linear State Space Modeling applied!
When working on a large project with many channels, ECO mode comes to the rescue when CPU load gets too high.
Channel Volume Controls
When a Channel sits in a Bus affected by Console Shaper, the Channel's volume fader does double-duty as both a standard volume con-
trol and input gain control to the processes in Console Shaper. This means that you can safely crank the volume of affected channels,
and analog-style soft saturation will result, rather than undesirable digital "overs." This further works to lend the forgiving feel of an analog
console to your digital mixing experience.
Passthrough Mode
Most Mix Engine FX feature Passthrough Mode, which allows you to configure how the effect processes its multiple inbound signals, and
allows you to avoid redundant overprocessing of signals in more complex workflows that may involve multiple instances of Console
Shaper in the same project. For example, you may choose to use distinct Console Shaper instances and settings on both your drum bus
and Main bus. Passthrough Mode can help you better manage this.
Mix Engine FX (Studio One Professional Only)

-
With Passthough ON, all source Channels feeding get processed at the source, the busses don't.
-
With Passthrough OFF, only the Channels/Busses directly connected with the Main output get processed at the source.
The small orange/yellow indicators on Channels and Busses tell you which signals get processed at the source.
In this example, Passthrough is set to On. Mix Engine effects are active on the Main bus. The vocals are processed by Mix Engine FX at
their Channel source and the vocal bus is ignored.
Mix Engine FX (Studio One Professional Only)

In this example, Passthrough is set to Off. Mix Engine effects are active on the Main bus. The vocals are processed by Mix Engine FX at
the vocal bus and not the channel source.
Note that Crosstalk is applied to the same channels that get processed at the source. So it's either applied to the channels feeding to a
bus or the busses, but not both.
Console Shaper
Console Shaper is a Mix Engine Effect included in Studio One Professional plug-in that offers quick, easy-to-manage console emulation.
Quality analog mixing consoles are revered for their depth and richness of tone, forgiving gain staging, and for a number of charming
technical "flaws" that are unseen in digital mixers. These issues, such as circuitry self-noise and crosstalk (a low-level bleeding of signals
Mix Engine FX (Studio One Professional Only)

between a console's channels and busses) were once the bane of console designers. Ironically, they are now thought to contribute to the
euphonic nature of analog summing.
Console Shaper is well-qualified to provide these sought-after analog attributes for your own mixing within Studio One.
Insert Console Shaper into the special Mix FX slot on your Master Bus, or on any Bus you wish to process separately (such as a drum
bus). All Channels flowing to that Bus are processed individually at their source, and tone shaping parameters for all affected tracks are
set simultaneously with the controls on the central Console Shaper plug-in window or Console controls.
The following parameters are available in Console Shaper:
-
Drive Lets you dial in the right amount of analog-style saturation for your mix. Lower settings bring just a hair of pleasing drive,
while higher settings can get into crunchier territory.
-
Noise Lets you add analog-style noise to the channels affected by this instance of Console Shaper. This type of per-channel
noise can have a "gluing" affect on your mix, and add a sense of depth to some sources. Lower settings add just a bit of noise to
each channel, while higher settings can add a more significant amount.
-
Crosstalk Lets you add a specified amount of inter-channel crosstalk to the channels affected by this instance of Console
Shaper. Lower settings let smaller amounts of crosstalk occur, and higher settings give you more. Note that as you add
crosstalk, overall signal level rises.
All Console Shaper parameters offer on-off switches, for easy toggling of a given feature.
Getting more Mix Engine FX
Further Mix Engine FX are available at shop.presonus.com, and at the time of this writing include CTC-1 Pro Console Shaper, which fea-
tures three different console models, as well as Alpine Desk, Brit Console, and Porta Studio—available individually or bundled as “Retro
Mix Legends.”
Softube’s TAPE is also available for emulation of vintage tape machines!
Mastering
Multiband Dynamics
Getting more Mix Engine FX

Multiband Dynamics is a compressor/expander with five completely independent compression/expansion bands, optional simultaneous
adjustment over all bands, and multiband metering. Use it to reduce unwanted signals or banded noise and to emphasize or limit instru-
ments. In practice, this effect can function as a dynamic equalizer or can be used for mastering compression on a complete mix.
This type of compression is regarded by many as an art form, and can be difficult for beginners to use. We recommend you load the fact-
ory presets as a starting point and learn how Multiband Dynamics works by using it.
The following parameters are available for Multiband Dynamics:
-
Global Display Float mouse in display to view parameter-editing Tooltips above the display.
-
Input Horizontal lines represent Low and High Threshold for dynamics processing.
-
Output Horizontal lines represent transformation of the High and Low Thresholds using Gain and Ratio. A signal at the Low
Threshold on the input would be at the low level on the output.
-
Color Coded Output Gain Red means attenuation, green means amplification.
-
Mix This control lets you set the mix between effected and non-effected (dry) signals, allowing for parallel processing.
Dynamic changes occur only between Low/High Threshold and Low/High Gain. If the signal is above or below these settings, only linear
gain is applied.
-
Bands
-
L, LM, M, HM, H Low, Low Mid, Mid, High Mid, High.
-
Frequency Knob Adjust crossover frequency between bands. You must have at least one octave between
adjacent bands.
-
M, S, Bypass Mute, Solo, and Bypass engage buttons for each band.
Editing the crossover frequencies in the display moves other bands when the bandwidth is below one octave. Editing using automation is
limited to a one octave bandwidth. Moving the crossover to limit frequencies disables bands.
-
Metering
-
Range Low This is the lowest amplitude to be displayed in band meters. Click to select from -120 dB, -80 dB, -48 dB, -
24 dB, or -12 dB.
Mastering

-
Range High This is the highest amplitude to be displayed in band meters. Click to select from +12 dB, 0 dB, -12 dB, -24
dB, or -48 dB.
-
Metering On/Off Click to engage/disengage metering for all bands.
-
Edit All Relative Click to engage/disengage relative dynamics-settings editing for all bands. When engaged, changing dynam-
ics settings for the selected band changes the same settings for all bands by the same amount.
-
Auto Speed Click to engage/disengage Auto Speed for the dynamics for all bands. Sets adaptive Attack and Release times for
all bands globally.
-
Dynamics Click on any band to select it and view/edit dynamics settings for that band.
-
Dynamics Display Click on handles in display to adjust dynamics settings.
-
Thresholds No dynamics processing occurs for signals outside of the Threshold settings—only gain amp-
lification/attenuation.
-
Low Threshold Adjusts the lower limit for signal to be processed. Variable from -60 dB to 2x the knee length.
-
High Threshold Adjusts the upper limit for signal to be processed. Variable from 0 dB to 2x the knee length.
-
Ratio Adjusts dynamics processing ratio. Variable from 1:10 (gating) to 20:1 (limiting).
-
Gain Adjusts output gain. Variable from -36 dB to 36 dB.
-
Attack Adjusts attack time for dynamics processing. Variable from 1 ms to 200 ms.
-
Release Adjusts release time for dynamics processing. Variable from 4 ms to 200 ms.
Dynamics speeds are adapted to provide a comparable smoothness at the same setting for expansion and compression, so expansion is
slightly slower than the shown length.
-
Sidechain Engage by clicking the [Sidechain] button at the top of the effect window to allow specific sources to control the Mult-
iband Dynamics processor.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Multiple
selections can be made.
Tricomp™
Tricomp is a three-band compressor. It provides automatic threshold and ratio settings for all three bands and relative control for the low
and high bands, as well as switchable automatic attack and release controls. Tricomp can be used to finalize your mix or to add brilliance
or punch to frequency-rich signals.
The following parameters are available for Tricomp:
-
Input Gain Set overall Input Gain to the compressor
-
Mix Adjust the mix between dry (unaffected) and wet (effected) signals, for parallel compression effects.
-
Low Adjusts the relative amount of compression to be applied to the Low compression band. Variable from -5 to 5 depending on
the Compress setting.
Mastering

-
High Adjusts the relative amount of compression to be applied to the High compression band. Variable from -0.50 to 0.50,
depending on the Compress setting.
-
Low Freq Adjusts the upper corner frequency of the Low compression band. Variable from 80 Hz to 480 Hz.
-
High Freq Adjusts the lower corner frequency of the High compression band. Variable from 800 Hz to 12 kHz.
-
Input Meter Displays Tricomp’s input level.
-
Reduction Meter Displays the amount of signal reduction.
-
Compression Amount The relative amount of compression to be applied to all three compression bands. Variable from 0 to 10.
-
Output Meter Displays Tricomp’s output level.
-
Knee Adjusts the distance/curve of the compressor knee. Variable from 0 dB (hard knee) to 6 dB (soft knee).
-
Gain Set overall output Gain. Variable from -18 dB to +18 dB.
-
Attack When Auto is not engaged, these buttons select the compressor attack time. Fast Attack is 0.1 ms; Slow Attack is 10 ms.
-
Release When Auto is not engaged, this adjusts the compressor release time. Release is variable from 1 ms to 300 ms.
-
Auto Click to engage adaptive settings for the compressor attack and release times, based on signal content.
-
Saturation Saturation recreates the saturation sound of famous leveling amplifiers using State Space Modeling. Variable from 0
to 100%.
-
Sidechain Engage by clicking the [Sidechain] button at the top of the effect window to allow specific sources to control the
Tricomp processor.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Multiple
selections can be made.
Mixing
Many tools can help to achieve proper balance and create space for the various parts of your mix. The following effects can help you craft
your mix with precision and excellent sound quality.
Binaural Pan
The Binaural Pan is a panning effect that employs mid/side processing to manipulate the perceived width of stereo signals, from mono to
double the normal width. Use the Binaural Pan on any stereo Track to tightly control its stereo width and pan, as well as to check for
mono compatibility using the Mono switch.
The following parameters are available for the Binaural Pan:
-
Pan Adjusts the balance in the left and right channels for the stereo Track. Variable from 100% L to 100% R.
-
Mono Switch to mono playback of the stereo Track.
-
Width Adjusts the stereo width of the stereo Track. Variable from 0 (mono) to 200% (double stereo width).
The Binaural Pan can only be used on stereo Tracks. If loaded onto a mono Track, the plug-in display shows “MONO CHANNEL.”
Channel Strip
Mixing

Channel Strip features three processors in one, including a low-cut filter, dynamics processor, and three-band parametric EQ. Channel
Strip optionally applies automatic gain correction to the EQ so that the input-signal power matches the output signal power. Use Channel
Strip on any mono or stereo Track that needs basic channel processing.
The following parameters are available for Channel Strip:
Low Cut
-
Low Cut Active Click on the Low Cut Active button to engage/disengage the Low Cut filter.
-
Frequency Adjusts the Low Cut Frequency to change the filter cutoff frequency. Variable from 40 Hz to 400 Hz.
Compressor
-
Compress Adjusts the compression amount. Variable from Off to 100%. Simultaneously adjusts threshold (0 dB to -20 dB) and
ratio (2:1 to 10:1).
-
Expand Adjusts the expansion amount. Variable from Off to 100%. Simultaneously adjusts threshold (-64 dB to -24 dB) and
ratio (1.5:1 to 2.5:1).
-
Active gain reduction is indicated by a red “LED"-like indicator.
-
Slow, Medium, Fast Adjusts the RMS averaging speed. Slower speeds may reduce artifacts with some audio material. The
default is Medium, and Studio One version 1 presets open set to Fast.
Display Displays low-cut filter and parametric EQ settings. Click on handles to adjust gain (up/down) and frequency (left/right).
-
Adapt Q Enable to change band Q depending on the level of boost or cut applied.
EQ
-
Low, Mid, High Adjusts gain and frequency for each band of the parametric EQ. Each band has fixed Q.
Global
-
Gain Adjusts the output gain of the Channel Strip. Variable from -12 dB to 12 dB.
-
Auto Click to engage automatic output-gain setting. This guarantees that a 0 dB input signal equals a 0 dB output signal.
Dual Pan
Dual Pan is a fully variable stereo panner with input balance control, selectable pan law, and independent left/right panning. The fol-
lowing parameters are available for Dual Pan:
Mixing

-
Input Balance Adjusts the balance of the stereo input signal from full left to full right.
-
Pan Law Select a pan law, choose from -6 dB Linear, -3 dB Constant Power Sin/Cos, -3 dB Constant Power Sqrt, 0 dB Balance
Sin/Cos, and 0 dB Linear.
-
Pan
-
Left Adjusts the pan of the left input signal from full left to full right.
-
Right Adjusts the pan of the right input signal from full left to full right.
-
Link Link the Left and Right panning.
Fat Channel XT
Fat Channel is a complete virtual version of the channel strip found on the PreSonus StudioLive III line of mixers, which allows you to use
all Fat Channel XT presets in both Studio One and on StudioLive III. With gate/expander, compressor, parametric EQ and limiter func-
tions, Fat Channel combines many essential processing functions into one easy-to-use tool. Along with its "clean" modern dynamics and
EQ processors, Fat Channel XT gives you a selection of high-quality emulations of vintage compressors and EQs to suit your needs..
Fat Channel XT Preset Interchange
To send a Studio One Fat Channel XT preset to StudioLive III or AI, click Export Channel Preset in the Preset Options menu of the Fat
Channel XT plug-in header. This saves the current preset to the Universal Control user preset folder, for use by a connected
StudioLive III or AI mixer.
Mixing

Newly added presets from a connected StudioLive III mixer are automatically added to the Studio One Fat Channel XT presets list each
time Studio One is launched.
StudioLive AI mixers do not have the ability to use the non-standard EQ and compressor models in Fat Channel XT. If you wish to send a
Fat Channel XT preset to your StudioLive AI mixer, be sure to use the standard processor models only.
Fat Channel XT Controls
Fat Channel XT features the following controls:
Header
-
Stacked Mode
Click this option to toggle the display state of Fat Channel XT. When disabled, only the currently selected
processor (such as Gate or Compressor) is displayed. When enabled, all four processors are displayed at once, in a stacked
arrangement.
-
Processor Select Buttons (HPF/Gate, Compressor, Equalizer, Limiter) When Fat Channel XT is not in Stacked Mode, click
these buttons to display the processor block of your choice.
-
Processor Enable/Disable Click the round button next to the processor name of your choice to toggle the on/off state
for that block of processing. Each processor also has its own enable/disable switch within the module interface.
-
Compressor and Equalizer Model Selectors Click the menu next to the name of the Compressor or Equalizer processors to
open a Gallery view, from which you can choose the desired Compressor or EQ model. Hover the cursor over each image to
view a brief description, then click to select the one you want.
-
Compressor offers the following choices:
-
Standard A flexible, modern compressor, with a clean, hi-fi sound.
-
Tube A model of one of the best-loved vintage tube-based opto-compressors. Excels at vocal smoothing and
at making bass instruments sound larger-than-life.
-
FET A model of one of the most-used vintage FET-based compressors. Great for adding an aggressive edge
and accentuating room sound for drums, guitars, and other highly transient signals.
-
Equalizer offers the following choices:
-
Standard A flexible, full-featured modern EQ, with a clean, hi-fi sound.
-
Passive A model of the "rolls-royce" of vintage tube-based passive EQs. Deceptively simple controls and a
rich, thick sound make it perfect for gentle tone shaping or adding vintage character.
-
Vintage A model of what some call the "final word" in vintage solid-state EQs. Combines an "everything
sounds better through it" quality with musically-chosen EQ frequencies for quick, reliable tonal magic.
-
Swap Comp/EQ Order Click this button to swap the places of the Compressor and Equalizer processors in the signal chain.
-
Sidechain Engage by clicking the [Sidechain] button at the top of the effect window to allow other sources to control the limiter.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Multiple
selections can be made.
High-Pass Filter (HPF)
Mixing

-
Enable/Disable Click the "HPF" legend to enable or disable the high-pass filter module.
-
High PassSets the frequency of the high-pass filter. Turn all the way left to disengage the filter.
Gate
-
Enable/Disable Click the "Gate" legend to enable or disable the Gate module.
-
Threshold This knob sets the level at which the gate opens. Essentially, all signals above the threshold setting are passed
through unaffected, whereas signals below the threshold setting are reduced in level by the amount set by the range control. If
the threshold is set all the way to the left, the gate is turned off (always open), allowing all signals to pass through unaffected.
You can set the threshold from 0 to -84 dB.
-
Range This adjusts the amount of gain reduction the gate produces. The range can be set from 0 to -84 dB. The Range control
is not available when using the expander.
-
Key Filter This knob adjusts the frequency at which the gate opens. Setting a specific frequency, in addition to a specific decibel
level, provides more sonic shaping. The key filter can be triggered by the selected channel or bus’s signal or by sidechaining a
channel and using its signal as the source.
-
Attack (Att) This adjusts the rate at which the gate opens on the selected channel or output. You can set the attack time from
0.02 to 500 ms.
-
Release (Rel) Adjusts and displays the rate at which the gate closes on the selected channel. The release time can be set from
0.05 to 2 seconds.
-
Key Listen This button engages and disengages the Key Listen function, which lets you hear how the gate Key Filter is set.
-
Expander Switch the gate into expander mode.
-
Interactive Graph This graph provides a visual representation of the settings and current activity of the gate. You can also
adjust the setting by moving the blue dots to adjust Threshold and Range.
Compressor Module - Standard Mode
Mixing

-
Enable/Disable Click the "Compressor" legend to enable or disable the Compressor module.
-
Threshold This knob adjusts the compressor threshold for the selected channel. The compressor engages as soon as the sig-
nal level (amplitude) exceeds the threshold value. Moving this control to the left lowers the threshold so that compression begins
at a lower amplitude value. The threshold can be set from -56 to 0 dB.
-
Ratio This knob adjusts the compression ratio (or slope). The ratio is a function of the output level versus the input level. For
example, if you have the ratio set at 2:1, any signal levels above the threshold setting are compressed at a ratio of 2:1. This
means that for every 2 dB of level increase above the threshold, the compressor’s output only increases by 1 dB. The ratio can
be set from 1:1 to 18:1 or “limit” which is the equivalent of infinity:1.
-
Gain This sets and displays the makeup gain of the compressor for the selected channel. Compressing a signal usually results
in an overall reduction in level (gain reduction), and the Makeup Gain control lets you increase the volume to make up for this
gain loss, if desired. You can adjust the Makeup Gain from 0 dB (no gain adjustment) to +28 dB.
-
Attack This adjusts the speed at which the compressor acts on the input signal. A slow attack time (moving the slider to the
right) allows the beginning component of a signal (commonly referred to as the initial transient) to pass through, uncompressed,
whereas a fast attack time (fully to the left) triggers compression immediately when a signal exceeds the threshold. You can set
the attack from 0.2 to 150 milliseconds.
-
Release This determines the length of time the compressor takes to return the gain reduction back to zero (no gain reduction)
after crossing below the compression threshold. Release can be set from 2.5 to 900 milliseconds.
-
Key Listen This button engages and disengages the Key Listen function, which lets you listen to the signal that is being fed to
the compressor's detector.
-
Auto This enables Automatic Attack and Release mode. When Auto mode is active, the Attack and Release controls become
inoperative, and a pre-programmed attack and release curve is used that sets the attack to 10 ms and the release to 150 ms.
Meanwhile, all other compressor parameters can still be adjusted manually.
-
Soft This engages soft-knee compression. In normal operating mode, the compressor is set for hard-knee compression, mean-
ing the gain reduction applied to the signal occurs as soon as the input signal level exceeds the threshold value. When the Soft
Knee button is engaged, the ratio increases gradually as the signal reaches the threshold.
-
Interactive Graph This graph provides a visual representation of the settings and current activity of the compressor. You can
also adjust the setting by moving the blue dot to change the Threshold and Ratio values.
Compressor Module - Tube Mode
Mixing

-
Enable/Disable Click the power switch to enable or disable the Tube Compressor module.
-
Comp/Limit Toggles the Tube Compressor between its compressor and limiter modes. When in compressor mode, it acts with
a variable ratio of 1:1-10:1. When in limiter mode, it acts with a variable ratio of 10:1-20:1, more aggressively limiting peaks.
-
Gain Sets input gain to the compressor. Because this type of compressor operates in a different way than a standard com-
pressor, much of the way that it affects signals is based on the input level. Try different settings to see what suits your needs.
-
Peak Reduction Sets the amount of peak reduction to apply to the signal. Higher settings result in more gain reduction and
more pronounced compression effect.
-
Key Filter Sets the frequency of a high-pass filter that sits in the compressor sidechain. The higher the setting, the more fre-
quencies are excluded from reaching the compressor's detector, with a variety of useful dynamic results. Ranges from "Off" to
16 kHz.
-
Key Listen This button engages and disengages the Key Listen function, which lets you listen to the signal that is being fed to
the compressor's detector, after it has passed through the Key Filter.
-
VU Meter (Gain Reduction) This vintage-style VU meter shows a smoothed representation of gain reduction applied by the
compressor over time.
Compressor Module - FET Mode
Mixing

-
Enable/Disable Click the power switch to enable or disable the FET Compressor module.
-
Input Sets input gain to the compressor. This setting affects the action of the compressor, so feel free to try various settings to
find the optimal effect for your needs.
-
Output Sets the amount of "makeup gain" to apply to a signal. Once a signal is compressed, its overall level is often reduced.
This gain control lets you bring it back up to the proper level after compression occurs.
-
Attack This adjusts the speed at which the compressor acts on the input signal. A slow attack time (moving the slider to the
right) allows the beginning component of a signal (commonly referred to as the initial transient) to pass through, uncompressed,
whereas a fast attack time (fully to the left) triggers compression immediately when a signal exceeds the threshold. Attack
ranges between 0.8 to 0.02 milliseconds.
-
Release This determines the length of time the compressor takes to return the gain reduction back to zero (no gain reduction)
after crossing below the compression threshold. Release ranges between 1.1 second to 50milliseconds.
-
Ratio Selector Buttons These buttons let you choose a compression ratio: 4:1, 8:1, 12:1, 20:1, or "All."The ratio is a function of
the output level versus the input level. For example, if you have the ratio set at 4:1, any signal levels above the threshold setting
are compressed at a ratio of 4:1. This means that for every 4 dB of level increase above the threshold, the compressor’s output
only increases by 1 dB. The "All" setting recreates the "all buttons pushed in" setting that helped make this compressor type a
legend, providing massive punch and crunch when driven hard.
-
Key Filter Sets the frequency of a high-pass filter that sits in the compressor sidechain. The higher the setting, the more fre-
quencies are excluded from reaching the compressor's detector, with a variety of useful dynamic results. Ranges from "Off" to
16 kHz.
-
Key Listen This button engages and disengages the Key Listen function, which lets you listen to the signal that is being fed to
the compressor's detector, after it has passed through the Key Filter.
-
VU Meter (Gain Reduction) This vintage-style VU meter shows a smoothed representation of gain reduction applied by the
compressor over time.
Equalizer Module - Standard Mode
Mixing

-
Enable/Disable Click this button to enable or disable the Equalizer module.
-
Low Shelf (LS) & High Shelf (HS) Buttons These buttons turns Shelving mode on or off for the High and Low bands. When
the Shelf button is engaged, the associated High or Low frequency section is switched from parametric EQ to shelving EQ.
-
Band Enable/Disable Buttons These buttons select which EQ band is being controlled by the Frequency, Gain, and Q con-
trols.
-
Freq This knob selects the center frequency of the corresponding band. You can adjust the center frequency in the following
ranges for each band: Low Band: 36 to 465 Hz Low-Mids: 90 Hz to 1.2 kHz Hi-Mids: 380 Hz to 5 kHz Highs: 1.4 to 18 kHz
-
Gain This knob boosts and attenuates the selected frequency with a range of -15 to +15 dB.
-
Q This adjusts the Q value for the corresponding frequency band. The Q is the ratio of the center frequency to the bandwidth.
When the center frequency is constant, the bandwidth is inversely proportional to the Q, so as you raise the Q, you narrow the
bandwidth. Hence, the smaller the number, the wider the curve.
-
Interactive Graph This graph provides a visual representation of the current settings. You can change the settings by moving
the blue dots to adjust the frequency and gain at the same time. The first time you touch a dot, the associated band automatically
turns on. Tapping or clicking a dot turns the band on and off.
Equalizer Module - Passive Mode
Mixing

-
Enable/Disable Click this On/Off switch to enable or disable the Passive Equalizer module.
-
(Low) Boost Sets the level of boost applied around the chosen low frequency. This control interacts nicely with the Low Atten-
uation control, allowing for boosts in apparent bass energy while keeping overall bass energy within optimal limits.
-
(Low) Attenuation Sets the level of attenuation applied around the chosen low frequency. This control interacts nicely with the
Low Boost control, allowing for boosts in apparent bass energy while keeping overall bass energy within optimal limits.
-
Low Frequency Sets the center frequency of the band covered by the Low Boost and Low Attenuation controls.
-
(Hi-Mid) Boost Sets the level of boost applied around the chosen high-mid frequency.
-
(Hi-Mid) Bandwidth Sets the Q (or width) of the effect of the high-mid EQ band.
-
(Hi-Mid) FrequencySets the center frequency of the high-mid EQ band.
-
(High) Attenuation Sets the amount of attenuation applied in a shelving fashion to frequencies at and above the chosen high
frequency.
-
(High) Attenuation Selector Sets the frequency at and above which the High Attenuation control attenuates treble content.
Equalizer Module - Vintage Mode
Mixing

-
Enable/Disable Click the power button to enable or disable the Vintage Equalizer module.
-
Low Frequency Sets the corner frequency of the low-frequency shelving band of this EQ. Choose from 35, 60, 110, or 220 Hz.
-
Low Gain (LF) Sets the amount of boost or cut to apply the to low-frequency band of this EQ. Range of plus or minus 16 dB.
-
Low-Mid Frequency Sets the center frequency of the low-mid-frequency band of this EQ. Choose from 360 Hz, 700 Hz, or 1.6
kHz.
-
Low-Mid Gain (LMF) Sets the amount of boost or cut to apply to the low-mid-frequency band of this EQ. Range of plus or minus
16 dB.
-
High-Mid Frequency Sets the center frequency of the low-mid-frequency band of this EQ. Choose from 3.2, 4.8, or 7.1 kHz.
-
High-Mid Gain (HMF) Sets the amount of boost or cut to apply to the high-mid-frequency band of this EQ. Range of plus or
minus 16 dB.
-
High Gain (HF) Sets the amount of boost or cut to apply the high-frequency shelving band of this EQ. Range of plus or minus 16
dB.
Limiter Module
-
Enable/Disable Click the "Limiter" legend to enable or disable the Limiter module.
-
Threshold Sets and displays the threshold of the limiter on the selected channel. The limiter engages as soon as the signal
level (amplitude) exceeds the threshold value. Moving this control to the left lowers the threshold so that limiting begins at a
lower amplitude value. The threshold can be set from -28 to 0 dB.
Splitter
While not technically an effect in itself, Splitter is a special routing module that lets you split signals and process them through multiple
parallel effects paths. These split signals are then mixed back into a single signal. You can add an instance of Splitter by dragging and
Mixing

dropping it to a Channel from the Effects section of the Browser, or by clicking-and-dragging from the [Splitter] button to your choice of
location in the Channel Editor’s Routing view.
Splitter is enhanced for use with multichannel audio. When using Splitter on a Channel containing a multi-channel Audio Event (like a 5.1
multichannel WAV file), the Channel Split option will provide the appropriate number of splits.
For more on how to use Splitter, see Routing View in the Channel Editor section.
Modulation
Modulation processors are great tools for creating interesting and innovative sounds. Studio One features the following modulation pro-
cessors:
Autofilter
Autofilter features two resonant filters with six selectable filter models. The filter cutoff frequency and resonance can be modulated by an
LFO using standard waveforms, a 16-step sequencer, and an envelope. Use Autofilter to create filtered effects from basic filter sweeps to
complex tempo-synced rhythmic filter patterns.
The following parameters are available for Autofilter:
-
Filter Type
-
Filter 1 and Filter 2 Select from 8 filter emulation types, including Ladder LP 12 dB, 18 dB, and 24 dB; Analog SVF 12
dB and 24 dB, Digital SVF 12 dB, Comb, and Zero Delay LP 24 dB (as found in the Mai Tai and Presence XT instru-
ments). Note that Filter 2 also has a Bypass option.
-
SVFs State Variable Filters can blend between low-pass, bandpass, and high-pass. Click-drag the vertical Fil-
ter Mix fader on the right to blend the filter types.
-
Chained/Parallel Switch the two filters between chained in series (Filter 1 followed by Filter 2; good for adding peaks,
creating band-reject filters, etc.) and parallel (Filter 1 and Filter 2 process and output the same signal simultaneously;
good for creating wide bandpass filters).
-
Filter
-
Cutoff Adjusts the cutoff frequency for both filters. Variable from 30 Hz to 16 kHz. Can be modulated by the envelope
and LFO.
-
Resonance Adjusts the resonance of the filters. Variable from 0 to 100%.
-
ENV/LFO Adjust the modulation amounts for each filter using the Env and LFO vertical faders. Variable from -100% to
100%. Negative values are phase-inverted. The LFO modulates around the value.
-
Speed
-
LFO Speed Can be synced to tempo or run free.
-
Sync Click to engage/disengage LFO tempo sync. When tempo is synced, the speed is variable from 4/1 to
1/64, with various triplet and dotted-time variants.
-
ENV Attack adjusts the attack time of the volume envelope, affecting the beginning of cutoff and resonance modulation
Modulation

-
ENV Release adjusts the release time of the volume envelope, affecting the end of cutoff and resonance modulation.
-
Auto Click to engage/disengage automatic envelope-length selection.
-
LFO Steps Display This area shows the amplitude for each step in the LFO. A vertical line sweeps through the display to indic-
ate the current position in the selected waveform. The LFO runs freely when Sync is disengaged; with Sync engaged the line
starts and stops with Song playback.
-
LFO Type Five LFO types are available along the bottom of the display. Click the buttons to select one of the following types:
-
16 Steps Click in the LFO display to adjust each step. The steps divide the current Speed/Beats time value. The LFO is
bipolar: the value of each step represents amplitude at that step from maximum negative to maximum positive, with the
mid-point as the zero-crossing frequency (no modulation). Click-drag to draw unique shapes.
-
Waveforms Select triangle, sine, sawtooth, or square.
-
Flip inverts the phase of the waveform.
-
Color
-
Drive Adjusts the filter’s feedback overdrive, which features State Space Modeling. Variable from 0 to 100%.
-
Cutoff 2 Shift Adjusts the offset of Filter 2 Cutoff frequency. Variable from -2 octaves to 2 octaves.
-
Global
-
Gain Adjusts Autofilter output gain. Variable from -24 dB to +24 dB.
-
Auto Click to engage Auto-Gain, to keep input and output signals at equivalent levels.
-
Mix Adjusts the mix of the Autofilter-processed signal with the original dry input signal. Variable from 0 to 100%.
-
Sidechain Click the Sidechain button at the top of the effect window to engage sidechain for envelope detection. This allows
you to use another Track to control the envelope.
-
Sources Click to display a list of potential sidechain channel sources. A checked box indicates the current source. Mul-
tiple selections can be made.
Chorus
The Chorus is a 1-3-voice chorus processor with optional LFO delay time modulation and stereo width control. Chorus processing is
often used on vocal tracks to help create a more full vocal sound so the track fits better in the overall mix. Guitar and synth parts some-
times feature chorus processing for similar reasons.
The following parameters are available for the Chorus:
-
Delay Adjusts the delay of the Chorus voices. The value you set is the delay time between voices.
-
LFO Shape Choose between the four waveforms for the LFO: Triangle, Sine, Sawtooth, or Square.
-
Voices Adjusts the number of added voices in the Chorus; select from 1, 2, or 3.
-
LFO The LFO modulates the Spacing parameter.
Modulation

-
Depth Adjusts the mix of the processed Chorus output with the dry input signal. Variable from 0 to 100%.
-
St. Width Adjusts the spreading of the Chorus voices in the stereo field. Click the Spread button to engage/disengage the Ste-
reo Width feature.
-
LFO Speed Adjusts the speed of the LFO.
-
LFO Width Adjusts the range of the LFO modulation of Spacing. Variable from 0 to 100%. A value of 100% would modulate the
Spacing parameter from 0 to 2x Spacing.
-
Low Freq Sets the corner frequency of the low-cut filter.
-
High Freq Sets the corner frequency of the high-cut filter.
-
Mode Choose between Doubler mode (equivalent to the Chorus effect in Studio One 2.5 and earlier) and Chorus mode, which
employs inverse all-pass movement, for truer chorus effect.
Flanger
Flanger creates spatial depths, swirls, timbre shifts, and percussive effects. Flanging is often used on guitar tracks to create interesting
shifts in timbre and tone, and it can help create lush synth sounds, as well. It works by splitting an audio signal into two identical signals;
applying a varying, short delay to one signal; feeding its output back to its input by varying amounts; and mixing the processed and unpro-
cessed signals. You can modulate Flanger’s delay time with an LFO, which can be tempo-synced.
The following parameters are available for Flanger:
-
Feedback Adjusts the amount of delayed output to be fed back into the input. Variable from -90% to 90%. Negative value results
in inverted feedback.
-
Delay Adjusts the delay time for the copied input signal. Variable from 0.25 ms to 10 ms.
-
Modulation This section uses an LFO to modulate the Speed/Beats parameter.
-
LFO-Amount Adjusts the range of the LFO modulation on delay time (speed). Variable from 0 to 100%. A value of
100% would modulate the Speed parameter from 0 to 2x Speed.
-
Sync Click to engage LFO tempo sync. Time is expressed as Beats.
-
Speed/Beats Adjusts the speed of the LFO.
-
Speed Variable from 0.01 Hz to 10 Hz.
-
Beats Select from 4/1 to 1/64 with triplet and dotted-time variants.
-
Global
-
Mix Adjusts the mix of the processed Flanger output with the original dry input signal. Variable from 0 to 100%.
Flanger is enhanced for use with multichannel audio. When assigned to a multi-channel source, the following parameters are added to
Flanger:
-
Surround Distribution changes the modulation offset amount among the output channels.
-
Spatial Mode Choose from Circular, Left/Right, or Front/Rear to affect the dynamic movement of the Flanger effect.
-
Stereo Spread Select the desired amount of stereo width.
Modulation

Phaser²
Phaser² applies a variable number of allpass filters in series (one fed into the other), along with one overall feedback loop, to the input sig-
nal. Phaser² features an LFO to modulate the center frequencies for each all-pass filter.
The allpass filters function as frequency-dependent delays, so that when the filtered output is added to the original input signal, certain
frequencies can be attenuated or amplified as the result of phase shifting. Phasers are commonly used on many types of signals, includ-
ing synths, guitars, and even vocals, to create a distinctive frequency-shifting effect.
The following parameters are available for Phaser²:
-
Stages Adjusts the number of allpass filter stages in Phaser². Variable from 2 to 20.
-
Speed/Beats Adjusts the speed of the LFO.
-
Speed Variable from 0 Hz to 10 Hz.
-
Beats Select from 4/1 to 1/64, with triplet and dotted-time variants.
-
Sync Click to engage LFO tempo sync. Time is expressed as Beats.
-
Color Modulates the frequency for the allpass filters within the limits set by the Range control, with the Center frequency as the
mid-point.
-
Center Adjusts the center frequency for the allpass filters. Variable from 10 Hz to 8 kHz.
-
Range Sets the range of Phaser² modulation from 0 to 100%.
-
Log. Sweep Changes the LFO behavior so that it operates on a logarithmic scale.
-
Soft Selects a triangle wave as the Phaser² modulation shape. When this is disengaged, a sine wave is used as the
modulation shape.
-
Feedback Adjusts the amount of the filtered output signal to be fed back into the input. Variable from 0 to 95%.
-
Global Adjusts the speed of the LFO.
-
Stereo Spread Adjusts the spread of each allpass filter in the stereo field from 0 to 100%.
-
Mix Adjusts the blend between the processed Phaser² output and the original dry input signal. Variable from 0 to 100%.
Phaser² is enhanced for use with multichannel audio. When assigned to a multi-channel source, the following parameters are
added to Phaser²:
-
Surround Distribution changes the modulation offset amount among the output channels.
-
Spatial Mode Choose from Circular, Left/Right, or Front/Rear to affect the dynamic movement of the Phaser effect.
-
Stereo Spread Select the desired amount of stereo width.
Modulation

Rotor
Rotor is a rotary speaker effect that simulates the sound of a tube-powered amplifier with independently rotating high-mid horn and bass
woofer, as you might find attached to a classic electric organ. Rotor excels at adding a sense of motion and unique tonal character to
organ sounds, guitars, or anything you want to try. Each speaker's rotation can be set to a range of speeds, with realistic braking and
acceleration effects when changing speeds.
The following parameters are available for Rotor:
-
Off/On Toggles the rotating action of the virtual speakers on and off, with a smooth speed transition between states.
-
Slow/Fast Toggles between the two preset speeds for the woofer and horn, with a smooth transition between speeds.
-
Amp
-
Drive Add the desired amount of amp drive to the tone using State Space Modeling technology. Lower settings are
cleaner, higher settings are more overdriven.
-
Horn Q Blends in a midrange peak that emulates the resonance of rotating horn speakers. Lower settings are more flat,
higher settings have a more pronounced resonance.
-
A/B Toggles between two amplifier models that are recreated using State Space Modeling technology.
-
Position
-
Distance Lets you choose the position of the virtual microphone that picks up the rotating speaker. At low settings, the
mic is close to the speaker, and the stereo sweeping effects are more pronounced. At higher settings, the mic is further
away from the speaker, and the effect is subtler and more diffuse.
-
Balance Lets you blend between the woofer and horn, to achieve the desired tonal balance. Fully down, you mainly
hear the woofer. Fully up, you mainly hear the horn.
-
Spread Controls the stereo width of the rotating speaker elements. At low settings, the part of the signal signifying the
front of each rotating element moves in a tight, distinct band across the stereo spectrum. At higher settings, the rotating
element appears wider and more diffuse.
-
Trim
-
Woofer Speed and Horn Speed These dual-slider controls let you set the speed at which the woofer and horn spin at
slow and fast speed settings. You can set them to identical values for more coordinated rotation between woofer and
horn, or to differing values that set up contrasting rotations.
Modulation

Vocoder
Vocoder is a creative effects processor that combines two input signals to create an entirely new sound. One signal is the modulator,
and the other is the carrier.
Vocoder works by splitting the sound of the modulator signal into 20 frequency bands, each with its own bandpass filter and envelope fol-
lower. The carrier signal is sent through the filterbank, and the levels adjust to match the frequency of the modulator. The resultant
sound is that of the carrier signal being filtered in such a way that its harmonic content resembles that of the modulator signal. When you
start manipulating the mapping of frequency band Inputs and Outputs… that's where the real fun starts!
While typically used to give the human voice the texture (and polyphony!) of a synthesized instrument, Vocoder is by no means limited to
this application. You’ll find Vocoder to be highly rewarding of experimentation.
Fun fact: hardware vocoders were originally created to encrypt radio transmissions, way back in 1928. They didn’t find use in creative
musical applications until the 1970s.
Assigning input sources
Drag and drop Vocoder onto the track you want to process. This Track will serve as Vocoder’s modulator signal.
Using the sidechain menu at the top of the Instrument Editor, assign the second audio source you want. This will be the carrier signal.
(You can also use an internal source from Vocoder itself as the carrier. More on that below.)
We recommend familiarizing yourself with sidechaining in Studio One by reading the Sidechaining Topic before using Vocoder.
The following parameters are available for Vocoder:
Modulator Envelope
-
Attack controls the attack speed of the modulator envelope.
-
Release controls the release time of the modulator envelope.
Carrier
Carrier Source - This section is used to set up Vocoder for use with an external (sidechain) carrier signal or an internal carrier signal gen-
erated by Vocoder itself. The LEDs will reflect whether a side chain is assigned or not.
-
Source select (power button) toggles between sidechain and internal carrier sources. Sidechain must be enabled at the
top of the Instrument Inspector for this feature to be available.
The following options apply only when using the Internal carrier.
Modulation

-
Waveform: Select Noise, Saw or Rect waveform. This is for the internal carrier generator only.
-
Frequency controls the frequency of the internal carrier signal. When the carrier source is set to Noise, Frequency controls a
blend between pink noise (left) and white noise (right).
-
Follow controls modulation amount of the internal carrier pitch as determined by following the input (modulator) level. Essen-
tially an envelope follower that can be used to add some pitch movement to an artificially static voice.
Patch Matrix
The patch matrix is a creative tool which allows you to specify routing from the vocoder’s analyzer section into the synthesizer section.
Doing so can help to improve intelligibility of a vocoded voice, or it can be used to push sounds from natural to more unnatural. The pos-
sibilities are almost endless!
The outputs of the 20 analyzer bands, identified at the bottom of the matrix, can be patched using “pins” to the inputs of the 20 syn-
thesizer bands, identified on the left of the matrix. The default mapping is a diagonal (1:1).
Routings can be clicked in one at a time, or click and drag to draw a routing configuration quickly.
There are two modes (X and Y) for these routings.
X mode: there is one pin per output band, thus it is possible to assign for example one input band to one or more output bands. Click to
activate X mode.
Y mode: there is one pin per input band, thus it is possible to assign or merge multiple input bands into one output band. Click to activate
Y mode.
-
Flip toggles between X and Y modes (see above).
-
Reset resets all pins and volume sliders to the 1:1 (diagonal) configuration.
-
Bypass bypasses the patching matrix.
-
Freeze: when activated, the contour of the synthesizer bands will be frozen (sample & hold) until the button is disengaged.
When you store a preset with Freeze activated, the structure will be stored and reloaded with the preset.
-
Volume: Click to toggle the matrix display to show the volume of each of the 20 synthesized output bands. Click or click-and-
drag within the matrix to set pins at the desired volume level of each band.
-
Analyzer LEDs indicate the level per analyzer band on the left of the matrix.
-
Synthesizer LEDs indicate the level per synthesizer band at the bottom of the matrix.
Unvoiced Replacement
Mode: Vocoding of unvoiced speech sounds (f, s, etc.,) is often unsatisfactory. Vocoder offers a function to detect these unvoiced
sounds and then replace them with other signals, including noise or a mix of the direct signal.
-
Off: No replacement is performed.
-
Noise: Unvoiced parts are replaced by a noise signal.
-
Direct: A filtered portion of the original carrier signal input is directly mixed into the output.
Speech intelligibility is increased significantly with Noise or Direct mode active.
-
Level: Controls the level of the replacement signal.
-
Voiced: Indicates whether the input signal is rated as voiced or unvoiced.
Output
-
Mix: Wet / Dry mix balance of the carrier input signal and the synthesized output signal.
-
Volume: Overall output volume.
Modulation

X-Trem
X-Trem is a tremolo effect that applies amplitude modulation at a varying amount and rate over time. The X-Trem features tempo sync
and a variable LFO with selectable 16-step and 16-gate sequencers, as well as auto-pan capability. Use X-Trem on any Track to create
anything from subtle shifts in amplitude to tempo-synced, glitchy, gated drums; trancy, gated pads; panned hi-hats; and other popular
sounds.
The following parameters are available for X-Trem:
-
LFO Steps Display This area shows the amplitude for each step in the LFO. A vertical line sweeps through the display to indic-
ate the current position in the selected waveform. The LFO runs freely when Sync is disengaged; with Sync engaged the line
starts and stops with Song playback.
-
LFO Type Six LFO types are available along the bottom of the display. Click the buttons to select one of the following types:
-
Waveforms Select triangle, sine, sawtooth, or square.
-
16 Steps Click in the LFO display to adjust each step. The steps divide the current Speed/Beats time value; the value of
each step represents amplitude/pan at that step from 0/hard left to 100%/hard right. Click-drag to draw unique shapes.
-
16 Gates Click in the LFO display to open/close the gate at each step. The steps divide the current Speed/Beats time
value. For each step, no color fill means the gate is closed, and total color fill means gate is open.
-
Flip This button above the display flips the phase of the selected waveform. It is grayed out and can't be selected when the
LFO mode is "16 Steps" or "16 Gates".
-
Modulation This section controls the depth, speed, and destination of the LFO.
-
Depth Adjusts the relative amount of maximum amplitude modulation. Variable from 0 to 100%.
-
Pan/Trem Click to switch the mode of the X-Trem to affect overall amplitude (Trem) or the left- and right-channel bal-
ance (Pan). Pan is only selectable on stereo Tracks.
-
LFO Speed Adjusts the speed of the LFO. With Sync disengaged the speed is expressed in frequency (rate); with Sync
engaged the speed is expressed in rhythmic values (beats).
-
Rate Variable from 0.01 Hz to 30 Hz.
-
Beats Select from 4/1 to 1/64 with triplet and dotted-time variants.
-
Sync Click to engage LFO tempo sync.
Reverb
Reverb effects are used in almost all music productions and for a variety of purposes. In everyday life, reverberation is the result of the
many reflections of sound that occur in a given room or other space. In an ambient space, sound may travel directly to your ear and also
be reflected many times off the walls and ceiling of a room before again reaching your ear. With each reflection, the sound is attenuated
as sound energy is absorbed by the reflecting surfaces and dissipated by traveling through a medium (usually air). This collection of
reflected and attenuated sounds is what we know as reverb.
Reverb

Reverb provides essential aural cues about the nature of any given space. As such, reverb is commonly used in music production to cre-
ate virtual spaces in which the various parts of a mix can interact.
Studio One features two built-in reverbs: Mixverb and Room Reverb. three built-in reverbs: Mixverb, Room Reverb, and OpenAIR. The
following describes these reverb effects.
Mixverb™
Mixverb is a simple and efficient reverb that is meant to be used as an Insert on mono or stereo Tracks. Mixverb features adjustable size,
pre-delay, and damping, as well as an adjustable gate and stereo width control.
Mixverb offers the following parameters:
-
Pre-delay Adjust the predelay time. Variable from 0 ms to 500 ms. Predelay is the amount of time before the first reverberated
signals are heard.
-
Size Adjusts the relative size of the reverberating space. Variable from 0 to 100%.
-
Damping Adjusts the relative amount of damping (attenuation of the upper frequencies) of the reverberated signal. Variable
from 0 to 100%.
-
Gate The gate is applied to the reverb output signal.
-
Gate Tail Click to engage/disengage the gate.
-
Gate Threshold Adjusts the threshold of the gate. Variable from -36 dB to 12 dB.
-
Gate Release Adjusts the release time of the gate. Variable from 10 ms to 250 ms.
-
Global
-
Width Adjusts the width of the stereo field. Variable from 0 to 100%. Only for stereo Tracks.
-
Mix Adjusts the mix of processed signal with the original dry signal. Variable from 0 to 100%.
-
Lock Mix Level Locks the Mix control in place.
Open AIR2
Open AIR2 is a highly efficient convolution reverb plug-in capable of delivering ultra-realistic reverberation based on impulses captured
from both real spaces and classic hardware reverbs. Open AIR2 includes a 4-band EQ and supports mono, stereo, or multichannel
impulse responses.
Open AIR2 provides three views with multiple parameters. These views are Image, IR, and EQ, and each view can be selected by click-
ing the navigation icons at the top of Open AIR2 or the IR and EQ icons at the bottom, within the Global section.
Global Controls
-
Impulse Name Click on the Impulse Name field to load your own impulse response
-
Prev/Next Switches the impulse response to the previous or next file in the same file location as the existing impulse response.]
-
Channel Configuration Displays the channel format of the currently loaded impulse response.
-
Pre-delay Defaults to 0 ms; adds pre-delay to the impulse response with a positive value, or truncates existing pre-delay in the
impulse response with a negative value. Values range from -150 to 300 ms.
-
Size For values smaller than the original impulse response length, this cuts the end (that is, shortens the reverb). For larger val-
ues, the range between the ER/LR (early reflections/late reflections) crossover point and the impulse response end gets time-
Reverb

stretched. The beginning (up to the ER/LR crossover point) is not stretched, so the room impression created by the early reflec-
tions stays intact. [Ctrl]/[Cmd]-click restores the length to the impulse response length.
-
View selectors Choose IR or EQ View.
-
ER/LR Scales volumes before and after the ER/LR crossover point, from 0 to 1.00.
-
Gain Sets the overall output volume.
-
Mix This is the wet/dry mix, from 0 to 100%.
IR View
This view contains a visualization of the loaded Impulse Response and Envelope and Processing controls.
-
IR Display and Selection
-
Log Time When engaged, this shows more details for the early reflections, making it easier to set ER/LR crossover
point.
-
Log Level When engaged, this makes it easier to see RMS curves.
-
Enable LFE When engaged, Open AIR2 will process content in the LFE channel. Available only in Songs with an LFE
channel.
-
IR Mixer Click to open a mixer with a level slider and mute button for each channel. Available only in multichannel
Songs.
-
Envelope
-
Fade-In Fades in the impulse response, from 0 ms to 2.0 s.
-
ER/LR Crossover Sets the crossover point in time for early and late reflections; affects the impulse response pro-
cessing. Range is from 0 to 500 ms.
-
Fade-Out Fades out the impulse response, from 1 ms to the length of the impulse response.
-
Shorten with Stretch When this is activated, and the length is smaller than the original impulse response, the impulse
response is not cut and is instead timestretched between the ER/LR breakpoint and impulse response end. The content
of the impulse response before the ER/LR breakpoint is not stretched or compressed, preserving the character of those
reflections and thus a large part of the reverb character.
-
Processing As Open AIR2 does not feature true stereo processing, channel cross-feed and cross-delay is built-in.
-
Cross-Feed Adjusts the amount of the delayed “other” channel that gets fed into the left and right IR channels, from 0 to 100%
-
Cross-Delay Adjusts the delay of the cross-fed channels, effectively acting as stereo distance, from 0 to 25 ms.
-
Asymmetry Adjusts delays and the mix of cross-feed to simulate an asymmetric recording setup, from full left to full right.
-
Stretch with Pitch When this is activated, time-stretching is not used for length changes, and re-sampling is used instead. This
scales the early reflections as well.
EQ View
Reverb

EQ View contains a four-band EQ to shape the sound of the impulse response.
-
Gain controls Low Shelf, Low Mid, High Mid, and High Shelf boost/cut controls from -36 to +12 dB.
-
Frequency controls Low Shelf, Low Mid, High Mid, and High Shelf frequency controls
You can also click and drag any of the nodes in the EQ display to adjust Gain and Frequency simultaneously for any band.
Image View
Image View allows you to store a photo for easy reference of your impulse response source.
Click the [...] menu to select an image to import, or drag and drop one from your OS’ file browser. To see your photo full-size, just click the
photo. Click the “x” button in the top-right corner of the display to remove the current photo.
Images are saved and recalled with OpenAIR Presets.
Room Reverb
Reverb

Room Reverb is a room simulator reverb that adjusts its internal reverb parameters based on virtual-room models. It is meant for use as
a send effect or as a Main Output Channel effect. Room Reverb features variable room parameters and geometry, selectable room mod-
els, and population, damping, and surface-smoothness controls.
Room Reverb provides the following parameters:
-
Pre Adjusts the offset for room-derived natural predelay amount. Variable from 0 ms to a higher value determined by current
Room settings.
-
Length Adjusts the offset for room-derived natural reverb tail length. Value range is variable based on current Room settings.
-
Reverb Mix Adjust the mix of the reverb tail and early reflections. Variable from 0 to 1. Reverb display is updated to indicate this
mix.
-
Room
-
Type Select one of four Room Type models: Small Room, Room, Medium Hall, or Large Hall.
-
Size Adjusts the geometric average of the width, depth, and height of the virtual-room model. Variable from 1 m to 20 m.
-
Width Adjusts the width relative to size. Variable from 0.1 to 2.
-
Height Adjusts the height relative to size. Variable from 0.1 to 1.
-
Display Displays the overall reverb characteristics across a self-adjusting time scale. Early reflections are represented by ver-
tical lines, and the reverb tail is represented by a colored envelope.
-
Character
-
Population Adjusts the relative population of people in the virtual room. Variable from 0 to 1.
-
Value of 0 results in enhanced bass, “static” tail.
-
Value of 1 results in attenuated bass, “moving” tail.
-
Reflexivity Adjusts the relative smoothness of the surfaces of the virtual room. Variable from 0 to 1. Higher values
evoke a more echo-like reverb tail.
-
Dampness Adjusts the relative humidity of the air in the room. This has the effect of attenuating the upper frequencies
of the reverberated signal. Variable from 0 to 1.
-
Geometry
-
Dist Adjusts the relative distance between the source and the listener position within the virtual room. Variable from 0.1
to 1.
Reverb

-
Asym. Adjusts the left and right asymmetry between the source and the listener position. Variable from -1 (listener pos-
ition far right) to 1 (listener position far left).
-
Plane Adjusts the relative height of the stereo source and listener position within the virtual room. Variable from 0 (half
the height of the room) to 1 (ceiling).
-
Room Model Select a synthetic reverb model: Small Room, Room, Medium Hall, and Large Hall.
-
W, D, H Display Displays approximate room dimensions based on current Room settings.
-
Global
-
Eco/HQ Mode HQ mode (High Quality) is selected by default. Engage Eco (economy performance mode) to use fewer
CPU resources by disabling floor and ceiling reflections and reducing the calculation accuracy for the reverberation.
Eco Mode is available for all speaker setups, ranging from mono to stereo (up to 9.1.6 spatial audio). While Eco Mode
improves CPU performance, keep in mind this benefit comes with the cost of a lower grade of detail.
-
Mix Adjusts the mix of the Room Reverb signal with the original dry signal. Variable from 0 to 100%.
-
Lock Mix Level Locks the Mix control in place.

## Pipeline XT

As mentioned in the Removing Inserts section, Pipeline XT allows hardware processors to be inserted on Audio Channels in much the
same way that virtual effects are inserted. This feature is commonly called a “hardware insert.”
Configuring an Instance of Pipeline XT
Insert an instance of Pipeline on any Channel just like any other effect, either by dragging it in from the Browser, or through the Add menu
in the Insert Device Rack. Note that there are Mono and Stereo versions of Pipeline XT. Use the version that is appropriate for your hard-
ware processor. If your processor is mono-in-stereo-out (as with some delay and reverb units), use the stereo version of Pipeline XT and
feel free to assign a mono send and a stereo return.

## Pipeline XT

Automatic Latency Compensation
Pipeline XT automatically compensates for the latency involved in routing audio from Studio One to your audio interface and back. This is
based on the reported input and output latency from your hardware interface driver. The roundtrip latency being compensated for is dis-
played in milliseconds at the top of the Pipeline XT interface and can be manually adjusted if necessary.
Automatic Audio Routing Latency Compensation
For practical purposes, analog hardware processors do not introduce latency (aside from the latency introduced by the interface), as
their processing takes place at close to the speed of light. However, a few other sources of latency may affect the signal, including
DA/AD-converter latency and digital signal processing (DSP) latency.
This latency is not compensated for automatically, which could result in the signal being delayed very slightly, altering its phase rela-
tionship to the rest of the mix. To compensate for this, tap the Auto button. This sends a "ping" signal through your external processor,
then measures the time it takes for that signal to return, and automatically compensates for this latency.
Before clicking Auto, set the hardware processor to be in Bypass, if possible, so that no processing is done on the signal. You also want
the send and return signal levels to match as closely as possible.
To make manual timing adjustments, manipulate the Offset control. The Offset value is added to the total roundtrip latency. Setting a pos-
itive value increases the latency-compensation time, and setting a negative value decreases the latency-compensation time.
As you move the knob or set a value, the signal path is automatically pinged again, and the scope updates to provide instant feedback on
the calibration.
You can also click on the [Difference] button to see the difference between the send and return signals. The smaller the waveform
becomes (less amplitude), the more aligned the signals are. This is also helpful for matching send and return levels.
Once you have the correct Offset value established, you should store a preset, as described in the next section. You can get back to the
normal mode by clicking the wrench-shaped button.
Once you do this, the real-time send and return signals are displayed. Using the Sensitivity fader, it is possible to trigger the display to
only update based on detected transients. For instance, you may want to see how the kick and snare drums are lining up from a drum-
bus channel, and you’d want to avoid having the scope display the entire signal all of the time. To do this, move the Sensitivity fader to
the right until the only the transients you want to see—in this case a kick or snare hit—are displayed.
Images and Notes
When working with external processors in the context of a DAW, one challenge you may run into is settings recall. When returning to a
Song after your initial work, you may find that your external processors have been reconfigured for another use in the meantime. So, how
to recall your original settings?
Pipeline XT gives you two useful ways to jog your memory: Images and Notes.
To add a photo of the current settings for your external processor, first click the Show Image button in the lower left part of the plug-in win-
dow, then drag your photo into the center of the window. Alternatively, click the “…” button in the top-rigth corner of the display area to
access your file system and add an image manually. You can reference this photo anytime by clicking the Show Images button again. To
see your photo full-size, just click the photo. Click the “x” button in the top-right corner of the display to remove the current photo.
To enter a text note with settings information or other important info, click the Show Notes button. This shows a text field to the right of the
button. Click within this field and type in your information.
Images and Notes are stored with each instance of Pipeline XT in your song and will be saved with presets, so they're always available to
help.
Pipeline XT Controls
-
Setup Mode Shows or hides the "Ping" signal overlay.
-
Auto Automatically "pings" your external processor send/return chain and compensates for any latency induced by AD/DA con-
verters and hardware processors.
-
Offset Set an offset value in samples to account for the latency induced directly by AD/DA converters and hardware processors.
-
Label Click in the empty space to type in a label. This is used to clearly identify the inserted hardware.
-
Send Selection Select the output Channel that is used to route audio from Studio One to your hardware processor.
-
Return Selection Selects the input Channel that is used to route audio from your hardware processor into Studio One.

## Pipeline XT

Send and Return Controls:
-
Send Gain Adjust the send gain to prevent clipping the hardware input.
-
Return Gain Adjusts the return gain as needed to prevent clipping after the hardware insert.
-
Phase Invert Inverts the phase of the return signal (relative to the send signal). This is useful when auditioning for calibration
purposes .
-
Mix Adjusts the mix of send and return signal. This makes parallel processing possible.
Realtime Display Controls:
-
Signal Scope Displays an oscilloscope view of the send and return signals, overlaid on one another for easy comparison.
-
Sensitivity Controls the update rate of the signal scope.
-
Difference Displays an oscilloscope view of the difference between input and output signals.
-
Zoom Displays a detailed view of the current signal.
To the far left and right of the Pipeline XT interface are Send and Return meters with separate clip indicators, enabling you to accurately
monitor send and return levels.
Change the Look
If you'd like to color-code your Pipeline XT instances for organizational purposes, or simply want a fresh new look, click the PreSonus
logo in the plug-in window to switch background colors.
Storing Pipeline Presets
Once Pipeline has been configured for a particular piece of hardware, you should store the setting as a preset so that the configuration
can be recalled at a later time, as with an effects preset. Any number of presets can be stored, which allows you to recall configurations
for any number of hardware processors. These presets appear under the Pipeline effect in the Browser, just like a preset stored for a vir-
tual effect.
If you create new I/O channels in the Audio I/O Setup while configuring a Pipeline preset, be sure to click on Make Default before exiting
the dialog. This ensures that the required I/O for that Pipeline preset is available in every Song and Project.
Normally, you would use only one instance at a time of Pipeline with a particular I/O configuration. However, it is possible to insert the
same Pipeline preset on multiple Channels, in which case the signal from each Channel effectively sums at the specified output, and that
summed signal returns from the hardware processor to every Channel simultaneously. While this might lead to interesting possibilities,
exercise caution, as levels could easily become excessive.
Mixing Down with Pipeline
When Pipeline XT is being used on an active channel in a Song, you must render a mixdown in real time, as this is required in order for
your hardware insert to be incorporated in the mix.
This is handled automatically, so that when any instance of Pipeline XT is inserted on a track that contains content in a Song or Project,
the mixdown is always done in real time. If Pipeline XT is only inserted on tracks that do not currently contain or produce audio, real time
rendering is not required.

## Pipeline XT
