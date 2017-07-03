class Map(object):
    #initialisation
    def __init__(self, name="None", description="None", sizeX=10, sizeY=10):
        self.name = name
        self.description = description
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.data = []
        for y in range(sizeY):
            row = []
            for x in range(sizeX):
                row.append("")
            self.data.append(row)
    #cell manipulating
    def update(self, coordX, coordY, value=""):
        self.data[coordY-1][coordX-1] = value
    #statistics
    def total(self):
        count = 0
        for y in self.data:
            for x in y:
                if x != "":
                    count += 1
        return "Total locations: " + str(count)
    def locations(self):
        locations = []
        for y in self.data:
            for x in y:
                if x != "":
                    locations.append(x)
        locations = list(set(locations))
        show = ""
        for location in range(len(locations)):
            if location == (len(locations) - 1):
                show += locations[location]
            else:
                show += locations[location] + ", "
        return "Locations: " + show
    #representation
    def __str__(self):
        return self.name + ": " + self.description
    def location(self, coordX, coordY):
        return "The location at x: " + str(coordX) + ", y: " + str(coordY) + " is the " + self.data[coordY-1][coordX-1]
    def show(self, mode="B"):
        if mode == "Plain" or mode == "P":
            show = ""
            for y in self.data:
                row = ""
                for x in y:
                    if x == "":
                        row += " "
                    else:
                        row += "."
                show += row + "\n"
            return show
        elif mode == "Border" or mode == "B":
            show = "+"
            for x in range(self.sizeX - 2):
                show += "-"
            show += "+\n"
            for y in self.data:
                row = "|"
                for x in y:
                    if x == "":
                        row += " "
                    else:
                        row += "."
                show += row + "|\n"
            show += "+"
            for x in range(self.sizeX - 2):
                show += "-"
            show += "+\n"
            return show
        elif mode == "Grid" or mode == "G":
            show = "+"
            for x in range(self.sizeX - 2):
                show += "-+"
            show += "\n"
            for y in self.data:
                row = ""
                for x in y:
                    if x == "":
                        row += "| "
                    else:
                        row += "|."
                show += row + "|\n"
                show += "+"
                for x in range(self.sizeX - 2):
                    show += "-+"
                show += "\n"
            return show
