import streamlit as st

# Set page configuration
st.set_page_config(page_title="My Portfolio", page_icon="🌟", layout="wide")

# Inject Custom CSS
st.markdown(
    """
    <style>
    
    /* Main container */
    .main-container {
        max-width: 1000px;  /* Increased width for more left & right margin */
        margin: 40px auto;  /* Adds space around */
        padding: 40px;
        background: white;
        border-radius: 15px;
        box-shadow: 4px 4px 20px rgba(0,0,0,0.1);
        text-align: center;
    }

    /* Section titles */
    .section-title {
        font-size: 30px;
        font-weight: bold;
        color: white;
        margin-top: 30px;
        padding-bottom: 10px;
        border-bottom: 3px solid #ff4081;
        display: inline-block;
    }

    /* Card-style div */
    .card {
        background: #ff4081;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 3px 3px 15px rgba(0,0,0,0.15);
        margin: 15px auto;
        border-left: 6px solid #ffffff;
        text-align: center;
        transition: 0.3s;
    }
    .card:hover {
        transform: scale(1.05);
        box-shadow: 5px 5px 20px rgba(0,0,0,0.2);
    }

    /* Social Media Buttons */
    .social-icons a {
        display: inline-block;
        margin: 10px;
        text-decoration: none;
        font-size: 22px;
        color: white;
        padding: 8px 15px;
        border-radius: 8px;
        border: 2px solid #ff4081;
        transition: 0.3s;
        font-weight: bold;
    }
    .social-icons a:hover {
        background-color: #ff4081;
        color: white;
    }

    /* Buttons */
    .btn {
        background-color: #ff4081;
        color: white;
        padding: 12px 25px;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
        margin-top: 15px;
        font-weight: bold;
        font-size: 18px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }
    .btn:hover {
        background-color: black;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: black;
        margin-top: 40px;
        font-size: 16px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Container

st.markdown("<h1 style='text-align: center; color: #ff4081;'> Welcome to My Portfolio</h1>", unsafe_allow_html=True)
st.write("<div style='text-align: center'> Hi, I'm Maqddus Buttool, a passionate Frontend Developer specializing in React.js, Next.js, and Tailwind CSS</div>", unsafe_allow_html=True)

# About Me Section
st.markdown("<div class='section-title'>🏆 About Me</div>", unsafe_allow_html=True)
st.write("I am a **frontend developer** with a strong interest in building **modern web applications** using cutting-edge technologies.")

# Skills Section
st.markdown("<div class='section-title'>🔧 Skills</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='card'><b>🌐 Frontend</b><br>React.js, Next.js, JavaScript, HTML, CSS</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><b>🎨 UI/UX</b><br>Tailwind CSS, Bootstrap, Figma</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'><b>🔗 Version Control</b><br>Git, GitHub</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><b>⚙️ Tools</b><br>Vercel, VS Code</div>", unsafe_allow_html=True)

# Projects Section
st.markdown("<div class='section-title'>🚀 Projects</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>📝 To-Do App – A simple and interactive to-do list app built with React.js.</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>📊 Data Dashboard – A data visualization dashboard using Next.js and Tailwind.</div>", unsafe_allow_html=True)
st.markdown("<div class='card'>🎮 Blackjack Game – A Python-based CLI Blackjack game with AI agents.</div>", unsafe_allow_html=True)

# Social Media Links
st.markdown("<div class='section-title'>📬 Connect with Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class="social-icons">
    <a href="https://github.com/Maqddus-Buttool" target="_blank">GitHub</a> 
    <a href="https://www.linkedin.com/in/MaqddusButtool" target="_blank">LinkedIn</a>
</div>
""", unsafe_allow_html=True)

# Contact Form
st.markdown("<div class='section-title'>📩 Contact Me</div>", unsafe_allow_html=True)
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")
if st.button("Send Message 🚀", key="contact_btn"):
    st.success("Message Sent! I'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("<p style=' background: white; bgcolor: #f9f9f9; padding: 10px; border-radius: 8px; border: 2px solid #ff4081; transition: 0.3s; font-weight: bold;' class='footer'>© 2025 Maqddus Buttool | Built with ❤️ in Streamlit</p>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True) 
