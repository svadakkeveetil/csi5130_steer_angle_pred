import numpy as np
import pandas as pd
import pygame
import glob
from config import VisualizeConfig
import cv2

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

config = VisualizeConfig()
preds = pd.read_csv(config.pred_path)
true = pd.read_csv(config.true_path)
filenames = glob.glob(config.img_path)
filenames = sorted(filenames)

pygame.init()
size = (640, 480)
pygame.display.set_caption("Data viewer")
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
myfont = pygame.font.SysFont("monospace", 15)

# Set up the video writer using OpenCV
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
video_filename = 'output_video_rambo.avi'
fps = 20  # Frames per second

video_writer = cv2.VideoWriter(video_filename, fourcc, fps, size)

# Main loop
running = True
clock = pygame.time.Clock()

for i in range(2000):
#for i in range(len(filenames)):
    angle = preds["steering_angle"].iloc[i] # radians
    true_angle = true["steering_angle"].iloc[i] # radians
    
    # add image to screen
    img = pygame.image.load(filenames[i])
    screen.blit(img, (0, 0))
    
    # add text
    pred_txt = myfont.render("Prediction:" + str(round(angle* 57.2958, 3)), 1, (255,255,0)) # angle in degrees
    true_txt = myfont.render("True angle:" + str(round(true_angle* 57.2958, 3)), 1, (255,255,0)) # angle in degrees
    screen.blit(pred_txt, (10, 380))
    screen.blit(true_txt, (10, 400))

    # draw steering wheel
    radius = 50
    pygame.draw.circle(screen, WHITE, [320, 400], radius, 2) 

    # draw cricle for true angle
    x = radius * np.cos(np.pi/2 + true_angle)
    y = radius * np.sin(np.pi/2 + true_angle)
    pygame.draw.circle(screen, WHITE, [320 + int(x), 400 - int(y)], 7)
    
    # draw cricle for predicted angle
    x = radius * np.cos(np.pi/2 + angle)
    y = radius * np.sin(np.pi/2 + angle)
    pygame.draw.circle(screen, BLACK, [320 + int(x), 400 - int(y)], 5) 
    
    # Convert the Pygame screen to a numpy array
    frame = pygame.surfarray.array3d(screen)
    frame = np.transpose(frame, (1, 0, 2))  # Convert to the correct shape (height, width, channels)

    # Write the frame to the video
    video_writer.write(frame)

    #pygame.display.update()
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(fps)
    print(filenames[i])   

# Release the video writer and quit Pygame
video_writer.release()
pygame.quit()