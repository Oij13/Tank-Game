# Tank-Game

You and a friend fight in an arena to the best of 3! Player 1 uses WASD to move and F to shoot and player 2 uses IJKL to move and H to shoot.

Game States:

## Intro Screen:
![Screenshot 2024-04-23 111952](https://github.com/Oij13/Tank-Game/assets/156932008/232f0378-cff2-41ec-b2d7-741ea41ade4a)

- Show Instructions
- Start Button (Start game)
- Quit Button (Exit game)

## Game Play:
![Screenshot 2024-04-23 112430](https://github.com/Oij13/Tank-Game/assets/156932008/cecee3c8-b94a-47b2-b63c-7c7770c1833b)

- Show predetermined map
- Give each user a score of 0
- Every hit to the other player increases the other's score by one
- Each hit moves hit player to opposite side of the screen from attacker
- First to 3 points wins (shows winner screen when player hits 3 points)

Game Over:
- Declares winner
- Shows play again btn (starts game over)
- Quit button shown

  Player win screen:
- Shows "Player [winner] Wins!" in text box
- Play again button (starts from Game Play screen)
- Quit button (goes to home screen)

  


## Sprites:
  Player1:
- User-controlled green tank sprite
- Rotate tank with A and D
- Move forward with W
- Backwards in facing direction with S
- Shoots with F in the directions the barrel is facing
- Cant pass through outer barrier or cover barriers
- Starts on left screen

  Player2:
- User-controlled red tank sprite
- Rotate tank with J and L
- Move forward with I
- Shoots with H in the direction the barrel is facing
- Cant pass through outer barrier or cover barriers
- Starts on right screen

  Bullets:
- Shoots in direction of barrel on either tank sprite
- if bullet on one player hits other player while their bullet is in motion, it resets the hit players bullet as well
      - Gets rid of simultaneous hits
- Sound effects from firing of bullet and colliding of bullet

  Barriers:
- Stops bullets
- Stops tank movement
- Keeps sprites from moving off the screen or through cover barriers
- Placed in predetermined locations
- Moves tank sprites to keep from going through barriers

  Player win screen:
- Shows "Player [winner] Wins!" in text box
- Play again button (starts from Game Play screen)
- Quit button (goes to home screen)

## UI Components
- Background
      - Rocky
      - Contrasts well with tanks and barriers
- LblScore
      - Adds a score for each tank
      - Adds by one for each hit on the opposing tank
      -
- LblStart
      - Starts game when clicked
      - Appears on title screen and win screen
- LblQuit
      - Quit the entire game when clicked
      - Appears on title screen and win screen
  





  
