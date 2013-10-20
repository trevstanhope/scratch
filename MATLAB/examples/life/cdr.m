% CDR.M
% Group 10: Nada Khan, Rodger Liu, Trevor Stanhope, Mei Xiao
% Returns the last page of a dim3 matrix

function last = cdr(list)
  [i,j,k] = size(list)
  last = list(:,:,k)
end
