import random
import pygame



class Button:
    def __init__(self, x , y, pos, width, height):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = width
        self.height = height
    

    def Clicked(self, pos):

        self.pos = pygame.mouse.get_pos()

        if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
            if self.pos[1] > self.x and self.pos[1] < self.u + self.height:

                return True
     
        return False


class RPSgame:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(960, 460)
        pygame.display.set_caption("RPS smasher")


        self.bg = pygame.image.load("background.jpg")
        self.r_button = pygame.image.load("r_button.png").convert_alpha()
        self.p_button = pygame.image.load("p_button.png").convert_alpha()
        self.s_button = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()



        self.screen.blit(self.bg,(0,0))
        self.screen.blit(self.r_btn,(20,500))
        self.screen.blit(self.p_btn,(330,500))
        self.screen.blit(self.s_btn,(640,500))


        self.rock_Btn = Button(30,520,(30,520),300,140)
        self.paper_Btn = Button(340,520,(340,520),300,140)
        self.scissors_Btn = Button(640,520,(640,520),300,140)


        self.font = pygame.font.Font(None,90)
        self.text = self.render("", True, (255,255,255))

        self.pl_score = 0
        self.pc_score = 0




def player(self):

    if self.rock_button.clicked(30):
        self.p_optioon = "Rock"
        self.screen.blit(self.choose_rock(120,200))



