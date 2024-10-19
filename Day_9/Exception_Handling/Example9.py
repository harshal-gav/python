
def fun():
	try:
		f=open("Example9.py","r")
		for content in f:
			print(content)
		var=10/0
	except ZeroDivisionError as z:
		print("error is\t",z)
	except Exception as e:
		print("some other error\t",e)
	print("Done")
fun()


