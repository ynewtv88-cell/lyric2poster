import streamlit as st

st.title("🎵 Lyric2Poster (Open-Source Edition)")
st.write("노래 가사를 입력하면 AI가 아트 브리프를 작성하고 포스터를 생성해주는 앱입니다.")

# 사이드바 설정
st.sidebar.header("설정")
api_key = st.sidebar.text_input("Anthropic API Key", type="password")
passcode = st.sidebar.text_input("Passcode", type="password")

# 메인 입력 폼
st.header("1. 곡 선택 및 가사 입력")
song_title = st.text_input("노래 제목", "Example Song")
artist = st.text_input("아티스트", "Example Artist")
lyrics = st.text_area("가사 입력 (브리프 생성 후 즉시 삭제됩니다)")

if st.button("아트 브리프 생성하기"):
    if not lyrics:
        st.warning("가사를 입력해주세요.")
    else:
        st.success("아트 브리프가 성공적으로 생성되었습니다! (데모 모드)")
        st.json({
            "summary": "A moody evening under neon lights",
            "mood": "Melancholic and dreamy",
            "imagery": "Abstract gradients and city lights",
            "palette": ["#1a1a2e", "#16213e", "#0f3460"]
        })
