from archivoFisico.Documento import Documento

class ArchivoFisicoRepository:
    def __init__(self):
        # Inicializar la colección de documentos físicos (Incapacidades)
        self.documentos = []

    def agregar_documento(self, documento):
        # Agregar un documento a la colección
        self.documentos.append(documento)

    def obtener_documento_por_id(self, documento_id):
        # Obtener un documento por su ID
        for documento in self.documentos:
            if documento.id == documento_id:
                return documento
        return None

    def eliminar_documento(self, documento):
        # Eliminar un documento de la colección
        self.documentos.remove(documento)
