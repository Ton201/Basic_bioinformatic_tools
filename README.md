In this repo, you will find code files that solve commod tasks when working with DNA and protein sequences.

-    reformat\_DNA/reformat_AA: Outputs a universal header ">output" first. The sys library is used to read the input line by line. Each line is then filtered so that only letters are sent to the output.

-    reverse\_complement_DNA: Lines are again read from the input using the sys library. A reverse function is written to reverse the lines and ensure output in the 5' -> 3' direction. The letters in each line are then translated in a loop mapped to a translation dictionary.

-    statistic\_DNA: This file loads the entire input file. It then calculates the frequency of each letter, the sequence length, and its MD5 hash.

-    get\_region: This file extracts a segment from the sequence according to provided arguments. Unlike Python indexing, it starts from 1 and includes both boundaries.

-    translate: This file reads the sequence and prepares three sets of triplets. This is necessary because we don’t know the starting position of the translation. These sets are then translated according to the genetic code.