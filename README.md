# 🗂️ CRUD com Python, SQLite e Streamlit

Este projeto é uma aplicação **CRUD** (Create, Read, Update, Delete) desenvolvida em Python, utilizando **SQLite** como banco de dados local e **Streamlit** para criar a interface web. O sistema permite que os usuários realizem as seguintes operações:

## ✨ Funcionalidades

- 📝 **Cadastro de Usuários**: O usuário pode registrar-se fornecendo nome, e-mail, senha e ano de nascimento. A idade mínima para cadastro é de 16 anos.
- 🔑 **Login**: O sistema valida o e-mail e a senha para permitir o acesso à conta.
- 🔄 **Alteração de Senha**: O usuário pode alterar sua senha após a validação do e-mail.
- 🗑️ **Exclusão de Conta**: O sistema permite que o usuário delete sua conta após o login.

## 🔍 Validação de Dados

O código inclui verificações para garantir que as informações fornecidas pelos usuários sejam válidas:

- 📧 **E-mail**: O sistema valida se o e-mail contém o símbolo "@".
- 🎂 **Idade**: O ano de nascimento é validado para garantir que o usuário tenha pelo menos 16 anos.
- 🔒 **Senha**: A senha deve ter pelo menos 6 caracteres e é confirmada durante o cadastro e alteração.

## 🗄️ Estrutura do Banco de Dados

O banco de dados **SQLite** contém uma tabela `Users` com as seguintes colunas:

- **Nome**: Nome do usuário.
- **E-mail**: E-mail utilizado para login.
- **Ano_Nascimento**: Ano de nascimento para verificação da idade.
- **Senha**: Senha do usuário.


