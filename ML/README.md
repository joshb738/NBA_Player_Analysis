## Model

### Goal

Predicting player regression based on archtype in NBA

### Datasets

- NBA.com - https://pypi.org/project/nba-api/#description
- Kaggle - https://www.kaggle.com/drgilermo/nba-players-stats?select=player_data.csv-

### Steps

- First cluster players using data into archtype each year
- Cluster ONCE then assign each year based on years into career
- Look at VORP to see when if they regress
- VORP is value over replacement player basically how good a player was that season with a -2.0 being a replacement level player (really bad player)
- Also look at if they change player type do they still regress

Model 1: https://www.baseballdatascience.com/machine-learning-to-predict-player-decline/
Article: https://www.baseballdatascience.com/machine-learning-to-predict-player-decline/

Model 2: https://towardsdatascience.com/redefining-nba-player-classifications-using-clustering-36a348fa54a8
