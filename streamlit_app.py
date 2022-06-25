import streamlit
import pandas
import requests
import snowflake.connector

from urllib.error import URLError


streamlit.title('Snowflake Training')
streamlit.header('June 2022')

streamlit.text('Hello World!')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header('API call')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')

try:
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # normalize json response
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # display in df
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
  streamlit.error()


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

my_cur.execute("insert into fruit_load_list values ('from streamlist')")
