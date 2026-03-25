import streamlit as st
import datetime
import time

# Page Config
st.set_page_config(page_title="Happy 5 Months!", page_icon="❤️")

# Custom CSS for a romantic vibe
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1 { color: #ff4b4b; text-align: center; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Happy 5 Month Anniversary, Astha! ❤️")

# 1. The Counter
start_date = datetime.date(2025, 10, 25) # Adjust this to your actual start date
today = datetime.date.today()
days_together = (today - start_date).days

st.subheader(f"We've been together for {days_together} beautiful days.")

# 2. The Interactive "Memory Box"
st.write("---")
st.write("### A few things I love about these 5 months:")

reasons = [
    "The way you support my crazy engineering projects.",
    "Our long-distance movie nights.",
    "Seeing the progress on your AutoCAD portrait.",
    "Every time we talk, the distance feels smaller.",
    "Just knowing I have you by my side."
]

if st.button("Click for a reason I love us"):
    import random
    st.balloons()
    st.info(random.choice(reasons))

# 3. The Digital Gift
st.write("---")
st.write("### A special creation for you:")
# You can upload your AutoCAD portrait here
# st.image("your_autocad_portrait.png", caption="My AutoCAD Portrait of You")

st.write("> 'Distance is just a test to see how far love can travel.'")

# 4. A Personal Note
with st.expander("Click to open my letter to you"):
    st.write("""
    Hey Astha, 
    Five months ago, we started this journey. Even though we are far apart right now, 
    you are the best part of my day, every single day. Happy Anniversary!
    """)
