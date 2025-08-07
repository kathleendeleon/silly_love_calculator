import streamlit as st
import random

st.set_page_config(page_title="Love Match Tarot App", page_icon="💘", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: pink;'>💘 Love Matchmaker + Tarot Cards 💘</h1>",
    unsafe_allow_html=True,
)

# Tarot card meanings
tarot_descriptions = {
    "The Lovers": "Represents harmony, love, and alignment of values.",
    "The Empress": "Symbolizes beauty, abundance, and nurturing.",
    "The Chariot": "Indicates determination, control, and victory.",
    "The Devil": "Represents temptation, passion, or unhealthy attachments.",
    "The Tower": "Signifies sudden change, upheaval, and revelation.",
    "The Star": "Symbolizes hope, inspiration, and renewal.",
    "The Moon": "Represents illusion, intuition, and emotional fluctuation.",
    "The Sun": "A card of joy, success, and positivity.",
    "Wheel of Fortune": "Signals fate, karma, and life's cycles.",
    "Justice": "Symbol of truth, fairness, and law.",
    "Temperance": "Indicates balance, harmony, and patience.",
    "Death": "Signifies endings, transformation, and rebirth."
}

# Form for user and partner input
with st.form("love_form"):
    st.subheader("💕 Enter Partner Info")
    name1 = st.text_input("Your Name")
    mbti1 = st.selectbox("Your MBTI", ["INTJ", "INFP", "ENFP", "ISTP", "ESFJ", "ENTP", "ISFJ"])
    zodiac1 = st.selectbox("Your Zodiac", [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    char1 = st.text_input("Favorite Movie/TV Character")
    snack1 = st.text_input("Favorite Snack")

    st.markdown("---")

    st.subheader("❤️ Partner Info")
    name2 = st.text_input("Partner's Name")
    mbti2 = st.selectbox("Partner's MBTI", ["INTJ", "INFP", "ENFP", "ISTP", "ESFJ", "ENTP", "ISFJ"])
    zodiac2 = st.selectbox("Partner's Zodiac", [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio",
