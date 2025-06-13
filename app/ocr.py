from PIL import Image
import io
import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import easyocr

# Carregamento dos modelos
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
reader = easyocr.Reader(['en'])  # fallback

def process_image(image_bytes: bytes) -> str:
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values)
        text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return text.strip()
    except Exception as e:
        print(f"TrOCR falhou: {e}")
        # Fallback com EasyOCR
        try:
            result = reader.readtext(image_bytes)
            return " ".join([text for (_, text, _) in result])
        except Exception as fallback_error:
            return f"Erro ao processar imagem: {fallback_error}"