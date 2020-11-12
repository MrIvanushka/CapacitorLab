settings = importdata("settings.txt");
data = importdata("data.txt");

dV = settings(1);
dT = settings(2);
U = data*dV;
T = (1:length(data))*dT;
[m, i] = max(data);
TCharge = dT*i;
figure('name','Budkin Ivan B03-006')
plot(T,U,'--o','MarkerIndices',1:(20+randi(10)):length(U),'LineWidth',2,'MarkerSize',3,'Color',[rand(1),rand(1),rand(1)]);
grid on;
title({'CAPACITOR',['time of Charging = ', num2str(TCharge), 's'],['time of Dischargitrng = ', num2str(T(length(T))-TCharge), 's']});
text(max(T)*0.55,max(U)*0.6,{['Time of Charging = ', num2str(TCharge), 's'],['Time of Dischargitrng = ', num2str(T(length(T))-TCharge), 's']},'BackgroundColor','w');
xlabel('Time, s');
ylabel('Voltage, V');
legend('charging');
saveas(gca,'C:\Users\ivanb\OneDrive\Рабочий стол\Budkin\Capacitor\capacitor.svg');
