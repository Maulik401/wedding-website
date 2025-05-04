import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Maulik & Riddhi's Wedding", page_icon="💍", layout="centered")

# --- HEADER ---
st.title("Maulik & Riddhi")
st.subheader("We're Getting Married!")
st.write("**Save the Date: June 2, 2025**")

# --- COUNTDOWN ---
wedding_date = datetime(2025, 6, 2)
days_left = (wedding_date - datetime.now()).days
st.markdown(f"### Countdown: {days_left} days to go!")

# --- LOVE STORY TIMELINE ---
st.header("Our Love Story")
timeline = [
    ("2018", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2019", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2021", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**  \n{event}")

# --- PHOTO GALLERY ---
st.header("Photo Gallery")
st.image(
    [
        "photos/photo1.jpg",
        "photos/photo1.jpg",
        "photos/photo1.jpg"
    ],
    width=300,
    caption=["Engagement Day", "Pre-Wedding Shoot", "Forever Together"]
)

# --- SCHEDULE ---
st.header("Schedule")
st.write("""
- **Wedding Ceremony**: June 2, 2025 @ 11:00 AM  
- **Reception**: June 2, 2025 @ 7:00 PM  
- **Location**: Ahmedabad, Gujarat
""")

# --- VENUE MAP ---
st.header("Venue Location")
st.components.v1.html("""
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3672.538664777448!2d72.571362!3d23.030357!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x395e84f2aafeabe1%3A0x9e4e4099b1a3e8f7!2sAhmedabad%2C%20Gujarat!5e0!3m2!1sen!2sin!4v1713623200000!5m2!1sen!2sin"
  width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy">
</iframe>
""", height=400)

# --- RSVP FORM (No backend, just a thank-you message) ---
st.header("RSVP")
name = st.text_input("Your Name")
guests = st.number_input("Guests (including you)", min_value=1, max_value=10)
attending = st.radio("Will you attend?", ["Yes", "No", "Maybe"])

if st.button("Submit RSVP"):
    if name:
        st.success("Thank you! Your RSVP has been received. 💌")
    else:
        st.warning("Please enter your name.")

# --- FOOTER ---
st.markdown("---")
st.caption("With love, Maulik & Riddhi")
