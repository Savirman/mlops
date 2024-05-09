import gradio as gr
from transformers import pipeline

classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)


def analyze_text(input_text):
    result = classifier(input_text)
    return result


interface = gr.Interface(
    fn=analyze_text,
    inputs=gr.Textbox(label="Введите предложение на английском языке", placeholder=""),
    outputs=gr.JSON(label="Результат"),
    title="Модель анализа текста"
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)