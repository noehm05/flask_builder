from flask_appbuilder import Model
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
 
class Categoria(Model):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique = True, nullable=False)
    descripcion = Column(String(250), nullable=True)
    activo = Column(Boolean, default=True, nullable=False)
   
    ingredientes = relationship(
        "Ingrediente",
        back_populates="categoria"
    )
   
    def __repr__(self):
        return self.nombre
   
   
class Ingrediente(Model) :
        __tablename__ = "ingredientes"
        id = Column(Integer, primary_key=True)
        nombre = Column(String(100), unique = True, nullable=False)
        categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
        cantidad = Column(Numeric(12,2), default=0, nullable=False )
        unidad_medida = Column(String(20), nullable=False)
        costo_unitario = Column(Numeric(12,2), default=0, nullable=False )
        stock_minimo = Column(Numeric(12,2), default=0, nullable=False )
        fecha_vencimiento = Column(Date, nullable=False )
        activo = Column(Boolean, default=True, nullable=False)
       
        categoria = relationship(
            "Categoria",
            back_populates="ingredientes"
        )
       
        def __repr__(self):
            return self.nombre
 
 
 
