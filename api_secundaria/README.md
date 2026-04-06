# API de Distância (API Secundária)

## 📌 Descrição

Esta API é responsável exclusivamente pelo cálculo de distância entre dois pontos geográficos, utilizando latitude e longitude.

Ela é utilizada pela [API Principal](https://github.com/DaviAmaral-SI/api-principal-mvp-backend-adv/), seguindo o conceito de separação de responsabilidades em uma arquitetura de microsserviços.

---

## 🧠 Funcionamento

A API recebe quatro parâmetros, convertidos do número identificador de dois CEPs passados pelo usuário:

* lat1 → latitude do ponto 1
* lon1 → longitude do ponto 1
* lat2 → latitude do ponto 2
* lon2 → longitude do ponto 2

E retorna a distância em quilômetros entre os dois pontos.

---

## 📐 Fórmula utilizada

A distância é calculada utilizando a **fórmula de Haversine**, que considera a curvatura da Terra.

---

## 🚀 Endpoint

### GET /distancia

#### Exemplo:

```
/distancia?lat1=-22.90&lon1=-43.20&lat2=-23.55&lon2=-46.63
```

#### Resposta:

```json
{
  "distancia_km": 357.12
}
```

---

## 🛠️ Tecnologias Utilizadas

* [Python](https://www.python.org/downloads/)
* [Flask](https://flask.palletsprojects.com/en/stable/)
* [Docker](https://www.docker.com/products/docker-desktop/)

---

## Como configurar o Ambiente Virtual

Esse tópico explica de forma simples como criar e ativar o ambiente virtual [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Digite os seguintes códigos em ordem no terminal de comando:

- Caso o virtualenv ainda não esteja instalado
```
pip install virtualenv
```

- Criar o ambiente virtual dentro da pasta backend
```
python -m venv venv
```

- Ativar o ambiente virtual
```
venv\Scripts\activate (Windows) ou source venv/bin/activate (Linux/MacOS)
```

---

## Como executar a API Flask

Será necessário instalar todas as bibliotecas presentes no arquivo **requirements.txt**. Para isso, é necessário abrir o terminal pelo diretório raiz do projeto e executar o seguinte comando (já com o ambiente virtual ativado).

```
(venv)$ pip install -r requirements.txt
```

Para executar a API, digite no prompt:
```
(venv)$ flask run --host 0.0.0.0 --port 5001
```

Caso queira utilizar em modo de desenvolvimento (sempre que o código for mudado, o servidor será reiniciado), digite essa linha:
```
(venv)$ flask run --host 0.0.0.0 --port 5001 --reload
```

Entre no http://localhost:5001/#/ no navegador para utilizar a API.


---

## 📦 Como executar via Docker

### Pré-requisitos

* Docker Desktop instalado

### Passos

Basta rodar o seguinte comando pelo terminal Docker, dentro do diretório da [API Principal](https://github.com/DaviAmaral-SI/api-principal-mvp-backend-adv/). 

```bash
docker-compose up --build
```

---

## 🌐 Acesso

```
http://localhost:5001/distancia
```

---

## 🔗 Integração

Esta API é consumida pela [API Principal](https://github.com/DaviAmaral-SI/api-principal-mvp-backend-adv/) através de requisições HTTP.

Exemplo de uso:

```python
requests.get("http://secundaria:5001/distancia")
```

---

## 🧠 Decisões de Projeto

* Separação da lógica de cálculo em um serviço independente
* Comunicação via HTTP
