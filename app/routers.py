from unittest import result
from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app import app,db,allowed_file
from app.models import usuarios,camino_mesa,calzado,servilletas,manteles,telas_tipicas,sandalias,tenis,tacones,blusas,faldas,categorias
from app.serializers import usuario_schema,usuarios_schema,camino_shema,caminos_shema,servilleta_shema,servilletas_shema,calzado_schema,manteles_shema,manteles_shema,telatipica_shema,telastipicas_shema,sandalia_shema,sandalias_shema,onetenis_shema,tenis_shema,tacon_shema,tacones_shema,blusa_shema,blusas_shema,falda_shema,faldas_shema, calzados_schema,categoria_schema,categorias_schema
from flask_cors import cross_origin

from werkzeug.utils import secure_filename
import os

############################
#LISTAR PRODUCTOS

@cross_origin
@app.route('/listar_camino_mesa',methods=["GET"])
def listar_camino_mesa():
    allcamino_mesa=camino_mesa.query.all()
    result=caminos_shema.dump(allcamino_mesa)
    data={
        'message':'todos los caminos de mesa',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_sevilletas',methods=["GET"])
def listar_servilletas():
    allservilleta=servilletas.query.all()
    result=servilletas_shema.dump(allservilleta)
    data={
        'message':'todas las servilletas',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_manteles',methods=["GET"])
def listar_manteles():
    allmanteles=manteles.query.all()
    result=manteles_shema.dump(allmanteles)
    data={
        'message':'todos los manteles',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_telas_tipicas', methods=["GET"])
def listar_telas_tipicas():
    alltelas=telas_tipicas.query.all()
    result=telastipicas_shema.dump(alltelas)
    data={
        'message':'todas las telas tipicas',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route ('/listar_sandalias',methods=["GET"])
def listar_sandalias():
    allsandalias=sandalias.query.all()
    result=sandalias_shema.dump(allsandalias)
    data={
        'message':'todas las sandalias',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data)
    )

@cross_origin
@app.route ('/listar_tenis',methods=["GET"])
def listar_tenis():
    alltenis=tenis.query.all()
    result=tenis_shema.dump(alltenis)
    data={
        'message':'todos los tenis',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_tacones',methods=["GET"])
def listar_tacones():
    alltacones=tacones.query.all()
    result=tacones_shema.dump(alltacones)
    data={
        'message':'todos los tacones',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_blusas',methods=["GET"])
def listar_blusas():
    allblusas=blusas.query.all()
    result=blusas_shema.dump(allblusas)
    data={
        'message':'todas las blusas',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

@cross_origin
@app.route('/listar_faldas',methods=["GET"])
def listar_faldas():
    allfladas=faldas.query.all()
    result=faldas_shema.dump(allfladas)
    data={
        'message':'todas las faldas',
        'status':200,
        'data':result
    }
    return make_response (jsonify(data))
@cross_origin
@app.route("/listar_calzado",methods=["GET"])
def listar_calzado():
    calzados=calzado.query.all()
    result=calzados_schema.dump(calzados)
    data={
        'message':'Todas mis categorias',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))



###################################

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
    new_usuario=usuarios(username=username,password=password,mail=mail,first_name=first_name,last_name=last_name)#,,,phone_number=phone_number,,photo_user=photo_user
    db.session.add(new_usuario)
    db.session.commit()
    result=usuario_schema.dump(new_usuario)
    data ={
            'message':'Se Registro el usuario con exito',
            'status':200,
            'data':result
        }
    return make_response(jsonify(data))

# #LISTAR USUARIO
@cross_origin
@app.route("/listar_usuarios",methods=["GET"])
def listar_usuarios():
    usuario=usuarios.query.all()
    result=usuarios_schema.dump(usuario)
    data={
        'message':'Todos mis usuarios',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))


#BUSCAR USUARIO

@app.route('/user_search/<nombre_usuario>', methods=["GET"])
def user_search(nombre_usuario):
    usuario=usuarios.query.filter_by(nombre_usuario=nombre_usuario).first()
    if usuario:
        result=usuario_schema.dump(usuario)        
        data= {
        'message':'usuario encontrado con exito',
        'status':200,
        'data':result
            }
    else:
        data = {
            'message':'usuario no encontrado',
            'status':400,
        }
    return make_response(jsonify(data))

# #ELIMINAR USUARIO

@app.route('/eliminar/<int:id>', methods=['DELETE']) #arreglar 
def eliminar(id):
    if not id or id !=0:
        usuario=usuarios.query.get(id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return redirect('/')
    return "termino la eliminacion" 

#AUTENTICAR USUARIO

@cross_origin
@app.route('/autenticar/<username>/<password>',methods=["POST"])
def autenticar(nombre_usuario,contraseña):
    login=usuarios.query.filter_by(username=nombre_usuario,password=contraseña).first()
    result=usuario_schema.dump(login)
    if login is not None:
        data ={
            'message':'Bienvenido',
            'data':result
        }
    else:
        data ={
            'message':'Error',
            'status':200
            
        }
    return make_response(jsonify(data))  


    

# #CATEGORIAS----------------------------------------


 #VER CATEGORIAS
@cross_origin
@app.route("/listar_categorias",methods=["GET"])
def listar_categorias():
    categoria=categorias.query.all()
    result=categorias_schema.dump(categoria)
    data={
        'message':'Todas mis categorias',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

# #AGREGAR CATEGORIA

# @cross_origin
# @app.route("/add_categorias",methods=["POST"])
# def add_categoria():
#     id=request.json['id']
#     name=request.json['name']
#     description=request.json['description']
#     photo_categoria=request.json['photo_categoria']
#     new_categoria=categorias(id=id,name=name,description=description,photo_categoria=photo_categoria)
#     db.session.add(new_categoria)
#     db.session.commit()
#     result=categoria_schema.dump(new_categoria)
#     data ={
#             'message':'Se Registro la categoria con exito',
#             'status':200,
#             'data':result
#         }
#     return make_response(jsonify(data))




# #BUSCAR CATEGORIA
# @app.route('/category_search/<int:id>', methods=["GET"])
# def category_search(id):
#     categoria=categorias.query.get(id)
#     if categoria:
#         result=categoria_schema.dump(categoria)        
#         data= {
#         'message':'1',
#         'status':200,
#         'data':result
#             }
#     else:
#         data = {
#             'message':'0',
#             'status':200,
#         }
#     return make_response(jsonify(data))


# #AGREGAR PRODUCTOS--------------------------------

# @cross_origin
# @app.route("/add_productos",methods=["POST"])
# def add_productos():
#     #id=request.json['id']
#     name=request.json['name']
#     #año_fabricacion=request.json['año_fabricacion']
#     description=request.json['description']
#     price=request.json['price']
#     photo_product=request.json['photo_product']
#     #category_id=request.json['category_id']
#     new_producto=Products(name=name,description=description,price=price,photo_product=photo_product)
#     db.session.add(new_producto)
#     db.session.commit()
#     result=Producto_schema.dump(new_producto)
#     data ={
#             'message':'Se Registro el producto con exito',
#             'status':200,
#             'data':result
#         }
#     return make_response(jsonify(data))

            
# #BUSCAR PRODUCTOS
# @app.route('/product_search/<int:id>', methods=["GET"])
# def product_search(id):
#     producto=Products.query.get(id)
#     if producto:
#         result=Producto_schema.dump(producto)        
#         data= {
#         'message':'1',
#         'status':200,
#         'data':result
#             }
#     else:
#         data = {
#             'message':'0',
#             'status':200,
#         }
#     return make_response(jsonify(data))
    
# #LISTAR PRODUCTOS
# @cross_origin
# @app.route("/listar_productos",methods=["GET"])
# def listar_productos():
#     productos=Products.query.all()
#     result=Productos_schema.dump(productos)
#     data={
#         'message':'Todos mis productos',
#         'status':200,
#         'data':result
#     }
#     return make_response(jsonify(data))      


# #AGREGAR PRODUCTOS DESDE FORMULARIO
# @app.route("/registrar_productos_view" , methods=["POST"])
# def registrar_productos_view():
#     if 'file' not in request.files:
#         resp = jsonify({'message' : 'No file part in the request'})
#         resp.status_code = 400
#         return resp
#     file = request.files['file']
#     if file.filename == '':
#         resp = jsonify({'message' : 'No file selected for uploading'})
#         resp.status_code = 400
#         return resp
#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         name=request.form['name']
#         description=request.form['description']
#         price=request.form['price']
#         new_producto=Products(name=name,price=price,photo_product=file.filename,description=description)
#         db.session.add(new_producto)
#         db.session.commit()
#         result=Producto_schema.dump(new_producto)
#         resp =jsonify({
#             'message':'Se Registro el producto con exito',
#             'status':200,
#             'data':result
#         })
#         resp.status_code = 201
#         return resp
#     else:
#         resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
#         resp.status_code = 400
#         return resp

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
