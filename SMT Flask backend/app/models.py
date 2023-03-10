from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from secrets import token_hex
from datetime import timezone, datetime
from werkzeug.security import generate_password_hash

db = SQLAlchemy()



def load_user(id):
    return User.query.get(int(id))


user_comp = db.Table(
    "user_comp",
    db.Column('user_id', db.Integer, db.ForeignKey('User.id'), nullable=False),
    db.Column('demon_id', db.Integer, db.ForeignKey('Demon.demon_id'), nullable=False)
)

demons_skills = db.Table(
    "demons_skills",
    db.Column('skill_id', db.Integer, db.ForeignKey('Skill.skill_id'), nullable=False),
    db.Column('demon_id', db.Integer, db.ForeignKey('Demon.demon_id'), nullable=False)
)



class User(db.Model, UserMixin):
    __tablename__ = "User" 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    apitoken = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    demon = db.relationship("Demon", 
        secondary = user_comp, 
        backref= "user_comp", lazy="dynamic")
    
    def __init__(self, username,  email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)

    

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def catch_demon(self, caught_demon):
        self.demon.append(caught_demon)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username' : self.username,
            'email' : self.email,
            'apitoken' : self.apitoken
        }

class Skill(db.Model):
    __tablename__ = "Skill"
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(60), nullable=False, unique=True)
    type = db.Column(db.String(50), nullable=False, unique=True)
    affinity = db.Column(db.String(50), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    range = db.Column(db.String(50), nullable=False)
    


    def __init__(self, skill_name, type, affinity, power, range):
        self.skill_name = skill_name
        self.type = type
        self.affinity = affinity
        self.power = power
        self.range = range

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()


class Demon(db.Model):
    __tablename__ ="Demon"
    demon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    strength = db.Column(db.Integer, nullable=False)
    magic = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    weak = db.Column(db.String(50), nullable=False)
    null = db.Column(db.String(50), nullable=False)
    repel = db.Column(db.String(50), nullable=False)
    lore = db.Column(db.String(1000), nullable=False)
    skills = db.relationship("Skill", 
        secondary = demons_skills, 
        backref= "demons_skills", lazy="dynamic")



    def __init__(self, name, hp, strength, magic, defense, weak, null, repel, lore):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.magic = magic
        self.defense = defense
        self.weak = weak
        self.null = null
        self.repel = repel
        self.lore = lore

    def saveToDB(self):
        db.session.add(self)
        db.session.commit()

    def deleteFromDB(self):
        db.session.delete(self)
        db.session.commit()

    

    

