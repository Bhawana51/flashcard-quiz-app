import tkinter as tk
from tkinter import messagebox, simpledialog

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        self.flashcards = []
        self.index = 0

        self.front_label = tk.Label(root, text="", font=('Arial', 18), width=40, height=5)
        self.front_label.pack(pady=20)

        self.show_btn = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_btn.pack()

        nav_frame = tk.Frame(root)
        nav_frame.pack(pady=10)
        tk.Button(nav_frame, text="Previous", command=self.prev_card).pack(side="left", padx=10)
        tk.Button(nav_frame, text="Next", command=self.next_card).pack(side="right", padx=10)

        edit_frame = tk.Frame(root)
        edit_frame.pack(pady=10)
        tk.Button(edit_frame, text="Add", command=self.add_card).pack(side="left", padx=5)
        tk.Button(edit_frame, text="Edit", command=self.edit_card).pack(side="left", padx=5)
        tk.Button(edit_frame, text="Delete", command=self.delete_card).pack(side="left", padx=5)

        self.update_display()

    def update_display(self):
        if self.flashcards:
            self.front_label.config(text=self.flashcards[self.index]["question"])
        else:
            self.front_label.config(text="No flashcards. Add one!")

    def show_answer(self):
        if self.flashcards:
            answer = self.flashcards[self.index]["answer"]
            messagebox.showinfo("Answer", answer)

    def prev_card(self):
        if self.flashcards:
            self.index = (self.index - 1) % len(self.flashcards)
            self.update_display()

    def next_card(self):
        if self.flashcards:
            self.index = (self.index + 1) % len(self.flashcards)
            self.update_display()

    def add_card(self):
        q = simpledialog.askstring("Question", "Enter the question:")
        a = simpledialog.askstring("Answer", "Enter the answer:")
        if q and a:
            self.flashcards.append({"question": q, "answer": a})
            self.index = len(self.flashcards) - 1
            self.update_display()

    def edit_card(self):
        if self.flashcards:
            q = simpledialog.askstring("Edit Question", "New question:", initialvalue=self.flashcards[self.index]["question"])
            a = simpledialog.askstring("Edit Answer", "New answer:", initialvalue=self.flashcards[self.index]["answer"])
            if q and a:
                self.flashcards[self.index] = {"question": q, "answer": a}
                self.update_display()

    def delete_card(self):
        if self.flashcards:
            del self.flashcards[self.index]
            self.index = max(0, self.index - 1)
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
