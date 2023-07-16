# Music Recommender System

> [Project Source Code](https://github.com/choijin/Music_Recommender_System)

A collaborative filtering recommender system built with the Alternating Least Squares (ALS) model, designed to recommend songs to users based on implicit feedback (interaction count).

## Table of Contents
- [Data Preprocessing](#data-preprocessing)
  - [Data Source](#data-source)
  - [Data Cleaning](#data-cleaning)
  - [Data Partitioning](#data-partitioning)
- [Model Development](#model-development)
  - [Popularity Baseline Model](#popularity-baseline-model)
  - [ALS Model](#als-model)
- [Model Evaluation](#model-evaluation)
  - [MAP@K](#mapk)
- [Conclusion](#conclusion)
- [Results](#results)

---

## Data Preprocessing

### Data Source

The data was sourced from ListenBrainz, using 2018, 2019, 2020 data for training, and 2021 data for testing.

### Data Cleaning

1. Checked for missing or irrelevant data.
2. Identified 'key' variables (`recording_msid`, `recording_mbid`, `track_name`, `artist_name`, `user_id`).
3. If a song had a `recording_mbid`, it replaced the `recording_msid`. This helped to uniquely identify each song in the dataset.
4. Noise reduction: filtered out `user_ids` associated with less than 10 unique `recording_msid`, and vice versa.

### Data Partitioning

1. Partitioned the dataset into a train and validation set, with an 8:2 split ratio.
2. Ensured every user in the training set also appeared in the validation set (user-based split).
3. For each user, created a list of tuples with distinct 'recording_msid' and its count (interaction).
4. Split each user’s **interactions** into an 8 to 2 ratio.

---

## Model Development

### Popularity Baseline Model

1. Calculated the popularity of each song based on the number of listens.
2. Recommended the top 100 most popular songs to all users.

### ALS Model

1. Converted string song id to index (since ALS only takes integer values).
2. Tuned hyperparameters to find the best parameters for the ALS model.
3. Implemented a Collaborative Filtering Recommender System leveraging the Alternating Least Squares (ALS) model.

---

## Model Evaluation

### MAP@K

Evaluated the performance of both the ALS model and the popularity baseline model using the Mean Average Precision at K (MAP@K) metric. 

---

## Conclusion

The personalized ALS recommender system demonstrated a clear improvement in recommendation quality when compared to the popularity baseline model.

---

## Results

| Dataset          | Popularity Baseline Model | ALS Model |
|------------------|---------------------------|-----------|
| Validation Small | 0.0004942                 | 0.01628   |
| Validation Full  | 0.0004317                 | 0.02194   |
| Test             | 0.0009574                 | 0.05147   |

The ALS model effectively recommended songs to users based on their individual preferences, improving the MAP@K scores across all data sets.
