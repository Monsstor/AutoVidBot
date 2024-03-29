import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip, AudioFileClip, VideoFileClip
from moviepy.video.io.bindings import mplfig_to_npimage

def generate_audio_visualizer(video_path, audio_path, output_file, audio_fps=24, fps=24, window_size=1024):
    # Function to generate frames for video
    def make_frame(t):
        # Get audio data at time t
        audio_frame = audio.subclip(t, t+1) # Adjust the frame duration as needed
        audio_array = audio_frame.to_soundarray(fps=24000)
        audio_data = audio_array.mean(axis=1)
        
        # Calculate time index in the audio
        audio_index = int(t * audio_fps)
        
        # Define the time window for visualization (adjust this based on your preference)
        start_index = max(0, audio_index - window_size // 2)
        end_index = min(len(audio_data), audio_index + window_size // 2)
        
        # Take a slice of the audio for visualization
        audio_slice = audio_data[start_index:end_index]
        
        # Compute the visualistaion using matplotlib
        plt.figure(figsize=(2.4,2.4))
        plt.plot(audio_slice, color='blue')
        plt.axis('off')
        
        # Convert the plot to an image
        image = mplfig_to_npimage(plt.gcf())
        plt.close()
        
        return image

    # Load input video and audio files
    video = VideoFileClip(filename=video_path)
    audio = AudioFileClip(filename=audio_path)

    # Set video duration to the minimum of audio and video duration
    video_duration = min(video.duration, audio.duration)

    # Create the video clip
    audio_visualizer = VideoClip(make_frame, duration=video_duration)
    # Write the video to a file
    audio_visualizer.write_videofile(output_file, fps=fps)


# Example usage
video_path = "lssets\source video.mp4"
audio_path = "lssets\ludio1.wav"
output_file = "audio_visualizer1.mp4"

generate_audio_visualizer(video_path, audio_path, output_file)
