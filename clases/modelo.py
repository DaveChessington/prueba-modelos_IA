from openai import OpenAI
from google import genai
import api_keys as api

class ModeloOpenAI:
    def __init__(self):
        self.cliente=OpenAI(api_key=api.open_AI)

    def modeloSimple(self,pregunta):
        respuesta=self.cliente.chat.completions.create(model="gpt-4o-mini",
                            messages=[{'role':'user',
                             'content':pregunta}])
        print(respuesta.choices[0].message.content)

class ModeloGemini:
    def __init__(self):
        self.cliente=genai.Client(api_key=api.Gemini)

    def modeloSimple(self,pregunta):
        respuesta=self.cliente.models.generate_content(model="gemini-2.5-flash",contents=pregunta)
        print(respuesta.candidates[0].content.parts[0].text)

class ModeloGrok:
    def __init__(self):
        self.cliente=OpenAI(
            api_key=api.XAI,
            base_url="https://api.x.ai/v1")
    
    def modeloSimple(self,pregunta):
        respuesta=self.cliente.chat.completions.create(model="grok-code-fast-1",
                     messages=[{'role':'user',
                     'content':pregunta}])
        print(respuesta.choices[0].message.content)  
