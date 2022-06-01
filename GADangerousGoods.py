from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn
def dangerous_goods():
    def next_page():
        if check_yes.value == 1:
            warn("Sorry...", "You cannot send dangerous goods through parcel postbox!")
            window.destroy()
        elif check_no.value == 1:
            app.destroy()
    def prevent_conflict():
        if check_yes.value == 1:
            check_no.disable()
        if check_no.value == 1:
            check_yes.disable()
        if check_yes.value == 0:
            check_no.enable()
        if check_no.value == 0:
            check_yes.enable()
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    title_box = Box(window, width="fill", height=50)
    title = Text(title_box, text="RMG DANGEROUS GOOD POLICY",
                 color="white", align="bottom", size=25)
    image = Picture(window, image="/home/pi/ga/dangerous_goods.PNG",
                    width=630, height=420)
    question_box = Box(window, width="fill", height=42)
    question = Text(question_box, text="Are you sending dangerous goods?",
                    color="white", align="bottom", size=25)
    answer_box = Box(window, width=300, height=28)
    yes = Text(answer_box, text="Yes ", align="left", color="white", size=18)
    check_yes = CheckBox(answer_box, align="left", command=prevent_conflict)
    check_no = CheckBox(answer_box, align="right", command=prevent_conflict)
    no = Text(answer_box, text="No ", align="right", color="white", size=18)
    button_box = Box(window, width=1000, height=50)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
app = App(height=600, width=1024, bg="Grey")
app.set_full_screen()
dangerous_goods()
app.display()