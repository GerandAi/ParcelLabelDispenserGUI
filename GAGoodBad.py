from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn, Combo, TextBox
def good_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    image = Picture(window, image="good_parcel.PNG", width=420, height=180)
    photo_box = Box(window, width=520, height=330, border=3)
    image = Picture(photo_box, image="Enclosure.jpg", width=517, height=347)
    def next_step():
        window.destroy()
        bad_parcel()
    window.after(5000, next_step)
def bad_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    image = Picture(window, image="bad_parcel.PNG", height=520, width=660)
    def window_destroy():
        logo.show()
        window.destroy()
    def next_page():
        #window.destroy()
        #entre_details()
        app.destroy()
    window.after(3000, next_page)

Grey = (127, 127, 127)
app = App(height=600, width=1024, bg=Grey)
app.set_full_screen()
good_parcel()
app.display()