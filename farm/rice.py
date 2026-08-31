from farm.crop import Crop

class Rice(Crop):
    def water(self):
        self.grains += 5

    def transplant(self):
        pass
