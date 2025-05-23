import streamlit as st

def get_best_friend_recommendations(my_mbti):
    """
    사용자의 MBTI 유형을 입력받아, 베스트 프렌드 궁합 유형을 추천합니다.
    """
    my_mbti = my_mbti.upper().strip() # 대소문자 구분 없이, 공백 제거

    # MBTI 유형별 추천 궁합 (일반적인 궁합 이론 기반)
    # 실제 관계는 개인의 성숙도와 노력에 따라 달라질 수 있습니다.
    mbti_friends_map = {
        # 분석가 (Analyst) 유형
        "INTJ": ["ENTP", "ENFP"],
        "INTP": ["ENTJ", "ENFJ"],
        "ENTJ": ["INTP", "INFJ"],
        "ENTP": ["INTJ", "INFJ"],

        # 외교관 (Diplomat) 유형
        "INFJ": ["ENFP", "ENTP"],
        "INFP": ["ENFJ", "ENTJ"],
        "ENFJ": ["INFP", "INTP"],
        "ENFP": ["INFJ", "INTJ"],

        # 관리자 (Sentinel) 유형
        "ISTJ": ["ESFP", "ESTP"],
        "ISFJ": ["ESFJ", "ESTJ"],
        "ESTJ": ["ISFJ", "ISTP"],
        "ESFJ": ["ISFJ", "ISTP"], # ESFJ는 ISFJ, ISTP와 상호보완적 관계

        # 탐험가 (Explorer) 유형
        "ISTP": ["ESTJ", "ESFJ"],
        "ISFP": ["ENFJ", "ESFJ"], # ISFP는 ENFJ, ESFJ와 상호보완적 관계
        "ESTP": ["ISTJ", "ISFJ"],
        "ESFP": ["ISTJ", "ISFJ"],
    }

    # 유효한 MBTI 유형 목록
    valid_mbti_types = list(mbti_friends_map.keys())

    if my_mbti in valid_mbti_types:
        recommendations = mbti_friends_map[my_mbti]
        st.success(f"**{my_mbti}** 유형의 베스트 프렌드 궁합은 다음과 같습니다:")
        for friend_mbti in recommendations:
            st.markdown(f"- **{friend_mbti}**")
        st.markdown(
            """
            <small>이 조합은 일반적으로 서로의 강점을 보완하고 새로운 관점을 제시해 줄 수 있습니다.
            물론, 가장 좋은 관계는 서로를 이해하고 존중하는 노력에서 비롯됩니다! 😊</small>
            """, unsafe_allow_html=True
        )
    else:
        st.error(f"**'{my_mbti}'**는 유효한 MBTI 유형이 아닙니다. 다시 확인해주세요.")
        st.info("올바른 MBTI 유형 (예: ENFP, ISTJ)을 4글자로 입력해주세요.")
        st.markdown(f"<small>유효한 MBTI 유형 목록: {', '.join(valid_mbti_types)}</small>", unsafe_allow_html=True)


# --- Streamlit 앱 구성 ---

st.set_page_config(
    page_title="MBTI 베스트 프렌드 궁합 찾기",
    page_icon="👯‍♀️",
    layout="centered"
)

st.title("💖 MBTI 베스트 프렌드 궁합 찾기 💖")
st.markdown("당신의 MBTI를 입력하면, 최고의 친구 궁합을 추천해 드립니다!")

# 사용자 입력 받기
user_mbti = st.text_input("당신의 MBTI 유형을 입력해주세요 (예: ENFP, ISTJ):")

# 버튼 클릭 시 결과 표시
if st.button("베스트 프렌드 추천받기"):
    if user_mbti:
        get_best_friend_recommendations(user_mbti)
    else:
        st.warning("MBTI 유형을 입력해주세요!")

st.markdown("---")
st.markdown(
    """
    <small>
    본 앱은 일반적인 MBTI 궁합 이론을 기반으로 재미를 위해 제작되었습니다.
    실제 사람과의 관계는 MBTI 유형만으로 판단할 수 없으며, 서로의 노력과 이해가 가장 중요합니다.
    </small>
    """, unsafe_allow_html=True
)

