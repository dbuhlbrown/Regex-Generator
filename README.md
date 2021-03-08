# Regex-Generator
This project was created as an experiment to see how accurately I can generate valid regex when simply given a string(s) to match. 

#How to use

#Basic Example:

from RegexGenerator import RegexGenerator

myRegexGenerator = RegexGenerator("123-555-7676")

print(myRegexGenerator).get_regex()

#Expected Output:

\d{3}[-]\d{3}[-]\d{4}