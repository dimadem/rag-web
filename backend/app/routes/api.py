from flask import request, jsonify
from app.services.rag_service import process_question
from app.services.buffer.utils import clear_buffer
from . import api_bp

@api_bp.route('/ask', methods=['POST'])
def ask():
    print("frontend->> ", request.json)
    data = request.json
    question = data.get('question')
    context = data.get('context', None) #todo add context 

    response = process_question(question, context)
    clear_buffer()
    return jsonify({"response": response})