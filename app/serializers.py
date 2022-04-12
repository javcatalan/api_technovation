from app import app
from app.models import usuarios,calzado,servilletas,camino_mesa,manteles,telas_tipicas,sandalias,tenis,tacones,calzado,blusas,faldas,categorias
from flask_marshmallow import Marshmallow



ma=Marshmallow(app)

class usuariosSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=usuarios
        fields=('id','nombre_usuario','contraseña','nombre','apellido','numero_celular','correo','foto_usuario')
       
usuario_schema=usuariosSerializer()
usuarios_schema=usuariosSerializer(many=True)   


class camino_mesaSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=camino_mesa
        fields=('id_camino_mesa','nombre','ancho','largo','colores','precio','material','manufactura','imagen','cantidad_disponible')

camino_shema=camino_mesaSerializer()
caminos_shema=camino_mesaSerializer(many=True)


class servilletasSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=servilletas
        fields=('id_servilletas','nombre','ancho','largo','colores','precio','material','manufactura','imagen','cantidad_disponible')

servilleta_shema=servilletasSerializer()
servilletas_shema=servilletasSerializer(many=True)
 

class mantelesSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=manteles
        fields=('id_manteles','nombre','ancho','largo','colores','precio','material','manufactura','imagen','cantidad_disponible')

mantel_shema=mantelesSerializer()
manteles_shema=mantelesSerializer(many=True)

class telastipicasSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=telas_tipicas
        fields=('id_telas','nobre','ancho','largo','colores','precio','material','manufatura','imagen','cantidad_disponible')

telatipica_shema=telastipicasSerializer()
telastipicas_shema=telastipicasSerializer(many=True)

class sandaliasSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=sandalias
        fields=('id_sandalias','nombre','color','tallas_disponibles','precio','descuento','imagen','cantidad_disponible')

sandalia_shema=sandaliasSerializer()
sandalias_shema=sandaliasSerializer(many=True)

class tenisSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=tenis
        fields=('id_tenis','nombre','color','tallas_disponibles','precio','descuento','imagen','cantidad_disponible')

onetenis_shema=tenisSerializer()
tenis_shema=tenisSerializer(many=True)

class taconesSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=tacones
        fields=('id_tacones','nombre','color','tallas_disponibles','precio','descuento','imagen','cantidad_disponible')

tacon_shema=taconesSerializer()
tacones_shema=taconesSerializer(many=True)

class blusasSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=blusas
        fields=('id_blusas','nombre','tallas_disponibles','material','manufactura','precio','descuento','imagen','cantidad_disponible')
    
blusa_shema=blusasSerializer()
blusas_shema=blusasSerializer(many=True)

class faldasSerializer(ma.SQLAlchemyAutoSchema):
    class faldas:
        model=faldas
        fields=('id_faldas','nombre','tallas_disponibles','material','manufactura','precio','descuento','imagen','cantidad_disponible')

falda_shema=faldasSerializer()
faldas_shema=faldasSerializer(many=True)

class calzadoSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=calzado
        fields=('id_calzado','id_zandalias','id_tenis','id_tacones')
       
calzado_schema=calzadoSerializer()
calzados_schema=calzadoSerializer(many=True)   


class categoriaSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=categorias
        fields=('id_categorias','id_manteleria','id_telas','id_calzado','id_vestimenta','foto_manteleria','foto_telas_tipicas','foto_calzado','foto_vestimenta')
        
categoria_schema=categoriaSerializer()
categorias_schema=categoriaSerializer(many=True)  


# class mantelesSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model=manteles
#         fields=('id_manteles','nombre','ancho','largo','colores','precio','material','manufactura','imagen','cantidad_disponible')
# manteles_shema=mantelesSerializer()
# manteles_shema=mantelesSerializer(many=True)




# class ProductsSerializer(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model=Products
#         fields=('id','name','description','price','photo_product')
        
# Producto_schema=ProductsSerializer()
# Productos_schema=ProductsSerializer(many=True)  
