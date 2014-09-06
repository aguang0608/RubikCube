import lib.ImageAnalysis
import Image

jpg = Image.open('./tmp/2014-09-06-18-16-21.jpg')

jpg.show()
for i in range(3):
    lib.ImageAnalysis.medianFiltering(jpg)
    jpg.show()
lib.ImageAnalysis.trans(jpg)
jpg.show()

