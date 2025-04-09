import os
from pathlib import Path
import time
import customtkinter as ctk
from customtkinter import filedialog


def createTitle(event):
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
    global font, fontSize
    text = textField.cget("font") #returns a tuple with the actual format of the field
    # print(text)
    if "bold" in text:
        textField.configure(font=(font, fontSize, "normal"))
        btn_bold.configure(fg_color="#ebebeb")
    else:
        textField.configure(font=(font, fontSize, "bold"))
        btn_bold.configure(fg_color="#dedede")
    

def setItalic():
    global font, fontSize
    text = textField.cget("font") #returns a tuple with the actual format of the field
    # print(text)
    if "italic" in text:
        textField.configure(font=(font, fontSize, "normal"))
        btn_bold.configure(fg_color="#ebebeb")
    else:
        textField.configure(font=(font, fontSize, "italic"))
        btn_bold.configure(fg_color="#dedede")

def setUnderline():
    global font, fontSize
    text = textField.cget("font") #returns a tuple with the actual format of the field
    # print(text)
    if "italic" in text:
        textField.configure(font=(font, fontSize, "normal"))
        btn_bold.configure(fg_color="#ebebeb")
    else:
        textField.configure(font=(font, fontSize, "italic"))
        btn_bold.configure(fg_color="#dedede")

def setFont(choice):
    global font, fontSize
    font = choice
    print(font)
    textField.configure(font=(font, fontSize))

def setFontSize(choice):
    global fontSize
    fontsize = int(choice)
    textField.configure(font=ctk.CTkFont(size=fontsize))

def saveFile():
    #formatting the title for the filename
    title = title_entry.get()
    title = title.lower().replace(" ", "_")
    # print(title)

    try:
        f = open(f"notes/{title}.txt", "x", encoding="UTF-8")
        f.write(textField.get('1.0', 'end'))
        f.close()

        #success
        btn_save.configure(fg_color="#95ff7a")
        time.sleep(2)
        btn_save.configure(fg_color="#ebebeb")
    except Exception as err:
        print("Error:", err)

def openFile():
    filepath = filedialog.askopenfilename()
    f = open(filepath, "r", encoding="UTF-8")
    filename = Path(filepath).stem #stem is a method for removing the ".txt" of the file
    filetext = f.read()
    #deleting actual content
    textField.delete("1.0", "end")
    #inserting the content of the file
    textField.insert("1.0", text=filetext)

    #changing the title
    title_value = ctk.StringVar(value=filename)
    title_entry.configure(textvariable=title_value)

# ===========
#  INTERFACE
# ===========

app = ctk.CTk()
app.geometry("500x500")
app.title("Editor de Texto")
app.resizable("False", "False")

#default configurations
font = "Arial"
fontSize = 16
fontFormat = "normal"

#color scheme (light)
light_bg = "#ebebeb" #fg for widgets
light_text="black"
light_hover="#dedede"

#color scheme (dark)
dark_bg = "red"
dark_text="white"
dark_hover = "#171717"

ctk.set_appearance_mode("light")

#grid config
app.grid_columnconfigure(0, weight=9, minsize="350")
app.grid_columnconfigure((1, 2, 3, 4), weight=1, minsize=50)

app.rowconfigure(0, weight=0)
app.rowconfigure(1, weight=0)
app.rowconfigure(2, weight=1)

title_entry = ctk.CTkEntry(app,
    placeholder_text="Insira o título do documento...",
    font=("Arial", 14),
    height=40,
    # fg_color="#ebebeb",
    border_width=0
    )
title_entry.grid(column=0, row=0, columnspan=2, padx=5, pady=5, sticky="ew")

title_entry.bind("<KeyRelease>", createTitle) #change the title of the window when the user stops typing

btn_save = ctk.CTkButton(app,
    text="💾",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    fg_color=[light_bg, dark_bg],
    text_color=light_text,
    hover_color=light_hover,
    command=saveFile
    )
btn_save.grid(column=2, row=0, padx=2, pady=5)

btn_print = ctk.CTkButton(app,
    text="📁",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    fg_color=light_bg,
    text_color=light_text,
    hover_color=light_hover,
    command=openFile
    )
btn_print.grid(column=3, row=0, padx=2, pady=5, sticky="w")

btn_theme = ctk.CTkButton(app,
    text="🌙",
    height=40,
    width=40,
    font=("Arial", 14, "bold"),
    fg_color=light_bg,
    text_color=light_text,
    hover_color=light_hover,
    command=changeTheme
    )
btn_theme.grid(column=4, row=0, padx=2, pady=5, sticky="w")

cbx_fonts = ctk.CTkComboBox(app,
    values=['Arial', 'Courier New', 'Times New Roman', 'Helvectica'],
    height=40,
    command=setFont,
    font=("Arial", 14),
    border_width=0
    )
cbx_fonts.grid(column=0, row=1, padx=5, pady=5, sticky="ew")

font_sizes = []
for i in range(8, 24):
    i+=2
    font_sizes.append(str(i))

cbx_size = ctk.CTkComboBox(app,
    values=font_sizes,
    height=40,
    command=setFontSize,
    font=("Arial", 14,),
    border_width=0
    )
cbx_size.set("14")
cbx_size.grid(column=1, row=1, padx=5, pady=5, sticky="ew")

btn_bold = ctk.CTkButton(app,
    text="B",
    font=("Arial", 16),
    height=40,
    width=40,
    fg_color=light_bg,
    text_color=light_text,
    hover_color=light_hover,
    command=setBold
    )
btn_bold.grid(column=2, row=1, padx=5, pady=5, sticky="w")

btn_italic = ctk.CTkButton(app,
    text="I",
    font=("Times New Roman", 16, "italic"),
    fg_color=light_bg,
    text_color=light_text,
    hover_color=light_hover,
    height=40,
    width=40,
    command=setItalic
    )
btn_italic.grid(column=3, row=1, padx=5, pady=5, sticky="w")

btn_underline = ctk.CTkButton(app,
    text="U",
    font=("Arial", 16, "underline"),
    fg_color=light_bg,
    text_color=light_text,
    hover_color=light_hover,
    height=40,
    width=40,
    command=setUnderline
    )
btn_underline.grid(column=4, row=1, padx=5, pady=5, sticky="w")

textField = ctk.CTkTextbox(app,
    border_width=0,   
    corner_radius=0,
    font=(font, fontSize),
    wrap="word"
    )

textField.grid(column=0, columnspan=5, rowspan=10, row=2, padx=10, pady=5, sticky="nsew")

app.mainloop()