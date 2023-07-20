import streamlit as st 
import pandas as pd

#gathering data
film_data_path = '/home/armaansyed/Programs/Python/kaggleData/filmStats/movie_statistic_dataset.csv'
data_frame = pd.read_csv(film_data_path) #reads data into data frame. (2d data thing idk. kinda like a cartesian plane)
