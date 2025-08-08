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
