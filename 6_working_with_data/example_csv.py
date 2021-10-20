import csv


def show_information_in_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # extracting information about rows
        header_rows = next(csv_reader)

        for idx_reader, line in enumerate(csv_reader):
            print(f"Record number {idx_reader + 1}")
            for idx_row, header_row in enumerate(header_rows):
                print(f"{header_row} - {line[idx_row]}")
            print()


def append_new_data_to_file(file_path):
    with open(file_path, 'r') as csv_in_file:
        csv_reader = csv.reader(csv_in_file)
        header_rows = next(csv_reader)

    new_info_line = [input(f"Enter new {header_row}: ")for header_row in header_rows]

    with open(file_path, 'a+', newline='') as csv_out_file:
        new_info_writer = csv.writer(csv_out_file)
        new_info_writer.writerow(new_info_line)


def delete_record_from_file(file_path):
    which_record_to_delete = int(input("Enter the number of record you want to delete: "))

    if which_record_to_delete == 0:
        print("Wrong number of record entered")
        return

    with open(file_path, 'r') as csv_in_file:
        reader = csv.reader(csv_in_file)
        lines = [row for row in reader]

        for idx, line in enumerate(lines):
            if which_record_to_delete == idx:
                lines.remove(line)
                break
        else:
            print("Could not find entered number of record")
            return

    with open(file_path, 'w', newline='') as csv_out_file:
        writer = csv.writer(csv_out_file)
        writer.writerows(lines)


def main_menu():
    file_path = "files/example_csv.csv"
    user_prompt = """
    Enter what you want to do with the CSV file
    1 - Show data in the file
    2 - Exit program
    3 - Append new data to the file
    4 - Delete a record from the file
    >> 
    """
    while True:
        user_answer = int(input(user_prompt))
        if user_answer == 1:
            show_information_in_csv(file_path)
        elif user_answer == 2:
            break
        elif user_answer == 3:
            append_new_data_to_file(file_path)
        elif user_answer == 4:
            delete_record_from_file(file_path)


if __name__ == '__main__':
    main_menu()


