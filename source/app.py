import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
from os import path


import source.filesystem as filesystem
import source.statistics as statistics

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.PATH_GABARITO = None
        self.PATH_RESPOSTAS = None
        self.PATH_SAVE = None


        self.ModuloEstatistica = None
        

        self.fb_frame = Filebrowser(self).pack(fill='x', expand=True)
        self.pack(expand=True, fill="x", anchor='n')

        btn = ttk.Button(self, text="Gerar relatorio", command=self.__gerar_relatorio )
        btn.pack(ipadx=20, ipady=15, pady=5, expand=True, fill="both")


    def __gerar_relatorio(self):
        

        if      self.PATH_GABARITO  \
            and self.PATH_RESPOSTAS \
            and self.PATH_SAVE:

            try:
                gabarito_formatado = filesystem.load_gabarito(self.PATH_GABARITO)
            except Exception as e:
                messagebox.showerror("Erro ao abrir arquivo", "Arquivo de gabarito mal formatado")
                return
            
            try:
                respostas_formatadas = filesystem.load_respostas(self.PATH_RESPOSTAS)
            except Exception as e:
                messagebox.showerror("Erro ao abrir arquivo", "Arquivo de respostas mal formatado")
                return


            self.ModuloEstatistica = statistics.Statistics(gabarito_formatado, respostas_formatadas)

            if self.PATH_SAVE == None:
                self.PATH_SAVE = path.dirname(self.PATH_GABARITO)
            status = filesystem.save_file(self.PATH_SAVE, self.ModuloEstatistica.get_data())
            if status != "success":
                print(status)
            else:
                messagebox.showinfo("Sucesso", "Relatorio Concluido")


        else:
            messagebox.showwarning("", "Selecione os arquivos de entrada e saida")

        


class Filebrowser(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        mainauxframe = tk.Frame(self)

        auxframe = tk.Frame(mainauxframe)
        self.path_gabarito = tk.StringVar(self)
        self.path_gabarito.set("Nao selecionado")
        self.label_gabarito = tk.Label(auxframe, text="Gabarito:", font=("Arial", 12)).pack(expand=True, fill="x")
        self.label_path_gabarito = tk.Label(auxframe, textvariable=self.path_gabarito,  width=30, wraplength=300).pack(expand=True, fill="x")
        self.path_respostas = tk.StringVar(self)
        self.path_respostas.set("Nao selecionado")
        self.label_respostas = tk.Label(auxframe, text="Respostas:", font=("Arial", 12)).pack(expand=True, fill="x")
        self.label_path_respostas = tk.Label(auxframe, textvariable=self.path_respostas, width=30, wraplength=300).pack(expand=True, fill="x")

        auxframe2 = tk.Frame(mainauxframe)
        self.button_gabarito = ttk.Button(auxframe2, command= lambda : self.__get_file_path("gabarito"), text="Procurar")
        self.button_gabarito.pack(ipadx = 30, ipady=10, pady=5, padx=5)
        self.button_respostas = ttk.Button(auxframe2, command= lambda : self.__get_file_path("respostas"), text="Procurar")
        self.button_respostas.pack(ipadx = 30, ipady=10, pady=5, padx=5)

        auxframe.pack(side="left", anchor="center", expand=True, fill="both")
        auxframe2.pack(side="right")
        mainauxframe.pack(anchor='w', fill='x', expand=True)


        mainauxframe2 = tk.Frame(self)


        ttk.Separator(mainauxframe2, orient='horizontal').pack(fill='x', expand=True)

        auxframe3 = tk.Frame(mainauxframe2)
        self.path_save = tk.StringVar(self)
        self.path_save.set("Nao selecionado")
        self.label_gabarito = tk.Label(auxframe3, text="Arquivo de saida:", font=("Arial", 12)).pack(expand=True, fill="x")
        self.label_path_gabarito = tk.Label(auxframe3, textvariable=self.path_save,  width=30, wraplength=300).pack(expand=True, fill="x")

        auxframe4 = tk.Frame(mainauxframe2)
        self.button_gabarito = ttk.Button(auxframe4, command=self.__get_save_path, text="Procurar")
        self.button_gabarito.pack(ipadx = 30, ipady=10, pady=5, padx=5)

        auxframe3.pack(side="left", anchor="center", expand=True, fill="both")
        auxframe4.pack(side="right")
        mainauxframe2.pack(expand=True, fill='x')

        ttk.Separator(self, orient='horizontal').pack(fill='x', expand=True, ipady=10)


    def __get_file_path(self, var):
        file = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("exel files","*.xlsx"),("all files","*.*")))
        
        if file == "":
            return

        if var == "gabarito":
            self.path_gabarito.set(file)
            self.master.PATH_GABARITO = file

        if var == "respostas":
            self.path_respostas.set(file)
            self.master.PATH_RESPOSTAS = file


    def __get_save_path(self):
        file_path = tk.filedialog.asksaveasfilename()
        if file_path != '':
            file_path = file_path + ".xlsx"
            self.master.PATH_SAVE = file_path
            self.path_save.set(file_path)


class ConfigFrame(tk.Frame):
    pass
