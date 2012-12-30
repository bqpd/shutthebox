clear all
%%
h = [29, 267, 1319, 4234, 9152, 14705, 18739, 18874, 15738, 10246, 5295, 1402, 0];
xx = [0:.1:12];
yy = spline([0:12],h/1e5,xx);
%%
figure(1); clf;
ylim([0 .2])
xlabel('tabs remainining at game end')
ylabel('probability')
hold on
%%
plot(xx,yy,'k')
for i = 1:length(xx)
    x = xx(i);
    y = yy(i);   
    plot([x,x],[0,y],'k','LineWidth',0.25)
end
%%
figure(1); clf;
ylim([0 .2])
xlabel('tabs remainining at game end')
ylabel('probability')
hold on
for i = 1:length(h)
    x = i-1;
    y = h(i)/1e5;   
    plot([x,x],[-.1,y],'k.-',...
     -0.5+[x,x],[-.1,q(i)/36],'b.--','LineWidth',0.5,'MarkerSize',20)
end
hold off
%%
a = [1 2 3 4 5 6;
     2 3 4 5 6 1;
     3 4 5 6 1 2;
     4 5 6 1 2 3;
     5 6 1 2 3 4;
     6 1 2 3 4 5];
b = a' + [1:6]'*ones(1,6);
q = [-.1,-.1];
for i = 2:12
    q(i+1) = length(find(b==i));
end
plot(q)