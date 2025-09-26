from clases.modeloopenai import ModeloOpenAI,ModeloGrok,ModeloGemini

def main():
    ModeloOpenAI().modeloSimple()
    #ModeloGrok().modeloSimple()
    ModeloGemini().modeloSimple()

if "__main__"==__name__:
    main()