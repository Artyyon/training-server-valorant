from flask import Flask, render_template, request, jsonify
import json
import os


app = Flask(__name__)


# Caminho para a pasta de arquivos de treinamento
trainings_folder_path = 'trainings/'
json_file_path = os.path.join(trainings_folder_path, 'trainings.json')


# Função para carregar os dados do arquivo JSON
def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Função para salvar os dados no arquivo JSON
def save_data_to_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


# Função para listar arquivos na pasta de treinamento
def list_training_files(folder_path):
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.json')]


# Rota principal para exibir a página inicial
@app.route('/')
def index():
    data = load_data_from_json(json_file_path)
    training_files = list_training_files(trainings_folder_path)
    return render_template('index.html', trainings=data['trainings'], training_files=training_files)


# Rota para carregar dados do arquivo de treinamento selecionado
@app.route('/load-training/<filename>', methods=['GET'])
def load_training(filename):
    file_path = os.path.join(trainings_folder_path, filename)
    if os.path.exists(file_path):
        data = load_data_from_json(file_path)
        return jsonify(data['trainings'])
    else:
        return jsonify({'error': 'File not found'}), 404


# Rota para atualizar contadores
@app.route('/update-counter', methods=['POST'])
def update_counter():
    data = load_data_from_json(json_file_path)
    training_id = int(request.json['training_id'])
    counter_id = int(request.json['counter_id'])

    # Atualiza o contador
    for training in data['trainings']:
        if training['id'] == training_id:
            for counter in training['counters']:
                if counter['id'] == counter_id:
                    counter['count'] += 1
                    if counter['count'] > counter['max_count']:
                        counter['count'] = counter['max_count']
                    break

    save_data_to_json(json_file_path, data)
    return jsonify({'message': 'Counter updated successfully!'})


# Rota para resetar contadores
@app.route('/reset-counter', methods=['POST'])
def reset_counter():
    data = load_data_from_json(json_file_path)
    training_id = int(request.json['training_id'])
    counter_id = int(request.json.get('counter_id', -1))

    # Resetar o contador
    for training in data['trainings']:
        if training['id'] == training_id:
            if counter_id == -1:
                for counter in training['counters']:
                    counter['count'] = 0
            else:
                for counter in training['counters']:
                    if counter['id'] == counter_id:
                        counter['count'] = 0
                        break

    save_data_to_json(json_file_path, data)
    return jsonify({'message': 'Counters reset successfully!'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')