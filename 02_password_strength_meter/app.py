import streamlit as st
import re
import random
import string

# Expanded Blacklist
COMMON_PASSWORDS = {"password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome", "name", "number", "iloveyou", "123456789", "football", "monkey", "sunshine", "princess", "dragon", "baseball", "copy345", "$$$$@@$$$$"}

# Store password history in session state
if "password_history" not in st.session_state:
    st.session_state.password_history = []

def check_password_strength(password):
    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is too common. Choose a more unique password."]
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, feedback

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check its strength.")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    
    st.progress(score / 4)
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    for tip in feedback:
        st.write(tip)
    
    if password in st.session_state.password_history:
        st.error("⚠️ You have used this password before. Choose a new one.")
    else:
        st.session_state.password_history.append(password)

st.write("---")
st.subheader("🔑 Need a Strong Password?")
if st.button("Generate Password"):
    strong_password = generate_password()
    st.text_input("Generated Password", value=strong_password, disabled=True)

# Sidebar for Password History
st.sidebar.title("🕒 Password History")
for past_password in st.session_state.password_history[-5:]:
    st.sidebar.write(past_password)
