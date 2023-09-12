import subprocess
import shutil

# Set your Parasoft test execution command. This will vary based on your setup.
PARASOFT_COMMAND = "parasoft-cli execute -testSuite MyTestSuite"

# Set the directory where Parasoft wvill generate the report.
REPORT_DIR = "../REPORTS"

# Execute Parasoft tests
print("Executing Parasoft tests...")
result = subprocess.run(PARASOFT_COMMAND, shell=True)

# Check if the tests were successful (adjust this condition as needed)
if result.returncode == 0:
    print("Parasoft tests passed.")
else:
    print("Parasoft tests failed.")
    exit(1)

# Generate a report (adjust the command based on your report format)
print("Generating report...")
report_command = f"parasoft-cli generate-report -source {REPORT_DIR} -format HTML -output {REPORT_DIR}/report.html"
result = subprocess.run(report_command, shell=True)

# Check if the report was generated successfully
if result.returncode == 0:
    print("Report generated successfully.")
else:
    print("Report generation failed.")
    exit(1)

# Fetch the report from the Parasoft server (if applicable)
# WE may need to use a different method to retrieve the report

# Archive the report as a build artifact
# This makes it accessible in Jenkins
print("Archiving the report as a build artifact...")
shutil.copy(f"{REPORT_DIR}/report.html", "/path/to/jenkins/workspace/artifacts/")

# Exit successfully
exit(0)



