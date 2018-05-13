# Project Idea

- Goal(s) : Creating a dynamic website for Ports Index.

- Abstract :

Ports Index allows one to understand about the Ports in a relatively easier way.In our case a port.There is no proper Ports index currently.The idea would be to create dynamic webpages using different languages ( HTML, python, css, django ) which will display all information about that port.

Information such as:

**1.** Description

**2.** Version

**3.** Homepage

**4.** Dependencies

**5.** Dependent Ports

**6.** Build Summary

**7.** Binary Package status

**8.** Installation Statistics

**9.** Results of Livecheck (Package outdated or not)

**10.** Git Log

**11.** Links to Track Tickets

**12.** Links for Pull Request(Optional)


**Technical Details**

- Methodology (Broken into steps/phases/short-goals)  :

This would be divided into several subtasks.

**1.** **Port Information**

description, version,maintainer, homepage, variants, dependencies, dependent ports,platforms,license,homepage,long description
All these must be gathered using portindex2json( [https://github.com/macports/macports-contrib/blob/master/portindex2json/portindex2json.tcl](https://github.com/macports/macports-contrib/blob/master/portindex2json/portindex2json.tcl))

Sample Result:
```
{ 
"subports":"py27-amqplib",

"portdir":"python/py-amqplib",

"description":"Simple non-threaded Python client library for AMQP.",

"homepage":"https://code.google.com/p/py-amqplib/",

"epoch":"0",

"platforms":"darwin",

"name":"py-amqplib",

"depends_lib":"port:py27-amqplib",

"license":"LGPL-2.1+",

"long_description":"{Simple non-threaded Python client library for AMQP.}",

"maintainers":"stromnov openmaintainer",

"version":"1.0.2",

"categories":"python devel",

"revision":"0"
}
```

Port Table would be filled using the data we get from portindex2json,
These basic Information would be taken from the data in Port Table, Port-version Table,maintainers .
The data would be taken using sql queries from the backend.

**2.** **Build History/Summary**

Plan is to use tables in database to manage the build history.From the build history table I can generate Build Summary relevant to that port.

First I would have to run a python script(only once) so as to get all the build history we have till date. It would involve using the JSON API we already have.(https://build.macports.org/json/help)


The Build History Table :


| sr_no | builderid | buildnumber | portid | portversionid | timestamp | success | version |  reason | info |   commitid   | distributable |
|:----:|:---------:|:-----------:|:------:|:-------------:|:---------:|:-------:|:-------:|:-------:|:----:|:-------------:|:-------------:|
|   1   |     1     |     5568    |   677  |       1       |  XX:XX:XX |    ok   |   1.2   |   abc   |  def | abxcss12asfva |               |
|   2   |     2     |     4554    |   234  |       3       |  XX:XX:XX |    no   |  1.0.4  |   def   |  abc |  asdasda231as |               |
|   3   |     1     |     5569    |   677  |       2       |  XX:XX:XX |  not ok |  1.0.5  | trigger | fail |     abc345    |               |


Once we populate the Build History Table we can get the Build History/Summary for a particular port just by running a query pertaining to the port id we are interested in.

We also have to update the Buildbot master for this task.
As we would like to have continuous updates after each build.
So whenever a build is completed a query to update the build history table would be sent.

**3.** **Binary Package status**

This can be done using checking/scraping
 [http://packages.macports.org](http://packages.macports.org)
We can get the packages for all ports present in macports.

**4.** **Installation Statistics**

Took some inspiration from GSOC 2011 statistics project.
 [http://stats.macports.neverpanic.de/categories/11/ports/18576](http://stats.macports.neverpanic.de/categories/11/ports/18576)

We get a json from user who enrolled for statistics program twice a month.
JSON looks like :

```
{
  "id": "270856DE-DD7E-494F-9A99-281BED099110",

  "os": {
    "macports_version": "2.4.2",

    "osx_version": "10.13",

    "os_arch": "i386",

    "os_platform": "darwin",

    "build_arch": "x86_64",

    "gcc_version": "none",

    "xcode_version": "9.2"
  },

  "active_ports": [
    {"name": "python2_select", "version": "0.0_2"},

    {"name": "python_select", "version": "0.3_7"},

    {"name": "llvm_select", "version": "2_0"},

    {"name": "xar", "version": "1.6.1_0"},

    {"name": "llvm-4.0", "version": "4.0.1_2", "requested": "true"},

    ]
}
```
We would now use this json:

To fill in the Statistics Tables.

### Port history Table :


| portid | portversionid |                userid                |     timestamp    | variants | requested |
|:------:|:-------------:|:------------------------------------:|:----------------:|:--------:|:---------:|
|   677  |       1       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:00 |     -    |    TRUE   |
|   677  |       2       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:30 | python27 |     -     |
|   234  |       3       | 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  22/05/2018 2:00 |  llvm40  |     -     |
|   677  |       1       |                  17                  | 07/09/2018 12:00 |     -    |     -     |

### OS History Table :


|                userid                | os_id | os_arch | platform | xcodeversion | macportsversion |     timestamp    | default_prefix |   stdlib  |
|:------------------------------------:|:-----:|:-------:|:--------:|:------------:|:---------------:|:----------------:|:--------------:|:---------:|
| 270856DE-DD7E-494F-9A99-281BED099110 |  10.5 |   i386  |  darwin  |      9.2     |      2.4.2      | 27/03/2018 12:00 |      TRUE      | stdlibc++ |
| 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  10.8 |   i486  |  darwin  |      9.2     |      2.4.0      | 27/03/2018 12:30 |      FALSE     | stdlibc++ |
|  5830GHS-DD7E-5939JS-9A99-982HSGA23  | 10.11 |   i223  |  darwin  |      9.4     |      2.4.1      |  22/05/2018 2:00 |      TRUE      |   libc++  |

These tables would be continuously updated with the data we get from the json received from users.

Parsing the json &amp; populating the table would be done using Django.


2) Storing the logs for Safekeeping

A simple log file would be created wherein the json received would be kept as it is in a log file for future use.

**5.** **Results of Livecheck**

This could be found out by running a simple command on the server once every day. Then the results would then need to be relayed back to the website.

**6.** **Git Log**

This can be done by using commands such as :
git log --pretty=oneline

**7.** **Links to track tickets for that port**

A simple scraper tool scraping all the ticket id&#39;s then displaying them .
Scraping should be done from :
 [https://trac.macports.org/query?status=accepted&amp;status=assigned&amp;status=new&amp;status=reopened](https://trac.macports.org/query?status=accepted&amp;status=assigned&amp;status=new&amp;status=reopened)

**8.** **Link for Pull Requests (Probably a Stretch Goal)**

Either using Github API to get the required data .
Or Scraping through github website.

This segment is not that well researched and is an option provided there is enough time to also complete this.



- **Milestones**

Some important Milestones during the summer.

### May 20 :

Database would be ready by then.( [https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing)) .

The important tables of Database are :

- Port Table
- Builder Table
- Maintainers
- Maintainer-portkey
- Build History (The most important table)
- Tables for Statistics

### May 28 :

- Basic Website Structure ready.
- Basic Port Information Implemented

### June 11 :

- Installation Statistics Implemented
- Start doing changes in BuildBot Master to send build history

### June 15 :

- Deployment of Installation Statistics done (Ideally under macports domain)
- Testers would be invited

### June 30 :

- Update Build History Feature Completed from Server End.

### July 15 :

- Front end for the entire website.(Entire CSS,HTML done.Site will look good to eyes)
- All the queries ready for Build Summary of each port


### July 30 :

- Track Tickets feature implemented
- Binary Package Status  feature implemented
- Git log Feature implemented

### Aug 7 :

- Documentation done
- Bugs/Exceptions/Issues Fixed.

### Aug 14 :

- Final GSOC Submission


- **Tentative Schedule**

| Time Periods | Plan of Action |
| --- | --- |
| April 22-May 13 | - Community Bonding Periods- Getting Aware of the MacPorts Code Base relevant to me and  my future goals- Getting to know/Setting up the entire environment. |
| May 14-May 20 | - working on creating the entire Database for my project( [https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing)) |
| May 21-May 28 | Working on
- Website Structure
- Basic Port Information |
| May 29 - June 11 | Working on
- Installation Statistics- Changes in Buildbot master |
| June 12-June 15 | - Submit for Phase 1
- Deployment of Installation Statistics
- Changes in Buildbot master |
| June 16-June 30 | - Working with Testers for installation Statistics
- Coding to update build history after every build |
| July 1 - July 15 | - Frontend work involving HTML,CSS,other technologies
- Preparing queries for Buildbot Master
- Submit for phase 2 evaluations |
| July 15-July 30 | Working on
- Track Tickets- Git Log
- Binary Package Status |
| July 30-Aug 7 | - Documentation
- Bug/Issue Fixing |
| Aug 7 - Aug 14 | - Final Tweaking to make everything run perfect
- Submit the final report. |

An **Utmost effort** will be done by me to stay on schedule.And am easily able to contribute more than 30+ hours weekly.

**Stretch Goals/Plans after GSoC**

- As the website of macports is not uptodate in terms of UI.I would like to revamp the entire website and its interface.
- Also I would like to update buildbot views .As that is what needed to be done.This would be my first priority .
- I Plan to keep on Contributing To open source and be a mentor at MacPorts .
Because I would really like to help my juniors.
- I have plans to keep on Contributing to open source community.
And grow the community as well as myself.
- Add one feature of listing the outdated ports of a maintainer
- Links for Github PR



**Appendix**

Database consist of following tables :

Link : [https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing)

| **Port table** : Describing all the ports and their basic information. |
| --- |
| **Builder table** : Information about Builder , linking with builder id, os name as well as architecture. |
| **Port-version** : Linking ports with their different versions. |
| **Maintainers** : LInking maintainers with their id. |
| **Maintainer-portid** : Linking Maintainer with the ports they manage. |
| **build history** : Most Crucial part of the database. Entire Builder history stored in here. |
| **Tables for Statistics** |
| **Port history** : Entire Port history stored in it, which can be used for statistics. |
| **OS history** : Entire os history stored to get statistics about various os related information. |