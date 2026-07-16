import { execFileSync } from 'child_process';
import ffmpegPath from 'ffmpeg-static';
import fs from 'fs';
import path from 'path';

const inputVideo = path.join(process.cwd(), 'assets', 'gate-transition.mp4');
const outputDir = path.join(process.cwd(), 'assets', 'frames');

// Create output directory if it doesn't exist
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
} else {
  // clear old frames
  fs.readdirSync(outputDir).forEach(f => fs.unlinkSync(path.join(outputDir, f)));
}

console.log(`Extracting frames using ffmpeg at: ${ffmpegPath}`);
console.log(`Input: ${inputVideo}`);
console.log(`Output Directory: ${outputDir}`);

try {
  // Extract frames at 30 fps, scale to width 1920 to keep size reasonable, quality 2
  execFileSync(ffmpegPath, [
    '-i', inputVideo,
    '-vf', 'fps=24,scale=1920:-1',
    '-q:v', '2',
    path.join(outputDir, 'frame-%04d.jpg')
  ], { stdio: 'inherit' });
  console.log('Frame extraction complete.');
} catch (error) {
  console.error('Failed to extract frames:', error.message);
  process.exit(1);
}
