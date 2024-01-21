import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

#공부시간 체크 가능한 클래스 
class StudyTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("과목별 공부시간 Tracker")

        self.subjects = ["독서", "영어", "수학", "물리", "화학","중국어","정보","정보과학"]  # 과목 리스트 설정
        self.study_times = {subject: timedelta(seconds=0) for subject in self.subjects}

        self.subject_var = tk.StringVar(value=self.subjects[0])
        self.time_var = tk.StringVar()

        self.subject_label = tk.Label(root, text="과목:")
        self.subject_label.pack()

        self.subject_menu = tk.OptionMenu(root, self.subject_var, *self.subjects)
        self.subject_menu.pack()

        self.time_label = tk.Label(root, text="공부 시간:")
        self.time_label.pack()

        self.time_entry = tk.Entry(root, textvariable=self.time_var)
        self.time_entry.pack()

        self.manual_record_button = tk.Button(root, text="수동 기록", command=self.manual_record_study_time)
        self.manual_record_button.pack()

        self.auto_record_button = tk.Button(root, text="자동 기록", command=self.start_auto_record)
        self.auto_record_button.pack()

        self.stop_auto_record_button = tk.Button(root, text="자동 기록 중지", command=self.stop_auto_record)
        self.stop_auto_record_button.pack()
        self.stop_auto_record_button.configure(state=tk.DISABLED)  # 초기에는 비활성화 상태로 시작한다. 

        self.view_button = tk.Button(root, text="기록 보기", command=self.view_study_times)
        self.view_button.pack()

        self.auto_recording = False

    def manual_record_study_time(self):
        subject = self.subject_var.get()
        time_str = self.time_var.get()

        try:
            hours, minutes, seconds = map(int, time_str.split(':')) #시간을 쪼개서 한번에 입력받기 
            time_delta = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            
            if time_delta.total_seconds() > 0:
                self.study_times[subject] += time_delta
                messagebox.showinfo("알림", f"{subject} 과목 {time_str} 시간이 기록되었습니다.")
                self.time_var.set('')
            else:
                messagebox.showwarning("경고", "0보다 큰 시간을 입력해주세요.")
        except ValueError:
            messagebox.showwarning("경고", "올바른 시간 형식을 입력해주세요. (HH:MM:SS)")

    def start_auto_record(self):
        self.auto_recording = True
        self.auto_record_button.configure(state=tk.DISABLED)
        self.stop_auto_record_button.configure(state=tk.NORMAL) #자동기록 시작하기 
        self.auto_record_loop()

    def stop_auto_record(self):
        self.auto_recording = False
        self.auto_record_button.configure(state=tk.NORMAL)
        self.stop_auto_record_button.configure(state=tk.DISABLED) # 멈추기 

    def auto_record_loop(self):
        if self.auto_recording:
            subject = self.subject_var.get()
            current_time = datetime.now().time()
            time_delta = timedelta(seconds=1)
            self.study_times[subject] += time_delta # 과목 마다 1초씩 더해서 기록 화면에 나타내기 
            self.root.after(1000, self.auto_record_loop)  # 1초마다 반복
        else:
            self.stop_auto_record()

    def view_study_times(self):
        result = "과목별 공부시간\n"
        for subject, time in self.study_times.items():
            hours, remainder = divmod(time.total_seconds(), 3600)  #몫과 나머지 구하기 시간을 1초로 세 놓은 상태로 쪼개서 시 분 초로 나타내기 
            minutes, seconds = divmod(remainder, 60)
            result += f"{subject}: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}\n"
        
        messagebox.showinfo("기록 보기", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudyTracker(root)
    root.mainloop()
