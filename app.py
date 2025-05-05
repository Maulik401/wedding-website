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

# --- Add Corner and Center Images (Moved to the Top) ---
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

# --- Header (with margin to bring title slightly lower and center it) --- 
st.markdown("<div style='margin-top: 160px;'></div>", unsafe_allow_html=True)  # Adjust the top margin here

# Custom CSS for centering the title and subheader
st.markdown(f"""
    <style>
        /* Full page background */
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-position: top center;
            padding-top: 150px;
        }}

        /* Center image styles (already in your code) */
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
        .left-img {{ top: 0; left: 0; }}
        .right-img {{ top: 0; right: 0; }}
        .center-img {{
            position: absolute;
            top: 20%;
            left: 50%;
            transform: translateX(-50%);
            width: 100px;
            z-index: 5;
            opacity: 0.9;
            pointer-events: none;
        }}

        /* Custom Section Header */
        .custom-section-header {{
            text-align: center;
            font-size: 2.2rem;
            font-weight: bold;
            font-family: 'Trebuchet MS', sans-serif;
            color: #c2185b; /* Magenta color */
            text-shadow: 2px 2px 4px #ffe0f0;
            margin-top: 2rem;
            margin-bottom: 1.2rem;
        }}

        /* Title */
        .custom-title {{
            text-align: center;
            font-family: 'Cinzel', serif;
            font-size: 4rem;
            font-weight: bold;
            color: #d4006d;
            text-shadow: 3px 3px 6px #fff0f5;
            margin-bottom: 0.5rem;
        }}

        /* Subheader */
        .custom-subheader {{
            text-align: center;
            font-family: 'Great Vibes', cursive;
            font-size: 2.5rem;
            color: #ff1493;
            margin-bottom: 0.2rem;
        }}

        /* Save the Date */
        .custom-save {{
            text-align: center;
            font-size: 1.75rem;
            color: #b5651d;
            font-family: 'Verdana', sans-serif;
            font-weight: bold;
            margin-bottom: 1.5rem;
        }}

        /* Countdown */
        .countdown-text {{
            text-align: center;
            font-size: 2.2rem;
            font-weight: bold;
            font-family: 'Trebuchet MS', sans-serif;
            color: #e91e63;
            text-shadow: 1px 1px 4px #fff0f5;
            margin-top: 30px;
        }}

        @media (max-width: 768px) {{
            .custom-title {{ font-size: 2.5rem; }}
            .custom-subheader {{ font-size: 1.8rem; }}
            .custom-save {{ font-size: 1.4rem; }}
            .countdown-text {{ font-size: 1.5rem; }}
        }}
    </style>
""", unsafe_allow_html=True)

# --- Title and Countdown Section (Centered and Styled) ---
st.markdown("<div class='custom-title'>Maulik & Riddhi</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-subheader'>We're Getting Married!</div>", unsafe_allow_html=True)
st.markdown("<div class='custom-save'>Save the Date: June 2, 2025</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 1.5rem; color: #6a1b9a; font-weight: bold; margin-top: 10px;'>💠 #MauRiPremKahani 💠</div>", unsafe_allow_html=True)


# --- Countdown ---
wedding_date = datetime(2025, 6, 2)
days_left = (wedding_date - datetime.now()).days
st.markdown(f"<div class='countdown-text'>⏳ Countdown: {days_left} days to go!</div>", unsafe_allow_html=True)

# --- Love Story Timeline ---
st.markdown("<div class='custom-section-header'>Our Love Story</div>", unsafe_allow_html=True)
timeline = [
    ("11/24/2023, 1:40:56 AM CST", "👀 We met for the first time — a simple hello turned into endless conversations."),
    ("2024 - June", "❤️ We started dating — our bond grew stronger with every passing day."),
    ("2025 - May", "💍 We got engaged — surrounded by love, family, and a thousand happy tears."),
    ("2025 - June 2nd", "💒 We're getting married — and you're invited to be part of it!")
]
for year, event in timeline:
    st.markdown(f"**{year}**  \n{event}")

# --- Photo Gallery ---
st.markdown("<div class='custom-section-header'>Photo Gallery</div>", unsafe_allow_html=True)
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
st.markdown("<div class='custom-section-header'>Schedule</div>", unsafe_allow_html=True)
st.write("""
- **Wedding Ceremony**: June 2, 2025 @ 9:00 AM  
- **Location**: Veraval, Gujarat
""")

# --- Venue Map ---
st.markdown("<div class='custom-section-header'>Venue Location</div>", unsafe_allow_html=True)
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
st.markdown("<div class='custom-section-header'>RSVP</div>", unsafe_allow_html=True)
name = st.text_input("Your Name")
guests = st.number_input("Guests (including you)", min_value=1, max_value=10)
attending = st.radio("Will you attend?", ["Yes", "No", "Maybe"])

if st.button("Submit RSVP"):
    if name:
        st.success("Thank you! Your RSVP has been received. 💌")
    else:
        st.warning("Please enter your name.")

# --- YouTube Video for Garba ---
st.markdown("<div class='custom-section-header'>🎶 Let's Celebrate with Garba Vibes!</div>", unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=-BI7m-S-TuY")  # Example: popular garba song

# --- Footer ---
st.markdown("---")
st.caption("🌸 With love, Maulik & Riddhi | Made with ❤️ in Gujarat 🌸")
