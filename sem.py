import tkinter as tk
from PIL import Image, ImageTk
import os

class SemaforoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Semáforo Peatonal")
        self.geometry("800x1000")
        
        # Cargar imágenes
        self.img_cruzando = self.cargar_imagen("cruzando.png")
        self.img_quieta = self.cargar_imagen("quieta.png")
        
        self.label = tk.Label(self, text="30", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=20)

        self.status_label = tk.Label(self, text="Verde", font=("Helvetica", 24), fg="green")
        self.status_label.pack(pady=20)

        self.green_time = 30
        self.red_time = 20
        
        self.is_green = True
        self.remaining_time = self.green_time
        
        # Mostrar imagen inicial
        self.image_label.config(image=self.img_cruzando)
        self.image_label.image = self.img_cruzando

        self.update_timer()

    def cargar_imagen(self, ruta):
        if not os.path.exists(ruta):
            print(f"Error: la imagen {ruta} no se encuentra.")
            return None
        try:
            print(f"Cargando imagen: {ruta}")
            return ImageTk.PhotoImage(Image.open(ruta).resize((550, 700)))  # Ajusta el tamaño según sea necesario
        except Exception as e:
            print(f"Error al cargar la imagen {ruta}: {e}")
            return None

    def update_timer(self):
        self.label.config(text=str(self.remaining_time))
        
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.after(1000, self.update_timer)
        else:
            self.toggle_light()

    def toggle_light(self):
        self.is_green = not self.is_green
        if self.is_green:
            self.status_label.config(text="Verde", fg="green")
            if self.img_cruzando:
                self.image_label.config(image=self.img_cruzando)
                self.image_label.image = self.img_cruzando  # Mantener una referencia para evitar que la imagen sea recolectada por el garbage collector
            else:
                print("Imagen de cruzando no cargada.")
            self.remaining_time = self.green_time
        else:
            self.status_label.config(text="Rojo", fg="red")
            if self.img_quieta:
                self.image_label.config(image=self.img_quieta)
                self.image_label.image = self.img_quieta  # Mantener una referencia para evitar que la imagen sea recolectada por el garbage collector
            else:
                print("Imagen de quieta no cargada.")
            self.remaining_time = self.red_time
        self.update_timer()

if __name__ == "__main__":
    app = SemaforoApp()
    app.mainloop()

