from flask import Flask 
from flask import Flask, jsonify
from flask import request
app = Flask (__name__)

todos = [ { "label": "My first task", "done": False }, 
         {'label': 'Sample Todo 2','done': True}
          ]

@app.route('/todos', methods=['GET'])
def  hello_world():
  j_son = jsonify(todos)

  return j_son
@app.route('/todos',methods = ['POST'])
def add_new_todo():
   request_body = request.json
   print("Incoming request with the following body", request_body)
   todos.append(request_body)
  
   return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", 1)
    todos.pop(position)
    return jsonify(todos)

   
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)