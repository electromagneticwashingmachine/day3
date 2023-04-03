import subprocess

# Run the update and upgrade commands with yes as the dafault answer
update_command = "sudo apt-get update -y"
upgrade_command = "sudo apt-get upgrade -y"

subprocess.run(update_command.split(), check=True)
subprocess.run(upgrade_command.split(), check=True)
