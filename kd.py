#Comments are for me! If you think they are bad idc!!!!
import random
import streamlit as st 
import pandas as pd #pandas is how we get data into a data frame 

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

st.dataframe(df['movie_averageRating'].unique())
