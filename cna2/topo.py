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
        cb = self.addHost('B')        
        cc = self.addHost('C')        
        cd = self.addHost('D')        
        switch1 = self.addSwitch('R1')        
        switch2 = self.addSwitch('R2')        
        
        # Add links        
        self.addLink(switch2, cb, bw=1000, delay='1ms')        
        self.addLink(switch2, cc, bw=1000, delay='5ms')
        self.addLink(sa, switch1, bw=1000, delay='1ms')        
        self.addLink(cd, switch1, bw=1000, delay='1ms')        
        self.addLink(switch1, switch2, bw=500, delay = '10ms')        

        
        
topos = { 'mytopo': ( lambda: MyTopo() ) }
