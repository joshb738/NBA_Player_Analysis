## Model

### Primary Objective

Predicting player regression based on archtype in NBA. We will feed the dataset into PCA.

#### Which model did you choose and why?

By looking at what was done with a great success in other sports. We determine that our chance to have a great accuracy would be by using clustering.

#### How are you training your model?

- First cluster players using data into archtype each year
- Cluster ONCE then assign each year based on years into career
- Look at VORP to see when if they regress
- VORP is value over replacement player basically how good a player was that season with a -2.0 being a replacement level player (really bad player)
- Also look at if they change player type do they still regress

#### What is the model's accuracy?

From the two references at the bottom of this file, we should have an accuracy between 75% and 85%

#### How does this model work?

We will use a "voting classifier". It aggregate a logistic regression, adaptive boosting, gradient boosting, random forest, and extra trees.

- The database in the schema (NBA_Analysis_ERD.png)

- Filter to use the data from 2003 to 2018

- For example, our dataset will include the year, is it his first year, salray, position (e.g. 3B) then each cluster will have parameters for each player.

E.g.

##### 3 and D Players (3 Point and Defensive Players)

The Cluster has the following traits:

- High 3 Point percentage
- High Steals/game
- High Perimeter Field Goals/game
- High Post and Perimeter Defended Field Goals/game
- Majority of Cluster 5’s offense come from Spot up shots

Refer to:

- The file: Model.drawio
- Model 2: https://towardsdatascience.com/redefining-nba-player-classifications-using-clustering-36a348fa54a8

### References

- NBA.com - https://pypi.org/project/nba-api/#description
- Kaggle - https://www.kaggle.com/drgilermo/nba-players-stats?select=player_data.csv-

Model 1: https://github.com/micahmelling/player_decline
Article: https://www.baseballdatascience.com/machine-learning-to-predict-player-decline/

Model 2: https://towardsdatascience.com/redefining-nba-player-classifications-using-clustering-36a348fa54a8