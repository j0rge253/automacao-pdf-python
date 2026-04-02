# Pipeline ETL - Koala Sports

Pipeline de dados que consolida relatórios mensais de vendas em CSV, aplica limpeza e gera uma base pronta para Power BI.

## Fluxo

```
dados_brutos/*.csv  →  etl_vendas.py  →  base_vendas_consolidada.csv
```

## Como rodar

```bash
pip install -r requirements.txt
python etl_vendas.py
```

## Transformações aplicadas

- Padronização de nomes de colunas
- Remoção de linhas com dados críticos ausentes
- Conversão e extração de datas (ano, mês)
- Cálculo de lucro e margem por venda

## Output

`base_vendas_consolidada.csv` — pronto para importar no Power BI ou Excel.
