from app import db

    
class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True) #autoincrement=True
    username=db.Column(db.String(15), unique=True)
    password=db.Column(db.String(25))
    first_name=db.Column(db.String(15))
    last_name=db.Column(db.String(15))
    phone_number=db.Column(db.String(20))
    mail = db.Column(db.String(100), unique=True)
    photo_user=db.Column(db.String(120))
    
    def __repr__(self):
        return self.username


class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    description=db.Column(db.String(250))
    items = db.relationship('products', backref='product_category', lazy='dynamic')
    
    def __repr__(self):
        return self.name

class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)#autoincrement=True
    name=db.Column(db.String(50))
    description=db.Column(db.String(1000))    
    category_id=db.Column(db.Integer,db.ForeignKey('Category.id'))
    category =db.Relationship('Category', backref='category_products')
    price=db.Column(db.Float)
    photo_product=db.Column(db.String(120))
    #discount_price=db.Column(db.Float)
    
    def __repr__(self):
        return self.name

# class Tallas(db.Model):
#     id=db.Column(db.Integer,primay_key=True) 
#     tallas=db.Column(db.Integer)
#     descripcion=db.Column(db.String(50))
#     products_id=db.Column(db.Integer,db.ForeignKey('Products.id'))
#     products=db.Relationship('Products', backref='products_tallas')

#     def __repr__(self):
#         return self.name


#===================================================================================================
# class Orders(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     user =db.Relationship('Users', backref='users_orders')
#     order_num = db.Column(db.String(50), unique=True)
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
