import streamlit as st
from datetime import datetime
from PIL import Image
import base64
import io

# --- Helper function to load images as base64 ---
def load_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load images as base64
left_corner = load_base64("photos/left_drum.png")
right_corner = load_base64("photos/right_drum.png")
bg_image = load_base64("photos/background.jpg")
center_image = load_base64("photos/god_image.png")

# --- PAGE CONFIG ---
st.set_page_config(page_title="Maulik & Riddhi's Wedding", page_icon="💍", layout="centered")

# --- Header --- 
st.title("Maulik & Riddhi")
st.subheader("We're Getting Married!")
st.write("**Save the Date: June 2, 2025**")

# --- Countdown ---
wedding_date = datetime(2025, 6, 2)
days_left = (wedding_date - datetime.now()).days
st.markdown(f"### Countdown: {days_left} days to go!")

# --- Love Story Timeline ---
st.header("Our Love Story")
timeline = [
    ("2024 - Nov", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2025 - June", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2025 - May", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025 - June 2nd", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**  \n{event}")

# --- Photo Gallery ---
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

# --- Schedule ---
st.header("Schedule")
st.write("""
- **Wedding Ceremony**: June 2, 2025 @ 9:00 AM  
- **Location**: Veraval, Gujarat
""")

# --- Venue Map ---
st.header("Venue Location")
st.components.v1.html("""
<iframe
  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3722.5438938326037!2d70.36196187504106!3d20.910310180761913!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be2a46b18ebc30b%3A0x47018f5d3a1a59f1!2sW989%2B8P5%2C%20Station%20Rd%2C%20Rayon%20Housing%20Society%2C%20Jobanpura%2C%20Veraval%2C%20Gujarat%20362265%2C%20India!5e0!3m2!1sen!2sin!4v1714827309421!5m2!1sen!2sin"
  width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy">
</iframe>
""", height=400)

# Directions button (clickable)
st.markdown("### 📍 Want Directions?")
st.markdown(
    "[🧭 Click here to open in Google Maps and get directions](https://www.google.com/maps/dir/?api=1&destination=Visawadia+Ni+Vandi,+W989%2B8P5,+Station+Rd,+Rayon+Housing+Society,+Jobanpura,+Veraval,+Gujarat+362265,+India)",
    unsafe_allow_html=True
)

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

# --- YouTube Video for Garba ---
st.header("🎶 Let's Celebrate with Garba Vibes!")
st.video("https://www.youtube.com/watch?v=-BI7m-S-TuY")  # Example: popular garba song

# --- Footer ---
st.markdown("---")
st.caption("🌸 With love, Maulik & Riddhi | Made with ❤️ in Gujarat 🌸")

# --- Add Background and Corner Images ---
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");  /* Background Image */
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
        padding-top: 140px;
    }}

    .relative-container {{
        position: relative;
    }}

    .corner-img {{
        position: absolute;
        width: 80px;
        z-index: 10;
        opacity: 0.9;
        pointer-events: none;
    }}

    .left-img {{
        top: 0;
        left: 0;
    }}

    .right-img {{
        top: 0;
        right: 0;
    }}

    .center-img {{
        display: flex;
        justify-content: center;
        margin-top: -90px;
        margin-bottom: 10px;
    }}

    @media (max-width: 768px) {{
        .corner-img {{
            width: 50px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Adding corner and center images
st.markdown(
    f"""
    <div class="relative-container">
        <img src="data:image/png;base64,{left_corner}" class="corner-img left-img">
        <img src="data:image/png;base64,{right_corner}" class="corner-img right-img">
        <img src="data:image/png;base64,{center_image}" class="center-img">
    </div>
    """,
    unsafe_allow_html=True
)
