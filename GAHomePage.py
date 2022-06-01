import time
from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn, Combo, TextBox
def dangerous_goods():
    logo.hide()
    def next_page():
        if check_yes.value == 1:
            logo.show()
            warn("Sorry...", "You cannot send dangerous goods through parcel postbox!")
            window.destroy()
        elif check_no.value == 1:
            window.destroy()
            packed_securely()
    def prevent_conflict():
        if check_yes.value == 1:
            check_no.disable()
        if check_no.value == 1:
            check_yes.disable()
        if check_yes.value == 0:
            check_no.enable()
        if check_no.value == 0:
            check_yes.enable()
    window = Window(app, height=600, width=1024, bg=Grey)
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
def packed_securely():
    def next_page():
        if check_yes.value == 1:
            window.destroy()
            check_debris()
        elif check_no.value == 1:
            logo.show()
            warn("Sorry...", "You cannot send dangerous goods through parcel postbox!")
            window.destroy()
    def prevent_conflict():
        if check_yes.value == 1:
            check_no.disable()
        if check_no.value == 1:
            check_yes.disable()
        if check_yes.value == 0:
            check_no.enable()
        if check_no.value == 0:
            check_yes.enable()
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="IS PARCEL TO BE SENT PACKAGED SECURELY?",
                 color="white", align="bottom", size=30)
    image = Picture(window, image="/home/pi/ga/packed_securely.PNG",
                    width=1000, height=350)
    answer_box = Box(window, width=300, height=50)
    yes = Text(answer_box, text="Yes ", align="left", color="white", size=22)
    check_yes = CheckBox(answer_box, align="left", command=prevent_conflict)
    check_no = CheckBox(answer_box, align="right", command=prevent_conflict)
    no = Text(answer_box, text="No ", align="right", color="white", size=22)
    button_box = Box(window, width=1000, height=50)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
def check_debris():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Please remove Debris from Enclosure",
                 color="white", align="bottom", size=30)
    image = Picture(window, image="/home/pi/ga/remove_debris.PNG",
                    width=830, height=420)
    debris = False
    if debris is False:
        window.update()
        time.sleep(3)
        window.destroy()
        input_parcel()
def input_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Place Parcel in Enclosure & Close Enclosure Door",
                 color="white", align="bottom", size=30)
    image_box = Box(window, width="fill", height=390)
    image = Picture(image_box, image="/home/pi/ga/input_parcel.PNG", align="bottom",
                    width=900, height=320)
    door_shut = True
    if door_shut is True:
        window.update()
        time.sleep(3)
        window.destroy()
        check_parcel()
def check_parcel():
    def change_image():
        if image.value == "/home/pi/ga/buffer0.PNG":
            image.value="/home/pi/ga/buffer1.PNG"
        elif image.value == "/home/pi/ga/buffer1.PNG":
            image.value="/home/pi/ga/buffer0.PNG"
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    title_box = Box(window, width="fill", height=90)
    title = Text(title_box, text="Please wait while we perform checks on the parcel ; )",
                 color="white", align="bottom", size=30)
    image_box = Box(window, width="fill", height=420)
    image = Picture(image_box, image="/home/pi/ga/buffer0.PNG", align="bottom",
                    width=390, height=390)
    image.repeat(500, change_image)
    def next_step():
        window.destroy()
        good_parcel()
    window.after(2000, next_step)
def good_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    correct_parcel = Text(window, text="                  We've done the checks!   ",
                          color="white", align="left", size=30)
    image = Picture(window, image="/home/pi/ga/right.PNG", align="left",
                    width=120, height=100)
    def next_step():
        window.destroy()
        enclosure_photo()
    window.after(1000, next_step)
def bad_parcel():
    window = Window(app, height=600, width=1024, bg=Grey)
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
        logo.show()
        window.destroy()
    window.after(5000, window_destroy)
def enclosure_photo():
    window = Window(app, height=600, width=1024, bg=Grey)
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
            window.destroy()
            entre_details()
        elif check_no.value == 1:
            logo.show()
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
def entre_details():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    
    top_space = Box(window, width="fill", height=10)
    
    line_height=50
    left_width=900
    text_size=22
    layout_box0_width=1000
    item_value_box0 = Box(window, width=layout_box0_width, height=line_height)
    item_value_box = Box(item_value_box0, align="left", height="fill", width=left_width)
    item_value_instruction = Text(item_value_box, color="white", align="left",
                                  size=text_size,
                                  text="PLEASE SELECT VALUE OF ITEM TO BE SENT")
    item_value_selection = Combo(item_value_box, align="right",
                                 options=["£20", "£50", "£100", "£500", "£1000", "£2500"])
    item_value_selection.bg="white"
    item_value_selection.text_size=text_size-5
    
    desired_service_box0 = Box(window, width=layout_box0_width, height=line_height)
    desired_service_box = Box(desired_service_box0, align="left", height="fill",
                              width=left_width)
    desired_service_instruction = Text(desired_service_box, color="white", align="left",
                                       size=text_size,
                                       text="PLEASE SELECT VALUE OF ITEM TO BE SENT")
    desired_service_selection = Combo(desired_service_box, align="right",
                                      options=["First Class", "Second Class", "Tracked"])
    desired_service_selection.bg="white"
    desired_service_selection.text_size=text_size-5
    
    empty_box = Box(window, width="fill", height=20)
    
    TextBox_width=25
    form_text_size=15
    empty_line_height=15
    postcode_from_instruction_box = Box(window, width=layout_box0_width, height=line_height-10)
    postcode_from_instruction = Text(postcode_from_instruction_box, color="white",
                                     text="PLEASE ENTER POSTCODE WHERE PARCEL IS BEING SENT FROM",
                                     align="left", size=text_size)
    postcode_from_form_box = Box(window, width=layout_box0_width, height=line_height-20)
    postcode_from_form = TextBox(postcode_from_form_box, align="left", width=TextBox_width)
    postcode_from_form.bg="white"
    postcode_from_form.text_size=form_text_size
    
    empty_line = Box(window, width="fill", height=empty_line_height)
    
    postcode_to_instruction_box = Box(window, width=layout_box0_width, height=line_height-10)
    postcode_to_instruction = Text(postcode_to_instruction_box, color="white",
                                     text="PLEASE ENTER POSTCODE WHERE PARCEL IS BEING SENT TO",
                                     align="left", size=text_size)
    postcode_to_form_box = Box(window, width=layout_box0_width, height=line_height-20)
    postcode_to_form = TextBox(postcode_to_form_box, align="left", width=TextBox_width)
    postcode_to_form.bg="white"
    postcode_to_form.text_size=form_text_size
    
    empty_line0 = Box(window, width="fill", height=empty_line_height)
    
    destination_town_instruction_box = Box(window, width=layout_box0_width, height=line_height-10)
    destination_town_instruction = Text(destination_town_instruction_box, color="white",
                                     text="PLEASE ENTER DESTINATION TOWN/CITY",
                                     align="left", size=text_size)
    destination_town_form_box = Box(window, width=layout_box0_width, height=line_height-20)
    destination_town_form = TextBox(destination_town_form_box, align="left", width=TextBox_width)
    destination_town_form.bg="white"
    destination_town_form.text_size=form_text_size
    
    empty_line1 = Box(window, width="fill", height=empty_line_height)
    
    destination_line1_instruction_box = Box(window, width=layout_box0_width, height=line_height-10)
    destination_line1_instruction = Text(destination_line1_instruction_box, color="white",
                                     text="PLEASE ENTER DESTINATION FIRST LINE OF ADDRESS",
                                     align="left", size=text_size)
    destination_line1_form_box = Box(window, width=layout_box0_width, height=line_height-20)
    destination_line1_form = TextBox(destination_line1_form_box, align="left", width=TextBox_width)
    destination_line1_form.bg="white"
    destination_line1_form.text_size=form_text_size
    
    empty_line2 = Box(window, width="fill", height=empty_line_height)
    
    recipients_name_instruction_box = Box(window, width=layout_box0_width, height=line_height-10)
    recipients_name_instruction = Text(recipients_name_instruction_box, color="white",
                                     text="PLEASE ENTER PARCEL RECIPIENTS NAME",
                                     align="left", size=text_size)
    recipients_name_form_box = Box(window, width=layout_box0_width, height=line_height-20)
    recipients_name_form = TextBox(recipients_name_form_box, align="left", width=TextBox_width)
    recipients_name_form.bg="white"
    recipients_name_form.text_size=form_text_size
    def next_page():
        window.destroy()
        payment_method()
    button_box = Box(window, width=1000, height=55)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
def payment_method():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    text_box = Box(window, align="left", width="fill", height=50)
    present_payment = Text(text_box, text="PLEASE PRESENT PAYMENT METHOD",
                           color="white", size=30)
    def next_step():
        window.destroy()
        close_door()
    window.after(2000, next_step)
def close_door():
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    text_box = Box(window, align="left", width="fill", height=90)
    take_label = Text(text_box, text="PLEASE TAKE DISPENSED LABEL",
                           color="white", size=30)
    shut_door = Text(text_box, text="AND CLOSE ENCLOSURE DOOR",
                           color="white", size=30)
    def next_step():
        window.destroy()
        final_page()
    window.after(3000, next_step)
def final_page():
    # Gerand Ai cc.2022
    window = Window(app, height=600, width=1024, bg=Grey)
    window.set_full_screen()
    text_box = Box(window, align="left", width="fill", height=50)
    credit = Text(text_box, text="THANK YOU!",
                           color="white", size=30)
    def next_step():
        app.destroy()
    window.after(2000, next_step)
Grey=(127, 127, 127)
app = App(height=600, width=1024, bg=Grey)
app.set_full_screen()
title_box = Box(app, width="fill", height=70)
title = Text(title_box, text="WELCOME TO PARCEL LABEL DISPENSER",
             color="white", align="bottom", size=35)
button_box = Box(app, width="fill", height=300)
begin_button = PushButton(button_box, text="CLICK TO BEGIN", align="bottom",
                          height=3, width=15, command=dangerous_goods)
begin_button.bg="white"
begin_button.text_size=30
logo_box = Box(app, align="bottom", width="fill")
logo = Picture(logo_box, image="/home/pi/ga/logo.png", align="right",
               width=290, height=190)
app.display()