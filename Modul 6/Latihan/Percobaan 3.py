from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
image = Image.open(
    "C:\\Users\\HP Probook\\Modul 6 latihan\\Logo\\Hero.jpg"
)

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer_brightness = ImageEnhance.Brightness(image)
brightened_image = enhancer_brightness.enhance(1.5)

enhancer_contrast = ImageEnhance.Contrast(brightened_image)
final_image = enhancer_contrast.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan
final_image.show()
