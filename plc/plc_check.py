from opcua import Client

PLC_URL = "opc.tcp://127.0.0.1:4840"

client = Client(PLC_URL)

try:
    print("Connecting to PLC...")

    client.connect()

    print("PLC connected successfully.")

    # Get PLC object
    objects = client.get_objects_node()

    plc = objects.get_child(["2:PLC"])

    # Read PLC tags
    motor_status = plc.get_child(["2:MotorStatus"]).get_value()
    temperature = plc.get_child(["2:Temperature"]).get_value()

    print(f"MotorStatus: {motor_status}")
    print(f"Temperature: {temperature}")

    print("PLC health check PASSED.")

except Exception as e:

    print("PLC health check FAILED.")
    print(f"Error: {e}")

    raise

finally:

    client.disconnect()