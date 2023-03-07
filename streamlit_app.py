import streamlit
streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
# Make the fruit name column the index column
my_fruit_list=my_fruit_list.set_index('Fruit')

# Include a multi-select list so a user can pick fruits from the fruit list on the website
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display fruit table on page
streamlit.dataframe(my_fruit_list)
