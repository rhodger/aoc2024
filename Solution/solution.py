class Solution:
	@staticmethod
	def load_input(input_file_location):
		try:
			with open(input_file_location, 'r') as file:
				content = file.read()
			return content
		except FileNotFoundError:
			print(f"Error: File '{input_file_location}' not found.")
			return None
		except Exception as e:
			print(f"An error occurred: {e}")
			return None
	
	def solve(self):
		print("Unimplemented")

	def __init__(self, input_file_location):
		self.input = self.load_input(input_file_location)