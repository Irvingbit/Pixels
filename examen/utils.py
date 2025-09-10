
# utils.py - helpers para carga y guardado de preguntas y resultados
import json, csv, os
from typing import List, Dict
from models import Question

def save_questions_json(questions: List[Question], filename: str):
    data = [q.to_dict() for q in questions]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def load_questions_json(filename: str):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    questions = []
    for d in data:
        q = Question(id=d.get('id'), text=d.get('text'), options=d.get('options'),
                     correct=int(d.get('correct')), category=d.get('category', ''), difficulty=d.get('difficulty', 'medium'))
        questions.append(q)
    return questions

def export_results_csv(results: List[Dict], filename: str):
    if not results:
        return False
    keys = results[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)
    return True
