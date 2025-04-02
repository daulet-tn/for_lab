import pygame
from math import *
pygame.init()

fps = 120
timer = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
active_size = 0
active_color = 'white'
painting = []
current_tool = 'brush'  

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Paint")

def draw_menu(color, size):
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0,70), (WIDTH, 70))
    xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35,35), 20)
    l_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (95,35), 15)
    m_brush = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (155,35), 10)
    s_brush = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215,35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]
    
    pygame.draw.circle(screen, color, (400,35),30)
    blue = pygame.draw.rect(screen, (0,0,255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255,0,0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0,255,0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255,255,0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0,255,255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255,0,255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255,255,255), [WIDTH - 110, 10, 25, 25])  
    black = pygame.draw.rect(screen, (0,0,0), [WIDTH - 110, 35, 25, 25])
    circle_button = pygame.draw.rect(screen, 'black', [250, 10, 50, 50]) 
    pygame.draw.circle(screen, 'white', (275, 35), 20)
    rectangle_button = pygame.draw.rect(screen, 'black', [310, 10, 50, 50]) 
    pygame.draw.rect(screen, 'white', [315, 15, 40, 40])
    righttriangle_button = pygame.draw.rect(screen, 'black', [450, 10, 50, 50]) 
    pygame.draw.polygon(screen, "white", [(475,15), (455,50), (495,50)])
    square_button = pygame.draw.rect(screen, 'black', [510, 10, 50, 50])
    pygame.draw.rect(screen, 'white', [520, 20, 30, 30])
    equilateral_triangle = pygame.draw.rect(screen, 'black', [570, 10, 50, 50])
    pygame.draw.polygon(screen, "white", [(595,15), (580,50), (610,50)])
    rhombus_button = pygame.draw.rect(screen, 'black', [630, 10, 50, 50])
    pygame.draw.polygon(screen, "white", [(655, 10), (630, 35), (655, 60), (680, 35)])
    color_rect = [blue, red, green, yellow, teal, purple, white, black, circle_button, rectangle_button, righttriangle_button, square_button, equilateral_triangle, rhombus_button]  
    rgb_list = [(0,0,255), (255,0,0), (0,255,0), (255,255,0), (0,255,255), (255,0,255), 
                (255,255,255), (0,0,0), None, None, None, None, None, None] 
    
    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        if paints[i][0] == 'circle':  
            pygame.draw.circle(screen, paints[i][1], paints[i][2], paints[i][3])
        elif paints[i][0] == 'rectangle':  
            pygame.draw.rect(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'righttriangle':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2]) 
        elif paints[i][0] =='square':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'equilateral_triangle':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])
        elif paints[i][0] == 'rhombus':
            pygame.draw.polygon(screen, paints[i][1], paints[i][2])
        else:
            pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
    
running = True
while running:
    timer.tick(fps)
    screen.fill("white")
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if left_click and mouse[1] > 70: # Не рисуем по меню
        if current_tool == 'brush':  
            painting.append((active_color, mouse, active_size))
        elif current_tool == 'circle':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos
                    radius = ((pos[0] - startPos[0])**2 + (pos[1] - startPos[1])**2)**0.5
                    pygame.draw.circle(screen, active_color, (startPos[0], startPos[1]), radius)
                    painting.append(('circle', active_color, (startPos[0], startPos[1]), radius))
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
        elif current_tool == 'rectangle':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    points = []
                    pos = event.pos
                    width = abs(pos[0] - startPos[0])
                    height = abs(pos[1] - startPos[1])
                    X1 = min(pos[0], startPos[0])
                    Y1 = min(pos[1], startPos[1])
                    points.append((X1))
                    points.append((Y1))
                    points.append((width))
                    points.append((height))
                    pygame.draw.rect(screen, active_color, points)
                    painting.append(('rectangle', active_color, points))
        
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
                current_tool = 'brush'

        elif current_tool == 'righttriangle':
            points = []
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos
                    a = abs(((pos[0] - startPos[0])**2 + (pos[1] - startPos[1])**2)**0.5)
                    points.append((pos[0], pos[1]))
                    points.append((abs(startPos[0] + sqrt(3)*a), startPos[1]))
                    points.append((abs(startPos[0]-sqrt(3)*a/2),abs(startPos[1] - a/2)))
                    pygame.draw.polygon(screen, active_color, points)
                    painting.append(('righttriangle', active_color,points))
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
                current_tool = 'brush'
        elif current_tool == 'square':
            points = []
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos
                    a = abs(((pos[0] - startPos[0])**2 + (pos[1] - startPos[1])**2)**0.5)
                    points.append(((startPos[0]),(startPos[1]))) # x1
                    points.append(((startPos[0]), (startPos[1] - a))) # x3
                    points.append(((startPos[0] + a), (startPos[1] - a))) # x4
                    points.append(((startPos[0] + a), startPos[1])) # x2
                    pygame.draw.polygon(screen, active_color, points)
                    painting.append(('square', active_color, points))
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
                current_tool = "brush"
        elif current_tool == 'equilateral_triangle':
            points = []
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                startPos = event.pos
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    pos = event.pos
                    a = abs(((pos[0] - startPos[0])**2 + (pos[1] - startPos[1])**2)**0.5)
                    points.append(((startPos[0]),startPos[1])) # x1
                    points.append(((pos[0] - (pos[0] - startPos[0])), (pos[1] - a))) # x2
                    points.append(((pos[0] + (pos[0] - startPos[0])), (pos[1] - a))) # x3
                    pygame.draw.polygon(screen, active_color, points)
                    painting.append(('equilateral_triangle', active_color, points))
            if event.type == pygame.MOUSEBUTTONUP:  
                drawStarted = False
                current_tool = "brush"
        elif current_tool == 'rhombus':
            points = []
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                drawStarted = True
                start_vertex = event.pos  # Начальная вершина
            if event.type == pygame.MOUSEMOTION:
                if drawStarted:
                    opposite_vertex = event.pos  # Противоположная вершина
                    # Находим координаты середины диагонали
                    diagonal_midpoint = ((start_vertex[0] + opposite_vertex[0]) / 2, (start_vertex[1] + opposite_vertex[1]) / 2)
                    # Находим координаты одной из сторон ромба, находящейся на том же расстоянии от середины диагонали
                    side_vertex = (diagonal_midpoint[0] + (opposite_vertex[1] - start_vertex[1]), diagonal_midpoint[1] - (opposite_vertex[0] - start_vertex[0]))
                    # Находим координаты второй стороны ромба
                    side_vertex_2 = (diagonal_midpoint[0] - (opposite_vertex[1] - start_vertex[1]), diagonal_midpoint[1] + (opposite_vertex[0] - start_vertex[0]))
                    # Отрисовываем ромб на экране
                    pygame.draw.polygon(screen, active_color, [start_vertex, opposite_vertex, side_vertex, side_vertex_2])
                    # Добавляем ромб в список рисунков
                    painting.append(('rhombus', active_color, [start_vertex, side_vertex,opposite_vertex, side_vertex_2]))
            if event.type == pygame.MOUSEBUTTONUP:
                drawStarted = False
                current_tool = "brush"
    draw_painting(painting)
    if mouse[1] > 70 and current_tool == 'brush':  
        pygame.draw.circle(screen, active_color, mouse, active_size)
    brushes, colors, rgbs = draw_menu(active_color, active_size)
         
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 20 - (i * 5)
                    
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    if rgbs[i] is not None:
                        active_color = rgbs[i]
                    else:
                        if i == len(colors) - 6:  
                            current_tool = 'circle'
                        elif i == len(colors) - 5:
                            current_tool = 'rectangle' 
                        elif i == len(colors) - 4:  
                            current_tool = 'righttriangle'
                        elif i == len(colors) - 3:
                            current_tool ='square'
                        elif i == len(colors) - 2:
                            current_tool = 'equilateral_triangle'
                        elif i == len(colors) - 1:
                            current_tool = 'rhombus'  
    pygame.display.flip()
    
pygame.quit()