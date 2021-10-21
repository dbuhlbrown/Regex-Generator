import re


class RegexGenerator():

	def __init__(self,string_pattern_to_detect):
		self.string_pattern_to_detect = string_pattern_to_detect
		self.regex_string = ""
		self.create_regex( )

		
	def create_regex(self):

		last_index_of_type = -1
		current_type = self.determine_char_type(self.string_pattern_to_detect[0])
		current_type_set = True
		
		for idx,char in enumerate(self.string_pattern_to_detect):
			
			last_index_of_type+=1

			if( (self.determine_char_type(char) != current_type) or self.determine_char_type(char) == "SPECIAL"):

				self.set_regex_strings(current_type,last_index_of_type,idx)

				current_type = self.determine_char_type(char)
				last_index_of_type = 0

				#This if only triggers if the last char is of a different type than the previous.
				#This is an easy fix to the problem of detecting strings like 'AA0' and 'BB1'.
				if(idx == len(self.string_pattern_to_detect) - 1):

					last_index_of_type+=1
					self.set_regex_strings(current_type,last_index_of_type,idx)
		
			#Since the way this works requires a different char to end the pattern,
			#the last character can never be properly accounted for.
			#This mean something like 'aaaa' will return nothing. Because there is no
			#different char. We can fix this by testing if it's the last index and if it's the
			#same type as the previous.
			if( idx == len(self.string_pattern_to_detect) - 1 and current_type == self.determine_char_type(self.string_pattern_to_detect[idx-1])):
				last_index_of_type+=1
				self.set_regex_strings(current_type,last_index_of_type,idx)

	def get_regex(self):
		return self.regex_string
		

	def set_regex_strings(self,current_type,last_index_of_type,idx):
		if current_type == "DIGIT":
			self.regex_string+= ("\\d{"+str(last_index_of_type)+"}")
		elif current_type == "CHARACTER":
			self.regex_string+= ("\\w{"+str(last_index_of_type)+"}")
		elif current_type == "WHITESPACE":
			self.regex_string+= ("\\s{"+str(last_index_of_type)+"}")
		elif current_type == "SPECIAL":
			self.regex_string += "[" + self.string_pattern_to_detect[idx-1] + "]"

	#not yet implemented
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

#Easy test code for self contained runs.
#myGen = RegexGenerator("2021-05-26T20:52:38.000Z")
#myGen = RegexGenerator("aaaa0aaaa")
#print(myGen.get_regex())