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
