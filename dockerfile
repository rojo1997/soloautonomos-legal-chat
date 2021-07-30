FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

COPY requirements.txt /SoloAutonomosLegalChat/

WORKDIR /SoloAutonomosLegalChat

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt && \
    python3 -c "from transformers import pipeline; pipeline('question-answering', model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es', tokenizer = ('mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es', {'use_fast': False}))"

COPY . /SoloAutonomosLegalChat

EXPOSE 5000
CMD [ "python", "-u", "app/main.py" ]