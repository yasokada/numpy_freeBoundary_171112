import numpy as np

'''
v0.4 Nov. 18, 2017 find_freeBoundary()
  - Test_get_shown_triangles() uses find_freeBoundary()
  - Test_get_shown_triangles_3tetrahedra() uses find_freeBoundary()
  - Test_get_shown_triangles_fromfile() uses find_freeBoundary()
  - add find_freeBoundary() 
v0.3 Nov. 18, 2017 test reading from file
  - add Test_get_shown_triangles_fromfile()
v0.2 Nov. 12, 2017 test with 3 tetrahedra
  - add Test_get_shown_triangles_3tetrahedra()
v0.1 Nov. 12, 2017
  - Test_get_shown_triangles()
  - is_same_list()
  - add get_shown_triangles()
  - add get_triangle_sets()
  - add find_hidden_triangleIndex()
'''

# on Python 3.5.2
# coding rule:PEP8

def find_freeBoundary(tris):
    trihdn = find_hidden_triangleIndex(tris)
    triall = get_triangle_sets(tris)
    trishown = get_shown_triangles(trihdn, triall)
    return trishown


def find_hidden_triangleIndex(tris):
    overlap = []
    for lidx in range(len(tris) - 1):
        for ridx in range(len(tris)):
            if lidx == ridx:
                continue
            wrk = []
            for elem in tris[lidx]:
                if elem in tris[ridx]:
                    wrk += [elem]
            if (len(wrk) == 3):
                overlap += [wrk]
    return overlap


def get_triangle_sets(tris):
    idx1 = [0, 1, 2]
    idx2 = [0, 1, 3]
    idx3 = [0, 2, 3]
    idx4 = [1, 2, 3]
    wrk = []
    for lidx in range(len(tris)):
        wrk += [tris[lidx][idx1]]
        wrk += [tris[lidx][idx2]]
        wrk += [tris[lidx][idx3]]
        wrk += [tris[lidx][idx4]]
    return wrk


def is_same_list(lhs, rhs):
    cnt = 0
    for lelem in lhs:
        if lelem in rhs:
            cnt += 1
    return (cnt == 3)


def get_shown_triangles(trihdns, triall):
    wrk = []
    for atri in triall:
        ishidden = False
        for ahidden in trihdns:
            if is_same_list(ahidden, atri):
                ishidden = True
        if not ishidden:
            wrk += [atri]
    return wrk


def Test_get_shown_triangles():
    tri1 = [1092, 856, 1094, 1095]  # index of triangles for tetrahedra
    tri2 = [1092, 1095, 896, 856]  # index of triangles for tetrahedra
    tris = [np.array(tri1), np.array(tri2)]

    trishown = find_freeBoundary(tris)
    print('---except for hidden---')
    for elem in trishown:
        print(elem)


def Test_get_shown_triangles_3tetrahedra():
    tri1 = [1098, 1175, 1170, 1204]  # index of triangles for tetrahedra
    tri2 = [1098, 1170, 1175, 1172]  # index of triangles for tetrahedra
    tri3 = [1098, 1170, 1203, 1204]  # index of triangles for tetrahedra
    tris = [np.array(tri1), np.array(tri2), np.array(tri3)]

    trishown = find_freeBoundary(tris)
    for elem in trishown:
        print(elem)


def Test_get_shown_triangles_fromfile():
    tris = np.genfromtxt('tri_bef_171118.txt', delimiter='   ')
    trishown = find_freeBoundary(tris)
    for elem in trishown:
        print(elem)

if __name__ == '__main__':
    Test_get_shown_triangles()
    # Test_get_shown_triangles_3tetrahedra()
    # Test_get_shown_triangles_fromfile()
