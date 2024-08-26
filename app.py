from flask import Flask, render_template, request, redirect, url_for
from pony.orm import Database, PrimaryKey, select, Required, db_session, Set, Optional

app = Flask(__name__)

db = Database()
db.bind(provider='sqlite', filename='poslovi.sqlite', create_db=True)

class Posao(db.Entity):
    id = PrimaryKey(int, auto=True)
    pozicija = Required(str)
    poslodavac = Required(str)
    lokacija = Required(str)
    placa = Required(int)
    opis = Required(str)
    nudimo = Required(str)
    trazimo = Required(str)

db.generate_mapping(create_tables=True)

@app.route('/')
@db_session
def index():
    poslovi = select(a for a in Posao)[:]
    return render_template('index.html', posao=poslovi)

@app.route('/spremi_posao', methods=['POST'])
@db_session
def spremi_posao():
    if request.method == 'POST':
        pozicija = request.form['pozicija']
        poslodavac = request.form['poslodavac']
        lokacija = request.form['lokacija']
        placa = int(request.form['placa'])
        trazimo = request.form['trazimo']
        nudimo = request.form['nudimo']
        opis = request.form['opis']
        posao = Posao(pozicija=pozicija, poslodavac=poslodavac, placa=placa, opis=opis, lokacija=lokacija, nudimo=nudimo, trazimo=trazimo)
    return redirect(url_for('index'))

@app.route('/<int:posao_id>/edit/', methods=['GET'])
@db_session
def edit(posao_id):
    posal = Posao.get(id=posao_id)
    if posal:
        return render_template('uresi.html', posal=posal)

@app.route('/<int:posao_id>/spremi_promjene', methods=['POST'])
@db_session
def spremi_promjene(posao_id):
    if request.method == 'POST':
        pozicija = request.form['pozicija']
        poslodavac = request.form['poslodavac']
        lokacija = request.form['lokacija']
        placa = int(request.form['placa'])
        trazimo = request.form['trazimo']
        nudimo = request.form['nudimo']
        opis = request.form['opis']
        posal = Posao.get(id=posao_id)
        posal.set(pozicija=pozicija, poslodavac=poslodavac, placa=placa, opis=opis, lokacija=lokacija, nudimo=nudimo, trazimo=trazimo)
    return redirect(url_for('index'))

@app.route('/dodaj', methods=['GET'])
@db_session
def dodaj():
    return render_template('dodaj.html')

@app.route('/<int:posao_id>/delete/', methods=['POST'])
@db_session
def delete(posao_id):
    posal = Posao.get(id=posao_id)
    if posal:
        posal.delete()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("8000"),)
