# Database Description

* [Port index](#port-index)
  - [Commits](#commits)
  - [Ports](#ports)
  - [Obsolete ports](#obsolete_ports)
  - [Deleted ports](#deleted_ports)
  - [Categories](#categories)
  - [Port - Category](#port_category)
  - [Maintainers](#maintainers)
  - [Port - Maintainer](#port_maintainer)
* [Build statistics](#build-statistics)
  - [Builders](#builders)
  - [Build History](#build_history) (The most important table)
* [Installation statistics](#installation-statistics)
  - [Statistics](#statistics)
  - [Port History](#port_history)
  - [OS History](#os_history)

# Port index

## commits

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 1
sha | varchar | unique, index | 3a1b845e6f4fa4a78dae5c1b58f4dc46f397b916
author_timestamp | datetime, index
commit_timestamp | datetime, index

* Maybe there's a way to order commits in some way

## ports

_This table consists of all the current port information._

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 123
portname | varchar | unique, index | python27
version | varchar | | 2.7.15
revision | integer | | 0
description | text | | An interpreted, object-oriented ...
long_desc | text | | Python is an interpreted, ... 
homepage | varchar | | https://www.python.org/
license | varchar | | PSF
openmaintainer | boolean | | true
active | boolean | | true
portdir | varchar | | lang/python27

* `openmaintainer` specifies whether the port is under an openmaintainer policy
* `active` is true for ports which are neither deleted nor obsolete (make sure not to end up in inconsistent database state)

## obsolete_ports

Column | Type | Notes
-------|------|------
port_id | integer | references ports(id), unique, index
replaced_by | integer | references ports(id)
commit_id | integer | references commit(id)

## deleted_ports

Column | Type | Notes
-------|------|------
port_id | integer | references ports(id), unique, index
commit_id | integer | references commit(id)

## categories

_This table lists all existing categories._

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 7
name | varchar | unique, index | lang

## port_category

_Which ports belong to which categories._

### Structure

Column | Type | Notes | Example
-------|------|-------|--------
port_id | integer | references ports(id) | 123
category_id | integer | references categories(id) | 7

## maintainers

_List of all port maintainers_

### Structure

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 42
email | varchar | unique, index | jmr.nospam@macports.org
github | varchar | unique, index | jmroot

* The (email, github) pair also needs to be unique.

**Notes:**
* I took the liberty to edit this table into what I think would be the "ideal" case. The problem is that our ports might not have the required consistency.
* The code to handle maintainers will need quite a bit of special handling. First of all, there's a high chance that some handles could be misspelled, lots of emails are lacking the corresponding github handles, many maintainers might not even have a github handle (or might have never told us one), some emails might have been accidentally removed.
* Maintainers change their emails or github handles. At some point we might want to figure out what to do with those, but let's not overengineer the problem for now.
* I wanted to add that we do have an additional (private) database with some links between github handles and emails. We could potentially use that information after actually deploying the app.
* If we want to use the app to also check the consistency of maintainer entries, we would probably need an additional many-to-many table like this one:

Column | Type | Notes
-------|------|------
maintainer_id | integer | references maintainer(id)
description | varchar |

maintainer_id | description | Notes
--------------|-------------|------
9 | vishnu |
9 | vishnu @Vishnum98 |
9 | @Vishnum98 vishnu | just different order
9 | @Vishnum98 vishnum | has a typo
9 | gmail.com:vishnum1998 @Vishnum98 | contains the old email address

But let's wait with this complication and just have a single simple table for now.

## port_maintainer

* _Sets up the relation between maintainer id & port id._
* _Basically tells us which maintainer is handling which all ports._

Column | Type
-------|---------
maintainer_id | integer | references maintainer(id), index | 42
port_id | integer | references port(id), index | 123

# Build statistics

## builders

_This table consist of list of all the port builders on our [build infrastructure](https://build.macports.org/builders)._

Column | Type | Notes
-------|------|------
**id (key)** | integer | primary key
name | varchar | unique, index
os_version | varchar | index
os_name | varchar | index
arch | varchar | index
stdlib | varchar | index

### Example

| id (key) | name | os_version | os_name | arch | stdlib
|----------|------|------------|---------|------|-------
| 1 | ports-10.5_ppc_legacy | 10.5 | Mac OS X 10.5 | ppc | stdlibc++
| 2 | ports-10.6_i386_legacy | 10.6 | Mac OS X 10.6 | i386 | stdlibc++
| 3 | ports-10.6_x86_64_legacy | 10.6 | Mac OS X 10.6 | x86_64 | stdlibc++
| 4 | ports-10.6_i386 | 10.6 | Mac OS X 10.6 | i386 | libc++
| 5 | ports-10.6_x86_64 | 10.6 | Mac OS X 10.6 | x86_64 | libc++
| 6 | ports-10.7_x86_64_legacy | 10.7 | OS X 10.7 | x86_64 | stdlibc++
| | ... | | | |
|   | ports-10.13_x86_64 | 10.13 | macOS 10.13 | x86_64 | libc++

## build_history

_Enitre build history would be saved here._

Column | Type | Notes
-------|------|------
**id (key)** | integer | primary key
builder_id | integer | references builder(id)
build_number | integer | index
port_id | integer | references ports(id), index
timestamp | datetime |
success | varchar |
version | varchar
reason | text
info | text
commit_id | integer | references commits(id)
distributable | text

* (builder_id, build_number) pair must be unique

### Example

| sr_no | builderid | buildnumber | portid | portversionid | timestamp | success | version |  reason | info |   commitid   | distributable |
|:----:|:---------:|:-----------:|:------:|:-------------:|:---------:|:-------:|:-------:|:-------:|:----:|:-------------:|:-------------:|
|   1   |     1     |     5568    |   677  |       1       |  XX:XX:XX |    ok   |   1.2   |   abc   |  def | abxcss12asfva |               |
|   2   |     2     |     4554    |   234  |       3       |  XX:XX:XX |    no   |  1.0.4  |   def   |  abc |  asdasda231as |               |
|   3   |     1     |     5569    |   677  |       2       |  XX:XX:XX |  not ok |  1.0.5  | trigger | fail |     abc345    |               |

# Installation statistics

## statistics

_All the results from 'mpstats' would be parsed and these 2 tables would be populated_

## port_history

### Structure

Column | Type
-------|---------
portid | integer
portversionid | integer
userid  | text
timestamp | time
variants | varchar
requested | varchar


### Example

| portid | portversionid |                userid                |     timestamp    | variants | requested |
|:------:|:-------------:|:------------------------------------:|:----------------:|:--------:|:---------:|
|   677  |       1       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:00 |     -    |    TRUE   |
|   677  |       2       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:30 | python27 |     -     |
|   234  |       3       | 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  22/05/2018 2:00 |  llvm40  |     -     |
|   677  |       1       |                  17                  | 07/09/2018 12:00 |     -    |     -     |


## os_history

### Structure

Column | Type
-------|---------
userid  | text
os_id | integer
os_arch | varchar
platform | text
xcodeversion | varchar
macportsversion | varchar
timestamp | time
default_prefix | varchar
stdlib | text



### Example

|                userid                | os_id | os_arch | platform | xcodeversion | macportsversion |     timestamp    | default_prefix |   stdlib  |
|:------------------------------------:|:-----:|:-------:|:--------:|:------------:|:---------------:|:----------------:|:--------------:|:---------:|
| 270856DE-DD7E-494F-9A99-281BED099110 |  10.5 |   i386  |  darwin  |      9.2     |      2.4.2      | 27/03/2018 12:00 |      TRUE      | stdlibc++ |
| 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  10.8 |   i486  |  darwin  |      9.2     |      2.4.0      | 27/03/2018 12:30 |      FALSE     | stdlibc++ |
|  5830GHS-DD7E-5939JS-9A99-982HSGA23  | 10.11 |   i223  |  darwin  |      9.4     |      2.4.1      |  22/05/2018 2:00 |      TRUE      |   libc++  |
