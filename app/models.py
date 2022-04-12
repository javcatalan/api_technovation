from app import db

    
class usuarios(db.Model):
    id=db.Column(db.Integer,primary_key=True) #autoincrement=True
    nombre_usuario=db.Column(db.String(15), unique=True)
    contraseña=db.Column(db.String(25))
    nombre=db.Column(db.String(15))
    apellido=db.Column(db.String(15))
    numero_celular=db.Column(db.String(20))
    correo = db.Column(db.String(100), unique=True)
    foto_usuario=db.Column(db.String(120))
    
    def __repr__(self):
        return self.username

class calzado(db.Model):
    id_calzado=db.Column(db.Integer,primary_key=True)
    id_sandalias =db.Column(db.Integer)
    id_tenis=db.Column(db.Integer)
    id_tacones =db.Column(db.Integer)

    # def __repr__(self):
    #     return self.username


class camino_mesa(db.Model):
    id_camino_mesa=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    ancho=db.Column(db.String(10))
    largo=db.Column(db.String(10))
    colores =db.Column(db.String(50))
    precio =db.Column(db.Integer)
    material =db.Column(db.String(100))
    manufactura =db.Column(db.String(200))
    imagen =db.Column(db.String)
    cantidad_disponible=db.Column(db.Integer)


class servilletas(db.Model):
    id_servilletas=db.Column(db.Integer,primary_key=True)
    nombre=db.Column(db.String(50))
    ancho=db.Column(db.String(10))
    largo=db.Column(db.String(10))
    colores=db.Column(db.String(50))
    precio=db.Column(db.Integer)
    material=db.Column(db.String(100))
    manufactura=db.Column(db.String(200))
    imagen=db.Column(db.String)
    cantidad_disponible=db.Column(db.Integer)


class manteles(db.Model):
    id_manteles=db.Column(db.Integer, primary_key=True)
    nombre =db.Column(db.String(50))
    ancho =db.Column(db.String(10))
    largo =db.Column(db.String(10))
    colores =db.Column(db.String(50))
    precio = db.Column(db.Integer)
    material =db.Column(db.String(100))
    manufactura =db.Column(db.String(200))
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)

class telas_tipicas(db.Model):
    id_telas=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    ancho =db.Column(db.String(10))
    largo =db.Column(db.String(10))
    colores =db.Column(db.String(50))
    precio = db.Column(db.Integer)
    material =db.Column(db.String(100))
    manufactura =db.Column(db.String(200))
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)
   
class sandalias(db.Model):
    id_sandalias=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    color =db.Column(db.String(50))
    tallas_disponibles =db.Column(db.String(50))
    precio = db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)

class tenis(db.Model):
    id_tenis=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    color =db.Column(db.String(50))
    tallas_disponibles =db.Column(db.String(50))
    precio = db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)

class tacones(db.Model):
    id_tacones=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    color =db.Column(db.String(50))
    tallas_disponibles =db.Column(db.String(50))
    precio = db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)

class blusas(db.Model):
    id_blusas=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    tallas_disponibles =db.Column(db.String(50))
    material =db.Column(db.String(100))
    manufactura =db.Column(db.String(200))
    precio = db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)
   
class faldas(db.Model):
    id_faldas=db.Column(db.Integer,primary_key=True)
    nombre =db.Column(db.String(50))
    tallas_disponibles =db.Column(db.String(50))
    material =db.Column(db.String(100))
    manufactura =db.Column(db.String(200))
    precio = db.Column(db.Integer)
    descuento=db.Column(db.Integer)
    imagen =db.Column(db.String)
    cantidad_disponible =db.Column(db.String)


class categorias(db.Model):
    id_categorias =db.Column(db.Integer,primary_key=True)
    id_manteleria  =db.Column(db.Integer)
    id_telas =db.Column(db.Integer)
    id_calzado =db.Column(db.Integer)
    id_vestimenta=db.Column(db.Integer)
    foto_manteleria =db.Column(db.String)
    foto_telas_tipicas=db.Column(db.String)
    foto_calzado=db.Column(db.String)
    foto_vestimenta=db.Column(db.String)
    # items = db.relationship('products', backref='product_category', lazy='dynamic')
    
    # def __repr__(self):
    #     return self.name

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)#autoincrement=True
    name=db.Column(db.String(50))
    description=db.Column(db.String(1000))    
    # category_id=db.Column(db.Integer,db.ForeignKey('Category.id'))
    # category =db.Relationship('Category', backref='category_products')
    price=db.Column(db.Float)
    photo_product=db.Column(db.String(120))
    #discount_price=db.Column(db.Float)

#===================================================================================================
# class Orders(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#   user =db.Relationship('Users', backref='users_orders')
#      user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#      order_num = db.Column(db.String(50), unique=True)
#     delivery_date = db.Column(db.Date)

#     def __repr__(self):
#         return self.order_num


# class OrderProduct(db.Model):
#     id = db.Column(db.Integer, primary_key= True)
#     order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
#     order =db.Relationship('Orders', backref='order_order_products')
#     product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
#     product = db.Relationship('Products', backref='product_order_products')
#     quantity = db.Column(db.Integer)

#     def __repr__(self):
#         return f'{self.order.user.username} - {self.product.name}' 

# class UserAddress(db.Model):
#     id = db.Column(db.integer, primary_key= True)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     user =db.Relationship('Users', backref='user_user_addresses')
#     address1 = db.Column(db.String(150))
#     address2 = db.Column(db.String(150))
#     zipcode = db.Column(db.Integer)
#     country = db.Column(db.String(50))
#     city = db.Column(db.String(50))
#     phone = db.Column(db.Integer)

#     def __repr__(self):
#         return self.user.username

# class Payment(db.Model):
#     id = db.Column(db.integer, primary_key= True)
#     order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
#     order =db.Relationship('Orders', backref='order_payments')
#     paymant_date = db.Column(db.Date)
#     payment_type = db.Column(db.String(20))

#     def __repr__(self):
#         return self.order.order_id
