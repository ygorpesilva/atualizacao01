from flask import Flask  
from flask_mysqldb import MySQL  

app = Flask(__name__)  
 
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'user'    
app.config['MYSQL_PASSWORD'] = '123456'   
app.config['MYSQL_DB'] = 'Servidor_IndustriasWayne'   
 
mysql = MySQL(app)

@app.route('/gerenciamento_equipamentos', methods=['GET', 'POST'])  
def gerenciamento_equipamentos():  
    if request.method == 'POST':  
        nome = request.form.get('nome')  
        descricao = request.form.get('descricao')  
        numero_serie = request.form.get('numeroSerie')  
        status = request.form.get('status')  
        localizacao = request.form.get('localizacao')  

         
        cur = mysql.connection.cursor()  
        cur.execute("INSERT INTO equipamentos(nome, descricao, numero_serie, status, localizacao) VALUES(%s, %s, %s, %s, %s)",   
                    (nome, descricao, numero_serie, status, localizacao))  
        mysql.connection.commit()  
        cur.close()  

        flash('Equipamento adicionado com sucesso!')  
        return redirect(url_for('gerenciamento_equipamentos'))  
 
    cur = mysql.connection.cursor()  
    cur.execute("SELECT * FROM equipamentos")  
    equipamentos = cur.fetchall()  
    cur.close()  

    return render_template('index.html', equipamentos=equipamentos) 