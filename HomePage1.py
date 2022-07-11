import os
os.chdir("/home/pi/parcellabeldispensergui")
from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn, Combo, TextBox
import FuncsPLD as fp
def dangerous_goods():
    logo.hide()
    fp.initiate_weight_check()
    def sorry_page():
        def next_step():
            logo.show()
            window.destroy()
        window = Window(app, height=600, width=1024, bg=Grey)
        window.set_full_screen("None")
        image = Picture(window, image="sorry_danger.PNG", width=750, height=420)
        window.after(5000, next_step)
    def next_page():
        if yes_button.bg == "yellow":
            window.destroy()
            sorry_page()
        elif no_button.bg == "yellow":
            window.destroy()
            packed_securely()
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
def packed_securely():
    def sorry_page():
        def next_step():
            logo.show()
            window.destroy()
        window = Window(app, height=600, width=1024, bg=Grey)
        window.set_full_screen("None")
        image = Picture(window, image="sorry_pack.PNG", width=630, height=420)
        window.after(5000, next_step)
    def next_page():
        if no_button.bg == "yellow":
            window.destroy()
            sorry_page()
        else:
            initial_weight = fp.return_initial_weight()
            if initial_weight == 0:
                window.destroy()
                input_parcel()
            elif initial_weight == 1 :
                window.destroy()
                check_debris()
            elif initial_weight == -1:
                window.info("Too fast!!!", "Please read carefully...")
    def yes_pressed():
        yes_button.bg="yellow"
        no_button.bg="white"
        confirm_button.enable()
    def no_pressed():
        no_button.bg="yellow"
        yes_button.bg="white"
        confirm_button.enable()
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    image = Picture(window, image="packed_securely.PNG",
                    width=800, height=420)
    yesno_box = Box(window, width=500, height=80)
    yes_button = PushButton(yesno_box, text="Yes", align="left",
                            height=1, width=8, command=yes_pressed)
    yes_button.bg="white"
    yes_button.text_size=25
    no_button = PushButton(yesno_box, text="No", align="right",
                           height=1, width=8, command=no_pressed)
    no_button.bg="white"
    no_button.text_size=25
    button_box = Box(window, width=1000, height=60)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=1, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
    confirm_button.disable()

hall_in_use = False
def check_debris():
    fp.servo_unlock()
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Please remove Debris from Enclosure",
                 color="white", align="bottom", size=30)
    image = Picture(window, image="remove_debris.PNG",
                    width=830, height=420)
    def next_step():
        fp.initiate_weight_check()
        title.value = "Please wait while we check if debris is cleared"
        def change_colour():
            if title.text_color == "white":
                title.text_color = "red"
            elif title.text_color == "red":
                title.text_color = "white"
        window.repeat(500, change_colour)
        def get_debris_status():
            debris = fp.return_initial_weight()
            if debris == 0:
                window.destroy()
                input_parcel()
            elif debris == 1:
                global hall_in_use
                if hall_in_use is False:
                    fp.initiate_hall_sensor()
                    hall_in_use = True
                    title.value = "Please close the door..."
                    def fall_back():
                        door_shut = fp.return_door_shut()
                        if door_shut == 1:
                            fp.servo_lock()
                            logo.show()
                            window.destroy()
                    window.repeat(200, fall_back)
        window.repeat(200, get_debris_status)
    confirm_button = PushButton(window, text="CLEARED", align="right",
                                height=1, width=8, command=next_step)
    confirm_button.bg="white"
    confirm_button.text_size=25
def input_parcel():
    fp.servo_unlock()
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Place Parcel in Enclosure & Close Enclosure Door",
                 color="white", align="bottom", size=30)
    image_box = Box(window, width="fill", height=390)
    image = Picture(image_box, image="input_parcel.PNG", align="bottom",
                    width=900, height=320)
    def delay():
        def check_door_shut():
            fp.initiate_hall_sensor()
            def next_step():
                door_shut = fp.return_door_shut()
                if door_shut == 1:
                    fp.servo_lock()
                    window.destroy()
                    check_parcel()
            window.repeat(200, next_step)
        #check_door_shut()
        window.repeat(5000, check_door_shut)
    window.after(5000, delay)
def check_parcel():
    fp.initiate_parcel_check()
    def change_image():
        if image.value == "buffer0.PNG":
            image.value="buffer1.PNG"
        elif image.value == "buffer1.PNG":
            image.value="buffer0.PNG"
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Please wait while the parcel is checked.",
                 color="white", align="bottom", size=30)
    image_box = Box(window, width="fill", height=420)
    image = Picture(image_box, image="buffer0.PNG", align="bottom",
                    width=390, height=390)
    image.repeat(500, change_image)
    def next_step():
        check_result = fp.return_parcel_spec()
        if check_result == 1:
            fp.camera()
            fp.servo_unlock()
            window.destroy()
            good_parcel()
        elif check_result == 0:
            fp.servo_unlock()
            window.destroy()
            bad_parcel()
    window.repeat(100, next_step)
def good_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    image = Picture(window, image="good_parcel.PNG", width=420, height=180)
    photo_box = Box(window, width=520, height=330, border=3)
    def display_image():
        image = Picture(photo_box, image="Enclosure.jpg", width=517, height=347)
    window.after(390, display_image)
    def next_page():
        window.destroy()
        entre_details()
    window.after(5900, next_page)
def bad_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    image = Picture(window, image="bad_parcel.PNG", height=520, width=650)
    def window_destroy():
        window.destroy()
        global print_label
        print_label = False
        close_door()
    window.after(10000, window_destroy)
service = "str"
receiver = "str"
road = "str"
city = "str"
postcode = "str"
def entre_details():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    
    top_space = Box(window, width="fill", height=80)
    
    line_height=50
    left_width=620
    text_size=25
    layout_box0_width=790
    item_value_box0 = Box(window, width=layout_box0_width, height=line_height)
    item_value_box = Box(item_value_box0, align="left", height="fill", width=left_width)
    item_value_instruction = Text(item_value_box, color="white", align="left",
                                  size=text_size,
                                  text="Select parcel value")
    item_value_selection = Combo(item_value_box, align="right",
                                 options=["up to £20", "up to £50", "up to £100", "up to £500",
                                          "up to £1000", "up to £2500"])
    item_value_selection.bg="white"
    item_value_selection.text_size=text_size-5
    
    desired_service_box0 = Box(window, width=layout_box0_width, height=line_height)
    desired_service_box = Box(desired_service_box0, align="left", height="fill",
                              width=left_width)
    desired_service_instruction = Text(desired_service_box, color="white", align="left",
                                       size=text_size,
                                       text="Select desired service:")
    desired_service_selection = Combo(desired_service_box, align="right",
                                      options=["First Class", "Second Class", "Tracked"])
    desired_service_selection.bg="white"
    desired_service_selection.text_size=text_size-5
    
    empty_box = Box(window, width="fill", height=20)
    
    info_box = Box(window, width=800, height=300)
    text_image = Picture(info_box, image="parcel_info.PNG", align="left",
                         height=300, width=360)
    text_box = Box(info_box, align="right", height="fill", width=390)
    form_text_size = 15
    TextBox_width = 25
    empty_line_height = 50
    empty_box0 = Box(text_box, width="fill", height=15)
    name = TextBox(text_box, width=TextBox_width)
    name.bg="white"
    name.text_size=form_text_size
    empty_box1 = Box(text_box, width="fill", height=empty_line_height)
    line = TextBox(text_box, width=TextBox_width)
    line.bg="white"
    line.text_size=form_text_size
    empty_box2 = Box(text_box, width="fill", height=empty_line_height)
    town = TextBox(text_box, width=TextBox_width)
    town.bg="white"
    town.text_size=form_text_size
    empty_box3 = Box(text_box, width="fill", height=empty_line_height)
    def enable_button():
        confirm_button.enable()
        global service
        global receiver
        global road
        global city
        global postcode
        service = desired_service_selection.value
        receiver = name.value
        road = line.value
        city = town.value
        postcode = code.value
    code = TextBox(text_box, width=TextBox_width, command=enable_button)
    code.bg="white"
    code.text_size=form_text_size
    def next_page():
        window.destroy()
        payment_method()
    button_box = Box(window, width=1000, height=55)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=1, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
    confirm_button.disable()
print_label = False
def payment_method():
    payment_in_use = fp.return_payment_in_use()
    if payment_in_use is False:
        fp.initiate_payment_check()
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    pay = Picture(window, image="pay.PNG", width=580, height=500)
    def next_step():
        info = Text(window, text="Payment cancelled...")
        def next_page():
            global print_label
            print_label = False
            window.destroy()
            close_door()
        window.after(3000, next_page)
    button_box = Box(window, width=1000, height=55)
    confirm_button = PushButton(button_box, text="CANCEL", align="right",
                                height=1, width=8, command=next_step)
    confirm_button.bg="white"
    confirm_button.text_size=25
    def next_page():
        payment_presented = fp.return_payment_presented()
        if payment_presented is True:
            global print_label
            print_label = True
            window.destroy()
            close_door()
    window.repeat(200, next_page)
def close_door():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    text_box = Box(window, align="left", width="fill", height=90)
    close = Text(text_box, text="Please take your parcel and close door...",
                           color="white", size=30)
    def delay():
        def next_step():
            fp.initiate_hall_sensor()
            def next_page():
                door_shut = fp.return_door_shut()
                if door_shut == 1:
                    if print_label is True:
                        window.destroy()
                        take_label()
                    elif print_label is False:
                        logo.show()
                        window.destroy()
                    fp.servo_lock()
            window.repeat(200, next_page)
        #next_step()
        window.repeat(5000, next_step)
    window.after(5000, delay)
def take_label():
    fp.label_creation(receiver,road,postcode,city,service)
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    text_box = Box(window, align="left", width="fill", height=50)
    take = Text(text_box, text="Please take your label...", color="white", size=30)
    def next_step():
        window.destroy()
        final_page()
    window.after(5000, next_step)
def final_page():
    # Gerand Ai cc.2022
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen("None")
    text_box = Box(window, align="left", width="fill", height=50)
    credit = Text(text_box, text="THANK YOU!",
                           color="white", size=30)
    def next_step():
        #app.destroy()
        logo.show()
        window.destroy()
    window.after(5000, next_step)
Grey=(127, 127, 127)
app = App(height=600, width=1024, bg=Grey)
app.set_full_screen("None")
title_box = Box(app, width="fill", height=80)
title = Text(title_box, text="WELCOME TO PARCEL LABEL DISPENSER",
             color="white", align="bottom", size=35)
button_box = Box(app, width="fill", height=300)
begin_button = PushButton(button_box, text="CLICK TO BEGIN", align="bottom",
                          height=3, width=15, command=dangerous_goods)
begin_button.bg="white"
begin_button.text_size=30
logo_box = Box(app, align="bottom", width="fill")
logo = Picture(logo_box, image="logo.png", align="right",
               width=290, height=190)
app.display()