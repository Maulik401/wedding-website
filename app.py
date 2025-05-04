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
    ("2024 - Nov", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2025 - June", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2025 - May", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025 - June 2nd", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**  \n{event}")

# --- PHOTO GALLERY ---
st.header("Photo Gallery")
st.image(
    [
        "photos/photo1.jpg",
        "photos/photo2.jpg",
        "photos/photo3.jpg"
    ],
    width=300,
    caption=["Engagement Day", "Pre-Wedding Shoot", "Forever Together"]
)

# --- SCHEDULE ---
st.header("Schedule")
st.write("""
- **Wedding Ceremony**: June 2, 2025 @ 9:00 AM   
- **Location**: Veraval, Gujarat
""")

# --- VENUE MAP ---
st.header("Venue Location")
st.components.v1.html("""
<iframe
  src="Visawadia Ni Vandi, W989+8P5, Station Rd, Rayon Housing Society, Jobanpura, Veraval, Gujarat 362265, India">
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
