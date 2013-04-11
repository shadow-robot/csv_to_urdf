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

import roslib; roslib.load_manifest('csv_to_urdf')
from csv_to_urdf.element import Element

class CsvToUrdf(object):
    """
    """

    def __init__(self, path):
        """
        """
        try:
            file = open(path, "r")
        except:
            print "Couldn't open file: "+ path
            return

        self.all_lines = file.readlines()
        file.close()

        #contains all the elements described in the csv file
        self.elements = []

        #first line contains titles
        self.titles = []
        first_line = True
        for line in self.all_lines:
            if first_line:
                first_line = False
                self.parse_titles_(line)
            else:
                self.parse_line_(line)

        self.to_urdf()

    def parse_titles_(self, line):
        splitted_line = line.split(";")
        for title in splitted_line:
            self.titles.append(title.strip(" ").strip("\n").strip("\t"))

    def parse_line_(self, line):
        splitted_line = line.split(";")
        data_map = dict()
        for title, data in zip(self.titles, splitted_line):
            data_map[title] = data.strip(" ").strip("\n").strip("\t")
        self.elements.append( Element(data_map) )

    def to_urdf(self):
        for element in self.elements:
            element.to_urdf()

if __name__ == "__main__":
    path = "test/robot.csv"
    csv_to_urdf = CsvToUrdf(path)

