import customtkinter as ctk
import tkinter

class CustClr():

    def __init__(self, 
                 Clr_master,
                 Clr_table_row,
                 Clr_table_column,
                 Clr_number=None, 
                 Clr_name=None, 
                 Clr_hex=None, 
                 Clr_switch=None,
                 name_entry=None,
                 hex_entry=None,
                 switch_var=None):
        
        self.Clr_number = Clr_number
        self.Clr_name = Clr_name
        self.Clr_hex = Clr_hex
        self.Clr_switch = Clr_switch
        self.Clr_master = Clr_master
        self.name_entry = name_entry
        self.hex_entry = hex_entry
        Clr_table_row = Clr_table_row
        Clr_table_column = Clr_table_column
        self.switch_var = switch_var
        self.color_fields = []
        self.hex_entry_fields = []
        self.switch_vars = []
        self.name_entry_fields = []

    def CustClr_Widget(self, Clr_master, Clr_table_row, Clr_table_column):
        
        Clr_widget_base = ctk.CTkFrame(master=Clr_master,
                                       width=70,
                                       height=83, 
                                       corner_radius=0, 
                                       border_width=0, 
                                       fg_color="#181818")
        Clr_widget_base.grid(row=Clr_table_row, column=Clr_table_column, padx=2, pady=5)

        self.name_entry = ctk.CTkEntry(master=Clr_widget_base, 
                                  placeholder_text=f"Color name", 
                                  font=("Roboto", 10), 
                                  width=80, 
                                  height=20, 
                                  corner_radius=0, 
                                  border_width=0, 
                                  fg_color="#141414")
        self.name_entry.pack(pady=2)
        self.name_entry_fields.append(self.name_entry)

        def switch_event():
            print("switch toggled, current value:", self.switch_var.get())

        self.switch_var = ctk.StringVar(value="off")
        switch = ctk.CTkSwitch(Clr_widget_base, 
                                text=" ",
                                height=10,
                                width=20,
                                switch_width=20,
                                switch_height=10, 
                                command=switch_event,
                                variable=self.switch_var,
                                onvalue="on", 
                                progress_color="#76AE22",
                                offvalue="off")
        switch.pack(anchor="center")
        self.switch_vars.append(self.switch_var)

        color_field = ctk.CTkFrame(master=Clr_widget_base, 
                                   width=20, 
                                   height=20, 
                                   corner_radius=4, 
                                   border_color="#6D6D6D", 
                                   fg_color="#1f1f1f", 
                                   border_width=1)
        color_field.pack(anchor="center")
        self.color_fields.append(color_field)

        def limit_characters(entry, limit):
            value = entry.get()
            if len(value) > limit:
                entry.set(value[:limit])

        text_var = ctk.StringVar()
        self.hex_entry = ctk.CTkEntry(master=Clr_widget_base, 
                                 placeholder_text="HEX-Value", 
                                 font=("Roboto", 10),
                                 textvariable=text_var, 
                                 width=70, 
                                 height=15, 
                                 corner_radius=0, 
                                 border_width=0, 
                                 fg_color="#141414")
        self.hex_entry.pack(pady=5)
        self.hex_entry_fields.append(self.hex_entry)

        character_limit = 6
        text_var.trace_add("write", lambda *args: limit_characters(text_var, character_limit))

        def update_color_field(color_field, hex_value):
            if not hex_value.startswith("#"):
                hex_value = "#" + hex_value
            try:
                if len(hex_value) == 7:
                    color_field.configure(fg_color=hex_value)
                else:
                    raise ValueError("Invalid Hex Value")
            except ValueError as e:
                print(e)

        def on_hex_entry_confirm(color_field, hex_entry):
            hex_value = hex_entry.get()
            update_color_field(color_field, hex_value)

        def create_lambda(color_field, hex_entry):
            return lambda event: on_hex_entry_confirm(color_field, hex_entry)
        
        self.hex_entry.bind("<Return>", create_lambda(color_field, self.hex_entry))

        return Clr_widget_base

    def update_color_field_xml(self, Clr_hex):

        Clr_val = Clr_hex[1:]

        for color_field in self.color_fields:
            color_field.configure(fg_color=Clr_hex)

        for hex_entry in self.hex_entry_fields:
            hex_entry.insert(0, Clr_val)

    def update_color_name_field_xml(self, Clr_name):

        for name_entry in self.name_entry_fields:
            name_entry.insert(0, Clr_name)

    def update_switches(self, switch_states):

        for switch_var in self.switch_vars:
            switch_var.set(switch_states)

    def build_name_string(self):
        name = self.name_entry.get()
        return name

    def build_hex_string(self):
        hex_value = self.hex_entry.get()
        return hex_value
    
    def clear_all_CustClr(self):
        base_color = "#181818"
        base_hex = ""
        base_name = ""
        base_switch_state = "off"

        for color_field, hex_entry, name_entry, switch_var in zip(self.color_fields, self.hex_entry_fields, self.name_entry_fields, self.switch_vars):
            color_field.configure(fg_color=base_color)
            hex_entry.delete(0, tkinter.END)
            hex_entry.insert(0, base_hex)
            name_entry.delete(0, tkinter.END)
            name_entry.insert(0, base_name)
            switch_var.set(base_switch_state)

    def get_switch_status(self):
        for var in self.switch_vars:
            print(var.get())