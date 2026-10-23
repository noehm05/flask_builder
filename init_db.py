
from app import app
from app.models import Categoria, Ingrediente


with app.app_context():
    metadata = Categoria.metadata
    engine = app.extensions["sqlalchemy"].engine

    print("Tablas registradas:")

    for tabla in metadata.sorted_tables:
        print("-", tabla.name)

    metadata.create_all(bind=engine)

    print("\n¡Tablas creadas o verificadas correctamente!")
