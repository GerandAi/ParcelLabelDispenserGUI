from guizero import App, Text, PushButton, Picture, Box, Window, CheckBox, warn, Combo, TextBox
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
    code = TextBox(text_box, width=TextBox_width, command=enable_button)
    code.bg="white"
    code.text_size=form_text_size
    def next_page():
        app.destroy()
    button_box = Box(window, width=1000, height=55)
    confirm_button = PushButton(button_box, text="CONFIRM", align="right",
                                height=1, width=8, command=next_page)
    confirm_button.bg="white"
    confirm_button.text_size=25
    confirm_button.disable()

Grey = (127, 127, 127)
app = App(height=600, width=1024, bg=Grey)
app.set_full_screen()
entre_details()
app.display()