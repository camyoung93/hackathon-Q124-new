FROM python:3.11 as build
ADD main.py .
RUN pip install "arize-phoenix[evals]" arize packaging openai>=1.0.0
CMD ["python", "./main.py"]