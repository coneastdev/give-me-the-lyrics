import customtkinter as ctk
import requests
from customtkinter import filedialog
from app import getLyrics

def checkEntry(self):
    if self.userInputEntry.get().strip():
        self.userSearchButton.configure(state="normal")
    else:
        self.userSearchButton.configure(state="disabled")

def setOutput(self, text):
    self.outputTextbox.configure(state="normal")
    self.outputTextbox.delete("1.0", "end")
    self.outputTextbox.insert("1.0", text)
    self.outputTextbox.configure(state="disabled")
    self.saveButton.configure(state="normal")

def callAppFunc(self):
    query = self.userInputEntry.get().strip()
    self.userSearchButton.configure(state="disabled")
    try:
        source = {"Genius": "genius", "LyricAdvisor": "lyricadvisor"}.get(self.sourceVar.get(), "genius")
        lyrics = getLyrics(query, source)
        self.setOutput(lyrics)
    except Exception as error:
        self.setOutput(f"Error: {error}")

def saveToFile(self):
    filePath = filedialog.asksaveasfilename(
        title="Save Lyrics As...",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not filePath:
        return

    text = self.outputTextbox.get("1.0", "end-1c")
    try:
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as error:
        self.setOutput(f"Error saving file: {error}")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("Give Me The Lyrics")

        ctk.set_appearance_mode("dark")

        self.userInputLabel = ctk.CTkLabel(self, text="Enter song query:")
        self.userInputEntry = ctk.CTkEntry(self)
        self.userSearchButton = ctk.CTkButton(self, text="Search", state="disabled", command=self.callAppFunc)

        self.sourceVar = ctk.StringVar(value="Genius")
        self.userSourceOptionMenu = ctk.CTkOptionMenu(self, variable=self.sourceVar, values=["Genius", "LyricAdvisor"])

        self.outputTextbox = ctk.CTkTextbox(self, state="disabled", wrap="word")
        self.saveButton = ctk.CTkButton(self, text="Save Lyrics", state="disabled", command=self.saveToFile)

        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.userInputEntry.bind("<KeyRelease>", lambda e: self.checkEntry())

        self.userInputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.userInputEntry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.userSourceOptionMenu.grid(row=0, column=2, padx=6, pady=6, sticky="ew")
        self.userSearchButton.grid(row=0, column=3, padx=5, pady=5)

        self.saveButton.grid(row=1, column=0, columnspan=4, padx=5, pady=(0, 5), sticky="ew")
        self.outputTextbox.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    checkEntry = checkEntry
    setOutput = setOutput
    callAppFunc = callAppFunc
    saveToFile = saveToFile

if __name__ == '__main__':
    app = App()
    app.mainloop()
