from py4j.java_gateway import JavaGateway
gateway = JavaGateway()                   # connect to the JVM

addition_app = gateway.entry_point        # get the AdditionApplication instance
addition_app.startAppletHD()

