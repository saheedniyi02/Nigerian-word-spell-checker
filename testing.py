from typing import Text
from spell_checker.correct_text import correct_text

text="""I am a supxstar axn i trist the fhture to be braght for me,I live in agehe, lagos and i attend Unilog, unilog is Nigerie's largest and best unifersity.
I studdy mechunical enginnnring and I also write codes in phython and I develop machune learnang midels thot solve ruel word problqms.
    """
corrected_text=correct_text(text)

print(f"Initial_text:\n{text}")
print(f"Corrected_text:\n{corrected_text}")