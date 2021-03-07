import re


class RegexGenerator():

	def __init__(self,string_pattern_to_detect):
		print("inside regexGenerator")
		self.string_pattern_to_detect = string_pattern_to_detect
		self.regex_string = ""
		self.create_regex( )

		
	def create_regex(self):

		last_index_of_type = -1
		current_type = self.determine_char_type(self.string_pattern_to_detect[0])
		current_type_set = True
		
		for idx,char in enumerate(self.string_pattern_to_detect):

			#print(self.determine_char_type(char))
			#print(idx)
			
			last_index_of_type+=1
			if( (self.determine_char_type(char) != current_type) or idx == len(self.string_pattern_to_detect)-1 or self.determine_char_type(char) == "SPECIAL"):

				if( idx == len(self.string_pattern_to_detect)-1):
					last_index_of_type+=1
				
				if current_type == "DIGIT":
					self.regex_string+= ("\\d{"+str(last_index_of_type)+"}")
				elif current_type == "CHARACTER":
					self.regex_string+= ("\\w{"+str(last_index_of_type)+"}")
				elif current_type == "WHITESPACE":
					self.regex_string+= ("\\s{"+str(last_index_of_type)+"}")

				elif current_type == "SPECIAL":
					self.regex_string += "[" + self.string_pattern_to_detect[idx-1] + "]"

				current_type = self.determine_char_type(char)
				last_index_of_type = 0

				print(self.regex_string)

			
		


	def check_if_valid(self):

		print("returns true if the regex is correct.")

	def determine_char_type(self, char):

		if( char.isnumeric() ):
			return "DIGIT"
		elif( char.isalpha() ):
			return "CHARACTER"
		elif( char.isspace() ):
			return "WHITESPACE"
		else:
			return "SPECIAL"
