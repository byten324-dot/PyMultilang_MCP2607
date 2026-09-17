import streamlit as st
import joblib
import sklearn

clf = joblib.load("freq.pkl")

def detect_lang(text):
    # 입력텍스트 소문자 변환
    text = text.lower()

    # 알파벳의 출현 빈도
    cnt = []
    for i in range(26):
      ch = chr(i + ord('a'))
      cnt.append(text.count(ch))

    total = sum(cnt)  # 전체 알파벳 문자 개수.
    if total == 0: return "입력이 없습니다."

    # 입력데이터 준비, 전처리
    freq = list(map(lambda n: n / total, cnt))

    # 예측하기
    pred = clf.predict([freq])

    # 예측결과 리턴
    lang_dic = {
        "en": "영어",
        "fr": "프랑스어",
        "id": "인도네시아어",
        "tl": "타갈로그어",
    }

    return lang_dic[pred[0]]
st.title("외국어 문장 판별")

text = st.text_area("외국어 입력 (입력후 CTRL+ENTER)", height=300)

if text:
  st.badge(detect_lang(text))
