### Problem Domain
* `Game Description:` The application implements the classic game of Tetris.
* `User Interaction:` Users interact with the game through mouse and keyboard inputs.
* `Game Mechanics:` Falling Tetris pieces are manipulated to complete lines and score points.
* `Sound:` Background music plays while user is in the game and various sound effects play during game.
* `Pause Condition:` The game can be paused and resumed at any point in the gameplay.
* `Game Over Condition:` The game ends when the player can not fit a new Tetris figure on the board.

### Architecture:
 `PlaySound Class` 
 * Manages the sound effects throughout the game
 * Uses Pygame's mixer module to play background music and various sounds through channels.

 `Gameover Class`
 * Displays the game over screen with an option to restart the game.
 * Handles user input to restart the game

 `Pause Class`
 * Manages state of game (paused versus playing/resume)
 * Handles user input to pause and resume game
