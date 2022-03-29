# set workspace
#setwd("~/Progetto1/R")

# Library con comandi per l'installazione se necessario
#install.packages(Matrix)
#install.packages(SparseM)
#install.packages(bigmemory)

library(Matrix)
library(SparseM)
library(bigmemory)


# function
solvelinear <- function(matrix){
  
  # Read matrix
  A <- readMM(matrix)
  
  # Time
  start_time <- Sys.time()
  
  # Exact solution
  xe = c(rep(1,dim(A)[1]))
  
  # Compute value of b
  b = A %*% xe 
  
  # Solve linear system
  x = SparseM::solve(A,b);
  
  # time
  end_time <- Sys.time();
  total_time = end_time - start_time;
  
  #errore
  err = norm(as.matrix(setdiff(x, xe)), type="2")/norm(as.matrix(xe), type="2")
  
  #result
  matrix = sub(".mtx","", matrix)
  total_time= sub("Time difference of ","",total_time)
  total_time= sub(" secs", "", total_time)
  result = c(err, total_time,matrix);
  
  return(result);
}

# solve matrix
x.1 = solvelinear("GT01R.mtx")
x.2 = solvelinear("TSC_OPF_1047.mtx")
x.3 = solvelinear("ns3Da.mtx")
x.4 = solvelinear("ifiss_mat.mtx")
x.5 = solvelinear("bundle_adj.mtx")
x.6 = solvelinear("G3_circuit.mtx")

# metrix
name  = c(x.1[3],x.2[3],x.3[3],x.4[3],x.5[3],x.6[3])
error = c(x.1[1],x.2[1],x.3[1],x.4[1],x.5[1],x.6[1])
time  = c(x.1[2],x.2[2],x.3[2],x.4[2],x.5[2],x.6[2])
print(time)
print(error)
print(name)