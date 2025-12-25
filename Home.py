import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MyBookBuddy | Your Personal Reading Companion",
    layout="wide",
    page_icon="📚"
)

# -----------------------------
# Sidebar Navigation
# -----------------------------
with st.sidebar:
    st.title("📚 MyBookBuddy")
    nav = st.radio("Navigate", ["🏠 Home", "📖 Recommender"])
    if nav == "📖 Recommender":
        st.switch_page("pages/1_Book_Recommender.py")

# -----------------------------
# Custom CSS (Dark Theme)
# -----------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: #F1F1F1;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4, p {
        color: #F1F1F1;
    }
    div.cta-button button {
        background-color: #2C2F35 !important;
        color: white !important;
        border: none;
        padding: 0.75rem 1.5rem;
        font-size: 18px;
        border-radius: 8px;
        transition: 0.3s ease;
    }
    div.cta-button button:hover {
        background-color: #3B3F47 !important;
        transform: scale(1.05);
        cursor: pointer;
    }
    hr {
        border: 0.5px solid #444;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>📖 Welcome to MyBookBuddy</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='text-align: center; font-size: 18px; max-width: 800px; margin: auto;'>
Your smart, AI-powered reading companion. Discover your next favorite book based on what you already love.
</p>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='cta-button'>", unsafe_allow_html=True)
    go = st.button("🚀 Get Recommendations", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

if go:
    st.switch_page("pages/1_Book_Recommender.py")

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------
# Features Section
# -----------------------------
st.markdown("<h2 style='text-align: center;'>✨ Why MyBookBuddy?</h2>", unsafe_allow_html=True)

features = [
    "🔍 Personalized book recommendations tailored to your taste",
    "🤖 Machine Learning–powered collaborative filtering",
    "📚 Explore books by similarity and popularity",
    "🎯 No login required — simple & fast discovery"
]

for feat in features:
    st.markdown(f"<p style='text-align: center; font-size: 16px;'>{feat}</p>", unsafe_allow_html=True)

st.markdown("<br><hr><br>", unsafe_allow_html=True)

# -----------------------------
# Testimonials (Anonymous)
# -----------------------------
st.markdown("<h3 style='text-align: center;'>💬 What Readers Say</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style='text-align: center;'>
            <div style='font-weight:bold;'>Avid Reader</div>
            <div style='font-size:14px;color:#DDD;'>
                “Discovered books I never imagined I would like.”<br>⭐️⭐️⭐️⭐️⭐️
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='text-align: center;'>
            <div style='font-weight:bold;'>Book Enthusiast</div>
            <div style='font-size:14px;color:#DDD;'>
                “Recommendations feel accurate and thoughtful.”<br>⭐️⭐️⭐️⭐️⭐️
            </div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div style='text-align: center;'>
            <div style='font-weight:bold;'>Student Reader</div>
            <div style='font-size:14px;color:#DDD;'>
                “Clean interface and very easy to use.”<br>⭐️⭐️⭐️⭐️
            </div>
        </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr style='border: 0.5px solid #444;'>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; font-size: 13px; color: #888'>
        Designed & Developed by <strong>Darshan Chandrashekar</strong><br>
        Powered by <strong>Streamlit</strong> & <strong>Machine Learning</strong><br>
        © 2025 MyBookBuddy. All rights reserved.
    </div>
""", unsafe_allow_html=True)
