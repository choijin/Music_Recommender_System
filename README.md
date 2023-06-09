# Music Recommender System

Click [HERE](https://github.com/choijin/Music_Recommender_System) to see the full and detailed script

## Project Overview
Developed and evaluated a Collaborative Filtering Recommender System using the Alternating Least Squares (ALS) model. The model is designed to recommend songs to users based on implicit feedback (the count of songs listened to) for each user-item pair.

* Processed the data using PySpark on the NYU High Performance Computing (HPC) Dataproc cluster
* Implemented the ALS model for the recommender system and developed a popularity baseline model for comparison
* Assessed the performance of both models using the Mean Average Precision at K (MAP@K) metric

## Objectives
* Develop a collaborative filtering recommender system using ALS model
* Evaluate the model against a popularity baseline model
* Use MAP@K metric for performance assessment

## Part I. Data Preprocessing
### ListenBrainz
The data is downloaded from ListenBrainz using 2018, 2019, 2020 data for training and 2021 data for testing. 

### Schema information
**recording_msid**: string id given to a specific song. Since ListenBrainz collects data from multiple sources, a song can have different      recording_msids depending on which source the data came from.

**recording_mbid**: to mitigate the issue of there being many recording_msid for a song, ListenBrainz consolidated the recording_msids corresponding to a unique song, and came up with a unique string id. However, it is possible that there is no recording_mbid present.

**track_name**: song title

**artist_name**: artist name

**user_id**: a unique id for each users

### Data Cleaning
* **Missing or Irrelevant Data**: First, I checked the datasets for any missing or irrelevant data. This is similar to ensuring all the pieces of a puzzle are present before starting to assemble it.

* **Key Variables Identification**: Next, I explored the variables in the datasets to identify the 'key' variable. In this case, I found that a song could have multiple recording_msid assigned, but the recording_mbid was unique for each song, unless it was null.

* **Data Substitution**: If a song had a recording_mbid, I used this as the key variable, replacing the recording_msid. This helped us to uniquely identify each song in our dataset.

* **Noise Reduction**: To reduce noise in the data and focus on relevant information, I filtered out user_ids associated with less than 10 unique recording_msid, and vice versa. This is akin to removing outliers in a data set.

### Data Partitioning
* The goal was to partition the dataset into a train and validation set, with a split ratio of 8:2, ensuring every user in the training set also appears in the validation set to avoid the cold start problem
* Created a distinct list of 'recording_msid' for each user
* Split each user’s interactions into an 8 to 2 ratio, where 80% of the interactions go to the training set and the remaining 20% go into the validation set

## Part II. Model Development
### What is a Popularity Baseline Model?
A popularity baseline model is a simple recommendation system that suggests the most popular items to all users. In this context, popularity is determined by the number of times a song has been listened to.

While this model doesn't account for individual user preferences, it serves as a useful baseline to evaluate the performance of more complex models, such as the Alternating Least Squares (ALS) model used in this project.

#### Steps
* Calculated the popularity of each song based on the number of listens
* Recommended the top 100 most popular songs to all users 

### What is ALS?
Alternating Least Squares (ALS) is a the matrix factorization algorithm that Spark MLlib uses for Collaborative Filtering. ALS is implemented in Apache Spark ML and built for a large-scale collaborative filtering problems.

#### Steps
* Convert string song id to index (since ALS only takes integer values)
* Tune hyperparameters to find the best parameters for ALS model
* Implemented a Collaborative Filtering Recommender System leveraging the Alternating Least Squares (ALS) model to make song recommendations based on implicit user feedback

## Part III. Model Evaluation
### What is MAP@K?
Mean Average Precision at K (MAP@K) is a popular information retrieval metric used to evaluate the quality of the ranked lists of recommendations.

#### Steps
* Assessed the performance of both the ALS model and the popularity baseline model using the Mean Average Precision at K (MAP@K) metric
* Evaluation involves using the two models trained on the full training set and evaluate the MAP@100 score on both the validation and test set
* Analyzed and compared the effectiveness of the ALS model against the popularity baseline model

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
