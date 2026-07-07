import gradio as gr
import torch
from torchvision import models, transforms
from PIL import Image
import json
import urllib.request

# -----------------------------
# 1. Cargar etiquetas ImageNet
# -----------------------------
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = urllib.request.urlopen(LABELS_URL).read().decode("utf-8").splitlines()

# -----------------------------
# 2. Cargar modelo liviano (una sola vez)
# -----------------------------
model = models.mobilenet_v2(pretrained=True)
model.eval()

# -----------------------------
# 3. Transformaciones estándar
# -----------------------------
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# -----------------------------
# 4. Función de inferencia
# -----------------------------
def classify_image(img: Image.Image):
    img = preprocess(img).unsqueeze(0)  # (1, 3, 224, 224)

    with torch.no_grad():
        outputs = model(img)
        probs = torch.nn.functional.softmax(outputs[0], dim=0)

    top5_prob, top5_idx = torch.topk(probs, 5)

    results = {
        labels[idx]: float(prob)
        for idx, prob in zip(top5_idx, top5_prob)
    }

    return results

# -----------------------------
# 5. Interfaz Gradio
# -----------------------------
demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil", label="Imagen de entrada"),
    outputs=gr.Label(num_top_classes=5, label="Predicción"),
    title="Clasificación de Imágenes (MobileNetV2)",
    description="Demo liviana de clasificación de imágenes usando PyTorch + Gradio."
)

demo.launch()
