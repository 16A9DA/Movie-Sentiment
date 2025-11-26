import pickle
import streamlit as st
from textCleaning import clean_text


model = pickle.load(open("svm.pkl", "rb"))
vectorizer = pickle.load(open("triVec.pkl", "rb"))


st.title("Welcome To Movie Sentiment Analysis 🎞️.")
st.header("Write your review about a Movie.",divider=True)

user_input = st.text_area("Enter your review here:")

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review before predicting.")
    else:
        cleaned_text = clean_text(user_input)
        user_vector = vectorizer.transform([cleaned_text])
        prediction = model.predict(user_vector)
        output  = "Positive 😊" if prediction == "positive" else "negative 😞"
        st.success(f"The sentiment of the review is: {output}")
st.markdown("---")
