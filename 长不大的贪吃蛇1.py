import random
import pygame
import sys

hh='\DuanNingMaoBiXingShuWanZhengBan-2.ttf'

pygame.init()

bj=(0,0,0)

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('长不大的贪吃蛇')#标题
#图标
#img =pygame.image.load('\桌面\爆炸.ico')
#pygame.display.set_icon(img)

# 分数
score=0

n1=False
n2 = True
n3 = False

def tc():
    pygame.quit()
    sys.exit()
'''退出'''

class MyGame:
    def h(self):
        pygame.draw.rect(screen, ('blue'), (250, 250, 250, 60))
        
        font = pygame.font.Font(hh,50)
        font_s = font.render(str('开始游戏'), True, 'red')
        # 返回宽高
        w, h = font_s.get_size()
        screen.blit(font_s, (250 + 250 / 2 - w / 2, 250))
        pygame.display.update()
        global n2,n1
        while n2:
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.QUIT:
                    # print('退出')
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # '''获取鼠标按下是的坐标'''
                    a=pygame.mouse.get_pos()
                    # print(a)
                    if 250 <= a[0] <= 500 and 250 <= a[1] <= 310:
                        n2=False
                        n1=True
    '''————————————————开始游戏页面及功能————————————————'''
    
    def main(self):
        
        # 蛇的初始坐标
        s_x=420
        s_y=300
        # 速度
        snake_speed = 20
        
        direction = 'RIGHT'
        # 食物
        food_x=random.randint(0,39)*20
        food_y=random.randint(0,29)*20
        
        clock=pygame.time.Clock()
        global n1,n3,score
        while n1:
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                if event.type==pygame.QUIT:
                    # print('退出')
                    tc()
            
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                        # print('左')
                        direction = 'LEFT'
                    elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                        # print('右')
                        direction = 'RIGHT'
                    elif event.key == pygame.K_UP or event.key==pygame.K_w:
                        # print('上')
                        direction = 'UP'
                    elif event.key == pygame.K_DOWN or event.key==pygame.K_s:
                        direction = 'DOWN'
                        # print('下')
        
            if direction == 'LEFT':
                s_x -= snake_speed
                if s_x < 0:
                    s_x = 800
            elif direction == 'RIGHT':
                s_x += snake_speed
                if s_x > 800:
                    s_x = -20
            elif direction == 'UP':
                s_y -= snake_speed
                
            elif direction == 'DOWN':
                s_y += snake_speed
        
            screen.fill(bj)
            snake=pygame.draw.rect(screen, 'red', (s_x,s_y, 20, 20))
            food=pygame.draw.rect(screen, 'blue',(food_x,food_y,20,20))
            
            '''重新绘制食物'''
            if snake==food:
                score+=1
                food_x = random.randint(0, 39) * 20
                food_y = random.randint(0, 29) * 20
            
            
            '''判断蛇是否出界，出界绘制game over'''
            if s_y<0 or s_y > 600:
                screen.fill(bj)
                font = pygame.font.Font(hh,50)
                font_s = font.render(str('game over'), True, 'red')
                # 返回字宽高
                w, h = font_s.get_size()
                
                screen.blit(font_s, (400 - w / 2, 300 - h / 2))
                snake_speed = 0
                n1=False
                n3=True
            
            # if food_x==s_x and food_y==s_y:
                
                
            '''分数'''
            font_name = pygame.font.match_font("黑体")
            font = pygame.font.Font(font_name, 50)
            font_surface = font.render(str(score), True, 'red')
            screen.blit(font_surface, (screen.get_width() / 2, 10))
            
            pygame.display.update()
        
            clock.tick(10)
    '''__________________游戏内循环_________________'''
    
    def my(self):
        # my_game.fil()
        global n1,n3,score
        while n3:
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
                if event.type==pygame.QUIT:
                    # print('退出')
                    tc()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        n3=False
                        n1 = True
                        score = 0
            
    '''——————————————————重新开始功能————————————————————'''

    def tcs(self):
        while True:
            my_game.main()#游戏内循环
            my_game.my()#重新开始功能
            my_game.main()#游戏内循环
    '''——————————————————整个游戏的循环—————————————————'''
if __name__ == '__main__':
    my_game=MyGame()
    my_game.h()#开始游戏页面及功能
    my_game.tcs()#整个游戏的循环
    