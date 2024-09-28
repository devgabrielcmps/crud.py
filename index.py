#Gabriel Campos 
#Criacao de um CRUD em python com SQLite

import datetime as dt
import sqlite3
import streamlit as st


def verifica_email(email):
    if '@' in email:
      return True
    else:
      st.error('Email Inválido.')


def verifica_idade(ano_nascimento):
  ano_atual=dt.datetime.now().year

  if ano_nascimento.isdigit() and len (ano_nascimento) != 4:
     st.error('Insira um ano valido')
     return False
  if ano_atual > int(ano_nascimento):
    if (ano_atual-int(ano_nascimento)) >= 16:
      return True
    else:
      st.error('Precisa ser maior de 16 anos para usar o site!')
      return False
  else:
    st.error('IDADE INCORRETA')
    return False



def verifica_senha(senha):
  if len(senha) > 6:
    return True
  else:
    st.error('Senha Inválida | Minimo 6 caracteres.')


def confirma_senha(senha,confirma_senha):
  if confirma_senha == senha:
    return True
  else:
    st.error('Senhas nao combinam')


def login(email,senha):

  st.markdown(
    """
    <style>
    .big-button {
        font-size: 20px;  /* Tamanho da fonte */
        padding: 5px 20px;  /* Espaçamento interno */
        background-color: #920;  /* Cor de fundo */
        color: white;  /* Cor do texto */
        border: none;  /* Sem borda */
        border-radius: 5px;  /* Bordas arredondadas */
        cursor: pointer;  /* Cursor pointer */
        margin-top: 15px;  /* Margem superior */
        width: 100%;  /* Largura do botão */
    }
    </style>
    """,
    unsafe_allow_html=True
)
  #Abre o database
  conexao = sqlite3.connect('Projetos2024\STREAMLIT\CRUD\database.db', timeout=30)
  #Inica o cursor
  cursor = conexao.cursor()
  # Executar a consulta para verificar se o email está presente
  cursor.execute("SELECT * FROM Users WHERE Email = ? AND Senha = ?", (email,senha))
  conexao.commit()
  # Obtem um resultado
  resultado = cursor.fetchone()
  #Fecha o cursor 
  cursor.close()
  #Fecha a conexao
  conexao.close()

  if resultado:
          st.success('EM CONSTRUCAO | NOVIDADES EM BREVE')
          return True  # Retorna True se o login for bem-sucedido
  else:
          st.error('Acesso negado! Email ou senha incorretos!')
          return False  # Retorna False se não for bem-sucedido
 
  
def cadastro(nome,email,senha,ano_nascimento):
  #Abre o database
  conexao = sqlite3.connect('Projetos2024\STREAMLIT\CRUD\database.db', timeout=30)
  #Inica o cursor
  cursor = conexao.cursor()
  # Executar a consulta para verificar se o email está presente
  cursor.execute(f"INSERT INTO Users (Nome,Email,Ano_Nascimento,Senha) VALUES ('{nome}','{email}','{senha}','{ano_nascimento}')")
  conexao.commit()
  # Obtem um resultado
  resultado = cursor.fetchone()
  #Fecha o cursor 
  cursor.close()
  #Fecha a conexao
  conexao.close()

 
def delete(email):
  #Abre o database
  conexao = sqlite3.connect('Projetos2024\STREAMLIT\CRUD\database.db', timeout=30)
  #Inica o cursor
  cursor = conexao.cursor()
  try:
        # Executar a consulta para deletar o usuário
        cursor.execute("DELETE FROM Users WHERE Email = ?", (email,))
        conexao.commit()

        # Verifica se a exclusão foi bem-sucedida
        cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
        resultado = cursor.fetchone()  # Se o resultado for None, a conta foi deletada
        
        return resultado is None  # Retorna True se a conta foi deletada, caso contrário False
  
  except sqlite3.Error as e:
        st.error(f"Erro ao tentar deletar a conta: {e}")
        return False
  finally:
        cursor.close()
        conexao.close()

  
def alterar_senha(email, nova_senha):
    # Abre o database
    conexao = sqlite3.connect('Projetos2024\STREAMLIT\CRUD\database.db', timeout=30)
    
    try:
        cursor = conexao.cursor()
        
        # Verifica se o email existe
        cursor.execute("SELECT * FROM Users WHERE Email = ?", (email,))
        resultado = cursor.fetchone()

        if not resultado:
            st.error('Email não localizado! Realize seu cadastro.')
            return

        # Tenta atualizar a senha
        cursor.execute("PRAGMA busy_timeout = 30000")  # Aguarda até 30 segundos se bloqueado
        cursor.execute("UPDATE Users SET Senha = ? WHERE Email = ?", (nova_senha, email))
        conexao.commit()
        
        st.success('MUDANÇA REALIZADA COM SUCESSO')

    except sqlite3.OperationalError as e:
        st.error(f"Erro ao atualizar a senha: {e}")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()

 
class Aplicativo():
  def __init__(self,email,senha):
    self.email=email 
    self.senha=senha


  def tela_login():
    # Aplicando CSS para mudar a fonte do texto
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
        
        .titulo {
            font-family: 'Open Sans', Courier, monospace;
            font-size: 45px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    col1,col2,col3=st.columns([1,10,1])  
    with col2:      
      # Título da Página
      st.markdown("<h1 class='titulo' style='text-align: center;'>🔑 LOGIN </h1>", unsafe_allow_html=True)

      in_email=st.text_input('Email:',key='login_senha').strip()
      in_senha=st.text_input('Password:',type='password',key='senha_login')
      bt_login=st.button('Login',use_container_width=True,key='login_botao')
  
      
      if bt_login:
          if verifica_email(in_email) and verifica_senha(in_senha):
              try:
                login(in_email,in_senha)
              except KeyError:
                    st.error('Erro ao processar os dados. Verifique se os dados foram digitados corretamente.')
              except NameError: 
                    st.error('Erro ao processar os dados. Verifique se os dados foram digitados corretamente.')
          else:
           #st.error('Email ou senha inválidos.')
           pass
      else:
         pass

  def tela_cadastro():
     # Aplicando CSS para mudar a fonte do texto
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');
        
        .titulo {
            font-family: 'Open Sans', Courier, monospace;
            font-size: 45px;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    col1,col2,col3=st.columns([1,10,1])  
    with col2:      
      # Título da Página
      st.markdown("<h1 class='titulo' style='text-align: center;'>🔑 CADASTRO </h1>", unsafe_allow_html=True)

      in_nome=st.text_input('Nome:',key='nome_cadastro').strip().capitalize()
      in_email=st.text_input('Email:',key='email_cadastro').strip()
      in_ano_nascimento=st.text_input('Ano nascimento:',key='ano_nascimento_cadastro').strip()
      in_senha=st.text_input('Password:',type='password',key='senha_cadastro')
      in_confirma_senha=st.text_input('Confirm Password:',type='password',key='confirma_senha_cadastro')
      

      bt_cadastro=st.button('Sign-in',use_container_width=True,key='botao_cadastro')
      #bt_volta_login=st.button('Return Login',use_container_width=True,key='volta_login_cadastro')
  
    
      if bt_cadastro:
          if verifica_email(in_email) and verifica_idade(in_ano_nascimento) and verifica_senha(in_senha) and confirma_senha(in_senha,in_confirma_senha):
              try:
                cadastro(in_nome,in_email,in_ano_nascimento,in_confirma_senha)
                st.success('CADASTRADO COM SUCESSO | VOLTE PARA TELA DE LOGIN')
              except KeyError:
                    st.error('Erro ao processar os dados. Verifique se os dados foram digitados corretamente.')
              except NameError: 
                    st.error('Erro ao processar os dados. Verifique se os dados foram digitados corretamente.')

  def tela_mudar_senha():

    col1,col2,col3=st.columns([1,10,1])  
    with col2:
      # Título da Página
      st.markdown("<h1 class='titulo' style='text-align: center;'>🔑 CHANGING PASSWORD </h1>", unsafe_allow_html=True)
    
      in_email=st.text_input('Email: ')
      in_nova_senha=st.text_input('Nova Senha: ',type='password')
      in_confirma_nova_senha=st.text_input('Confirma: ',type='password')

      mudar_senha=st.button('Change password',use_container_width=True)
      if mudar_senha:
        if verifica_email(in_email) and verifica_senha(in_nova_senha) and confirma_senha(in_nova_senha,in_confirma_nova_senha):
           alterar_senha(in_email,in_confirma_nova_senha)
        else:
                st.error('Por favor, verifique as informações fornecidas.')
        
        
  def tela_delete():
      
 
    col1, col2, col3 = st.columns([1, 10, 1])
    with col2:
        st.markdown("<h1 class='titulo' style='text-align: center;'>🗑️ DELETE </h1>", unsafe_allow_html=True)

        in_email = st.text_input('Email: ')
        in_senha = st.text_input('Senha: ', type='password')

        bt_delete = st.button('Delete Account', use_container_width=True)

        if bt_delete:
            if verifica_email(in_email) and verifica_senha(in_senha):  
                # Aqui você deve verificar se o login é bem-sucedido #
              if login(in_email, in_senha) != False:  
                if delete(in_email):  
                    st.success('DADOS APAGADOS')
                else:
                    st.error('Erro ao excluir a conta. O email pode não existir ou ocorreu um erro.')
            else:
              st.error('Acesso negado! Email ou senha incorretos!')
        else:
            #st.error('Email ou senha inválidos.')
            pass

    
  def main():
      st.sidebar.title("MENU")
      option = st.sidebar.radio("SELECT:", ["LOGIN", "SIGN-UP","CHANGE PASSWORD","DELETE"])

      if option == "LOGIN":
          Aplicativo.tela_login()
      elif option == "SIGN-UP":
          Aplicativo.tela_cadastro()
      elif option == "CHANGE PASSWORD":
          Aplicativo.tela_mudar_senha()
      elif option == "DELETE":
          Aplicativo.tela_delete()

if __name__ == "__main__":
    Aplicativo.main()