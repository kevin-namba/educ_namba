from mininet.net import Mininet
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import RemoteController

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

if __name__ == '__main__':
    setLogLevel( 'info' )
    net = Mininet(topo=MyTopo(), build=False)

    # Add remote controller
    c1 = RemoteController( 'c1', ip='127.0.0.1')
    net.addController(c1)

    net.build()
    net.start()

    CLI(net)

    net.stop()