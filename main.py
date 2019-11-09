from PIL import Image, ImageFilter
from filters import Filters


fil = [ImageFilter.BLUR, ImageFilter.CONTOUR,
       ImageFilter.DETAIL, ImageFilter.EDGE_ENHANCE,
       ImageFilter.EMBOSS, ImageFilter.EDGE_ENHANCE_MORE,
       ImageFilter.FIND_EDGES, ImageFilter.SMOOTH,
       ImageFilter.SMOOTH_MORE, ImageFilter.SHARPEN]

file_name = "2sSzuXCn2SE.jpg"
size = (128, 128)
saved = "picture.jpeg"
new_image = Filters(file_name, size, saved)
new_image.filters(fil[1])
