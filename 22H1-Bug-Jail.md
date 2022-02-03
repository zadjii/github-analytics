# 22H1 Bug Jail

[Bug Jail Query](https://github.com/microsoft/terminal/issues?q=is%3Aopen+is%3Aissue+milestone%3A%2222H1%22+-label%3AIn-PR++label%3AIssue-Bug++-label%3AResolution-Fix-Committed)

### IME support
* [ ] [#6439] Make sure that key bindings work in all IMEs
* [ ] [#6186] Japanese IME doesn't preserve the text that it overwrites
* [ ] [#4052] When using IME in wt, user is unable to edit pending words by moving the cursor (with the arrow keys?)
* [ ] [#3730] Input method problem, cursor bar not following
* [ ] [#11479] Vietnamese IME word composition bug

### Localization
* [ ] [#12297] Bad german translation
* [ ] [#12183] German translation for FOR /F command description is incorrect
* [ ] [#12182] German translation for RENAME command description is incorrect
* [ ] [#10691] Spanish localization of "Summon Quake window" is weird (English original not too great)
* [ ] [#11210] Wrong pt-Br translation to "Close Tab"

### DefApp
* [ ] [#11749] Changing Console Host breaks Win 11 boot
* [ ] [#11676] [DefApp] Conhostv1 activation fails from runbox when Default Terminal is set
* [ ] [#11627] Running as a default terminal causes app to create terminal window
* [ ] [#10974] Windows Terminal Preview does not work with Visual Studio 2019.
* [ ] [#10453] [DefApp] Sometimes, the first launch of the day results in 0xc0000142
* [ ] [#11443] Opening a file in any Office app will restore your windows when you have defterm enabled
* [ ] [#11354] [1.12] Crash when persisting a defterm window

### Performance / Rendering
* [ ] [#10462] Extremely slow performance when processing virtual terminal sequences
* [ ] [#6974] Extremely lower performance when displaying too many box-shading glyphs
* [ ] [#3515] Extremely sluggish behavior when in full screen on a 4K monitor
* [ ] [#3075] Processing large data is extremely slow (in VMware)
* [ ] [#410] Rendering performance of chafa is very slow
* [ ] [#368] cmd execution and GCC compilation scripts slow
* [ ] [#10678] windows terminal preview bold / cut-off fonts

### Alt Buffer
* [ ] [#3686] ED3 in the alt buffer should erase the main scrollback buffer
* [ ] [#3493] Consider not wrapping the alternate screen on resize
* [ ] [#3492] Alternate screen shouldn't write to scrollback or normal screen

### A11y
* [ ] [#12052] [Terminal > Export Text]: Keyboard only users do not have option to use 'Export text' functionality.
* [ ] [#11996] [Settings]: The Name property of a focusable element (Font Weight, Background image path, Background opacity, Padding, Delete) must not be null.
* [ ] [#11973] [Command prompt>Find] : Screen Reader users are not getting any information about 'Search results'.
* [ ] [#11971] [Settings>Color schemes] : Keyboard focus jumps to first tab, when user activates 'Yes, delete color scheme' button.
* [ ] [#11809] UIA in conhost: incorrect word boundaries when text is selected
* [ ] [#7766] Screenreader NVDA is not able to read text in terminal
* [ ] [#5936] Opening a new tab with ctrl+shift+1 provides no spoken feedback with NVDA
* [ ] [#10911] Incoming text is periodically not read by screen readers
* [ ] [#9248] CommandPalette's keyboard accelerators not read properly sometimes
* [ ] [#9243] Windows Magnifier doesn't follow text cursor
* [ ] [#2176] Bug Report: ConHost Caption BoundingRects dissapeared

### Misc Conhost bugs
* [ ] [#10647] Cannot set SetConsoleCtrlHandler
* [ ] [#6759] ConIoSrvComm::Connect memory leak
* [ ] [#5843] conhost crashes on SetConsoleWindowInfo
* [ ] [#5310] Vim in WSL scrolls 3 lines when gaining focus with mouse click
* [ ] [#5271] Crash in ScrollConsoleScreenBuffer when destination coordinates overflow
* [ ] [#5033] conhost VK_F4 regression
* [ ] [#4628] ReadConsoleW fails with non-BMP characters
* [ ] [#4189] Can't bypass DOSkey macro with leading space
* [ ] [#4186] Discard old duplicates needs to be case-sensitive
* [ ] [#399] SetConsoleScreenBufferInfoEx color palette behavior broken
* [ ] [#335] GenerateConsoleCtrlEvent should not succeed when dwProcessGroupId is not a group ID
* [ ] [#3088] WSL Terminal Line Endings (the "exact wrap" bug)
* [ ] [#3483] Ctrl+Keys that can't be encoded as VT should still fall through as the unmodified character

### Misc Conpty
* [ ] [#11213] PSEUDOCONSOLE_INHERIT_CURSOR sends DSR CPR to terminal, if the process is closed before a response is received, conhost will max out a core
* [ ] [#6859] ConPTY: transmit DECSET/DECRST state when client application enters/exits ENABLE_VIRTUAL_TERMINAL_INPUT mode
* [ ] [#6056] Cannot scroll buffer in Terminal with inbox telnet client
* [ ] [#2712] Bug: When headless, GetLargestConsoleWindowSize reports a MUCH too small size

### SUI / Settings
* [ ] [#10688] Settings sometimes don't load when rapidly clicking save
* [ ] [#10609] Memory leak and other issues when saving settings
* [ ] [#9861] Settings from settings.json lost when updated to Version: 1.7.1033.0

### Others

* [ ] [#12072] Wrong character when pasting into Windows Terminal with a Windows Subsystem for Linux profile
* [ ] [#11793] Underline Keyboard Shortcut for Windows Terminal in Administrator mode missing in Win+X menu
* [ ] [#11777] Windows terminal path is different if launched with wt.exe
* [ ] [#11759] Console icon?
* [ ] [#11309] [#7422] may have regressed - click on the top pixel of a tab when maximized
* [ ] [#9914] Orphaned processes when terminal is force-closed by windows itself
* [ ] [#8663] OpenConsole crash when pasting emoji
* [ ] [#7197] WSL home directory behaviour unexpected
* [ ] [#6865] Windows Terminal text glitches when using vim !
* [ ] [#6692] Redrawing / flickering issues while using Magnifier
* [ ] [#5506] Terminal locks its starting directory; perhaps it shouldn't do that?
* [ ] [#3546] The text layout code is expecting the quantity of glyphs is equal to the cells allocated for each line
* [ ] [#1225] [host] If you resize in a fullscreen app and the cursor is past the right of a line, but above the bottom of the buffer, then we'll insert an extraneous newline with the cursor on it.
* [ ] [#663] CMD does not show Unix LF when pasting
* [ ] [#351] Exiting from Full Screen mode incorrectly restores window size



[#6439]: https://github.com/microsoft/terminal/issues/6439
[#6186]: https://github.com/microsoft/terminal/issues/6186
[#4052]: https://github.com/microsoft/terminal/issues/4052
[#3730]: https://github.com/microsoft/terminal/issues/3730
[#11479]: https://github.com/microsoft/terminal/issues/11479
[#12297]: https://github.com/microsoft/terminal/issues/12297
[#12183]: https://github.com/microsoft/terminal/issues/12183
[#12182]: https://github.com/microsoft/terminal/issues/12182
[#10691]: https://github.com/microsoft/terminal/issues/10691
[#11210]: https://github.com/microsoft/terminal/issues/11210
[#11749]: https://github.com/microsoft/terminal/issues/11749
[#11676]: https://github.com/microsoft/terminal/issues/11676
[#11627]: https://github.com/microsoft/terminal/issues/11627
[#10974]: https://github.com/microsoft/terminal/issues/10974
[#10453]: https://github.com/microsoft/terminal/issues/10453
[#11443]: https://github.com/microsoft/terminal/issues/11443
[#11354]: https://github.com/microsoft/terminal/issues/11354
[#10462]: https://github.com/microsoft/terminal/issues/10462
[#6974]: https://github.com/microsoft/terminal/issues/6974
[#3515]: https://github.com/microsoft/terminal/issues/3515
[#3075]: https://github.com/microsoft/terminal/issues/3075
[#410]: https://github.com/microsoft/terminal/issues/410
[#368]: https://github.com/microsoft/terminal/issues/368
[#10678]: https://github.com/microsoft/terminal/issues/10678
[#3686]: https://github.com/microsoft/terminal/issues/3686
[#3493]: https://github.com/microsoft/terminal/issues/3493
[#3492]: https://github.com/microsoft/terminal/issues/3492
[#12052]: https://github.com/microsoft/terminal/issues/12052
[#11996]: https://github.com/microsoft/terminal/issues/11996
[#11973]: https://github.com/microsoft/terminal/issues/11973
[#11971]: https://github.com/microsoft/terminal/issues/11971
[#11809]: https://github.com/microsoft/terminal/issues/11809
[#7766]: https://github.com/microsoft/terminal/issues/7766
[#5936]: https://github.com/microsoft/terminal/issues/5936
[#10911]: https://github.com/microsoft/terminal/issues/10911
[#9248]: https://github.com/microsoft/terminal/issues/9248
[#9243]: https://github.com/microsoft/terminal/issues/9243
[#2176]: https://github.com/microsoft/terminal/issues/2176
[#10647]: https://github.com/microsoft/terminal/issues/10647
[#6759]: https://github.com/microsoft/terminal/issues/6759
[#5843]: https://github.com/microsoft/terminal/issues/5843
[#5310]: https://github.com/microsoft/terminal/issues/5310
[#5271]: https://github.com/microsoft/terminal/issues/5271
[#5033]: https://github.com/microsoft/terminal/issues/5033
[#4628]: https://github.com/microsoft/terminal/issues/4628
[#4189]: https://github.com/microsoft/terminal/issues/4189
[#4186]: https://github.com/microsoft/terminal/issues/4186
[#399]: https://github.com/microsoft/terminal/issues/399
[#335]: https://github.com/microsoft/terminal/issues/335
[#3088]: https://github.com/microsoft/terminal/issues/3088
[#3483]: https://github.com/microsoft/terminal/issues/3483
[#11213]: https://github.com/microsoft/terminal/issues/11213
[#6859]: https://github.com/microsoft/terminal/issues/6859
[#6056]: https://github.com/microsoft/terminal/issues/6056
[#2712]: https://github.com/microsoft/terminal/issues/2712
[#10688]: https://github.com/microsoft/terminal/issues/10688
[#10609]: https://github.com/microsoft/terminal/issues/10609
[#9861]: https://github.com/microsoft/terminal/issues/9861
[#12072]: https://github.com/microsoft/terminal/issues/12072
[#11793]: https://github.com/microsoft/terminal/issues/11793
[#11777]: https://github.com/microsoft/terminal/issues/11777
[#11759]: https://github.com/microsoft/terminal/issues/11759
[#11309]: https://github.com/microsoft/terminal/issues/11309
[#7422]: https://github.com/microsoft/terminal/issues/7422
[#9914]: https://github.com/microsoft/terminal/issues/9914
[#8663]: https://github.com/microsoft/terminal/issues/8663
[#7197]: https://github.com/microsoft/terminal/issues/7197
[#6865]: https://github.com/microsoft/terminal/issues/6865
[#6692]: https://github.com/microsoft/terminal/issues/6692
[#5506]: https://github.com/microsoft/terminal/issues/5506
[#3546]: https://github.com/microsoft/terminal/issues/3546
[#1225]: https://github.com/microsoft/terminal/issues/1225
[#663]: https://github.com/microsoft/terminal/issues/663
[#351]: https://github.com/microsoft/terminal/issues/351
