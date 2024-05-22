import PIL.IcnsImagePlugin
import PIL.Image
import PIL.ImageChops

# List of ascii values to use
ASCII = ['@', '#', '&', '%', '?', '*', '+', ';', ':', ',', '.']

# Converts each pixel to greyscale
def greyscale(image):
    greyscale_img = image.convert('L')
    
    return greyscale_img

# Resizes image to new width
def resize(image, new_width = 100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_img = image.resize((new_width, new_height))
    
    return resized_img
    
# Converts pixels to a string of ASCII characters
def imageToAscii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII[pixel//25] for pixel in pixels])
    
    return characters
    

def main(new_width = 100):
    
    
    path = input('Enter a valid pathname to an image:\n')
    try:
        image = PIL.Image.open(path)
    except:
        print(path, 'is not a valid path name to open the image.')
    
    
    # Convert image to Ascii
    new_image = imageToAscii(greyscale(resize(image)))
    
    
    # Format the image
    pixel_count = len(new_image)
    ascii_img = '\n'.join(new_image[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    
    
    # Prints result
    print(ascii_img)
    
    
    # Saves current result to 'ascii_image.txt'
    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_img)
        
main()