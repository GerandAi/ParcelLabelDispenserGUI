from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn
def dangerous_goods():
    def sorry_page():
        def next_step():
            #logo.show()
            #window.destroy()
            app.destroy()
        window = Window(app, height=600, width=1024, bg="Grey")
        window.set_full_screen("None")
        image = Picture(window, image="sorry_danger.PNG", width=750, height=420)
        window.after(5000, next_step)
    def next_page():
        if yes_button.bg == "yellow":
            window.destroy()
            sorry_page()
        elif no_button.bg == "yellow":
            app.destroy()
    def yes_pressed():
        yes_button.bg="yellow"
        no_button.bg="white"
        confirm_button.enable()
    def no_pressed():
        no_button.bg="yellow"
        yes_button.bg="white"
        confirm_button.enable()
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    title_box = Box(window, width="fill", height=50)
    title = Text(title_box, text="Are you sending prohibited or restricted items?",
                 color="white", align="bottom", size=25)
    image = Picture(window, image="/home/pi/ga/dangerous_goods.PNG",
                    width=630, height=420)
    yesno_box = Box(window, width=500, height=70)
    yes_button = PushButton(yesno_box, text="Yes", align="left",
                            height=1, width=8, command=yes_pressed)
    yes_button.bg="white"
    yes_button.text_size=25
    no_button = PushButton(yesno_box, text="No", align="right",
                           height=1, width=8, command=no_pressed)
    no_button.bg="white"
    no_button.text_size=25
    button_box = Box(window, width=1000, height=50)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
    confirm_button.disable()
app = App(height=600, width=1024, bg="Grey")
app.set_full_screen()
dangerous_goods()
app.display()