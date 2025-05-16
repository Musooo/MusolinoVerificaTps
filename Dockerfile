# Usa un'immagine Python di base
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file nel container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta su cui gira Flask
EXPOSE 5000

# Comando per avviare l'app
CMD ["python", "app.py"]
