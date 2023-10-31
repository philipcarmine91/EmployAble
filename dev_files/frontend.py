# frontend.py
import subprocess

while True:
    print("Please press Enter to start recording. Type 'exit' to quit.")
    user_input = input()
    
    if user_input.lower() == 'exit':
        break

    print("Recording... Press Enter again to stop.")
    subprocess.run(["python", "backend.py"])

print("Exiting the application.")


