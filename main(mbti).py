def recommend_best_friend(my_mbti):
    """
    사용자의 MBTI 유형을 입력받아, 베스트 프렌드 궁합 유형을 추천합니다.
    """
    my_mbti = my_mbti.upper() # 대소문자 구분 없이 처리

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

    if my_mbti in mbti_friends_map:
        recommendations = mbti_friends_map[my_mbti]
        print(f"당신과 같은 **{my_mbti}** 유형의 베스트 프렌드 궁합은:")
        for friend_mbti in recommendations:
            print(f"- **{friend_mbti}**")
        print("\n이 조합은 일반적으로 서로의 강점을 보완하고 새로운 관점을 제시해 줄 수 있습니다. 물론, 가장 좋은 관계는 서로를 이해하고 존중하는 노력에서 비롯됩니다!")
    else:
        print(f"**'{my_mbti}'**는 유효한 MBTI 유형이 아닙니다. 다시 확인해주세요. (예: ENFP, ISTJ)")

# --- 사용 예시 ---
# 당신의 MBTI를 입력해보세요.
# my_mbti_type = input("당신의 MBTI 유형을 입력해주세요 (예: ENFP): ")
# recommend_best_friend(my_mbti_type)

# 예시 호출 (직접 코드를 실행하며 테스트해볼 수 있습니다)
print("--- 예시 1 ---")
recommend_best_friend("ENFP")
print("\n--- 예시 2 ---")
recommend_best_friend("istj") # 소문자로 입력해도 작동
print("\n--- 예시 3 (잘못된 입력) ---")
recommend_best_friend("ABCD")
