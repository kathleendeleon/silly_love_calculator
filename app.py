import streamlit as st
import random

st.set_page_config(page_title="💘 Love Compatibility Matchmaker", page_icon="💘")

st.markdown("<h1 style='text-align: center; color: #ff66b2;'>💘 Kitty's MBTI Love Compatibility Matchmaker 💘</h1>", unsafe_allow_html=True)
st.markdown("Discover if you're the ultimate duo based on MBTI, zodiac signs, favorite characters, and snack vibes. 🌟")

mbti_types = [
    "INFP", "ENFP", "INFJ", "ENFJ", "INTJ", "ENTJ", "INTP", "ENTP",
    "ISFP", "ESFP", "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ"
]

zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

compatibility_matrix = [[5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 1, 1], [5, 5, 5, 5, 4, 4, 4, 5, 1, 1, 1, 1, 2, 2, 1, 1], [5, 5, 5, 5, 4, 4, 4, 4, 1, 1, 1, 1, 2, 2, 2, 1], [5, 5, 5, 5, 4, 4, 4, 5, 1, 1, 1, 1, 2, 2, 2, 1], [4, 4, 4, 4, 5, 5, 5, 4, 2, 2, 2, 2, 3, 3, 2, 2], [4, 4, 4, 4, 5, 5, 5, 5, 2, 2, 2, 2, 3, 3, 2, 2], [4, 4, 4, 4, 5, 5, 5, 5, 2, 2, 2, 2, 3, 3, 3, 3], [5, 5, 4, 5, 4, 5, 5, 5, 2, 2, 2, 2, 3, 3, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 5, 4, 3, 3, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3, 5, 5, 4, 4, 3, 3, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3, 5, 4, 5, 4, 3, 3, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 3, 3, 3, 3], [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 4], [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5], [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5], [2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5]]

def get_compatibility_score(type1, type2):
    idx1 = mbti_types.index(type1)
    idx2 = mbti_types.index(type2)
    score = compatibility_matrix[idx1][idx2]
    return score

def interpret_score(score):
    if score == 5:
        return "💖 Often Listed as an Ideal Match"
    elif score == 4:
        return "🌟 It's Got a Good Chance"
    elif score == 3:
        return "💡 One Sided Match"
    elif score == 2:
        return "⚠️ It Could Work, But Not Ideal"
    else:
        return "🚨 Uh-Oh, Think This One Through"

def funny_description(score):
    options = {
        5: [
            "You're the peanut butter to their jelly. Wedding Pinterest board ready.",
            "Soulmates. You probably finish each other's sentences and sandwiches.",
            "This duo could write a rom-com and star in it. Netflix deal pending."
        ],
        4: [
            "You're like WiFi and a good password—meant to connect.",
            "Arguments may occur, but so do shared Spotify playlists and tacos.",
            "Definitely a 'we met at Trader Joe's' love story waiting to happen."
        ],
        3: [
            "You’re vibing on one channel while they're buffering. Could be cute or chaotic.",
            "One of you is falling hard. The other? Still reading red flags as love letters.",
            "A bit like pineapple on pizza—unexpected, and someone definitely has opinions."
        ],
        2: [
            "This might require a relationship user manual... and maybe a fire extinguisher.",
            "You talk feelings, they talk facts. But hey, opposites *sometimes* attract?",
            "Could work if you both take turns being the emotional support burrito."
        ],
        1: [
            "This match is like trying to hug a cactus—best from a safe distance.",
            "You’ll learn a lot… mostly about patience and how to bite your tongue.",
            "Like oil and water... in a blender... on fire."
        ]
    }
    return random.choice(options[score])

st.markdown("### 💁 Partner 1")
col1, col2 = st.columns(2)
with col1:
    mbti1 = st.selectbox("MBTI Type", mbti_types, key="mbti1")
    zodiac1 = st.selectbox("Zodiac Sign", zodiac_signs, key="zodiac1")
with col2:
    char1 = st.text_input("Favorite Movie Character", key="char1")
    snack1 = st.text_input("Favorite Snack", key="snack1")

st.markdown("### 💘 Partner 2")
col3, col4 = st.columns(2)
with col3:
    mbti2 = st.selectbox("MBTI Type", mbti_types, key="mbti2")
    zodiac2 = st.selectbox("Zodiac Sign", zodiac_signs, key="zodiac2")
with col4:
    char2 = st.text_input("Favorite Movie Character", key="char2")
    snack2 = st.text_input("Favorite Snack", key="snack2")

if st.button("🔮 Reveal the Love Match!"):
    score = get_compatibility_score(mbti1, mbti2)
    meaning = interpret_score(score)
    funny = funny_description(score)

    st.markdown("---")
    st.subheader("💌 Compatibility Summary")
    st.markdown(f"**{mbti1} ({zodiac1})** ❤️ **{mbti2} ({zodiac2})** = **Score: {score}/5**")
    st.success(meaning)
    st.info(f"📝 {funny}")

    st.markdown("### 🥰 Love Vibe Breakdown")
    st.markdown(f"- **{char1}** meets **{char2}** on a romantic quest for {snack1} & {snack2}.")
    st.markdown(f"- Will this snack-fueled, zodiac-approved, MBTI-entangled duo thrive? Only time—and maybe a horoscope—will tell!")

    st.balloons()
