# Manual testing for RStudio Cloud

\### **NOTE: I found the following bug when working on the manual test:**\
Within RStudio Cloud, according to the delete space action pop-up typing the phrase “Delete [spacename]” should be required to enable the delete button, but I can delete the space by pressing the enter/return key with nothing in the field. If I enter random data into the field, the Delete button doesn’t become enabled, but I can still press the enter/return key and the space is deleted. 
![Screen Shot 2022-05-09 at 10 42 10 PM](https://user-images.githubusercontent.com/2002406/167876493-a2b5fe8e-a5ea-4f9e-bdb5-481c1fd8b816.png)

## Manual Tests: 

Manually testing on community, non-commercial version:
* Confirm loading of default page:
  * When visiting https://rstudio.cloud/, the landing page should be "Your Workspace" within the Projects tab

* Test creation of a New Space:
  * Click the "+ New Space" option on the side bar, name it "TESTSPACE" and click create
  * The new space should open and land on the Projects tab by default   
 
* Confirm projects can be created and deleted:
  * Within your **TESTSPACE** workspace, click "New Project" and select "New RStudio Project". Confirm creation of RStudio Project
  * Within your **TESTSPACE** workspace, click "New Project" and select "New Project from Git Repository". Enter the URL of a Github repository and click OK. Confirm creation of Project.
  * Within your **TESTSPACE** workspace, click "New Project" and select "New Jupyter Project". As this is the community version, you should receive a message stating this is a feature only available in Premium.

* Confirm creation limits are respected (default workspace seems to have no limit on projects, but personal workspace does):
  * Within your **TESTSPACE** workspace, create multiple new projects with the "New Project" button.
  * Every time you create a new project, confirm that the message "This space can have up to X more projects." updates
  * Create 10 projects and confirm you cannot create more within the **TESTSPACE** workspace 

* Verify moving of projects from default workspace to personal workspace and vice versa:
  * Within your **TESTSPACE** workspace, click the "Move Project" button (looks like a dolly/hand truck) and select "Your Workspace" then click "OK"
  * Your Project page should now show 9 projects next to "ALL Projects" and you should have a message indicating "This space can have 1 more project."
  * Click "Your Workspace" on the side bar. You should see the project you just moved from **TESTSPACE**. Click the "Move Project" button (looks like a dolly/hand truck) and select "TESTSPACE" then click "OK"
  * Click "TESTSPACE" on the sidebar, the project you just moved should be visible, and the "All Projects" count should now read 10 and you should have a message which states "This space is full - no more projects can be created."

* Confirm **TESTSPACE** pages load:
  * Navigate to **TESTSPACE** and click "Members", "Usage", then "About" to confirm all pages load. Then confirm clicking "Projects" returns you to the Projects page.

* Confirm Your Workspace pages load:
  * Navigate to Your Workspace and click "Usage", then "About" to confirm all pages load. Then confirm clicking "Projects" returns you to the Projects page.

* Confirm Projects can be deleted and restored:
  * Navigate to **TESTSPACE** and click the trash can (delete) button next to a project name.
  * Your Project page should now show 9 projects next to "ALL Projects" and you should have a message indicating "This space can have 1 more project." 
  * Open the "Trash" section of **TESTSPACE** and confirm deleted project is contained here.
  * Click the "Restore Project" button.
  * Navigate back to "All Projects", the project you just restored should be visible, and the "All Projects" count should now read 10 and you should have a message which states "This space is full - no more projects can be created."  

* Confirm deletion of **TESTSPACE** requires disable button to be enabled:
  * Navigate to **TESTSPACE**. Click the "..." button in the header (next to your account name) and select "Delete Space".
  * The "Delete" button should be disabled. Confirm that clicking it does nothing. 
  * Type "Delete" into the field. The "Delete" button should remain disabled.
  * Type "Delete TESTSPACE" into the field. The "Delete" button should now be enabled.

* Confirm all pages linked on the sidebar load:
  * Guide 
  * What’s New
  * Primers
  * Cheat sheets
  * Current System Status
  * RStudio Community
  * Plans & Pricing
  * Terms and Conditions


