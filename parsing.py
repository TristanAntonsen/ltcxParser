import numpy as np

class Lattice():

    def __init__(self, filename):

        self.parse_ltcx(filename)
        self.bounding_box()
        self.centroid()

    def parse_ltcx(self, filename):

        with open(filename,'r',encoding="UTF-8") as file:
            lines = file.readlines()

        nodes = {}
        beams = {}
        radii = {}

        for row in lines:
            row=row.rstrip('\n')
            row = row.strip().strip('<').strip('/>')
            row = row.replace('"','')

            row = row.split(" ")

            if row[0] == "graph":
                for item in row[1:]:
                    item = item.split("=")
                    if item[0] == 'units':
                        self.units = item[1]

            if row[0] == "node":
                node = []
                id = int(row[1][3:])
                node.append(float(row[2][2:]))
                node.append(float(row[3][2:]))
                node.append(float(row[4][2:]))
                radius = float(row[5][2:])

                nodes[id] = node
                radii[id] = radius

            if row[0] == "beam":
                beam = []
                id = int(row[1][3:])
                beam.append(int(row[2][3:]))
                beam.append(int(row[3][3:]))
                beams[id] = beam
    
        self.beams = beams
        self.nodes = nodes
        self.node_radii = radii

        self.beam_count = len(beams)
        self.node_count = len(nodes)

    def bounding_box(self):
        
        node_coords = self.nodes.values()
        x_vals = [n[0] for n in node_coords]
        y_vals = [n[1] for n in node_coords]
        z_vals = [n[2] for n in node_coords]

        min_x = np.min(x_vals)
        min_y = np.min(y_vals)
        min_z = np.min(z_vals)
        max_x = np.max(z_vals)
        max_y = np.max(y_vals)
        max_z = np.max(z_vals)

        # bbox = [min point, max point]
        self.aabb = [[min_x, min_y, min_z],
                     [max_x, max_y, max_z]]

        # lengths = x/y/z spans
        self.x_length = max_x - min_x
        self.y_length = max_y - min_y
        self.z_length = max_z - min_z

    def centroid(self):
        cx = (self.aabb[1][0] + self.aabb[0][0]) / 2
        cy = (self.aabb[1][1] + self.aabb[0][1]) / 2
        cz = (self.aabb[1][2] + self.aabb[0][2]) / 2

        self.aabb_centroid = [cx, cy, cz]

if __name__ == "__main__":
    from pprint import pprint

    lattice = Lattice("demo.ltcx")

    print("Beam conut:",lattice.beam_count)
    print("Node count:",lattice.node_count)
    print("Units:",lattice.units)
    print("Bounding box:",lattice.aabb)
    print("Dimensions:",f"{lattice.x_length} x {lattice.y_length} x {lattice.z_length}")
    print("Bounding box centroid:",lattice.aabb_centroid)