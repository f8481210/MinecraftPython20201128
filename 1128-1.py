#1128-1
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#print('請問你要什麼方塊：') #印出來
#block = input('請問你要什麼方塊：')
#print(type(block))
block = int(input('請問你要什麼方塊：'))
#print(type(block))
x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,block)