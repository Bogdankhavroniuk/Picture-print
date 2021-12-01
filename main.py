
import pygame
import numpy as np


class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Z = create_image()
            surf = pygame.surfarray.make_surface(Z)
            self.display.blit(surf, (0, 0))




            pygame.display.update()

        pygame.quit()

def  buffering_line(line):
    buf = []
    b = ""
    for c in range(0, len(line)):


       if line[c] == " " :
           buf.append(int(b))
           b = ""
       if  c == len(line)-1:
           b = b + line[c]
           buf.append(int(b))
       else:
            b = b + line[c]

    return buf



def create_image():
   a = 0
   file1 = open('DS3.txt', 'r')
   start_list=[]
   while True:
           line = file1.readline()
           if buffering_line(line) != []:
             start_list.append(buffering_line(line))
           if not line:
               break

   mas = np.zeros((960,540,3))

   for  a in  start_list:

          mas[a[0]][a[1]][:]=255

   print(mas[78][434])
   return mas


def update():
    image = create_image()

    return image.astype('uint8')

def main():
    viewer = Viewer(update(), (540, 960))
    viewer.start()


if __name__ == '__main__':
   main()


