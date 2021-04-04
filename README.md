# NBA-Winner-Predictor (Version 1.0)

## Introduction

Using the Python NBA API, I was able to create a script that predicts the outcome of NBA games before they commence. To read more about the NBA API, you can follow the following link. https://pypi.org/project/nba-api/

## Dataset -- Last Updated (April 1, 2021)

The dataset was created via the NBA API. Through the API **players** module, I was able to get a list of all active players that are playing in the NBA at the time that the module is called. From there, I was able to get the unique ID's associated with every player. Finally, using the new ID's I was able to use the **Player Game Log** and the **Season All* module to get statistics from each player starting with their first season. 

I have added the database as a separate file but if you would like to parse the data and experiment, you can look at the the *parser.py* file.

## Installation and How to Use

### Installation

There are a few additional libraries that are used in this model which can be found in the *requirements.txt* file. Additionally you can run the following command in your terminal.

```bash

pip install -r requirements.txt

```

The NBA API is also worth investigating. While it is included in the requirements txt file, it is worth installing and exploring.

```bash

pip install nba-api

```

### How To Use

Navigate to the *main.py* file. From there you can chnage the variable names to the Home Team and Away Team of your choosing depending on the game. Once teams have been selected, run the file.

## Methodology

Using the NBA API and the database that I created, you are able to find all the players that make up a certain team as well as all the historical stats associated with them. With that information at hand, I decided to pick 5 random players from each team, normalize the data, and add up the total points that each player would receive on average. The winning team would be recorded. This process repeats 101 times. At the end of all 101 iterations, the team that has more predicted wins tallied would be declated the ultimate winner.

### Random Forests

The method that I used to precict winners is based off the random forests machine learning model. The reason I did not use the Random Forests Method directly is due to the fact that when predicting a game before it starts, there are no input values to initiate. That's to say, there is no information to feed into the model so that it could make a prediction. You can not use results of previous games directly because that woould imply that there is a correlation between prior games and future games and that is not what this project was set out to prove.

### Noise

There is always some variance that must be taken into consideration when working with data relating to sports. A player is not going to consistenly score the same exact amount of points every single game. For that reason, with every iteration, there was a random amount of noise applied to each player from each time to take into account these variations. The noise added was selected at random using the mean and variance between the five randomly selected players with each iteration before normalizing the data.

A Z-score was detected to allow the same amount of noise to be scaled down after normalization.

## Results

At the time of writing, the database has data recorded up until April 1, 2021. For that reason I decided to test my model on all 10 games that were played the following day, April 2, 2021.

The following confusion table was created with the results of each game.

![Confusion](https://user-images.githubusercontent.com/74287805/113521187-abf5d500-954c-11eb-96d4-ccaf0a7d3ec8.png)

From there we calculate the following results.

- Accuracy = **70%**

- Preciison = **71%**

- Recall = **83**

At this point in time, the sample size is too small to determine the efficacy of this model. First results are promising, but only time will tell.

## To Do List

- Incorporate an Injured Player Databse to incorporate to improve accuracy
- Incoporate a player "experience" variable to improve accuracy.
- Fix database so that every single player shows up include players that have not played.

## Changelog

### Version 1.0
- Release.
