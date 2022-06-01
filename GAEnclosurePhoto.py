from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn
def enclosure_photo():
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    display_box = Box(window, align="left", width=550, height=380)
    image_box = Box(display_box, width=520, height=350, border=3)
    photo_box = Box(image_box, align="bottom", width="fill", height=338)
    image = Picture(photo_box, image="/home/pi/ga/Enclosure.jpg",
                    width=502, height=330)
    caption = Text(display_box, text="(PICTURE OF INSIDE PARCEL ENCLOSURE)",
                   color="white", align="bottom", size=15)
    interaction_box = Box(window, align="right", width=470, height=320)
    question_line0= Text(interaction_box, text="IS PARCEL SHOWN ON",
                         color="white", size=25)
    question_line1 = Text(interaction_box, text="LEFT THE PARCEL TO",
                          color="white", size=25)
    question_line2 = Text(interaction_box, text="BE SENT?",
                          color="white", size=25)
    def next_page():
        if check_yes.value == 1:
            app.destroy()
        elif check_no.value == 1:
            warn("Sorry...", "Please restart the process!")
            window.destroy()
    button_box = Box(interaction_box, align="bottom", width="fill", height=55)
    confirm_button = PushButton(button_box, text="CONFIRM",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
    def prevent_conflict():
        if check_yes.value == 1:
            check_no.disable()
        if check_no.value == 1:
            check_yes.disable()
        if check_yes.value == 0:
            check_no.enable()
        if check_no.value == 0:
            check_yes.enable()
    answer_box = Box(interaction_box, width=300, height=170)
    yes = Text(answer_box, text="Yes ", align="left", color="white", size=22)
    check_yes = CheckBox(answer_box, align="left", command=prevent_conflict)
    check_no = CheckBox(answer_box, align="right", command=prevent_conflict)
    no = Text(answer_box, text="No ", align="right", color="white", size=22)

app = App(height=600, width=1024, bg="Grey")
app.set_full_screen()
title_box = Box(app, width="fill", height=100)
title = Text(title_box, text="WELCOME TO PARCEL LABEL DISPENSER",
             color="white", align="bottom", size=35)
button_box = Box(app, width="fill", height=280)
begin_button = PushButton(button_box, text="CLICK TO BEGIN", align="bottom",
                          height=3, width=15, command=enclosure_photo)
begin_button.bg="white"
begin_button.text_size=30
logo_box = Box(app, align="bottom", width="fill")
logo = Picture(logo_box, image="/home/pi/ga/logo.png", align="right",
               width=290, height=190)
app.display()