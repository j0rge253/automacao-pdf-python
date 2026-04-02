# Automação de Gestão Documental com Python 🚀

Este projeto foi desenvolvido para automatizar o processo de organização e renomeação de documentos PDF (mensalidades, pedidos e ingressos) através da extração inteligente de dados.

## 🛠️ Tecnologias e Bibliotecas
- **Python 3.12+**
- **PyPDF2**: Para extração de texto de ficheiros PDF.
- **Regex (re)**: Para localização e extração de padrões de datas.
- **OS & Time**: Para manipulação do sistema de ficheiros e geração de identificadores únicos.

## 📋 Funcionalidades
- **Leitura Automática**: Identifica o conteúdo do PDF sem necessidade de abertura manual.
- **Categorização Inteligente**: Renomeia ficheiros com base em palavras-chave (ex: Estácio, Natura, Fortaleza).
- **Extração de Datas**: Utiliza Expressões Regulares para encontrar a data do documento e incluí-la no nome.
- **Prevenção de Duplicatas**: Utiliza timestamps para garantir que nenhum ficheiro seja sobrescrito.

## 🚀 Como Executar
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Coloque os seus PDFs na pasta `documentos_recebidos/`.
5. Execute o script: `python leitor_pdf.py`.