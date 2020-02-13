

import pysam
from collections import defaultdict


files=["/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130241-T.bwa.sorted.connor.bam",
"/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130244-T.bwa.sorted.connor.bam",
"/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130248-T.bwa.sorted.connor.bam"]
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130248-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130250-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130250-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130309-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130313-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130313-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130321-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130322-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130326-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130327-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130332-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130339-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130339-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130340-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130341-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130341-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130344-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130344-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130346-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130349-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130376-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130376-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130381-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130381-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130382-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130382-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130383-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130383-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130385-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130385-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130406-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130414-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130414-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130416-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130417-T.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130417-TP.bwa.sorted.connor.bam",
# "/scratch/uc23/hfettke/cfDNA_BAMs_41/post_connor/130463-T.bwa.sorted.connor.bam"]


final={}
file_short_list = []

for file in files:
    #file_short = file.split("/")
    #file_short_list.append(file_short[5])
    samfile = pysam.AlignmentFile(file, "rb")
    tags = []

    for line in samfile.fetch():
        t = line.get_tag("X5")
        tags.append(t)

    counts = dict()
    for i in range(1000):
       counts[i] = 0


    for i in tags:
        counts[i] = counts.get(i, 0) + 1

    for x, y in counts.iteritems():
        if x in final:
            final[x].update({file: y/2})
        else:
            final.update({x:{file: y/2}})

print final
 

#with open('temp.txt', 'w') as outf:
#    for key, value in final.items():
#        outf.write(str(key) + "\t")
#        for key2 in value:
#            if final[key][key2] >= 1:
#                outf.write(str(final[key][key2]) + "\t")
#            else:
#                outf.write("0" + "\t")
#        outf.write("\n")


with open('temp.txt', 'w') as outf:
    for key, value in final.items():
        for key2 in value:
            outf.write(str(value) + "\t")
        outf.write("\n")


#for list_item in file_short_list:
#    for key, value in final.items():
#        print final[key][list_item]




 





