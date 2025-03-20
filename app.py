import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stTextInput, .stNumberInput, .stSelectbox {
            text-align: center;
        }
        .result-box {
            background-color: #5f5f5f;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔄 Unit Converter")

categories = {
    "Length": {
        "Metre": 1,
        "Centimetre": 100,
        "Kilometre": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Pound": 2.20462,
    },
    "Time": {
        "Second": 1,
        "Minute": 1 / 60,
        "Hour": 1 / 3600,
        "Day": 1 / 86400,
    },
    "Speed": {
        "Meter per second": 1,
        "Kilometer per hour": 3.6,
        "Miles per hour": 2.23694,
        "Feet per second": 3.28084,
    },
    "Volume": {
        "Liter": 1,
        "Milliliter": 1000,
        "Cubic meter": 0.001,
        "Gallon (US)": 0.264172,
        "Pint (US)": 2.11338,
    },
}

category = st.selectbox("📌 Select a category", list(categories.keys()))
units = categories[category]
from_unit = st.selectbox("🔄 From", units.keys())
to_unit = st.selectbox("➡️ To", units.keys())
value = st.number_input("✏️ Enter value", min_value=0.0, format="%.2f")

# Conversion Button
if st.button("✅ Convert Now"):
    if from_unit and to_unit:
        result = value * (units[to_unit] / units[from_unit])
        
        # Styled Output
        st.markdown(f"""
        <div class="result-box">
            <h2>{value} {from_unit} = {result:.2f} {to_unit}</h2>
            <h5>Formula:</h5>
            <p>Multiply {value} by {units[to_unit] / units[from_unit]:.4f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Success Message
        st.success("🎉 Conversion Successful!")
