import os.path


def print_with_tabulation(path, depth):
	print("\t" * depth + path)


def find_files_recursively(start_dir, depth=1):
	last_element_of_dir = start_dir.split("\\")[-1]
	print_with_tabulation(last_element_of_dir, depth - 1)
	for element in os.listdir(start_dir):
		if not os.path.isdir(os.path.join(start_dir, element)):
			print_with_tabulation(element, depth)
		else:
			find_files_recursively(os.path.join(start_dir, element), depth + 1)


if __name__ == '__main__':
	starting_directory = "example_files"
	find_files_recursively(starting_directory)
