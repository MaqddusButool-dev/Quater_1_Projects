import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .normal-weight { color: green; font-size: 18px; }
    .underweight { color: blue; font-size: 18px; }
    .overweight { color: orange; font-size: 18px; }
    .obese { color: red; font-size: 18px; }
    .container {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Calculate your Body Mass Index (BMI) to check your health status.</p>", unsafe_allow_html=True)

# User input using sliders
weight = st.slider("Select your weight (kg)", 10.0, 200.0, 70.0)
height = st.slider("Select your height (m)", 0.5, 2.5, 1.7)

# Calculate BMI
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2)

if st.button("Calculate BMI 🚀"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        st.markdown(f"<p class='big-font'>Your BMI is: {bmi}</p>", unsafe_allow_html=True)

        if bmi < 18.5:
            st.markdown("<p class='underweight'>⚠️ You are underweight. Consider eating a balanced diet.</p>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p class='normal-weight'>✅ You have a normal weight. Keep up the healthy lifestyle!</p>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<p class='overweight'>⚠️ You are overweight. Consider regular exercise and a balanced diet.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='obese'>🚨 You are obese. It's important to seek medical advice and adopt a healthier lifestyle.</p>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>💙 Stay fit, stay healthy! 💪</p>", unsafe_allow_html=True)
