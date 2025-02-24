from flask import Blueprint,jsonify,request
from models import db,to_do_list
from datetime import datetime

api_bp=Blueprint('api',__name__)

@api_bp.route('/items',methods=['POST'])
def create_item():
    
    data=request.get_json()
    date_str = data.get('date')
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    new_item=to_do_list(title=data['title'],task=data['task'],date=date_obj)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'item added lol'}), 200

@api_bp.route('/items',methods=['GET'])
def get_all_items():
    items=to_do_list.query.all()
    return jsonify([{'id': item.id, 'title':item.title,'task': item.task, 'date': item.date,'done':item.done} for item in items]), 200

@api_bp.route('/items/<int:id>',methods=['PUT'])
def update_item(id):
    item=to_do_list.query.get_or_404(id)
    data=request.get_json()
    item.task=data.get('task',item.task)
    item.done=data.get('done',item.done)
    db.session.commit()
    return jsonify({'message': 'updated with success'}), 200

@api_bp.route('/items/<int:id>',methods=['DELETE'])
def delete_item(id):
    item=to_do_list.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'deleted with successfully'}), 200