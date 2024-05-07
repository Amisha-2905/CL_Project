
## CL Project

### Training Data
-It has 60 files of 50 sentences each which are annotated.The data from the files was scraped by scrape.py and the output for the same was staored in train.txt.
-It also has a dataset of nearly 500 sentences that is manually annotated for model training. This data is from the same domain as train.txt.

Finally, the whole training data is in final_train.txt which has all the training data from tourism domain with around 60,000 tokens.

### Test Data
-Test data has 4 text files of different domain with nearly 50 sentences each.
These files are manually annotated and saved in the folder 'annotated_files'.

### CRF model training
CRF model was run based on template.txt which considers two words before and after the current word.
It was trained using final_train.txt .
The trained model was run on the annotated files and Precision, Recall and F1 Score were calculated and stored in analysis_output.txt 

### Unicode to WX and WX to Unicode
So the code to convert Unicode from WX and from WX to Unicode is stored in uniwx.py and wxuni.py respectively.
The functions take a single word as input without any spaces or symbol and give a single word as output.

### Final_code
The overall model is run through final.py.
When the code is run, It asks if you want to enter the sentence in Hindi Unicode or WX notation.
If WX is selected, the sentence gets converted into unicode and then processed.
The final Hindi sentence (either the initial input or converted from WX) is tokenized and stored in tokens.txt .
The trained CRF model is then run on tokens.txt whose output is displayed on terminal and saved in output.txt.
This is how our POS tagger works.
Now, our code extracts the tokens which are tagged as either V_VM or V_VAUX and passes the verbs one by one into final_main function in wxuniwx.py that works as morph analyzer using lttoolbox.
The final_main function takes hindi word as input which is a verb, converts it into WX, passes the WX notation word through lttoolbox,gets the output in WX, converts the WX output to unicode and finally returns the analysis of verb.
The morph-analysis is also written in the output.txt.

The further analysis of the crf model is written in analysis.txt .

## List of tasks and respective contributions:
-> Data scraping of train data (Amisha)
-> Tokenization of manually annotated data and test data (Aaryan)
-> Annotation of 500 sentences training data (Amisha)
-> Annotation of 4 * 50 sentences test data (Both)
-> Training and running the CRF model on test data (Amisha)
-> POS tagger and analysis (Amisha)
-> WX to hindi unicode and hindi unicode to WX converter (Aaryan)
-> Dictionary of morph analyser (Both)
-> Pipelining of the whole model (Aaryan)

