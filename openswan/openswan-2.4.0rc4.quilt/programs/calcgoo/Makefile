# Makefile for miscelaneous programs
# Copyright (C) 2002  Michael Richardson	<mcr@freeswan.org>
# 
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See <http://www.fsf.org/copyleft/gpl.txt>.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# RCSID $Id: Makefile,v 1.3 2004/12/18 18:13:39 mcr Exp $

OPENSWANSRCDIR?=$(shell cd ../..; pwd)
include ${OPENSWANSRCDIR}/Makefile.inc

PROGRAM=calcgoo

include ${srcdir}../Makefile.program

#
# $Log: Makefile,v $
# Revision 1.3  2004/12/18 18:13:39  mcr
# 	adjusted Makefiles so that ${OBJDIR} builds work.
#
# Revision 1.2  2004/04/03 19:44:45  ken
# FREESWANSRCDIR -> OPENSWANSRCDIR (patch by folken)
#
# Revision 1.1  2002/06/10 04:27:25  mcr
# 	calcgoo program processes kernel symbol list and generates a
# 	composite value by xor'ing the programmed symbol.
#
# Revision 1.1  2002/06/10 00:19:44  mcr
# 	rename "ipsec check" to "ipsec verify"
#
# Revision 1.1  2002/06/08 17:01:25  mcr
# 	added new program "ipsec check" to do rudamentary testing
# 	on a newly installed system to see if it is OE ready.
#
#
#

