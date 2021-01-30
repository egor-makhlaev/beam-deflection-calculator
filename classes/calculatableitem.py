class CalculatableItem:
    system_units_weights = {
        "mm": 10**-3,
        "GPa": 10**9,
        "N": 10**0,
        "N/m": 1
    }

    def __init__(self, name, image_path, formula, parameters, constraints):
        self.name = name
        self.image_path = image_path
        self.formula = formula
        self.parameters = parameters
        self.constraints = constraints

    def update_parameters(self, new_parameters):
        for parameter in new_parameters.keys():
            value = new_parameters[parameter]
            parameter_name = self.parameters[parameter]["text"]

            try:
                value = int(value)
            except:
                # print(f"check 1: {parameter_name} is not an integer")
                value = None

            self.parameters[parameter].update({"value": value})

    def validate_parameters(self):
        parameters = self.parameters

        for parameter in parameters.keys():
            value = parameters[parameter]["value"]
            parameter_name = parameters[parameter]["text"]
            min = parameters[parameter]["min_value"]
            max = parameters[parameter]["max_value"]

            try:
                value = int(value)
            except:
                # print(f"check 2: {parameter_name} is not an integer")
                return False

            if value < min or value > max:
                # print(f"check 3: {parameter_name} is not in a valid range")
                return False

        for constraint in self.constraints:
            if not eval(constraint, self.get_simplified_parameters()):
                # print(f"check 4: constraint is broken: {constraint}")
                return False

        return True


    def get_simplified_parameters(self):
        parameters = self.parameters
        return {key: parameters[key]["value"] for key in parameters.keys()}

    def convert_to_system_units(self):
        parameters = self.parameters

        for key in parameters.keys():
            value = parameters[key]["value"]
            measurement = parameters[key]["measurement"]
            weight = CalculatableItem.system_units_weights[measurement]
            new_value = value * weight
            parameters[key].update({"value": new_value})

    def calculate(self, additional_parameters={}):
        result = None
        if self.validate_parameters():
            # TODO Check for missing parameter
            self.convert_to_system_units()
            params = self.get_simplified_parameters()
            params.update(additional_parameters)
            # print(f"check 5: {params}")
            result =  eval(self.formula, params)

        return result
