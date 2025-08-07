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

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# Compatibility roast descriptions
def funny_compatibility_summary(score):
    if score > 90:
        return "🔥 Soulmate energy! Y’all are like PB & J—sweet, sticky, and destined."
    elif score > 80:
        return "💞 A power couple with the occasional rom-com misunderstanding."
    elif score > 70:
        return "🫶 Not bad! With snacks and therapy, you could last forever-ish."
    elif score > 60:
        return "😬 There’s hope… if Mercury isn’t in retrograde and nobody forgets to text back."
    else:
        return "🚩 Cosmic red flags detected. Proceed only if you're into emotional roller coasters."

# Form for user and partner input
with st.form("love_form"):
    st.subheader("💕 Enter Your Info")
    name1 = st.text_input("Your Name")
    mbti1 = st.selectbox("Your MBTI", mbti_types)
    zodiac1 = st.selectbox("Your Zodiac", [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    char1 = st.text_input("Favorite Movie/TV Character")
    snack1 = st.text_input("Favorite Snack")

    st.markdown("---")

    st.subheader("❤️ Partner Info")
    name2 = st.text_input("Partner's Name")
    mbti2 = st.selectbox("Partner's MBTI", mbti_types)
    zodiac2 = st.selectbox("Partner's Zodiac", [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    char2 = st.text_input("Partner's Favorite Movie/TV Character")
    snack2 = st.text_input("Partner's Favorite Snack")

    submitted = st.form_submit_button("🔮 Reveal Love Match")

# Results
if submitted:
    st.markdown("## 💞 Compatibility Results")
    score = random.randint(55, 98)
    st.success(f"🌹 {name1} and {name2} are **{score}% compatible!**")
    st.markdown(f"💌 {funny_compatibility_summary(score)}")

    st.markdown(f"""
### 💖 Couple Vibes:
- **MBTI Match**: {mbti1} 💘 {mbti2}
- **Zodiac Signs**: {zodiac1} + {zodiac2}
- **Fave Characters**: {char1} + {char2}
- **Snack Combo**: {snack1} & {snack2}
""")

    st.markdown("## 🃏 Tarot Love Forecast")
    tarot_cards = list(tarot_descriptions.keys())
    selected = random.sample(tarot_cards, 3)
    positions = ["Past", "Present", "Future"]
    for i in range(3):
        st.markdown(f"### {positions[i]}: {selected[i]}")
        st.info(tarot_descriptions[selected[i]])

    st.markdown("## 🔥 Bonus Modes")
    if score < 70:
        st.warning("💔 Roast Mode: Y'all might be cosmic frenemies. Try again in your next life!")
    else:
        st.info("💌 Your destiny is written in the stars... and snacks.")

