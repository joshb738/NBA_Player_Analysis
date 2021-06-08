## Model

This section was completed by:

- Josh B.
- Pierre-Olivier B.

### Primary Objective

Predicting player regression based on archtype in NBA. We will feed the dataset into PCA.

#### Which model did you choose and why?

By looking at what was done with a great success in other sports. We determine that our chance to have a great accuracy would be by using clustering.

#### How are you training your model?

##### Clustering

- A general cluster that have all the players and years to determine the archtype
- generate a KMeans (we conclude at 9 cluster would be a valid result by looking at the chart), the variable is 0.89 with 9 clusters and the deriatives confirm this is the most useful threshold.
- The model only works with complete dataset; We dropped the "na"
- Vizualise all clusters to confirm if our hypothesis seems correct that players have archetypes.
- By using, 'cluster_centers\_', 'components\_' and vectorize and determined the content of each cluster. This is be use to conclude on if our clusters are truly different.

##### Timeseries

- We uses the same cluster that we previously used.
- Compared the T0 to T1 and confirm if there is a variation
- Then we created a DataFrame for those that improved and those who regressed.

#### What is the model's accuracy?

From the two references at the bottom of this file, we should have an accuracy between 75% and 90%. For the timeseries, we stopped at 0.9148 which was 10 clusters to explain our model. This means we would have to find 10 styles of playing that result to a high or low VORP.

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
