import streamlit as st
from modules import functions

list = functions.get_todos()

def add_todo():
    todo = st.session_state["-IN-"] + "\n"
    if todo not in list and todo.strip() != "":
        list.append(todo)
        functions.save_todos(list)
    else:
        print("Forget it mate...")
    st.session_state["-IN-"] = ""

def remove_selections():
    temp_list = []
    for i in list:
        if st.session_state[i] == True:
            temp = i
            temp_list.append(temp)
    for i in temp_list:
        print(i)
        del st.session_state[i]
        list.remove(i)
    functions.save_todos(list)

st.title("My todos")
st.subheader("WebUI")

for i in list:
    st.checkbox(i, key=i)

st.text_input(label="321tseT", placeholder="Enter a todo here", on_change=add_todo, key="-IN-")
st.button(label="Delete", on_click=remove_selections)