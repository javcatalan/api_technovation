from itertools import product
from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app import app,db,allowed_file
from app.models import Users,Category,Products
from app.serializers import User_schema,Users_schema,Categoria_schema,Categorias_schema,Producto_schema,Productos_schema
from flask_cors import cross_origin

from werkzeug.utils import secure_filename
import os

#USUARIOS----------------------
#AGREGAR
@cross_origin
@app.route("/add_usuarios",methods=["POST"])
def add_usuarios():
    username=request.json['username']
    password=request.json['password']
    first_name=request.json['first_name']
    last_name=request.json['last_name']
    #phone_number=request.json['phone_number']
    mail=request.json['mail']
    #photo_user=request.json['photo_user']
    new_usuario=Users(username=username,password=password,mail=mail,first_name=first_name,last_name=last_name)#,,,phone_number=phone_number,,photo_user=photo_user
    db.session.add(new_usuario)
    db.session.commit()
    result=User_schema.dump(new_usuario)
    data ={
            'message':'Se Registro el usuario con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))

#AUTENTICAR USUARIO

@cross_origin
@app.route('/autenticar/<username>/<password>',methods=["POST"])
def autenticar(username,password):
    login=Users.query.filter_by(username=username,password=password).first()
    result=User_schema.dump(login)
    if login is not None:
        data ={
            'message':'Bienvenido',
            'status':200,
            'data':result
        }
    else:
        data ={
            'message':'Error',
            'status':200
            
        }
    return make_response(jsonify(data))  

#LISTAR USUARIO
    
@cross_origin
@app.route("/listar_usuarios",methods=["GET"])
def listar_usuarios():
    usuarios=Users.query.all()
    result=Users_schema.dump(usuarios)
    data={
        'message':'Todas mis usuarios',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

#BUSCAR USUARIO

@app.route('/user_search/<int:username>', methods=["GET"])
def user_search(username):
    usuario=Users.query.get(username)
    if usuario:
        result=User_schema.dump(usuario)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))

#ELIMINAR USUARIO

@app.route('/eliminar/<int:id>')#, methods=['DELETE'])
def eliminar(id):
    if not id or id !=0:
        usuario=Users.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return redirect('/')
    return "termino la eliminacion" 

#CATEGORIAS----------------------------------------

#AGREGAR CATEGORIA

@cross_origin
@app.route("/add_categorias",methods=["POST"])
def add_categoria():
    id=request.json['id']
    name=request.json['name']
    description=request.json['description']
    photo_categoria=request.json['photo_categoria']
    new_categoria=Category(id=id,name=name,description=description,photo_categoria=photo_categoria)
    db.session.add(new_categoria)
    db.session.commit()
    result=Categoria_schema.dump(new_categoria)
    data ={
            'message':'Se Registro la categoria con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))

 #VER CATEGORIAS
@cross_origin
@app.route("/listar_categorias",methods=["GET"])
def listar_categorias():
    categorias=Category.query.all()
    result=Categorias_schema.dump(categorias)
    data={
        'message':'Todas mis categorias',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

#BUSCAR CATEGORIA
@app.route('/category_search/<int:id>', methods=["GET"])
def category_search(id):
    categoria=Category.query.get(id)
    if categoria:
        result=Categoria_schema.dump(categoria)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))


#AGREGAR PRODUCTOS--------------------------------

@cross_origin
@app.route("/add_productos",methods=["POST"])
def add_productos():
    #id=request.json['id']
    name=request.json['name']
    #año_fabricacion=request.json['año_fabricacion']
    description=request.json['description']
    price=request.json['price']
    photo_product=request.json['photo_product']
    #category_id=request.json['category_id']
    new_producto=Products(name=name,description=description,price=price,photo_product=photo_product)
    db.session.add(new_producto)
    db.session.commit()
    result=Producto_schema.dump(new_producto)
    data ={
            'message':'Se Registro el producto con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))

            
#BUSCAR PRODUCTOS
@app.route('/product_search/<int:id>', methods=["GET"])
def product_search(id):
    producto=Products.query.get(id)
    if producto:
        result=Producto_schema.dump(producto)        
        data= {
        'message':'1',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'0',
            'status':200,
        }
    return make_response(jsonify(data))
    
#LISTAR PRODUCTOS
@cross_origin
@app.route("/listar_productos",methods=["GET"])
def listar_productos():
    productos=Products.query.all()
    result=Productos_schema.dump(productos)
    data={
        'message':'Todos mis productos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))      


#AGREGAR PRODUCTOS DESDE FORMULARIO
@app.route("/registrar_productos_view" , methods=["POST"])
def registrar_productos_view():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        name=request.form['name']
        description=request.form['description']
        price=request.form['price']
        new_producto=Products(name=name,price=price,photo_product=file.filename,description=description)
        db.session.add(new_producto)
        db.session.commit()
        result=Producto_schema.dump(new_producto)
        resp =jsonify({
            'message':'Se Registro el producto con exito',
            'status':200,
            'data':result
        })
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
        resp.status_code = 400
        return resp

# @cross_origin
# @app.route("/add_productos_view",methods=["POST"])
# def add_productos_views():
#     name=request.json['name']
#     photo_product=request.json['photo_product']
#     new_producto=Products(name=name,photo_product=photo_product)
#     db.session.add(new_producto)
#     db.session.commit()
#     result=Producto_schema.dump(new_producto)
#     data ={
#             'message':'Se Registro el producto con exito',
#             'status':200,
#             'data':result
#         }
#     return make_response(jsonify(data))