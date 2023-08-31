import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

def browse_button(root, entry):
    folder_path = filedialog.askdirectory()
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

def generate_txt(src_folder, output_folder, output_filename):
    structure_text = 'Estrutura do projeto:\n"'
    code_text = ''
    
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".java") or file.endswith(".py"):
                relative_path = os.path.relpath(os.path.join(root, file), src_folder)
                structure_text += relative_path + '\n'
                
                with open(os.path.join(root, file), 'r', encoding="utf-8", errors='ignore') as f:
                    file_content = f.read()
                    
                code_text += f'Arquivo {relative_path}:\n'
                code_text += f"'\n{file_content}\n'\n"

    structure_text += '"\n'
    
    with open(os.path.join(output_folder, output_filename + ".txt"), "w") as f:
        f.write(structure_text)
        f.write(code_text)

def main():
    root = tk.Tk()
    root.title("Project Reader")

    # Make the window always on top
    root.attributes('-topmost', 1)

    # Added padding to the main window
    root.grid_rowconfigure(0, pad=10)
    root.grid_columnconfigure(0, pad=10)

    ttk.Label(root, text="Select Source Folder:").grid(row=0, column=0, padx=10, pady=10)
    src_entry = ttk.Entry(root, width=50)
    src_entry.grid(row=0, column=1, padx=10, pady=10)
    ttk.Button(root, text="Browse", command=lambda: browse_button(root, src_entry)).grid(row=0, column=2, padx=10, pady=10)

    ttk.Label(root, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=10)
    output_entry = ttk.Entry(root, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=10)
    ttk.Button(root, text="Browse", command=lambda: browse_button(root, output_entry)).grid(row=1, column=2, padx=10, pady=10)

    ttk.Label(root, text="Output Filename:").grid(row=2, column=0, padx=10, pady=10)
    filename_entry = ttk.Entry(root, width=50)
    filename_entry.grid(row=2, column=1, padx=10, pady=10)

    ttk.Button(root, text="Generate", command=lambda: generate_txt(src_entry.get(), output_entry.get(), filename_entry.get())).grid(row=3, columnspan=3, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
