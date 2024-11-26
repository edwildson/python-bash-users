# Use uma imagem base oficial do Python
# FROM demisto/fastapi:0.115.4.116237
FROM python:3.12.7-alpine3.19

# Defina o diretório de trabalho
ENV PYTHONPATH="/http"
WORKDIR /http
RUN pwd
RUN cd /http

# Adiciona o bash ao container
RUN apk add --no-cache bash

# Copie os arquivos de requisitos
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código da aplicação
COPY . .


RUN ls -la

# Certifique-se de que o diretório tem permissões corretas
RUN mkdir -p ./app/tmp/files && \
    chmod -R 755 ./app/tmp/files && \
    chown -R 1000 ./app/tmp/files

# Exponha a porta que a aplicação irá rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]