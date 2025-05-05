import streamlit as st
from datetime import datetime
from PIL import Image
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Maulik & Riddhi's Wedding", page_icon="💍", layout="centered")

# --- BASE64 UTILITY FUNCTION ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- LOAD CORNER IMAGES ---
left_img = get_base64_of_bin_file("photos/drum-left.png")
right_img = get_base64_of_bin_file("photos/drum-right.png")

# --- BACKGROUND AND CORNER IMAGES ---
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("photos/drum-pattern-bg.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }}
    .corner-image {{
        position: fixed;
        width: 100px;
        z-index: 100;
    }}
    .top-left {{
        top: 10px;
        left: 10px;
    }}
    .top-right {{
        top: 10px;
        right: 10px;
    }}
    </style>

    <img src="data:image/png;base64,{left_img}" class="corner-image top-left">
    <img src="data:image/png;base64,{right_img}" class="corner-image top-right">
""", unsafe_allow_html=True)

# --- GANESHJI CENTER IMAGE ---
st.markdown('<div style="display:flex; justify-content:center; margin-top: -20px; margin-bottom: 10px;">', unsafe_allow_html=True)
st.image("photos/god.png", width=120)
st.markdown('</div>', unsafe_allow_html=True)

# --- HEADER ---
st.title("Maulik & Riddhi")
st.subheader("We're Getting Married! 💑💍")
st.write("**Save the Date: June 2, 2025**")

# --- COUNTDOWN ---
wedding_date = datetime(2025, 6, 2)
days_left = (wedding_date - datetime.now()).days
st.markdown(f"### ⏳ Countdown: {days_left} days to go!")

# --- LOVE STORY TIMELINE ---
st.header("📖 Our Love Story")
timeline = [
    ("2024 - Nov", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2025 - June", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2025 - May", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025 - June 2nd", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**  \n{event}")

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
st.header("🗓️ Schedule")
st.write("""
- **Wedding Ceremony**: June 2, 2025 @ 9:00 AM  
- **Location**: Visawadia Ni Vandi, Veraval, Gujarat
""")

# --- MAP + DIRECTIONS ---
st.header("📍 Venue Location")
st.components.v1.html("""
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3722.5438938326037!2d70.36196187504106!3d20.910310180761913!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be2a46b18ebc30b%3A0x47018f5d3a1a59f1!2sW989%2B8P5%2C%20Station%20Rd%2C%20Rayon%20Housing%20Society%2C%20Jobanpura%2C%20Veraval%2C%20Gujarat%20362265%2C%20India!5e0!3m2!1sen!2sin!4v1714827309421!5m2!1sen!2sin"
  width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy">
</iframe>
""", height=400)

st.markdown("### 🧭 [Click here to get directions](https://www.google.com/maps/dir/?api=1&destination=Visawadia+Ni+Vandi,+W989%2B8P5,+Station+Rd,+Rayon+Housing+Society,+Jobanpura,+Veraval,+Gujarat+362265,+India)")

# --- YOUTUBE MUSIC EMBED ---
st.header("🎶 Let's Celebrate with Garba Vibes!")
st.video("https://www.youtube.com/watch?v=-BI7m-S-TuY")

# --- RSVP FORM ---
st.header("📨 RSVP")
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
st.caption("🌸 With love, Maulik & Riddhi | Made with ❤️ in Gujarat 🌸")
