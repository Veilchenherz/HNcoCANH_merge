class Headers():

    def __init__(self, dimensions, spectrum_name, dim1 = "H", dim2 = "H", dim3 = "H", dim4 = "H"):
        self.top_header = (
             f"#\tNumber\tof\tdimensions\t{dimensions}\n"
             f"#FORMAT xeasy{dimensions}D\n"
        )
        self.dimension1 = dim1
        self.dimension2 = dim2
        self.dimension3 = dim3
        self.dimension4 = dim4
        self.dimensions = dimensions
        self.spectrum_name = spectrum_name

    def header_2d(self, spectrum_name):
        header = str(self.top_header
                  + f"#INAME\t1\t{self.dimension1}\n"
                  + f"#INAME\t2\t{self.dimension2}\n"
                  + f"#SPECTRUM {spectrum_name} {self.dimension1} {self.dimension2}\n"
                  )
        return header


    def header_3d(self, spectrum_name):
        header = str(self.top_header
                  + f"#INAME\t1\t{self.dimension1}\n"
                  + f"#INAME\t2\t{self.dimension2}\n"
                  + f"#INAME\t3\t{self.dimension3}\n"
                  + f"#SPECTRUM {spectrum_name} {self.dimension1} {self.dimension2} {self.dimension3}\n"
                  )
        return header


    def header_4d(self, spectrum_name):
        header = str(self.top_header
                  + f"#INAME\t1\t{self.dimension1}\n"
                  + f"#INAME\t2\t{self.dimension2}\n"
                  + f"#INAME\t3\t{self.dimension3}\n"
                  + f"#INAME\t4\t{self.dimension4}\n"
                  + f"#SPECTRUM {spectrum_name} {self.dimension1} {self.dimension2} {self.dimension3} {self.dimension4}\n"
                  )
        return header

    def create_header(self):

        if self.dimensions == 2:
            return self.header_2d(self.spectrum_name)
        elif self.dimensions == 3:
            return self.header_3d(self.spectrum_name)
        elif self.dimensions == 4:
            return self.header_4d(self.spectrum_name)