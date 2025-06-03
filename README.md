# 🎬 IMDb Movie Search

Bem-vindo ao **IMDb Movie Search**, um projeto Flask que permite pesquisar filmes utilizando a base de dados do IMDb!

---

## 📚 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Personalização](#personalização)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## 📝 Sobre o Projeto

Este projeto utiliza Flask e a biblioteca IMDbPY para buscar e exibir informações de filmes. O código segue o padrão MVC, separando modelos, controladores e templates para facilitar a manutenção e evolução.

---

## 📁 Estrutura de Pastas

```
filmimdbapi/
│
├── app.py
├── controllers/
│   └── movie_controller.py
├── models/
│   └── movie_model.py
├── static/
│   └── index.css
├── templates/
│   ├── index.html
│   └── movie_details.html
└── .gitignore
```

---

## ⚙️ Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

---

## 🚀 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/filmimdbapi.git
   cd filmimdbapi
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   # Ative no Windows:
   venv\Scripts\activate
   # Ou no Linux/Mac:
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

   > Se não existir um arquivo `requirements.txt`, crie um com:
   > ```
   >pip
   >autopep8
   >Flask==3.0.3
   >requests
   >Werkzeug==3.0.6
   >imdbpy
   > ```

---

## ▶️ Como Usar

1. **Acesse no navegador:**
   ```
   https://filmimdbapi.onrender.com
   ```

3. **Pesquise por um filme e veja os resultados!**

---

## 🎨 Personalização

- **CSS:** Edite o arquivo `static/index.css` para alterar o visual.
- **Templates:** Modifique os arquivos em `templates/` para mudar o layout das páginas.

---

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request


---

<div align="center">
  Feito com 💛 por Antoni Mattei
</div>
