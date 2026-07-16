import cv2
import numpy as np

def remove_bg_white(input_path, output_path):
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    if img is None:
        return
    img = img.astype(np.float32) / 255.0
    
    # Calculate luminance
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Alpha mask: white (1.0) -> alpha 0.0, anything darker than 0.7 -> alpha 1.0
    # Map [0.7, 0.98] -> [1.0, 0.0]
    alpha = np.clip((0.98 - gray) / (0.98 - 0.70), 0.0, 1.0)
    
    # Un-premultiply colors to remove the white halo
    # C_original = C_foreground * alpha + C_background * (1 - alpha)
    # C_foreground = (C_original - C_background * (1 - alpha)) / alpha
    # Background is white (1.0, 1.0, 1.0)
    
    bg = np.ones_like(img)
    # Avoid division by zero
    safe_alpha = np.where(alpha < 0.01, 1.0, alpha)
    safe_alpha = np.expand_dims(safe_alpha, axis=-1)
    
    foreground = (img - bg * (1.0 - safe_alpha)) / safe_alpha
    foreground = np.clip(foreground, 0.0, 1.0)
    
    # Combine back
    result = np.concatenate([foreground, np.expand_dims(alpha, axis=-1)], axis=-1)
    result = (result * 255).astype(np.uint8)
    
    cv2.imwrite(output_path, result)
    print(f"Saved {output_path}")

def remove_bg_black(input_path, output_path):
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)
    if img is None:
        return
    img = img.astype(np.float32) / 255.0
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Alpha mask: black (0.0) -> alpha 0.0, anything brighter than 0.3 -> alpha 1.0
    # Map [0.02, 0.30] -> [0.0, 1.0]
    alpha = np.clip((gray - 0.02) / (0.30 - 0.02), 0.0, 1.0)
    
    bg = np.zeros_like(img)
    safe_alpha = np.where(alpha < 0.01, 1.0, alpha)
    safe_alpha = np.expand_dims(safe_alpha, axis=-1)
    
    foreground = (img - bg * (1.0 - safe_alpha)) / safe_alpha
    foreground = np.clip(foreground, 0.0, 1.0)
    
    result = np.concatenate([foreground, np.expand_dims(alpha, axis=-1)], axis=-1)
    result = (result * 255).astype(np.uint8)
    
    cv2.imwrite(output_path, result)
    print(f"Saved {output_path}")

remove_bg_white("assets/logo-cream.jpg", "assets/logo-cream-perfect.png")
remove_bg_black("assets/logo-transparent.jpg", "assets/logo-trans-perfect.png")
