import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import math
from kivy.graphics import Color,Line,Ellipse,Rotate,Ellipse,PushMatrix,PopMatrix
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.graphics.vertex_instructions import Mesh
from kivy.core.window import Window
Window.clearcolor=[0.2,0.9,0.5,0.1]
from kivy.uix.video import Video
Window.fullscreen='auto'

class screen1(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
     
        with self.canvas:
            ##main screen
            Color(0,0.1,0.1)
            l=[x,y,0,0,x+200*w/200,y,0,0,x+200*w/200,y+100*h/400,0,0,x,y+100*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##shape for power button
            Color(0,0.2,0.2)
            l=[x+200*w/200,y,0,0,x+200*w/200,y-13*h/400,0,0,x+185*w/200,y-13*h/400,0,0,x+185*w/200,y,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##shape for guide button
            Color(0,0.2,0.2)
            l=[x+185*w/200,y,0,0,x+185*w/200,y-13*h/400,0,0,x+150*w/200,y-13*h/400,0,0,x+150*w/200,y,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            
            ##upperside3d
            Color(0.2,0.2,0.2)
            l=[x,y+100*h/400,0,0,x+200*w/200,y+100*h/400,0,0,x+180*w/200,y+105*h/400,0,0,x-10*w/200,y+105*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##leftside3d
            Color(0.2,0.2,0.2)
            l=[x,y,0,0,x,y+100*h/400,0,0,x-10*w/200,y+105*h/400,0,0,x-10*w/200,y+5*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##base of tv panel
            Color(0.3,0.15,0)
            l=[x-110*w/200,y-20*h/400,0,0,x-140*w/200,y-90*h/400,0,0,x+330*w/200,y-90*h/400,0,0,x+300*w/200,y-20*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##middle stand of tv (vertical  rectangular in yellow coloured shape)
            Color(1,1,0)
            l=[x+90*w/200,y,0,0,x+90*w/200,y-30*h/400,0,0,x+110*w/200,y-30*h/400,0,0,x+110*w/200,y,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##support for tv
            Color(0,0.1,0.1)
            l=[x+70*w/200,y-30*h/400,0,0,x+50*w/200,y-50*h/400,0,0,x+150*w/200,y-50*h/400,0,0,x+130*w/200,y-30*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##left side walls
            Color(0.3,0.15,0)
            l=[x-130*w/200,y-85*h/400,0,0,x-110*w/200,y-85*h/400,0,0,x-110*w/200,y+230*h/400,0,0,x-130*w/200,y+230*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side walls
            Color(0.3,0.15,0)
            l=[x+310*w/200,y-90*h/400,0,0,x+290*w/200,y-90*h/400,0,0,x+290*w/200,y+230*h/400,0,0,x+310*w/200,y+230*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##middle rectangle
            Color(0.62,0.31,0)
            l=[x-110*w/200,y+180*h/400,0,0,x+290*w/200,y+180*h/400,0,0,x+290*w/200,y+215*h/400,0,0,x-110*w/200,y+215*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##upper middle wall
            Color(0.3,0.15,0)
            l=[x-110*w/200,y+230*h/400,0,0,x-110*w/200,y+215*h/400,0,0,x+290*w/200,y+215*h/400,0,0,x+290*w/200,y+230*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

                    ##3d effect of left line of left side
            Color(0.44,0.21,0)
            l=[x-75*w/200,y-20*h/400,0,0,x-65*w/200,y-13*h/400,0,0,x-65*w/200,y+168*h/400,0,0,x-75*w/200,y+168*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

                    ##3d effect of right line of right side
            Color(0.44,0.21,0)
            l=[x+255*w/200,y-20*h/400,0,0,x+245*w/200,y-13*h/400,0,0,x+245*w/200,y+168*h/400,0,0,x+255*w/200,y+168*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            

            ##lower wall
            Color(0.3,0.15,0)
            l=[x-110*w/200,y+180*h/400,0,0,x-110*w/200,y+165*h/400,0,0,x+290*w/200,y+165*h/400,0,0,x+290*w/200,y+180*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##middle line
            Color(0.3,0.15,0)
            l=[x+90*w/200,y+230*h/400,0,0,x+96*w/200,y+230*h/400,0,0,x+96*w/200,y+180*h/400,0,0,x+90*w/200,y+180*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")


            ##side rectangle along wall
            Color(0.62,0.31,0)
            l=[x-110*w/200,y-20*h/400,0,0,x-80*w/200,y-20*h/400,0,0,x-80*w/200,y+165*h/400,0,0,x-110*w/200,y+165*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

              ##left line
            Color(0.3,0.15,0)
            l=[x-80*w/200,y-20*h/400,0,0,x-75*w/200,y-20*h/400,0,0,x-75*w/200,y+165*h/400,0,0,x-80*w/200,y+165*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

      

             ##left side cupboard line first 3d rectngle
            Color(0.44,0.21,0)
            l=[x-110*w/200,y+25*h/400,0,0,x-80*w/200,y+25*h/400,0,0,x-80*w/200,y+45*h/400,0,0,x-108*w/200,y+45*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

              ##left side cupboard line second 3d rectangle
            Color(0.44,0.21,0)
            l=[x-110*w/200,y+100*h/400,0,0,x-80*w/200,y+100*h/400,0,0,x-80*w/200,y+120*h/400,0,0,x-108*w/200,y+120*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            

            ##left side cupboard line first
            Color(0.3,0.15,0)
            l=[x-110*w/200,y+25*h/400,0,0,x-80*w/200,y+25*h/400,0,0,x-80*w/200,y+30*h/400,0,0,x-110*w/200,y+30*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

             ##left side cupboard line second
            Color(0.3,0.15,0)
            l=[x-110*w/200,y+100*h/400,0,0,x-80*w/200,y+100*h/400,0,0,x-80*w/200,y+105*h/400,0,0,x-110*w/200,y+105*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side rectangle
            Color(0.62,0.31,0)
            l=[x+290*w/200,y-20*h/400,0,0,x+260*w/200,y-20*h/400,0,0,x+260*w/200,y+165*h/400,0,0,x+290*w/200,y+165*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right line
            Color(0.3,0.15,0)
            l=[x+260*w/200,y-20*h/400,0,0,x+255*w/200,y-20*h/400,0,0,x+255*w/200,y+165*h/400,0,0,x+260*w/200,y+165*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side cupboard line first 3d rectngle
            Color(0.44,0.21,0)
            l=[x+290*w/200,y+25*h/400,0,0,x+260*w/200,y+25*h/400,0,0,x+260*w/200,y+45*h/400,0,0,x+288*w/200,y+45*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side cupboard line second 3d rectangle
            Color(0.44,0.21,0)
            l=[x+290*w/200,y+100*h/400,0,0,x+260*w/200,y+100*h/400,0,0,x+260*w/200,y+120*h/400,0,0,x+288*w/200,y+120*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side cupboard line first
            Color(0.3,0.15,0)
            l=[x+290*w/200,y+25*h/400,0,0,x+260*w/200,y+25*h/400,0,0,x+260*w/200,y+30*h/400,0,0,x+290*w/200,y+30*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##right side cupboard line second
            Color(0.3,0.15,0)
            l=[x+290*w/200,y+100*h/400,0,0,x+260*w/200,y+100*h/400,0,0,x+260*w/200,y+105*h/400,0,0,x+290*w/200,y+105*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
                        
            ##middle rectangle at lower in middle
            Color(0.63,0.31,0)
            l=[x-125*w/200,y-90*h/400,0,0,x+315*w/200,y-90*h/400,0,0,x+315*w/200,y-210*h/400,0,0,x-125*w/200,y-210*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ## tv panel 3d rectangle at lower side in left
            Color(0.44,0.21,0)
            l=[x-140*w/200,y-210*h/400,0,0,x-10*w/200,y-210*h/400,0,0,x-10*w/200,y-150*h/400,0,0,x-110*w/200,y-150*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

             ## tv panel 3d triangle at lower side in left
            Color(0.44,0.21,0)
            l=[x-140*w/200,y-210*h/400,0,0,x-110*w/200,y-150*h/400,0,0,x-125*w/200,y-90*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##tv panel stand lower side walls on left
            Color(0.3,0.15,0)
            l=[x-140*w/200,y-90*h/400,0,0,x-125*w/200,y-90*h/400,0,0,x-125*w/200,y-210*h/400,0,0,x-140*w/200,y-210*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")


               ## tv panel 3d rectangle at lower side in right
            Color(0.44,0.21,0)
            l=[x+330*w/200,y-210*h/400,0,0,x+176*w/200,y-210*h/400,0,0,x+176*w/200,y-150*h/400,0,0,x+300*w/200,y-150*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ## tv panel 3d triangle at lower side in right
            Color(0.44,0.21,0)
            l=[x+330*w/200,y-210*h/400,0,0,x+300*w/200,y-150*h/400,0,0,x+315*w/200,y-90*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##tv panel stand lower side walls on right
            Color(0.3,0.15,0)
            l=[x+330*w/200,y-90*h/400,0,0,x+315*w/200,y-90*h/400,0,0,x+315*w/200,y-210*h/400,0,0,x+330*w/200,y-210*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

             ##support of tv panel rectangle base
            Color(0.77,0.38,0)
            l=[x-140*w/200,y-90*h/400,0,0,x+330*w/200,y-90*h/400,0,0,x+330*w/200,y-100*h/400,0,0,x-140*w/200,y-100*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")

            ##tv panel stand lower side walls in middle
            Color(0.3,0.15,0)
            l=[x-125*w/200,y-210*h/400,0,0,x+315*w/200,y-210*h/400,0,0,x+315*w/200,y-190*h/400,0,0,x-125*w/200,y-190*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")


            ##tv panel stand lower side walls in middle rectangle
            Color(0.3,0.15,0)
            l=[x-10*w/200,y-190*h/400,0,0,x+180*w/200,y-190*h/400,0,0,x+180*w/200,y-140*h/400,0,0,x-10*w/200,y-140*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
             ##tv panel stand lower side walls in middle rectangle left side stand
            Color(0.3,0.15,0)
            l=[x-10*w/200,y-190*h/400,0,0,x-6*w/200,y-190*h/400,0,0,x-6*w/200,y-100*h/400,0,0,x-10*w/200,y-100*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")


            ##tv panel stand lower side walls in middle rectangle right side stand
            Color(0.3,0.15,0)
            l=[x+180*w/200,y-190*h/400,0,0,x+176*w/200,y-190*h/400,0,0,x+176*w/200,y-100*h/400,0,0,x+180*w/200,y-100*h/400,0,0]
            Mesh(vertices=l,indices=range(int(len(l)/4)),mode="triangle_fan")
            
            ##power button
            self.start=Button(size_hint=(0.015*w/200,0.023*h/400),pos=(x+182*w/200,y-13*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\power1.png',border=(0.5,0.5,0.5,0.5))
            self.add_widget(self.start)
            self.start.bind(on_press=self.to)
            
            self.fav=Button(text="Fav",size_hint=(0.032*w/200,0.025*h/400),pos=(x+145*w/200,y-13*h/400),color=(1,1,1,1),background_color=(0,255,255,0))
            self.add_widget(self.fav)
            self.fav.bind(on_press=self.sf)
    ##fav button functionality
    def sf(self,instance):
        
        self.cartoon1=Button(size_hint=(0.09,0.06),pos=(x+15*w/200,y+62*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\cartoon1.png',border=(0.5,0.5,0.5,0.5))
        self.add_widget(self.cartoon1)
        self.entertainment1=Button(size_hint=(0.09,0.06),pos=(x+15*w/200,y+21*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\entertainment.png',border=(0.5,0.5,0.5,0.5),background_color=(255,255,0,255))
        self.add_widget(self.entertainment1)
        self.exit=Button(text="EXIT",size_hint=(0.03*w/200,0.022*h/400),pos=(x+165*w/200,y+3*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.exit)
        self.cartoon1.bind(on_press=self.vd)
        self.entertainment1.bind(on_press=self.vo)
        self.exit.bind(on_press=self.sm)
        self.cartoon1.bind(on_press=self.sm)
        self.entertainment1.bind(on_press=self.sm)
         
    def sm(self,instance):
        
        self.cartoon1.disabled=True
        self.cartoon1.opacity=0
        self.entertainment1.disabled=True
        self.entertainment1.opacity=0
        self.exit.disabled=True
        self.exit.opacity=0
        ##cartoon video functionality
    def vd(self,instance):
        self.background = Video(source=r'C:\Users\Lenovo\Desktop\android\2.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.background)
        self.pause=Button(text="PAUSE",size_hint=(0.03*w/200,0.022*h/400),pos=(x,y+20*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.pause)
        self.play=Button(text="PLAY",size_hint=(0.03*w/200,0.025*h/400),pos=(x,y+35*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.play)
        self.stop=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop)
        self.pause.bind(on_press=self.ps)
        self.play.bind(on_press=self.pl)
        self.stop.bind(on_press=self.ex)
        self.stop.bind(on_press=self.rm)
        
    def ps(self,instance):
        self.background.state='pause'
    def pl(self,instance):
        self.background.state='play'
        self.background.play=True
    def ex(self,instance):
        self.background.state='stop'
        self.remove_widget(self.background)
    def rm(self,instance):
        self.pause.disabled=True
        self.pause.opacity=0
        self.play.disabled=True
        self.play.opacity=0
        self.stop.disabled=True
        self.stop.opacity=0
        ##entertainment video functionality
    def vo(self,instance):
        self.background1 = Video(source=r'C:\Users\Lenovo\Desktop\android\kapil.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.background1)
        self.stop1=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop1)
        self.stop1.bind(on_press=self.et)
        self.stop1.bind(on_press=self.rt)
    def et(self,instance):
        self.background1.state='stop'
        self.remove_widget(self.background1)
    def rt(self,instance):
        self.stop1.disabled=True
        self.stop1.opacity=0
    
       ##power button functionality     
    
    def to(self,instance):
    
        self.BACK=Button(text="BACK",size_hint=(0.024*w/200,0.02*h/400),pos=(x+170*w/200,y+3*h/400),color=(1,1,1,1),background_color=(255,0,255,0))
        self.add_widget(self.BACK)
        
        self.channel=Button(text="ALL CHANNELS",size_hint=(0.06*w/200,0.018*h/400),pos=(x+15*w/200,y+83*h/400),color=(1,1,1,1),background_color=(255,0,255,0))
        self.add_widget(self.channel)
        
        self.movie=Button(size_hint=(0.05,0.04),pos=(x+15*w/200,y+50*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\movie2.png',border=(0.5,0.5,0.5,0.5))
        self.add_widget(self.movie)
        self.entertainment=Button(size_hint=(0.052,0.042),pos=(x+15*w/200,y+20*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\entertainment.png',border=(0.5,0.5,0.5,0.5),background_color=(255,255,0,255))
        self.add_widget(self.entertainment)
        self.sports=Button(size_hint=(0.054,0.045),pos=(x+90*w/200,y+50*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\sports.png',border=(0.5,0.5,0.5,0.5))
        self.add_widget(self.sports)
        self.news=Button(size_hint=(0.057,0.045),pos=(x+90*w/200,y+20*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\news.png',border=(0.5,0.5,0.5,0.5))
        self.add_widget(self.news)
        self.cartoon=Button(size_hint=(0.05,0.04),pos=(x+150*w/200,y+45*h/400),background_normal=r'C:\Users\Lenovo\Desktop\android\cartoon1.png',border=(0.5,0.5,0.5,0.5))
        self.add_widget(self.cartoon)
        self.BACK.bind(on_press=self.al)
        self.movie.bind(on_press=self.al)
        self.entertainment.bind(on_press=self.al)
        self.sports.bind(on_press=self.al)
        self.news.bind(on_press=self.al)
        self.cartoon.bind(on_press=self.al)
        self.entertainment.bind(on_press=self.pd)
        self.movie.bind(on_press=self.dp)
        self.news.bind(on_press=self.di)
        self.sports.bind(on_press=self.ss)
        self.cartoon.bind(on_press=self.sh)
   
    def al(self,instance):
        self.BACK.disabled=True
        self.BACK.opacity=0
        self.movie.disabled=True
        self.movie.opacity=0
        self.entertainment.disabled=True
        self.entertainment.opacity=0
        self.sports.disabled=True
        self.sports.opacity=0
        self.news.disabled=True
        self.news.opacity=0
        self.cartoon.disabled=True
        self.cartoon.opacity=0
        self.channel.disabled=True
        self.channel.opacity=0
        ##entertainment video functioning
    def pd(self,instance):
        self.video = Video(source=r'C:\Users\Lenovo\Desktop\android\tmkoc.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.video)
        self.stop2=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop2)
        self.stop2.bind(on_press=self.ei)
        self.stop2.bind(on_press=self.ra)
    def ei(self,instance):
        self.video.state='stop'
        self.remove_widget(self.video)
    def ra(self,instance):
        self.stop2.disabled=True
        self.stop2.opacity=0
        ##movie video functionality
    def dp(self,instance):
        self.video1 = Video(source=r'C:\Users\Lenovo\Desktop\android\moviee.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.video1)
        self.stop3=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop3)
        self.stop3.bind(on_press=self.ee)
        self.stop3.bind(on_press=self.re)
    def ee(self,instance):
        self.video1.state='stop'
        self.remove_widget(self.video1)
    def re(self,instance):
        self.stop3.disabled=True
        self.stop3.opacity=0
      ##news button functionality
    def di(self,instance):
        self.video2 = Video(source=r'C:\Users\Lenovo\Desktop\android\news.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.video2)
        self.stop4=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop4)
        self.stop4.bind(on_press=self.eo)
        self.stop4.bind(on_press=self.ro)
    def eo(self,instance):
        self.video2.state='stop'
        self.remove_widget(self.video2)
    def ro(self,instance):
        self.stop4.disabled=True
        self.stop4.opacity=0
            ##sports video functionality
    
    def ss(self,instance):
        self.video3 = Video(source=r'C:\Users\Lenovo\Desktop\android\cricket.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.video3)
        self.stop5=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop5)
        self.stop5.bind(on_press=self.es)
        self.stop5.bind(on_press=self.rs)
    def es(self,instance):
        self.video3.state='stop'
        self.remove_widget(self.video3)
    def rs(self,instance):
        self.stop5.disabled=True
        self.stop5.opacity=0
        ##cartoonn  video functionality
    def sh(self,instance):
        self.video4 = Video(source=r'C:\Users\Lenovo\Desktop\android\shinchan.mpeg',play=True,state='play',size_hint=(0.78,0.16),pos_hint={'x':-0.095,'y':0.39})
        self.add_widget(self.video4)
        self.stop6=Button(text="EXIT",size_hint=(0.03*w/200,0.027*h/400),pos=(x+166*w/200,y+5*h/400),color=(1,0,0,1),background_color=(255,0,255,0))
        self.add_widget(self.stop6)
        self.stop6.bind(on_press=self.eh)
        self.stop6.bind(on_press=self.rh)
    def eh(self,instance):
        self.video4.state='stop'
        self.remove_widget(self.video4)
    def rh(self,instance):
        self.stop6.disabled=True
        self.stop6.opacity=0
        
class main(App):
    def build(self):
        return screen1()
            
x=250
y=300
w=300
h=500

main().run()
            
        


