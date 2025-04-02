to Run first run: "pip install -r requirements.txt"
and then "python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto"
then run: "python grpc_server.py"

after it connects to server, open a new terminal

then run: "python main.py" 
