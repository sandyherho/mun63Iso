function [filtered_anom] = lowpassAnom(anom_data)
    for ii = 1:size(anom_data,2)
        [e,ln,A,rc,check] = fssa(anom_data(:,ii), 7);
        filtered_anom(:,ii) = sum(rc(2:7,:),1)';
        clear e ln A rc check
    end
end