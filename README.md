# 🎨 Sistema de Galeria de Imagens

Bem-vindo ao **Sistema de Galeria**, uma aplicação web simples, moderna e funcional para gerenciamento de imagens. Criada com foco em organização e praticidade, essa galeria permite cadastrar, visualizar e remover imagens de forma intuitiva.

![Badge](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Badge](https://img.shields.io/badge/Feito%20com-Django-blue)
![Badge](https://img.shields.io/badge/Front--end-Bootstrap-purple)

---

## ✨ Funcionalidades

- ✅ Upload de imagens
- ✅ Visualização em grade responsiva
- ✅ Edição e exclusão de imagens
- ✅ Organização por categorias (opcional)
- ✅ Interface amigável e responsiva

---

## 🧰 Tecnologias utilizadas

- **Back-end**: Python + Django
- **Front-end**: HTML5, CSS3, Bootstrap
- **Banco de dados**: SQLite
- **Outros**: Pillow (para manipulação de imagens)

---

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/Arthurtrin/Sistema-Galeria.git

# Entre na pasta do projeto
cd galeria

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # no Windows use: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
