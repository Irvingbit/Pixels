
# models.py - Definición de clases para el Quiz
from dataclasses import dataclass, asdict
from typing import List, Dict
import random

@dataclass
class Question:
    id: int
    text: str
    options: List[str]
    correct: int  # index starting at 0
    category: str = ''
    difficulty: str = 'medium'

    def is_correct(self, choice_index: int) -> bool:
        return choice_index == self.correct

    def to_dict(self) -> Dict:
        return asdict(self)

class Quiz:
    def __init__(self, questions: List[Question] = None):
        self.questions = questions or []

    def add_question(self, q: Question):
        self.questions.append(q)

    def get_random_questions(self, n: int):
        qlist = self.questions.copy()
        random.shuffle(qlist)
        return qlist[:n] if n <= len(qlist) else qlist

    def total_questions(self):
        return len(self.questions)
