import streamlit as st
from datetime import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Maulik & Riddhi's Wedding", page_icon="💍", layout="centered")

# --- Custom CSS to add background and corner images ---
st.markdown(
    """
    <style>
    .main {
        background-image: url('photos/background.jpg');  /* Background image */
        background-size: cover;  /* Ensures the image covers the entire page */
        background-position: center;  /* Keeps the image centered */
        background-repeat: no-repeat;
        position: relative;
        height: 100vh;  /* Set the height to cover the entire viewport */
    }

    /* Add corner images at the top */
    .left-corner {
        position: absolute;
        top: 0%;
        left: 5%;
        width: 150px;
        z-index: 2;  /* Ensures the images appear on top */
    }

    .right-corner {
        position: absolute;
        top: 0%;
        right: 5%;
        width: 150px;
        z-index: 2;  /* Ensures the images appear on top */
    }

    /* Add center image (God image) */
    .center-image {
        position: absolute;
        top: 10%;  /* Positioned slightly below the top to avoid overlap */
        left: 50%;
        transform: translateX(-50%);
        width: 250px;
        z-index: 2;  /* Ensures the image appears on top */
    }

    /* Add padding to content */
    .stApp {
        padding-top: 150px;  /* Adjust the padding to give space to the background image */
    }
    </style>
    """, unsafe_allow_html=True
)

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

# --- RSVP FORM ---
st.header("RSVP")
name = st.text_input("Your Name")
guests = st.number_input("Guests (including you)", min_value=1, max_value=10)
attending = st.radio("Will you attend?", ["Yes", "No", "Maybe"])

if st.button("Submit RSVP"):
    if name:
        st.success("Thank you! Your RSVP has been received. 💌")
    else:
        st.warning("Please enter your name.")

# --- EMBEDDED YOUTUBE VIDEO (Garba music) ---
st.header("🎶 Let's Celebrate with Garba Vibes!")
st.video("https://www.youtube.com/watch?v=-BI7m-S-TuY")  # Example: popular garba song

# --- FOOTER ---
st.markdown("---")
st.caption("🌸 With love, Maulik & Riddhi | Made with ❤️ in Gujarat 🌸")

# --- CORNER IMAGES (drums) ---
left_corner = "photos/left_drum.png"  # Ensure the image is in the photos/ folder
right_corner = "photos/right_drum.png"  # Ensure the image is in the photos/ folder
center_image = "photos/god_image.png"  # Image for the center (God)

# Add the images to the page
st.markdown(
    f"""
    <img class="left-corner" src="{left_corner}" alt="Left Drum Image">
    <img class="right-corner" src="{right_corner}" alt="Right Drum Image">
    <img class="center-image" src="{center_image}" alt="God Image">
    """,
    unsafe_allow_html=True
)
