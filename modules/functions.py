import whisper


class Whisper():

    def __init__(self):
        pass

    def check_extension(self, filename):
        if filename.endswith(".mp3") or filename.endswith(".wav") or filename.endswith(".mp4"):
            return True
        else:
            return False

    def to_text(self, audio, filename):
        try:
            if not self.check_extension(filename):
                return {"message": "Please upload an mp3 file"}
            model = whisper.load_model("base")
            result = model.transcribe(audio)
            return result
        except Exception as e:
            return {"message": str(e)}