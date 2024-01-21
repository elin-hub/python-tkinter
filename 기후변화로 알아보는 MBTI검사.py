from tkinter import *
import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.ttk import *


#MBTI타입 
mbti_type = {"INTJ": "용의주도한 전략가형", 
"INTP": "논리적인 사색가형",
"ENTJ": "대담한 통솔자형",
"ENTP": "뜨거운 논쟁을 즐기는 변론가형",
"ENFP": "재기발랄한 활동가형",
"ENFJ": "정의로운 사회 운동가형",
"INFP": "열정적인 중재자형",
"INFJ": "선의의 옹호자형",
"ESFJ": "사교적인 외교관형",
"ESTJ": "엄격한 관리자형",
"ISFJ": "용감한 수호자형",
"ISTJ": "청렴결백한 논리주의자형",
"ESFP": "자유로운 영혼의 연예인형",
"ESTP": "모험을 즐기는 사업가형",
"ISFP": "호기심 많은 예술가형",
"ISTP": "만능 재주꾼형"
}
#MBTI유형별 환경관련 직업추천 
mbti_job = {
"INTJ": "환경공학 기술자",
"INTP": "환경법률 전문가",
"ENTJ": "환경 컨설턴트",
"ENTP": "환경관련 고위임원",
"ENFP": "재활용 코디네이터",
"ENFJ": "친환경 제품 개발자",
"INFP": "소음진동 기술자",
"INFJ": "기후변화 전문가",
"ESFJ": "신재생 에너지 전문가",
"ESTJ": "실내 공기질 관리사",
"ISFJ": "지구과학 선생님",
"ISTJ": "생태계 복원 관리 연구원",
"ESFP": "재활용품 예술가",
"ESTP": "환경 영향 평가원",
"ISFP": "나무치료사",
"ISTP": "온라인 전기자동차 연구원"}

#최고궁합
mbti_good = {
"INTJ": "ESFP", 
"INTP": "ESFJ", 
"ENTJ": "ISFP", 
"ENTP": "ISFJ", 
"ENFP": "ISTJ", 
"ENFJ": "ISTP", 
"INFP": "ESTJ", 
"INFJ": "ESTP", 
"ESFJ": "INTP", 
"ESTJ": "INFP",  
"ISFJ": "ENTP", 
"ISTJ": "ENFP", 
"ESFP": "INTJ", 
"ESTP": "INFJ",  
"ISFP": "ENTJ", 
"ISTP": "ENFJ"    
}

#최악궁합 
mbti_bad = {
"INTJ": "ESFJ",
"INTP": "ESFP",
"ENTJ": "ISFJ",
"ENTP": "ISFP",
"ENFP": "ISTP",
"ENFJ": "ISTJ",
"INFP": "ESTP",
"INFJ": "ESTJ",
"ESFJ": "INTJ",
"ESTJ": "INFJ",
"ISFJ": "ENTJ",
"ISTJ": "ENFJ",
"ESFP": "INTP",
"ESTP": "INFP",
"ISFP": "ENTP",
"ISTP": "ENFP"    
}

def check():
    global sms_result
    #MBTI를 결정해주기 위한 check(),  결과를 합쳐주고,직업, 최고궁합 최악궁합 설명해줌. 

    ans1 = ""
    ans2 = ""
    ans3 = ""
    ans4 = ""

    if radio_var1.get() == 1: ans1 = "I"
    elif radio_var1.get() == 2: ans1 = "E"
    if radio_var2.get() == 1: ans2 = "T"
    elif radio_var2.get() == 2: ans2 = "F"
    if radio_var3.get() == 1: ans3 = "J"
    elif radio_var3.get() == 2: ans3 = "P"
    if radio_var4.get() == 1: ans4 = "S"
    elif radio_var4.get() == 2: ans4 = "N"

    if radio_var1.get() and radio_var2.get() and radio_var3.get() and radio_var4.get():
        result = ans1+ans4+ans2+ans3
        
        my_type = "["+result + "] " + mbti_type[result]
        my_job = mbti_job[result]
        my_good = mbti_good[result]
        my_bad = mbti_bad[result]

        label_9['text'] = my_type
        label_10['text'] = my_job
        label_11['text'] = my_good
        label_12['text'] = my_bad

        sms_result = name+"님의 MBTI 심리검사 결과입니다.\n\n" \
            "* 타입: "+my_type+"\n" \
            "* 직업: "+my_job+"\n" \
            "* 환상의궁합: "+my_good+"\n" \
            "* 최악의궁합: "+my_ba
 


window = tk.Tk()
window.title("기후변화 MBTI 테스트 ") #기후변화 시작전 이름과 나이 이름입력 
window.geometry("900x550")


answer = messagebox.askyesno("질문","기후변화 MBTI 테스트를 시작하시겠습니까? ")

if answer == True:
    name = simpledialog.askstring("입력", "이름을 입력해주세요.", parent=window)
    age = simpledialog.askstring("입력", "나이를 입력해주세요.", parent=window)
    
  
    

font=tkinter.font.Font(family="맑은 고딕", size=18)
font2=tkinter.font.Font(family="맑은 고딕", size=11)

tk.Label(window, text="기후변화 mbti 테스트 ", fg="red", font=font).pack()

frame1 = tk.Frame(window)
frame1.pack()

label_sinsang = tk.Label(frame1, text=name+"("+age+")", anchor="w", width="60", font=font2, fg="green")
label_0 = tk.Label(frame1, text="※ 각 문항에 대해 예, 아니오로 답해주세요", anchor="w", width="60", font=font2)
label_1 = tk.Label(frame1, text="1.기후변화에 대해 알고, 실천하기 위해 관련 캠페인 혹은 동호회에 가입하는것을 선호하지 않는다.  ", anchor="w", width="75", font=font2)
label_2 = tk.Label(frame1, text="2. 지구온난화의 원인은 선진국의 무자비한 개발 때문이라고 생각한다. ", anchor="w", width="75", font=font2)
label_3 = tk.Label(frame1, text="3.기후변화 박물관을 가기 하루전 날씨에 맞는 옷을 미리 정해둔다.", anchor="w", width="75", font=font2)
label_4 = tk.Label(frame1, text="4. 지구온난화로 지구멸망이 되는 영화를 볼때 당신은 CG 잘 해 놨네 라고 생각한다.", anchor="w", width="75", font=font2)

label_sinsang.grid(row=0, column=0, padx=10, pady=5)
label_0.grid(row=1, column=0, padx=10, pady=5)
label_1.grid(row=2, column=0, padx=10, pady=5)
label_2.grid(row=3, column=0, padx=10, pady=5)
label_3.grid(row=4, column=0, padx=10, pady=5)
label_4.grid(row=5, column=0, padx=10, pady=5)

radio_var1 = tk.IntVar()
radio_var2 = tk.IntVar()
radio_var3 = tk.IntVar()
radio_var4 = tk.IntVar()

radio_1 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var1, command=check, font=font2)
radio_2 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var1, command=check, font=font2)
radio_3 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var2, command=check, font=font2)
radio_4 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var2, command=check, font=font2)
radio_5 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var3, command=check, font=font2)
radio_6 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var3, command=check, font=font2)
radio_7 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var4, command=check, font=font2)
radio_8 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var4, command=check, font=font2)

radio_1.grid(row=2, column=1, padx=10, pady=5)
radio_2.grid(row=2, column=2, padx=10, pady=5)
radio_3.grid(row=3, column=1, padx=10, pady=5)
radio_4.grid(row=3, column=2, padx=10, pady=5)
radio_5.grid(row=4, column=1, padx=10, pady=5)
radio_6.grid(row=4, column=2, padx=10, pady=5)
radio_7.grid(row=5, column=1, padx=10, pady=5)
radio_8.grid(row=5, column=2, padx=10, pady=5)

tk.Label(window, text="").pack()

frame2 = tk.Frame(window)
frame2.pack()

label_blank = tk.Label(frame2, text="")
label_5 = tk.Label(frame2, text="타입", width=10, height=1, anchor="w", font=font2, fg="red")
label_6 = tk.Label(frame2, text="직업", width=10, height=1, anchor="w", font=font2, fg="red")
label_7 = tk.Label(frame2, text="환상의궁합", width=10, height=1, anchor="w", font=font2, fg="red")
label_8 = tk.Label(frame2, text="최악의궁합", width=10, height=1, anchor="w", font=font2, fg="red")
label_9 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_10 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_11 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_12 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)

label_5.grid(row=0, column=0, padx=10, pady=1)
label_6.grid(row=1, column=0, padx=10, pady=1)
label_7.grid(row=2, column=0, padx=10, pady=1)
label_8.grid(row=3, column=0, padx=10, pady=1)
label_9.grid(row=0, column=1, padx=10, pady=1)
label_10.grid(row=1, column=1, padx=10, pady=1)
label_11.grid(row=2, column=1, padx=10, pady=1)
label_12.grid(row=3, column=1, padx=10, pady=1)
label_blank.grid(row=4, column=0, padx=10, pady=1)




window.mainloop()
