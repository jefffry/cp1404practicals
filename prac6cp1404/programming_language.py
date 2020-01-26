class ProgrammingLanguage:

    def __init__(self, field, typing, reflection, year):
        """ construct a ProgrammingLanguage from the value"""
        self.typing_type = typing
        self.has_reflection = reflection
        self.year = year
        self.field = field

    def __str__(self):
        """return string representation from ProgrammingLanguage"""
        return " {}, {} Typing, Reflection={}, First appeared in {} ".format(self.field, self.typing_type, self.has_reflection, self.year)

    def is_dynamic(self):
        """function for checking the type of the value is it dynamic or no"""
        return self.typing_type == "Dynamic"

    def get_name(self):
        """function for the name of the dynamic type"""
        return self.field
