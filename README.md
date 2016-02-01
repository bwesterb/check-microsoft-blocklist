Simple script to be run by cron which checks whether there were changes in
the junk listing of certain IP's.

How to install
==============

Create a feed for your IPs at

  https://postmaster.live.com/snds

Copy `settings.example.yaml` to `settings.yaml` and change the URL to the one
you may find at

  https://postmaster.live.com/snds/auto.aspx

Add an entry in crontab like

    */10 * * * * cd path-to/check-microsoft-blocklist && python check.py

Delist IP
---------

Some links that might be helpful

 - [Microsoft Support Request Delist Form](https://support.microsoft.com/en-us/getsupport?oaspworkflow=start_1.0.0.0&wfname=capsub&productkey=edfsmsbl3&locale=en-us)
 - [Comic Relief](http://cdn.meme.am/instances/500x/64726785.jpg)
