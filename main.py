from src.Control import Controller #import your controller

def main():
	team = {"lead": "Salmaan", "backend": "Shijun (Jay)", "frontend": "Lucas"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])				
    			
	c = Controller()		#Create an instance on your controller object
	c.mainloop()			#Call your mainloop

main()
