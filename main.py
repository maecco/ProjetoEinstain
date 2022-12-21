import tkinter as tk
import source.app as app

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Corretor de Provas")
    root.geometry("500x280")
    root.resizable(False, False)
    application = app.App(root)
    application.mainloop()
