import streamlit

import pandas

import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('🥗 My Mom"s New Healthy Diner')

streamlit.header('🐔 BreakFast Menu')

streamlit.text('🥣 Omega 3 and BlueBerry Oatmeal')  
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text(' 🐔 Hard Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#create fucntions
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# Display the table on the page.
#streamlit.dataframe(fruits_to_show)
streamlit.header('Fruity Fruit Advice!')
try:
  #fruit_choice = streamlit.text_input('What fruit would you like information about?','apple')
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get the information")
  else:  
    back_from_function = get_fruityvice_data(fruit_choice):
    streamlit.dataframe(back_from_function)
#streamlit.write('The user entered ', fruit_choice)
#import requests
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ this_fruit_choice)
# streamlit.text(fruityvice_response.json())
# take the json version and normalize it
#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output to the table
#streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()

streamlit.stop()

#import snowflake.connector

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
def get_fruit_load_list
    with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)
# allow users to add the fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add')
streamlit.write('Thank you for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit') ")
