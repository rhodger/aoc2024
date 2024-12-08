import re

from Solution.solution import Solution

class SolutionD1C1(Solution):
		@staticmethod
		def load_input(input_file_location):
			try:
				with open(input_file_location, 'r') as file:
					content = file.readlines()
				formatted_content = []
				for line in content:
					nums = re.findall(r'\d+', line)
					if len(nums) != 2:
						print(f"Invalid line in input: {line}")
						return None
					else:
						formatted_content.append(nums)
				return formatted_content
			except FileNotFoundError:
				print(f"Error: File '{input_file_location}' not found.")
				return None
			except Exception as e:
				print(f"An error occurred: {e}")
				return None
		
		def solve(self):
			print(self.input)
			return 69