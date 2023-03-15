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

# Include a multi-select list so a user can pick fruits from the fruit list on the website. Include two fruits as examples.
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Create a 'fruits_to_show' variable to only show fruits picked from multiselect picker
fruits_to_show=my_fruit_list.loc[fruits_selected]

# Display fruit table on page
streamlit.dataframe(fruits_to_show)

#Display Fruityvice API response
streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
