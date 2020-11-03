
To remove build log spam on failure: https://stackoverflow.com/questions/33191173/sublime-text-3-showing-unnecessary-output

Shell:
`$ZSH/themes/agnoster.zsh-theme` and add a newline to the prompt.

    # End the prompt, closing any open segments
    prompt_end() {
      if [[ -n $CURRENT_BG ]]; then
        echo -n " %{%k%F{$CURRENT_BG}%}$SEGMENT_SEPARATOR \n$SEGMENT_SEPARATOR"
      else
        echo -n "%{%k%} \n$SEGMENT_SEPARATOR"
      fi
      echo -n "%{%f%}"
      CURRENT_BG=''
    }



MacOS:
use iTerm2.
https://apple.stackexchange.com/questions/48502/how-can-i-permanently-add-my-ssh-private-key-to-keychain-so-it-is-automatically
System Settings -> keyboard -> map capslock to control
`subl ~/Library/KeyBindings/DefaultKeyBinding.Dict`
Make text nagivation shortcuts similar to Linux/Windows: http://benogle.com/2010/01/18/windowslinux-developers-remap-your-mac.html


    /*
    This file remaps the key bindings of a single user on Mac OS X 10.5 to more closely
    match default behavior on Windows systems.  This particular mapping assumes
    that you have also switched the Control and Command keys already.

    This key mapping is more appropriate after switching Ctrl for Command in this menu:
    Apple->System Preferences->Keyboard & Mouse->Keyboard->Modifier Keys...->
    Change Control Key to Command
    Change Command key to Control
    This applies to OS X 10.5 and possibly other versions.

    Here is a rough cheatsheet for syntax.
    Key Modifiers
    ^ : Ctrl
    $ : Shift
    ~ : Option (Alt)
    @ : Command (Apple)
    # : Numeric Keypad

    Non-Printable Key Codes

    Up Arrow:     \UF700        Backspace:    \U0008        F1:           \UF704
    Down Arrow:   \UF701        Tab:          \U0009        F2:           \UF705
    Left Arrow:   \UF702        Escape:       \U001B        F3:           \UF706
    Right Arrow:  \UF703        Enter:        \U000A        ...
    Insert:       \UF727        Page Up:      \UF72C
    Delete:       \UF728        Page Down:    \UF72D
    Home:         \UF729        Print Screen: \UF72E
    End:          \UF72B        Scroll Lock:  \UF72F
    Break:        \UF732        Pause:        \UF730
    SysReq:       \UF731        Menu:         \UF735
    Help:         \UF746

    NOTE: typically the Windows 'Insert' key is mapped to what Macs call 'Help'.
    Regular Mac keyboards don't even have the Insert key, but provide 'Fn' instead,
    which is completely different.
    */

    {
    "@\UF702"  = "moveWordBackward:";                            // Cmd  + LeftArrow
    "@\UF703"  = "moveWordForward:";                             // Cmd  + RightArrow
    "@$\UF702" = "moveWordBackwardAndModifySelection:";   // Shift + Cmd  + Leftarrow
    "@$\UF703" = "moveWordForwardAndModifySelection:";   // Shift + Cmd  + Rightarrow
    "\UF729"  = "moveToBeginningOfLine:"; // home
    "\UF72B"  = "moveToEndOfLine:"; // end
    "$\UF729" = "moveToBeginningOfLineAndModifySelection:"; // shift-home
    "$\UF72B" = "moveToEndOfLineAndModifySelection:"; // shift-end
    "@\UF728" = "deleteWordBackward:"; // Cmd + Delete
    "@$\UF728" = "deleteWordForward:"; // Cmd + Shift + Delete




    "\UF729"   = "moveToBeginningOfLine:";                       /* Home         */
    "@\UF729"  = "moveToBeginningOfDocument:";                   /* Cmd  + Home  */
    "$\UF729"  = "moveToBeginningOfLineAndModifySelection:";     /* Shift + Home */
    "$@\UF729" = "moveToBeginningOfDocumentAndModifySelection:"; /* Shift + Cmd  + Home */
    "\UF72B"   = "moveToEndOfLine:";                             /* End          */
    "@\UF72B"  = "moveToEndOfDocument:";                         /* Cmd  + End   */
    "$\UF72B"  = "moveToEndOfLineAndModifySelection:";           /* Shift + End  */
    "$@\UF72B" = "moveToEndOfDocumentAndModifySelection:";       /* Shift + Cmd  + End */

    "^\UF702"   = "moveToBeginningOfLine:";                       /* Home         */
    "^\UF703"   = "moveToEndOfLine:";                             /* End          */
    "$^\UF703"  = "moveToEndOfLineAndModifySelection:";           /* Shift + End  */
    "$^\UF702"  = "moveToBeginningOfLineAndModifySelection:";     /* Shift + Home */

    "\UF72C"   = "pageUp:";                                      /* PageUp       */
    "\UF72D"   = "pageDown:";                                    /* PageDown     */
    "@x"  = "cut:";                                         /* Shift + Del  */
    "@v"  = "paste:";                                       /* Shift + Help */
    "@c"  = "copy:";                                        /* Cmd  + Help (Ins) */
    "@\UF702"  = "moveWordBackward:";                            /* Cmd  + LeftArrow */
    "@\UF703"  = "moveWordForward:";                             /* Cmd  + RightArrow */
    "$@\UF702" = "moveWordBackwardAndModifySelection:";   /* Shift + Cmd  + Leftarrow */
    "$@\UF703" = "moveWordForwardAndModifySelection:";   /* Shift + Cmd  + Rightarrow */
    }
