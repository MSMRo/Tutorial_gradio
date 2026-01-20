import gradio as gr

"""
INPUTS:
    gr.Textbox()
    gr.Number()
    gr.Slider(minimum=0, maximum=100)
    gr.Checkbox()
    gr.Dropdown(choices=["A", "B", "C"])
    gr.Image(type="numpy")
    gr.Audio(type="filepath")

OUTPUTS:
    gr.Textbox()
    gr.Label()
    gr.Image()
    gr.Audio()
    gr.JSON()

"""

def saludo(nombre):
    return f"Hola {nombre}, bienvenido a Gradio!"

demo = gr.Interface(
    fn=saludo,
    inputs=gr.Textbox(label="Ingresa tu nombre"),
    outputs=gr.Textbox(label="Saludo")
)

demo.launch()