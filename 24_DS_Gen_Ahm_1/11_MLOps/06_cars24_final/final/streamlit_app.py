import streamlit as st
import base64

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Car Price Predictor UI",
    page_icon="🚗",
    layout="wide"
)

# ----------------------------
# Function to encode image
# ----------------------------
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return data

# Load image
img = get_base64("bg.jpg")

# ----------------------------
# Background Styling (with blur + glass effect)
# ----------------------------
page_bg = f"""
<style>

/* Background image (full, no crop) */
[data-testid="stAppViewContainer"] {{
    background-image: url("https://images.unsplash.com/photo-1459603677915-a62079ffd002?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGNhcnxlbnwwfHwwfHx8MA%3D%3D");
    background-size: contain;
    background-color: #0e1117;
}}

# /* Blur overlay (VISIBLE now) */
# [data-testid="stAppViewContainer"]::before {{
#     content: "";
#     position: fixed;
#     inset: 0;
#     background: url("data:image/jpg;base64,{img}") no-repeat center center;
#     background-size: contain;
    
#     filter: blur(6px) brightness(0.7);  /* 🔥 strong blur */
#     transform: scale(1.05);
    
#     z-index: 0;   /* IMPORTANT: bring it above bg */
# }}

/* Make content sit ABOVE blur */
.main, .block-container {{
    position: relative;
    z-index: 1;
    background: rgba(0, 0, 0, 0.55);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 25px;
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background: rgba(0,0,0,0.85);
}}

/* Text */
label, .stMarkdown, h1, h2, h3 {{
    color: white !important;
}}

/* Buttons */
.stButton>button {{
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ----------------------------
# Title
# ----------------------------
st.title("🚗 Car Selling Price Predictor")
st.write("Fill in the car details below")

# ----------------------------
# Layout
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔧 Car Specifications")

    km_driven = st.slider("Km Driven", 0, 300000, 50000)
    mileage = st.number_input("Mileage (km/l)", 5.0, 40.0, 18.0)
    engine = st.number_input("Engine (cc)", 500, 5000, 1200)
    max_power = st.number_input("Max Power (bhp)", 20.0, 500.0, 80.0)
    age = st.slider("Car Age (years)", 0, 20, 5)

with col2:
    st.subheader("🚘 Car Details")

    make_model = st.text_input("Make + Model (e.g., MARUTI ALTO)")

    dealer = st.selectbox(
        "Seller Type",
        ["Individual", "Trustmark Dealer"]
    )

    fuel = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "Electric", "CNG", "Hybrid"]
    )

    seats = st.selectbox(
        "Seats",
        ["<5", ">5"]
    )

# ----------------------------
# Sidebar Summary
# ----------------------------
st.sidebar.title("📋 Input Summary")

st.sidebar.write(f"**Km Driven:** {km_driven}")
st.sidebar.write(f"**Mileage:** {mileage} km/l")
st.sidebar.write(f"**Engine:** {engine} cc")
st.sidebar.write(f"**Max Power:** {max_power} bhp")
st.sidebar.write(f"**Age:** {age} years")
st.sidebar.write(f"**Model:** {make_model}")
st.sidebar.write(f"**Dealer:** {dealer}")
st.sidebar.write(f"**Fuel:** {fuel}")
st.sidebar.write(f"**Seats:** {seats}")

# ----------------------------
# Predict Button
# ----------------------------
if st.button("🔍 Predict Price"):
    st.success("⚡ Model not connected yet. This is UI only.")