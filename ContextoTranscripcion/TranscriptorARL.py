from Estrategia import Estrategia

class TranscriptorARL(Estrategia):
    def transcribir(self, incapacidad):
        print(f"Transcribiendo incapacidad para ARL: {incapacidad.tipo}")