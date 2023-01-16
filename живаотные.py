class Annimals:
    def __init__(self, name, vid="нету информации про вид", zv="Э"):
        if name == "Ворона"or"ворона":
            zv = "Кар"
            self.zv = zv
        elif name == "Курица"or"курица":
            zv = "ko-ко-ko"
            self.zv = zv
vorona = Annimals("ворона")
print(vorona.zv)