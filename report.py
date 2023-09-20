import subprocess
import webbrowser

# Define the path to cpptestcli and the test project file
cpptestcli_path = "C:/Program Files/parasoft_cpptest_professional-2022.2.0-win32.x86_64/cpptest/cpptestcli"  # Update with the actual path
test_folder = "C:/Users/ssharma42/parasoft/workspace/.cpptest/AFMC_ALU_RCV_Check_Time"

cpptestcli_command = [
    cpptestcli_path,
    "-data", test_folder,
    "test",
    "-config", "C:\Users\ssharma42\parasoft\workspace\.cpptest\.metadata\.plugins\com.parasoft.ptest.common.eclipse.core\com.parasoft.xtest.checkers.api\configs\c++test\Example Configuration.properties",  # Update with your configuration name
    "-report", "repor1t.html"  # Name of the report file to generate
]
log_dir = "C:/Users/ssharma42/Desktop/JENKINS_TASK/REPORTS"
report_file = "C:/Users/ssharma42/Desktop/JENKINS_TASK/REPORTS"

stdout_log = open(f"{log_dir}/execution.log", "w")
stderr_log = open(f"{log_dir}/error.log", "w")



# Run the tests using cpptestcli and capture logs
try:
    completed_process = subprocess.run(
        cpptestcli_command,
        stdout=stdout_log,
        stderr=stderr_log,
        text=True,  # Ensure the output is in text mode for Python 3.5+
    )

    # Check the exit code to determine success or failure
    if completed_process.returncode == 0:
        print("Command executed successfully.")
        
        # Open the generated report in a web browser
        webbrowser.open("report.html")
    else:
        print("Command encountered an error. Please check error.log for details.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Close the log files
    stdout_log.close()
    stderr_log.close()