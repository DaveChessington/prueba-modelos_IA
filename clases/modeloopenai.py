from openai import OpenAI
from google import genai
import api_keys as api

class ModeloOpenAI:
    def __init__(self):
        pass

    def modeloSimple(self):
        cliente=OpenAI(api_key=api.open_AI)
        respuesta=cliente.chat.completions.create(model="gpt-4o-mini",
                            messages=[{'role':'user',
                             'content':'crea un resumen de la pelicula back to the future'}])
        print(respuesta.choices[0].message.content)

class ModeloGemini:
    def __init__(self):
        pass

    def modeloSimple(self):
        cliente=genai.Client(api_key=api.Gemini)
        respuesta=cliente.models.generate_content(model="gemini-2.5-flash",contents="por qué el cielo es azul?")
        print(respuesta.candidates[0].content.parts[0].text)

class ModeloGrok:
    def __init__(self):
        pass
    
    def modeloSimple(self):
        cliente=OpenAI(
            api_key=api.XAI,
            base_url="https://api.x.ai/v1")
        respuesta=cliente.chat.completions.create(model="grok-code-fast-1",
                     messages=[{'role':'user',
                     'content':'crea un resumen de la pelicula el hobbit'}])
        print(respuesta.choices[0].message.content)