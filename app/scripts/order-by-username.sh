#!/bin/bash

# Verificar se o número correto de argumentos foi passado
if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "Arquivo não passado por parâmetro.
Para executar o script, utilize o seguinte comando:
$0 <caminho do arquivo> [-desc]
"
    exit 1
fi

# Variáveis de entrada
file=$1
flag=$2

# Verificar se o arquivo existe
if [ ! -f "$file" ]; then
    echo "Arquivo '$file' não encontrado."
    exit 1
fi

# Determinar o tipo de ordenação
if [ -z "$flag" ]; then
    # Ordenação crescente (padrão)
    result=$(sort -k1,1 "$file")
elif [ "$flag" == "-desc" ]; then
    # Ordenação decrescente
    result=$(sort -rk1,1 "$file")
else
    echo "Flag desconhecida '$flag'. Use '-desc' para ordem decrescente ou nenhuma flag para ordem crescente."
    exit 1
fi

# Exibir o resultado
echo "$result"
