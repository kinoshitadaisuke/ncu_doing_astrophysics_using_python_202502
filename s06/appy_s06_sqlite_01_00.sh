#!/bin/sh

#
# Time-stamp: <2025/03/24 19:28:17 (UT+08:00) daisuke>
#

# making a table
sqlite3 element.db \
	"create table element (AtomicNumber integer primary key, \
	Symbol text, Name text, AtomicMass real, CPKHexColor text, \
	ElectronConfiguration text, Electronegativity real, AtomicRadius real, \
	IonizationEnergy real, ElectronAffinity real, OxidationStates text, \
	StandardState text, MeltingPoint real, BoilingPoint real, Density real, \
	GroupBlock text, YearDiscovered text);"
