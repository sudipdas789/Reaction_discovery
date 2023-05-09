from sys import argv

def read_xyz(filename):
    """Read XYZ file and return atom names and coordinates

    Args:
        filename:  Name of xyz data file

    Returns:
        atom_names: Element symbols of all the atoms
        coords: Cartesian coordinates for every frame.
    """
    with open(filename, 'r') as f:
        for line in f:
            try:
                natm = int(line)  # Read number of atoms
                next(f)     # Skip over comments
                atom_names = []
                index = []
                for i in range(natm):
                    line = next(f).split()
                    atom_names.append(line[0])
                    index.append(line[1])
            except (TypeError, IOError, IndexError, StopIteration):
                raise ValueError('Incorrect XYZ file format')
    return atom_names,index 


def cv(filename,nm,r0_data):

    atoms,index = read_xyz(filename)

    n = nm[0]
    m = nm[1]

    arg =[]
    print('UNITS LENGTH=A')
    for i,ii in enumerate(index):
      for j,jj in enumerate(index):
          r0 = r0_data[atoms[i]+atoms[j]]
          aij = "a_"+str((i+1))+"_"+str((j+1))
          aji = "a_"+str((j+1))+"_"+str((i+1))
          if (aji) in arg:
             print('{}: CUSTOM ARG={} FUNC=x PERIODIC=NO\t'.format(aij,aji))
          else:
             print('{}: COORDINATION GROUPA={} GROUPB={} R_0={} NN={} MM={}\t'.format(aij,ii,jj,r0,n,m))
          arg.append(aij)
      print()
    print()
    print("cv: PYTORCH_MODEL MODEL=torch_cv.pt ARG=",*arg,sep = ',')
    print()
    print("PRINT ARG=cv.* FILE=colvar")

    return

filename = argv[1]
NARG=1+1
#----------------------------------------------------------------------
# Required Input file:
# 1) frame.xyz 
#----------------------------------------------------------------------
if (len(argv) != NARG) :
   print (argv[0],": error in argument number")
   print ("USAGE :")
   print (argv[0]," frame.xyz")
   exit(33)


r0_data = {'OH': 1.4,
           'HO': 1.4,
           'HH': 1.2,
           'CH': 1.2,
           'HC': 1.2,
           'CC': 1.7,
           'OO': 1.6,
           'OC': 1.8,
           'CO': 1.8,
           }
n = 6
m = 10 

nm = [n,m]
cv(filename,nm,r0_data)
