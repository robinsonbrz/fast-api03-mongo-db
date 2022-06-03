

# Experimento Python | FastAPI | MongoDBAtlas


## Api com persistência MongoDB Atlas
<br>

Projeto aplicação gerenciador de tarefas com FastAPI
<br><br>
  <div align="center">
    <table>
      </tr>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                Adaptação e deploy por Robinson Enedino
            </td>
        <td>
            <a  href="https://www.linkedin.com/in/robinsonbrz/">
            <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/linkedin.png" width="30" height="30">
        </td>
        <td>
            <a  href="https://www.linkedin.com/in/robinsonbrz/">
            <img  src="https://avatars.githubusercontent.com/u/18150643?s=96&amp;v=4" alt="@robinsonbrz" width="30" height="30">
        </td>
        <td>
            <a href="mailto:robinsonbrz@gmail.com">
            <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/gmail.png" width="30" height="30" ></a>
        </td>
      </tr>
<br>
            <a  href="https://www.linkedin.com/in/robinsonbrz/">
            <img src="FastAPI-MongoDB-Atlas.jpg" width="256" height="256">

<br>
    </table>
  </div>
  <br>
<br>

Persistência de dados na nuvem utilizando o banco de dados não relacional MongoDb, MongoDB Atlas.
<br><br>

### A implementação pode ser visualizada nos links: 
 [https://mdb.enedino.com.br/docs](https://mdb.enedino.com.br/docs)
 <br>
 [https://fast-api03-mongo-db.vercel.app/docs](https://fast-api03-mongo-db.vercel.app/docs)


<br>
            <a  href="https://mdb.enedino.com.br/docs">
            <img src="05-put.png" >
<br><br><br>
## Utilização do programa 
_______________________


## 01 Criar o virtual environment e instalar as bibliotecas
pip instal -r requirements.txt

## 02 Setup MongoDB Atlas
Crir um database em MongoDB Atlas.

Copiar o arquivo de conexão para utilizar no arquivo config/database.py

MongoClient(f"mongodb+srv://{USER}:{PASSW}@cluster0.0nnjfk0.mongodb.net/?retryWrites=true&w=majority")

Para acesso local, digite a senha e o password do banco de dados em .env conforme o arquivo .envsample em anexo

No caso de deploy na Vercel... é necessário definir as variáveis de ambiente com a senha e usuario. Para que se conecte com o MongoDB Atlas. Devido a ausência do arquivo .env pelo .gitignore.

Criar também um arquivo .gitignore para não expor sua senha.

## Para executar o programa
```
pyhton main.py
```

# Próximas features para o app. 

Implementação de segurança OAUTH2 e autenticação
Front End para o Crud.




<br>
<br>
<br>



<h1 align="center"> Informações e contato </h1> 
  <div align="center">
    <table>
        </tr>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/linkedin.png" width="50" height="50">
            </td>
            <td>
                <a  href="https://www.linkedin.com/in/robinsonbrz/">
                <img  src="https://avatars.githubusercontent.com/u/18150643?s=96&amp;v=4" alt="@robinsonbrz" width="30" height="30">
            </td>
            <td>
                <a href="https://www.enedino.com.br/contato">
                <img src="https://raw.githubusercontent.com/robinsonbrz/robinsonbrz/main/static/img/gmail.png" width="50" height="50">
            </td>
        </tr>
    </table> 
  </div>