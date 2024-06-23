import whisper
import modules.conexiones as c
import pyttsx3

db = "patitofeo"
tabla = "ventas"


class Whisper:
    def __init__(self):
        pass

    def check_extension(self, filename):
        if (
            filename.endswith(".mp3")
            or filename.endswith(".wav")
            or filename.endswith(".mp4")
        ):
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


def convert_text_to_audio(text):
    engine = pyttsx3.init()
    filename = "output.mp3"
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename


class Process:
    def __init__(self):
        self.queries = [
            (
                ["total", "ventas"],
                f"select sum(TotalVenta) as total from {tabla}",
            ),
            (
                ["cantidad", "productos"],
                f"select sum(cantidad) as total from {tabla}",
            ),
            (
                ["cliente", "mas", "compras"],
                f"""SELECT TOP 1 Cliente, COUNT(*) as Ventas
                FROM {tabla}
                GROUP BY Cliente
                ORDER BY Ventas ASC""",
            ),
            (
                ["producto", "mas", "vendido"],
                f"""SELECT TOP 1 Producto, SUM(Cantidad) as TotalVendido
                FROM {tabla}
                GROUP BY Producto
                ORDER BY TotalVendido DESC""",
            ),
            (
                ["producto", "menos", "vendido"],
                f"""SELECT TOP 1 Producto, SUM(Cantidad) as TotalVendido
                FROM {tabla}
                GROUP BY Producto
                ORDER BY TotalVendido ASC""",
            ),
        ]

    def select_query(self, text: str):
        text_set = set(text.lower().split())
        for keywords, query in self.queries:
            keywords_set = set(keyword.lower() for keyword in keywords)
            if keywords_set.issubset(text_set):
                product_name = " ".join(
                    keywords[:-1]
                )  # Join all keywords except the last one
                return query.format(product_name)
        return "Texto no reconocido"

    def execute_query(self, query):
        result = c.consulta(query)
        return result

    def send_results(self, results):
        # Implement send_results logic here
        pass
