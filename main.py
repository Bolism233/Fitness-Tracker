import pygame
from src.Control import Controller #import your controller

def main():
	pygame.init()
	team = {"lead": "Salmaan", "backend": "Shijun(Jay)", "frontend": "Lucas"}
	print("Software Lead is:", team["lead"])
	print("Backend is:", team["backend"])
	print("Frontend is:" , team["frontend"])
					#Create an instance on your controller object
    					#Call your mainloop
	c = Controller(900, 500)
	c.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 2 LINES OF CODE ######
main()

