# criar venv (opcional)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# instalação das dependências
pip install -r requirements.txt

# executar a API
uvicorn main:app --reload
