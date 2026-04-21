import psycopg2

conexao = psycopg2.connect (
    host="localhost",
    database="produtos1",
    user="postgres",
    password="1234" ,
    port="5432" )

print("Conexão bem-sucedida!")

meu_cursor = conexao.cursor()


    
meu_cursor.execute(''' 
       CREATE TABLE IF NOT EXISTS PRODUTO (
        Codigo SERIAL PRIMARY KEY,
        Nome VARCHAR(100) NOT NULL,
        Preco DECIMAL(10, 2) NOT NULL
                       
    )''')

conexao.commit()
print("Tabela criada com sucesso!")
