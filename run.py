import os

def calculate_seconds(hours=0, minutes=0, seconds=0) -> int:
   total_seconds = (hours * (60 ** 2)) + (minutes * 60) + seconds
   
   return total_seconds

print("TIMED SHUTDOWN HELPER".center(50, "="))
print(">> Press CTRL + C to close and cancel the program <<\n\n")

print("Countdown".center(25, "-"))

try:
   hours = int(input("Hours: "))
   minutes = int(input("Minutes: "))
   seconds = int(input("Seconds: "))
      
   if hours < 0: hours = 0
   if minutes < 0: minutes = 0
   if seconds < 0: seconds = 0
      
   print(f"Informed time: {hours}h {minutes}m {seconds}s")
   confirmed = str(input("\nProceed to creating the shutdown? (y/n)\n> ")).lower().strip()
      
   if confirmed == "y":
      if hours == 0 and minutes == 0 and seconds == 0:
         confirmed = str(input("\nWARNING: Creating a shutdown with no countdown results in an instant shutdown. Do you REALLY want do proceed? (y/n)\n> ")).lower().strip()
            
         if confirmed == "y":
            os.system('shutdown /s /f /t 0')
            
      else:   
         countdown = calculate_seconds(hours, minutes, seconds)
         os.system(f'shutdown /s /t {countdown}')
      
except:
   print("\nPlease inform the time in Integer numbers.")
   input("Press ENTER to end the execution.")
