
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder
from .models import Categoria, Ingrediente


class CategoriaView(ModelView):
    datamodel = SQLAInterface(Categoria)

    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripción",
        "activo": "Activo",
        "ingredientes": "Ingredientes",
    }

    list_columns = ["nombre", "descripcion", "activo"]

    show_columns = [
        "id",
        "nombre",
        "descripcion",
        "activo",
        "ingredientes",
    ]

    add_columns = ["nombre", "descripcion", "activo"]

    edit_columns = ["nombre", "descripcion", "activo"]

    order_columns = ["nombre"]


class IngredienteView(ModelView):
    datamodel = SQLAInterface(Ingrediente)

    label_columns = {
        "nombre": "Nombre",
        "categoria": "Categoría",
        "cantidad": "Cantidad",
        "unidad_medida": "Unidad de Medida",
        "costo_unitario": "Costo Unitario",
        "stock_minimo": "Stock Mínimo",
        "fecha_vencimiento": "Fecha de Vencimiento",
        "activo": "Activo",
    }

    list_columns = [
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo",
    ]

    show_columns = [
        "id",
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo",
    ]

    add_columns = [
        "nombre",
        "categoria",
        "cantidad",
        "unidad_medida",
        "costo_unitario",
        "stock_minimo",
        "fecha_vencimiento",
        "activo",
    ]

    edit_columns = add_columns

    search_columns = ["nombre"]

    order_columns = ["nombre"]


# Registro de las vistas en el menú
appbuilder.add_view(
    CategoriaView,
    "Módulo Categorías",
    icon="fa-tags",
    category="Inventario",
)

appbuilder.add_view(
    IngredienteView,
    "Módulo Ingredientes",
    icon="fa-cubes",
    category="Inventario",
)
