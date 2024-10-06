import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PIL
import trimesh

class FileRenamerImporter:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer and Importer Tool")
        self.filepath = ""

        # Set up UI
        self.label = tk.Label(root, text="Choose a file to import")
        self.label.pack(pady=10)

        self.import_button = tk.Button(root, text="Import File", command=self.import_file)
        self.import_button.pack(pady=5)

        self.rename_button = tk.Button(root, text="Rename File", command=self.rename_file)
        self.rename_button.pack(pady=5)

        self.preview_label = tk.Label(root, text="")
        self.preview_label.pack(pady=10)

    def import_file(self):
        self.filepath = filedialog.askopenfilename(
            filetypes=[("All Files", "*.*"), ("Images", "*.png;*.jpg"), ("3D Mesh", "*.obj;*.fbx")]
        )
        if self.filepath:
            filename = os.path.basename(self.filepath)
            self.label.config(text=f"File selected: {filename}")

            # Handle image preview or 3D mesh loading
            if self.filepath.endswith(('.png', '.jpg')):
                self.preview_image(self.filepath)
            elif self.filepath.endswith(('.obj', '.fbx')):
                self.load_3d_mesh(self.filepath)
            else:
                self.preview_label.config(text="Preview not available")

    def preview_image(self, image_path):
        img = Image.open(image_path)
        img.thumbnail((200, 200))
        img = ImageTk.PhotoImage(img)
        self.preview_label.config(image=img)
        self.preview_label.image = img

    def load_3d_mesh(self, mesh_path):
        mesh = trimesh.load(mesh_path)
        self.preview_label.config(text=f"3D Mesh: {mesh_path} loaded")

    def rename_file(self):
        if self.filepath:
            new_name = filedialog.asksaveasfilename(defaultextension=os.path.splitext(self.filepath)[1])
            if new_name:
                os.rename(self.filepath, new_name)
                messagebox.showinfo("Success", f"File renamed to: {new_name}")
                self.label.config(text="File renamed successfully")
        else:
            messagebox.showerror("Error", "No file selected")


# Initialize Tkinter window
root = tk.Tk()
app = FileRenamerImporter(root)
root.mainloop()
