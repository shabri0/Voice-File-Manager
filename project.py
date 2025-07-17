import speech_recognition as sr 
import pyautogui 
 
class VoiceFileManager: 
    def __init__(self): 
        self.recognizer = sr.Recognizer() 
        self.microphone = sr.Microphone() 
         
    def listen_command(self): 
        with self.microphone as source: 
            print("\nListening... (say 'select', 'copy', or 'paste')") 
            self.recognizer.adjust_for_ambient_noise(source) 
            audio = self.recognizer.listen(source, timeout=5) 
             
            try: 
                command = self.recognizer.recognize_google(audio).lower() 
                print(f"Command recognized: {command}") 
                return command 
            except Exception as e: 
                print(f"Error: {str(e)}") 
                return None 
 
    def execute_command(self, command): 
        if command: 
            if 'select' in command: 
                print("Selecting all files...") 
                pyautogui.hotkey('ctrl', 'a') 
                print("Selection done!") 
            elif 'copy' in command: 
                print("Copying files...") 
                pyautogui.hotkey('ctrl', 'c')  
                print("Copying done!") 
            elif 'paste' in command: 
                print("Pasting files...") 
                pyautogui.hotkey('ctrl', 'v') 
                print("Pasting done!") 
            elif 'exit' in command: 
                print("Ok, exiting...") 
                return True 
             
        return False 
    def run(self): 
        print("=== VOICE FILE MANAGER ===") 
        print("Valid commands: select, copy, paste, exit") 
 
        while True: 
            command = self.listen_command() 
            if command and self.execute_command(command): 
                break 
 
if __name__ == "__main__": 
    VoiceFileManager().run() 
# This code is a simple voice-controlled file manager that allows users to select, copy, and paste files using voice commands.
# It uses the SpeechRecognition library to listen for commands and pyautogui to perform the actions.
# The program runs in a loop, listening for commands until the user says "exit".