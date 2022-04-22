import bashExecutor

class VideoAudioMerger:
    def __init__(self) -> None:
        self.bash_code_executor = bashExecutor.BashExecutor()

    def merge_video_and_audio(self, input_video_filename, input_audio_filename, output_video_filename):
        # Understanding flags:
        # -loglevel: to print only errors to stderr (source: https://stackoverflow.com/questions/35169650/differentiate-between-error-and-standard-terminal-log-with-ffmpeg-nodejs)
        # -y: accept overwrite automatically
        command = f"ffmpeg -loglevel error -y -i {input_video_filename} -i {input_audio_filename} -c:a copy {output_video_filename}"
        
        output, error = self.bash_code_executor.executeCommand(command)

        print(output)
        if error:
            raise Exception(error)
        
        print(f"Successfully merge the video {input_video_filename} and audio {input_audio_filename}")


def main():
    input_video_filename='../videos/output/output.avi'
    input_audio_filename='../videos/output/3.aac'
    output_video_filename='../videos/output/output_video_audio.mp4'
    
    my_video_merger = VideoAudioMerger()
    
    my_video_merger.merge_video_and_audio(input_video_filename, input_audio_filename, output_video_filename)
    
if __name__ == "__main__":
    main()
    