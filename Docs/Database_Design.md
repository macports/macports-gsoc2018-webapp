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

Column | Type
-------|---------
**id (key)** | integer
portname | varchar
description | text
long_desc | text
homepage | varchar
platform | varchar
portversionid | varchar
license | varchar
portdir | varchar

### Example

| portid(key) | portname |                                          description | long_desc                                                                                                                                 | homepage     | platform | portversionid | license | portdir       |
|-------------|:--------:|-----------------------------------------------------:|-------------------------------------------------------------------------------------------------------------------------------------------|--------------|----------|---------------|---------|---------------|
| 123         | python27 | An interpreted, object-oriented programming language | Python is an interpreted, interactive, object-oriented programming language.                                                              | python.org   | darwin   | 1             | GPL-2+  | lang/python27 |
| 234         |  AppHack |             Program for hacking application bundles. | AppHack is a developer and theming tool to alter, replace or extract the property lists or icons of Mac OS X application bundle packages. |  apphack.com | macosx   | 10            | GPL-2+  | aqua/AppHack  |

## builders

_This table consist of all the builders information available._

### Structure

...

### Example

| builderid (key) |            builder             |   osname  | architecture |
|:---------------:|:------------------------------:|:---------:|:------------:|
|        1        | ports-10.6_i386_legacy-builder | OS X 10.6 |  i386 x86_64 |
|        2        |    ports-10.8_x86_64-builder   | OS X 10.8 |    x86_64    |

## port_versions

_This table maps the ports with multiple different version._

### Structure

...

### Example

| portversionid(key) | portid  | version | variants |
|:------------------:|:-------:|:-------:|:--------:|
|          1         |   677   |  2.7.0  |          |
|          2         |   677   |  2.7.1  |          |
|          3         |   234   |  1.5.0  |          |

## maintainers

_Which maintainers maintain which ports_

### Structure

...

### Example

| maintainid(key) | maintainers | version |
|:---------------:|:-----------:|:-------:|
|        1        |    mojca    |  2.7.0  |
|        2        |    vishnu   |  2.7.1  |

## maintainer_portid

* _Sets up the relation between maintainerid & portid  portversionid._
* _Basically tells us which maintainer is handling which all ports._

| maintainid (not unique) | portid (not unique) | portversionid |
|:-----------------------:|:-------------------:|:-------------:|
|            1            |         234         |       3       |
|            1            |         677         |       2       |
|            2            |         677         |       1       |

## build_history

_Enitre build history would be saved here._

| Sr no | builderid | buildnumber | portid | portversionid | timestamp | success | version |  reason | info |   commit id   | distributable |
|:-----:|:---------:|:-----------:|:------:|:-------------:|:---------:|:-------:|:-------:|:-------:|:----:|:-------------:|:-------------:|
|   1   |     1     |     5568    |   677  |       1       |  XX:XX:XX |    ok   |   1.2   |   abc   |  def | abxcss12asfva |               |
|   2   |     2     |     4554    |   234  |       3       |  XX:XX:XX |    no   |  1.0.4  |   def   |  abc |  asdasda231as |               |
|   3   |     1     |     5569    |   677  |       2       |  XX:XX:XX |  not ok |  1.0.5  | trigger | fail |     abc345    |               |

## statistics

_All the results from 'mpstats' would be parsed and these 2 tables would be populated_

## port_history

| portid | portversionid |                userid                |     timestamp    | variants | requested |
|:------:|:-------------:|:------------------------------------:|:----------------:|:--------:|:---------:|
|   677  |       1       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:00 |     -    |    TRUE   |
|   677  |       2       | 270856DE-DD7E-494F-9A99-281BED099110 | 27/03/2018 12:30 | python27 |     -     |
|   234  |       3       | 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  22/05/2018 2:00 |  llvm40  |     -     |
|   677  |       1       |                  17                  | 07/09/2018 12:00 |     -    |     -     |


## os_history

|                userid                | os id | os_arch | platform | xcodeversion | macportsversion |     timestamp    | default prefix |   stdlib  |
|:------------------------------------:|:-----:|:-------:|:--------:|:------------:|:---------------:|:----------------:|:--------------:|:---------:|
| 270856DE-DD7E-494F-9A99-281BED099110 |  10.5 |   i386  |  darwin  |      9.2     |      2.4.2      | 27/03/2018 12:00 |      TRUE      | stdlibc++ |
| 28130GH-ASD7E-494F-9A99-283HSJVU1293 |  10.8 |   i486  |  darwin  |      9.2     |      2.4.0      | 27/03/2018 12:30 |      FALSE     | stdlibc++ |
|  5830GHS-DD7E-5939JS-9A99-982HSGA23  | 10.11 |   i223  |  darwin  |      9.4     |      2.4.1      |  22/05/2018 2:00 |      TRUE      |   libc++  |
