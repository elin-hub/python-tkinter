from tkinter import *
from tkinter import messagebox
import datetime
import random
import tkinter.messagebox as msbox
import tkinter as tk
from tkcalendar import DateEntry
date = datetime.date.today()
from tkinter import simpledialog

# tkinter 객체
window = Tk()
window.geometry('350x300+500+200')
window.title('Login')

# 사용자 id와 password를 저장하는 변수 
user_id, password = StringVar(), StringVar()

questions = [
    "어떤 음식을 좋아하시나요?",
    "가장 좋아하는 색깔은 무엇인가요?",
    "오늘 하루 어떤 일이 있었나요?",
    "좋아하는 여행지가 어디인가요?",
    "가장 기억에 남는 책은 무엇인가요?",
    "어떤 음식을 좋아하시나요?",
    "가장 좋아하는 색깔은 무엇인가요?",
    "오늘 하루 어떤 일이 있었나요?",
    "좋아하는 여행지가 어디인가요?",
    "가장 기억에 남는 책은 무엇인가요?",
    "가장 좋아하는 계절은 무엇인가요?",
    "어릴 적 어떤 꿈을 가지고 있었나요?",
    "가장 인상깊게 본 영화는 무엇인가요?",
    "오늘 하루 무엇을 배웠나요?",
    "최근에 들은 좋아하는 노래가 있나요?",
    "자주 가는 카페나 음식점이 있나요? 어떤 곳인가요?",
    "가장 좋아하는 동물은 무엇인가요?",
    "만약 시간을 멈출 수 있다면 어떤 일을 하고 싶나요?",
    "자신의 장점과 단점은 무엇인가요?",
    "아침에 일어나서 가장 먼저 하는 일은 무엇인가요?",
    "가장 행복한 순간은 언제였나요?",
    "꿈에서 제일 자주 나오는 상황이나 사물은 무엇인가요?",
    "만약 하루 동안 다른 사람이 되어볼 수 있다면 누구가 되고 싶나요?",
    "새로운 기술이나 능력을 배울 수 있다면 무엇을 배우고 싶나요?",
    "언어 하나를 순식간에 배울 수 있다면 어떤 언어를 선택하고 싶나요?",
    "가장 힘들었던 결정은 무엇이었나요?",
    "자신을 한 마디로 소개해보세요.",
    "현재까지의 인생 중 가장 자랑스러운 순간은 언제였나요?",
    "새로운 능력을 얻을 수 있다면 어떤 능력을 얻고 싶나요?",
    "지금까지 한 일 중 후회하는 일이 있나요?",
    "좋아하는 스포츠나 운동이 있나요?",
    "자신을 어떤 유명인과 비교해본다면 누구와 비슷하다고 생각하시나요?",
    "마지막으로 가장 크게 웃은 적은 언제였나요?",
    "무엇을 하면 시간 가는 줄 모르겠나요?",
    "가장 인상깊게 본 예술 작품이나 전시회는 무엇인가요?",
    "만약 하루 동안 무엇이든지 할 수 있다면 어떤 일을 하고 싶나요?",
    "현재의 삶에서 바꾸고 싶은 점이 있다면 무엇인가요?",
    "좋아하는 명언이나 격언이 있나요?",
    "가장 추억에 남는 여행 경험은 어디인가요?",
    "가장 소중한 가치나 원칙은 무엇인가요?",
    "자신이 가장 끌리는 장소나 풍경은 어떤 곳인가요?",
    "언제, 어디서 가장 편안하고 안전하게 느껴지나요?",
    "새로운 취미나 활동을 시도해 본 적이 있나요?",
    "좋아하는 유머 스타일이나 웃긴 상황이 있나요?",
    "매일 반복해서 먹을 수 있는 음식이 있다면 무엇인가요?",
    "자신이 성공적인 사람으로 인정받는 기준은 무엇인가요?",
    "다른 사람들에게 어떤 영향을 주고 싶나요?",
    "언제 자주 생각나는 동화나 이야기가 있나요?",
    "가장 좋아하는 시간대는 언제인가요? 아침, 낮, 저녁, 밤?",
    "다른 사람들과 함께 시간을 보낼 때 가장 행복한 순간은 언제였나요?",
    "가장 힐링되는 활동이나 장소는 어디인가요?",
    "좋아하는 계절마다 하는 특별한 활동이 있나요?",
    "자신의 목표나 꿈을 이루기 위해 어떤 노력을 하고 있나요?",
    "자신이 무엇을 좋아하는지, 무엇을 싫어하는지 정확히 알고 있나요?",
    "가장 힘들 때 도움을 받는 사람이나 방법은 무엇인가요?",
    "좋아하는 냄새나 향기가 있나요?"
    # 추가적인 질문들을 여기에 계속 추가할 수 있습니다.
]
















# 사용자 id와 password를 비교하는 def
def check_data():
    if user_id.get() == "배도연" and password.get() == "qoehdusqkqh":
        # 새로운 화면 생성
        ws = Tk()
        ws.geometry('400x450+500+200')
        ws.title('TODOLIST')
        ws.config(bg='#dcdcdc')
        ws.resizable(width=False, height=False)

        date = datetime.date.today()


        def newTask():
            task = my_entry.get()
            if task != "":
                lb.insert(END, task)
                my_entry.delete(0, "end")
            else:
                messagebox.showwarning("주의", "할 일을 입력하세요.")



        def deleteTask():
            lb.delete(ANCHOR)

        def create():
            win = Toplevel(ws)
            win.title("Memo")
            win.geometry("400x300")
            title_frame = Frame(win)
            title_frame.pack()
            filename = str(date) + '.txt'

            date_text = Label(title_frame, text = date)
            date_text.pack()

            file_frame = Frame(win)
            file_frame.pack(padx=5,pady=5)

            txt = Text(file_frame, width=30, heigh=3)
            txt.pack(side="left", expand=True)
            txt.insert(END, "내용을 입력하세요")

    
            def saveFile():
                file = open(filename, "w")
                ts = str(list_file.get(0, END))
                file.write(ts)
                file.close
                msbox.showinfo("알림", "정상적으로 저장되었습니다.")

    
            button_save = Button(title_frame, padx=5, pady=5, width=12, text="저장", command=saveFile)
            button_save.pack(fill="both")

            def addList():
                index = txt.get("1.0", END)
                if index == '':
                    return
                list_file.insert(END, txt.get("1.0", END))
                txt.delete("1.0", END)


            def deleteList():
                index = list_file.curselection()
                list_file.delete(index)

            list_frame = Frame(win)
            list_frame.pack(fill="both", padx=5, pady=5)

            scrollbar = Scrollbar(list_frame)
            scrollbar.pack(side = "right", fill="y")
    
            list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
            list_file.pack(side="left", fill="both", expand=True)
            scrollbar.config(command=list_file.yview)

            button_add = Button(file_frame, padx=5, pady=5, width=12, text="추가", command=addList)
            button_add.pack(side="left")

            button_del = Button(file_frame, padx=5, pady=5, width=12, text="삭제", command=deleteList)
            button_del.pack(side="left")

        def calendar():
            win = Toplevel(ws)
            win.title("calendar")
            win.geometry("200x200")
            
            f1=Frame(win,width=500,height=50,relief=SUNKEN,bd=4,bg='light steel blue')
            f1.pack(side=TOP)
            f2=Frame(win,width=500,height=50,relief=SUNKEN,bd=4,bg='white')
            f2.pack()
            f3=Frame(win,width=160,height=100,relief=SUNKEN,bd=4,bg='white')
            f3.pack(side=BOTTOM)


       
            l4=Label(f2,text='DATE',font=('tahoma',20,'bold'),fg='black',anchor='w')
            l4.grid(row=0,column=3)

            cal=DateEntry(f2,dateformat=3,width=12, background='darkblue',
                    foreground='white', borderwidth=4,Calendar =2023)
            cal.grid(row=1,column=3,sticky='nsew')

            

        def question():
            
            random_question = random.choice(questions)
            user_answer = simpledialog.askstring("질문", random_question)
            if user_answer:
                answer_label.config(text=f"당신의 대답: {user_answer}")
            else:
                answer_label.config(text="응답이 없습니다.")




        frame = Frame(ws)
        frame.pack(pady=10)

        lb = Listbox(
            frame,
            width=35,
            height=13,
            font=('consolas', 12),
            bd=0,
            fg='#464646',
            highlightthickness=0,
            selectbackground='#a6a6a6',
            activestyle="none",
    
            )
        lb.pack(side=LEFT, fill=BOTH)

        task_list = [
            '9시반에는 기상하기.',
            '운동은 30분이상! 건강을 위해!',
            '아침 꼭꼭 먹기!!',
            ]

        for item in task_list:
            lb.insert(END, item)

        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=BOTH)

        lb.config(yscrollcommand=sb.set)
        sb.config(command=lb.yview)

        my_entry = Entry(
            ws,
            font=('consolas', 15)
            )

        my_entry.pack(pady=30)

        button_frame = Frame(ws)
        button_frame.pack(pady=20)

        addTask_btn = Button(
            button_frame,
            text='Add Task',
            font=('bold 12'),
            bg='#ffe4e1',
            padx=10,
            pady=8,
            command=newTask
    

        )
        addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
    

        delTask_btn = Button(
            button_frame,
            text='Delete Task',
            font=('bold 12'),
            bg='#e0ffff',
            padx=10,
            pady=8,
            command=deleteTask
        )
        delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
    

        btn = Button(ws, text='memo', width=5,
                 height=1, bd='2', command = create)
        btn.place(x=33, y=280)


        btn = Button(ws, text='calender', width=7,
                 height=1, bd='2', command = calendar)
        btn.place(x=310, y=280) 



        btn = Button(ws, text='Question', width=7,
                 height=1, bd='2', command = question)
        btn.place(x=90, y=280) 

        answer_label = tk.Label(ws, text="", wraplength=300)
        answer_label.pack()


      


        ws.mainloop()


       
    else:  
            print("Check your Username/Password")
        

# id와 password, 그리고 확인 버튼의 UI를 만드는 부분
tk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 20, pady = 10)
tk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Label(window, text = " 로그인을 한 후 할 일과").grid(row = 3, column = 1, padx = 10, pady = 10)
tk.Label(window, text = " 메모를 관리해보세요:)").grid(row = 4, column = 1, padx = 10, pady = 10)
tk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Entry(window, textvariable = password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
tk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)


window.mainloop()
