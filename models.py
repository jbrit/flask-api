import enum
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Person(db.Model):
    class PersonType(enum.Enum):
        PARTICIPANT = "participant"
        SPEAKER = "speaker"

        def __str__(self):
            return self.value
    
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(120))
    person_type = db.Column(
        db.Enum(PersonType, values_callable=lambda obj: [e.value for e in obj]),
        default=PersonType.PARTICIPANT,
        nullable=False
    )
    # cascade foreign key on delete
    talk_id = db.Column(db.Integer, db.ForeignKey('talks.id'), nullable=False)


    def __repr__(self):
        return '<User {}>'.format(self.username)


class Talk(db.Model):
    __tablename__ = 'talks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False)
    people = db.relationship('Person', backref='talk', lazy=True)
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