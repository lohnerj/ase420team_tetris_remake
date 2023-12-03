# Design Doc

## Problem Domain:

- Users need a way to be challenged while playing our game
- Users need to be able to track and evaluate how well they’re doing
- Users need to be rewarded for their skill while playing our game
- Implement Features that meet the user’s needs:
    - Level System
    - Score System
    - Combo System
- Constraints:
    - Increased difficulty must be something visible to the user while also compatible with rest of game
    - Scoring mechanism must be in place visually appealing and not distracting
    - Reward system should not be out-of-character for the game yet it must also be rewarding in a way that means something to the user
    - Ensure that there’s not too much happening on the screen
    - Make sure players get points but not too many, also not to little
    - Make sure player does not level up too easily yet also not too hardly

## Architecture

### Level

- Placed at top of screen and increments by 1 every 500 points that the user gets
- Increases the speed at which the pieces drop by 10 multiplied by the last level

### Score

- Placed at the top of the screen and updated in real time
- Player receives 10 points for every piece dropped and 100 for every row cleared

### Combo

- Player receives points for the number of rows cleared when it's more than 2.
- Calculated by 50 multiplied by number of rows cleared