import streamlit as st
import functions

todos= functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"    #working as a dictionary
    todos.append(todo)
    functions.write_todos(todos)


st.title('Hello !')
st.subheader("My todo list app")
st.write('give all the relevant work to be completed.')
# st.checkbox("Buy groceries")

for index,todo in enumerate(todos):
    checkbox= st.checkbox(todo,key=todo)    #to show the todo as a checkbox in the screen
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Different types of todo",placeholder="Add new todo...",
              on_change=add_todo,key='new_todo')

print("hello")

st.session_state


