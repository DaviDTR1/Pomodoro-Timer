from tkinter import *
from pygame import mixer


# -----------------------------CONSTANTS---------------------------------

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Cuorier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = '✔'
pomodoros = 0
timer = None

# -----------------------------Timer Reset-------------------------------
def reset_button_clicked():
    global pomodoros
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    pomodoros = 0
    pomodoro_label.config(text="")


# -----------------------------Timer Mechanism---------------------------
def start_button_clicked():
    global is_reset
    is_reset = False
    timer_move(1)

def timer_move(moves):
    global count,pomodoros
    mixer.init()
    mixer.music.load("data/sound1.mp3")
    mixer.music.play()
    if moves%2==1:
        count = WORK_MIN*60
        pomodoros -= 1
        timer_label.config(text="Work", fg=GREEN)
    elif moves%2==0 and moves%8!=0:
        count = SHORT_BREAK_MIN*60
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count = LONG_BREAK_MIN*60
        timer_label.config(text="Long Break", fg=RED)
        
    pomodoros += 1
    texts = ""
    for i in range(pomodoros):
        texts += CHECK_MARK 
    pomodoro_label.config(text= texts)
    
    # .after(miliseconds, function, parameters)
    window.after(1000, Count_Down,moves,count)
    
        
# -----------------------------Countddown Mechanism----------------------
def Count_Down(moves = 1,count = 1):
    global timer
    count_min = int(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    # change config in canvas
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count == 0:
        timer_move(moves+1)
        return 
    # save action in timer
    timer = window.after(1000, Count_Down,moves,count-1)
         


# -----------------------------UI Setup----------------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
icon = PhotoImage(file="data/pomodoro.png")
window.iconphoto(True,icon)

timer_label = Label(text="Timer", font=(FONT_NAME,32,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(column=1,row=0)

canvas = Canvas(width=300,height=286, bg=YELLOW,highlightthickness=0)
background = PhotoImage(file="data/tomato.png")
canvas.create_image(150,143, image=background)
# save canvas text in time_text
time_text = canvas.create_text(150,183,text="00:00",fill="white",font=(FONT_NAME,26,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start",bg=YELLOW, command=start_button_clicked)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",bg=YELLOW, command=reset_button_clicked)
reset_button.grid(column=2,row=2)

pomodoro_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME,15,'bold'))
pomodoro_label.grid(column=1,row=3)








window.mainloop()