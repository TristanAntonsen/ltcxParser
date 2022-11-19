# nTopology .LTCX file parser

Simple tool for parsing nTopology .ltcx lattice file types. Creates a Lattice class containing beams, nodes, and basic bounding box information. 

Later additions could include writing .ltcx files or performing simple manipulations or additional calculations.

---

### Usage

``` python
lattice = Lattice(<file_path>)
```

| Attribute | Type | Description | Format |
| :--- | :---: | :---: |  :---: | 
| units | Str | Units | "mm" | 
| beams | Dict | Beam connections | { id : [n1, n2] } | 
| nodes | Dict | Node coordinates | { id : [x, y, z] } | 
| node_count | Int | Node count | | 
| beam_count | Int | Beam count | | 
| aabb | List | Axis-oriented bounding box | [min_point, max_point] | 
| aabb_centroid | List | AABB Centroid | [x, y, z] | 
| x/y/z_length | Float | AABB dimensions | | 
