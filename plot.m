load size.out
[y2,x2] = ecdf(size);
[y1,x1] = hist(size);
plotyy(x1,y1,x2,y2,@(x,y)bar(x,y,1,'c'),'stairs')