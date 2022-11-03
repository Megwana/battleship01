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
- [Testing](#)
- [Deployment](#structure)
- [Credits](#credits)

</details>

-----

# Introduction

# Features 

# Testing 

## Bugs 

1. While testing my game, I realised that you could press enter on any key and the game would continue without the personalised feature taking effect. To fix this, I added a while loop to ensure that should the name = less than 1 character, the game would repeatedly ask you until you typed one character or more for your user name. 

2. Counting number of successfully hit ships. While doing a test run, i realised the game was not registering that 3 ships had been hit and the game had not actioned the next stage. I realised i needed to add "for column in row:" underneath for row in board. As I had keyed if the '!' to be == to column then it would increment +1. 

# Deployment

# Credits

The general structure of the game is based off of Pranjal Dev's Battelship game.
However, I have made changes to create my own game.
#### [PRANJAL DEV](https://copyassignment.com/battleship-game-code-in-python/)