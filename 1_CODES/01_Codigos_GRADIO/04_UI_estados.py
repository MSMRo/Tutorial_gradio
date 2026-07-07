import gradio as gr

def incrementar(estado):
    estado += 1
    return estado, estado

with gr.Blocks() as demo:
    contador = gr.State(0)
    salida = gr.Number(label="Contador")
    boton = gr.Button("Sumar +1")

    boton.click(
        fn=incrementar,
        inputs=contador,
        outputs=[salida, contador]
    )

demo.launch()
