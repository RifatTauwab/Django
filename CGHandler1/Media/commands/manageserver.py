from connections import *

def play() :
    cmd = 'PLAY 1-10 AMB'
    SendAMCPCommand(HOSTS['LOCALHOST'], PORTS['AMCP'], cmd)
