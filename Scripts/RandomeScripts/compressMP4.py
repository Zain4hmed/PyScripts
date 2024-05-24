import os
import subprocess

def get_file_size(file_path):
    # Get size of file in bytes
    return os.path.getsize(file_path)

def compress_videos(input_dir, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get a list of all .mp4 files in the input directory
    video_files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f)) and f.endswith('.mp4')]
    
    # Compress each video file
    for video_file in video_files:
        input_file_path = os.path.join(input_dir, video_file)
        output_file_path = os.path.join(output_dir, video_file)
        
        # Get size of input file
        input_size = get_file_size(input_file_path)
        
        # Run ffmpeg command to compress the video
        subprocess.run(['ffmpeg', '-i', input_file_path, '-vf', 'scale=1280:-2', '-c:a', 'aac', '-b:a', '128k', output_file_path])
        
        # Get size of output file
        output_size = get_file_size(output_file_path)
        
        # Calculate compression percentage
        compression_percentage = ((input_size - output_size) / input_size) * 100 if input_size > 0 else 0
        
        print(f"Video: {video_file}")
        print(f"Before compression size: {input_size} bytes")
        print(f"After compression size: {output_size} bytes")
        print(f"Compression percentage: {compression_percentage:.2f}%\n")

# Input and output directories
input_dir = r'D:\uncompressed'
output_dir = r'D:\compressed'

# Compress videos
compress_videos(input_dir, output_dir)
