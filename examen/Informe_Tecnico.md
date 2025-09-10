
# Informe técnico - Juego Educativo (Quiz)

## Problema y objetivo
Se busca aumentar la motivación de estudiantes mediante un juego de preguntas y respuestas que facilite la práctica y evaluación rápida.

## Arquitectura del software
- models.py: Question y Quiz (POO).
- utils.py: funciones para cargar/guardar preguntas (JSON) y exportar resultados (CSV).
- main.py: interfaz CLI con menú para jugar, añadir y listar preguntas.

## Características técnicas
- Uso de estructuras de control: condicionales y bucles para la lógica del juego.
- Modularidad: separación en módulos modelos, utilidades y ejecutable.
- POO: objetos Question con métodos y Quiz para gestión de preguntas.
- No se utiliza base de datos; persistencia opcional con archivo JSON 'questions.json'.

## Herramientas y editores IA usados
- VS Code + GitHub Copilot
- Replit (IA integrada)
- PyCharm + Tabnine

## Testeo
Se probó con 5 compañeros; se mejoró la presentación de opciones y se añadió feedback tras cada pregunta.

## Conclusión
El prototipo cumple con los requisitos del proyecto: es simple, extensible y adecuado para pruebas con usuarios. Siguientes pasos: interfaz web y temporizador por pregunta.
