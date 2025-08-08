import streamlit as st
import random

# MBTI Types
mbti_types = [
    "INFP", "ENFP", "INFJ", "ENFJ", "INTJ", "ENTJ", "INTP", "ENTP",
    "ISFP", "ESFP", "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ"
]

mbti_descriptions = {
    "INFP": "The poetic softie who overthinks texts and falls in love with your Spotify playlist. 🧚‍♀️📖",
    "ENFP": "A chaotic glitter cannon of affection who starts 5 new hobbies every month (and might flirt with a houseplant). ✨🌱",
    "INFJ": "The psychic therapist who’ll analyze your childhood *and* bake you banana bread. 🔮🍞",
    "ENFJ": "Your overachieving emotional life coach who schedules cuddles and inspires cult followings. 🫶📅",
    "INTP": "Living in their brain, forgetting your birthday, but inventing a teleportation machine to make it up to you. 🧠🔧",
    "ENTP": "Flirts via debate, seduces via chaos, disappears via trapdoor. 🌀📣",
    "INTJ": "Plans your wedding and funeral in the same spreadsheet. Loves deeply, but won’t admit it until Q4. 📊🖤",
    "ENTJ": "Dominates the boardroom, forgets your dog's name. But buys it stock in your future. 💼💋",
    "ISFP": "Hot, mysterious, and probably writing a love song about you as we speak. 🎨🎶",
    "ESFP": "The human disco ball. Will cry over a dog video then drag you to karaoke. 💃😭🎤",
    "ISTP": "Fixes your sink, ghosts your texts, then reappears like nothing happened. 🛠️🫥",
    "ESTP": "Red flag in human form, but makes it *so fun*. Will win your heart and a bar fight. 🥊❤️",
    "ISFJ": "The cinnamon roll who’ll remember your dog’s half-birthday and never leave your side. 🐾🎀",
    "ESFJ": "PTO president of your heart. Throws themed dinners, texts back immediately, and lowkey controls the group chat. 📱🍝",
    "ISTJ": "A stoic teddy bear. Takes 5 years to open up, then never stops fixing your life. 🧸📏",
    "ESTJ": "Emotionally constipated but will help you file your taxes, clean your garage, and organize your soul. 🗂️❤️"
}

# Zodiac signs and their love insights and elements
zodiac_signs = {
    "Aries": ("🔥 Passionate but impatient. Needs sparks AND stability.", "Fire"),
    "Taurus": ("🌿 Loyal and indulgent. Feed them snacks and love.", "Earth"),
    "Gemini": ("🌬️ Chatty, curious, and prone to ghosting their own emotions.", "Air"),
    "Cancer": ("🌊 Deep feeler, moon child. Handle with care or tissues.", "Water"),
    "Leo": ("🌞 Loves hard, but loves themselves just a little more.", "Fire"),
    "Virgo": ("🌾 Overanalyzing everything you just said. But with love.", "Earth"),
    "Libra": ("⚖️ Charm machine. Can’t pick a restaurant or a partner.", "Air"),
    "Scorpio": ("🦂 Loyal, intense, mysterious. Dangerously hot.", "Water"),
    "Sagittarius": ("🔥 Adventure-loving flirt with commitment allergies.", "Fire"),
    "Capricorn": ("⛰️ Ambitious and guarded. Will schedule love on a spreadsheet.", "Earth"),
    "Aquarius": ("🌌 Emotionally intelligent or emotionally unavailable. Or both.", "Air"),
    "Pisces": ("🐟 Romantic dreamers. Will write you poetry and cry during it.", "Water")
}

# Element compatibility
element_compatibility = {
    ("Fire", "Air"): "🔥🔥 Dynamic Duo! Air fuels Fire.",
    ("Air", "Fire"): "🔥🔥 Dynamic Duo! Air fuels Fire.",
    ("Earth", "Water"): "🌍🌊 Grounded and nurturing. Earth supports Water.",
    ("Water", "Earth"): "🌍🌊 Grounded and nurturing. Earth supports Water.",
    ("Fire", "Water"): "🔥🌊 Steamy but volatile! Opposites attract.",
    ("Water", "Fire"): "🔥🌊 Steamy but volatile! Opposites attract.",
    ("Air", "Earth"): "🌬️🌎 Can be rocky. Air feels confined.",
    ("Earth", "Air"): "🌬️🌎 Can be rocky. Air feels confined.",
    ("Fire", "Earth"): "🔥🌍 Passion meets practicality. Needs balance.",
    ("Earth", "Fire"): "🔥🌍 Passion meets practicality. Needs balance.",
    ("Air", "Water"): "🌬️🌊 Emotion meets logic. Communication is key.",
    ("Water", "Air"): "🌬️🌊 Emotion meets logic. Communication is key.",
    ("Fire", "Fire"): "🔥🔥 Explosive chemistry. Also actual explosions?", 
    ("Earth", "Earth"): "🌍🌍 Steady and loyal. Possibly a bit too chill.",
    ("Air", "Air"): "🌬️🌬️ Endless ideas, but who’s doing the dishes?",
    ("Water", "Water"): "🌊🌊 All the feels. Drowning in emotions (in a good way?)"
}

# Compatibility chart scores
legend_scores = {
    "blue": 100,
    "teal": 75,
    "olive": 62,
    "yellow": 50,
    "red": 25
}

mbti_types_list = mbti_types
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

color_badge = {
    "blue": "💙 Ideal Match",
    "teal": "💚 Good Chance",
    "olive": "💛 One-Sided Match",
    "yellow": "🧡 Might Work",
    "red": "❤️‍🔥 Think This One Through"
}

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

# Streamlit UI
st.set_page_config("MBTI Love Match", page_icon="💘")
st.title("💘 Kath's MBTI Love Match Analyzer")
st.subheader("_Loveshack bb_ 😗")

st.audio("https://ia803409.us.archive.org/31/items/The_B-52s_Love_Shack_1989/The_B-52s_Love_Shack_1989.mp4", format="audio/mpeg", loop=True)

col1, col2 = st.columns(2)
with col1:
    name1 = st.text_input("Your Name")
    user1 = st.selectbox("Your MBTI Type:", mbti_types)
    zodiac1 = st.selectbox("Your Zodiac Sign:", list(zodiac_signs.keys()))
with col2:
    name2 = st.text_input("Their Name")
    user2 = st.selectbox("Their MBTI Type:", mbti_types)
    zodiac2 = st.selectbox("Their Zodiac Sign:", list(zodiac_signs.keys()))

if st.button("💞 Calculate Love Match"):
    key = (user1, user2)
    if key not in compatibility_scores:
        key = (user2, user1)
    score, color = compatibility_scores.get(key, (50, "yellow"))

    st.subheader("❤️ Compatibility Results")
    st.markdown(f"### **{name1 or user1} x {name2 or user2}**")
    st.markdown(f"**Score:** {score}/100")
    st.markdown(f"**Match Type:** {color_badge[color]}")
    st.info(get_match_description(score))
    st.markdown(f"**You ({user1})**: {mbti_descriptions[user1]}")
    st.markdown(f"**Them ({user2})**: {mbti_descriptions[user2]}")

    st.subheader("🌟 Zodiac Insights")
    insight1, elem1 = zodiac_signs[zodiac1]
    insight2, elem2 = zodiac_signs[zodiac2]
    st.markdown(f"**{zodiac1} ({elem1})**: {insight1}")
    st.markdown(f"**{zodiac2} ({elem2})**: {insight2}")

    elem_combo = (elem1, elem2)
    zodiac_match = element_compatibility.get(elem_combo, "🤷 Element vibes are neutral. Depends on the mood!")
    st.success(f"**Element Match:** {zodiac_match}")

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

if st.button("🔥 Roast My Ex"):
    st.subheader("💔 Roast Mode Activated")
    roasts = [
        "They were the walking red flag collection 🧨",
        "Honestly, your ex made Mercury retrograde feel peaceful.",
        "You dodged a personality black hole. Cheers 🥂",
        "They thought 'emotional depth' was a swimming pool. Shallow AF.",
        "Your ex's love language was probably 'confusing signals'."
    ]
    st.warning(random.choice(roasts))
