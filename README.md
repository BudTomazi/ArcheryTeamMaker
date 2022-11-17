# ArcheryTeamMaker

This is a tool for making balanced teams of 3 when the scores of the different participants vary greatly.  To run:
1. click on ArcheryTeamMaker.ipynb and then click on the option to open in google colab. 
2.  From here you can select run all from the runtime menu at the top.  
3.  One of the cells will wait for you to upload a csv file from your computer from which it will make the scores.  The csv file should have two columns labeled Name and Score.  There is an example scores csv file in the repository.  
4.  Once this is uploaded it will continue to run, and the teams as well as their average scores will appear at the bottom.  

It should be noted that if the number of participants is not divisible by 3, it will compensate by making some teams of two, basing performance on the average score of the participants.  

There is also a normal python file which can be run locally if access to internet is not available.  

