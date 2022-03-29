from solve_linear import solve_linear
from plot_metrics import plot_metrics
from memory_profiler import profile, memory_usage

# Calcolo della memoria: sfrutto memory_usage, non profile (non penso si possano salvare i risultati su una variabile da lì):
# una volta che ha svolto tutti i task il main chiama la funzione solve linear tramite la funzione memory usage e restituisce una lista con
# la quantità di memoria impegata (non ho capito bene con quale timeframe). Facendo il max di questa lista comunque troviamo quanta memoria 
# e stata impiegata. Ci serve solo vedere quanta memoria viene impiegata prima di iniziare a risolvere i sistemi, poi la sottraiamo ad ogni valore
# Una volta visto questo, e una volta caricate tutte le matrici si possono salvare i risultati su una lista (basta eliminare la variabile relativa
# alla matrice, per evitare difficolta o tempi molto lunghi

def main():
    errs = []
    times = []
    mems = []

    # TODO: Add all the matrices 
    matrices = ["GT01R", "ns3Da"]

    for matrix in matrices:
        matrix_path = "./Matrix/" + matrix + ".mtx"
        err, el_time = solve_linear(matrix_path)
        #memoria impiegata 
        mem = memory_usage((solve_linear, {matrix_path}))
        #picco di memoria utilizzata (dato che ci serve per il plot)
        max_mem = max(mem)
        
        print ("%5.2f secs %5.2f MByte for the matrix %s" % (el_time, max_mem, matrix))

        errs.append(err)
        times.append(el_time)
        mems.append(max_mem)
    
    # TODO: Use the shape of the matrices instead of the names
    plot_metrics(matrices, errs, times, mems)


if __name__ == "__main__":
    main()