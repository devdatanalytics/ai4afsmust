import os
import pandas as pd
#test = ['tempofecal_copy']
test = ['healthy']
# replace test in for loop with os.listdir('rawImg') for full image renaming
for dirname in test:
    if os.path.isdir('rawImage/' + dirname):
        oldnames = []
        for i, f in enumerate(os.listdir('rawImage/' + dirname)):
            f_name, f_ext = os.path.splitext(f)
            new_name = dirname + str(i) + f_ext
            oldnames.append([new_name, f_name])
            os.rename('rawImage/' + dirname + '/' + f, 'rawImage/healthy/' + new_name)

        df = pd.DataFrame(oldnames)
        df.columns = ['new_filename', 'old_filename']
        df.to_csv('filenames.csv',index=False)   #first run
        #imgdf.to_csv('filenames.csv',mode='a',header=False,index=False) #appending if not all files were renamed