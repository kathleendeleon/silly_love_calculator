
import streamlit as st
from PIL import Image

st.set_page_config(page_title="💘 Love Match Analyzer", page_icon="💘")

# Aesthetic header
st.markdown(
    "<h1 style='text-align: center; color: #e75480;'>💘 Love Match Analyzer 💘</h1>",
    unsafe_allow_html=True,
)

st.markdown("Welcome to your personalized compatibility experience! 💫 Fill in your preferences and see how they align with your cosmic and cinematic love fate. ✨")

with st.form("match_form"):
    col1, col2 = st.columns(2)

    with col1:
        mbti = st.selectbox("💡 Your MBTI", [
            "INTJ", "INTP", "ENTJ", "ENTP",
            "INFJ", "INFP", "ENFJ", "ENFP",
            "ISTJ", "ISFJ", "ESTJ", "ESFJ",
            "ISTP", "ISFP", "ESTP", "ESFP"
        ])
        sign = st.selectbox("🔮 Your Zodiac Sign", [
            "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
            "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
        ])
    with col2:
        character = st.text_input("🎬 Favorite Movie or TV Character")
        snack = st.text_input("🍿 Favorite Snack")

    submitted = st.form_submit_button("💞 Find Your Match Vibes!")

if submitted:
    st.markdown("---")
    st.subheader("🧠 Compatibility Vibes Summary")

    # Sample aesthetic logic
    if mbti in ["INFP", "ENFP", "INFJ", "ISFP"]:
        st.success("You're a tender soul with deep emotional currents. You pair well with someone who balances spontaneity with grounding energy.")
    elif mbti in ["INTJ", "ENTJ"]:
        st.success("You're a strategic lover, looking for purpose and power in your connections. You vibe best with someone emotionally aware and patient.")
    else:
        st.success("Your type craves adventure, joy, and playful banter. You thrive with partners who embrace life’s spontaneity.")

    if "chocolate" in snack.lower():
        st.markdown("🍫 Your snack of choice shows you’re a romantic at heart—rich, classic, and sweet.")
    elif "chips" in snack.lower():
        st.markdown("🥔 You like your love salty and crunchy—bold, addictive, and a little dangerous.")
    elif snack:
        st.markdown(f"🍭 '{snack}' is such a unique craving! That says a lot about your quirky and lovable side.")

    st.subheader("✨ Star-Crossed Forecast")
    if sign in ["Aries", "Leo", "Sagittarius"]:
        st.markdown("🔥 You're a fire sign—passionate, daring, and magnetic. You vibe with confident, driven types.")
    elif sign in ["Taurus", "Virgo", "Capricorn"]:
        st.markdown("🌱 An earth sign—you crave stability, depth, and shared values. You ground and grow your relationships.")
    elif sign in ["Gemini", "Libra", "Aquarius"]:
        st.markdown("🌬️ As an air sign, you're curious, expressive, and drawn to mental stimulation and lively dialogue.")
    else:
        st.markdown("🌊 Water signs like you are emotional, nurturing, and intuitive—you seek soulful connections.")

    if character:
        st.subheader("🎬 Inspired by Your Favorite Character")
        st.markdown(f"If you love **{character}**, you probably admire their traits—and your match should too! That says a lot about your values and desires in love 💗")

    st.markdown("---")
    st.balloons()
    st.markdown("<p style='text-align: center;'>✨ Love isn’t logic—it’s vibe ✨</p>", unsafe_allow_html=True)
