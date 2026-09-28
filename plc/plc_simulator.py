from opcua import Server
import time

# Create OPC UA server
server = Server()

# OPC UA endpoint
server.set_endpoint("opc.tcp://127.0.0.1:4840")

# Create namespace
uri = "http://localhost/PLC"
idx = server.register_namespace(uri)

# Create PLC object
objects = server.get_objects_node()

plc = objects.add_object(idx, "PLC")

# Create PLC tags
motor_status = plc.add_variable(idx, "MotorStatus", True)
temperature = plc.add_variable(idx, "Temperature", 25.0)

# Make tags writable
motor_status.set_writable()
temperature.set_writable()

print("Starting OPC UA PLC Simulator...")
print("Endpoint: opc.tcp://127.0.0.1:4840")
print("Tags:")
print("  MotorStatus")
print("  Temperature")

server.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping PLC simulator...")
    server.stop()