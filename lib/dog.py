from models import Dog
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker




def create_table(base, engine):
    base.metadata.create_all(engine)
    pass

def save(session, dog):
    session.add(dog)
    session.commit()
    pass

def get_all(session):
    list= [ dogs for dogs in session.query(Dog)]
    return list
    pass

def find_by_name(session, name):
    name=session.query(Dog).filter(Dog.name==name).first()
    return name
    pass

def find_by_id(session, id):
    id=session.query(Dog).filter(Dog.id== id).first()
    return id
    pass

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()
    pass

def update_breed(session, dog, breed):
    dog.breed=breed
    session.commit()
    pass