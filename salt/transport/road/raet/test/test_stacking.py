# -*- coding: utf-8 -*-
'''
Tests to try out stacking. Potentially ephemeral

'''
# pylint: skip-file
from ioflo.base.odicting import odict
from ioflo.base.aiding import Timer

from ioflo.base.consoling import getConsole
console = getConsole()

from salt.transport.road.raet import (raeting, nacling, packeting,
                                     estating, yarding, transacting, stacking)


def testStackUdp():
    '''
    initially
    master on port 7530 with eid of 1
    minion on port 7531 with eid of 0
    eventually
    master eid of 1
    minion eid of 2
    '''
    console.reinit(verbosity=console.Wordage.concise)

    signer = nacling.Signer()
    masterSignKeyHex = signer.keyhex
    privateer = nacling.Privateer()
    masterPriKeyHex = privateer.keyhex

    signer = nacling.Signer()
    minionSignKeyHex = signer.keyhex
    privateer = nacling.Privateer()
    minionPriKeyHex = privateer.keyhex

    #master stack
    estate = estating.LocalEstate(   eid=1,
                                     name='master',
                                     sigkey=masterSignKeyHex,
                                     prikey=masterPriKeyHex,)
    stack0 = stacking.StackUdp(estate=estate)

    #minion stack
    estate = estating.LocalEstate(   eid=0,
                                     name='minion1',
                                     ha=("", raeting.RAET_TEST_PORT),
                                     sigkey=minionSignKeyHex,
                                     prikey=minionPriKeyHex,)
    stack1 = stacking.StackUdp(estate=estate)


    print "\n********* Join Transaction **********"
    stack1.join()

    timer = Timer(duration=0.5)
    while not timer.expired:
        stack1.serviceUdp()
        stack0.serviceUdp()

    stack0.serviceUdpRx()
    stack0.process()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()


    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} dids=\n{1}".format(stack0.name, stack0.eids)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    for estate in stack0.estates.values():
        print "Remote Estate {0} joined= {1}".format(estate.eid, estate.joined)

    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} dids=\n{1}".format(stack1.name, stack1.eids)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    for estate in stack1.estates.values():
            print "Remote Estate {0} joined= {1}".format(estate.eid, estate.joined)


    print "\n********* Allow Transaction **********"

    stack1.allow()
    timer.restart()
    while not timer.expired:
        stack1.serviceUdp()
        stack0.serviceUdp()

    stack0.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack0.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()

    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} dids=\n{1}".format(stack0.name, stack0.eids)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    for estate in stack0.estates.values():
        print "Remote Estate {0} allowed= {1}".format(estate.eid, estate.allowed)

    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} dids=\n{1}".format(stack1.name, stack1.eids)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    for estate in stack1.estates.values():
            print "Remote Estate {0} allowed= {1}".format(estate.eid, estate.allowed)


    print "\n********* Message Transaction Minion to Master **********"
    body = odict(what="This is a message to the master. How are you", extra="And some more.")
    stack1.message(body=body, deid=1)

    timer.restart()
    while not timer.expired:
        stack1.serviceUdp()
        stack0.serviceUdp()

    stack0.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()

    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} dids=\n{1}".format(stack0.name, stack0.eids)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    print "{0} Received Messages =\n{1}".format(stack0.name, stack0.rxMsgs)

    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} dids=\n{1}".format(stack1.name, stack1.eids)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    print "{0} Received Messages =\n{1}".format(stack1.name, stack1.rxMsgs)

    print "\n********* Message Transaction Master to Minion **********"
    body = odict(what="This is a message to the minion. Get to Work", extra="Fix the fence.")
    stack0.message(body=body, deid=2)

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack1.serviceUdp()
        stack0.serviceUdp()

    stack0.serviceUdpRx()

    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} dids=\n{1}".format(stack0.name, stack0.eids)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    print "{0} Received Messages =\n{1}".format(stack0.name, stack0.rxMsgs)

    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} dids=\n{1}".format(stack1.name, stack1.eids)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    print "{0} Received Messages =\n{1}".format(stack1.name, stack1.rxMsgs)

    print "\n********* Message Transactions Both Ways **********"

    stack1.txMsgs.append((odict(house="Mama mia1", queue="fix me"), None))
    stack1.txMsgs.append((odict(house="Mama mia2", queue="help me"), None))
    stack1.txMsgs.append((odict(house="Mama mia3", queue="stop me"), None))
    stack1.txMsgs.append((odict(house="Mama mia4", queue="run me"), None))

    stack0.txMsgs.append((odict(house="Papa pia1", queue="fix me"), None))
    stack0.txMsgs.append((odict(house="Papa pia2", queue="help me"), None))
    stack0.txMsgs.append((odict(house="Papa pia3", queue="stop me"), None))
    stack0.txMsgs.append((odict(house="Papa pia4", queue="run me"), None))

    #segmented packets
    stuff = []
    for i in range(300):
        stuff.append(str(i).rjust(4, " "))
    stuff = "".join(stuff)

    stack1.txMsgs.append((odict(house="Mama mia1", queue="big stuff", stuff=stuff), None))
    stack0.txMsgs.append((odict(house="Papa pia4", queue="gig stuff", stuff=stuff), None))

    stack1.serviceTxMsg()
    stack0.serviceTxMsg()

    timer.restart()
    while not timer.expired:
        stack1.serviceUdp()
        stack0.serviceUdp()

    stack0.serviceUdpRx()
    stack1.serviceUdpRx()

    timer.restart()
    while not timer.expired:
        stack0.serviceUdp()
        stack1.serviceUdp()

    stack1.serviceUdpRx()
    stack0.serviceUdpRx()


    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print
    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
            print msg


    print "\n********* Message Transactions Both Ways Again **********"

    stack1.txMsg(odict(house="Oh Boy1", queue="Nice"))
    stack1.txMsg(odict(house="Oh Boy2", queue="Mean"))
    stack1.txMsg(odict(house="Oh Boy3", queue="Ugly"))
    stack1.txMsg(odict(house="Oh Boy4", queue="Pretty"))

    stack0.txMsg(odict(house="Yeah Baby1", queue="Good"))
    stack0.txMsg(odict(house="Yeah Baby2", queue="Bad"))
    stack0.txMsg(odict(house="Yeah Baby3", queue="Fast"))
    stack0.txMsg(odict(house="Yeah Baby4", queue="Slow"))

    #segmented packets
    stuff = []
    for i in range(300):
        stuff.append(str(i).rjust(4, " "))
    stuff = "".join(stuff)

    stack1.txMsg(odict(house="Snake eyes", queue="near stuff", stuff=stuff))
    stack0.txMsg(odict(house="Craps", queue="far stuff", stuff=stuff))

    timer.restart(duration=2)
    while not timer.expired:
        stack1.serviceAll()
        stack0.serviceAll()


    print "{0} eid={1}".format(stack0.name, stack0.estate.eid)
    print "{0} estates=\n{1}".format(stack0.name, stack0.estates)
    print "{0} transactions=\n{1}".format(stack0.name, stack0.transactions)
    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print
    print "{0} eid={1}".format(stack1.name, stack1.estate.eid)
    print "{0} estates=\n{1}".format(stack1.name, stack1.estates)
    print "{0} transactions=\n{1}".format(stack1.name, stack1.transactions)
    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
            print msg


def testStackUxd():
    '''
    initially


    '''
    console.reinit(verbosity=console.Wordage.concise)

    #lord stack
    #yard0 = yarding.Yard(name='lord')
    stack0 = stacking.StackUxd()

    #serf stack
    #yard1 = yarding.Yard(name='serf', yid=1)
    stack1 = stacking.StackUxd()

    stack0.addRemoteYard(stack1.yard)
    stack1.addRemoteYard(stack0.yard)

    print "{0} yard name={1} ha={2}".format(stack0.name, stack0.yard.name, stack0.yard.ha)
    print "{0} yards=\n{1}".format(stack0.name, stack0.yards)
    print "{0} names=\n{1}".format(stack0.name, stack0.names)

    print "{0} yard name={1} ha={2}".format(stack1.name, stack1.yard.name, stack1.yard.ha)
    print "{0} yards=\n{1}".format(stack1.name, stack1.yards)
    print "{0} names=\n{1}".format(stack1.name, stack1.names)

    print "\n********* UXD Message lord to serf serf to lord **********"
    msg = odict(what="This is a message to the serf. Get to Work", extra="Fix the fence.")
    stack0.transmit(msg=msg)

    msg = odict(what="This is a message to the lord. Let me be", extra="Go away.")
    stack1.transmit(msg=msg)

    timer = Timer(duration=0.5)
    timer.restart()
    while not timer.expired:
        stack0.serviceAll()
        stack1.serviceAll()


    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print

    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
        print msg
    print

    print "\n********* Multiple Messages Both Ways **********"

    stack1.transmit(odict(house="Mama mia1", queue="fix me"), None)
    stack1.transmit(odict(house="Mama mia2", queue="help me"), None)
    stack1.transmit(odict(house="Mama mia3", queue="stop me"), None)
    stack1.transmit(odict(house="Mama mia4", queue="run me"), None)

    stack0.transmit(odict(house="Papa pia1", queue="fix me"), None)
    stack0.transmit(odict(house="Papa pia2", queue="help me"), None)
    stack0.transmit(odict(house="Papa pia3", queue="stop me"), None)
    stack0.transmit(odict(house="Papa pia4", queue="run me"), None)

    #big packets
    stuff = []
    for i in range(300):
        stuff.append(str(i).rjust(4, " "))
    stuff = "".join(stuff)

    stack1.transmit(odict(house="Mama mia1", queue="big stuff", stuff=stuff), None)
    stack0.transmit(odict(house="Papa pia4", queue="gig stuff", stuff=stuff), None)

    timer.restart(duration=2)
    while not timer.expired:
        stack1.serviceAll()
        stack0.serviceAll()

    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print

    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
        print msg
    print

    src = ('minion', 'serf', None)
    dst = ('master', None, None)
    route = odict(src=src, dst=dst)
    msg = odict(route=route, stuff="Hey buddy what is up?")
    stack0.transmit(msg)

    timer.restart(duration=2)
    while not timer.expired:
        stack1.serviceAll()
        stack0.serviceAll()

    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print

    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
        print msg
    print

    estate = 'minion1'
    #lord stack yard0
    stack0 = stacking.StackUxd(name='lord', lanename='cherry')

    #serf stack yard1
    stack1 = stacking.StackUxd(name='serf', lanename='cherry')

    print "Yid", yarding.Yard.Yid

    print "\n********* Attempt Auto Accept ************"
    #stack0.addRemoteYard(stack1.yard)
    yard = yarding.Yard( name=stack0.yard.name, prefix='cherry')
    stack1.addRemoteYard(yard)

    print "{0} yard name={1} ha={2}".format(stack0.name, stack0.yard.name, stack0.yard.ha)
    print "{0} yards=\n{1}".format(stack0.name, stack0.yards)
    print "{0} names=\n{1}".format(stack0.name, stack0.names)

    print "{0} yard name={1} ha={2}".format(stack1.name, stack1.yard.name, stack1.yard.ha)
    print "{0} yards=\n{1}".format(stack1.name, stack1.yards)
    print "{0} names=\n{1}".format(stack1.name, stack1.names)

    print "\n********* UXD Message serf to lord **********"
    src = (estate, stack1.yard.name, None)
    dst = (estate, stack0.yard.name, None)
    route = odict(src=src, dst=dst)
    msg = odict(route=route, stuff="Serf to my lord. Feed me!")
    stack1.transmit(msg=msg)

    timer = Timer(duration=0.5)
    timer.restart()
    while not timer.expired:
        stack0.serviceAll()
        stack1.serviceAll()


    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print

    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
        print msg
    print

    print "\n********* UXD Message lord to serf **********"
    src = (estate, stack0.yard.name, None)
    dst = (estate, stack1.yard.name, None)
    route = odict(src=src, dst=dst)
    msg = odict(route=route, stuff="Lord to serf. Feed yourself!")
    stack0.transmit(msg=msg)


    timer = Timer(duration=0.5)
    timer.restart()
    while not timer.expired:
        stack0.serviceAll()
        stack1.serviceAll()

    print "{0} Received Messages".format(stack0.name)
    for msg in stack0.rxMsgs:
        print msg
    print

    print "{0} Received Messages".format(stack1.name)
    for msg in stack1.rxMsgs:
        print msg
    print

    print "{0} yard name={1} ha={2}".format(stack0.name, stack0.yard.name, stack0.yard.ha)
    print "{0} yards=\n{1}".format(stack0.name, stack0.yards)
    print "{0} names=\n{1}".format(stack0.name, stack0.names)

    print "{0} yard name={1} ha={2}".format(stack1.name, stack1.yard.name, stack1.yard.ha)
    print "{0} yards=\n{1}".format(stack1.name, stack1.yards)
    print "{0} names=\n{1}".format(stack1.name, stack1.names)



if __name__ == "__main__":
    testStackUdp()
    testStackUxd()
