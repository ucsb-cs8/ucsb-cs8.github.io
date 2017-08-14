---
topic: "CSIL: Via MacOS"
desc: "Accessing CSIL from your MacOS system"
---

# Accessing CSIL from MacOS

To access CSIL from MacOS, you can use the Terminal command, and type the following, replacing `cgaucho` with your ECI/CSIL username, and `csil-12` with any CSIL hostname from `csil-01 through csil-48`:

```
ssh -X cgaucho@csil-12.cs.ucsb.edu
```

# What about the `no $DISPLAY environment variable` error?

If you find when you type idle3 to bring up IDLE that you get this message:

```
no display name and no $DISPLAY environment variable
```

then you need to install XQuartz as explained below, log out, log in, and try again.

# Installing XQuartz

## What is XQuartz and why do I need to install it?

When you use the `ssh` command to access CSIL in a terminal window, essentially you are running all your software on CSIL in a terminal
window on CSIL, and just connecting your Mac's terminal window to the CSIL terminal window over the internet.  That's what the ssh
command does.

This works just fine <em>until</em> you try to do something involving graphics, or windows, such as the `idle3` program.  On CSIL, `idle3` brings
up a window in the Linux windowing system, which is called X11.  However, MacOS does not have the capability to display that kind of window
built into it.  You need an extra piece of software called an X11 Server&mdash;that's exactly what XQuartz provides.

By installing XQuartz, and using the `-X` flag when you connect to CSIL with the `ssh` command, you allow your CSIL terminal window to 
open up graphics windows on your Mac for programs such as `idle`.   If you don't have a program like this in place, you get the
`NODISPLAY` error message.

## Where do I get it

Go to <http://xquartz.org>, and look for the link to download and install the latest version.   Follow the instructions.

At the end, you will need to logout and log back in to your Mac session (not just your ssh session, 
but your entire MacOS session.)  To do this, go to the Apple menu, i.e.  at upper left of your desktop
where it says "Log Out Chris Gaucho" or whatever your name is.   Log back in, and then try terminal again with the `ssh -X ...` command
listed above.




https://www.xquartz.org/
