# Manual testing for RStudio Cloud

\### **I found the following bug when working on the manual test:**\
Within RStudio Cloud, according to the delete space action pop-up typing the phrase “Delete [spacename]” should be required to enable the delete button, but I can delete the space by pressing the enter/return key with nothing in the field. If I enter random data into the field, the Delete button doesn’t become enabled, but I can still press the enter/return key and the space is deleted. 
![Screen Shot 2022-05-09 at 10 42 10 PM](https://user-images.githubusercontent.com/2002406/167876493-a2b5fe8e-a5ea-4f9e-bdb5-481c1fd8b816.png)\
\###

## Manual Tests: 

Manually testing on community, non-commercial version:
* Confirm loading of default page:
  * When visiting https://rstudio.cloud/, the landing page should be "Your Workspace" within the Projects tab

* Test creation of a New Space:
  * Click the "+ New Space" option on the side bar, name it "TESTSPACE" and click create
  * The new space should open and land on the Projects tab by default   
 
* Confirm projects can be created and deleted:
  * Within your TESTSPACE workspace, click "New Project" and select "New RStudio Project". Confirm creation of RStudio Project
  * Within your TESTSPACE workspace, click "New Project" and select "New Project from Git Repository". Enter the URL of a Github repository and click OK. Confirm creation of Project.
  * Within your TESTSPACE workspace, click "New Project" and select "New Jupyter Project". As this is the community version, you should receive a message stating this is a feature only available in Premium.

* make sure creation limits are respected (default workspace seems to have no limit on projects, but personal workspace does):
  * Within your TESTSPACE workspace, create multiple new projects with the "New Project" button.
  * Every time you create a new project, confirm that the message "This space can have up to X more projects." updates
  * Create 10 projects and confirm you cannot create more within the TESTSPACE workspace 

* make sure deletion requires disable button to be enabled via “delete [spacename]”


* verify moving of projects from default workspace to personal workspace and vice versa 

* confirm ingestion of git repo as project

* make sure Guide, What’s New, Primers, Cheat sheets, current system Status, RStudio Community, Plans & Pricing, Terms and Conditions all load (from sidebar and top menu)

* Confirm Members of non-default workspace are shared

* Confirm Usage page loads from default and personal workspace

* Selecting default and personal workspace should land on Projects tab by default.
