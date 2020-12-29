from app import app
from models import db, User, Vocab, Word


db.drop_all()
db.create_all()

c1 = User(username="testuser5",
    password="password5",
    )

c2 = User(
    username="testuser55",
    password="password5",
    )

d1 =Vocab(
    title="Week 1",
    username="testuser5"

)

d2 =Vocab(
    title="Week 2",
    username="testuser5"

)

d3 =Vocab(
    title="Week 3",
    username="testuser5"

)

d4 =Vocab(
    title="Colors",
    username="testuser55"

)

d5 =Vocab(
    title="Verbs",
    username="testuser55"

)

e1 = Word(word="adios", translation="bye", list_title="Week 1")

e2 = Word(word="hola", translation="hi", list_title="Week 1")

e3 = Word(word="buenos dias", translation="good day", list_title="Week 1")

print("i'm running")

db.session.add_all([c1, c2, d1, d2, d3, d4, d5, e1, e2, e3])
db.session.commit()