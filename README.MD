# Project22
#### NOTE: This project has been put on pause. Progress will continue after the Spotify forecasting project is finished. 

### Summary:
The goal of this program is to expose people to film outside the American mainstream, the "hidden gems" types of movies. 
I am going to build a recommender system that will suggest what the user should watch next based on the program's movie 
library and the user's interest profile. 

Ideally, the contributions to the movie library will be a community effort. Users will be able to submit movie names 
they wish to add to the library. Whether the suggested contribution is accepted or rejected will be based on numerical 
criteria. For example, movies like anything Marvel, Love Actually, Superbad, etc. would be rejected as they are within 
the mainstream.

#### The Movie Database (TMDB)
I am compiling data on various movies. To access and save the details of these movies I am using TMDB API. 
It's basically a easy-to-use, free version of IMDB. 
Explore the [documentation](https://developers.themoviedb.org/3/getting-started/introduction).

#### Project22 dataframe
My dataframe is a collection of lesser-known movies for American audiences. A small sample of what I plan to include in 
the full database can be found [here](https://github.com/amayabrios/Project22/blob/master/movie_features.csv).

#### User interest profile
User will answer a series of questions for the system to develop a sense of their interests. The
recommendations will improve as the user rates more movies. 

### Currently working on... Branch 1
thinking about how I'm storing the data, optimizing that, currently a csv
creating functions that will automate adding data based on user inputed movie name
as of now I am the only user but the big picture idea is that anyone will be able 
to contribute to the movie repository if the movie meets the qualifications,
these qualifications will be determined during branch 2/3 in the classification part of it

### Branches:
What needs to be built and the order to which I am doing so.

#### Branch 1: Build the dataframe
Building movie dataset, justify why I'm doing this instead of pulling from one 
of the thousands of movie data repositories
API practice (mainly)

#### Branch 2: Run data analysis
Running data analysis on movies gathered, find patterns commonalities, 
potentially build to creating classification algorithm for these movies, 
contrast them to the biggest movies of the last 50 or so years
incorporate Einblick into this part

#### Branch 3: ML system
Implementing machine learning tools/principles, user data, recommender system, 
classification system determine by branch 3
