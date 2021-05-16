## Model

### Goal

Predicting player regression based on archtype in NBA

#### Which model did you choose and why?

By looking at what was done with a great success in other sports. We determine that our chance to have a great accuracy would be by using clustering.

#### How are you training your model?

- First cluster players using data into archtype each year
- Cluster ONCE then assign each year based on years into career
- Look at VORP to see when if they regress
- VORP is value over replacement player basically how good a player was that season with a -2.0 being a replacement level player (really bad player)
- Also look at if they change player type do they still regress

#### What is the model's accuracy?

From the two references below we should have between 75% nad 85%

#### How does this model work?

We will use a voting classifier. It aggregate a logistic regression, adaptive boosting, gradient boosting, random forest, and extra trees.

- The database in the schema (NBA_Analysis_ERD.png)

- Filter to use the data from 2003 to 2018

### References

- NBA.com - https://pypi.org/project/nba-api/#description
- Kaggle - https://www.kaggle.com/drgilermo/nba-players-stats?select=player_data.csv-

Model 1: https://github.com/micahmelling/player_decline
Article: https://www.baseballdatascience.com/machine-learning-to-predict-player-decline/

Model 2: https://towardsdatascience.com/redefining-nba-player-classifications-using-clustering-36a348fa54a8
