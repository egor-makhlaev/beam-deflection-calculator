class Manager:
    @staticmethod
    def get_fields_information(calculatable_items):
        number_of_parameters_fields = 0
        parameters_description = {}

        for item in calculatable_items:
            for parameter in item.parameters.keys():
                if parameter not in parameters_description:
                    number_of_parameters_fields += 1
                    parameters_description.update({
                        parameter: (
                            item.parameters[parameter]["text"],
                            item.parameters[parameter]["measurement"]
                        )
                    })

        return number_of_parameters_fields, parameters_description

    def __init__(self, main_f, calculatable_items):
        self._items = calculatable_items
        self._current_active = None
        self._current_active_index = None

        listbox = main_f.get_listbox()
        listbox.fill([item.name for item in calculatable_items])
        listbox.set_callback_on_selection(self.manage_selection)
        self._listbox = listbox

        self._canvas = main_f.get_canvas()

        number, params_desc = Manager.get_fields_information(calculatable_items)
        fields = main_f.get_parameters_fields(number)
        # Parameters are appeared in alphabetical order
        for index, key in enumerate(sorted(params_desc.keys())):
            fields[index].set_parameter(key)
            fields[index].set_left_lb_text(params_desc[key][0])
            fields[index].set_right_lb_text(params_desc[key][1])
        self._parameters_fields = fields

    def manage_selection(self, event):
        selection = self._listbox.curselection()

        if selection:
            index_of_chosen_text = selection[0]
            self._current_active_index = index_of_chosen_text
            self._current_active = self._items[index_of_chosen_text]
            self.activate()

    def activate(self):
        self._canvas.set_image(self._current_active.image_path)

        for field in self._parameters_fields:
            field.clear_text()
            field.disable()

        for parameter in self._current_active.parameters.keys():
            for field in self._parameters_fields:
                if parameter == field.get_parameter():
                    field.activate()

    def is_active(self):
        return self._current_active is not None

    def get_entered_parameters(self):
        entered_parameters = {}

        for field in self._parameters_fields:
            parameter = field.get_parameter()
            if parameter in self._current_active.parameters:
                text = field.get_text()
                entered_parameters.update({parameter: text})

        return entered_parameters

    def get_current_active(self):
        return self._current_active

    def set_callback_on_text_change(self, callback):
        for field in self._parameters_fields:
            field.set_callback_on_text_change(callback)

    def calculate(self, additional_parameters):
        item = self._current_active
        result = None

        if item:
            new_parameters = self.get_entered_parameters()
            item.update_parameters(new_parameters)
            result = item.calculate(additional_parameters)

        return result

    def reset(self):
        self._current_active = None
        self._current_active_index = None
        self._listbox.reset()
        self._canvas.reset()

        for field in self._parameters_fields:
            field.clear_text()
            field.disable()
