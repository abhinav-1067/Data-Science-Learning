import streamlit as st 
import pandas as pd
import time

st.header("this is streamlit header")
st.title("this is streamlit title")
st.write('this is normal text')

st.markdown("""
- im abhinav yadav
- im 1st year btech student
- persuing computer science
""")

st.code("""
def foo(input):
    return input**2

x = foo(2)
""")

## Print dataframe,

df = pd.DataFrame({
    'name':['Abhinav','Surbhi','Rohan'],
    'age': [18,23,30],
    'packge(In LPA)':[30,20,15]
})

st.dataframe(df)


st.header("- Metric Element,")
st.metric('Revenue', 'Rs 3 Lakh', '-10%')

# Adding Sidebar,

st.sidebar.title("This Is SideBar!")

# adding progress Bar,

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.001)
    bar.progress(i)

## Adding user input section,

email = st.text_input("Enter Email Here")
number = st.number_input("Enter Age Here")
date = st.date_input("Enter Registration Date")