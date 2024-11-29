#!/bin/bash

if [ $# -lt 1 ]  || [ $# -gt 2 ]; then
    echo "Arquivo não passado por parâmetro.
Para executar o script, utilize o seguinte comando:
$0 <caminho do arquivo> [-min]
"
    exit 1
fi

file=$1
flag=$2

if [ ! -f "$file" ]; then
    echo "Arquivo '$file' não encontrado."
    exit 1
fi

# Determinar se é para buscar o maior ou menor size
if [[ -n "$flag" ]] && [[ "$flag" == -* ]]; then
    if [[ "$flag" == "-min" ]]; then
        # Encontrar a linha com o menor tamanho (size)
        result=$(awk '{size = substr($0, length($0) - 8, 9); if (min_size == "" || size < min_size) { min_size = size; line = $0 }} END {print line}' "$file")
        mode="menor"
    else
        echo "Flag desconhecida '$flag'. Use apenas '-min' para buscar o menor size."
        exit 1
    fi
else
    # Encontrar a linha com o maior tamanho (size)
    result=$(awk '{size = substr($0, length($0) - 8, 9); if (size > max_size) { max_size = size; line = $0 }} END {print line}' "$file")
    mode="maior"
fi

# Exibir o resultado
echo "$result"
exit 0
