import streamlit as st
import pickle

movies_list =pickle.load(open('movie.pkl','rb'))

st.title('Movie Recommmender System')
st.write('By Saurabh Tanwer')
st.write('This is a simple movie recommender system that recommends movies based on user ratings')  
st.write('You can rate movies from 1 to 5')

option = st.selectbox(
    'How would you like to be contacted?',
    ['Email', 'Home phone', 'Mobile phone']
    )

















