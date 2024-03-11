import sys
from file_handler import FileHandler


def load_system_arguments():
    arguments = sys.argv
    return sys.argv[1], sys.argv[2], sys.argv[3:]


print(len(sys.argv))
if len(sys.argv) >= 3:
    input_file, output_file, changes = load_system_arguments()

    file_handler = FileHandler(input_file, output_file, changes)
    print(input_file)
    print(output_file)
    print(changes)

    file_handler.modify()
    file_handler.save_data_to_output_file()
else:
    print("You provided too many or less arguments than expected (3)")
