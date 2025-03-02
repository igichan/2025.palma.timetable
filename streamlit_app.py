import tkinter as tk
import time
from tkinter import ttk

# 반별 알파벳 과목 매칭 입력 및 시간표 생성

# 반별 사용하는 알파벳 기본값 설정
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

# 반별 시간표 템플릿
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
    "3-3": {"월": ["자율", "C", "I", "A", "B", "F", "공강"],
    "화": ["F", "E", "수과탐", "영1", "음악", "스생", "A"],
    "수": ["진로", "I", "H", "수과탐", "창체", "창체"],
    "목": ["영2", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "음악", "G", "수과탐", "스생"]},
    "3-4": {"월": ["자율", "C", "I", "A", "B", "F", "D"],
    "화": ["F", "E", "영2", "D", "스생", "음악", "A"],
    "수": ["진로", "I", "H", "음악", "창체", "창체"],
    "목": ["D", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "공강", "G", "스생", "영1"]},
    "3-5": {"월": ["자율", "C", "I", "A", "B", "F", "D"],
    "화": ["F", "E", "공강", "D", "스생", "진로", "A"],
    "수": ["영2", "I", "H", "음악", "창체", "창체"],
    "목": ["D", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "스생", "G", "영1", "음악"]},
    "3-6": {"월": ["자율", "C", "I", "A", "B", "F", "D"],
    "화": ["F", "E", "음악", "D", "영2", "영1", "A"],
    "수": ["스생", "I", "H", "공강", "창체", "창체"],
    "목": ["D", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "진로", "G", "음악", "스생"]},
    "3-7": {"월": ["자율", "C", "I", "A", "B", "F", "D"],
    "화": ["F", "E", "스생", "D", "공강", "음악", "A"],
    "수": ["음악", "I", "H", "영2", "창체", "창체"],
    "목": ["D", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "영1", "G", "스생", "진로"]},
    "3-8": {"월": ["자율", "C", "I", "A", "B", "F", "D"],
    "화": ["F", "E", "영1", "D", "음악", "스생", "A"],
    "수": ["진로", "I", "H", "스생", "창체", "창체"],
    "목": ["D", "E", "B", "J", "C", "A", "G"],
    "금": ["H", "B", "C", "음악", "G", "영2", "공강"]}
}

# 반 선택
class_number = input("몇 반입니까? (예: 3-1, 3-2, ..., 3-8 ): ")
if class_number not in class_alphabets:
    print("잘못된 반입니다. 프로그램을 종료합니다.")
    exit()

# 사용자 이름 입력
user_name = input("이름을 입력하세요: ")

# 과목 입력
subject_mapping = {}
print(f"\n{class_number} 반에서 사용하는 알파벳: {', '.join(class_alphabets[class_number])}")
subject_mapping[class_number] = {}
for alpha in class_alphabets[class_number]:
    subject = input(f"{user_name} 님의 {alpha} 과목: ")
    subject_mapping[class_number][alpha] = subject

# 시간표를 과목명으로 변환
def convert_timetable(timetable, mapping):
    converted_timetable = {}
    for day, subjects in timetable.items():
        converted_timetable[day] = [mapping.get(sub, sub) for sub in subjects]
    return converted_timetable

# 선택한 반의 시간표 생성 및 출력
final_timetable = convert_timetable(timetable_template[class_number], subject_mapping[class_number])
print(f"\n{class_number} 반 시간표:")
for day, subjects in final_timetable.items():
    print(f"{day}: {', '.join(subjects)}")

# 파일 이름 자동 설정
txt_filename = f"{class_number} {user_name}_시간표.txt"

# 시간표를 텍스트 파일로 저장
with open(txt_filename, mode='w', encoding='utf-8') as file:
    file.write(f"{class_number} - {user_name} 시간표\n\n")
    for day, subjects in final_timetable.items():
        file.write(f"{day}: {', '.join(subjects)}\n")
print(" ")
time.sleep(1)
print("잠시 후 생성되는 시간표를 캡쳐해서 사용하십시오.")
time.sleep(2)

# GUI 창에서 시간표 표시
def show_timetable():
    root = tk.Tk()
    root.title(f"{class_number} - {user_name} 시간표")
    
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 12), rowheight=30)
    style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
    
    tree = ttk.Treeview(root, columns=["교시"] + list(final_timetable.keys()), show='headings')
    tree.tag_configure("center", anchor="center")
    
    tree.heading("교시", text="교시")
    tree.column("교시", width=50, anchor="center")
    for col in final_timetable.keys():
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")
    
    max_periods = max(len(subjects) for subjects in final_timetable.values())
    for period in range(max_periods):
        row_values = [f"{period+1}교시"] + [final_timetable[day][period] if period < len(final_timetable[day]) else "" for day in final_timetable.keys()]
        tree.insert("", "end", values=row_values, tags=("center",))
    
    tree.pack(expand=True, fill='both')
    root.mainloop()

show_timetable()
