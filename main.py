import streamlit as st
import joblib
import sklearn

clf = joblib.load("freq.pkl")

st.title("외국어 문장 판별")
