import streamlit as st

st.write("session state", st.session_state)
text_list = []
# Text input
user_input = st.text_input('Enter some text')

# Buttons
if st.button('Append'):
  text_list.append(user_input)
  
if st.button('Clear'):
  text_list = []


# Display the list
st.write('Text list:', text_list)
# for item in text_list:
#     st.write(item)
    
# def main():
#     # Initialize session state
#     if 'text_list' not in st.session_state:
#         st.session_state.text_list = []

#     # Text input
#     user_input = st.text_input('Enter some text')

#     # Buttons
#     if st.button('Append'):
#         st.session_state.text_list.append(user_input)
    
#     if st.button('Clear'):
#         st.session_state.text_list = []

#     # Display the list
#     st.write('Text list:')
#     for item in st.session_state.text_list:
#         st.write(item)

# if __name__ == '__main__':
#     main()
