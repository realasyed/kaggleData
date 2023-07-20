#Comments are for me! If you think they are bad idc!!!!
import random
import streamlit as st 
import pandas as pd #pandas is how we get data into a data frame 
import numpy

#Taking data and putting it into a data frame with pandas
dataPath = ('./filmStats/movie_statistic_dataset.csv')
df = pd.read_csv(dataPath)

#random_index = random.randint(0, len(df) - 1) #takes a random int between 0 and the amount of data - 1.
#random_movie_title = df.loc[random_index, 'Title'] #From W3: "The loc property gets, or sets, the value(s) of the specified labels."
#print("Random Movie Title:", random_movie_title)
#The commented code above didnt work because I didn't specify what particular column I need to len.
#this was not especially relevant anyways. i wasted some time.

movieTitles = df['movie_title'].unique()
selectedMovie = st.selectbox("Select a movie:", movieTitles)
st.write("You selected:", selectedMovie)

selectedMovieRow = df[df['movie_title'] == selectedMovie] #showing a df of movie_titles but only selectedMovie title(s).
averageRating = selectedMovieRow['movie_averageRating'].values[0] #sets averageRating to first instance of a movie's particular rating. it searches the selectedMovieRow.
st.write(selectedMovie + "'s average rating is" + averageRating)

#The second code snippet is a little unintuitive; here's how it works:
#After selecting a movie, selectedMovieRow creates another data frame
#that consists of the data in the same row as the user selected movie.
#Creating a data frame out of another data frame makes the second
#data frame only contain data relevant to the first df. In this case,
#that means only data contained in the same row as the selectedMovie.
#note that == is a check while = assigns.

#On line 22, averageRating looks for the movie_averageRating column,
#however, it only searches for the relevant cell in selectedMovieRow.
#The .values[0] section indexes for the first instance of
#movie_averageRating and sets that equal to averageRating
#just in case two selectedMovie's have the same name. 
