import csv


class FileHandler:

    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.content = self.load_data_from_input_file()

    def load_data_from_input_file(self):
        temp_table = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_table.append(line)
        return temp_table

    def save_data_to_output_file(self):
        with open(self.output_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for line in self.content:
                writer.writerow(line)

    def modify(self):
        for modification in self.changes:
            modification_list = modification.split(",")
            column = int(modification_list[0])
            row = int(modification_list[1])
            value = modification_list[2]
            self.content[row][column] = value
