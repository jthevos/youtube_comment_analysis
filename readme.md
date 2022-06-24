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


### Sources
E. Poché, N. Jha, G. Williams, J. Staten, M. Vesper and A. Mahmoud, "Analyzing User Comments on YouTube Coding Tutorial Videos," 2017 IEEE/ACM 25th International Conference on Program Comprehension (ICPC), 2017, pp. 196-206, doi: 10.1109/ICPC.2017.26.

This paper uses Naive Bayes and Support Vector Machines. I think XGBoost or an RNN would be better. Data science uniquely relies on the input data for successful results. Will comments even help with this? 

H. Bhuiyan, J. Ara, R. Bardhan and M. R. Islam, "Retrieving YouTube video by sentiment analysis on user comment," 2017 IEEE International Conference on Signal and Image Processing Applications (ICSIPA), 2017, pp. 474-478, doi: 10.1109/ICSIPA.2017.8120658.

This source presents a compelling NLP approach, but a video being positively received does not necessarily correlate to its utility as a tutorial - especially after a certain time frame. 

Luo, T., Freeman, C. & Stefaniak, J. “Like, comment, and share”—professional development through social media in higher education: A systematic review. Education Tech Research Dev 68, 1659–1683 (2020). https://doi.org/10.1007/s11423-020-09790-5

This paper focuses on the professional value of social media. 

Obadimu, A., Mead, E., Hussain, M.N., Agarwal, N. (2019). Identifying Toxicity Within YouTube Video Comment. In: Thomson, R., Bisgin, H., Dancy, C., Hyder, A. (eds) Social, Cultural, and Behavioral Modeling. SBP-BRiMS 2019. Lecture Notes in Computer Science(), vol 11549. Springer, Cham. https://doi.org/10.1007/978-3-030-21741-9_22
https://link.springer.com/chapter/10.1007/978-3-030-21741-9_22#citeas

This paper looks at toxic comments.

Stefan Siersdorfer, Sergiu Chelaru, Wolfgang Nejdl, and Jose San Pedro. 2010. How useful are your comments? analyzing and predicting youtube comments and comment ratings. In Proceedings of the 19th international conference on World wide web (WWW '10). Association for Computing Machinery, New York, NY, USA, 891–900. https://doi.org/10.1145/1772690.1772781

This paper looks at analysis of comment utility. 