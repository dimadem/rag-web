from flask import request, jsonify
from app.services.rag_service import process_question
from . import api_bp

@api_bp.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    context = data.get('context', None)

    response = process_question(question, context)

    return jsonify({"response": response})