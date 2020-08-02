# **ABOUT THE PROJECT**

#

**1 OUR PROJECT – Movie Recommendation System**

The main goal of this machine learning project is to build a recommendation engine that recommends movies to users. This R project is designed to help you understand the functioning of how a recommendation system works. We will be developing an Item Based Collaborative Filter. By the end of this tutorial, you will gain experience of implementing your R, Data Science, and Machine learning skills in a real-life project.

Before moving ahead in this movie recommendation system project in ML, you need to know what recommendation system means. Read below to find the answer.

**2 What is Movie Recommendation System?**

A recommendation system provides suggestions to the users through a filtering process that is based on user preferences and browsing history. The information about the user is taken as an input. The information is taken from the input that is in the form of browsing data. This information reflects the prior usage of the product as well as the assigned ratings. A recommendation system is a platform that provides its users with various contents based on their preferences and likings. A recommendation system takes the information about the user as an input.

**3 The Dataset**

This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from [MovieLens](http://movielens.org), a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018. This dataset was generated on September 26, 2018.

Users were selected at random for inclusion. All selected users had rated at least 20 movies. No demographic information is included. Each user is represented by an id, and no other information is provided.

The data are contained in the files `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. More details about the contents and use of all these files follows.

This is a \*development\* dataset. As such, it may change over time and is not an appropriate dataset for shared research results. See available \*benchmark\* datasets if that is your intent.

This and other GroupLens data sets are publicly available for download at \&lt;http://grouplens.org/datasets/\&gt;.

**4 Prerequisites**

Before starting with this Python project with source code, we should be familiar with the library of Python that is _ **scipy** _and[_ **Pandas** _](https://data-flair.training/blogs/pandas-tutorials-home/)[**.**](https://data-flair.training/blogs/pandas-tutorials-home/)

**Tkinter, Pandas, and Scipy** are the Python packages that are necessary for this project in Python. To install them, simply run this pip command in your terminal:



**STEPS FOR BULIDING MOVIE RECOMMENDATION SYSTEM**

**1 Importing Essential Libraries**

In our Data Science project, we will make use of these 2 packages – &#39; pandas &#39;, &#39;scipy&#39;

![](Screenshot/1.png)

**2 We read the CSV file with pandas**

The pandas library is very useful when we need to perform various operations on data files like CSV. **pd.read\_csv()** reads the CSV file and loads it into the pandas DataFrame. We have assigned each column with a name for easy accessing.

![](Screenshot/2.png)


**3 Data Pre-processing**

From the above table, we observe that the userId column, as well as the movieId column, consist of integers. Furthermore, we need to convert the genres present in the movie\_data dataframe into a more usable format by the users.

![](Screenshot/3.png)


In order to do so, we will first create a encoding to create a corrMatrix that comprises of corresponding genres for each of the films ![](Screenshot/4.png)

**4 Create the recommendation system function**

We will create a top\_recommendations variable which will be initialized to 10, specifying the number of films to each user. We will then use the predict() function that will identify similar items and will rank them appropriately. Here, each rating is used as a weight. Each weight is multiplied with related similarities. Finally, everything is added in the end. ![](Screenshot/5.png)


**5 Steps to create GUI**

**5.1 Import the module and create a screen**

Here we will import the Tkinter module and create a screen namely root ![](Screenshot/6.png)


**5.2 Creating notebook**

Now we will create a notebook which will contain 3 frames :

&quot;CREATE DATABASE &quot; , &quot;VIEW DATABASE &quot; , &quot;RECOMMENDATION &quot;

![](Screenshot/7.png)


**5.3 ADDING WIDGET IN CREATE DATABASE TAB**

In this we will add widget like lable , entry , listbox , button and radio button

![](Screenshot/8.png)


**5.4 ADDING FUNCTIONALITY TO ENTRYAND LISTBOX**

For this we will use 2 functions i.e. on\_keyrelease and listbox\_ update

![](Screen(hot/9.png)/
**5.5 ADDING CAPABILITY TO RADIO BUTTON**

When we select a radio button for rateing the movie that number is added to the rat list .

![](Screenshot/10.png)

    1. **BUTTONS CAPABILITY**

In this GUI we have two buttons i.e.

1. **SAVE DATABASE**

This button saves the data in the tabular form and display the same in the c\_database frame (create database tab)

![](Screenshot/11.png)


**2.RECOMMEND MOVIES**

This button calls the similar\_movies function and return the list of top 20 recommended movies and display the same in the data frame in the tab RECOMMEND MOVIES

![](Screenshot/12.png)




#

# **OUTPUT**

#

**1 Run Python File**

We can run the Python file from the command(prompt. ![/Screenshot/13.png)


**2**** Screenshot of the program**

![](Screenshot/14.png)
![](Screenshot/5.png)
![](Screenshot/16.png)
![](Screenshot/17.png)
![](Screenshot/18.png)

**3 OUTPUT**

![](Screenshot/19.png)




**STEP 2 OUTPUT**

![](Screenshot/20.png)

**STEP 3 OUTPUT**

![](Screenshot/21.png)
