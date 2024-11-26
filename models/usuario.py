from main import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    nome = db.Column(db.String(100), nullable= False)
    email = db.Column(db.String(100), nullable= False)
    senha = db.Column(db.String(100), nullable= False)

    def __repr__(self ):
        return '<Usuario %r>'%self.nome 
