from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn
def check_parcel():
    def change_image():
        if image.value == "/home/pi/ga/buffer0.PNG":
            image.value="/home/pi/ga/buffer1.PNG"
        elif image.value == "/home/pi/ga/buffer1.PNG":
            image.value="/home/pi/ga/buffer0.PNG"
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Please wait while we perform checks on the parcel ; )",
                 color="white", align="bottom", size=30)
    image_box = Box(window, width="fill", height=420)
    image = Picture(image_box, image="/home/pi/ga/buffer0.PNG", align="bottom",
                    width=390, height=390)
    parcel_qualified = -1
    image.repeat(500, change_image)
    def next_step():
        window.destroy()
        good_parcel()
    window.after(2000, next_step)
def good_parcel():
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    correct_parcel = Text(window, text="                  We've done the checks!   ",
                          color="white", align="left", size=30)
    image = Picture(window, image="/home/pi/ga/right.PNG", align="left",
                    width=120, height=100)
    def next_step():
        window.destroy()
        bad_parcel()
    window.after(1000, next_step)
def bad_parcel():
    window = Window(app, height=600, width=1024, bg="Grey")
    window.set_full_screen()
    text_box = Box(window, width="fill", height=150)
    correct_parcel_line1 = Text(text_box, text="TO BE SENT THROUGH PARCEL POSTBOX",
                                color="white", align="bottom", size=30)
    correct_parcel_line0 = Text(text_box, text="PARCEL IS OF INCORRECT DIMENSIONS / WEIGHT",
                                color="white", align="bottom", size=30)
    image = Picture(window, image="/home/pi/ga/wrong.PNG", width=100, height=100)
    website_redirect = Text(window, text="Please scan below QR code for further details:",
                                color="white", size=30)
    QR_code = Picture(window, image="/home/pi/ga/QR_code.png", width=250, height=250)
    def window_destroy():
        window.destroy()
    window.after(5000, window_destroy)

app = App(height=600, width=1024, bg="Grey")
app.set_full_screen()
title_box = Box(app, width="fill", height=100)
title = Text(title_box, text="WELCOME TO PARCEL LABEL DISPENSER",
             color="white", align="bottom", size=35)
button_box = Box(app, width="fill", height=280)
begin_button = PushButton(button_box, text="CLICK TO BEGIN", align="bottom",
                          height=3, width=15, command=check_parcel)
begin_button.bg="white"
begin_button.text_size=30
logo_box = Box(app, align="bottom", width="fill")
logo = Picture(logo_box, image="/home/pi/ga/logo.png", align="right",
               width=290, height=190)
app.display()