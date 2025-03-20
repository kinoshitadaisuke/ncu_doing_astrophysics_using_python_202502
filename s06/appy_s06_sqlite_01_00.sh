#!/bin/sh

#
# Time-stamp: <2025/03/20 21:12:15 (UT+08:00) daisuke>
#

# making a table
sqlite3 element.db "create table element (AtomicNumber integer primary key, \
Symbol text, Name text, AtomicMass real, CPKHexColor text, \
ElectronConfiguration text, Electronegativity real, AtomicRadius real, \
IonizationEnergy real, ElectronAffinity real, OxidationStates text, \
StandardState text, MeltingPoint real, BoilingPoint real, Density real, \
GroupBlock text, YearDiscovered text);"
