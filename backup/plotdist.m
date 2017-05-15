clc;
clear;
%load size.out % load raw data
load size.out 
pts = (min(size):max(size));
[f,xi,bw]= ksdensity(size,pts);
[result,gof] = createFit(xi,f)
% Result is the exponential function 
% gof if the goodness of fit stats

%load simulate.txt
%range = (0:50000);
%[f2,xi2,bw2] = ksdensity(simulate,pts);
%[out_sim,gof_sim] = createFit(xi2,f2)
