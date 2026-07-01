# timed-shutdown-helper
Python executable for scheduling or aborting a shutdown for your Windows device. I made this Timed Shutdown Helper because recently I've been downloading games and sometimes it took all night long, so scheduling an automatic shutdown seems appropriate to reduce the energy consumption and for safety measures.

> [!NOTE]
> Leaving your computer ON for long periods of time, while away from it, *is a breach for external hackers.* Trust me, someone got into my laptop because of this in the pandemic, but luckily I was there to prevent potential damage.

## How to run
Just execute the `run.py` file and follow the instructions.

## How to abort the created shutdown
Just execute the `abort.py` file. If you have an active shedule for a shutdown, you should see a notification informing its abortion, otherwise no notification will show up.

### How does the application work?
The application asks the user for the inputs: `hours`, `minutes` and `seconds`.

After all inputs have been successfully sent, it will run a function to calculate the given time in seconds (called `calculate_seconds()`), which is what your OS needs to know.
