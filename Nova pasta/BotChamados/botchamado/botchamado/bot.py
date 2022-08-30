"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot

#Uncomment the line below for integrations with BotMaestro
#Using the Maestro SDK
#rom botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        #Fetch the Activity ID from the task:
        #task = self.maestro.get_task(execution.task_id)
        #activity_id = task.activity_id

        O#pens the BotCity website.
        self.browse("http://www.www.google.com")

         #Uncomment to mark this task as finished on BotMaestro
        #self.maestro.finish_task(
         #    task_id=execution.task_id,
          #  status=AutomationTaskFinishStatus.SUCCESS,
           # message="Task Finished OK."
        #)

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
