from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn, Combo, TextBox
def entre_details():
    window = Window(app, height=600, width=1024, bg="Grey")
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
    item_value_selection.text_size=text_size-10
    
    desired_service_box0 = Box(window, width=layout_box0_width, height=line_height)
    desired_service_box = Box(desired_service_box0, align="left", height="fill",
                              width=left_width)
    desired_service_instruction = Text(desired_service_box, color="white", align="left",
                                       size=text_size,
                                       text="PLEASE SELECT VALUE OF ITEM TO BE SENT")
    desired_service_selection = Combo(desired_service_box, align="right",
                                      options=["First Class", "Second Class", "Tracked"])
    desired_service_selection.bg="white"
    desired_service_selection.text_size=text_size-10
    
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
        app.destroy()
    button_box = Box(window, width=1000, height=55)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=2, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25

app = App(height=600, width=1024, bg="Grey")
app.set_full_screen()
title_box = Box(app, width="fill", height=100)
title = Text(title_box, text="WELCOME TO PARCEL LABEL DISPENSER",
             color="white", align="bottom", size=35)
button_box = Box(app, width="fill", height=280)
begin_button = PushButton(button_box, text="CLICK TO BEGIN", align="bottom",
                          height=3, width=15, command=entre_details)
begin_button.bg="white"
begin_button.text_size=30
logo_box = Box(app, align="bottom", width="fill")
logo = Picture(logo_box, image="/home/pi/ga/logo.png", align="right",
               width=290, height=190)
app.display()