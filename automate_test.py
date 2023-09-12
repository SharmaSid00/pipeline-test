import subprocess
import shutil

project_to_be_adjusted= "input"

### command to be edited
CPTESTCLI_COMMAND = "cpptestcli -config "+ project_to_be_adjusted + " -report report.xml"

REPORT_DIR = "../REPORTS/"


print("Executing Parasoft tests...")
result = subprocess.run(CPTESTCLI_COMMAND, shell=True)

# SUCCESS OR NOT
if result.returncode == 0:
    print("Parasoft tests passed.")
else:
    print("Parasoft tests failed.")
    exit(1)


print("Generating report...")
report_command = f"cpptestcli -report-format HTML -source {REPORT_DIR} -destination {REPORT_DIR}/report.html"
result = subprocess.run(report_command, shell=True)

if result.returncode == 0:
    print("Report generated successfully.")
else:
    print("Report generation failed.")
    exit(1)


##ARTIFACTS
print("Archiving the report as a build artifact...")
shutil.copy(f"{REPORT_DIR}/report.html", "/path/to/jenkins/workspace/artifacts/")

exit(0)
