---
topic: "submit.cs"
desc: "An automatic grading feedback program used at UCSB"
---

In some sections of CS8, the submit.cs system may be used for some assignments.  This system allows you to get quick feedback on your 
programming assignment submissions.

On this page, there is information on these topics:

* Creating a submit.cs account
* Joining a class
* Joining a pair/group for a class
* Additional information

# Creating a submit.cs account


Before you can make submissions, you will need an account on submit.cs. 

Navigate to <https://submit.cs.ucsb.edu> and click "Create Account", or [follow this link](https://submit.cs.ucsb.edu/form/user).

You must enter your umail email address. Upon submission you will receive an email (to your umail) which will allow you to set a password for your account.

If you do not have a umail address (e.g. extension students), you may contact the submit.cs administrator to request creation of an account.    That is also how faculty accounts are created, since faculty do not have umail addresses.

# Joining a class

Once your account is created you will need to join the appropriate class. Login to submit.cs and click the "Join Class" tab. 

Clicking the button for the appropriate class will join to the the class and subsequently allow you to view which projects are available for submission.

If you get a message in submit.cs that you are not authorized to submit a solution for a given project, it may be because you have an incorrect project number, or it may be because you have not yet joined the course for which you are trying to make a submission.

# Joining a pair/group for a class

Some projects will allow pair or group submissions.   To create a group, navigate to the page for the particualr programming assignment.
If the assignment allows pair/groups submissions, you'll see a "Join Group" button.  Click this button.
The subsequent page will allow you to accept and reject invitations from your classmates, 
as well invite one of your classmates by their umail address to join your group.

While multiple students can invite you to join a group, the system only permits you to have one outstanding 
invitation at a time. You must revoke an invitation if you would like to invite someone else. 

Once grouped together, all the members of a group will be able to see all the submissions made by everyone in 
the group for that project, regardless of when the submission was made.

Additional notes on groups:

* Groups exist only within the context of a specific programming assignment.  
* You can be in a different group/pair for each programming assignment.  
* If you want to pair/group with the same person each time, you still have to create that group/pair with a new invitation for each programming assignment in the course.
* The instructor sets the limit on the maximum group size.  The default is 1, which prohibits groups/pairs from forming.  The instructor has to override the default and change to at least 2 before the invite system is enabled.


# Additional information about submit.cs

The submit.cs system was built by UCSB Ph.D. Student Bryce Boe as part of his Ph.D. dissertation research, under the supervision of
Dr. Diana Franklin.  It is built in Python using the Pyramid web application framework.  The backend also uses RabbitMQ.
