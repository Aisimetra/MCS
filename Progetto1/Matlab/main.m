%look at properties of each matrix in order to better understand matlab
%output: { diagonal, U, L, Hermitian, tridiagonal, Real}
%(don't execute them all together!)

%{
[prop0] = check_properties('./matrices/GT01R.mat');
[prop1] = check_properties('./matrices/ns3Da.mat');
[prop2] = check_properties('./matrices/TSC_OPF_1047.mat');
[prop3] = check_properties('./matrices/G3_circuit.mat');
[prop4] = check_properties('./matrices/ifiss_mat.mat');
[prop5] = check_properties('./matrices/nd24k.mat');
[prop6] = check_properties('./matrices/bundle_adj.mat');
[prop7] = check_properties('./matrices/Hook_1498.mat');

%}


%capire quale workflow usa per risolvere la matrice
%spparms('spumoni',2)

[x, err, time, memory] = solve_linear('./Matrix/GT01R.mat'); %7,980
plot_matrix = [size(x), err, time, memory];

[x, err,time, memory] = solve_linear('./Matrix/TSC_OPF_1047.mat'); %8,140
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory] = solve_linear('./Matrix/ns3Da.mat'); %20,414
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory] = solve_linear('./Matrix/nd24k.mat'); %72,000
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory] = solve_linear('./Matrix/ifiss_mat.mat'); %96,307
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory]= solve_linear('./Matrix/bundle_adj.mat'); %513,351
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory] = solve_linear('./Matrix/Hook_1498.mat'); %1,498,023
plot_matrix = [plot_matrix; [size(x), err, time, memory]];

[x, err,time, memory] = solve_linear('./Matrix/G3_circuit.mat'); %1,585,478
plot_matrix = [plot_matrix; [size(x), err, time, memory]];


plot_things(plot_matrix);


