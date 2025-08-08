import streamlit as st
import random

# MBTI Types
mbti_types = [
    "INFP", "ENFP", "INFJ", "ENFJ", "INTJ", "ENTJ", "INTP", "ENTP",
    "ISFP", "ESFP", "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ"
]

# Compatibility chart scores
legend_scores = {
    "blue": 100,
    "teal": 75,
    "olive": 62,
    "yellow": 50,
    "red": 25
}

compatibility_colors = [
    ["blue","blue","blue","blue","blue","blue","blue","blue","red","red","red","red","red","red","red","red"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","red","red","red","red","red","red","red","red"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","red","red","red","red","red","red","red","red"],
    ["blue","blue","blue","red", "blue","blue","blue","red", "olive","olive","yellow","yellow","yellow","yellow","blue","blue"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","olive","olive","yellow","yellow","yellow","yellow","blue","blue"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","olive","olive","yellow","yellow","yellow","yellow","blue","blue"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","olive","olive","yellow","yellow","yellow","yellow","blue","blue"],
    ["blue","blue","blue","blue","blue","blue","blue","blue","olive","olive","yellow","yellow","yellow","yellow","blue","blue"],
    ["red", "blue","red", "olive","olive","olive","olive","olive","olive","yellow","yellow","yellow","yellow","yellow","blue","blue"],
    ["red", "red", "red", "olive","olive","olive","olive","olive","yellow","yellow","yellow","yellow","yellow","yellow","blue","blue"],
    ["red", "red", "red", "yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","blue","blue"],
    ["red", "red", "red", "yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","blue","blue"],
    ["red", "red", "red", "yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","blue","blue","blue","blue"],
    ["red", "red", "red", "yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","yellow","blue","blue","blue","blue"],
    ["red", "red", "red", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"],
    ["red", "red", "red", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue", "blue"]
]

compatibility_scores = {}
for i, row_type in enumerate(mbti_types):
    for j, col_type in enumerate(mbti_types):
        key = (row_type, col_type)
        color = compatibility_colors[i][j]
        score = legend_scores.get(color, 50)
        compatibility_scores[key] = (score, color)

# Fun match descriptions by tier
def get_match_description(score):
    if score >= 90:
        return "Soulmates written in the stars 💍💖"
    elif score >= 75:
        return "A power duo with real couple goals vibes ✨"
    elif score >= 60:
        return "Some sparks, some chaos... classic rom-com energy 🎭"
    elif score >= 45:
        return "There's potential, but also potential for drama 🍿"
    else:
        return "This might belong in the 🚩 museum. Proceed with popcorn. 🍿🫣"

# Emoji/Color badges
color_badge = {
    "blue": "💙 Ideal Match",
    "teal": "💚 Good Chance",
    "olive": "💛 One-Sided Match",
    "yellow": "🧡 Might Work",
    "red": "❤️‍🔥 Think This One Through"
}

# Tarot card descriptions
tarot_cards = [
    ("The Lovers", "A bond filled with passion and mutual respect."),
    ("The Tower", "Sudden changes or revelations shake the relationship."),
    ("The Star", "Hope and healing bring light to your love story."),
    ("The Moon", "Hidden truths or mysteries may affect your connection."),
    ("The Sun", "Joy, warmth, and mutual happiness shine on your bond."),
    ("The Devil", "Temptation or unhealthy attachment may cloud your love."),
    ("The Empress", "Fertile grounds for nurturing and romance blossom."),
    ("The Fool", "A fresh, spontaneous start full of playful energy."),
    ("Justice", "A relationship balanced with fairness and integrity."),
    ("Death", "An ending that leads to a transformative new chapter."),
    ("Temperance", "Harmony, balance, and mutual understanding abound."),
    ("Judgement", "A moment of reckoning, reflection, or reconciliation."),
]

def draw_tarot():
    return random.sample(tarot_cards, 3)

# Streamlit App
st.set_page_config("MBTI Love Match", page_icon="💘")
st.title("💘 MBTI Love Match Analyzer")

col1, col2 = st.columns(2)
with col1:
    user1 = st.selectbox("Select Your MBTI Type:", mbti_types, index=0)
with col2:
    user2 = st.selectbox("Select Their MBTI Type:", mbti_types, index=1)

if st.button("💞 Calculate Love Match"):
    key = (user1, user2)
    if key not in compatibility_scores:
        key = (user2, user1)
    score, color = compatibility_scores.get(key, (50, "yellow"))
    st.subheader("❤️ Compatibility Results")
    st.markdown(f"### **{user1} x {user2}**")
    st.markdown(f"**Score:** {score}/100")
    st.markdown(f"**Match Type:** {color_badge[color]}")
    st.info(get_match_description(score))

    st.subheader("🔮 3-Card Tarot Love Spread")
    tarot_spread = draw_tarot()
    col_past, col_present, col_future = st.columns(3)
    with col_past:
        st.markdown("**Past**")
        st.write(f"{tarot_spread[0][0]}: {tarot_spread[0][1]}")
    with col_present:
        st.markdown("**Present**")
        st.write(f"{tarot_spread[1][0]}: {tarot_spread[1][1]}")
    with col_future:
        st.markdown("**Future**")
        st.write(f"{tarot_spread[2][0]}: {tarot_spread[2][1]}")
