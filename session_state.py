import streamlit as st


if 'text_list' not in st.session_state:
  st.session_state.text_list = []
# Text input
user_input = st.text_input('Enter some text')

# Buttons
if st.button('Append'):
  st.session_state.text_list.append(user_input)
  
if st.button('Clear'):
  st.session_state.text_list = []

# Display the list
st.write('Text list:', st.session_state.text_list)

# st.write("session state", st.session_state)