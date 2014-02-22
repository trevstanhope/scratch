import sys, datetime, numpy, ast
dataset = sys.argv[1]

class Clean:

  def strip(self, filename):
    output = 'clean_' + filename
    with open(filename, 'r') as dataset:
      with open(output, 'w') as clean_dataset:
        for row in dataset:
          row_list = row.split(',')
          if (row_list[1] == '') or (row_list[5] == '\n'):
            pass
          else:
          
            # extract stuff
            date_string = row_list.pop(0)
            energy = int(ast.literal_eval(row_list.pop(4)))
            
            # hack stuff
            date_object = datetime.datetime.strptime(date_string[:-6], '%Y-%m-%dT%H:%M')
            row_list.append(str(date_object.isoweekday()))
            row_list.append(str(date_object.month))
            row_list.append(str(date_object.hour))
                     
            # finalize stuff
            row_list.append(str(energy) + '\n')
            clean_dataset.write(','.join(row_list))
  
if __name__ == '__main__':
  root = Clean()
  clean_dataset = root.strip(dataset)
