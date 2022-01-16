#pip install captcha
from captcha.image import ImageCaptcha
import random2
import string

image = ImageCaptcha(width = 280, height = 98)

def captcha_generate():
    all_char = string.ascii_letters + string.digits
    capt = ''
    for char in range(6):
        rand_char = random2.choice(all_char)
        capt += rand_char
    return capt

captcha_text = captcha_generate()
data = image.generate(captcha_text)
image.write(captcha_text, 'CAPTCHA.png')