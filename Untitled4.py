#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from googletrans import Translator

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")
        self.root.geometry("400x200")

        self.label1 = tk.Label(root, text="Enter text:")
        self.label1.pack()

        self.text_box = tk.Text(root, height=5, width=40)
        self.text_box.pack()

        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack()

        self.label2 = tk.Label(root, text="Translated text:")
        self.label2.pack()

        self.translated_text = tk.Text(root, height=5, width=40, state=tk.DISABLED)
        self.translated_text.pack()

        self.translator = Translator()

    def translate_text(self):
        input_text = self.text_box.get("1.0", tk.END).strip()
        if input_text:
            try:
                translated_result = self.translator.translate(input_text, dest="en")  # Translate to English
                self.translated_text.config(state=tk.NORMAL)
                self.translated_text.delete("1.0", tk.END)
                self.translated_text.insert(tk.END, translated_result.text)
                self.translated_text.config(state=tk.DISABLED)
            except Exception as e:
                self.translated_text.config(state=tk.NORMAL)
                self.translated_text.delete("1.0", tk.END)
                self.translated_text.insert(tk.END, "Translation Error: " + str(e))
                self.translated_text.config(state=tk.DISABLED)
        else:
            self.translated_text.config(state=tk.NORMAL)
            self.translated_text.delete("1.0", tk.END)
            self.translated_text.insert(tk.END, "Please enter some text to translate.")
            self.translated_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()


# In[ ]:





# In[ ]:




