from flask import Blueprint,render_template
from flask import Flask,request, jsonify
from .models import *
from .models import db

bp=Blueprint('main',__name__)

@bp.route('/')
def home():
    return 'Hello, World!'


@bp.route('/add_entry',methods=['POST'])
def add_entry():
    try:
        data=request.get_json()
        content=data.get('content')
        if not content:
            return jsonify({'error':'Content is required'}),400
        new_entry=Entry(content=content)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message':'Entry added succesfully'}), 201
    except Exception as e:
        return jsonify({'error':str(e)}),500