*Obs:Baixar arquivo readme para melhor viualização

# app_api_farmacias
API de consulta de Pacientes, Farmácias e Transações: Uma API em Python usando FastAPI e SQLite para visualizar e filtrar dados de pacientes, farmácias e transações. A API também dispõem de token de segurança para autenticação de usuários.

-Estrutura

app
├── db
│   ├── connection.py -> (conexão com o banco de dados sqlite)
│   └── models.py -> (modelos/schemas) para os dados do banco
├── filters.py -> (filtros e sanitização para os endpoints)
├── main.py -> (endpoints)
├── test_main.py -> (teste automático utilizando pytes)
└── token_verification.py -> (lógica de geração e verifiação do token com usuário padrão)

- Funcionalidades

Autenticação via token para acessar os endpoints da API.
Endpoint para obter informações de pacientes.
Endpoint para obter informações de farmácias.
Endpoint para obter informações de transações.

- Requisitos

Python 3.8 ou superior
Bibliotecas Python listadas no arquivo requirements.txt
Banco de dados SQLite

-Instalação

1 - Clone o repositório para sua máquina local.
2 - Crie um ambiente virtual usando o uvicorn (FastAPI) -> https://fastapi.tiangolo.com/
3 - Ative o ambiente virtual: source nome_do_ambiente/bin/activate (Linux/Mac) ou nome_do_ambiente\Scripts\activate (Windows).
4 - Instale as dependências do projeto: pip install -r requirements.txt.
5 - Utilize o comando uvicorn main:app --reload (FastAPI)

-Uso

1 - Após iniciar o servidor com uvicorn, acesse a URL http://localhost:8000/auth para obter o token de acesso. Utilizando por exemplo o software Insomnia, 
pasta enviar no body da requisição POST o seguinte Json com um usuário padrão: 

{
  "username": "admin",
  "password": "$Enha123"
}

que é um usuário padrão e preencher os headers da seguinte forma:

header: Content-Type
value: application/json

e enviar a requisição obtendo um token de acesso (verificação de usuário).

2 - Tendo recebido o token de verificação de usuário, basta enviá-lo no cabeçalho da requisião dos enpoints http://localhost:8000/patients, http://localhost:8000/pharmacies ou http://localhost:8000/transactions da seguinte forma:

header: Authorization
value: Bearer <token> (exemplo: Bearer d48a010f001ee8b747e5)

Assim, é possível obter as informações de cada endpoint. Também é possível aplicar filtros em cada um dos endpoints da seguinte forma:
  
endpoint = "?" + nome do filtro = informação desejada
  
exemplo: http://localhost:8000/transactions?transaction_id=TRAN0001*%) -> Esse filtro devolve as seguintes informações (*% foram colocados apenas para demonstrar as funções de sanitização) :
  
{
	"transactions": [
		{
			"patient_id": "PATIENT0045",
			"patient_name": "CRISTIANO",
			"patient_last_name": "SALOMAO",
			"patient_date_of_birth": "1993-09-30",
			"pharmacy_id": "PHARM0008",
			"pharmacy_name": "DROGAO SUPER",
			"pharmacy_city": "CAMPINAS",
			"transaction_id": "TRAN0001",
			"transation_amount": 3.5,
			"transaction_date": "2020-02-05"
		}
	]
}

Os endpoints possuem os seguintes filtros: 
  
Patients: 
  
patient_name (opcional): Filtra os pacientes pelo nome.
patient_last_name (opcional): Filtra os pacientes pelo sobrenome.
patient_id (opcional): Filtra os pacientes pelo ID.
  
Pharmacies: pharmacy_name, pharmacy_id, pharmacy_city

pharmacy_name (opcional): Filtra as farmácias pelo nome.
pharmacy_id (opcional): Filtra as farmácias pelo ID.
pharmacy_city (opcional): Filtra as farmácias pela cidade.
  
Transactions: 
  
transaction_id (opcional): Filtra as transações pelo ID.
patient_name (opcional): Filtra as transações pelo nome do paciente.
patient_id (opcional): Filtra os pacientes pelo ID.
  
  


