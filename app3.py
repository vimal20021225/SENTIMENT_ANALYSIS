import streamlit as st
from textblob import TextBlob
from transformers import pipeline
from streamlit_extras.let_it_rain import rain
st.title("Sentiment Analysis App")
pipe = pipeline(model = "lxyuan/distilbert-base-multilingual-cased-sentiments-student")


message=st.text_input("Please Enter your text")
if st.button("Analyze the Sentiment"):
    output_model = pipe(message)
    result = output_model[0]['label']
    if result == "positive":
        st.warning("The predicted sentiment is positive!!")
        rain(emoji="😄",
             font_size=30,
             falling_speed=2,
             animation_length=30,)
    elif result=="neutral":
        st.warning("The predicted sentiment is neutral")
        rain(emoji="😑",
             font_size=30,
             falling_speed=2,
             animation_length=30,)
    else:
        st.warning("The predicted sentiment is negative")
        rain(emoji="😠",
             font_size=30,
             falling_speed=2,
             animation_length=30,)
    st.success(result)
