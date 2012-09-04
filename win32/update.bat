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

:: __author__    = Jo�o Magalh�es <joamag@hive.pt>
:: __version__   = 1.0.0
:: __revision__  = $LastChangedRevision$
:: __date__      = $LastChangedDate$
:: __copyright__ = Copyright (c) 2008-2012 Hive Solutions Lda.
:: __license__   = GNU General Public License (GPL), Version 3

:: turns off the echo
@echo off

:: prints an information message
echo Updating the hive repositories ...

:: cloning the various colony repositories
cd colony && git pull && git submodule foreach git pull
cd ..
cd colony_plugins && git pull && git submodule foreach git pull
cd ..
cd colony_config && git pull && git submodule foreach git pull
cd ..
cd omni && git pull && git submodule foreach git pull
cd ..

:: cloning the ui external libraries
cd uxf && git pull && git submodule foreach git pull
cd ..
cd uxf_bin && git pull && git submodule foreach git pull
cd ..

:: cloning the varius extra plugins
cd hive_site && git pull && git submodule foreach git pull
cd ..
cd hive_blog && git pull && git submodule foreach git pull
cd ..

:: cloning the viriatum projects
cd viriatum && git pull && git submodule foreach git pull
cd ..
