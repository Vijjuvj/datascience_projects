
# Fraud Analysis of Credit Cards:
In this Repo,I have done a project on machine learning classification problem statement which requires a huge dataset where i got it from 3rd party websites.



## Project Overview

![App Screenshot](https://resources.cdn.seon.io/uploads/2021/12/Credit_Card_Fraud_12.06_isolated.png)

Using Pandas library I loaded the dataset and also check the complete information about the dataset using the same library.
since the data is having lot of null values ,iam going to take help of statistics concept to clean the data and if my approach is not good way for doing this project , please let me know.
But while focusing on Missing values, i got to know that last 2 rows are completely null values,so i removed last 2 rows. Then again focusing on null values , i got to know that 2 columns "MonthlyIncome.1" and "MonthlyIncome" having same data , so i removed one of the column "MonthlyIncome.1"

## Iam Following Machine learning Pipeline for developing this project

    Pipeline of Machine Learning Project
        Collect the data
        Check the data info
        split the data
        training operations should be done on test data [just keep on mind]
        Handling missing values if there
        EDA part (Exploratory Data Analysis)
        checking the Normal Distribution
        checking the outlier
        Handling Them
        Handling Categorical data
        Transformation Techniques
        select best feature for both numerical and training data
        model development
        check validation
        evaluate model
        check AUC and ROC and select best model
        Hyperparameter tuning on best model
        save the model
        Read the model and check once again
        Using Flask integrate with html and css
        Genearate outcome in localhost
        Deploy in server
        API generation
        Share our Project API
## Why splitting the data
If we divide the data after feature engineering part , the std[standard deviation and variance] will be completely different for both train and test data, this leads to data leakage. so to overcome this , I am splitting the data and applying the operations on training data and same result saving it for test data.

## Handle Missing Values
For handling missing values , we have used mean,median and mode concept where its working really fine and when coming to Outliers, I applied a Technique called std and IQR since it really works fine the worst feature converts into proper feature.

Meanwhile while working with feature engineering part I am taking sklearn and feature engineering frameworks for better EDA and model delevelopment part .

    Technique done using sklearn and feature engine:
        - variable Transformation
        - Outliers 
        - data scaling concpets
## since EDA part Feature engineering part is too high Iam not going to explain each line of code , here you can check it from the above coding file.

## Feature Selection 

![App Screenshot](https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/feature-selection-methods-1.png?resize=767%2C452&ssl=1)


As mentioned in the above image there are multiple methods for Analysis of Feature selection.For my data using sklearn and feature engine I have gone with correlation and filter methods for numerical columns since some columns selected remaining things removed from the data.     
Using correlation , even my threshold values is too high 0.85 , but no feature is passing or crossing the threshold values, so correlation didn't select best features.
Using Hypothesis testing i got best features with p_value < 0.5 concept .

## Finally entire data is set ready for model development purpose.

Since the data is not balanced ,using Upsampling and down sampling concepts I handle them.

Now I selected KNN, Naive Bayes , Logistic regression , Decision Tree and Randome Forest for Model development.

Since after training the model I got results of testing accuracy:

        - KNN Accuracy = 0.8703838383838384
        - Naive Bayes Accuracy=0.6992929292929293
        - Logistic Regression Accuracy=0.7377373737373737
        - Decision tree Accuarcy=0.708040404040404
        - Random forest Accuracy =0.7483030303030302

Since Above values are similar , It is difficult for us to select the trained models:
using AUC and Roc I will find best one as Logistic Regression.
