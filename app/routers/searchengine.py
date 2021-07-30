from transformers import pipeline
from fastapi import APIRouter, Query
import unidecode

nlp = pipeline(
    'question-answering', 
    model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',
    tokenizer = (
        'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es',  
        {"use_fast": False}
    ),
    device = 0
)

file = open('app/data/Ley de Arrendamientos Urbanos.txt', mode = 'r')
context = unidecode.unidecode(file.read().lower())
file.close()

router = APIRouter()

@router.get("/gptneo")
def get_gptneo(
    question: str = Query("¿La fianza arrendaticia mantiene su carácter obligatorio?")
):
    return nlp(
        {
            'question': question,
            'context': context
        }
    )