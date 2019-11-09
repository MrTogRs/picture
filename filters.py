from PIL import Image, ImageFilter


class Filters:

    def __init__(self, file_name, size, saved):
        self.file_name = file_name
        self.size = size
        self.saved = saved

    def open(self):
        global myimage
        myimage = Image.open(self.file_name)
        myimage.load()

    def mini(self):
        Filters.open(self)
        myimage.thumbnail(self.size)
        myimage.save(self.saved)
        myimage.show()

    def filters(self, fil):
        Filters.open(self)
        fil_image = myimage.filter(fil)
        fil_image.save(self.saved)
        fil_image.show()



