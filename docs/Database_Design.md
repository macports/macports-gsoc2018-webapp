# Database Description

- [Ports](#ports)
- [Builders](#builders)
- [Maintainers](#maintainers)
- [Maintainer - Port](#maintainer_portid)
- [Build History](#build_history) (The most important table)
- [Statistics](#statistics)
- [Port History](#port_history)
- [OS History](#os_history)

Please go through : https://docs.google.com/spreadsheets/d/1Kgbpl1aHn-10fjXh-f4Wz24-TQw4Coaucidpxp7ZqOQ/edit?usp=sharing

For better visualisations. Then do comment/ suggest changes in this file .

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
portversionid | varchar | |
license | varchar | | PSF
portdir | varchar | | lang/python27

**Suggestions:**
* I would remove `portversionid`
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

## port_versions

_This table maps the ports with multiple different version._

### Structure

Column | Type
-------|---------
**portversionid (key)** | integer
builder | integer
version | text
variants | text

### Example

| portversionid(key) | portid  | version | variants |
|:------------------:|:-------:|:-------:|:--------:|
|          1         |   677   |  2.7.0  |          |
|          2         |   677   |  2.7.1  |          |
|          3         |   234   |  1.5.0  |          |

## maintainers

_Maintainer and ther id_

### Structure

Column | Type
-------|---------
**maintainid (key)** | integer
maintainers | text


### Example

| maintainid(key) | maintainers | 
|:---------------:|:-----------:|
|        1        |    mojca    |
|        2        |    vishnu   |

## maintainer_port

* _Sets up the relation between maintainerid & portid  portversionid._
* _Basically tells us which maintainer is handling which all ports._

### Structure

Column | Type
-------|---------
**maintainer_id** | integer
portid | integer
portversionid | integer


### Example

| maintainer_id (not unique) | portid (not unique) | portversionid |
|:-----------------------:|:-------------------:|:-------------:|
|            1            |         234         |       3       |
|            1            |         677         |       2       |
|            2            |         677         |       1       |

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
