from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
our_timer="None"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global our_timer
    window.after_cancel(our_timer)
    global reps
    reps=0
    canvas.itemconfig(timer_text, text="00:00")
    text_label.config(text="TIMER", fg=GREEN)
    check_mark.config(text="")




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global our_timer
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        our_timer=window.after(1000,count_down,count-1)
    else:
        if reps % 2 == 1:
            current = check_mark.cget("text")
            check_mark.config(text=current + "✓")
        start_click()



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_click():
    work_time=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    global reps
    reps += 1

    if reps%8==0:
        count_down(long_break)
        text_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break)
        text_label.config(text="Break", fg=PINK)
    else:
        count_down(work_time)
        text_label.config(text="Work Time", fg=GREEN)

# if reps!=8 and reps % 2 != 0:
    #     count_down(work_time)
    # elif reps!=8 and reps % 2 == 0:
    #     count_down(short_break)
    # else:
    #     reps=0
    #     count_down(long_break)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro app")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=233,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,100,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,27,"bold"))
canvas.grid(column=2,row=1)


text_label=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=("FONT_NAME",35,"normal"))
text_label.grid(column=2,row=0)


start_button=Button(text="Start", font="FONT_NAME", highlightthickness=0, command=start_click)
start_button.grid(column=1,row=3)

reset_button=Button(text="Reset",font="FONT_NAME",highlightthickness=0,command=reset_time)
reset_button.grid(column=3,row=3)
check_mark=Label(fg=GREEN,bg=YELLOW)
check_mark.grid(column=2,row=3)




window.mainloop()