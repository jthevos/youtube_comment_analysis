# CSIS 638 Final Project

## Project Summary
This project seeks to provide insight into data science educational content on YouTube by analyzing comments on tutorial videos. Data science specific videos will serve as the test group, and non-data sciecne Python tutorial videos will be used as the control group. Comments will be scraped with a Python script, classified manually with another script, and analyzed using standard statisitical techniques (z scores and logistic regression)

## Research Questions
_RQ1 - Do content correction comments occur more frequently in data science videos than in other coding tutorials?_

Because data science uniquely depends on input data for successful results, I would think fewer content correction comments are present in the comments on data science videos than others. 

_RQ2 - Do some comment catagories recieve a significant number more likes than others when normalized?_

Statisitcally signiciant differences in normalized content catagory could provide intetesting insight. A high number of likes on a content correction comment would suggest the correction helped several other viewers. If most liked comments are usually humorous in nature, that would indicate a more experienced viewer base as a novice might find esoteric humor innaccesible until they progress in the mastery of the topic. 

_RQ3 - Is there a "critical age" where a video becomes too old to be useful?_

This is the most interest question. I find that many data science videos are useful in theory; however, they are using a version of TensorFlow that has now depreciated methods or is outdated in some other way. The answer to this question could help content creators factor in a "half-life" to their content and update when needed. We define "useful" as a function of comment category composition in order to save time labeling the dataset. The function is a weak area conceptually and needs to be fleshed out more.

Methodology:
- We create a python script to scrape data science youtube comments and log their data into a csv.
- We use this same script to scape standard python tutorial youtube video comments and log their data into a separate csv.
- We write a quick python script to manually classify approx 300 comments into five catagories: Content corrections, unrelated, humorous, gratuitous, and misc. for both the data science and non data science videos.
- Using the non data science csv as our control, we perform simple stats tests to answer RQ1 and RQ2. 
- RQ3 can be answered with logistic regression; however, it might be difficult to infer "usefulness" from comment category composition. 

If time permits:
- Train a simple XGBoost or RNN machine learning model on these labeled data. 
- Add this model to an automated pipeline to classify comments on more videos. 


## Installation Instuctions
1. create and activate a virtual environment using `pyenv` and `venv`, `conda`, `virtualenv` or other tool.
2. activate this venv.
3. `pip install -r requirements.txt`
4. More when I get to this. There are no plans for a UI at this time. 
