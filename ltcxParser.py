def parse_ltcx(filename):

    with open(filename,'r',encoding="UTF-8") as file:
        lines = file.readlines()

    nodes = {}
    beams = {}

    for row in lines:
        row=row.rstrip('\n')
        row = row.strip().strip('<').strip('/>')
        row = row.replace('"','')

        row = row.split(" ")

        if row[0] == "node":
            node = []
            id = int(row[1][3:])
            node.append(float(row[2][2:]))
            node.append(float(row[3][2:]))
            node.append(float(row[4][2:]))
            nodes[id] = node

        if row[0] == "beam":
            beam = []
            id = int(row[1][3:])
            beam.append(int(row[2][3:]))
            beam.append(int(row[3][3:]))
            beams[id] = beam

    return beams, nodes
