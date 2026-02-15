import tkinter as tk
from tkinter import messagebox, scrolledtext, filedialog
import json
import os
import random

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Manager")
        self.window.geometry("700x630")  # 5% longer (600 * 1.05 = 630)
        self.window.configure(bg='#1E1E1E')
        
        # Questions database file - same folder as script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.questions_file = os.path.join(script_dir, "questions_database.json")
        self.questions = self.load_questions()
        
        # Current question index for testing
        self.current_question_index = 0
        self.test_questions = []
        self.score = 0
        
        # Answer labels
        self.answer_labels = ['A', 'B', 'C', 'D']
        
        # Main menu
        self.show_main_menu()
    
    def load_questions(self):
        """Load questions from JSON file"""
        if os.path.exists(self.questions_file):
            try:
                with open(self.questions_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_questions(self):
        """Save questions to JSON file"""
        with open(self.questions_file, 'w', encoding='utf-8') as f:
            json.dump(self.questions, f, indent=2, ensure_ascii=False)
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.window.winfo_children():
            widget.destroy()
    
    def show_main_menu(self):
        """Display main menu"""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.window,
            text="📚 Quiz Manager",
            font=("Arial", 24, "bold"),
            bg='#1E1E1E',
            fg='#00FF00'
        )
        title.pack(pady=30)
        
        # Show database file path
        tk.Label(
            self.window,
            text=f"Database: {self.questions_file}",
            font=("Arial", 9),
            bg='#1E1E1E',
            fg='#808080'
        ).pack()
        
        # Statistics
        stats = tk.Label(
            self.window,
            text=f"Total Questions in Database: {len(self.questions)}",
            font=("Arial", 12),
            bg='#1E1E1E',
            fg='#4ECDC4'
        )
        stats.pack(pady=10)
        
        # Buttons
        btn_frame = tk.Frame(self.window, bg='#1E1E1E')
        btn_frame.pack(pady=20)
        
        tk.Button(
            btn_frame,
            text="➕ Add New Question",
            font=("Arial", 14, "bold"),
            bg='#4CAF50',
            fg='white',
            width=25,
            height=2,
            command=self.show_add_question
        ).pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="📝 Start Test",
            font=("Arial", 14, "bold"),
            bg='#2196F3',
            fg='white',
            width=25,
            height=2,
            command=self.show_test_mode
        ).pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="📋 View All Questions",
            font=("Arial", 14, "bold"),
            bg='#FF9800',
            fg='white',
            width=25,
            height=2,
            command=self.show_view_questions
        ).pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="📁 Import Questions (JSON)",
            font=("Arial", 14, "bold"),
            bg='#9C27B0',
            fg='white',
            width=25,
            height=2,
            command=self.import_questions
        ).pack(pady=10)
        
        tk.Button(
            btn_frame,
            text="💾 Export Questions (JSON)",
            font=("Arial", 14, "bold"),
            bg='#607D8B',
            fg='white',
            width=25,
            height=2,
            command=self.export_questions
        ).pack(pady=10)
    
    def show_add_question(self):
        """Show add question form"""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.window,
            text="Add New Question",
            font=("Arial", 20, "bold"),
            bg='#1E1E1E',
            fg='#4CAF50'
        )
        title.pack(pady=10)
        
        # Scrollable frame
        canvas = tk.Canvas(self.window, bg='#1E1E1E', highlightthickness=0)
        scrollbar = tk.Scrollbar(self.window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#1E1E1E')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Question input
        tk.Label(
            scrollable_frame,
            text="Question:",
            font=("Arial", 12, "bold"),
            bg='#1E1E1E',
            fg='white'
        ).pack(pady=5)
        
        question_text = tk.Text(scrollable_frame, height=3, width=60, font=("Arial", 11))
        question_text.pack(pady=5)
        
        # Answer options with A, B, C, D labels
        answer_entries = []
        for i in range(4):
            tk.Label(
                scrollable_frame,
                text=f"Answer {self.answer_labels[i]}:",
                font=("Arial", 11, "bold"),
                bg='#1E1E1E',
                fg='white'
            ).pack(pady=5)
            
            entry = tk.Entry(scrollable_frame, width=60, font=("Arial", 11))
            entry.pack(pady=5)
            answer_entries.append(entry)
        
        # Correct answer selection
        tk.Label(
            scrollable_frame,
            text="Correct Answer:",
            font=("Arial", 12, "bold"),
            bg='#1E1E1E',
            fg='#4ECDC4'
        ).pack(pady=5)
        
        correct_var = tk.IntVar(value=0)
        radio_frame = tk.Frame(scrollable_frame, bg='#1E1E1E')
        radio_frame.pack(pady=5)
        
        for i in range(4):
            tk.Radiobutton(
                radio_frame,
                text=self.answer_labels[i],
                variable=correct_var,
                value=i,
                font=("Arial", 11, "bold"),
                bg='#1E1E1E',
                fg='white',
                selectcolor='#2D2D2D'
            ).pack(side=tk.LEFT, padx=10)
        
        # Explanation
        tk.Label(
            scrollable_frame,
            text="Explanation (why correct/incorrect):",
            font=("Arial", 11, "bold"),
            bg='#1E1E1E',
            fg='white'
        ).pack(pady=5)
        
        explanation_text = tk.Text(scrollable_frame, height=4, width=60, font=("Arial", 10))
        explanation_text.pack(pady=5)
        
        # Buttons
        btn_frame = tk.Frame(scrollable_frame, bg='#1E1E1E')
        btn_frame.pack(pady=20)
        
        def save_question():
            question = question_text.get("1.0", tk.END).strip()
            answers = [entry.get().strip() for entry in answer_entries]
            correct = correct_var.get()
            explanation = explanation_text.get("1.0", tk.END).strip()
            
            # Validation
            if not question:
                messagebox.showerror("Error", "Please enter a question!")
                return
            
            if not all(answers):
                messagebox.showerror("Error", "Please fill all 4 answers!")
                return
            
            if not explanation:
                messagebox.showerror("Error", "Please provide an explanation!")
                return
            
            # Create question object
            new_question = {
                "question": question,
                "answers": answers,
                "correct": correct,
                "explanation": explanation
            }
            
            # Add to database
            self.questions.append(new_question)
            self.save_questions()
            
            messagebox.showinfo("Success", "Question added successfully!")
            self.show_main_menu()
        
        tk.Button(
            btn_frame,
            text="💾 Save Question",
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            width=20,
            command=save_question
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame,
            text="🔙 Back to Menu",
            font=("Arial", 12),
            bg='#607D8B',
            fg='white',
            width=20,
            command=self.show_main_menu
        ).pack(side=tk.LEFT, padx=10)
        
        canvas.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
    
    def show_view_questions(self):
        """Show all questions"""
        self.clear_window()
        
        # Title
        title = tk.Label(
            self.window,
            text=f"All Questions ({len(self.questions)} total)",
            font=("Arial", 18, "bold"),
            bg='#1E1E1E',
            fg='#FF9800'
        )
        title.pack(pady=10)
        
        # Scrolled text to display questions
        text_area = scrolledtext.ScrolledText(
            self.window,
            width=80,
            height=25,
            font=("Consolas", 10),
            bg='#2D2D2D',
            fg='white'
        )
        text_area.pack(pady=10, padx=10)
        
        # Display all questions
        for i, q in enumerate(self.questions, 1):
            text_area.insert(tk.END, f"\n{'='*70}\n")
            text_area.insert(tk.END, f"Question {i}:\n")
            text_area.insert(tk.END, f"{q['question']}\n\n")
            
            for j, answer in enumerate(q['answers']):
                prefix = "✓ " if j == q['correct'] else "  "
                text_area.insert(tk.END, f"{prefix}{self.answer_labels[j]}. {answer}\n")
            
            text_area.insert(tk.END, f"\nExplanation: {q['explanation']}\n")
        
        text_area.config(state=tk.DISABLED)
        
        # Back button
        tk.Button(
            self.window,
            text="🔙 Back to Menu",
            font=("Arial", 12),
            bg='#607D8B',
            fg='white',
            width=20,
            command=self.show_main_menu
        ).pack(pady=10)
    
    def show_test_mode(self):
        """Start test mode"""
        if not self.questions:
            messagebox.showwarning("No Questions", "Please add questions first!")
            return
        
        # Shuffle questions for test
        self.test_questions = self.questions.copy()
        random.shuffle(self.test_questions)
        self.current_question_index = 0
        self.score = 0
        
        self.show_question()
    
    def show_question(self):
        """Display current question"""
        self.clear_window()
        
        if self.current_question_index >= len(self.test_questions):
            self.show_results()
            return
        
        question = self.test_questions[self.current_question_index]
        
        # Progress
        progress = tk.Label(
            self.window,
            text=f"Question {self.current_question_index + 1} of {len(self.test_questions)}",
            font=("Arial", 12),
            bg='#1E1E1E',
            fg='#4ECDC4'
        )
        progress.pack(pady=10)
        
        # Question text
        q_frame = tk.Frame(self.window, bg='#2D2D2D', relief=tk.RAISED, bd=2)
        q_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            q_frame,
            text=question['question'],
            font=("Arial", 14, "bold"),
            bg='#2D2D2D',
            fg='white',
            wraplength=600,
            justify=tk.LEFT
        ).pack(pady=20, padx=20)
        
        # Answer options with A, B, C, D
        selected_answer = tk.IntVar(value=-1)
        
        for i, answer in enumerate(question['answers']):
            tk.Radiobutton(
                self.window,
                text=f"{self.answer_labels[i]}. {answer}",
                variable=selected_answer,
                value=i,
                font=("Arial", 12),
                bg='#1E1E1E',
                fg='white',
                selectcolor='#2D2D2D',
                wraplength=600,
                justify=tk.LEFT
            ).pack(anchor=tk.W, padx=40, pady=5)
        
        # Submit button
        def submit_answer():
            if selected_answer.get() == -1:
                messagebox.showwarning("No Answer", "Please select an answer!")
                return
            
            self.check_answer(selected_answer.get(), question)
        
        tk.Button(
            self.window,
            text="✓ Submit Answer",
            font=("Arial", 14, "bold"),
            bg='#4CAF50',
            fg='white',
            width=20,
            command=submit_answer
        ).pack(pady=20)
        
        # Back button
        tk.Button(
            self.window,
            text="🔙 Back to Menu",
            font=("Arial", 11),
            bg='#607D8B',
            fg='white',
            width=20,
            command=self.show_main_menu
        ).pack(pady=5)
    
    def check_answer(self, selected, question):
        """Check if answer is correct and show explanation"""
        self.clear_window()
        
        is_correct = (selected == question['correct'])
        if is_correct:
            self.score += 1
        
        # Result title
        result_color = '#4CAF50' if is_correct else '#F44336'
        result_text = "✓ Correct!" if is_correct else "✗ Incorrect"
        
        tk.Label(
            self.window,
            text=result_text,
            font=("Arial", 24, "bold"),
            bg='#1E1E1E',
            fg=result_color
        ).pack(pady=20)
        
        # Show question
        tk.Label(
            self.window,
            text="Question:",
            font=("Arial", 12, "bold"),
            bg='#1E1E1E',
            fg='white'
        ).pack(pady=5)
        
        tk.Label(
            self.window,
            text=question['question'],
            font=("Arial", 11),
            bg='#1E1E1E',
            fg='#E0E0E0',
            wraplength=600
        ).pack(pady=5)
        
        # Show selected vs correct with A, B, C, D
        tk.Label(
            self.window,
            text=f"Your answer: {self.answer_labels[selected]}. {question['answers'][selected]}",
            font=("Arial", 11),
            bg='#1E1E1E',
            fg='#FF9800'
        ).pack(pady=5)
        
        if not is_correct:
            tk.Label(
                self.window,
                text=f"Correct answer: {self.answer_labels[question['correct']]}. {question['answers'][question['correct']]}",
                font=("Arial", 11, "bold"),
                bg='#1E1E1E',
                fg='#4CAF50'
            ).pack(pady=5)
        
        # Explanation
        exp_frame = tk.Frame(self.window, bg='#2D2D2D', relief=tk.RAISED, bd=2)
        exp_frame.pack(fill=tk.BOTH, padx=20, pady=10, expand=True)
        
        tk.Label(
            exp_frame,
            text="Explanation:",
            font=("Arial", 12, "bold"),
            bg='#2D2D2D',
            fg='#4ECDC4'
        ).pack(pady=5)
        
        tk.Label(
            exp_frame,
            text=question['explanation'],
            font=("Arial", 11),
            bg='#2D2D2D',
            fg='white',
            wraplength=600,
            justify=tk.LEFT
        ).pack(pady=10, padx=20)
        
        # Next button
        def next_question():
            self.current_question_index += 1
            self.show_question()
        
        tk.Button(
            self.window,
            text="→ Next Question",
            font=("Arial", 14, "bold"),
            bg='#2196F3',
            fg='white',
            width=20,
            command=next_question
        ).pack(pady=20)
    
    def show_results(self):
        """Show final test results"""
        self.clear_window()
        
        percentage = (self.score / len(self.test_questions)) * 100
        
        # Title
        tk.Label(
            self.window,
            text="🎯 Test Complete!",
            font=("Arial", 24, "bold"),
            bg='#1E1E1E',
            fg='#00FF00'
        ).pack(pady=30)
        
        # Score
        tk.Label(
            self.window,
            text=f"Your Score: {self.score} / {len(self.test_questions)}",
            font=("Arial", 20, "bold"),
            bg='#1E1E1E',
            fg='#4ECDC4'
        ).pack(pady=10)
        
        tk.Label(
            self.window,
            text=f"Percentage: {percentage:.1f}%",
            font=("Arial", 18),
            bg='#1E1E1E',
            fg='#FF9800'
        ).pack(pady=10)
        
        # Grade
        if percentage >= 90:
            grade = "Excellent! 🌟"
            color = '#4CAF50'
        elif percentage >= 70:
            grade = "Good! 👍"
            color = '#2196F3'
        elif percentage >= 50:
            grade = "Pass ✓"
            color = '#FF9800'
        else:
            grade = "Need more practice 📚"
            color = '#F44336'
        
        tk.Label(
            self.window,
            text=grade,
            font=("Arial", 20, "bold"),
            bg='#1E1E1E',
            fg=color
        ).pack(pady=20)
        
        # Buttons
        btn_frame = tk.Frame(self.window, bg='#1E1E1E')
        btn_frame.pack(pady=30)
        
        tk.Button(
            btn_frame,
            text="🔄 Take Test Again",
            font=("Arial", 12, "bold"),
            bg='#2196F3',
            fg='white',
            width=20,
            command=self.show_test_mode
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            btn_frame,
            text="🏠 Back to Menu",
            font=("Arial", 12, "bold"),
            bg='#607D8B',
            fg='white',
            width=20,
            command=self.show_main_menu
        ).pack(side=tk.LEFT, padx=10)
    
    def import_questions(self):
        """Import questions from JSON file"""
        file_path = filedialog.askopenfilename(
            title="Select JSON file",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_questions = json.load(f)
            
            # Validate format
            if not isinstance(new_questions, list):
                messagebox.showerror("Error", "Invalid JSON format! Must be a list of questions.")
                return
            
            # Add to existing questions
            count = len(new_questions)
            self.questions.extend(new_questions)
            self.save_questions()
            
            messagebox.showinfo("Success", f"Imported {count} questions!\nTotal: {len(self.questions)}")
            self.show_main_menu()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import:\n{str(e)}")
    
    def export_questions(self):
        """Export questions to JSON file"""
        if not self.questions:
            messagebox.showwarning("No Questions", "No questions to export!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Save questions as",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(self.questions, f, indent=2, ensure_ascii=False)
            
            messagebox.showinfo("Success", f"Exported {len(self.questions)} questions!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export:\n{str(e)}")
    
    def run(self):
        self.window.mainloop()

# Launch
if __name__ == "__main__":
    QuizApp().run()
