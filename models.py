from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Talk(db.Model):
    __tablename__ = 'talks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    speaker_ids = db.Column(db.Integer, db.ForeignKey('people.id'))
    participant_ids = db.Column(db.Integer, db.ForeignKey('people.id'))
    participants = db.relationship('Person', foreign_keys=[participant_ids])
    speakers = db.relationship('Person', foreign_keys=[speaker_ids])
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'), nullable=False)

    def __repr__(self):
        return '<Talk {}>'.format(self.title)

class Conference(db.Model):
    __tablename__ = 'conferences'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    talks = db.relationship('Talk', backref='conference', lazy='dynamic')

    def __repr__(self):
        return '<Conference {}>'.format(self.name)