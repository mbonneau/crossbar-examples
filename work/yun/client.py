from autobahn.asyncio.wamp import ApplicationSession
from autobahn.asyncio.wamp import ApplicationRunner

class MyComponent(ApplicationSession):

    def onJoin(self, details):
        print("session ready")

runner = ApplicationRunner(url=u"ws://192.168.1.130:8080/ws", realm=u"realm1")
runner.run(MyComponent)
