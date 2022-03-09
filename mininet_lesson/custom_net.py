from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import NullController, OVSBridge

class MyTopo( Topo ):
    "Custom topology example."

    def build( self ):
        "Build custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' ,cls=OVSBridge)
        rightSwitch = self.addSwitch( 's4' ,cls=OVSBridge)

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

if __name__ == '__main__':
    setLogLevel( 'info' )
    net = Mininet(topo=MyTopo(), controller=NullController)
    net.start()
    CLI(net)
    net.stop()s