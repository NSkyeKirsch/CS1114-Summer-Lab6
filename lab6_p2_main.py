import lab6_p2_tetrahedron as tetra
import lab6_p2_dodecahedron as dodeca
import lab6_p2_cube as cube
import lab6_p2_icosahedron as icosa
import lab6_p2_octahedron as octa
import lab6_p2_pentagonal as penta_trape


def main():
    die_list = [tetra.Tetrahedron(3), tetra.Tetrahedron(),
                dodeca.Dodecahedron(3), dodeca.Dodecahedron(),
                cube.Cube(3), cube.Cube(),
                icosa.Icosahedron(3), icosa.Icosahedron(),
                octa.Octahedron(3), octa.Octahedron(),
                penta_trape.Pentagonal_Trapezohedron(3), penta_trape.Pentagonal_Trapezohedron()]

    for die in die_list:
        print('BEFORE:', die)
        die.roll()
        print('AFTER:', die)


if __name__ == "__main__":
    main()

