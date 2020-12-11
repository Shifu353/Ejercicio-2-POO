import sys 

python_version = sys.version_info.major

print(python_version)

if python_version < 3:
    try:
        import kinter
    except ImportError:
        raise ("Se nenecesita una version 3.X de Python")
else:
    try:
        import tkinter as tk
        from tkinter import font,ttk,messagebox
        import getpass
        import json 
        import requests

        class Moneda ():
            __ventana = None 
            __Conversion  = None
            __dolar = None

            def __init__ (self):
                respuesta = requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
                
                respuesta_json = json.loads(respuesta.text)
                i = 0
                while(i < len(respuesta_json) & (respuesta_json[i]["casa"]["nombre"] != "Oficial")):
                    i += 1
                if (i < len(respuesta_json)):
                    self.__venta = float(respuesta_json[i]["casa"]["venta"].replace(",","."))
                
                texto = "Bienvenido/a %s a mi ejercicio 2" %getpass.getuser()
                self.__ventana = tk.Tk()
                self.__ventana.title(texto)
                self.__ventana.geometry("290x115")
                self.__ventana.resizable(False,False)

                self.__dolar = tk.IntVar()
                self.__Conversion = tk.StringVar()

                mainframe = ttk.Frame(self.__ventana)
                #mainframe.columnconfigure(0,weight=1)
                #mainframe.rowconfigure(0,weight=1)
                mainframe.grid(row=0,column=0)
                self.Entry = ttk.Entry(mainframe,textvariable=self.__dolar,width=10)
                self.Entry.grid(row=0,column=2,sticky="w")
                ttk.Label(mainframe,text="dólares",anchor=tk.NE).grid(row=0,column=3)
                ttk.Label(mainframe,text="es equivalente a ").grid(row=1,column=1)
                ttk.Label(mainframe,text="pesos").grid(row=1,column=3)
                ttk.Label(mainframe,textvariable=self.__Conversion).grid(row=1,column=2)
                ttk.Button(mainframe,text="Salir",command=self.__ventana.destroy).grid(row=2,column=3)
                
                self.Entry.focus()
                self.__dolar.trace("w",self.Calcular)
                self.__ventana.mainloop()
            def Calcular (self,*args):
                try:
                    cant=float(self.__dolar.get())
                    total = self.__venta * cant
                    self.__Conversion.set(total)
                except ValueError:
                    messagebox.showerror(title="Error de Tipo",message="Introduzca un numero")
                    self.__dolar.set("")
                    self.Entry.focus()
                    
                
    
        
        if __name__ == "__main__":
            app = Moneda()
                

    
    except ImportError:
        raise ImportError ("Error al ejecutar el programa")
