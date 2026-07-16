from PIL import Image
import os

def remove_background(input_path, output_path, bg_color='white', tolerance=30):
    try:
        img = Image.open(input_path).convert("RGBA")
        data = img.getdata()
        
        new_data = []
        for item in data:
            r, g, b, a = item
            if bg_color == 'white':
                # Remove white-ish pixels
                if r > 255 - tolerance and g > 255 - tolerance and b > 255 - tolerance:
                    new_data.append((r, g, b, 0))
                else:
                    new_data.append(item)
            elif bg_color == 'black':
                # Remove black-ish pixels
                if r < tolerance and g < tolerance and b < tolerance:
                    new_data.append((r, g, b, 0))
                else:
                    new_data.append(item)
                    
        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Success: {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

# logo-cream.jpg has a white background
remove_background("assets/logo-cream.jpg", "assets/logo-cream-alpha.png", bg_color="white", tolerance=50)

# logo-transparent.jpg has a black background
remove_background("assets/logo-transparent.jpg", "assets/logo-trans-alpha.png", bg_color="black", tolerance=50)
