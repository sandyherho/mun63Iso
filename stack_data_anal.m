clear all; close; clc

tg01c = readtable("./raw_data/cleantg01c.csv");
tg11a = readtable("./raw_data/cleantg11a.csv");
mun63 = readtable("./raw_data/cleanmun63.csv");

max_date = [max(floor(tg01c.date)), max(floor(tg11a.date)), max(floor(mun63.date))];
min_date = [min(floor(tg01c.date)), min(floor(tg11a.date)), min(floor(mun63.date))];

t = min(min_date):max(max_date);

anom_tg01c = anomal(tg01c, t);
anom_tg11a = anomal(tg11a, t);
anom_mun63 = anomal(mun63, t);
%[t' anom_tg01c];

low_pass_tg01c = lowpassAnom(anom_tg01c);
low_pass_tg11a = lowpassAnom(anom_tg11a);
low_pass_mun63 = lowpassAnom(anom_mun63);

lp = [low_pass_tg01c low_pass_tg11a low_pass_mun63];

% percentile calc.
pc=[2.5 50 97.5];
ci95 = prctile(lp, pc, 2);
final_ts = array2table([t' ci95]);
final_ts.Properties.VariableNames(1:4) = {'year','lower','median', 'upper'};
writetable(final_ts,'./processed_data/muna_low_pass_stack.csv');