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

#Create a text input variable called 'fruit_choice' that requires a text input with the fruit name. Default is Kiwi.
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
#The sentence 'The user entered [fruit_choice]' will be printed on the webpage
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# Flatten the json data into a tabular format
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Insert flattened data into a dataframe. The website will show the data in a table.
streamlit.dataframe(fruityvice_normalized)

#use below library
import snowflake.connector

#query snowflake data
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("USE WAREHOUSE PC_RIVERY_WH")
my_cur.execute("SELECT * FROM PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
