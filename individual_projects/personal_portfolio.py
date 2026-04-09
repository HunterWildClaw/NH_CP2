# NH 2nd personal portfolio
import tkinter as tk

class MyProjectsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My fav projects")
        self.root.geometry("500x400")

        # Container to stack frames on top of each other
        self.container = tk.Frame(self.root)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        # Create the Main Menu and the four blank pages
        for PageClass in (MainMenu, FractalPage, MorsePage, WoWPage, LibraryPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self.container, controller=self)
            self.frames[page_name] = frame
            # Put all pages in the same location; the top one is the visible one
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="My fav projects", font=("Arial", 18, "bold"))
        label.pack(pady=20)

        # Buttons to navigate to other pages
        buttons = [
            ("Fractal Pattern Generator", "FractalPage"),
            ("Morse Code Translator", "MorsePage"),
            ("WoW", "WoWPage"),
            ("Personal Library", "LibraryPage")
        ]

        for text, page in buttons:
            btn = tk.Button(self, text=text, width=25, pady=10,
                            command=lambda p=page: controller.show_frame(p))
            btn.pack(pady=5)

# Template for the sub-pages
class ProjectPage(tk.Frame):
    def __init__(self, parent, controller, title):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Exit button in the top left
        exit_btn = tk.Button(self, text="Exit to Menu", command=lambda: controller.show_frame("MainMenu"))
        exit_btn.place(x=10, y=10)

        # Title for the blank page
        label = tk.Label(self, text=title, font=("Arial", 14, "italic"))
        label.pack(pady=100)

# Defining each specific page class
class FractalPage(ProjectPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Fractal Pattern Generator (Blank)")

class MorsePage(ProjectPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Morse Code Translator (Blank)")

class WoWPage(ProjectPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "WoW (Blank)")

class LibraryPage(ProjectPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Personal Library (Blank)")

if __name__ == "__main__":
    root = tk.Tk()
    app = MyProjectsApp(root)
    root.mainloop()