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
		
		def get_formatted_input(self):
			sorted_input = [[],[]]
			for pair in self.input:
				sorted_input[0].append(int(pair[0]))
				sorted_input[1].append(int(pair[1]))
			sorted_input[0].sort()
			sorted_input[1].sort()

			return sorted_input

		def solve(self):
			sorted_input = self.get_formatted_input()

			total_distance = 0
			for pair_index in range(len(sorted_input[0] if sorted_input[0] < sorted_input[1] else sorted_input[1])):
				pair = [sorted_input[0][pair_index], sorted_input[1][pair_index]]
				total_distance += abs(pair[0] - pair[1])
			
			return total_distance