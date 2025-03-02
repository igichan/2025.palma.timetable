import streamlit as st
import pandas as pd

# 반별 알파벳 과목 매칭 입력 및 시간표 생성
class_alphabets = {
    "3-1": sorted(["C", "I", "B", "F", "D", "E", "J", "G", "H"]),
    "3-2": sorted(["I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-3": sorted(["C", "I", "A", "B", "F", "E", "J", "G", "H"]),
    "3-4": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-5": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-6": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-7": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-8": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"])
}

# 반별 시간표 데이터
timetable_template = {
    "3-1": {"월": ["자율", "C", "I", "진로", "B", "F", "D"],
            "화": ["F", "E", "음악", "D", "화작", "영2", "스생"],
            "수": ["영1", "I", "H", "화작", "창체", "창체"],
            "목": ["D", "E", "B", "J", "C", "스생", "G"],
            "금": ["H", "B", "C", "공강", "G", "음악", "화작"]},
    "3-2": {"월": ["자율", "진로", "I", "A", "B", "F", "D"],
            "화": ["F", "E", "스생", "D", "공강", "화작", "A"],
            "수": ["화작", "I", "H", "영1", "창체", "창체"],
            "목": ["D", "E", "B", "J", "음악", "A", "G"],
            "금": ["H", "B", "음악", "스생", "G", "화작", "영2"]},
}

# Streamlit UI 생성
st.title("📅 학교 시간표 생성기")

# 반 선택
class_number = st.selectbox("반을 선택하세요", list(timetable_template.keys()))

# 사용자 이름 입력
user_name = st.text_input("이름을 입력하세요")

if user_name:
    # 과목 입력
    subject_mapping = {}
    st.write(f"{class_number} 반에서 사용하는 알파벳: {', '.join(class_alphabets[class_number])}")
    for alpha in class_alphabets[class_number]:
        subject_mapping[alpha] = st.text_input(f"{user_name} 님의 {alpha} 과목: ", key=alpha)

    # 시간표를 과목명으로 변환
    def convert_timetable(timetable, mapping):
        return {day: [mapping.get(sub, sub) for sub in subjects] for day, subjects in timetable.items()}

    # 선택한 반의 시간표 생성
    final_timetable = convert_timetable(timetable_template[class_number], subject_mapping)

    # 시간표 표시
    df = pd.DataFrame.from_dict(final_timetable, orient='index', columns=["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"])
    st.write(f"### 🏫 {class_number}반 {user_name}의 시간표")
    st.dataframe(df)

    # 다운로드 기능
    csv = df.to_csv(index=True).encode('utf-8')
    st.download_button("📥 시간표 다운로드 (CSV)", csv, f"{class_number}_{user_name}_timetable.csv", "text/csv")
