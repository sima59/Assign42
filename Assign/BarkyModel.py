from flask import Flask,render_template,request,redirect
from models import db,BarkyModel
 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<bookmarks>.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        id = request.form['id']
        title = request.form['title']
        url = request.form['url']
        note = request.form['note']
        date_added=request.form['date_added']
        bookmarks= BarkyModel(id=id, title=title, url=url, note = note)
        db.session.add(bookmarks)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def RetrieveDataList():
    bookmarks = BarkyModel.query.all()
    return render_template('datalist.html',bookmarks = bookmarks)

@app.route('/data/<int:id>')
def RetrieveSinglefield(id):
    bookmarks = BarkyModel.query.filter_by(id=id).first()
    if bookmarks:
        return render_template('data.html', title = 'title')
    return f"data with id ={id} Doenst exist"

#--------------------Update View
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
   bookmarks = BarkyModel.query.filter_by(id=id).first()
   if request.method == 'POST':
        if bookmarks:
            db.session.delete(bookmarks)
            db.session.commit()
            title = request.form['Title']
            url = request.form['url']
            note = request.form['note']
            employee = BarkyModel(employee_id=id, title=title, url=url, note = note)
            db.session.add(bookmarks)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"column with id = {id} Does nit exist"

   return render_template('update.html', bookmarks = bookmarks)
    

    #--------------------------------delete
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    bookmarks= BarkyModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if bookmarks:
            db.session.delete(bookmarks)
            db.session.commit()
            return redirect('/data')
        #abort(404)
 
    return render_template('delete.html')

app.run(host='localhost', port=5000)