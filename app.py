from PIL import Image
import time

import streamlit as st
import random

st.set_page_config(page_title="💘 Love Compatibility Matchmaker", page_icon="💘")

st.markdown("<h1 style='text-align: center; color: #ff66b2;'>💘 MBTI Love Compatibility Matchmaker 💘</h1>", unsafe_allow_html=True)
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

    tarot_fortunes = {
        5: [
            "🃏 The Lovers: Divine union, destined paths. This is a soulmate connection wrapped in cosmic timing.",
            "🃏 The Sun: Joy, warmth, and shared purpose. This relationship radiates abundance and light.",
            "🃏 The Empress: Overflowing affection, nurturing energy, and growth. A fertile ground for long-term love."
        ],
        4: [
            "🃏 The Star: Hope and inspiration guide your bond. Stay open to deep emotional healing.",
            "🃏 The Strength: Grace through challenges, loyalty, and courage in love.",
            "🃏 The Chariot: You're both moving forward—just make sure the reins are in sync!"
        ],
        3: [
            "🃏 The Wheel of Fortune: Things could go either way. Are you ready to spin the emotional roulette?",
            "🃏 The Hanged Man: Time to pause and reframe your connection. Growth is possible—if you're patient.",
            "🃏 Justice: This is karmic. Lessons will be learned, whether love lasts or not."
        ],
        2: [
            "🃏 The Tower: Expect emotional earthquakes. But destruction clears the path for truth.",
            "🃏 The Moon: Illusions abound. Dive deep, or risk staying in the shallow end of your feelings.",
            "🃏 Temperance: Only through compromise and healing can this survive. Do you both have the range?"
        ],
        1: [
            "🃏 Death: Let this go. What’s meant for you won’t require CPR.",
            "🃏 The Devil: Obsession, temptation, and codependency. Hot? Yes. Healthy? Nope.",
            "🃏 Five of Cups: Grief, regret, and spilled emotional tea. Better to move on with grace."
        ]
    }
    

    st.markdown("### 🃏 Shuffle & Draw Your Tarot")

    if st.button("🔮 Shuffle the Deck and Draw"):
        with st.spinner("Shuffling the deck..."):
            time.sleep(2)
            drawn_card = random.choice(list(tarot_fortunes[score]))
            card_name = drawn_card.split(":")[0].replace("🃏", "").strip()
            card_file = f"tarot_cards/{card_name.replace(' ', '_')}.png"
            st.image(card_file, caption=card_name)
            st.markdown(f"**Fortune:** _{drawn_card}_")


    st.markdown("### 🃏 Three-Card Tarot Spread")

    if st.button("🔮 Draw Past, Present, and Future Cards"):
        with st.spinner("Drawing your fate..."):
            time.sleep(3)
            cards_drawn = random.sample(list(tarot_fortunes[score]), 3)
            positions = ["Past", "Present", "Future"]
            for i in range(3):
                card_name = cards_drawn[i].split(":")[0].replace("🃏", "").strip()
                card_file = f"tarot_cards/{card_name.replace(' ', '_')}.png"
                st.image(card_file, caption=f"{positions[i]} - {card_name}")
                st.markdown(f"**{positions[i]}:** _{cards_drawn[i]}_")

st.markdown("### 🔮 Tarot of Your Situationship")
    st.markdown(random.choice(tarot_fortunes[score]))
    
    st.markdown("### 🥰 Love Vibe Breakdown")
    st.markdown(f"- **{char1}** meets **{char2}** on a romantic quest for {snack1} & {snack2}.")
    st.markdown(f"- Will this snack-fueled, zodiac-approved, MBTI-entangled duo thrive? Only time—and maybe a horoscope—will tell!")

    st.balloons()


st.markdown("---")
st.markdown("### 😬 Feeling brave? Try **Ex Compatibility Roast Mode**")
if st.button("🔥 Roast My Ex"):
    roast_lines = [
        "Yeah... this one was better off as a plot twist.",
        "Like mixing toothpaste and orange juice. Just—no.",
        "Even the stars gave this one a side-eye.",
        "Your MBTI types clashed like two cats in a bathtub.",
        "Snack compatibility: 0%. One’s popcorn, the other’s raw celery.",
        "This wasn’t a rom-com. This was a horror-com.",
        "They were your villain origin story, huh?",
        "Not a match. Just a lesson… with receipts.",
        "If red flags were currency, y’all would’ve been billionaires.",
        "Astrologers are still recovering from this alignment disaster."
    ]
    st.error("💔 Roast Mode Activated: " + random.choice(roast_lines))


st.markdown("---")
st.markdown("### 📜 Lessons Learned Scroll")

if st.button("🧠 Generate Lessons Learned"):
    lessons = [
        "Trust your gut. And maybe your group chat too.",
        "Just because it's passionate doesn't mean it's permanent.",
        "Red flags don’t turn green with time. Or therapy. (For them.)",
        "You can’t build a castle with someone who brings sand.",
        "Love shouldn't feel like an unpaid internship.",
        "Next time, choose peace over potential.",
        "‘Fixer upper’ is for houses, not partners."
    ]
    st.markdown(f"**🪶 Lesson:** _{random.choice(lessons)}_")

st.markdown("### 🤔 Would You Ever Get Back Together?")
get_back = st.radio("Be honest…", ["Nope. I'm healed 💅", "Maybe, if they changed 🤷", "Absolutely not. 🚫"], key="get_back")

st.markdown(f"**Your answer:** {get_back}")

if get_back == "Nope. I'm healed 💅":
    st.balloons()
    st.success("Proud of you. Growth looks good on you. 💖")
elif get_back == "Absolutely not. 🚫":
    st.error("Block. Delete. Move on. 🔥")
else:
    st.info("Oof. Be careful with that nostalgia loop.")

st.markdown("### 📨 Spicy Mode: Send This To Your Ex")
if st.button("📤 Generate a Spicy Message"):
    messages = [
        "Just ran your MBTI… turns out you were the error in the simulation. 🫠",
        "According to science, snacks, and stardust—this should’ve never happened. ✨🚫",
        "Compatibility says: You were the plot hole in my story arc.",
        "Fun fact: The stars and snacks both said 'nah.'",
        "I checked our match. Spoiler: even Streamlit crashed."
    ]
    st.warning(f"🧨 {random.choice(messages)}")
