import os.path


separator = " "


def find_files_recursively(start_dir, depth=1):
	last_element_of_dir = start_dir.split("\\")[-1]

	print(f"{separator * (depth - 1)}{last_element_of_dir}")

	directories_to_traverse = []
	for element in os.listdir(start_dir):
		if not os.path.isdir(os.path.join(start_dir, element)):
			print(f"{separator * depth}{element}")
		else:
			directories_to_traverse.append(element)

	for directory_to_traverse in directories_to_traverse:
		find_files_recursively(os.path.join(start_dir, directory_to_traverse), depth + 1)


if __name__ == '__main__':
	starting_directory = "example_files"
	find_files_recursively(starting_directory)
