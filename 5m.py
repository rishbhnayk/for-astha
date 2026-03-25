import streamlit as st
import datetime
import time

# Page Config
st.set_page_config(page_title="Happy 5 Months!", page_icon="🐘")

# Custom CSS for a romantic vibe
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1 { color: #ff4b4b; text-align: center; }
    .stButton>button { background-color: #ff4b4b; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("Happy 5 Month Anniversary, Astha! 🐘")

# 1. The Counter
start_date = datetime.date(2025, 10, 25) # Adjust this to your actual start date
today = datetime.date.today()
days_together = (today - start_date).days

st.subheader(f"We've been together for {days_together} beautiful days.")

# 2. The Interactive "Memory Box"
st.write("---")
st.write("### A few things I love about:")

reasons = [
    "The way you call me rishu.",
    "Our late night vid calls.",
    "I get pregnent for sure when u talk dirty.",
    "My only fav english teacher.",
    "The voice of yours."
    "The expressions when u r mad at me.(i can never forget that day)"
    "I love your kamar babyyyy <3."
    "Goddess."
    "Also your bf.(he's hawt)"
    "Your smell. (sniff sinff sniff)"
    
]

if st.button("Click for a reason I love us"):
    import random
    st.balloons()
    st.info(random.choice(reasons))

st.write("---")
st.subheader("Countdown to our next meeting")
next_meet_date = datetime.date(2026, 06, 05) # Update this to your next meetup date
days_left = (next_meet_date - today).days

if days_left > 0:
    st.write(f"Only **{days_left} days** until I get to see you in person again!")
else:
    st.write("I can't wait to be with you again!")
    

# 3. The Digital Gift
st.write("---")
st.write("### for you:")
# You can upload your AutoCAD portrait here
# st.image("your_autocad_portrait.png", caption="My AutoCAD Portrait of You")

st.write("> 'Distance just makes me crave more for you.'")

# 4. A Personal Note
with st.expander("Click to open my letter to you"):
    st.write("""
    Muwah Kanna, 
    Just few months are left I'll able to hug you againnn. I am very much excited to wait in the paradise for u to come.
    That feeling when I am with you i can't express, those first meetups
    after getting apart by distance i can't even speak properly but wanted to tell u kitna sara. Those walks with u holding your hands, aaaahhhhhhhhh!!!!.
    I need it nowww babyyy...I need you everyday for life...
    Hold your hands tight and take you everywhere i go.
    I LOVE YOU SO SO SO MUCH ASTHAAAAA <3
    """)
