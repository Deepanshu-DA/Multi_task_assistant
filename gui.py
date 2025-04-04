import tkinter as tk
from tkinter import scrolledtext
from command_parser import CommandParser
from services.speech import listen, speak  # import the speak function
import threading
import sys
import io

class AssistantGUI:
    def __init__(self, root):
        self.parser = CommandParser()
        self.root = root
        self.root.title("My Assistant")
        self.root.geometry("500x500")

        self.text_output = scrolledtext.ScrolledText(root, height=15, wrap=tk.WORD)
        self.text_output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(root)
        self.entry.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.entry.bind("<Return>", self.handle_input)

        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Run", command=self.run_command).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="🎙️ Voice", command=self.run_voice_command).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Task Status", command=self.show_tasks).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear Finished", command=self.clear_tasks).pack(side=tk.LEFT, padx=5)

    def log(self, text):
        self.text_output.insert(tk.END, f"{text}\n")
        self.text_output.see(tk.END)

    def run_command(self):
        command = self.entry.get()
        self.log(f"> {command}")
        threading.Thread(target=self.run_and_capture, args=(command,)).start()
        self.entry.delete(0, tk.END)

    def handle_input(self, event):
        self.run_command()

    def run_voice_command(self):
        self.log("🎙️ Listening...")
        def listen_and_run():
            voice_input = listen()
            if voice_input:
                self.log(f"> {voice_input}")
                self.run_and_capture(voice_input)
            else:
                self.log("❌ Could not understand audio.")

        threading.Thread(target=listen_and_run).start()

    def run_and_capture(self, command):
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        self.parser.handle_command(command)
        sys.stdout = old_stdout
        output = redirected_output.getvalue().strip()
        if output:
            self.log(output)

    def show_tasks(self):
        status = self.parser.get_task_status()
        if not status:
            self.log("No active tasks.")
        else:
            for i, name, alive in status:
                self.log(f"Task {i}: {'Running' if alive else 'Stopped'}")

    def clear_tasks(self):
        self.parser.clear_finished_tasks()
        self.log("Finished tasks cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = AssistantGUI(root)
    root.mainloop()
