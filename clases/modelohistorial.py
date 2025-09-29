from openai import OpenAI
from google import genai
import api_keys as api

class ModeloHistorialOpenAI:
    def __init__(self):
        self.cliente=OpenAI(api_key=api.open_AI)
        self.historial=[{"role":"system","content":
                "Eres un sistema util y amigable"}]

    def modeloHistorial(self,n_historial="",n_preguntas="",historial=""):
        print("Chatbot de Open AI iniciado, escribe 'salir' para terminar la conversación")
        n_pregunta=0
        while True:
            if n_historial==n_pregunta:
                print("\nSe borró el historial\n")
                self.__init__()
            pregunta=input(f"{n_pregunta+1} Tu: ")

            if pregunta.lower()=="salir" or n_preguntas==n_pregunta:
                print("chatbot terminado")
                break
            self.historial.append({"role":"user","content":pregunta})

            respuesta=self.cliente.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.historial
            )
            respuesta_chatbot=respuesta.choices[0].message.content
            print(f"chatbot:{respuesta_chatbot}\n")
            self.historial.append({"role":"assistant", "content": respuesta_chatbot})
            n_pregunta+=1

class ModeloHistorialGemini:
    def __init__(self):
        self.cliente=genai.Client(api_key=api.Gemini)
        model_name = 'gemini-2.5-flash'
        instruccion = "Eres un sistema util y amigable"
        self.chat = self.cliente.chats.create(model=model_name,
                                              config=genai.types.GenerateContentConfig(
                # El equivalente al {"role": "system", "content": ...} de OpenAI
                system_instruction=instruccion 
            ))

    def modeloHistorial(self,n_historial="",n_preguntas=""):
        print("Chatbot de Gemini iniciado, escribe 'salir' para terminar la conversación")
        n_pregunta=0
        while True:
            if n_historial==n_pregunta:
                print("\nSe borró el historial\n")
                self.__init__()
            pregunta=input(f"{n_pregunta+1} Tu:")

            if pregunta.lower()=="salir" or n_preguntas==n_pregunta:
                print("chatbot terminado")
                break

            respuesta_chatbot=self.chat.send_message(message=pregunta)

            print(f"chatbot:{respuesta_chatbot.text}\n")
            n_pregunta+=1
