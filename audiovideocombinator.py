from moviepy.editor import VideoFileClip, AudioFileClip

# Load video and audio files
video_path = "audio_visualizer.mp4"
audio_path = "lssets\ludio1.wav"

video_clip = VideoFileClip(video_path)
audio_clip = AudioFileClip(audio_path)

# Set the audio of the video clip to the loaded audio clip
video_clip = video_clip.set_audio(audio_clip)

# Write the combined video with audio to a new file
output_path = "combined_video.mp4"
video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
