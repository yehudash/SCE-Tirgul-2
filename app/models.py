from app import db


class User(db.Model):
    first_name = db.Column(db.String(120), index=True, unique=False)
    last_name = db.Column(db.String(120), index=True, unique=False)
    id = db.Column(db.Integer, primary_key=True)
    voted = db.Column(db.Integer, default=0 ,  unique=False)
    def __init__(self, first_name, last_name , id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.voted = 0



    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % self.first_name


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=False)
    picture = db.Column(db.String(120), index=True, unique=False)
    votes = db.Column(db.Integer, default=0, unique=False)

    def __init__(self, name, picture):
        self.name = name
        self.picture = picture
        self.votes = 0

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<Party %r>' % self.name

db.Model.metadata.create_all(engine)
