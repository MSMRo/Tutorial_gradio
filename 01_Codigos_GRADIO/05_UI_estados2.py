import gradio as gr

def responder(mensaje, historial):
    respuesta = f"Eco: {mensaje}"
    #historial.append((mensaje, respuesta))
    historial.append({"role": "user", "content": mensaje})
    historial.append({"role": "assistant", "content": respuesta})
    return historial, "" #historial


with gr.Blocks() as demo:
    chat = gr.Chatbot()
    msg = gr.Textbox(label="Mensaje")
    historial = gr.State([])

    msg.submit(
        responder,
        inputs=[msg, historial],
        outputs=[chat, msg]
    )

demo.launch()
