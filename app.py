from solcx import compile_source, compile_files, install_solc
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def output(compilerVersion, output_values, myContract):

    install_solc(compilerVersion)

    method = 1 

    file_path = 'contracts/hello_world.sol'

    if (method == 1):
        compiled_sol = compile_source(
            myContract,
            output_values = output_values,
            solc_version = compilerVersion
        )
    elif (method == 2):
        compiled_sol = compile_files(
            [file_path],
            output_values = output_values,
            solc_version = compilerVersion
        )
    else:
        print("Wrong option")
        
    contract_id, contract_interface = compiled_sol.popitem()
    
    if len(output_values) == 2:
        both = dict()
        both['abi'] = contract_interface['abi']
        both ['bytecode'] = contract_interface['bin']
        return both
    elif output_values[0] == 'bin':
        bytecode = contract_interface['bin']
        return bytecode
    elif output_values[0] == 'abi':
        abi = contract_interface['abi']
        return abi

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/join', methods=['GET','POST'])

def my_form_post():
    compilerVersion = request.form['compilerVersion']
    binContract = request.form['bin']
    abiContract = request.form['abi']
    myContract = request.form['contract']

    output_values = []
    if abiContract == "true":
        output_values.append('abi')
    if binContract == "true":
        output_values.append('bin')

    op = str(output(compilerVersion, output_values, myContract))
    print(op)
    result = {
        "output": op
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)