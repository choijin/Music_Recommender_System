# Music Recommender System
> Click [HERE](https://github.com/choijin/Music_Recommender_System) to see the full and detailed script.

## Table of Contents
- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Part I. Data Preprocessing](#part-i-data-preprocessing)
- [Part II. Model Development](#part-ii-model-development)
- [Part III. Model Evaluation](#part-iii-model-evaluation)
- [Conclusion](#conclusion)

---

## Project Overview
This project involves the development and evaluation of a collaborative filtering recommender system using the Alternating Least Squares (ALS) model. The model recommends songs to users based on implicit feedback (the count of songs listened to) for each user-item pair.

## Objectives
1. Data processing using PySpark on the NYU High Performance Computing (HPC) Dataproc cluster.
2. Collaborative filtering recommender system development using ALS model.
3. Comparison of the model with a popularity baseline model.
4. Performance assessment of models using Mean Average Precision at K (MAP@K) metric.

---

## Part I. Data Preprocessing

### Data Source
Data was obtained from [ListenBrainz](https://listenbrainz.org/) using 2018, 2019, 2020 data for training and 2021 data for testing. 

### Data Cleaning
- Checked for missing or irrelevant data.
- Identified 'key' variables, and used the `recording_mbid` to uniquely identify each song.
- Noise reduction: filtered out `user_ids` associated with less than 10 unique `recording_msid`, and vice versa.

### Data Partitioning
- Partitioned the dataset into a train and validation set, with a split ratio of 8:2.
- Used user-based split to ensure every user in the training set also appears in the validation set to avoid the cold start problem.

---

## Part II. Model Development

### Popularity Baseline Model
A simple recommendation system that suggests the most popular items (songs in this case) to all users. Popularity was determined by the number of times a song has been listened to.

### ALS Model
Alternating Least Squares (ALS) is a matrix factorization algorithm used for Collaborative Filtering. The model was developed in Apache Spark ML for large-scale collaborative filtering problems.

---

## Part III. Model Evaluation

### MAP@K
Mean Average Precision at K (MAP@K) is an information retrieval metric used to evaluate the quality of the ranked lists of recommendations.

---

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

The ALS model's approach of leveraging implicit feedback (the count of songs listened to for each user-item pair) proved to be a more effective strategy for recommending songs to users, tailoring the recommendations to individual user preferences.
