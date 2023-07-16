# Music Recommender System

Click [HERE](https://github.com/choijin/Music_Recommender_System) to see the full and detailed script

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Part I. Data Preprocessing](#part-i-data-preprocessing)
- [Part II. Model Development](#part-ii-model-development)
- [Part III. Model Evaluation](#part-iii-model-evaluation)
- [Conclusion](#conclusion)

## Project Overview
Developed and evaluated a collaborative filtering recommender system using the Alternating Least Squares (ALS) model. The model is designed to recommend songs to users based on implicit feedback (the count of songs listened to) for each user-item pair.

## Objectives
1. Process the data using PySpark on the NYU High Performance Computing (HPC) Dataproc cluster.
2. Develop a collaborative filtering recommender system using ALS model.
3. Evaluate the model against a popularity baseline model.
4. Assess the performance of models using the Mean Average Precision at K (MAP@K) metric.

## Part I. Data Preprocessing
### Data
Data was obtained from [ListenBrainz](https://listenbrainz.org/) using 2018, 2019, 2020 data for training and 2021 data for testing.

* **`recording_msid`**: string id given to a specific song. Since ListenBrainz collects data from multiple sources, a song can have different recording_msids depending on which source the data came from.

* **`recording_mbid`**: to mitigate the issue of there being many recording_msid for a song, ListenBrainz consolidated the recording_msids corresponding to a unique song, and came up with a unique string id (recording_mbid). However, it is possible that there is no recording_mbid present.

* **`track_name`**: song title

* **`artist_name`**: artist name

* **`user_id`**: a unique id for each users


### Data Cleaning
* **`Missing or Irrelevant Data`**: First, I checked the datasets for any missing or irrelevant data.

* **`Key Variables Identification`**: Next, I explored the variables in the datasets to identify the 'key' variable. In this case, I found that a song could have multiple recording_msid assigned, but the recording_mbid was unique for each song, unless it was null.

* **`Data Substitution`**: If a song had a recording_mbid, I used this as the key variable and replaced the recording_msid to recording_mbid. This helped us to uniquely identify each song in our dataset.

* **`Noise Reductio`n**: To reduce noise in the data and focus on relevant information, I filtered out user_ids associated with less than 10 unique recording_msid, and vice versa. This is akin to removing outliers in a data set.

### Data Partitioning
* The goal is to partition the dataset into a train and validation set, with a split ratio of 8:2.
* Ensure every user in the training set also appears in the validation set to avoid the cold start problem (user-based split).
* For each user, created a list of tuples with distinct `recording_msid` and its count (interaction).
* Split each user’s **interactions** into an 8 to 2 ratio, where 80% of the interactions go to the training set and the remaining 20% go into the validation set.

## Part II. Model Development
### What is a Popularity Baseline Model?
A popularity baseline model is a simple recommendation system that suggests the most popular items to all users. In this context, popularity is determined by the number of times a song has been listened to.

While this model doesn't account for individual user preferences, it serves as a useful baseline to evaluate the performance of more complex models, such as the Alternating Least Squares (ALS) model used in this project.

#### Steps
1. Calculate the popularity of each song based on the number of listens.
2. Recommend the top 100 most popular songs to all users .

### What is ALS?
Alternating Least Squares (ALS) is a the matrix factorization algorithm that Spark MLlib uses for Collaborative Filtering. ALS is implemented in Apache Spark ML and built for a large-scale collaborative filtering problems.

#### Steps
1. Convert string song id to index (since ALS only takes integer values).
2. Tune hyperparameters on validation set to find the best parameters for ALS model.
3. After hyperparameter tuning, fit the Alternating Least Squares (ALS) model on the full train data.

## Part III. Model Evaluation
### What is MAP@K?
Mean Average Precision at K (MAP@K) is a popular information retrieval metric used to evaluate the quality of the ranked lists of recommendations.

#### Steps
1. After fitting the ALS model, predict the 100 recommended songs per user.
2. Assess the performance of the model by evaluating MAP@100 on predicted result and the test set.
3. Analyze and compare the effectiveness of the ALS model against the popularity baseline model.

## Conclusion
### Results
The popularity baseline model yielded the following Mean Average Precision at 100 (MAP@100) scores:

| Dataset          | MAP@100   |
|------------------|-----------|
| Validation Small | 0.0004942 |
| Validation Full  | 0.0004317 |
| Test             | 0.0009574 |

The ALS model yielded the following Mean Average Precision at 100 (MAP@100) scores:

| Dataset          | MAP@100 |
|------------------|---------|
| Validation Small | 0.01628 |
| Validation Full  | 0.02194 |
| Test             | 0.05147 |


These results demonstrate a clear improvement in recommendation quality when using the personalized ALS recommender system, as compared to the popularity baseline model.

This suggests that the ALS model's approach of leveraging implicit feedback (the count of songs listened to for each user-item pair) is a more effective strategy for recommending songs to users, as it tailors the recommendations to individual user preferences.
