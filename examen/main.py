
# main.py - Juego Educativo de Preguntas y Respuestas (CLI)
from models import Question, Quiz
from utils import load_questions_json, save_questions_json, export_results_csv
import os, time

QUESTIONS_FILE = 'questions.json'
RESULTS_FILE = 'results.csv'

def load_quiz():
    qlist = load_questions_json(QUESTIONS_FILE)
    quiz = Quiz(qlist)
    return quiz

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    print("\n=== Juego Educativo: Preguntas y Respuestas ===")
    print("1. Jugar (modo rápido)")
    print("2. Jugar (elegir número de preguntas)")
    print("3. Añadir pregunta")
    print("4. Listar preguntas")
    print("5. Exportar preguntas (JSON)")
    print("6. Exportar resultados (CSV)")
    print("0. Salir")

def ask_questions(questions):
    score = 0
    results = []
    for q in questions:
        print("\nPregunta:", q.text)
        for i, opt in enumerate(q.options, 1):
            print(f"  {i}. {opt}")
        while True:
            ans = input("Tu respuesta (número): ").strip()
            if ans.isdigit() and 1 <= int(ans) <= len(q.options):
                ans_i = int(ans) - 1
                break
            else:
                print("Entrada inválida. Ingresa el número de la opción.")
        correct = q.is_correct(ans_i)
        if correct:
            print("¡Correcto! ✅")
            score += 1
        else:
            print(f"Incorrecto ❌. Respuesta correcta: {q.options[q.correct]}")
        results.append({'question_id': q.id, 'question': q.text, 'your_answer': q.options[ans_i], 'correct_answer': q.options[q.correct], 'correct': correct})
        time.sleep(0.6)
    return score, results

def add_question_flow(quiz):
    print("\n--- Añadir nueva pregunta ---")
    try:
        nid = max([q.id for q in quiz.questions]) + 1 if quiz.questions else 1
    except Exception:
        nid = 1
    text = input("Enunciado: ").strip()
    opts = []
    for i in range(4):
        o = input(f"Opción {i+1}: ").strip()
        opts.append(o)
    while True:
        corr = input("Número de opción correcta (1-4): ").strip()
        if corr.isdigit() and 1 <= int(corr) <= 4:
            corr_i = int(corr) - 1
            break
        else:
            print("Valor inválido.")
    cat = input("Categoría (opcional): ").strip()
    diff = input("Dificultad (easy/medium/hard) [medium]: ").strip() or "medium"
    q = Question(id=nid, text=text, options=opts, correct=corr_i, category=cat, difficulty=diff)
    quiz.add_question(q)
    save_questions_json(quiz.questions, QUESTIONS_FILE)
    print("Pregunta añadida y guardada en", QUESTIONS_FILE)

def list_questions(quiz):
    print(f"\nTotal preguntas: {quiz.total_questions()}")
    for q in quiz.questions:
        print(f"{q.id}. {q.text} [{q.category}] (dif: {q.difficulty})")

def export_results(results):
    if export_results_csv(results, RESULTS_FILE):
        print("Resultados exportados a", RESULTS_FILE)
    else:
        print("No hay resultados para exportar.")

def main():
    quiz = load_quiz()
    last_results = []
    while True:
        print_menu()
        choice = input("Elija opción: ").strip()
        if choice == '1':
            n = min(5, quiz.total_questions()) or 0
            questions = quiz.get_random_questions(n)
            score, results = ask_questions(questions)
            print(f"\nResultado final: {score}/{len(questions)}")
            last_results = results
        elif choice == '2':
            total = quiz.total_questions()
            if total == 0:
                print("No hay preguntas cargadas. Añade algunas primero.")
                continue
            while True:
                qn = input(f"¿Cuántas preguntas quieres? (1-{total}): ").strip()
                if qn.isdigit() and 1 <= int(qn) <= total:
                    qn = int(qn); break
                else:
                    print("Valor inválido.")
            questions = quiz.get_random_questions(qn)
            score, results = ask_questions(questions)
            print(f"\nResultado final: {score}/{len(questions)}")
            last_results = results
        elif choice == '3':
            add_question_flow(quiz)
        elif choice == '4':
            list_questions(quiz)
        elif choice == '5':
            # save current questions file (already saved when adding)
            print("Preguntas guardadas en", QUESTIONS_FILE)
        elif choice == '6':
            if last_results:
                export_results(last_results)
            else:
                print("No hay resultados recientes. Juega primero para poder exportar.")
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == '__main__':
    main()
