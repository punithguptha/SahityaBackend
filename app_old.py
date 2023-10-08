# from flask import Flask,request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import click
# from flask.cli import with_appcontext
# from pathlib import Path
# import os
# from dotenv import load_dotenv


# app= Flask(__name__)

# def create_app():
#     app=Flask(__name__)
#     app.debug=False
#     return app

# application=create_app()

# load_dotenv(Path("local.env"))

# user=os.getenv('user',None)
# password=os.getenv('password',None)
# host=os.getenv('host',None)
# database=os.getenv('database',None)

# print(user+" "+password+" "+host+" "+database)

# app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{user}:{password}@{host}/{database}'
# db=SQLAlchemy(app)

# @app.cli.command("init-db")
# @with_appcontext
# def init_db():
#     # Initialize the database
#     db.create_all()
#     click.echo("Initialized the database")

# class Entry(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     content=db.Column(db.String(200),nullable=False)




# db.create_all()
# print("After create all command")


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route('/add_entry',methods=['POST'])
# def add_entry():
#     try:
#         data=request.get_json()
#         content=data.get('content')
#         if not content:
#             return jsonify({'error':'Content is required'}),400
#         new_entry=Entry(content=content)
#         db.session.add(new_entry)
#         db.session.commit()
#         return jsonify({'message':'Entry added succesfully'}), 201
#     except Exception as e:
#         return jsonify({'error':str(e)}),500


# # if __name__=='__main__':
# #     db.create_all()
# #     print("Inside if condition")
# #     app.run(debug=True)