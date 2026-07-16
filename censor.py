import glob
from PIL import Image, ImageDraw

def censor_frames():
    files = glob.glob('assets/frames/*.jpg')
    print(f"Found {len(files)} frames to censor.")
    
    for f in files:
        img = Image.open(f)
        draw = ImageDraw.Draw(img, 'RGBA')
        
        w, h = img.size
        
        # Meta AI is typically very large and on the bottom left and top right.
        # We will draw a black box that fades into the image (a gradient or just a solid black box with some opacity).
        # Since it's a night scene, a solid dark box that covers the corners will look like a shadow.
        
        # Bottom left watermark: covers roughly x: 0 to 450, y: h-150 to h
        for i in range(150):
            alpha = int(255 * (1 - (i/150)**2)) # fade out upwards
            draw.line([(0, h - i), (500, h - i)], fill=(0, 0, 0, alpha))
            
        # Top right watermark: covers roughly x: w-450 to w, y: 0 to 150
        for i in range(150):
            alpha = int(255 * (1 - (i/150)**2)) # fade out downwards
            draw.line([(w - 500, i), (w, i)], fill=(0, 0, 0, alpha))

        img = img.convert('RGB')
        img.save(f, quality=95)
        
    print("Done censoring all frames.")

if __name__ == '__main__':
    censor_frames()
