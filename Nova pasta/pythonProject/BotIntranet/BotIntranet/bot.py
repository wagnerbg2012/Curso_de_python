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
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):
        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Abri site
        self.browse('https://chamados.ati.to.gov.br/otrs/index.pl?')
        
        if not self.find( "CPF", matching=0.97, waiting_time=10000):
         self.not_found("CPF")
        self.click()
     
        self.paste("04827358133")
        
        if not self.find( "Senha", matching=0.97, waiting_time=10000):
           self.not_found("Senha")
        self.click()

        self.paste("04827358133")
        
       
        if not self.find( "Autenticação", matching=0.97, waiting_time=10000):
            self.not_found("Autenticação")
        self.click()
        
      
        if not self.find( "Ikhon_Chamdados", matching=0.97, waiting_time=10000):
          self.not_found("Ikhon_Chamdados")
        self.click()
     



        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
 
