#!/usr/bin/env python
#
# Copyright 2011 Shadow Robot Company Ltd.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#

PKG = "csv_to_urdf"
import roslib; roslib.load_manifest(PKG)
import unittest
import os

from csv_to_urdf.csv_to_urdf import CsvToUrdf

class TestCsvToUrdf(unittest.TestCase):
    def test_csv_to_urdf(self):
        csv_path = "test/robot.csv"
        urdf_path = "/tmp/robot_tmp.urdf"
        CsvToUrdf(csv_path, urdf_path)

        # check if urdf is correct
        if os.system("`rospack find urdf_parser`/bin/check_urdf /tmp/robot_tmp.urdf") != 0:
            self.fail("urdf not correct")

if __name__ == "__main__":
    import rostest
    rostest.rosrun(PKG, 'test_csv_to_urdf.py', TestCsvToUrdf)
