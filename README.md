# vee-board-config

Shield configuration for [vee-board][1], a 36-key diodeless interpretation of the [corne][2].

Modify the vee_board.keymap for new layouts. The easiest way is to use the [keymap website][3].

Once committed [Github actions][4] builds the firmware automatically.

Alter the uploader.py file to make uploading the firmware easier once downloaded. The paths and filenames will need changing to suit.
Then call the file in the terminal everytime you want to flash the boards. Double press the reset button on the boards to flash them (one at a time)

[1]: https://github.com/v-Zak/vee_board
[2]: https://github.com/foostan/crkbd
[3]: https://nickcoutsos.github.io/keymap-editor/
[4]: https://github.com/v-Zak/zmk-config/actions

