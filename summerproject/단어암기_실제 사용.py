import tkinter as tk
import random

class VocabularyQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("단어 암기 및 퀴즈")

        self.word_label = tk.Label(root, text="단어:") # 첫 인터페이스를 결정해주는 selfbutton 구성 
        self.word_label.pack()
        self.word_entry = tk.Entry(root)
        self.word_entry.pack()

        self.definition_label = tk.Label(root, text="정의:")
        self.definition_label.pack()
        self.definition_entry = tk.Entry(root)
        self.definition_entry.pack()

        self.add_button = tk.Button(root, text="추가", command=self.add_word)
        self.add_button.pack()

        self.start_quiz_button = tk.Button(root, text="퀴즈 시작", command=self.start_quiz)
        self.start_quiz_button.pack()

        self.edit_button = tk.Button(root, text="수정", command=self.edit_word)
        self.edit_button.pack()
        self.edit_button.config(state=tk.DISABLED)

        self.delete_button = tk.Button(root, text="삭제", command=self.delete_word)
        self.delete_button.pack()
        self.delete_button.config(state=tk.DISABLED)

        self.words_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.words_listbox.pack()
        self.words_listbox.bind("<<ListboxSelect>>", self.selection_changed)

        self.words = []

    def add_word(self):
        word = self.word_entry.get()  # selfword 리스트안에 단어를 추가 할수 있도록 하였음 ++
        definition = self.definition_entry.get()

        if word and definition:
            self.words.append({"word": word, "definition": definition})
            self.words_listbox.insert(tk.END, f"{word}: {definition}")
            self.word_entry.delete(0, tk.END)
            self.definition_entry.delete(0, tk.END)

    def start_quiz(self):
        if self.words:
            self.quiz_word() # 리스트 안에 있는 단어들로 퀴즈 시작 
        else:
            self.show_message("퀴즈를 위한 단어가 없습니다.")

    def quiz_word(self):
        quiz_word = random.choice(self.words)
        self.quiz_window(quiz_word)

    def quiz_window(self, quiz_word):
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("단어 퀴즈")

        self.quiz_label = tk.Label(quiz_window, text=f"정의: {quiz_word['definition']}", font=("Helvetica", 12))
        self.quiz_label.pack()

        self.answer_entry = tk.Entry(quiz_window)
        self.answer_entry.pack()

        self.check_button = tk.Button(quiz_window, text="정답 확인", command=lambda: self.check_answer(quiz_window, quiz_word))
        self.check_button.pack()

    def check_answer(self, quiz_window, quiz_word):
        user_answer = self.answer_entry.get()
        correct_answer = quiz_word["word"]
        if user_answer.lower() == correct_answer.lower():
            self.show_message("정답입니다! 계속해서 퀴즈를 풀어보세요.")
            quiz_window.destroy()
            self.quiz_word()  # 새 퀴즈 시작하깅
        else:
            self.show_message("틀렸습니다. 다시 시도하세요.")
            self.quiz_window(quiz_word)  # 다시 퀴즈 내깅 ><

    def edit_word(self):
        selected_index = self.words_listbox.curselection()  #단어를 편집 가능한.다 선택이 가능
        if selected_index:
            selected_index = selected_index[0]
            selected_word = self.words[selected_index]
            new_word = self.word_entry.get()
            new_definition = self.definition_entry.get()
            selected_word["word"] = new_word
            selected_word["definition"] = new_definition
            self.words_listbox.delete(selected_index)
            self.words_listbox.insert(selected_index, f"{new_word}: {new_definition}")
            self.clear_inputs()

    def delete_word(self):
        selected_index = self.words_listbox.curselection() #단어 선택 후 삭제가 가능한 함수 
        if selected_index:
            selected_index = selected_index[0]
            self.words.pop(selected_index)
            self.words_listbox.delete(selected_index)
            self.clear_inputs()

    def selection_changed(self, event):
        selected_index = self.words_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_word = self.words[selected_index]
            self.word_entry.delete(0, tk.END)
            self.definition_entry.delete(0, tk.END)
            self.word_entry.insert(0, selected_word["단어 "])
            self.definition_entry.insert(0, selected_word["뜻"])
            self.edit_button.config(state=tk.NORMAL)
            self.delete_button.config(state=tk.NORMAL)

    def clear_inputs(self):
        self.word_entry.delete(0, tk.END)
        self.definition_entry.delete(0, tk.END)
        self.edit_button.config(state=tk.DISABLED)
        self.delete_button.config(state=tk.DISABLED)

    def show_message(self, message):
        message_window = tk.Toplevel(self.root)
        message_window.title("알림")
        tk.Label(message_window, text=message, font=("Helvetica", 12)).pack()

# 메인 윈도우 생성하기 >< 
root = tk.Tk()
app = VocabularyQuizApp(root)

# 메인 루프 시작 ><
root.mainloop()
        
