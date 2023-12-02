## Problem Domain:
* Users need more customization in their regular tetris game.
* Users need some more difficulty once they master playing tetris with four block figures
* Implement features that meet the users needs: more figure options, change background option, and changes color schemes for figures.
* constraints: Users have to select from the given options. All background colors must be compatable with all color schemes to avoid invisible like figures.

## Architecture:
* Startup menu allows users to specify which options they want at startup.
* UI interaction, when a user clicks their option the code runs according to their selection.
* Strategy pattern to control the while loop in the game class.
* Factory Pattern to create the right figures. (4 block, 5 block, or 6 block).