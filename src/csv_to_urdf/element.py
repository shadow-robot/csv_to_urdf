class Element(object):
    """
    """

    def __init__(self, data):
        """
        """
        self.data = data

        self.compute_sizes_()

    def to_urdf(self):
        urdf = ""
        urdf += "<link name=\""+self.data["JOINT"]+"_link\">\n"
        urdf += "  <inertial>\n"
        urdf += "    <origin xyz=\"0 0 0\" rpy=\"0 0 0\" />\n"
        urdf += "    <mass value=\"0.008\" />\n"
        urdf += "    <inertia  ixx=\"0.0\" ixy=\"0.0\"  ixz=\"0.0\"  iyy=\"0.1\"  iyz=\"0.0\"\n"
        urdf += "	      izz=\"0.0\" />\n"
        urdf += "  </inertial>\n"
        urdf += "  <visual>\n"
        urdf += "    <origin xyz=\""+str(self.size_x / 2.0)+ " " +str(self.size_y / 2.0)+ " " +str(self.size_z / 2.0)+ " " + "\" rpy=\"0 0 0\" />\n"
        urdf += "    <geometry name=\""+self.data["JOINT"]+"_visual\">\n"
        urdf += "      <box size=\""+ str(self.size_x) + " " + str(self.size_y) + " "+ str(self.size_z) + "\" />\n"
        urdf += "    </geometry>\n"
        urdf += "    <material name=\"LightGrey\" />\n"
        urdf += "  </visual>\n"
        urdf += "  <collision>\n"
        urdf += "    <origin xyz=\""+str(self.size_x / 2.0)+ " " +str(self.size_y / 2.0)+ " " +str(self.size_z / 2.0)+ " " + "\" rpy=\"0 0 0\" />\n"
        urdf += "    <geometry name=\""+self.data["JOINT"]+"_collision_geom\">\n"
        urdf += "      <box size=\""+ str(self.size_x) + " " + str(self.size_y) + " "+ str(self.size_z) + "\" />\n"
        urdf += "    </geometry>\n"
        urdf += "  </collision>\n"
        urdf += "</link>\n"
        urdf += "\n"
        urdf += "<joint name=\""+self.data["JOINT"]+"\" type=\"revolute\">\n"
        urdf += "  <parent link=\""+self.data["PARENT"]+"_link\"/>\n"
        urdf += "  <child link=\""+self.data["JOINT"]+"_link\"/>\n"
        urdf += "  <origin xyz=\""+ self.data["OFFSETX"]+" " +self.data["OFFSETY"]+" "+self.data["OFFSETZ"] + "\" rpy=\""+self.data["ROLL"]+" " +self.data["PITCH"]+" "+self.data["YAW"]+"\" /> \n"
        urdf += "  <axis xyz=\""+ self.data["AXISXY"]+" "+ self.data["AXISYZ"]+" "+ self.data["AXISZX"]+" "+"\"/>\n"
        urdf += "  <limit lower=\""+self.data["AXISMIN"]+"\" upper=\""+self.data["AXISMAX"]+"\"\n"
        urdf += "	 effort=\"10\" velocity=\"1.0\"/>\n"
        urdf += "  <dynamics damping=\"50.5\"/>\n"
        urdf += "</joint>\n"
        urdf += "\n"
        urdf += "<transmission type=\"pr2_mechanism_model/SimpleTransmission\" name=\""+self.data["JOINT"]+"_transmission\">\n"
        urdf += "  <actuator name=\""+self.data["JOINT"]+"\" />\n"
        urdf += "  <joint name=\""+self.data["JOINT"]+"\" />\n"
        urdf += "  <mechanicalReduction>1</mechanicalReduction>\n"
        urdf += "  <motorTorqueConstant>1</motorTorqueConstant>\n"
        urdf += "  <pulsesPerRevolution>90000</pulsesPerRevolution>\n"
        urdf += "</transmission>\n"

        return urdf

    def compute_sizes_(self):
        self.size_x = max(float(self.data["OFFSETX"]), 0.02)
        self.size_y = max(float(self.data["OFFSETY"]), 0.02)
        self.size_z = max(float(self.data["OFFSETZ"]), 0.02)
