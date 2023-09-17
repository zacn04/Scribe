import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")
        
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.start_rectangle)
        self.canvas.bind("<B1-Motion>", self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.end_rectangle)

        self.start_x, self.start_y = None, None
        self.current_rect = None

    def start_rectangle(self, event):
        self.start_x, self.start_y = event.x, event.y

    def draw_rectangle(self, event):
        if self.start_x and self.start_y:
            if self.current_rect:
                self.canvas.delete(self.current_rect)
            x, y = event.x, event.y
            self.current_rect = self.canvas.create_rectangle(
                self.start_x,
                self.start_y,
                x,
                y,
                outline="black",
                width=2
            )

    def end_rectangle(self, event):
        self.start_x, self.start_y = None, None
        self.current_rect = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
