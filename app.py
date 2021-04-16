import streamlit as st
import joblib
model=joblib.load("Email_class")
st.title('review classifier')
ip=st.text_input('enter your review')
op=model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
