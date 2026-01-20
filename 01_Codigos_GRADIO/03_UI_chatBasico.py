import gradio as gr

def responder(mensaje, historial):
    historial = historial or []
    respuesta = f"Eco: {mensaje}"
    historial.append({"role": "user", "content": mensaje})
    historial.append({"role": "assistant", "content": respuesta})
    return historial, ""

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Mensaje")
    btn = gr.Button("Enviar")

    btn.click(responder, inputs=[msg, chatbot], outputs=[chatbot, msg])

demo.launch()

