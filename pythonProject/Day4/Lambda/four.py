def variable(*arg):
    for i in arg:
        print(i)
variable(10,20,30,40)

variable= lambda *arg:[print(i) for i in arg]
variable(10,20,30,40)