import streamlit as st
import time

st.header("Shapes Calculations")
# st.subheader("I am here!")
# st.caption("helpp")

# st.sidebar.title("Configurations")

# with st.sidebar:
shape = st.selectbox("Choose shape:", ['Circle', 'Rectangle'])
  
if shape == 'Circle':
  radius = st.number_input('Radius', 0., 20., step=0.1)
  area = radius * radius * 3.14
  perimeter = 2 * 3.14 * radius
else:
  width = st.number_input('Width', 0., 20., step=0.1)
  height = st.number_input('Height', 0., 20., step=0.1)
  area = width * height
  perimeter = 2 * (width + height)
  
if st.button('Compute Area and Perimeter'):
  with st.spinner("Computing..."):
    time.sleep(1)
    st.write(f"Area: {area}")
    st.write(f"Perimeter: {perimeter}")
    
# 1. Basic header
# 2. Select box and shape
# 3. Compute using button
# 4. Show
# 5. Sidebar (put select box there)
# 6. Spinner