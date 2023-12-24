import streamlit as st
import function
todos = function.get_todos()
def Add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    function.write_todos(todos)



st.title("My Todo Web App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo)
    if checkbox:
        # todos = function.get_todos()
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a Todos:",
              placeholder="Add new Todo.......",
              on_change=Add_todo,
              key="new_todo")    


# st.write("this is my first web app")