from flask import Flask, render_template, request, redirect, url_for, flash  

app = Flask(__name__)  
app.secret_key = 'senha'  
 
valid_user = 'usuario'  
valid_password = 'senha'  

# Lista de equipamentos armazenados  
equipamentos = []  

@app.route('/', methods=['GET', 'POST'])  
def index():  
    if request.method == 'POST':  
        username = request.form['username']  
        password = request.form['password']  

        if username == valid_user and password == valid_password:  
            flash('Seja bem-vindo às Indústrias Wayne!')  
            return redirect(url_for(''))  
        else:  
            flash('Usuário ou senha incorretos. Tente novamente.')  

    return render_template('index.html', equipamentos=equipamentos)  

@app.route('/gerenciamento_equipamentos', methods=['GET', 'POST'])  
def gerenciamento_equipamentos():  
    if request.method == 'POST':  
        nome = request.form.get('nome')  
        descricao = request.form.get('descricao')  
        numero_serie = request.form.get('numeroSerie')  
        status = request.form.get('status')  
        localizacao = request.form.get('localizacao')  

        # Adiciona o novo equipamento à lista  
        equipamentos.append({  
            'nome': nome,  
            'descricao': descricao,  
            'numero_serie': numero_serie,  
            'status': status,  
            'localizacao': localizacao  
        })  

        flash('Equipamento adicionado com sucesso!')  
        return redirect(url_for('gerenciamento_equipamentos'))  

    return render_template('index.html', equipamentos=equipamentos)  

if __name__ == '__main__':  
    app.run(debug=True)