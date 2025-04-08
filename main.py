import customtkinter as ctk 

def createTitle():
    app.title(title_entry.get())

def changeTheme():
    actual_theme = app._get_appearance_mode()

    if actual_theme == "light":
        app._set_appearance_mode("dark")
        btn_theme.configure(text="☀")
    elif actual_theme == "dark":
        app._set_appearance_mode("light")
        btn_theme.configure(text="🌙")

def setBold():
    selected_text = textField.selection_get()
    print(selected_text)
    textField.configure(font=("Arial", 14, "bold"))

def setItalic():
    textField.configure(font=("Arial", 14, "italic"))

def setUnderline():
    textField.configure(font=("Arial", 14, "underline"))

def setFont(choice):
    font = choice
    print(font)
    textField.configure(font=(font, 14))

def setFontSize(choice):
    fontsize = int(choice)
    textField.configure(font=ctk.CTkFont(size=fontsize))

# ===========
#  INTERFACE
# ===========

app = ctk.CTk()
app.geometry("500x500")
app.title("Editor de Texto")
app.resizable("False", "False")

#default theme
ctk.set_appearance_mode("light")

#grid config
app.grid_columnconfigure(0, weight=9, minsize="350")
app.grid_columnconfigure((1, 2, 3, 4), weight=1, minsize=50)

app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=0)
app.rowconfigure(2, weight=1)

title_value = ctk.StringVar(value="Insira o nome do título...")
title_value.trace_add("write", lambda *args: createTitle())

title_entry = ctk.CTkEntry(app,
    textvariable=title_value,
    font=("Arial", 14),
    height=40,
    border_width=0
    )
title_entry.grid(column=0, row=0, padx=5, pady=5, sticky="ew")

btn_save = ctk.CTkButton(app,
    text="💾",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    )
btn_save.grid(column=1, row=0, padx=2, pady=5, sticky="w")

btn_print = ctk.CTkButton(app,
    text="📄",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    )
btn_print.grid(column=2, row=0, padx=2, pady=5, sticky="w")

btn_theme = ctk.CTkButton(app,
    text="🌙",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    command=changeTheme
    )
btn_theme.grid(column=3, row=0, padx=2, pady=5, sticky="ew")

print(app.grid_size())

cbx_fonts = ctk.CTkComboBox(app,
    values=['Arial', 'Courier New', 'Times New Roman', 'Helvectica'],
    height=40,
    command=setFont,
    border_width=0
    )
cbx_fonts.grid(column=0, row=1, padx=5, pady=5, sticky="ew")

cbx_size = ctk.CTkComboBox(app,
    values=['8', '10', '12', '14', '16', '18', '20'],
    height=40,
    command=setFontSize,
    border_width=0
    )
cbx_size.grid(column=1, row=1, padx=5, pady=5, sticky="ew")

btn_bold = ctk.CTkButton(app,
    text="B",
    font=("Arial", 16, "bold"),
    height=40,
    width=40,
    command=setBold
    )
btn_bold.grid(column=2, row=1, padx=5, pady=5, sticky="w")

btn_italic = ctk.CTkButton(app,
    text="I",
    font=("Times New Roman", 16, "italic"),
    height=40,
    width=40,
    command=setItalic
    )
btn_italic.grid(column=3, row=1, padx=5, pady=5, sticky="w")

btn_underline = ctk.CTkButton(app,
    text="U",
    font=("Arial", 16, "underline"),
    height=40,
    width=40,
    command=setUnderline
    )
btn_underline.grid(column=4, row=1, padx=5, pady=5, sticky="w")

textField = ctk.CTkTextbox(app,
    border_width=0,   
    corner_radius=0,
    font=("Arial", 14)
    )

textField.grid(column=0, columnspan=4, rowspan=10, row=2, padx=10, pady=5, sticky="nsew")

app.mainloop()