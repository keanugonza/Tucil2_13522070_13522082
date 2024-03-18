# Fungsi ini untuk menerima masukan dari user dan
# Menghandle jika masukan tidak sesuai atau salah format

class textcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    CYAN = '\033[36m'

def get_points():
    while True:
        try:
            n = int(input(textcolors.BOLD + textcolors.CYAN + "Enter the number of points: " + textcolors.ENDC))
            if n <= 2:
                print(textcolors.FAIL + "Bezier Curve Cannot be Constructed. Please Re-enter Input!" + textcolors.ENDC)
                continue
            points = [tuple(map(float, input(textcolors.BOLD + textcolors.CYAN + f"Enter the coordinates of point P{i} (separated by space): " + textcolors.ENDC).split())) for i in range(n)]
            iterations = int(input(textcolors.BOLD + textcolors.CYAN + "Enter the number of iterations: " + textcolors.ENDC))
            if iterations <= 0:
                print(textcolors.FAIL + "Number of iterations cannot be less than one. Please Re-enter Input!" + textcolors.ENDC)
                continue
            return n, points, iterations
        except ValueError:
            print(textcolors.FAIL + "Input must be an integer. Please Re-enter Input!" + textcolors.ENDC)