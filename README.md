# **Battleship Game - Project 3**

Welcome to Battleships, a game that can be played in the command line using Python and deployed in Heroku.

![Battleships](/images/battleshipWelcomeImage.jpg)

-----

#### [Click this Link to view the Deployed App in Heroku](https://battleship01.herokuapp.com/)
Preview Below: 

![Heroku Python Terminal](/images/AmIResponsiveBattle.png)

<details>
<summary>
Table of Contents - Click to Expand
</summary>

- [Introduction](#introduction)
- [Feature](#features)
- [Technology Used](#technology-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

</details>

-----

# Introduction

I have selected project idea 2 for my Python command line application. It is based on the game [Battleships](https://en.wikipedia.org/wiki/Battleship_(game)).

My game is 1 player, the player must try to locate the enemy (computer) ships which are hidden on a 5 X 5 board.

The aim of the game is for the user to guess the 10 locations of the computer's hidden ships. 

! = explosion (A hit ship)
~ = a wave (open water, target missed)

I did initially set the game to 15 turns, however, since running the game through, I felt 20 turns is more fitting. Especially because the player needs to find all 10 ships.

Originally, the game required the player to locate 3 ships. However, after test playing the game, I concluded that just 3 ships are quite hard to locate out of 25 spaces across the board. In gameplay, you would rarely have success locating a ship at all, which could take away the enjoyment of the game. 

Therefore, I decided that it would bring more enjoyment if players were more likely to come across ships by increasing the number to 10. However, the game is still kept it challenging as they are required to hit **all 10** in order to win.

After testing this number, users playing the game came across more ships which brought more of an interactive/exciting experience to the game rather than constantly seeing the 'miss' symbol and become bored never hitting anything.

Users still felt challenged playing the game because they had to locate more ships in order to win. 

These changes have balanced the experience of the game bringing more joy and excitement while still maintaining a challenge.

# Features 

## Existing Features
* Welcome message which explains the game and asks for the player's name.
* Name entry to add a personalisation to the game. 
* The user cannot continue unless they key a name of 1 letter or more. 
* Ships are hidden and auto-generated at random in each game using randint.
* The player must select a row number 1-5 and column letter A-E, otherwise they cannot continue. 
* The game does not allow any blank data to be input. 
  - Incorrect data or blank data is managed by **error/exception handling**. See below:
  
  The First example handles the player's name input. The player will be prompted if a number or blank entry has been input and ask them to type 1 letter or more:
  ![Name Value Error](/images/NameValueError.png)
  The Second example handles the Row input in `find_ships`. It prompts the player is a number not between 1 and 5 has been entered, incorrect input such as a letter or blank input. An error message will appear advising the player to input a number between 1 and 5. 
  ![Row Value Error](/images/RowValueError.png)
  The Third example handles the Column input in `find_ships`. An error message is provided if the player does input a letter between A and E, incorrect input such as a number or blank input. The player will be prompted each time to enter a letter between A and E. 
  ![Column Value Error](/images/ColumnValueError.png)
* The player is not allowed to pick the same coordinates again and is reminded if they have (The number of turns are not deducted either). The example below shows the first time it is input and then the message that appears should they be input again.
![Same Coordinates](/images/SameCoordinates.png)

* The player has 20 Turns to locate the hidden ships on the board. 
![20 Turns](/images/20turns.png)

* The game keeps count of turns and reminds the user each go. 
![Turns](/images/No.Turns.png)

* The game registers when 0 turns are remaining, signalling "game over". 
![Loser](/images/LostGame.png)

* The game registers when 10 ships have been hit, signalling "game over". 
![Winner](/images/WinGame.png)

* When the play wins/ loses they will be prompted to either exit the game or play again.
![Play Again](/images/ExitGame.png) 

## Future Features
* To implement the name feature at the end of the game to give the user a personalised congratulations or commiserations. 
* When the player selects `y` to play again, it saves the players name from the last game and does not need to ask for their name again.
* Allow larger ships more than 1X1.
* Implement an Easy, medium, and hard and make the board bigger or reduce the number of turns a player can use.


# Technology Used

* [Python](https://www.python.org/)
    - [random randint](https://www.w3schools.com/python/ref_random_randint.asp) from Python
* [Node js](https://nodejs.org/en/)
* [Heroku](https://id.heroku.com) to deploy the project
* [W3 Schools](https://www.w3schools.com) 
   - To check/ research actions to carry out.
* [PEP8 Online Checker](https://www.pythonchecker.com/)
  - To ensure Python code meets appropriate PEP8 Standards.
* [Code Institue Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template)
* [Grammarly](https://www.grammarly.com/a?utm_source=google&utm_medium=cpc&utm_campaign=brand_core_row&utm_content=brandcorerow&utm_term=grammarly&matchtype=e&placement=&network=gt%7d&network=g&gclid=CjwKCAjwzY2bBhB6EiwAPpUpZlsGqYATQkfUFW8wozDtRB9oeULmkiNT00iSLkwm9qYXjWWB4XjZPRoCE0MQAvD_BwE&gclsrc=aw.ds)
   - To check for spelling/ grammar issues. 
* [Am I Responsive](https://ui.dev/amiresponsive)
  - To preview what the python terminal looks like in Heroku via the README.md.

# Testing 

## Python Validator 

I have checked my code on [PythonChecker PEP8 Standard](https://www.pythonchecker.com/) and it came back at 100%. I screenshoted two images showing the total number of lines of code as it was not registering the additional lines in one.

Part 1 = 110 lines and Part 2 = 85 Lines totalling to the 195 Lines of code in `run.py`.

![PythonChecker Part 1](/images/PythonChecker1.png)

![PythonChecker Part 2](/images/PythonChecker2.png)

## Game Checks

* Name Input Testing = **No Empty or Invalid data Entry**
  - I checked that the loop for the name personalisation works. 
  
  The game prompts the user to input at least 1 character or more. The user cannot proceed if a blank input is made or if numbers are typed in.
    - [Name Test](/images/NameTest.png)

* Row and Column Testing = **No Empty or Invalid data Entry**
  - That numbers and letters outside of 1 to 5 and A to E could not be input as valid for the row and column.
  - That **EMPTY INPUTS** cannot be made for the row and column.
    - [Row Test](/images/RowTesting.png)
    - [Column Test](/images/ColumnTesting.png)

* That the symbol of hit or miss appears after the player entry.
  - [Hit](/images/HitMessage.png)
  - [Miss](/images/MissMessage.png)

* The player is shown how many turns they have left so they can keep track.
  - [Number of Turns](/images/No.Turns.png)

* Same Coordinates Testing
  - The player cannot input the same coordinates and will be prompted to re-enter.
  - The player does not lose turns if they enter duplicate coordinartes.
    - [Same Coordinates](/images/SameCoordinates.png)

* Board showing 5X5 and letters and numbers are all in line. 
  - [Board Alligned](/images/BoardAlligned.png)

* When the number of turns reach 0 the game ends.
  - [0 Turns](/images/LostGame.png)

* When the number of ships hit is 10, the game ends. 
  - [10 Ships Hit](/images/WinGame.png)

* Game End Testing = **No blank or invalid data entry**
  - When the game ends, whether the player won or lost; they are prompted to input 'y' or 'n'. If a blank input or anything other that 'y' or 'n' is input. The game will ask the player to input 'y' or 'n'. See testing below of this when testing both 'y' and 'n' functionality:

    - When 'y' is selected, the game will ask the user to re-enter their name and play again.
      - [Play Again](/images/PlayAgain.png)
    - When 'n' is selected, the game will exit the python game.
      - [Exit Game](/images/ExitGame.png) 

* The board resets if the player choses to play again. 
  - [Board Reset](/images/BoardReset.png)

* The boards hidden ships are randomly places each new game. 
  - Comparison example of two different games: 

    ![Ships Hidden Randomly Each Time pt1](/images/boardA.png)
    ![Ships Hidden Randomly Each Time pt2](/images/BoardB.png)

## Fixed Bugs 

1. While testing my game, I realised that you could press enter on any key and the game would continue without the personalised feature taking effect. To fix this, I added a while loop to ensure that should the name = less than 1 character, the game would repeatedly ask you until you typed one character or more for your user name.

In addition, I have added a ValueError feature to ensure users must have a name with letters and not numbers.

2. Counting the number of successfully hit ships. While doing a test run, I realised the game was not registering that 3 ships had been hit and the game had not actioned the next stage. I realised I needed to add "for column in row:" underneath for "row in board". As I had keyed if the '!' to be == to column then it would increment +1. 

3. The game would break in multiple places due to lack of error handling placed. I have since inserted multiple improvements such as:
- The game no longer breaks if empty data is input. 
- The game can end or restart should the user select yes or no (y / n). This applies to both instances, if they win or lose.
- Players can no longer input their first name with any digits, it will only allow 1 letter or more.

4. The game would print the old guess board from the previous game if the player opted 'y' to play again. To fix this, I created a reset_board function. That will reset the board and hidden pattern. This is then called after the welcome function in the `main` game play. 

To conclude, the game use to previously break due to lack of error/exception handling which allowed blank entries to be input. However, this is no longer an issues and the game runs consistently.

# Deployment

The first stage of deploying my game to Heroku was checking that nothing needed to be imported to the requirement.txt document. I had only used randint from random which is already installed in Python. But I carried out pip3 freeze > requirements.txt as a precaution. 

I had already set up my Heroku login. 

The next stage required me to create an app in Heroku.

Then connect my Github and search for Battleship01. 

Once I had located this, I was able to add the buildpacks in the settings section, in the following order:
1. Python
2. Node.js

From here, I was able to go back to the deploy section and press the deploy branch manually. I have enabled automatic deploys each time I add, commit and push to GitHub. 

Once this had loaded, I was able to access my app through the [link](https://battleship01.herokuapp.com/).

# Credits

Thank you to my mentor Akshat Garg for reviewing my project and providing feedback. 

The general structure of the game is based on Pranjal Dev's Battleship game.
However, I have made changes to create my own game.
### [Pranjal Dev](https://copyassignment.com/battleship-game-code-in-python/)

W3 Schools was very helpful in researching. Especially for the name personalisation. 
### [W3 Schools](https://www.w3schools.com/python/ref_func_input.asp)