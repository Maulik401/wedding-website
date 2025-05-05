import streamlit as st
from datetime import datetime

import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Maulik & Riddhi's Wedding", page_icon="💍", layout="centered")

# --- MUSIC PLAYER WITH MUTE BUTTON ---
st.components.v1.html("""
<div style="text-align:center; margin-bottom: 10px;">
  <audio id="bgmusic" autoplay loop>
    <source src="https://paglasongs.com/files/download/id/13597" type="audio/mp3">
    Your browser does not support the audio element.
  </audio>
  <button onclick="toggleMute()" style="padding: 8px 16px; font-size: 16px; background-color: #ff4081; color: white; border: none; border-radius: 5px; cursor: pointer;">
    🔈 Mute/Unmute Music
  </button>
</div>
<script>
  function toggleMute() {
    var audio = document.getElementById("bgmusic");
    audio.muted = !audio.muted;
  }
</script>
""", height=100)

# --- HEADER ---
st.markdown("<h1 style='text-align: center; color: #b30059;'>💍 Maulik & Riddhi 💍</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🎉 We're Getting Married! 🎉</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>📅 Save the Date: <b>June 2, 2025</b></p>", unsafe_allow_html=True)

# --- COUNTDOWN ---
wedding_date = datetime(2025, 6, 2)
days_left = (wedding_date - datetime.now()).days
st.markdown(f"<h4 style='text-align: center;'>⏳ Countdown: <span style='color:#ff6600'>{days_left} days to go!</span></h4>", unsafe_allow_html=True)

# --- LOVE STORY TIMELINE ---
st.header("💖 Our Love Story")
timeline = [
    ("2024 - Nov", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2025 - June", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2025 - May", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025 - June 2nd", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**<br>{event}", unsafe_allow_html=True)

# --- PHOTO GALLERY ---
st.header("📸 Photo Gallery")
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
st.header("📅 Schedule")
st.write("""
- 🕘 **Wedding Ceremony**: June 2, 2025 @ 9:00 AM  
- 📍 **Location**: Visawadia Vadi, Veraval, Gujarat
""")

# --- VENUE MAP ---
st.header("📍 Venue Location")
st.components.v1.html("""
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3722.5438938326037!2d70.36196187504106!3d20.910310180761913!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be2a46b18ebc30b%3A0x47018f5d3a1a59f1!2sW989%2B8P5%2C%20Station%20Rd%2C%20Rayon%20Housing%20Society%2C%20Jobanpura%2C%20Veraval%2C%20Gujarat%20362265%2C%20India!5e0!3m2!1sen!2sin!4v1714827309421!5m2!1sen!2sin"
  width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy">
</iframe>
""", height=400)

# Directions button
st.markdown("### 🧭 Need Directions?")
st.markdown(
    "[🚗 Click here to open Google Maps](https://www.google.com/maps/dir/?api=1&destination=Visawadia+Ni+Vandi,+W989%2B8P5,+Station+Rd,+Rayon+Housing+Society,+Jobanpura,+Veraval,+Gujarat+362265,+India)",
    unsafe_allow_html=True
)

# --- RSVP FORM ---
st.header("📨 RSVP")
name = st.text_input("Your Name")
guests = st.number_input("Guests (including you)", min_value=1, max_value=10)
attending = st.radio("Will you attend?", ["Yes", "No", "Maybe"])

if st.button("Submit RSVP"):
    if name:
        st.success("🎉 Thank you! Your RSVP has been received.")
    else:
        st.warning("Please enter your name before submitting.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align: center;'>With love, 💕 Maulik & Riddhi 💕</p>", unsafe_allow_html=True)
