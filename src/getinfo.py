from bioservices import *
import time
import sys

def get_uniprot_list(file_name):
    res = {}
    with open(file_name, "r") as f:
        for line in f:
            array = line.strip().split(",")
            res[array[1]] = array[0]
    return res

def get_pdbid(uniprot_list):
    u = UniProt()
    return u.mapping("ID", "PDB_ID", uniprot_list)

def write_res(out_file_name, info_map, name_map):
    with open(out_file_name, "w") as f:
        for key in name_map.keys():
            if info_map.has_key(key):
                f.write(name_map[str(key)] + "," + str(key) + "," + str(info_map[key]) + "\n")
            else:
                f.write(name_map[str(key)] + "," + str(key) + "," + "[]" + "\n")
            #f.write(str(key) + str(info_map[key]) + "\n")

def main(file_name, out_file_name):
    name_map = get_uniprot_list(file_name)
    info_map = get_pdbid(list(name_map.keys()))
    write_res(out_file_name, info_map, name_map)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 3:
        print "invalid argment"
        sys.exit()
    main(argv[1], argv[2])
