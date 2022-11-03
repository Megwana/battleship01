# **Battleship Game - Project 3**

Welcome to Battleships, a game that can be play in the command line using Python and deployed in Heroku.

![Battleships](/images/battleshipWelcomeImage.jpg)

-----

#### [Link to Deployed App in Heroku](https://battleship01.herokuapp.com/)

<details>
<summary>
Table of Contents - Click to Expand
</summary>

- [Introduction](#introduction)
- [Feature](#features)
- [Technology Used](#technology-used)
- [Testing](#)
- [Deployment](#structure)
- [Credits](#credits)

</details>

-----

# Introduction

I have selected project idea 2 for my Python command line application. It is based on the game [Battleships](https://en.wikipedia.org/wiki/Battleship_(game)).

My game is 1 player, the player must try to locate the enemy (computer)'s ships which are hidden on a 5 X 5 board.

The aim of the game is for the user to guess the 3 locations of the computer's hidden ships. 

! = explosion (A hit ship)
~ = a wave (open water, target missed)


# Features 

## Existing Features
* Welcome message
* Personalised name added to the introduction. 
* The user cannot continue unless they key a name of 1 character or more. 
* ships are hidden and auto generated at random each game using randint.
* The game keeps count of turns and remind the user each go. 
* The game registers when 3 ships have been hit, signalling game over. 
* The player must select a number 1-5 and A-E, otherwise they cannot continue. 
* The player is not allowed to pick the same coordinates again and is reminded if they have (no. turns are not deducted either).

## Future Features
* The implement the name feature at the end of the game to give the user a personalised congratulations or commiserations. 
* Allow larger ships more than 1X1.
* Implement an Easy, medium and hard and make the board bigger or reduce the number of turns a player can use.

# Technology Used

* [Python Language](https://www.python.org/)
    - [random randint](https://www.w3schools.com/python/ref_random_randint.asp) from Python
* [Node js](https://nodejs.org/en/)
* [Heroku](https://id.heroku.com) to deploy the project
* [W3 Schools]() 
* [PEP8 Online Checker](https://www.pythonchecker.com/)
* Code Institue Python Template

# Testing 

## Python Validatior 

I have checked my code on [PythonChecker PEP8 Standard](https://www.pythonchecker.com/) and it came back at 96%.

![PythonChecker](/images/PythonChecker.png)

## Fixed Bugs 

1. While testing my game, I realised that you could press enter on any key and the game would continue without the personalised feature taking effect. To fix this, I added a while loop to ensure that should the name = less than 1 character, the game would repeatedly ask you until you typed one character or more for your user name. 

2. Counting number of successfully hit ships. While doing a test run, i realised the game was not registering that 3 ships had been hit and the game had not actioned the next stage. I realised i needed to add "for column in row:" underneath for row in board. As I had keyed if the '!' to be == to column then it would increment +1. 

# Deployment

The first stage of deploying my game to Heroku was checking that nothing needed to imported to requriement.txt document. I had only used randint from random which is already installed into Python. But I carried out pip3 freeze > requirements.txt as a precaution. 

I had already set up my heroku login. 

The next stage required me to create an app in heroku.

Then connnect my Github and search for Battleship01. 

Once I had located this, I was able to add the buildpacks in the settings section, in the following order:
1. Python
2. Node.js

From here, I was able to go back to the deploy section and press deploy branch manually. I have enabled automatic deploys each time I add, commit and push to github. 

Once this had loaded, I was able to access my app through the [link](https://battleship01.herokuapp.com/).

# Credits

The general structure of the game is based off of Pranjal Dev's Battelship game.
However, I have made changes to create my own game.
### [Pranjal Dev](https://copyassignment.com/battleship-game-code-in-python/)

### [W3 Schools](https://www.w3schools.com/python/ref_func_input.asp)