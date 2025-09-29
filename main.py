from clases.modelo import ModeloOpenAI,ModeloGrok,ModeloGemini
from clases.modelohistorial import ModeloHistorialOpenAI,ModeloHistorialGemini


def main():
    #ModeloOpenAI().modeloSimple()
    #ModeloGrok().modeloSimple()
    #ModeloGemini().modeloSimple()
    ModeloHistorialOpenAI().modeloHistorial(3)
    #ModeloHistorialGemini().modeloHistorial(3)

if "__main__"==__name__:
    main()