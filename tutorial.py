"""
    Make sure you have installed the requirements, the trdg took a while when downloading ...
"""
# STEP 1: IMPORTS
import os

## The text Recognition Data Generator
from trdg.generators import GeneratorFromStrings

## The reverse fix for arabic text
from arabic_reshaper import ArabicReshaper
from bidi.algorithm import get_display

## reading the data
import csv

# STEP 2: READ DATA
# Our data is stored in a csv file, lets create a function that returns the data we need!
# We could have used pandas but I felt its not worth installing this package just to extract data into strings XD
def get_strings_from_csv(path):
    """
        path: string, the data.csv filename
        returns array of strings
    """
    strings = [] # Store the data inside this array

    with open(path, encoding='utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = True

        for row in csv_reader:
            if header: # This is the column names [Name, Gender]
                header = False
                continue

            # row contains (name, gender), we only care about the name [0]
            strings.append(row[0])
    
    return strings
            

# STEP 3: USE TRDG
def ar_generate_data(strings, fonts, size=32, limit=100, image_dir='images/', output_dir='synth_sample/'):
    """
        strings: array -> text(label) to generate
        size: int -> size of the text
        limit: int -> # of text images we want to generate
        image_dir -> image_dir with background images we want to use 
        output_dir -> where to store the images
    """
    # Lets reshape the strings first
    arabic_reshaper = ArabicReshaper()
    reshaped_strings = [get_display(arabic_reshaper.reshape(str(w))) for w in strings]

    # then lets use trgd
    generator = GeneratorFromStrings(

        # If you visit the trdg repo and read the GeneratorFromStrings.py -
        # you'll find a lot more args to pass in. I do recommend checking out other parameters
        # when passing language to 'ar' trgd by default uses fonts specifically 
        # for arabic language but in the current Pypi still not reflected, 
        # but you can pass your own using 'fonts' which accpets an array .
        
        reshaped_strings,
        language= 'ar',
        fonts=fonts,
        size=size, # the default size is a bit too small (my opinion)
        background_type=3, # 3 is for images, trgd will use the default but we will specify our own image_dir
        image_dir = image_dir,
    )
    

    # When generating an images we want to save the image inside
    # a directory + save results to a .txt file that has path/to/img.jpg and label
    generated_labels = [] # this array contains a tuple (path_to_image, label)

    # looping over the generators results
    for (img, label) in generator:
        if limit <= 0:
            break

        # name 1000.jpg, 999.jpg, 998.jpg ... 1.jpg
        name = str(limit)+ ".jpg"

        path_to_image = os.path.join(output_dir, name)
        img.save(path_to_image) # save to output_dir/name
        
        # to store the label name in its correct arabic format 
        label = get_display(arabic_reshaper.reshape(str(label)))
        generated_labels.append((path_to_image, label))

        limit -= 1
    
    # now lets store the generated labels to a txt file
    file_name = 'labels.txt'
    save_txt(generated_labels, output_dir, file_name)


# STEP 4: STORE RESULTS
def save_txt(strings, path, file_name):
    label_file = open(os.path.join(path, file_name), 'w', encoding='utf8')
    
    for l in strings: 
        line = '\t'.join(l)
        label_file.write(line)
        label_file.write('\n')


# STEP 5: RUN
if __name__ == '__main__':
    path_to_csv = 'Arabic_names.csv'
    dir_to_fonts = 'fonts/'

    strings = get_strings_from_csv(path_to_csv)

    # get all fonts in dir
    fonts_in_dir = os.listdir(dir_to_fonts)
    
    fonts = [] # to append the name of dir to font name
    for font in fonts_in_dir:
        fonts.append(dir_to_fonts + font)

    # fonts =['fonts/Amiri-Regular.ttf'] <- if you only have one font

    ar_generate_data(strings, fonts, size=64, limit=10)