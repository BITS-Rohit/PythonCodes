import streamlit as st

st.title("Tweakio Python Interface")
st.subheader("Made By Rohit Gupta")
st.text("Below you will have to select the options for the Tweakio Options")

# ================= Country Selection =================
option: str = st.selectbox(
    "Select the country : ",
    ["Choose one [Required]", "India", "USA", "UK", "Canada", "Australia"]
)
if option != "Choose one [Required]":
    st.success(f"Selected Country : {option} [Success]")

button: bool = st.button("Submit")
if button and option == "Choose one [Required]":
    st.error("Please select a valid country [Error]")
elif button:
    st.info(f"Submitted Country : {option} [Info]")

# ================= Agree to Terms =================
agreeTerms = st.checkbox("I agree to the terms and conditions", key="agree")

# ================= Login Mode =================
Login_Mode = st.radio("Login Mode", ("Choose One [Required]", "0 [QR Scan Mode]", "1 [Via Code Mode]"))

# ================= Feedback =================
Feedback = st.text_input("Feedback on the APP : ", max_chars=100)
if st.button("Submit Feedback"):
    st.success("Feedback Submitted : " + Feedback)

# ================= Slider with Disable Logic =================
# Use session_state for persistent control
if "slider_disabled" not in st.session_state:
    st.session_state.slider_disabled = False

TopChatFetch = st.slider(
    "Select No of Top Chat Fetch",
    min_value=0, max_value=6, step=1, value=3, format="%d",
    disabled=st.session_state.slider_disabled
)
st.write("Top Chat Fetch : " + str(TopChatFetch))

# Checkbox to toggle disable/enable
if st.checkbox("Disable slider", key="dis"):
    st.session_state.slider_disabled = True
    st.write("Slider Disabled")
else:
    st.session_state.slider_disabled = False
    st.write("Slider Enabled")

# ================= Number Input =================
num_input = st.number_input(
    "Enter No of Bots to be deployed : ",
    min_value=1, step=1, max_value=20
)
st.write("No of Bots to be deployed : " + str(num_input))

# ================= Date Input =================
date = str(st.date_input("Select Date : ", format="YYYY-MM-DD"))
st.write("Selected Date : " + date)
