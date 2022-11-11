#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:56:23 2022

@author: bhaveshjain
"""

#Code template taken from
#http://mininet.org/walkthrough/#changing-topology-size-and-type"


from mininet.topo import Topo
class MyTopo( Topo ):    
    "Simple topology example."    

    def build( self ):      
        "Create custom topo."        
        # Add hosts and switches       
        sa = self.addHost('A')        
        cd = self.addHost('D')             
        switch1 = self.addSwitch('R1')        
       
        
        # Add links        

        self.addLink(sa, switch1, bw=1000, delay='1ms',loss=5)        
        self.addLink(cd, switch1, bw=1000, delay='1ms',loss=5)        
     

        
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
