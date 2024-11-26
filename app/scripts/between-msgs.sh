#!/bin/bash

# Verificar se o número correto de argumentos foi passado
if [ $# -ne 3 ]; then
    echo "Error: comando inválido.
Para executar o script, utilize o seguinte comando:
$0 <caminho do arquivo> <mensagens_min> <mensagens_max>
"
    exit 1
fi

# Variáveis de entrada
file=$1
min_msgs=$2
max_msgs=$3


if ! [[ "$min_msgs" =~ ^[0-9]+$ ]]; then
    echo "Erro: 'mensagens_min' não é um número válido."
    exit 1
fi

if ! [[ "$max_msgs" =~ ^[0-9]+$ ]]; then
    echo "Erro: 'mensagens_max' não é um número válido."
    exit 1
fi

# Verificar se o arquivo existe
if [ ! -f "$file" ]; then
    echo "Erro: Arquivo '$file' não encontrado."
    exit 1
fi

# Filtrar os usuários na faixa de mensagens
result=$(awk -v min="$min_msgs" -v max="$max_msgs" '{
    msgs = $3 + 0;
    if (msgs >= min && msgs <= max) {
        print $0
    } 
}' "$file")

# Exibir o resultado

if [ -n "$result" ]; then
    echo "$result"
    exit 0
else
    echo "Erro: Não há usuários na faixa especificada."
    exit 0
fi
