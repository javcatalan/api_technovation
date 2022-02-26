from app import app
from app.models import Users,Category,Products
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class UserSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Users
        fields=('id','username','password','first_name','last_name','phone_number','mail','photo_user')
       
User_schema=UserSerializer()
Users_schema=UserSerializer(many=True)        


class CategoriaSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Category
        fields=('id','name','description','photo_categoria')
        
Categoria_schema=CategoriaSerializer()
Categorias_schema=CategoriaSerializer(many=True)  

class ProductosSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Products
        fields=('id','name','description','price','photo_product')
        
Producto_schema=ProductosSerializer()
Productos_schema=ProductosSerializer(many=True)  
