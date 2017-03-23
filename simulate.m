clear;
clc
load size.out;
pd = fitdist(size,'Exponential');
fout = fopen('simulate.txt','at');
for i=1:45190
   r = random(pd);
   fprintf(fout,'%5.5f \n',r);
   disp(r)
end
fclose(fout);