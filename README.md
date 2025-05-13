
# Investe.AI - Simulação Automatizada com Ações da Petrobras (PETR4)

Este projeto simula uma estratégia de trading simples baseada em regras, utilizando dados simulados da ação PETR4 (Petrobras). A proposta foi desenvolvida como parte do desafio Investe.AI, sem uso de internet ou bibliotecas externas como `gym`, apenas com Python puro e bibliotecas padrão de análise de dados.

## Tecnologias Utilizadas

- Python 3.x
- pandas
- matplotlib
- numpy

## Como Executar

1. Instale os pacotes necessários:

```bash
pip install pandas matplotlib numpy
```

2. Execute o arquivo:

```bash
python main.py
```

## Estratégia Simulada

- Compra (`Buy`) quando o fechamento do dia é maior que o do dia anterior.
- Venda (`Sell`) quando o fechamento do dia é menor que o do dia anterior.
- Mantém (`Hold`) se o preço não variar.

O código registra o saldo, quantidade de ações e patrimônio líquido em cada dia, além de plotar um gráfico com a evolução do patrimônio.

## Reprodutibilidade

- Seed fixa: 42
- Dados fixos e determinísticos
