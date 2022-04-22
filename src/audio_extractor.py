import bash_executor

class AudioExtractor:
    
    def __init__(self) -> None:
        self.bash_code_executor = bash_executor.BashExecutor()
    
    def extract_audio(self, input_video_filename, output_audio_filename):
        command = f"ffmpeg -loglevel error -y -i {input_video_filename} -vn -acodec copy {output_audio_filename}"
        
        output, error = self.bash_code_executor.executeCommand(command)

        if error:
            raise Exception(error)
        
        print(f"Successfully extracted the audio from {input_video_filename}")


def main():
    input_video_filename='../videos/3.mp4'
    output_audio_filename='../videos/output/3.aac'
    
    my_audio_extractor = AudioExtractor()    
    my_audio_extractor.extract_audio(input_video_filename, output_audio_filename)
    
    
if __name__ == '__main__':
    main()