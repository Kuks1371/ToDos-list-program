import streamlit as st
import todo_functions

todos = todo_functions.get_todos()

st.title("My Todo App")
st.subheader("This app is made to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...")