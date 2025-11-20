import sys
if len(sys.argv)==3:
  script_name=sys.argv[0]
  name=sys.argv[1]
  rollno=sys.argv[2]
  print("user provided input values:")

else:
  script_name=sys.argv[0]
  name="AB"
  rollno="17"
  print("No input given --using default values:")
  
print("script Name:",script_name)
print("student Name:",name)
print("rollno:",rollno)
