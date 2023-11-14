import colorsys

from PIL import Image


RGB_SCALE = 255
CMYK_SCALE = 100

# Create a function to convert RGB to HSV
def rgb_to_hsv(rgb):
    r, g, b = rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return int(h * 360), int(s * 100), int(v * 100)

def rgb_to_hsv_colorsys(image: Image, area_to_edit: list) -> Image.Image:
    # image = Image.open(input_img)

    # Convert the image to RGB mode if it's not already
    image = image.convert('RGB')

    # Create a new image with HSV colors
    hsv_image = Image.new('HSV', image.size)
    for x in range(image.width):
        for y in range(image.height):
            rgb_pixel = image.getpixel((x, y))

            # if (x, y) not in area_to_edit:
                # hsv_image.putpixel((x, y), rgb_pixel)
                # continue

            hsv_pixel = rgb_to_hsv(rgb_pixel)
            hsv_image.putpixel((x, y), hsv_pixel)

    # Convert the HSV image back to RGB
    rgb_image = hsv_image.convert('RGB')
    # rgb_image.save('backend/imgs/hsv.png')

    # replace part of input image with converted image
    for x, y in area_to_edit:
        image.putpixel((x, y), rgb_image.getpixel((x, y)))

    return image


def rgb_to_cmyk(r,g,b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, CMYK_SCALE
    
    k = 1 - max(r, g, b) / RGB_SCALE

    # rgb [0,255] -> cmy [0,1]
    c = (1 - r / RGB_SCALE - k) / (1 - k)
    m = (1 - g / RGB_SCALE - k) / (1 - k)
    y = (1 - b / RGB_SCALE - k) / (1 - k)

    # rescale to the range [0,CMYK_SCALE]
    return round(c * CMYK_SCALE), round(m * CMYK_SCALE), round(y * CMYK_SCALE), round(k * CMYK_SCALE)


def rgb_to_cmyk_colorsys(image: Image, area_to_edit: list) -> Image.Image:
    # image = Image.open(input_img)

    # Convert the image to RGB mode if it's not already
    image = image.convert('RGB')

    # Create a new image with CMYK colors
    cmyk_image = Image.new('CMYK', image.size)

    for x in range(image.width):
        for y in range(image.height):
            # Get the RGB pixel value
            rgb_pixel = image.getpixel((x, y))

            # if (x, y) not in area_to_edit:
                # cmyk_image.putpixel((x, y), rgb_pixel)
                # continue

            cmyk_pixel = rgb_to_cmyk(*rgb_pixel)
            # Set the CMYK pixel in the new image
            cmyk_image.putpixel((x, y), cmyk_pixel)

    # Convert the HSV image back to RGB
    rgb_image = cmyk_image.convert('RGB')

    # replace part of input image with converted image
    for x, y in area_to_edit:
        image.putpixel((x, y), rgb_image.getpixel((x, y)))
    # rgb_image.save('imgs/cmyk1.png')

    return image


def change_image_sat_and_brightness(img: Image, saturation: int, brightness: int, area_to_edit: list) -> Image.Image:

    img_hsv = img.convert("HSV")

    # Separate channels
    h, s, v = img_hsv.split()

    # blue_pixels = [(h, s, v) if h >= 100 and h <= 150 else (h, s, v) for h, s, v in zip(h.getdata(), s.getdata(), v.getdata())]
    # s = s.point(lambda i: i * 5 if i >= 0 and i <= 250 else i)
    
    result = [
        (h, s * saturation / 50, v * brightness / 50) if h >= 130 and h <= 220 else (h, s, v)
        for h, s, v in zip(h.getdata(), s.getdata(), v.getdata())
    ]

    h.putdata([pixel[0] for pixel in result])
    s.putdata([int(pixel[1]) for pixel in result])
    v.putdata([pixel[2] for pixel in result])

    # Merge the channels back
    img_hsv = Image.merge("HSV", (h, s, v))

    # Convert back to RGB
    img_rgb = img_hsv.convert("RGB")

    # replace part of input image with converted image
    for x, y in area_to_edit:
        img.putpixel((x, y), img_rgb.getpixel((x, y)))

    # Save the modified image
    # img_rgb.save("backend/imgs/modified.jpg")
    return img


if __name__ == '__main__':
    change_image_sat_and_brightness(rgb_to_hsv_colorsys('backend/imgs/girl.jpg'), 0, 0)