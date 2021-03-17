# numpy package (sains komputasi machine learning dan ai)
# Pil/pillow (paackage untuk menampilkan gambar)

import numpy as np
from PIL import Image
a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])
gambar = Image.open("gam.jpg")

print("Formatnya : " + gambar.format)
print("Ukurannya : " + str(gambar.size))
gambar.show()
print(a+b)