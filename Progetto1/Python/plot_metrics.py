import matplotlib.pyplot as plt
from scipy import io

def plot_metrics(matrices, errs, times, mems):

    matrices = get_shapes(matrices)

    #TODO: Improve plots
    plt.plot(matrices, errs)
    plt.yscale('log')
    plt.title('errs')
    plt.grid(True)
    plt.ylabel('some numbers')
    plt.show()

    plt.plot(matrices, times)
    plt.yscale('log')
    plt.title('times')
    plt.grid(True)
    plt.ylabel('some numbers')
    plt.show()

    plt.plot(matrices, mems)
    plt.yscale('log')
    plt.title('mems')
    plt.grid(True)
    plt.ylabel('some numbers')
    plt.show()

def get_shapes(matrices):
    i = 0
    for matrix_name in matrices:
        matrix_path = "./Matrix/" + matrix_name + ".mtx"
        matrix = io.mmread(matrix_path)
        matrices[i] = matrix_name + ": " + str(matrix.shape[0])
        i = i + 1
    
    return matrices