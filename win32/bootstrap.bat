:: Hive Colony Framework
:: Copyright (C) 2008-2012 Hive Solutions Lda.
::
:: This file is part of Hive Colony Framework.
::
:: Hive Colony Framework is free software: you can redistribute it and/or modify
:: it under the terms of the GNU General Public License as published by
:: the Free Software Foundation, either version 3 of the License, or
:: (at your option) any later version.
::
:: Hive Colony Framework is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
:: GNU General Public License for more details.
::
:: You should have received a copy of the GNU General Public License
:: along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

:: __author__    = João Magalhães <joamag@hive.pt>
:: __version__   = 1.0.0
:: __revision__  = $LastChangedRevision$
:: __date__      = $LastChangedDate$
:: __copyright__ = Copyright (c) 2008-2012 Hive Solutions Lda.
:: __license__   = GNU General Public License (GPL), Version 3

:: turns off the echo
@echo off

:: prints an information message
echo Cloning the hive repositories ...

:: cloning the various colony repositories
git clone git@github.com:hivesolutions/colony.git colony
cd colony && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
git clone git@github.com:hivesolutions/colony_plugins.git colony_plugins
cd colony_plugins && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
git clone git@github.com:hivesolutions/colony_config.git colony_config
cd colony_config && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
git clone git@github.com:hivesolutions/omni.git omni
cd omni && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..

:: cloning the ui external libraries
git clone git@github.com:hivesolutions/uxf.git uxf
cd uxf && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
git clone git@github.com:hivesolutions/uxf_bin.git uxf_bin
cd uxf_bin && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..

:: cloning the varius extra plugins
git clone git@github.com:hivesolutions/hive_site.git hive_site
cd hive_site && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
git clone git@github.com:hivesolutions/hive_blog.git hive_blog
cd hive_blog && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..

:: cloning misc projects
git clone git@github.com:hivesolutions/dns_registers.git dns_registers
cd dns_registers && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..

:: cloning the viriatum projects
git clone git@github.com:hivesolutions/viriatum.git viriatum
cd viriatum && git submodule init && git submodule update && git submodule foreach git checkout master
cd ..
