from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Talk(db.Model):
    __tablename__ = 'talks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), null=False)
    description = db.Column(db.String(120), null=False)
    speaker_ids = db.Column(db.Integer, db.ForeignKey('people.id'))
    participant_ids = db.Column(db.Integer, db.ForeignKey('people.id'))
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'))

    def __repr__(self):
        return '<Talk {}>'.format(self.title)

class Conference(db.Model):
    __tablename__ = 'conferences'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), null=False)
    description = db.Column(db.String(120), null=False)
    start_date = db.Column(db.DateTime, null=False)
    end_date = db.Column(db.DateTime, null=False)
    talks = db.relationship('Talk', backref='conference', lazy='dynamic')

    def __repr__(self):
        return '<Conference {}>'.format(self.name)