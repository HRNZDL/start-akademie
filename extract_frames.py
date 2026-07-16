import cv2
import os

video_path = r'C:\Users\Harun\Desktop\üniversite kapi.mp4'
output_dir = r'c:\Users\Harun\Downloads\beautiful-websites-kit-dist\sites\start-akademie\assets\gate-frames'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

cap = cv2.VideoCapture(video_path)
frame_idx = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    # Resize to 1280x720 for optimal web delivery
    resized = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_AREA)
    
    # Save as webp with 80% quality
    out_path = os.path.join(output_dir, f'frame_{frame_idx:03d}.webp')
    cv2.imwrite(out_path, resized, [cv2.IMWRITE_WEBP_QUALITY, 80])
    
    if frame_idx % 20 == 0:
        print(f"Extracted frame {frame_idx}")
        
    frame_idx += 1

cap.release()
print(f"Successfully extracted {frame_idx} frames to {output_dir}")
