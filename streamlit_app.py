import streamlit
import pandas

streamlit.title('Snowflake Training')
streamlit.header('June 2022')

streamlit.text('Hello World!')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
