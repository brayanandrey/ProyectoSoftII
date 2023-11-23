from Estrategia import Estrategia

class TranscriptorEPS(Estrategia):
    def transcribir(self, incapacidad):
        print(f"Transcribiendo incapacidad para EPS: {incapacidad.tipo}")