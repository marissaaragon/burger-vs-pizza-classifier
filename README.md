# Burger vs Pizza Classifier

A deep learning image classifier that predicts whether an image is a burger or pizza.

## How it works
Images were downloaded from DuckDuckGo and used to train a ResNet18 model with fastai. 
The app is built with Gradio and deployed on Hugging Face Spaces.

## Try it live
[Click here to try the app](https://huggingface.co/spaces/marissaaragon/burger-vs-pizza)

## Built with
- fastai
- Gradio
- Hugging Face Spaces

## Usage
Upload an image of a burger or pizza and the model will predict which one it is.
The model was only trained on burgers and pizzas, so other foods may give unexpected results.
