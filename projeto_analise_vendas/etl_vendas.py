import pandas as pd
import glob
import os


def processar_dados_vendas():
    caminho_bruto = "./dados_brutos"
    arquivos = glob.glob(os.path.join(caminho_bruto, "*.csv"))

    if not arquivos:
        print("❌ Nenhum arquivo encontrado em /dados_brutos")
        return

    print(f"📊 Localizados {len(arquivos)} arquivos. Iniciando limpeza...")

    lista_dfs = []

    for arquivo in arquivos:
        df = pd.read_csv(arquivo)

        # --- ETAPA DE TRANSFORMAÇÃO ---

        # 1. Padroniza colunas para minúsculo e remove espaços
        df.columns = [col.lower().strip() for col in df.columns]

        # 2. Remove linhas com valores nulos nos campos críticos
        linhas_antes = len(df)
        df = df.dropna(subset=['valor_venda', 'custo_produto'])
        linhas_removidas = linhas_antes - len(df)
        if linhas_removidas > 0:
            print(f"  ⚠️  {os.path.basename(arquivo)}: {linhas_removidas} linha(s) removida(s) por dados incompletos")

        # 3. Converte coluna de data para o formato correto
        df['data'] = pd.to_datetime(df['data'])

        # 4. Extrai ano e mês para facilitar filtros no Power BI
        df['ano'] = df['data'].dt.year
        df['mes'] = df['data'].dt.month
        df['mes_nome'] = df['data'].dt.strftime('%B')

        # 5. Cálculo de métricas de negócio
        df['lucro'] = df['valor_venda'] - df['custo_produto']
        df['margem_%'] = (df['lucro'] / df['valor_venda']) * 100

        lista_dfs.append(df)

    # Consolida todos os meses em um único DataFrame
    base_final = pd.concat(lista_dfs, ignore_index=True)

    # Ordena por data para facilitar análise temporal
    base_final = base_final.sort_values('data').reset_index(drop=True)

    # Salva o resultado final (encoding utf-8-sig garante acentos no Excel/Power BI)
    output_path = "base_vendas_consolidada.csv"
    base_final.to_csv(output_path, index=False, encoding='utf-8-sig')

    # --- RELATÓRIO RESUMIDO NO TERMINAL ---
    print("\n✅ PROCESSO CONCLUÍDO!")
    print(f"📈 Total de vendas processadas: {len(base_final)}")
    print(f"💰 Lucro Total: R$ {base_final['lucro'].sum():,.2f}")
    print(f"📉 Margem Média: {base_final['margem_%'].mean():.1f}%")
    print(f"\n🏆 Top 3 Produtos por Lucro:")
    top_produtos = (
        base_final.groupby('produto')['lucro']
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )
    for produto, lucro in top_produtos.items():
        print(f"   • {produto}: R$ {lucro:,.2f}")

    print(f"\n📁 Arquivo gerado: {output_path}")


if __name__ == "__main__":
    processar_dados_vendas()
