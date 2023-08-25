# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\tigge\OneDrive\Área de Trabalho\HT testes\Rifa_clube_maes\build\assets\frame0"
)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x500")
window.configure(bg="#2B3EEB")







canvas = Canvas(
    window,
    bg="#4285F4",
    height=500,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)
canvas.create_text(
    175.0,
    8.0,
    anchor="nw",
    text="Descrição dos Prêmios:",
    fill="#16730E",
    font=("Inter ExtraBold", 30 * -1),
)

canvas.create_text(
    21.0, 47.0, anchor="nw", text="1º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 67.0, anchor="nw", text="2º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 87.0, anchor="nw", text="3º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 107.0, anchor="nw", text="4º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 127.0, anchor="nw", text="5º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 147.0, anchor="nw", text="6º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 167.0, anchor="nw", text="7º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 187.0, anchor="nw", text="8º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    20.0, 207.0, anchor="nw", text="9º Prêmio:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    12.0,
    427.0,
    anchor="nw",
    text="20º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    7.0, 447.0, anchor="nw", text="Observação:", fill="#17740E", font=("Inter", 13 * -1)
)

canvas.create_text(
    12.0,
    469.0,
    anchor="nw",
    text="A observação vai localizada embaixo dos prêmios.\n O nome do arquivo é Rifa_data do sorteio.pdf.",
    fill="#17740E",
    font=("Inter", 12 * -1),
)

canvas.create_text(
    14.0,
    227.0,
    anchor="nw",
    text="10º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    16.0,
    247.0,
    anchor="nw",
    text="11º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    267.0,
    anchor="nw",
    text="12º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    287.0,
    anchor="nw",
    text="13º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    13.0,
    307.0,
    anchor="nw",
    text="14º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    327.0,
    anchor="nw",
    text="15º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    347.0,
    anchor="nw",
    text="16º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    367.0,
    anchor="nw",
    text="17º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    387.0,
    anchor="nw",
    text="18º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_text(
    14.0,
    407.0,
    anchor="nw",
    text="19º Prêmio:",
    fill="#17740E",
    font=("Inter", 13 * -1),
)

canvas.create_rectangle(86.0, 47.0, 692.0, 63.0, fill="#A9C2E7", outline="")

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(389.0, 55.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_1.place(x=88.0, y=49.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 67.0, 692.0, 83.0, fill="#A9C2E7", outline="")

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(389.0, 75.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_2.place(x=88.0, y=69.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 87.0, 692.0, 103.0, fill="#A9C2E7", outline="")

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(389.0, 95.0, image=entry_image_3)
entry_3 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_3.place(x=88.0, y=89.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 107.0, 692.0, 123.0, fill="#A9C2E7", outline="")

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(389.0, 115.0, image=entry_image_4)
entry_4 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_4.place(x=88.0, y=109.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 127.0, 692.0, 143.0, fill="#A9C2E7", outline="")

entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(389.0, 135.0, image=entry_image_5)
entry_5 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_5.place(x=88.0, y=129.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 147.0, 692.0, 163.0, fill="#A9C2E7", outline="")

entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(389.0, 155.0, image=entry_image_6)
entry_6 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_6.place(x=88.0, y=149.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 167.0, 692.0, 183.0, fill="#A9C2E7", outline="")

entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(389.0, 175.0, image=entry_image_7)
entry_7 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_7.place(x=88.0, y=169.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 187.0, 692.0, 203.0, fill="#A9C2E7", outline="")

entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(389.0, 195.0, image=entry_image_8)
entry_8 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_8.place(x=88.0, y=189.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 207.0, 692.0, 223.0, fill="#A9C2E7", outline="")

entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(389.0, 215.0, image=entry_image_9)
entry_9 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_9.place(x=88.0, y=209.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 227.0, 692.0, 243.0, fill="#A9C2E7", outline="")

entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(389.0, 235.0, image=entry_image_10)
entry_10 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_10.place(x=88.0, y=229.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 247.0, 692.0, 263.0, fill="#A9C2E7", outline="")

entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(389.0, 255.0, image=entry_image_11)
entry_11 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_11.place(x=88.0, y=249.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 267.0, 692.0, 283.0, fill="#A9C2E7", outline="")

entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(389.0, 275.0, image=entry_image_12)
entry_12 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_12.place(x=88.0, y=269.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 287.0, 692.0, 303.0, fill="#A9C2E7", outline="")

entry_image_13 = PhotoImage(file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(389.0, 295.0, image=entry_image_13)
entry_13 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_13.place(x=88.0, y=289.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 307.0, 692.0, 323.0, fill="#A9C2E7", outline="")

entry_image_14 = PhotoImage(file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(389.0, 315.0, image=entry_image_14)
entry_14 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_14.place(x=88.0, y=309.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 327.0, 692.0, 343.0, fill="#A9C2E7", outline="")

entry_image_15 = PhotoImage(file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(389.0, 335.0, image=entry_image_15)
entry_15 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_15.place(x=88.0, y=329.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 347.0, 692.0, 363.0, fill="#A9C2E7", outline="")

entry_image_16 = PhotoImage(file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(389.0, 355.0, image=entry_image_16)
entry_16 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_16.place(x=88.0, y=349.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 367.0, 692.0, 383.0, fill="#A9C2E7", outline="")

entry_image_17 = PhotoImage(file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(389.0, 375.0, image=entry_image_17)
entry_17 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_17.place(x=88.0, y=369.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 387.0, 692.0, 403.0, fill="#A9C2E7", outline="")

entry_image_18 = PhotoImage(file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(389.0, 395.0, image=entry_image_18)
entry_18 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_18.place(x=88.0, y=389.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 407.0, 692.0, 423.0, fill="#A9C2E7", outline="")

entry_image_19 = PhotoImage(file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(389.0, 415.0, image=entry_image_19)
entry_19 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_19.place(x=88.0, y=409.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 427.0, 692.0, 443.0, fill="#A9C2E7", outline="")

entry_image_20 = PhotoImage(file=relative_to_assets("entry_20.png"))
entry_bg_20 = canvas.create_image(389.0, 435.0, image=entry_image_20)
entry_20 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_20.place(x=88.0, y=429.0, width=602.0, height=10.0)

canvas.create_rectangle(86.0, 447.0, 692.0, 463.0, fill="#A9C2E7", outline="")

entry_image_21 = PhotoImage(file=relative_to_assets("entry_21.png"))
entry_bg_21 = canvas.create_image(389.0, 455.0, image=entry_image_21)
entry_21 = Entry(bd=0, bg="#A9C2E7", fg="#000716", highlightthickness=0)
entry_21.place(x=88.0, y=449.0, width=602.0, height=10.0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
)
button_1.place(x=382.0, y=469.0, width=204.0, height=25.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(entry_21.get()),
    relief="flat",
)
button_2.place(x=629.0, y=469.0, width=63.0, height=25.0)
window.resizable(False, False)
window.mainloop()
