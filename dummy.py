from P4 import P4, P4Exception

# Create a P4 instance
p4 = P4()

# Set your Perforce server details
p4.port = "kzopforce01:2666"

# Optional: Set the Perforce username and password if needed
# p4.user = "your_username"
# p4.password = "your_password"

try:
    # Connect to the Perforce server
    p4.connect()

    # List all workspaces
    workspaces = p4.run("clients")

    print("All Workspaces:")
    for workspace in workspaces:
        if "z_aravindang_AltrixDev.dev" in workspace['client']:
            print(workspace['client'])
            # p4.client=workspace['client']
            # p4.run_sync()

except P4Exception as e:
    print("Perforce error occurred:", e)
except Exception as ex:
    print("An error occurred:", ex)
finally:
    # Disconnect from the server when done
    p4.disconnect()
