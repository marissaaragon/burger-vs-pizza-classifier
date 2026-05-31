from fastai.vision.all import *
import gradio as gr

learn_inf = load_learner("/app/burger-vs-pizza.pkl")

def predict(img):
    result = learn_inf.predict(PILImage.create(img))
    return result[0]

gr.Interface(fn=predict, inputs=gr.Image(type="pil"), outputs=gr.Label()).launch()