from pathlib import Path

def get_path(dir_for, name):
    return Path("assets") / dir_for / f"{name}.png"

class Stage:

    """необхожимо подать текст окна, ассеты для фона и персоонажа, варианты ответа"""

    def __init__(self, info_stage):

        self.text = info_stage['text']
        self.bg = get_path('bg', info_stage['bg'])

        if info_stage['unit'] is not None:
            self.unit = get_path('units', info_stage['unit'])
            self.name_unit = info_stage['name_unit']
        else:
            self.name_unit = None
            self.unit = None

        self.scale_unit = info_stage['scale_unit']
        self.unit_offset_y = info_stage['unit_offset_y']
        self.unit_offset_x = info_stage['unit_offset_x']

        self.vars_return = [VarReturn(var) for var in info_stage['vars_return']]
        self.count_vars_return = len(self.vars_return)


class VarReturn:

    """необходимо подать текст и сцену, которую вызовет ответ."""

    def __init__(self, info_var):

        self.text = info_var['text']
        self.func = info_var['func']
        self.args = info_var['args']

