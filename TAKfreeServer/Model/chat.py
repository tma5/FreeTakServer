#######################################################
# 
# __chat.py
# Python implementation of the Class __chat
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:10 AM
# Original author: Corvo
# 
#######################################################
from Model.chatgrp import chatgrp


class chat:

      # default constructor       
    def __init__(self, chatType = None, senderCallsign = None, chatroom = None, groupOwner = None, id = None, parent = None, uid0 = None, uid1 = None):
        self.senderCallsign = senderCallsign
        self.id = id
        self.parent = parent
        self.chatgrp = chatgrp(chatType = chatType, uid0 = uid0, uid1 = uid1, id = id)


    def getparent(self): 
        return self.parent 

     # parent setter 
    def setparent(self,parent=0):  
        self.parent=parent 
    
    # senderCallsign getter 
    def getsenderCallsign(self):
        return senderCallsign 

    # senderCallsign setter 
    def setsenderCallsign(self,senderCallsignn):
        global senderCallsign
        senderCallsign=senderCallsignn 

      # chatroom getter 
    def getchatroom(self): 
        return self.chatroom 

    # chatroom setter 
    def setchatroom(self, chatroom=0):  
        self.chatroom=chatroom 

        # groupOwner getter 
    def getgroupOwner(self): 
        return self.groupOwner 

    # groupOwner setter 
    def setgroupOwner(self, groupOwner=0):  
        self.groupOwner=groupOwner 

      # id getter 
    def getid(self): 
        return self.id 

    # id setter 
    def setid(self, id=0):  
        self.id=id
    #chatgrp uid0 getter
    def getuid0(self):
      chatgrp().getuid0()
  
    def setuid0(self, uid0=0):
        chatgrp().setuid0(uid0)

    def getuid1(self):
        chatgrp().getuid1()
  
    def setuid1(self, uid1=0):
        chatgrp().setuid1(uid1)

    def getchatgrpid(self):
        chatgrp().getid()
  
    def setchatgrpid(self, id=0):
        chatgrp().setid(id)
