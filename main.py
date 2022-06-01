from solcx import compile_source, compile_files
contract = '''
    contract hello_world {
        string hello_string = "HELLO_WORLD!";
        function hello() view public returns (string memory) {
            return hello_string;
        }
    }
''' 
compiler_version = '0.8.14'

method = int(input("enter 1 for source or 2 for file:"))

file_path ='hello_world.sol'

if (method == 1):
    compile_sol = compile_source(
        contract,
        output_values=["abi"],
        solc_version = compile_version
    )
elif (method == 2):
    compile_sol = compile_files(
        [file_path],
        output_values=["abi"],
        solc_version = compile_version
    )
else:
    print("Wrong option")

print(compile_sol)