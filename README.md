# service-to-shell

Holds data for my [service-to-shell](https://connorshade.com/projects/service-to-shell) project

## dnssearcher

A simple Python application written with FastAPI used for performing command injection.
The `/dns2` endpoint should be secured.

## proxy

The proxy used for the nmap scanner portion of the service-to-shell project, not actually used.

## custom_nmap_minimal

A minified nmap-service-probes file, as small as I could get (without modifying the regex) for detecting DNSSearcher

## msf4

Data required for a custom metasploit module - really just the `dnssearcher.rb` file
