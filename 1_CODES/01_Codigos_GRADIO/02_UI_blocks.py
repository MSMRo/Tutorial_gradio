import gradio as gr


def f1(x):
    return x.upper()

def f2(x):
    return x.lower()

with gr.Blocks() as demo:
    gr.Markdown("## Ejemplo de Gradio con Blocks")
    
    with gr.Row():
        with gr.Column():
            input_text = gr.Textbox(label="Ingresa tu texto aquí")
            btn_upper = gr.Button("Convertir a MAYÚSCULAS")
            btn_lower = gr.Button("Convertir a minúsculas")
            outputs=gr.Label(label="Resultado")
        
        with gr.Column():
            inputs=gr.Textbox(lines=4, label="Texto")
            inputs=gr.Slider(0, 1, step=0.01, label="Valor")
            output_upper = gr.Textbox(label="Texto en MAYÚSCULAS")
            output_lower = gr.Textbox(label="Texto en minúsculas")
    
    btn_upper.click(fn=f1, inputs=input_text, outputs=output_upper)
    btn_lower.click(fn=f2, inputs=input_text, outputs=output_lower)

demo.launch()