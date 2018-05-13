# Database Description

* [Port index](#port-index)
  - [Ports](#ports)
  - ~[Port versions](#port_versions)~
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

Please go through [this spreadsheet](https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing) for better visualisations. Then do comment/ suggest changes in this file.

# Port index

## ports

_This table consists of all the current port information._

### Structure

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 123
portname | varchar | unique | python27
description | text | | An interpreted, object-oriented ...
long_desc | text | | Python is an interpreted, ... 
homepage | varchar | | https://www.python.org/
platform | varchar | | darwin
portversion_id | integer | references port_versions(id) |
license | varchar | | PSF
portdir | varchar | | lang/python27

**Suggestions:**
* I would remove `portversion_id`.
* And add a `version` field instead.
* The version is encoded as `@2.7.14_1`, where `2.7.14` is the actual version and `1` is the revision. It would probably be cleaner to add a separate column for `revision` than to keep parsing the version string each time when displaying the information. That's a minor hardly important personal preference though, but it might help with various database queries (often we are not really interested in revision).
* While we can keep `platform` for now, I doubt in its usefulness. What we need is either a decent implementation for listing which macOS versions are supported, potentially having a different version for different OS versions (in which case a simple `platform` field won't be enough anyway).
* I would add a boolean field specifying whether a port is under open maintainership. Maybe just call it `openmaintainer` with values True and False.
* I would add one or two fields to specify whether a port is active, obsolete or deleted. This is a slightly lower priority. Obsolete ports are always `replaced_by` another port.
  * If we want to keep track of deleted ports, it would make sense to create another table with deleted ports, listing `port_id`, `commit_shasum` (of the commit which deleted the port). And then have another table with commits, from which we could determine the date of when the port was deleted.
  * For obsolete (`replaced_by`) ports it would also make sense to have a separate table with `obsolete_port_id`, `replaced_port_id`, `commit_shasum`.

### Example

| portid(key) | portname |                                          description | long_desc                                                                                                                                 | homepage     | platform | portversionid | license | portdir       |
|-------------|:--------:|-----------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|---------------|---------|---------------|
| 123         | python27 | An interpreted, object-oriented programming language | Python is an interpreted, interactive, object-oriented programming language.                                                              | python.org   | darwin   | 1             | GPL-2+  | lang/python27 |
| 234         |  AppHack |             Program for hacking application bundles. | AppHack is a developer and theming tool to alter, replace or extract the property lists or icons of Mac OS X application bundle packages. |  apphack.com | macosx   | 10            | GPL-2+  | aqua/AppHack  |

## port_versions

_This table maps the ports with multiple different version._

**Suggestions:**
* I would remove this table, as explained in #2.
* How exactly does builder fit into this picture?

### Structure

Column | Type | Notes
-------|------|------
**id (key)** | integer | primary key
builder | integer |
version | varchar |
variants | varchar |

### Example

| portversionid(key) | portid  | version | variants |
|:------------------:|:-------:|:-------:|:--------:|
|          1         |   677   |  2.7.0  |          |
|          2         |   677   |  2.7.1  |          |
|          3         |   234   |  1.5.0  |          |

## categories

_This table lists all existing categories._

### Structure

Column | Type | Notes | Example
-------|------|-------|--------
**id (key)** | integer | primary key | 7
name | varchar | unique | lang

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
email | varchar | | jmr.nospam@macports.org
github | varchar | | jmroot

The (email, github) pair needs to be unique.

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

* _Sets up the relation between maintainerid & portid portversionid._
* _Basically tells us which maintainer is handling which all ports._

### Structure

Column | Type
-------|---------
maintainer_id | integer | references maintainer(id) | 42
port_id | integer | references port(id) | 123
portversion_id | integer | unique, references portversion(id) | 3

**Notes:**
* I would remove `portversion_id`, as per reasons already explained below the `ports` table.

# Build statistics

## builders

_This table consist of all the builders information available._

### Structure

Column | Type
-------|---------
**builderid (key)** | integer
builder | varchar
osname | text
architecture | text

### Example

| builderid (key) |            builder             |   osname  | architecture |
|:---------------:|:------------------------------:|:---------:|:------------:|
|        1        | ports-10.6_i386_legacy-builder | OS X 10.6 |  i386 x86_64 |
|        2        |    ports-10.8_x86_64-builder   | OS X 10.8 |    x86_64    |

## build_history

_Enitre build history would be saved here._

### Structure

Column | Type
-------|---------
**sr_no (key)** | integer
builderid | integer
buildnumber | integer
portid | integer
portversionid | integer
timestamp | time
success | varchar
version | varchar
reason | text
info | text
commitid | varchar
distributable | text

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
